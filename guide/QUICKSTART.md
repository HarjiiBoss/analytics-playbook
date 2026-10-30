# Playbook Quick Start

How to use the playbook day to day: setting up, starting a project, and which check to run, when, and from which folder. The full standard is in [`playbook/DATA_ANALYSIS_PLAYBOOK.md`](../playbook/DATA_ANALYSIS_PLAYBOOK.md); this page only tells you what to type.

A Word copy of this page is in [`Playbook_Quick_Start.docx`](Playbook_Quick_Start.docx).

---

## 1. Where things live

| Folder | What it holds | Git |
|---|---|---|
| `~/analytics-playbook` | The playbook, templates and tools. New projects are created from here | Public repository |
| `~/projects/<project-name>` | Each project made by `new_project.py` | One repository per project |
| `~/datasets/<source>` | Downloaded raw data, with `SOURCE.txt` and `SHA256SUMS.txt` (data in BigQuery stays there) | Never committed |
| `~/financial-model-foundation/04-learning-notes` | Private learning notes and interview prep, one file per project | Private repository |

Two folders, two kinds of command:

- **Starting a project:** run from `~/analytics-playbook`.
- **Everything during a project:** run from the project folder, `~/projects/<project-name>`. Every project carries its own copy of the check tools in `tools/`.

---

## 2. One-time setup (once per computer)

1. Clone the two repositories into your home folder:
   ```bash
   cd ~
   git clone https://github.com/HarjiiBoss/analytics-playbook.git
   git clone https://github.com/HarjiiBoss/financial-model-foundation.git
   ```
2. Log the GitHub CLI in, so `new_project.py` can create repositories:
   ```bash
   gh auth login
   ```
3. Install the check tools' requirements:
   ```bash
   pip install pre-commit nbclient nbformat ipykernel pypdf
   ```
4. Let zsh accept `#` comments in pasted commands. Without this, a pasted line with a comment fails with "unknown file attribute":
   ```bash
   echo 'setopt interactivecomments' >> ~/.zshrc && source ~/.zshrc
   ```
5. Keep raw data in `~/datasets/<source>/`, with a `SOURCE.txt` note and a `SHA256SUMS.txt` written at download (Playbook Phase 1 → Dataset Library).

---

## 3. Start a new project

Run from `~/analytics-playbook`.

1. Get the latest templates:
   ```bash
   cd ~/analytics-playbook && git checkout main && git pull
   ```
2. See what would be created, without creating anything:
   ```bash
   python3 tools/new_project.py --dry-run --title "Project Title" --domain "Credit Risk" --data ~/datasets/<source>
   ```
3. Create it. Drop `--data` if the data is not in the Dataset Library yet. Repositories are private until you make them public at the end of Phase 5:
   ```bash
   python3 tools/new_project.py --title "Project Title" --industry "Industry" --domain "Credit Risk" --data ~/datasets/<source>
   ```
   If the data stays in BigQuery instead of being downloaded, use `--source bigquery` in place of `--data`. It adds the BigQuery packages, the BigQuery settings in `.env.example`, a `data/raw/SOURCE.txt` to fill in, and a loading notebook that checks the tables against a snapshot instead of a checksum.
4. Go into the project and set up its Python environment:
   ```bash
   cd ~/projects/<project-name>
   python3 -m venv .venv && source .venv/bin/activate
   pip install -r requirements.txt
   cp .env.example .env
   ```
   For a BigQuery project, also log in once per computer with `gcloud auth application-default login`, and fill in `GCP_PROJECT_ID` and `BQ_SOURCE_DATASET` in `.env`.
5. Confirm the setup is right:
   ```bash
   python3 tools/check_phase.py 0
   ```
   The first three lines should say PASS. The unticked boxes it lists are your Phase 0 to-do list.
6. You are now on the `phase-0-scoping` branch. Fill in `PROJECT_INFO.md` and `docs/phase_00_setup.md`.
7. Your private learning notes file is at `~/financial-model-foundation/04-learning-notes/<project-name>.md`. Commit it in that repository, never in the project.

---

## 4. Work through a phase

The same loop for every phase, 0 to 5. Run everything from the project folder.

1. **Branch.** Start each phase on its own branch (Phase 0's is made for you):
   ```bash
   git checkout main && git pull
   git checkout -b phase-2-business-analysis
   ```
2. **Work.** Write notebooks and SQL. Fill in `docs/phase_0N_*.md` as you go, including Methods Explained.
3. **Commit in small steps, staging files by name:**
   ```bash
   git add notebooks/02_business_analysis.ipynb docs/phase_02_business_analysis.md
   git commit -m "feat: churn rate by tenure band"
   ```
   Avoid `git add -A` and `git add .`. They also stage scratch notebooks, `.DS_Store` and data files that happen to be in the folder. The pre-commit hooks run on every commit. If a hook fails, the commit did not happen: fix what it names and commit again.
4. **End of phase.** In each notebook you changed: restart the kernel, run all cells, save. Then:
   ```bash
   python3 tools/check_phase.py 2
   ```
5. **Fix and tick.** Fix every FAIL using the "To fix" lines it prints. Tick each Exit Checklist box in the phase document, or note why it does not apply. Run the check again until every line says PASS.
6. **Push and review:**
   ```bash
   git push -u origin phase-2-business-analysis
   ```
   Open the pull request on GitHub. The template lists the checks. Squash-merge it, then delete the branch.
7. **Back to main** before the next phase:
   ```bash
   git checkout main && git pull
   git branch -D phase-2-business-analysis
   ```

---

## 5. Which check runs when

| When | Command (from the project folder) | Runs by itself? | What it catches |
|---|---|---|---|
| Every commit | The pre-commit hooks | Yes, on `git commit` | Large files, private keys, merge markers; notebook problems when a notebook changes; figures not in the outputs when README or `docs/` changes |
| End of Phase 0 | `python3 tools/check_phase.py 0` | No | Wrong branch, hooks not installed, any hook failing on any file |
| End of Phases 1–4 | `python3 tools/check_phase.py N` | No | All of the above, plus a notebook that fails when run top to bottom from a fresh kernel |
| End of Phase 5 | `python3 tools/check_phase.py 5` | No | All of the above, plus figures in the write-up that no output holds, and template text, local paths or private notes left in the repository |
| Any time, one notebook | `python3 tools/check_notebooks.py notebooks/<file>.ipynb` | No | Empty cells, cells run out of order, saved errors, local paths |
| Any time, the write-up | `python3 tools/check_figures.py .` | No | Figures in README, project page and executive summary not found in the outputs |

`check_phase.py` changes nothing; it only reports. Add `--no-execute` when a notebook queries BigQuery or another paid service, and run those notebooks yourself from a restarted kernel instead. `python3 tools/check_phase.py --list` shows what each phase runs.

---

## 6. When a check fails

| Message | What it means | Fix |
|---|---|---|
| `You are on main` | Phase work is on `main` | `git checkout -b phase-N-description`, then commit there |
| `pre-commit is installed, but not in this clone` | Hooks not set up in this project | `pre-commit install` |
| `cells run out of order` | Saved outputs did not come from one top-to-bottom run | Restart the kernel, run all cells, save |
| `fails when run from a fresh kernel` | The notebook depends on something run earlier or elsewhere | Fix the cell named, then restart and run all |
| `absolute local path: /Users/...` | A path to your Mac is in the code or its output | Use a path relative to the project (`data/raw/...`), re-run the cell, save |
| A figure listed by `check_figures.py` | That number is in the text but not in any output | Correct the text from the output; if derived and checked by hand, add it to `.figures-allow` with its calculation |
| `template comment` or `placeholder` | Template text left in a document | Delete it or fill it in |
| `large files` hook fails | A file over 5 MB was staged, usually data | `git restore --staged <file>`; add its folder to `.gitignore` if needed |

---

## 7. Finishing a project (Phase 5)

1. Write the executive summary first, then the README, project page and dashboard text from it.
2. Fill in `docs/published_surfaces.md`: every place the findings will appear (portfolio card, GitHub profile, resume, LinkedIn).
3. Run `python3 tools/check_phase.py 5` until every line says PASS.
4. Merge the Phase 5 pull request.
5. Make the repository public on GitHub (Settings → General → Danger Zone → Change visibility).
6. Update each surface in `docs/published_surfaces.md` and set its Last checked date.

---

## 8. Projects made before v3.6.3

Projects created before this version do not have `tools/check_phase.py`, and the older ones have no `tools/` folder at all. To add the current tools to a project, on a branch:

```bash
cd ~/projects/<project-name>
git checkout -b chore-update-check-tools
mkdir -p tools
cp ~/analytics-playbook/tools/check_figures.py ~/analytics-playbook/tools/check_notebooks.py \
   ~/analytics-playbook/tools/check_publication.py ~/analytics-playbook/tools/check_phase.py tools/
git add tools/ && git commit -m "chore: update check tools to playbook v3.6.3"
```

The pre-commit hooks also need `.pre-commit-config.yaml`; copy it from `~/analytics-playbook/templates/pre-commit-config.yaml` to `.pre-commit-config.yaml` and run `pre-commit install`.
