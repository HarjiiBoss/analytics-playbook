# Data Analysis Playbook
### A Personal Standard Operating Procedure for End-to-End Analytics Projects

> A practical, project-tested framework for planning, executing, validating, documenting, and communicating analytics projects—from business problem to business recommendation.

**Author:** Taofeek Salami

---

## Overview

Most analytics resources teach individual tools.

This repository focuses on something different:

> **How professional analytical work is performed.**

The **Data Analysis Playbook** captures the workflow, standards, and decision-making framework I developed across multiple end-to-end analytics projects.

Rather than documenting a single project, it serves as a reusable operating manual for approaching analytics work consistently, transparently, and reproducibly.

Although the examples come from portfolio projects, the workflow is designed to scale naturally to professional analytics environments.

---

# Philosophy

Professional analytics is not defined by the complexity of its models.

It is defined by the consistency of its thinking.

Every project should:

- Start with a clearly defined business problem.
- Select methods appropriate to the question.
- Preserve analytical evidence.
- Document assumptions.
- Validate findings.
- Communicate conclusions honestly.
- Support better business decisions.

The objective is not impressive analysis.

The objective is **trustworthy analysis**.

---

# What You'll Find

## 📘 Data Analysis Playbook

The core handbook covering the complete analytics lifecycle, including:

- Business problem framing
- Project planning
- Data preparation
- Exploratory analysis
- Business analysis
- Analytical method selection
- Statistical analysis
- Predictive modelling
- Reporting
- Dashboard design
- Executive communication
- Documentation
- Quality assurance
- Repository standards
- Continuous improvement

---

## 📂 Templates

Reusable templates for future analytics projects.

Examples include:

- README and project charter (PROJECT_INFO) templates
- Phase documentation templates
- Data dictionary, glossary, assumption register and cleaning log templates
- SQL header template
- Notebook template with the standard header
- Tableau blueprint template
- `.gitignore` and `.env.example`

The objective is to eliminate repetitive setup work while maintaining consistent project quality.

---

## 🛠 Starting a New Project

`tools/new_project.py` creates a new project from the templates in this repository: folder structure, filled-in documents, SQL and notebook stubs, a first commit on `main`, the GitHub repository, and a `phase-0-scoping` branch.

```bash
git clone https://github.com/HarjiiBoss/analytics-playbook.git
cd analytics-playbook
git pull                     # use the latest templates
python3 tools/new_project.py --dry-run --title "Project Title"
python3 tools/new_project.py --title "Project Title" --industry "Industry" --domain "Domain"
```

Projects are created in `~/projects/` unless `--parent-dir` is given. The tool stops if the chosen folder is inside another Git repository. Creating the GitHub repository needs the GitHub CLI (`gh`) logged in; use `--no-github` to skip that step.

---

## 📊 Example Projects

Practical implementations demonstrating how the playbook is applied in real analytics projects.

Current examples include:

- Fintech Credit Risk Analysis
- Superstore Sales Analysis

Additional examples will be added as the framework evolves.

---

# Workflow

Every project follows the same high-level workflow.

```text
Business Problem
        │
        ▼
Project Scoping
        │
        ▼
Data Preparation
        │
        ▼
Business Analysis
        │
        ▼
Method Selection
        │
        ▼
Advanced Analytics
        │
        ▼
Validation
        │
        ▼
Reporting
        │
        ▼
Communication
        │
        ▼
Publication
```

Each phase has:

- clear objectives,
- defined deliverables,
- quality checkpoints,
- and exit criteria.

---

# Core Principles

Every project built using this framework follows the same principles.

- Start with the business problem—not the data.
- Select the simplest method capable of answering the question.
- Preserve analytical evidence before modifying data.
- Document assumptions explicitly.
- Match conclusions to the strength of the evidence.
- Validate before interpreting.
- Communicate uncertainty honestly.
- Design analysis for decision-making.
- Prioritize transparency over unnecessary complexity.
- Keep every project reproducible.

---

# Repository Structure

```text
analytics-playbook/
│
├── README.md
│
├── playbook/
│   └── DATA_ANALYSIS_PLAYBOOK.md
│
├── tools/
│   └── new_project.py
│
└── templates/
    ├── README_template.md
    ├── PROJECT_INFO_template.md
    ├── .gitignore
    ├── .env.example
    ├── LICENSE
    ├── requirements.txt
    │
    ├── docs/
    │   ├── documentation_index_template.md
    │   ├── data_dictionary_template.md
    │   ├── project_glossary_template.md
    │   ├── assumption_register_template.md
    │   ├── cleaning_log_template.md
    │   ├── security_notes_template.md
    │   └── tableau_blueprint_template.md
    │
    ├── notebooks/
    │   └── notebook_template.ipynb
    │
    ├── phases/
    │   ├── phase_00_setup_template.md
    │   ├── phase_01_data_preparation_template.md
    │   ├── phase_02_business_analysis_template.md
    │   ├── phase_03_method_selection_template.md
    │   ├── phase_04_advanced_analysis_template.md
    │   └── phase_05_reporting_template.md
    │
    ├── reports/
    │   ├── executive_summary_template.md
    │   └── presentation_notes_template.md
    │
    └── sql/
        └── sql_template.sql
```

Phases are numbered 0 to 5, and each phase template's number matches its phase.

---

# Who This Repository Is For

This repository is intended for anyone who wants a structured approach to analytics work, including:

- Data Analysts
- Business Intelligence Analysts
- Product Analysts
- CRM Analysts
- Credit Risk Analysts
- Analytics Engineers
- Students building portfolios
- Career changers entering analytics

---

# Relationship to the Financial Model Foundation

This repository focuses on **how analytical work should be performed**.

Its companion repository, **Financial Model Foundation**, focuses on **the analytical methods and modelling concepts themselves**.

Together they form a complementary learning system.

| Repository | Focus |
|------------|-------|
| **Data Analysis Playbook** | Workflow, documentation, reporting, communication, operational standards |
| **Financial Model Foundation** | Statistics, predictive modelling, forecasting, experimentation, financial analytics, analytical frameworks |

---

# Why This Repository Exists

Many analytics portfolios demonstrate technical skills.

Few demonstrate **how the work is actually organised, validated, documented, and communicated**.

This repository attempts to bridge that gap by documenting a repeatable process that can be applied across industries, datasets, and business domains.

The goal is not simply to complete analytics projects.

The goal is to build projects that are:

- Reproducible
- Transparent
- Technically defensible
- Business-focused
- Easy to maintain
- Easy to review

---

# Related Projects

This playbook serves as the operating framework behind the analytics projects published in my portfolio.

Current implementations include:

- Fintech Credit Risk Analysis
- Superstore Sales Analysis

Future projects will continue to refine and expand the methodology.

---

# License

This project is released under the MIT License.

You are welcome to use, adapt, and improve the framework with appropriate attribution.

---

## Continuous Improvement

This playbook is intentionally a living document.

As new projects introduce better analytical methods, documentation practices, or communication techniques, the framework will continue to evolve.

Every improvement is recorded in the playbook's version history to ensure the methodology remains transparent, reproducible, and continuously refined.
