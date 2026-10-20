# {{PROJECT_TITLE}}

<!-- One sentence: what the project analyses and what decision it supports. -->

Built with the Data Analysis Playbook v{{PLAYBOOK_VERSION}}.

> **Status:** Phase 0 in progress. Findings will be added when the project is complete.

<!-- Add an Executive Summary section (key findings, business impact, recommendations) in Phase 5, once the analysis is finished. Until then the status line above is enough. -->

---

# Business Problem

{{BUSINESS_PROBLEM}}

# Business Question

{{BUSINESS_QUESTION}}

---

# Approach

<!-- Primary and secondary metrics, the decision rule (for experiments), validity checks and the tool stack, in a few bullet points. -->

- **Primary metric:**
- **Stack:**

Full scoping (hypotheses, metric definitions, scope, risks and assumptions): [PROJECT_INFO.md](PROJECT_INFO.md)

---

# Dataset

| Item | Details |
|------|---------|
| Source | |
| Contents | |
| Licence | |
| Size | |

<!-- State whether the data is stored in the repository. If not, point to Reproducibility for how to download it. -->

---

# Progress

- [ ] Phase 0 — Scoping & Project Setup
- [ ] Phase 1 — Data Loading, Cleaning & Exploration
- [ ] Phase 2 — Business Analysis
- [ ] Phase 3 — Analytical Method Selection
- [ ] Phase 4 — Advanced Analytics & Modelling
- [ ] Phase 5 — Reporting, Communication & Publication

---

# Reproducibility

1. Clone the repository and create the environment:
   ```bash
   git clone <repository-url>
   cd {{PROJECT_SLUG}}
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
2. Copy `.env.example` to `.env` and fill in your own values.

<!-- Add one step per action needed to rebuild the results: database setup, data download with its checksum check, then each notebook and SQL script in order. -->

---

# Repository Structure

```text
{{PROJECT_SLUG}}/
├── assets/            # Images used in documentation
├── data/
│   ├── raw/           # Downloaded data (not committed)
│   └── processed/     # Cleaned outputs (not committed)
├── docs/              # Phase documents, registers and notes
├── notebooks/         # Jupyter notebooks, run in numbered order
├── outputs/           # Finished charts (chart_*.png) and result tables
├── reports/           # Written reports
├── sql/               # SQL scripts, run in numbered order
├── tableau/           # Dashboard files
├── .env.example       # Template for local configuration
├── PROJECT_INFO.md    # Project charter
├── README.md
└── requirements.txt
```

---

# Documentation

| Document | Purpose |
|----------|---------|
| [PROJECT_INFO.md](PROJECT_INFO.md) | Project charter: question, metrics, decision rules, scope, risks |
| [docs/phase_00_setup.md](docs/phase_00_setup.md) | Phase 0 record: setup, issues and exit checklist |
| [docs/data_dictionary.md](docs/data_dictionary.md) | Definition of every column |
| [docs/cleaning_log.md](docs/cleaning_log.md) | Every change between the raw and clean data |
| [docs/project_glossary.md](docs/project_glossary.md) | Terms used in the project |
| [docs/assumption_register.md](docs/assumption_register.md) | Assumptions and their validation status |
| [docs/security_notes.md](docs/security_notes.md) | Security checks and data handling |
| [docs/documentation_index.md](docs/documentation_index.md) | Index of all project documents |

<!-- Add each phase document to this table when its phase starts. -->

---

# License

The code and documentation in this repository are released under the MIT License. <!-- State the dataset's own licence or terms, or say they are unknown. -->
