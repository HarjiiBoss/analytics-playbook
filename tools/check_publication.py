#!/usr/bin/env python3
"""
check_publication.py

Checks a project before its repository goes public (Playbook Part V → Public and Private
Content). Run it from the project root at the end of Phase 5, after check_figures.py:

    python3 tools/check_publication.py

It reads only files Git tracks (so ignored data and private files are skipped) and reports:

  1. Template comments left in Markdown (<!-- ... -->). They do not show on GitHub's page but
     do show in the raw file, and they are written for the author, not the reader.
  2. Template placeholders: {{NAME}}, "To be defined in Phase ...", "[Project subtitle]",
     "[Dataset name...", "[Method, rule or definition]", and table rows with no content.
  3. Absolute local paths (/Users/..., /home/..., C:\\Users\\...) in any tracked text file,
     including notebook outputs and Tableau workbooks. They expose folder and user names and
     break on any other machine.
  4. Private notes committed by mistake (learning_notes*.md). Those belong in the private
     financial-model-foundation repository.

Exit code 0 when nothing is found, 1 otherwise. It is not a commit hook: comments and
placeholders are expected while the project is in progress.
"""

import re
import subprocess
import sys
from pathlib import Path

COMMENT = re.compile(r"<!--.*?-->", re.S)
PLACEHOLDERS = [
    re.compile(r"\{\{[A-Z_]+\}\}"),
    re.compile(r"To be defined in Phase \d"),
    re.compile(r"\[(Project subtitle|Dataset name[^\]]*|Method, rule or definition|One paragraph[^\]]*)\]"),
]
EMPTY_ROW = re.compile(r"^\|(\s*\|)+\s*$", re.M)          # | | | with nothing in any cell
LOCAL_PATH = re.compile(r"(/Users/[^/\s\"']+|/home/[^/\s\"']+|[A-Za-z]:\\\\?Users\\\\?[^\\\s\"']+)")
PRIVATE = re.compile(r"(^|/)learning_notes[^/]*\.md$")
TEXT_SUFFIXES = {".md", ".ipynb", ".py", ".sql", ".txt", ".csv", ".json", ".html", ".twb", ".yaml", ".yml", ".toml", ".cfg"}
SKIP = {"tools/check_publication.py"}  # this file contains the patterns it looks for
SKIP_DIRS = (".github/", "tools/")      # PR template comments are prompts on purpose; tools/ holds the checks themselves, whose patterns would match


def tracked_files():
    out = subprocess.run(["git", "ls-files"], capture_output=True, text=True)
    if out.returncode != 0:
        sys.exit("Run from the project root, inside the Git repository.")
    return [Path(p) for p in out.stdout.splitlines()]


def line_of(text, index):
    return text.count("\n", 0, index) + 1


def main():
    problems = []
    for path in tracked_files():
        name = path.as_posix()
        if name in SKIP or name.startswith(SKIP_DIRS):
            continue
        if PRIVATE.search(name):
            problems.append(f"{name}: private learning notes; remove with `git rm --cached` and keep them in financial-model-foundation")
            continue
        if path.suffix.lower() not in TEXT_SUFFIXES or not path.is_file():
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue

        if path.suffix.lower() == ".md":
            for m in COMMENT.finditer(text):
                snippet = " ".join(m.group(0).split())[:70]
                problems.append(f"{name}:{line_of(text, m.start())}: template comment: {snippet}")
            for rx in PLACEHOLDERS:
                for m in rx.finditer(text):
                    problems.append(f"{name}:{line_of(text, m.start())}: placeholder: {m.group(0)}")
            for m in EMPTY_ROW.finditer(text):
                problems.append(f"{name}:{line_of(text, m.start())}: empty table row")

        for m in LOCAL_PATH.finditer(text):
            problems.append(f"{name}:{line_of(text, m.start())}: absolute local path: {m.group(0)}")

    if problems:
        print(f"{len(problems)} item(s) to fix before publishing:\n")
        for p in problems:
            print("  - " + p)
        return 1
    print("Ready to publish: no template comments, placeholders, local paths or private notes found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
