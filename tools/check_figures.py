#!/usr/bin/env python3
"""
check_figures.py

Checks that every number a reader sees in a project's write-up can be found in the
project's own outputs (Playbook v3.4, Single Source of Truth → Figures in Text).

What it does, in order:
  1. Reads the reader-facing text: README.md, docs/index.html and docs/executive_summary.md
     by default, or the files given with --text.
  2. Pulls out every significant number: decimals, percentages, money, values with K/M/x/pp,
     and whole numbers of three or more digits. Years (1900-2099) are skipped.
  3. Collects every number from the outputs: notebook outputs and code, SQL code, CSV, TXT,
     JSON and PDF files, and the numeric cells of Excel workbooks, anywhere in the project
     (PDFs need pypdf or pdftotext; workbooks need openpyxl). Not used as evidence: Markdown
     and HTML (they are the write-up being checked), SQL comments, notebook Markdown cells,
     numbers inside string literals, printed numbers that the printing cell typed in a string
     literal, and numbers typed inside text cells of a workbook (a label such as "Churn 26.54%").
  4. Reports each text number that no output value rounds to, with the sentence around it.

A number counts as found when an output value rounds to it at the same number of decimals,
directly or after a common change of unit: x100 for percentages written from fractions,
/1,000 for K and /1,000,000 for M. So 47.11% matches 0.4711, and $5.7M matches 5730573.28.

What it cannot do: it checks that a number exists in the outputs, not that it describes the
right thing. A correct number attached to the wrong group still passes, so the meaning of
each claim is still reviewed by eye. Derived figures (sums, ratios) are flagged even when
correct; once checked by hand, list them in a .figures-allow file (one number per line,
optional "# reason") and they are reported as allowed.

Examples:
  python3 tools/check_figures.py ~/cookie-cats-ab-test
  python3 tools/check_figures.py ~/logistics-analysis --text README.md docs/index.html
  python3 tools/check_figures.py ~/Telco_Customer_Churn_Analysis --max-csv-mb 50

Exit code 0 when every number is found or allowed, 1 when any is unmatched, so the
check can run as a pre-commit hook or in CI.
"""

import argparse
import csv
import html
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

DEFAULT_TEXT = ["README.md", "docs/index.html", "docs/executive_summary.md"]
EVIDENCE_SUFFIXES = {".ipynb", ".sql", ".csv", ".txt", ".json", ".pdf", ".xlsx", ".xlsm"}
SIZE_LIMITED = {".csv", ".txt", ".json", ".xlsx", ".xlsm"}
SKIP_DIRS = {".git", ".ipynb_checkpoints", "__pycache__", ".venv", "venv", "node_modules", ".virtual_documents"}

# A number in text: optional currency, digits with optional thousands commas and decimals,
# optional unit. Unicode minus and en dash are treated as signs or range separators.
TEXT_NUMBER = re.compile(r"(?<![\w.])([£$€]?)(\d{1,3}(?:,\d{3})+|\d+)(\.\d+)?\s?(%|pp|[KMB]\b|×|x\b)?")
# A number in evidence files: plain digits, optional decimals and exponent
# Thousands commas are accepted only in groups of three, so "3875,1655,42.71" in a CSV row is
# read as three numbers, not one.
EVIDENCE_NUMBER = re.compile(r"(?<![\d.,])-?(?:\d{1,3}(?:,\d{3})+(?![\d])|\d+)(?:\.\d+)?(?:[eE][-+]?\d+)?")


def visible_text(path):
    """Text a reader sees: HTML with scripts, styles and tags removed; Markdown as is."""
    raw = path.read_text(encoding="utf-8", errors="ignore")
    if path.suffix.lower() in (".html", ".htm"):
        raw = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", raw, flags=re.S | re.I)
        raw = re.sub(r"<[^>]+>", " ", raw)
        raw = html.unescape(raw)
    else:
        raw = re.sub(r"```.*?```", " ", raw, flags=re.S)  # code blocks show commands, not findings
        raw = re.sub(r"\]\([^)]*\)", "]", raw)          # drop Markdown link targets
        raw = re.sub(r"!\[[^\]]*\]", " ", raw)          # drop image alt text markers
    raw = re.sub(r"https?://\S+", " ", raw)             # numbers inside URLs are not figures
    return re.sub(r"\s+", " ", raw)


STRING_LITERAL = re.compile(r'''("""|\'\'\'|"|\')(?:\\.|(?!\1).)*?\1''', re.S)


def strip_strings(code):
    """Code with string literals removed: a number typed inside quotes is text, not a result."""
    return STRING_LITERAL.sub(" ", code)


def typed_numbers(code):
    """Numbers written inside the string literals of a cell, e.g. a hand-typed finding."""
    typed = set()
    for lit in STRING_LITERAL.finditer(code):
        for token in EVIDENCE_NUMBER.findall(lit.group(0)):
            typed.add(token.replace(",", "").lstrip("-"))
    return typed


def notebook_text(path):
    """Code (without string literals) and computed outputs of a notebook.

    Markdown cells are excluded, and so is any printed number that is also typed in a string
    literal of the cell that printed it: that number was written by hand, not computed.
    """
    try:
        nb = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, UnicodeDecodeError):
        return ""
    parts = []
    for cell in nb.get("cells", []):
        if cell.get("cell_type") != "code":
            continue
        code = "".join(cell.get("source", ""))
        parts.append(strip_strings(code))
        typed = typed_numbers(code)
        for out in cell.get("outputs", []):
            data = out.get("data", {})
            shown = "".join(out.get("text", "")) + "\n" + "".join(data.get("text/plain", "")) + "\n" \
                + re.sub(r"<[^>]+>", " ", "".join(data.get("text/html", "")))
            if typed:
                shown = EVIDENCE_NUMBER.sub(
                    lambda m: " " if m.group(0).replace(",", "").lstrip("-") in typed else m.group(0), shown)
            parts.append(shown)
    return "\n".join(parts)


def pdf_text(path):
    """Text of a PDF result export, using pypdf or the pdftotext command if either is available."""
    try:
        from pypdf import PdfReader
        return "\n".join(page.extract_text() or "" for page in PdfReader(str(path)).pages)
    except ImportError:
        pass
    if shutil.which("pdftotext"):
        done = subprocess.run(["pdftotext", "-layout", str(path), "-"], capture_output=True, text=True)
        return done.stdout
    return None


def workbook_text(path):
    """Numbers held in the numeric cells of every sheet of an Excel workbook.

    Formula cells are read as the value Excel last calculated and saved (data_only=True), so a
    KPI built with =COUNTIF(...)/COUNTA(...) counts as computed evidence. Text cells are left
    out: a number typed into a label or a title is written by hand, like a string literal in a
    notebook. A formula with no saved value (a workbook written by a script and never opened
    in Excel) contributes nothing. Returns None when openpyxl is not installed.
    """
    try:
        from openpyxl import load_workbook
    except ImportError:
        return None
    try:
        wb = load_workbook(path, read_only=True, data_only=True)
    except Exception:            # a damaged or password-protected workbook is skipped, not fatal
        return ""
    numbers = []
    for sheet in wb.worksheets:
        for row in sheet.iter_rows(values_only=True):
            for cell in row:
                # bool is a subclass of int in Python, so TRUE/FALSE cells are excluded explicitly
                if isinstance(cell, (int, float)) and not isinstance(cell, bool):
                    numbers.append(repr(float(cell)))
    wb.close()
    return " ".join(numbers)


def sql_without_comments(text):
    """SQL code only: comments often hold typed insights, which are not evidence."""
    text = re.sub(r"/\*.*?\*/", " ", text, flags=re.S)
    return re.sub(r"--[^\n]*", " ", text)


def evidence_values(project, text_files, max_csv_mb):
    """Every number found in the project's outputs, as floats, plus the list of files read."""
    values, used, skipped = set(), [], []
    for path in sorted(project.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in EVIDENCE_SUFFIXES:
            continue
        if SKIP_DIRS & set(path.relative_to(project).parts) or path in text_files:
            continue
        if path.suffix.lower() in SIZE_LIMITED and path.stat().st_size > max_csv_mb * 1e6:
            skipped.append((path, f"larger than {max_csv_mb:g} MB"))
            continue
        suffix = path.suffix.lower()
        if suffix == ".ipynb":
            content = notebook_text(path)
        elif suffix == ".pdf":
            content = pdf_text(path)
            if content is None:
                skipped.append((path, "no PDF reader; run: pip install pypdf"))
                continue
        elif suffix in (".xlsx", ".xlsm"):
            content = workbook_text(path)
            if content is None:
                skipped.append((path, "no Excel reader; run: pip install openpyxl"))
                continue
        elif suffix == ".sql":
            content = sql_without_comments(path.read_text(encoding="utf-8", errors="ignore"))
        elif suffix == ".csv":
            # read cell by cell so the delimiter is never mistaken for a thousands separator
            with path.open(encoding="utf-8", errors="ignore", newline="") as f:
                content = "\n".join(" ".join(row) for row in csv.reader(f))
        else:
            content = path.read_text(encoding="utf-8", errors="ignore")
        for token in EVIDENCE_NUMBER.findall(content):
            try:
                values.add(abs(float(token.replace(",", ""))))
            except ValueError:
                pass
        used.append(path)
    return values, used, skipped


# Which unit conversions a text number may use, by its unit. Keeping these narrow stops a
# figure matching an unrelated output value at another scale.
SCALES = {"": ("x1",), "%": ("x1", "x100"), "pp": ("x1", "x100"), "K": ("k",), "M": ("m",), "B": ("b",),
          "×": ("x1",), "x": ("x1",)}
FACTORS = {"x1": 1, "x100": 100, "k": 1e-3, "m": 1e-6, "b": 1e-9}


def build_index(values):
    """Map (scale, decimals, rounded value) for each output value."""
    index = set()
    for v in values:
        for name, factor in FACTORS.items():
            scaled = v * factor
            for d in range(0, 5):
                index.add((name, d, round(scaled, d)))
    return index


def is_found(index, value, decimals, unit):
    scales = SCALES.get(unit or "", ("x1",))
    if not unit and decimals:
        scales = ("x1", "x100")   # a bare decimal is often a percentage written without "%"
    return any((s, decimals, round(value, decimals)) in index for s in scales)


def text_numbers(text):
    """(display string, value, decimals, unit, context) for each significant number in the text."""
    found = []
    for m in TEXT_NUMBER.finditer(text):
        currency, whole, frac, unit = m.group(1), m.group(2), m.group(3) or "", m.group(4)
        digits = whole.replace(",", "")
        if not (frac or unit or currency or len(digits) >= 3):
            continue                                    # small bare integers are rarely figures
        if not frac and not unit and not currency and 1900 <= int(digits) <= 2099:
            continue                                    # years
        value = float(digits + frac)
        decimals = len(frac) - 1 if frac else 0
        display = (currency + whole + frac + (unit or "")).strip()
        start, end = max(0, m.start() - 70), min(len(text), m.end() + 50)
        found.append((display, value, decimals, unit or "", "…" + text[start:end].strip() + "…"))
    return found


def read_allow(project):
    """Numbers already checked by hand, from .figures-allow (one per line, '# reason' optional)."""
    allow = {}
    path = project / ".figures-allow"
    if path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            number, _, reason = line.partition("#")
            if number.strip():
                allow[number.strip()] = reason.strip()
    return allow


def main():
    parser = argparse.ArgumentParser(description="Check that figures in a project's write-up appear in its outputs.")
    parser.add_argument("project", type=Path, help="Path to the project repository")
    parser.add_argument("--text", nargs="+", help="Reader-facing files to check, relative to the project (default: %(default)s)",
                        default=DEFAULT_TEXT)
    parser.add_argument("--max-csv-mb", type=float, default=20,
                        help="Skip CSV/TXT/JSON/Excel evidence files larger than this (default: 20)")
    parser.add_argument("--quiet", action="store_true", help="Print only the summary")
    args = parser.parse_args()

    project = args.project.expanduser().resolve()
    text_files = [project / t for t in args.text if (project / t).exists()]
    if not text_files:
        sys.exit(f"No text files found in {project} (looked for: {', '.join(args.text)})")

    values, used, skipped = evidence_values(project, set(text_files), args.max_csv_mb)
    if not used:
        sys.exit(f"No output files found in {project} to check against")
    index = build_index(values)
    allow = read_allow(project)

    unmatched, allowed, checked = [], [], 0
    for path in text_files:
        for display, value, decimals, unit, context in text_numbers(visible_text(path)):
            checked += 1
            if is_found(index, value, decimals, unit):
                continue
            key = (path.relative_to(project), display)
            target = allowed if display in allow or display.lstrip("£$€") in allow else unmatched
            if key not in {(r, d) for r, d, _ in target}:   # report each figure once per file
                target.append((key[0], display, context))

    print(f"Checked {checked} figures in {len(text_files)} file(s) against {len(used)} output file(s).")
    for path, why in skipped:
        print(f"  skipped ({why}): {path.relative_to(project)}")
    if allowed and not args.quiet:
        print(f"\nAllowed by .figures-allow ({len(allowed)}):")
        for rel, display, _ in allowed:
            print(f"  {rel}: {display}")
    if unmatched:
        print(f"\nNot found in any output ({len(unmatched)}):")
        if not args.quiet:
            for rel, display, context in unmatched:
                print(f"  {rel}: {display}\n      {context}")
        print("\nCheck each one against its source. Fix typed or drifted figures; list correct derived ones in .figures-allow.")
        sys.exit(1)
    print("\nEvery figure was found in the outputs.")


if __name__ == "__main__":
    main()
