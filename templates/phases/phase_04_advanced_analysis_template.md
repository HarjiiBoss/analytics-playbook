# Phase 4 — Advanced Analytics & Modelling

> This document records all advanced analytical work performed during **Phase 4 — Advanced Analytics & Modelling**.
>
> This phase should only begin after **Phase 3 — Analytical Method Selection** has demonstrated that descriptive and diagnostic analysis alone cannot adequately answer the business question.
>
> Every analytical method used should be explicitly justified, validated, and interpreted within the limits of the available evidence.

---

# Phase Overview

| Field | Value |
|--------|-------|
| Project | {{PROJECT_TITLE}} |
| Repository | {{PROJECT_SLUG}} |
| Phase | Phase 4 — Advanced Analytics & Modelling |
| Status | Not Started |
| Started | |
| Completed | |
| Analyst | {{AUTHOR}} |
| Last Updated | {{LAST_UPDATED}} |

---

# Phase Objective

Describe the objective of this phase.

Explain what business question requires advanced analytical methods and why the selected approach is appropriate.

---

# Business Question

{{BUSINESS_QUESTION}}

---

# Selected Analytical Method

| Item | Description |
|------|-------------|
| Method | |
| Business Decision Supported | |
| Expected Output | |

---

# Data Used

| Dataset | Purpose | Notes |
|----------|---------|-------|
| | | |

---

# Feature Engineering

Document any engineered variables created for the analysis.

| Feature | Purpose | Creation Logic | Notes |
|---------|----------|----------------|------|
| | | | |

---

# Analytical Workflow

Document the major analytical steps completed during this phase.

- Data preparation
- Feature engineering
- Model development
- Statistical analysis
- Validation
- Interpretation

---

# Model Development

Describe the analytical model or statistical procedure.

Include:

- Inputs
- Target variable (if applicable)
- Independent variables
- Parameter choices
- Configuration
- Software or libraries used

---

# Statistical Analysis

Record any inferential analyses performed.

Examples include:

- Hypothesis testing
- Confidence intervals
- ANOVA
- Chi-square tests
- Regression analysis
- Non-parametric tests

| Analysis | Purpose | Result |
|----------|---------|--------|
| | | |

---

# Model Validation

Describe how the analytical outputs were validated.

| Validation Method | Purpose | Result |
|-------------------|---------|--------|
| | | |

Examples include:

- Cross-validation
- Hold-out testing
- Residual analysis
- Assumption testing
- Back-testing
- Confusion matrix
- ROC-AUC
- Precision / Recall
- Calibration
- Manual verification

---

# Performance Metrics

Document model or analytical performance.

| Metric | Value | Interpretation |
|--------|-------|----------------|
| | | |

---

# Key Findings

Summarize the major analytical findings supported by the evidence.

| Finding | Supporting Evidence | Business Interpretation |
|----------|---------------------|-------------------------|
| | | |

---

# Business Interpretation

Translate technical results into business language.

Explain:

- What the results mean.
- Why they matter.
- Which decisions become easier because of the analysis.

---

# Recommendations

Provide evidence-based recommendations supported by the analysis.

For each recommendation, explain:

- What should be done.
- Why.
- Supporting evidence.
- Expected business impact.

| Recommendation | Evidence | Expected Impact |
|----------------|----------|-----------------|
| | | |

---

# Assumptions

Record assumptions introduced during modelling or statistical analysis.

| Assumption | Reason | Potential Impact |
|------------|--------|------------------|
| | | |

---

# Limitations

Document limitations affecting interpretation.

Examples include:

- Sample size
- Data quality
- Missing predictors
- Model assumptions
- Generalisability
- Historical data limitations

-

-

-

---

# Future Work

Identify opportunities for improving or extending the analysis.

-

-

-

---

# Phase Deliverables

- [ ] Feature engineering documented
- [ ] Advanced analysis completed
- [ ] Validation completed
- [ ] Performance metrics recorded
- [ ] Findings documented
- [ ] Recommendations prepared
- [ ] Limitations documented

---

# Methods Explained

<!-- The reasoning behind this phase's choices, written for a reviewer such as a hiring manager or a client's analyst (Playbook Part V → Reasoning in the Project Files). One block per method, rule or definition; state each point once, plainly. This is a decision record, not a tutorial: background on how a method works belongs in financial-model-foundation. Delete the example block if the phase used none. -->

### [Method, rule or definition]

- **Decision:** what was used, with its settings
- **Alternatives considered:** and why they were not used
- **How to read the result:** what the output means for the business question, and its limits

---

# Exit Checklist

Proceed only when:

- [ ] The selected analytical method has been completed.
- [ ] Results have been validated.
- [ ] Effect sizes reported with confidence intervals, not p-values alone.
- [ ] Practical significance stated against the threshold set in advance.
- [ ] Multiple comparisons handled: primary comparison fixed in advance, others marked exploratory or corrected.
- [ ] No split or filter on a variable measured after assignment (experiments).
- [ ] Predictive inputs were known before the outcome; performance measured on held-out data.
- [ ] Random seeds set for every random step.
- [ ] Findings are supported by evidence.
- [ ] Business implications have been clearly explained.
- [ ] Assumptions and limitations have been documented.
- [ ] Recommendations are ready for stakeholder communication.
- [ ] Methods Explained filled in for every method, rule or definition used in this phase
- [ ] `python3 tools/check_phase.py 4` passes (includes every notebook run from a fresh kernel)

---

# Notes

Use this section to record additional modelling decisions, experimental observations, implementation notes, references to the Financial Model Foundation, or considerations that may influence reporting and future work.
