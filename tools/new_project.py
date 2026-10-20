#!/usr/bin/env python3
"""
new_project.py

Creates a new analytics project that follows the Data Analysis Playbook (v3.2).

The tool lives in the analytics-playbook repository and reads the templates from
that repository's templates/ folder, so the playbook, the templates and the tool
are always the same version.

What it does, in order:
  1. Builds the folder structure from Part V (Repository Standards).
  2. Fills the templates with the project details and writes them into the project,
     including the first notebook with its header filled in.
  3. Initialises Git and makes the first commit on main.
  4. Creates the GitHub repository and pushes main (needs the GitHub CLI, `gh`, logged in).
  5. Switches to a phase-0-scoping branch, so no work happens on main (Branching Strategy).

Examples:
  python3 tools/new_project.py --dry-run --title "GA4 Ecommerce Funnel"
  python3 tools/new_project.py --title "GA4 Ecommerce Funnel" --industry "Ecommerce" \
      --domain "Web Analytics" --visibility private

Always run with --dry-run first. It prints everything it would do and changes nothing.
"""

import argparse
import datetime
import json
import re
import shlex
import shutil
import subprocess
import sys
from pathlib import Path

PLAYBOOK_VERSION = "3.2"
DEFAULT_AUTHOR = "Taofeek Salami"
FIRST_BRANCH = "phase-0-scoping"
COMMIT_MESSAGE = "docs: initialise project scaffold from Playbook v" + PLAYBOOK_VERSION
NOT_SET = "To be defined in Phase 0"

# The repository root is one folder above tools/, and the templates sit in templates/.
PLAYBOOK_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_TEMPLATES = PLAYBOOK_ROOT / "templates"

# Projects are created outside the playbook repository by default, so a project
# can never end up nested inside another Git repository.
DEFAULT_PARENT_DIR = Path.home() / "projects"

# Folders from the playbook's repository structure, plus assets/ and reports/
# which the README template lists.
FOLDERS = [
    "assets",
    "data/raw",
    "data/processed",
    "docs",
    "notebooks",
    "outputs",
    "reports",
    "sql",
    "tableau",
]

# Each entry: (accepted template file names, output path inside the project).
# Template names are matched ignoring upper/lower case, anywhere under templates/.
DOCUMENTS = [
    (["README_template.md"], "README.md"),
    (["PROJECT_INFO_template.md"], "PROJECT_INFO.md"),
    (["LICENSE", "LICENSE.md", "LICENSE.txt"], "LICENSE"),
    ([".gitignore", "gitignore"], ".gitignore"),
    ([".env.example", "env.example"], ".env.example"),
    (["requirements.txt"], "requirements.txt"),
    (["documentation_index_template.md"], "docs/documentation_index.md"),
    (["data_dictionary_template.md"], "docs/data_dictionary.md"),
    (["project_glossary_template.md"], "docs/project_glossary.md"),
    (["assumption_register_template.md"], "docs/assumption_register.md"),
    (["cleaning_log_template.md"], "docs/cleaning_log.md"),
    (["security_notes_template.md"], "docs/security_notes.md"),
    (["tableau_blueprint_template.md"], "docs/tableau_blueprint.md"),
    (["executive_summary_template.md"], "docs/executive_summary.md"),
    (["presentation_notes_template.md"], "docs/presentation_notes.md"),
    (["phase_00_setup_template.md"], "docs/phase_00_setup.md"),
    (["phase_01_data_preparation_template.md"], "docs/phase_01_data_preparation.md"),
    (["phase_02_business_analysis_template.md"], "docs/phase_02_business_analysis.md"),
    # The three templates below were written with the older numbering
    # (3 = method selection, 4 = modelling, 5 = reporting). The playbook uses
    # 2.5, 3 and 4, so these outputs get renumbered (see RENUMBER_OUTPUTS).
    (["phase_03_method_selection_template.md"], "docs/phase_025_method_selection.md"),
    (["phase_04_advanced_analysis_template.md"], "docs/phase_03_advanced_analysis.md"),
    (["phase_05_reporting_template.md"], "docs/phase_04_reporting.md"),
]

RENUMBER_OUTPUTS = {
    "docs/phase_025_method_selection.md",
    "docs/phase_03_advanced_analysis.md",
    "docs/phase_04_reporting.md",
}
PHASE_MAP = {"3": "2.5", "4": "3", "5": "4"}

# Renumbering only happens if the template still carries its old-style heading.
# Once a template is fixed, the script leaves its numbering alone.
OLD_HEADINGS = {
    "docs/phase_025_method_selection.md": "# Phase 3 — Analytical Method Selection",
    "docs/phase_03_advanced_analysis.md": "# Phase 04 —",
    "docs/phase_04_reporting.md": "# Phase 05 —",
}

# Values filled in later phases. Used only where a template asks for them.
LATER_VALUES = {
    "DASHBOARD_NAME": "To be defined in Phase 4",
    "AUDIENCE": "To be defined in Phase 4",
}

# SQL stubs built from sql_template.sql: (file, phase number, phase name, phase title, purpose)
SQL_STUBS = [
    ("00_setup.sql", "00", "setup",
     "Phase 0 - Scoping & Project Setup", "Create the database or dataset and any required tables."),
    ("01_data_preparation.sql", "01", "data_preparation",
     "Phase 1 - Data Loading, Cleaning & Exploration", "Profile, clean and validate the raw data."),
    ("02_business_analysis.sql", "02", "business_analysis",
     "Phase 2 - Business Analysis", "Answer the descriptive business questions."),
]

# Notebook stub built from notebook_template.ipynb: (file, phase title, purpose heading)
NOTEBOOK_STUB = ("01_data_loading.ipynb",
                 "1 — Data Loading, Cleaning & Exploration",
                 "Load Raw Data")


# ----------------------------------------------------------------------------
# Small helpers
# ----------------------------------------------------------------------------

def slugify(text):
    """'Cookie Cats A/B Test' -> 'cookie-cats-ab-test'"""
    text = re.sub(r"\ba/b\b", "ab", text, flags=re.IGNORECASE)
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def ask(label, given, default, interactive):
    """Use the command-line value if given, otherwise ask, otherwise fall back to the default."""
    if given:
        return given
    if not interactive:
        if default is None:
            sys.exit("Missing required value: " + label)
        return default
    suffix = " [" + default + "]" if default else ""
    answer = input(label + suffix + ": ").strip()
    if answer:
        return answer
    if default is None:
        sys.exit("Missing required value: " + label)
    return default


def render(text, values):
    """Replace every {{NAME}} with its value."""
    for key, value in values.items():
        text = text.replace("{{" + key + "}}", value)
    return text


def renumber_phases(text):
    """Old numbering -> current numbering, in a single pass so changes never chain."""
    return re.sub(
        r"\bPhase 0?([345])\b(?!\.\d)",
        lambda m: "Phase " + PHASE_MAP[m.group(1)],
        text,
    )


def index_templates(templates_dir):
    """Map lower-case file name -> path for every file under templates/, subfolders included.
    Stops if two files share a name, since the script could not tell which one to use."""
    found = {}
    for path in sorted(templates_dir.rglob("*")):
        if not path.is_file():
            continue
        key = path.name.lower()
        if key in found:
            sys.exit("Two templates share the name " + path.name + ":\n  " + str(found[key])
                     + "\n  " + str(path) + "\nRename or remove one.")
        found[key] = path
    return found


def find_template(index, accepted_names):
    for name in accepted_names:
        if name.lower() in index:
            return index[name.lower()]
    return None


def render_notebook(text, values):
    """Fill placeholders cell by cell, so a value containing quotes cannot break the JSON."""
    notebook = json.loads(text)
    for cell in notebook["cells"]:
        source = "".join(cell["source"])
        cell["source"] = render(source, values).splitlines(True)
    return json.dumps(notebook, indent=1, ensure_ascii=False) + "\n"


def run(cmd, cwd, dry_run):
    print("  $ " + shlex.join(cmd))
    if dry_run:
        return True
    result = subprocess.run(cmd, cwd=str(cwd), capture_output=True, text=True)
    if result.returncode != 0:
        message = result.stderr.strip() or result.stdout.strip()
        print("    FAILED: " + message)
        return False
    return True


def inside_git_repo(path):
    """True if path, or any folder above it, is already a Git repository."""
    for folder in [path] + list(path.parents):
        if (folder / ".git").exists():
            return folder
    return None


# ----------------------------------------------------------------------------
# Main steps
# ----------------------------------------------------------------------------

def parse_args():
    p = argparse.ArgumentParser(description="Scaffold a project from the Data Analysis Playbook.")
    p.add_argument("--title", help="Project title, e.g. 'Cookie Cats A/B Test'")
    p.add_argument("--slug", help="Repository name. Default: built from the title")
    p.add_argument("--industry")
    p.add_argument("--domain", help="Analytics domain, e.g. 'Product Analytics'")
    p.add_argument("--type", dest="project_type", help="Default: Portfolio Project")
    p.add_argument("--business-question")
    p.add_argument("--business-problem")
    p.add_argument("--author", default=DEFAULT_AUTHOR)
    p.add_argument("--templates", default=str(DEFAULT_TEMPLATES),
                   help="Folder holding the templates. Default: the playbook repository's templates/")
    p.add_argument("--parent-dir", default=str(DEFAULT_PARENT_DIR),
                   help="Where the project folder is created. Default: ~/projects")
    p.add_argument("--visibility", choices=["private", "public"], default="private",
                   help="GitHub repo visibility. Default: private")
    p.add_argument("--no-github", action="store_true", help="Skip creating the GitHub repository")
    p.add_argument("--extra-packages", default="",
                   help="Comma-separated extra packages for requirements.txt")
    p.add_argument("--dry-run", action="store_true", help="Show what would happen, change nothing")
    return p.parse_args()


def collect_details(args):
    interactive = sys.stdin.isatty()
    title = ask("Project title", args.title, None, interactive)
    slug = args.slug or slugify(title)
    return {
        "PROJECT_TITLE": title,
        "PROJECT_SLUG": slug,
        "INDUSTRY": ask("Industry", args.industry, NOT_SET, interactive),
        "DOMAIN": ask("Analytics domain", args.domain, NOT_SET, interactive),
        "PROJECT_TYPE": ask("Project type", args.project_type, "Portfolio Project", interactive),
        "BUSINESS_QUESTION": ask("Primary business question", args.business_question, NOT_SET, interactive),
        "BUSINESS_PROBLEM": ask("Business problem", args.business_problem, NOT_SET, interactive),
        "AUTHOR": args.author,
    }


def build_values(details):
    today = datetime.date.today().isoformat()
    values = dict(details)
    # The templates use both names for the same thing.
    values["ANALYTICS_DOMAIN"] = details["DOMAIN"]
    values["DATE_CREATED"] = today
    values["LAST_UPDATED"] = today
    values["DATE"] = today
    values["PLAYBOOK_VERSION"] = PLAYBOOK_VERSION
    values.update(LATER_VALUES)
    return values


def build_files(index, values, extra_packages, warnings):
    """Return {output path: file text}. Nothing is written here."""
    files = {}

    for names, output in DOCUMENTS:
        template = find_template(index, names)
        if template is None:
            warnings.append("No template found for " + output + " (looked for: " + ", ".join(names) + "). Skipped.")
            continue
        text = template.read_text(encoding="utf-8")
        if output in RENUMBER_OUTPUTS:
            if OLD_HEADINGS[output] in text:
                text = renumber_phases(text)
            else:
                warnings.append(output + ": template already uses the v" + PLAYBOOK_VERSION
                                + " numbering, so it was copied as it is.")
        files[output] = render(text, values)

    # Extra packages are added after the template's list, skipping any already there.
    if "requirements.txt" in files:
        listed = files["requirements.txt"].split()
        extras = [p.strip() for p in extra_packages.split(",") if p.strip() and p.strip() not in listed]
        if extras:
            files["requirements.txt"] = files["requirements.txt"].rstrip("\n") + "\n" + "\n".join(extras) + "\n"

    sql_template = find_template(index, ["sql_template.sql"])
    if sql_template is None:
        warnings.append("No sql_template.sql found. SQL stubs skipped.")
    else:
        for filename, number, name, title, purpose in SQL_STUBS:
            merged = dict(values)
            merged.update({"PHASE": title, "PHASE_NUMBER": number, "PHASE_NAME": name, "PURPOSE": purpose})
            files["sql/" + filename] = render(sql_template.read_text(encoding="utf-8"), merged)

    notebook_template = find_template(index, ["notebook_template.ipynb"])
    if notebook_template is None:
        warnings.append("No notebook_template.ipynb found. Notebook stub skipped.")
    else:
        filename, phase, purpose = NOTEBOOK_STUB
        merged = dict(values)
        merged.update({"NOTEBOOK_NAME": filename, "PHASE": phase, "NOTEBOOK_PURPOSE": purpose})
        files["notebooks/" + filename] = render_notebook(notebook_template.read_text(encoding="utf-8"), merged)

    for output, text in files.items():
        leftover = sorted(set(re.findall(r"\{\{[A-Z_]+\}\}", text)))
        if leftover:
            warnings.append(output + " still contains unfilled placeholders: " + ", ".join(leftover))
    return files


def write_project(project_dir, files, dry_run):
    print("\nFolders")
    for folder in FOLDERS:
        print("  " + folder + "/")
        if not dry_run:
            (project_dir / folder).mkdir(parents=True, exist_ok=True)

    print("\nFiles")
    for output in sorted(files):
        print("  " + output)
        if not dry_run:
            path = project_dir / output
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(files[output], encoding="utf-8")

    # Git ignores empty folders, so empty ones get a .gitkeep file.
    if not dry_run:
        for folder in FOLDERS:
            path = project_dir / folder
            if not any(path.iterdir()):
                (path / ".gitkeep").write_text("", encoding="utf-8")


def setup_git(project_dir, slug, title, args, warnings):
    dry_run = args.dry_run
    print("\nGit")
    if shutil.which("git") is None:
        warnings.append("Git is not installed. Skipped version control.")
        return
    run(["git", "init"], project_dir, dry_run)
    run(["git", "symbolic-ref", "HEAD", "refs/heads/main"], project_dir, dry_run)
    run(["git", "add", "-A"], project_dir, dry_run)
    if not run(["git", "commit", "-m", COMMIT_MESSAGE], project_dir, dry_run):
        warnings.append("The first commit failed. Check `git config user.name` and `user.email`.")
        return

    print("\nGitHub")
    if args.no_github:
        print("  Skipped (--no-github)")
    elif shutil.which("gh") is None:
        warnings.append("GitHub CLI (`gh`) not found, so no repository was created. "
                        "Install it (brew install gh), run `gh auth login`, then from the project folder: "
                        "gh repo create " + slug + " --" + args.visibility + " --source . --remote origin --push")
    else:
        ok = run(["gh", "auth", "status"], project_dir, dry_run)
        if ok:
            description = title + " - built with the Data Analysis Playbook v" + PLAYBOOK_VERSION
            ok = run(["gh", "repo", "create", slug, "--" + args.visibility, "--source", ".",
                      "--remote", "origin", "--push", "--description", description],
                     project_dir, dry_run)
        if not ok:
            warnings.append("GitHub step failed (reason shown above). The project and first commit exist locally. "
                            "After fixing it (usually `gh auth login`), run from the project folder: "
                            "gh repo create " + slug + " --" + args.visibility + " --source . --remote origin --push")

    print("\nBranch")
    run(["git", "checkout", "-b", FIRST_BRANCH], project_dir, dry_run)


def main():
    args = parse_args()
    templates_dir = Path(args.templates).expanduser()
    if not templates_dir.is_dir():
        sys.exit("Templates folder not found: " + str(templates_dir) + "\nUse --templates to point to it.")
    index = index_templates(templates_dir)

    details = collect_details(args)
    values = build_values(details)
    slug = values["PROJECT_SLUG"]
    parent_dir = Path(args.parent_dir).expanduser().resolve()
    project_dir = parent_dir / slug

    if project_dir.exists() and any(project_dir.iterdir()):
        sys.exit("Folder already exists and is not empty: " + str(project_dir))

    # A project inside another repository would be committed to that repository too.
    enclosing = inside_git_repo(parent_dir)
    if enclosing is not None:
        sys.exit("The parent folder is inside an existing Git repository: " + str(enclosing)
                 + "\nChoose a parent folder outside it with --parent-dir.")

    warnings = []
    print(("DRY RUN - nothing will be created\n" if args.dry_run else "") + "Project folder: " + str(project_dir))
    print("Templates: " + str(templates_dir))

    files = build_files(index, values, args.extra_packages, warnings)
    write_project(project_dir, files, args.dry_run)
    setup_git(project_dir, slug, values["PROJECT_TITLE"], args, warnings)

    print("\nSummary")
    print("  " + str(len(files)) + " files, " + str(len(FOLDERS)) + " folders")
    if warnings:
        print("\nWarnings")
        for w in warnings:
            print("  - " + w)
    print("\nNext steps")
    print("  1. cd " + str(project_dir))
    print("  2. python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt")
    print("  3. cp .env.example .env, then add the settings the project needs")
    print("  4. Complete PROJECT_INFO.md and docs/phase_00_setup.md")
    print("  5. When the Phase 0 exit checklist is done: push the " + FIRST_BRANCH
          + " branch and open a pull request into main")


if __name__ == "__main__":
    main()
