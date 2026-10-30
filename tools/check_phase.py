#!/usr/bin/env python3
"""
check_phase.py

Runs every check that is due at the end of a phase (Playbook Part V → Automated Checks),
so there is one command to remember instead of four. Run it from the project root, the
folder that holds README.md, PROJECT_INFO.md and tools/:

    python3 tools/check_phase.py 0        # end of Phase 0, before its pull request
    python3 tools/check_phase.py 2        # end of Phase 2
    python3 tools/check_phase.py 5        # end of Phase 5, before the repository goes public
    python3 tools/check_phase.py --list   # show what each phase runs, change nothing

What it runs:

    Phase  Checks
    0      Git state, pre-commit hooks installed, every pre-commit hook on every file
    1-4    The Phase 0 checks, then every notebook run from a fresh kernel
    5      The Phase 1-4 checks, then figures in text and the publication check

It also lists any unticked boxes left in the phase document's Exit Checklist. Those are a
reminder, not a failure: some boxes do not apply to every project (an experiments-only
rule in an observational project, for example), and only you can decide that.

The fresh-kernel run re-executes every notebook. If a notebook queries a paid or
rate-limited service (BigQuery, an API), that costs the same as running it yourself;
use --no-execute to skip it and run the notebooks yourself from a restarted kernel.

Exit code 0 when every check passes, 1 otherwise. Nothing in the project is changed.
"""

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

PHASE_DOCS = {
    0: "docs/phase_00_setup.md",
    1: "docs/phase_01_data_preparation.md",
    2: "docs/phase_02_business_analysis.md",
    3: "docs/phase_03_method_selection.md",
    4: "docs/phase_04_advanced_analysis.md",
    5: "docs/phase_05_reporting.md",
}

# What each check is for and what to do when it fails, printed with the result so the
# fix does not have to be looked up.
FIXES = {
    "git": "Work on a phase branch, not main: git checkout -b phase-N-description",
    "hooks": "Install the hooks once in this clone: pip install pre-commit && pre-commit install",
    "pre-commit": "Read the hook output above, fix the file it names, then run this check again.",
    "notebooks": "Open the notebook named above, fix the failing cell, restart the kernel, "
                 "run all cells, save, and run this check again.",
    "figures": "For each figure listed: correct the text from the output, or, if it is derived "
               "and checked by hand, add it to .figures-allow with its calculation.",
    "publication": "Remove each item listed: template comments, placeholders, local paths "
                   "or private notes.",
}


def run(cmd, label):
    """Run one check as a subprocess, show its output as it happens, return True on success."""
    print("\n" + "-" * 70)
    print(label)
    print("$ " + " ".join(cmd))
    print("-" * 70, flush=True)
    return subprocess.run(cmd).returncode == 0


def check_git(root):
    """The project must be a Git repository, and work must not happen on main."""
    print("\n" + "-" * 70)
    print("Git state")
    print("-" * 70)
    if not (root / ".git").exists():
        print("Not a Git repository.")
        return False
    branch = subprocess.run(["git", "branch", "--show-current"], capture_output=True,
                            text=True, cwd=root).stdout.strip()
    changes = subprocess.run(["git", "status", "--short"], capture_output=True,
                             text=True, cwd=root).stdout.strip()
    print("Branch: " + (branch or "(detached)"))
    if changes:
        # Uncommitted work is normal at this point; listing it shows what the next
        # commit will contain, so nothing unexpected (data, scratch files) slips in.
        print("Uncommitted changes (review before git add; stage files by name):")
        for line in changes.splitlines():
            print("  " + line)
    else:
        print("No uncommitted changes.")
    if branch in ("main", "master"):
        print("You are on " + branch + ". Phase work belongs on its own branch.")
        return False
    return True


def check_hooks(root):
    """pre-commit must be installed on this machine and its hook installed in this clone."""
    print("\n" + "-" * 70)
    print("Pre-commit hooks installed")
    print("-" * 70)
    if shutil.which("pre-commit") is None:
        print("The pre-commit command is not installed.")
        return False
    hook = root / ".git" / "hooks" / "pre-commit"
    if not hook.is_file() or "pre-commit" not in hook.read_text(errors="ignore"):
        print("pre-commit is installed, but not in this clone (.git/hooks/pre-commit missing).")
        return False
    print("Installed.")
    return True


def unticked_boxes(root, phase):
    """Return the unticked lines under '# Exit Checklist' in the phase document."""
    doc = root / PHASE_DOCS[phase]
    if not doc.is_file():
        return None
    text = doc.read_text(encoding="utf-8")
    match = re.search(r"^# Exit Checklist\s*$(.*?)(?=^# |\Z)", text, re.M | re.S)
    if not match:
        return []
    return [line.strip() for line in match.group(1).splitlines()
            if re.match(r"\s*- \[ \]", line)]


def plan(phase, execute):
    """The ordered list of (key, label) checks for a phase."""
    steps = [("git", "Git state"), ("hooks", "Pre-commit hooks installed"),
             ("pre-commit", "All pre-commit hooks on every file")]
    if phase >= 1:
        steps.append(("notebooks", "Notebooks run from a fresh kernel"
                      + ("" if execute else " (skipped: --no-execute)")))
    if phase == 5:
        steps.append(("figures", "Figures in text found in the outputs"))
        steps.append(("publication", "Ready to publish"))
    return steps


def main():
    p = argparse.ArgumentParser(description="Run the checks due at the end of a playbook phase.")
    p.add_argument("phase", nargs="?", type=int, choices=range(6), help="Phase just finished, 0 to 5")
    p.add_argument("--no-execute", action="store_true",
                   help="Skip the fresh-kernel notebook run (paid or rate-limited queries)")
    p.add_argument("--list", action="store_true", help="Show what each phase runs, then stop")
    args = p.parse_args()

    if args.list or args.phase is None:
        for ph in range(6):
            print("Phase " + str(ph) + ": " + "; ".join(label for _, label in plan(ph, True)))
        if args.phase is None and not args.list:
            print("\nGive the phase you just finished, e.g.: python3 tools/check_phase.py 2")
        return 0

    root = Path.cwd()
    tools = root / "tools"
    if not (root / "PROJECT_INFO.md").is_file() or not tools.is_dir():
        sys.exit("Run this from the project root (the folder with PROJECT_INFO.md and tools/), "
                 "e.g.: cd ~/projects/<project-name>")

    py = sys.executable   # the Python running this script, so the project's .venv is used
    results = []
    for key, label in plan(args.phase, not args.no_execute):
        if key == "git":
            ok = check_git(root)
        elif key == "hooks":
            ok = check_hooks(root)
        elif key == "pre-commit":
            ok = shutil.which("pre-commit") is not None and run(
                ["pre-commit", "run", "--all-files"], label)
        elif key == "notebooks":
            if args.no_execute:
                results.append((label, None, key))
                continue
            ok = run([py, str(tools / "check_notebooks.py"), "--execute"], label)
        elif key == "figures":
            ok = run([py, str(tools / "check_figures.py"), "."], label)
        elif key == "publication":
            tool = tools / "check_publication.py"
            if not tool.is_file():
                print("\ntools/check_publication.py is missing. Copy it from the playbook: "
                      "cp ~/analytics-playbook/tools/check_publication.py tools/")
                ok = False
            else:
                ok = run([py, str(tool)], label)
        results.append((label, ok, key))

    # Summary: one line per check, then what to do about each failure.
    print("\n" + "=" * 70)
    print("Phase " + str(args.phase) + " checks")
    print("=" * 70)
    failed = []
    for item in results:
        label, ok = item[0], item[1]
        status = "SKIPPED" if ok is None else ("PASS" if ok else "FAIL")
        print(f"  {status:<8}{label}")
        if ok is False:
            failed.append(item[2])

    boxes = unticked_boxes(root, args.phase)
    if boxes is None:
        print("\n" + PHASE_DOCS[args.phase] + " not found; check its Exit Checklist by hand.")
    elif boxes:
        print("\nUnticked in the " + PHASE_DOCS[args.phase] + " Exit Checklist (tick each one, "
              "or note why it does not apply):")
        for b in boxes:
            print("  " + b)
    else:
        print("\nExit Checklist in " + PHASE_DOCS[args.phase] + ": every box ticked.")

    if failed:
        print("\nTo fix:")
        for key in failed:
            print("  - " + FIXES[key])
        return 1
    if boxes:
        print("\nAll checks passed. Deal with the unticked boxes above, then commit, push the "
              "branch and open the pull request.")
    else:
        print("\nAll checks passed. Commit, push the branch and open the pull request.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
