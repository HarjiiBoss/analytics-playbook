# {{PROJECT_TITLE}}

<!-- Project charter. This is the one place where the Phase 0 scoping decisions are recorded: business question, hypotheses, metrics, decision rules, scope, risks and assumptions. Other documents link here instead of repeating them. -->

---

# Project Overview

| Field | Value |
|--------|-------|
| Project Title | {{PROJECT_TITLE}} |
| Repository | {{PROJECT_SLUG}} |
| Industry | {{INDUSTRY}} |
| Analytics Domain | {{ANALYTICS_DOMAIN}} |
| Project Type | {{PROJECT_TYPE}} |
| Status | Phase 0 — Scoping |
| Author | {{AUTHOR}} |
| Date Created | {{DATE_CREATED}} |
| Last Updated | {{LAST_UPDATED}} |

---

# Business Context

<!-- The business environment: the organisation or product, the current situation and why this analysis is needed. State where any description comes from if it cannot be verified. -->

---

# Business Problem

{{BUSINESS_PROBLEM}}

<!-- Describe what needs to be solved, not the analysis that will be performed. -->

---

# Primary Business Question

{{BUSINESS_QUESTION}}

**Decision supported:** <!-- The options the decision-maker will choose between. -->

---

# Supporting Analytical Questions

<!-- The questions that must be answered to support the primary business question. -->

-

---

# Hypotheses

<!-- For experiments and statistical tests. State whether tests are one-sided or two-sided. Delete this section if no formal tests are planned. -->

| Metric | Type | Null Hypothesis (H₀) | Alternative Hypothesis (H₁) |
|--------|------|----------------------|-----------------------------|
| | Primary | | |

---

# Decision Rules

<!-- For experiments. Set before the data is downloaded or examined (Playbook Part II, Phase 0). Include: significance level, minimum effect of interest (δ) or why none could be justified, what each outcome means, whether guardrails can block the decision, and whether the author had seen published results for this dataset. Delete this section if the project does not test a change. -->

Set before any data was examined.

**Significance level:**

**Minimum effect of interest:**

| Outcome | Rule |
|---------|------|
| | |

**Guardrail:**

**Blinding:**

---

# Stakeholders

| Stakeholder | Role | Decision Supported | Needs from the Result |
|-------------|------|--------------------|-----------------------|
| | | | |

---

# Business Objectives

-

---

# Success Criteria

-

---

# Scope

## Included

-

## Excluded

-

---

# Expected Deliverables

<!-- Keep the items that apply. -->

- [ ] README
- [ ] Executive Summary
- [ ] Technical Report
- [ ] SQL Scripts
- [ ] Python Notebooks
- [ ] Dashboard
- [ ] Presentation
- [ ] Data Dictionary
- [ ] Cleaning Log
- [ ] Assumption Register
- [ ] Project Glossary

---

# Available Data

<!-- Copy source, licence, download date and checksum file from data/raw/SOURCE.txt and data/raw/SHA256SUMS.txt (Playbook Phase 1 → Dataset Library). -->

| Dataset | Source | Publisher/uploader | Refresh Frequency | Status |
|----------|--------|--------------------|-------------------|--------|
| | | | | |

---

# Planned Analytical Approach

<!-- One bullet per phase: what will be done and why. -->

- **Phase 1:**
- **Phase 2:**
- **Phase 3:**
- **Phase 4:**
- **Phase 5:**

---

# Planned Success Metrics

| Metric | Business Meaning | Notes |
|---------|------------------|-------|
| | | |

<!-- For each metric, add a block answering the six questions below. -->

## [Metric name] ([primary / secondary / guardrail])

| Question | Answer |
|----------|--------|
| What is measured? | |
| Why does it matter? | |
| How is it calculated? | |
| What assumptions exist? | |
| What are the limitations? | |
| How will decisions change? | |

---

# Known Risks

| Risk | Potential Impact | Mitigation |
|------|------------------|------------|
| | | |

---

# Constraints

<!-- Data, time, tool and resource limits, for example platform quotas or missing variables. -->

-

---

# Initial Assumptions

| Assumption | Reason | Validation Planned |
|------------|--------|--------------------|
| | | |

This table is the Phase 0 snapshot. Validation results are tracked in [docs/assumption_register.md](docs/assumption_register.md).

---

# Dependencies

<!-- Anything required before analysis can begin: access, accounts, credentials, data. Tick each when it is in place. -->

- [ ]

---

# Planned Workflow

- [ ] Phase 0 — Scoping & Project Setup
- [ ] Phase 1 — Data Loading, Cleaning & Exploration
- [ ] Phase 2 — Business Analysis
- [ ] Phase 3 — Analytical Method Selection
- [ ] Phase 4 — Advanced Analytics & Modelling
- [ ] Phase 5 — Reporting, Communication & Publication

---

# Project Notes

<!-- Facts confirmed during the project, with where they were confirmed, kept separate from points that can only be taken from documentation. -->

---

# Revision History

| Date | Version | Summary |
|------|---------|---------|
| {{DATE_CREATED}} | 1.0 | Initial project charter created. |
