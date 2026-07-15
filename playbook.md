# Data Analysis Playbook
### A Personal Standard Operating Procedure for End-to-End Analytics Projects

**Author:** Taofeek Salami  
**First Formalized:** July 2026 (Project 08 — Fintech Credit Risk Analysis)  
**Version:** 1.0  
**Purpose:** Establish a repeatable, well-documented workflow for approaching any analytics project—from portfolio work to production environments. This playbook is tool-agnostic and can be applied across industries, datasets, and business domains.

---

# Why This Exists

Good analysts are not defined by avoiding messy data—they are defined by having a consistent process for handling it.

This playbook captures the workflow, standards, and analytical principles developed across multiple end-to-end projects. Rather than documenting a single project, it serves as a reusable framework that can be applied whenever a new dataset or business problem is encountered.

The goal is simple:

- Solve business problems systematically.
- Make analytical decisions reproducible.
- Produce work that can withstand technical review.
- Create outputs that business stakeholders can confidently act upon.

---

# Core Principles

Every project should satisfy these principles regardless of the dataset, industry, or technology stack.

1. **Start with the business problem—not the data.**
2. **Make every analytical decision reproducible.**
3. **Document assumptions before drawing conclusions.**
4. **Preserve evidence before modifying data.**
5. **Treat data quality issues as potential analytical findings.**
6. **Prefer transparent methodology over unnecessary complexity.**
7. **Never imply precision the data cannot support.**
8. **Build outputs that both technical and non-technical audiences can understand.**

---

# The Five-Phase Workflow

---

## Phase 0 — Scoping & Setup

### Objective

Understand the business problem and prepare the project environment.

### Exit Condition

- Business problem defined
- Repository created
- Environment configured
- Dataset accessible
- Documentation skeleton prepared

### Standard Tasks

- Define the business question before touching the data.
- Identify stakeholders and intended business impact.
- Determine project success criteria.
- Create repository structure:

```text
data/
docs/
notebooks/
outputs/
sql/
tableau/
```

- Configure version control.
- Store credentials securely using `.env`.
- Create an initial README containing:
  - Title
  - Problem Statement
  - Repository Structure
  - Methodology
  - Findings placeholders

---

## Phase 1 — Data Loading, Cleaning & Exploration

### Objective

Understand the dataset before attempting any analysis.

### Exit Condition

- Clean dataset saved
- EDA completed
- Data Dictionary started
- Data quality decisions documented

### Standard Workflow

### 1. Load

Import the dataset into the chosen analytical environment.

Examples:

- SQL database
- Pandas DataFrame
- DuckDB
- Spark

---

### 2. Understand

Profile the dataset.

Always determine:

- Row count
- Column count
- Data types
- Missing values
- Duplicate records
- Target balance
- Basic descriptive statistics

---

### 3. Clean

Every cleaning decision must be intentional.

For every issue:

- Identify it
- Measure it
- Decide how to treat it
- Record the rationale

Never silently:

- Drop rows
- Remove columns
- Impute values
- Cap outliers

Document every decision.

---

### 4. Explore

Perform exploratory analysis to understand:

- Variable distributions
- Relationships
- Correlations
- Business patterns
- Potential analytical risks

Generate supporting visualizations before moving forward.

---

## Phase 2 — Business Domain Analysis

### Objective

Answer the first major business question.

### Exit Condition

Documented business findings supported by quantitative evidence.

Typical activities:

- SQL segmentation
- Business metrics
- Initial visualizations
- Written interpretation

---

## Phase 3 — Advanced Analysis

### Objective

Develop higher-level analytical outputs that cannot be obtained through simple aggregation.

Examples include:

- Composite scores
- Behavioral segmentation
- Financial indices
- Customer segmentation
- Feature engineering

### Exit Condition

Custom analytical outputs validated against real outcomes whenever possible.

---

## Phase 4 — Reporting & Communication

### Objective

Transform analysis into decision-ready outputs.

### Exit Condition

Repository is publicly presentable and fully reproducible.

Deliverables include:

- Tableau dashboard
- README
- Documentation
- Screenshots
- Supporting exports

---

# Analysis Principles

These principles apply throughout every phase.

## 1. Let the data speak.

State only what the data supports.

Interpret patterns.

Do not invent causes.

---

## 2. Every decision deserves documentation.

Cleaning decisions should never exist only inside notebook code.

Document:

- What changed
- Why it changed
- Business impact

---

## 3. Correlation is not causation.

Describe observed relationships.

Avoid unsupported causal claims.

---

## 4. Weird values may be valuable.

Before removing an outlier, test whether it contains business signal.

Unexpected observations often become the strongest findings.

---

## 5. Name every proxy.

Whenever an exact metric cannot be calculated:

- Build a proxy
- Name it clearly
- Explain assumptions
- Explain limitations

Never disguise a proxy as an exact measurement.

---

## 6. Evidence before assumptions.

Every recommendation should trace back to:

- SQL result
- Python output
- Visualization
- Statistical evidence

---

# Technical Standards

---

## SQL

### File Naming

```text
00_setup.sql
01_exploration.sql
02_business_question.sql
03_business_question.sql
04_business_question.sql
```

Every SQL file should include:

```sql
Project
Phase
Purpose
Author
Status
```

Every structural change should be verified immediately.

Examples:

- Row count
- NULL audit
- Duplicate check
- Constraint validation

---

## Python

- One notebook per major phase.
- Explain decisions using Markdown before code.
- Use descriptive variable names.
- Avoid modifying filtered DataFrames without `.copy()`.
- Load credentials from `.env`.
- Keep notebooks reproducible.

---

## Tableau

Each dashboard should answer one business question.

Recommended structure:

- Executive Overview
- Dashboard 1
- Dashboard 2
- Dashboard 3

Each dashboard should contain:

- KPI cards
- Supporting charts
- Interactive filters
- Navigation buttons
- Business commentary

---

# Documentation Standards

Every project should contain:

```text
README.md

docs/
│
├── documentation_index.md
├── data_dictionary.md
├── project_glossary.md
├── tableau_blueprint.md
├── security_notes.md
├── phase_00_setup.md
├── phase_01_cleaning_eda.md
├── phase_02_business_analysis.md
├── phase_03_business_analysis.md
└── phase_04_business_analysis.md
```

Documentation should be written immediately after each phase—not reconstructed at project completion.

---

# Naming Conventions

## SQL

```text
00_setup.sql
01_cleaning.sql
02_default_risk.sql
03_revenue_leakage.sql
04_operational_inefficiency.sql
```

---

## Outputs

```text
outputs/sql_<description>.csv

outputs/chart_<description>.png

outputs/table_<description>.csv
```

---

## Processed Data

```text
data/processed/

dataset_cleaned.csv

dataset_risk_scored.csv

dataset_final.csv
```

---

## Documentation

```text
docs/phase_00_setup.md

docs/phase_01_cleaning_eda.md

docs/phase_02_analysis.md
```

---

# Data Dictionary Standard

Build the data dictionary during cleaning—not after the project ends.

Every variable should include:

- Name
- Data Type
- Business Meaning
- Missingness
- Cleaning Decision
- Notes

Engineered variables should additionally include:

- Purpose
- Creation logic
- Business interpretation

---

# Quality Assurance Checklist

Before publishing a project:

- [ ] All notebooks execute from top to bottom.
- [ ] SQL scripts run without errors.
- [ ] Dashboard matches documented findings.
- [ ] README reflects the final project.
- [ ] Documentation is complete.
- [ ] Data Dictionary is current.
- [ ] Project Glossary is updated.
- [ ] Screenshots exported.
- [ ] Credentials removed from version control.
- [ ] `.gitignore` verified.
- [ ] Repository structure is clean.
- [ ] No temporary files remain.
- [ ] Results are reproducible from raw data.

---

# Standard Deliverables

Every completed analytics project should contain:

- README
- SQL scripts
- Python notebooks
- Raw dataset
- Processed datasets
- Tableau dashboard
- Dashboard screenshots
- Data Dictionary
- Project Glossary
- Tableau Blueprint
- Phase Documentation
- Documentation Index
- Security Notes

---

# Applying This Framework at Work

This workflow scales naturally from portfolio projects to professional analytics environments.

The terminology may change, but the process remains the same.

| Portfolio Project | Workplace Equivalent |
|-------------------|----------------------|
| README | Executive Summary or Technical Report |
| Repository | Project Workspace |
| Dashboard | Business Intelligence Report |
| Phase Documentation | Project Documentation |
| Business Questions | Stakeholder Requirements |
| Deliverables | Sprint Deliverables |
| Findings | Business Recommendations |

Whether working independently or within a cross-functional team, the same principles apply:

- Understand the problem first.
- Preserve analytical evidence.
- Document every important decision.
- Make results reproducible.
- Deliver clear business value.

---

# Lessons Learned

Every project teaches something worth keeping.

Some recurring lessons include:

- Outliers can be valuable business signals rather than data errors.
- Missing values often contain information and should not always be imputed.
- Proxy variables are acceptable when exact measures are unavailable, provided assumptions are documented.
- Data quality issues frequently become analytical findings.
- Strong documentation is as important as strong analysis.
- Dashboards communicate findings; documentation explains how those findings were produced.
- Simplicity and clarity usually outperform unnecessary analytical complexity.

---

# Continuous Improvement

This playbook is intended to evolve.

Whenever a project introduces a new analytical technique, documentation practice, or workflow improvement worth repeating, update this document.

The objective is not to create a perfect process—it is to build a better one with every project completed.
