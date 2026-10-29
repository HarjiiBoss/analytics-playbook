#!/usr/bin/env python3
"""
check_notebooks.py

Checks Jupyter notebooks against the playbook's Code standards (Part V → Quality Assurance → Code;
Reproducibility Standard). Two modes:

  Static (default, fast, used by the pre-commit hook). For each notebook, reports:
    - empty code cells
    - code cells that were never run, while other cells in the notebook were
    - cells run out of order (execution counts not increasing top to bottom), which means the
      saved outputs did not come from one top-to-bottom run
    - error outputs (a traceback saved in the notebook)
    - absolute local paths in code (/Users/..., /home/..., C:\\Users\\...), which break on any
      other machine and expose your folder names

  --execute (slow, run by hand at the end of each phase). Runs every notebook from a fresh
    kernel, top to bottom, on an in-memory copy, and reports the first cell that fails.
    The notebooks on disk are not changed. Notebooks that query a paid or rate-limited service
    (BigQuery, an API) cost the same as running them yourself.

Examples:
  python3 tools/check_notebooks.py                       # every notebook under notebooks/
  python3 tools/check_notebooks.py notebooks/01_data_loading.ipynb
  python3 tools/check_notebooks.py --execute             # end of phase

Exit code 0 when every notebook passes, 1 otherwise, so it can run as a pre-commit hook.
Notebook outputs are evidence for check_figures.py, so this tool never strips them.
"""

import argparse
import json
import re
import sys
from pathlib import Path

# Absolute paths that only exist on one machine. Matched in code cells only.
LOCAL_PATH = re.compile(r"""(["'])(/Users/|/home/|[A-Za-z]:\\\\Users\\\\)""")


def code_cells(nb):
    """(position, cell) for every code cell, numbered from 1 as Jupyter shows them."""
    return [(i, c) for i, c in enumerate(nb.get("cells", []), start=1) if c.get("cell_type") == "code"]


def static_problems(path):
    """Return a list of problem strings for one notebook. Reads the JSON only; runs nothing."""
    try:
        nb = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return ["cannot be read as a notebook: " + str(exc)]

    problems = []
    cells = code_cells(nb)
    run_counts = [c.get("execution_count") for _, c in cells if "".join(c.get("source", [])).strip()]
    any_run = any(n is not None for n in run_counts)

    last = 0
    for pos, cell in cells:
        source = "".join(cell.get("source", []))
        count = cell.get("execution_count")
        if not source.strip():
            problems.append(f"cell {pos}: empty code cell (delete it)")
            continue
        if any_run and count is None:
            problems.append(f"cell {pos}: never run, but other cells were (restart and run all)")
        elif count is not None:
            if count <= last:
                problems.append(f"cell {pos}: run out of order (count {count} after {last}); "
                                f"restart the kernel and run all")
            last = count
        for out in cell.get("outputs", []):
            if out.get("output_type") == "error":
                problems.append(f"cell {pos}: saved error output ({out.get('ename', 'error')})")
        for line_no, line in enumerate(source.splitlines(), start=1):
            if LOCAL_PATH.search(line):
                problems.append(f"cell {pos}, line {line_no}: absolute local path; "
                                f"build it from the project root instead")
    return problems


def execute_problem(path, timeout):
    """Run the notebook from a fresh kernel in a temporary copy. Return None or a problem string."""
    try:
        import nbformat
        from nbclient import NotebookClient
        from nbclient.exceptions import CellExecutionError
    except ImportError:
        sys.exit("--execute needs nbclient and nbformat: pip install nbclient nbformat ipykernel")

    nb = nbformat.read(str(path), as_version=4)
    # Run with notebooks/ as the working folder, as Jupyter would, so relative paths behave the same.
    client = NotebookClient(nb, timeout=timeout, kernel_name="python3",
                            resources={"metadata": {"path": str(Path(path).parent)}})
    try:
        client.execute()
    except CellExecutionError as exc:
        # Remove terminal colour codes from the traceback so the message prints cleanly.
        text = re.sub(r"\x1b\[[0-9;]*m", "", str(exc)).strip()
        first_line = text.splitlines()[-1] if text else "error"
        return "fails when run from a fresh kernel: " + first_line
    # The executed copy lives only in memory and is discarded, so the file on disk is unchanged.
    return None


def main():
    p = argparse.ArgumentParser(description="Check notebooks against the playbook's Code standards.")
    p.add_argument("notebooks", nargs="*", help="Notebook files. Default: every .ipynb under notebooks/")
    p.add_argument("--execute", action="store_true", help="Also run each notebook from a fresh kernel")
    p.add_argument("--timeout", type=int, default=600, help="Seconds allowed per cell with --execute")
    args = p.parse_args()

    paths = [Path(n) for n in args.notebooks] or sorted(Path("notebooks").rglob("*.ipynb"))
    paths = [n for n in paths if ".ipynb_checkpoints" not in n.parts]
    if not paths:
        print("No notebooks found.")
        return 0

    failed = 0
    for path in paths:
        problems = static_problems(path)
        if args.execute and not problems:
            problem = execute_problem(path, args.timeout)
            if problem:
                problems.append(problem)
        if problems:
            failed += 1
            print(f"{path}")
            for problem in problems:
                print("  - " + problem)
        else:
            print(f"{path}: OK" + (" (ran from a fresh kernel)" if args.execute else ""))

    print(f"\n{len(paths)} notebook(s) checked, {failed} with problems.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
