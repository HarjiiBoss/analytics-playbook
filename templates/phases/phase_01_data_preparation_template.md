# Phase 1 — Data Loading, Cleaning & Exploration

<!-- This document records all activities completed during **Phase 1 — Data Loading, Cleaning & Exploration**. The objective of this phase is to understand the available evidence, evaluate data quality, prepare the dataset for analysis, and generate initial hypotheses. -->

---

# Phase Objective

Understand the dataset before attempting to answer business questions.

The purpose of exploratory work is **not** to produce business conclusions.

It is to understand the evidence available for later analysis.

---

# Phase Status

| Field | Value |
|--------|-------|
| Status | Not Started |
| Started | |
| Completed | |
| Owner | |
| Last Updated | {{LAST_UPDATED}} |

---

# Data Acquisition

Document every dataset used during this phase.

| Dataset | Source | Owner | Extraction Date | Refresh Frequency | Notes |
|----------|--------|-------|-----------------|-------------------|------|
| | | | | | |

## Provenance

| File | Licence | Original Publisher | SHA-256 Checksum | Download Date | Row Count |
|------|---------|--------------------|------------------|---------------|-----------|
| | | | | | |

<!-- The loading notebook stops if the checksum differs (Playbook Phase 1 → Data Provenance). -->

---

# Dataset Overview

Provide a high-level description of the dataset and its relevance to the business problem.

---

# Initial Data Profiling

Record the initial characteristics of the dataset before any modifications.

| Item | Value |
|------|-------|
| Row Count | |
| Column Count | |
| Observation Unit | |
| Time Coverage | |
| Target Variable | |
| Primary Identifier | |

---

# Variable Summary

Document the major variable groups within the dataset.

| Variable Group | Description |
|---------------|-------------|
| | |

---

# Data Quality Assessment

Evaluate data quality before making any changes.

## Missing Values

Summary:

---

## Duplicate Records

Summary:

---

## Invalid Values

Summary:

---

## Outliers

Summary:

---

## Inconsistent Categories

Summary:

---

## Timestamp Integrity

Summary:

---

## Potential Data Leakage

Summary:

---

## Other Data Quality Issues

Summary:

---

# Cleaning Decisions

Summarize the major cleaning activities performed during this phase.

| Activity | Reason | Related Documentation |
|----------|--------|-----------------------|
| | | Cleaning Log |

---

# Raw-to-Clean Reconciliation

<!-- Every difference must be explained by a logged cleaning decision (Playbook Phase 1 → Reconcile Raw and Clean). -->

| Check | Raw | Clean | Difference | Explained by |
|-------|-----|-------|------------|--------------|
| Row count | | | | |
| Distinct keys | | | | |
| Category counts | | | | |
| Numeric column totals | | | | |
| Values that failed type conversion | | | | |
| Date range (earliest – latest) | | | | |

Date format or locale set at import: <!-- for example, "English (United States), m/d/yyyy" -->

Dates checked against an ordered key (invoice or ID numbers): <!-- yes / not applicable, with the result -->

---

# Supporting Documentation Updated

Confirm supporting documentation has been maintained throughout this phase.

- [ ] Data Dictionary
- [ ] Cleaning Log
- [ ] Assumption Register
- [ ] Project Glossary

---

# Exploratory Data Analysis (EDA)

## Univariate Analysis

Summarize key distributional characteristics.

-

-

-

---

## Bivariate Analysis

Summarize important relationships identified between variables.

-

-

-

---

## Multivariate Analysis (if applicable)

Summarize higher-order relationships explored during EDA.

-

-

-

---

# Initial Observations

Record observations supported directly by the data.

These observations should describe patterns rather than explain causes.

-

-

-

---

# Initial Hypotheses

Document hypotheses generated during exploration.

These should guide later analysis and should **not** be presented as conclusions.

-

-

-

---

# Data Risks

Identify risks that may influence interpretation or later modelling.

-

-

-

---

# Related Documentation

- Project Information
- Data Dictionary
- Cleaning Log
- Assumption Register
- Project Glossary

---

# Phase Deliverables

- [ ] Clean dataset
- [ ] Data Dictionary updated
- [ ] Cleaning Log updated
- [ ] Assumption Register updated
- [ ] EDA completed
- [ ] Initial observations documented
- [ ] Initial hypotheses documented

---

# Methods Explained

<!-- The reasoning behind this phase's choices, written for a reviewer such as a hiring manager or a client's analyst (Playbook Part V → Reasoning in the Project Files). One block per method, rule or definition; state each point once, plainly. This is a decision record, not a tutorial: background on how a method works belongs in financial-model-foundation. Delete the example block if the phase used none. -->

### [Method, rule or definition]

- **Decision:** what was used, with its settings
- **Alternatives considered:** and why they were not used
- **How to read the result:** what the output means for the business question, and its limits

---

# Exit Checklist

Proceed to **Phase 2 — Business Analysis** only when:

## Data Understanding

- [ ] Dataset fully profiled
- [ ] Variables understood
- [ ] Major business entities identified

---

## Data Quality

- [ ] Missing values assessed
- [ ] Duplicate records assessed
- [ ] Invalid values investigated
- [ ] Outliers reviewed
- [ ] Timestamp integrity verified
- [ ] Date format or locale set explicitly at import, and the date range matches the documented period

---

## Cleaning

- [ ] Cleaning decisions documented
- [ ] Raw data preserved
- [ ] Processed dataset created
- [ ] Raw-to-clean reconciliation recorded, with every difference explained
- [ ] Checksum recorded and checked by the loading notebook

---

## Documentation

- [ ] Data Dictionary updated
- [ ] Cleaning Log complete
- [ ] Assumption Register updated
- [ ] Phase documentation complete
- [ ] Methods Explained filled in for every method, rule or definition used in this phase
- [ ] `python3 tools/check_phase.py 1` passes (includes every notebook run from a fresh kernel)

---

# Phase Outcome

Summarize the overall condition of the dataset, the major findings from exploratory work, and confirm readiness to proceed to **Phase 2 — Business Analysis**.

---
