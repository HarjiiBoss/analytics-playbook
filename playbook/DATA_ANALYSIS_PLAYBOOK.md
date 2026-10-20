# Data Analysis Playbook
## A Personal Standard Operating Procedure for End-to-End Analytics Projects

**Author:** Taofeek Salami  
**Current Version:** 3.2  
**First Formalized:** July 2026 (Project 08 — Fintech Credit Risk Analysis)  
**Last Updated:** October 2026

---

# Purpose

This playbook defines my standard operating procedure for approaching analytics projects from initial business problem to final business recommendation.

It is designed to ensure that every project follows a consistent, reproducible, and evidence-based workflow regardless of the industry, dataset, or analytical tools involved.

Rather than documenting a single project, this document captures the principles, standards, workflows, and quality controls that govern how I perform analytical work.

It serves four primary purposes:

- Standardize analytical workflows.
- Improve reproducibility and documentation.
- Produce technically defensible analyses.
- Deliver business insights that stakeholders can confidently act upon.

This playbook is intentionally tool-agnostic. Whether using SQL, Python, Excel, Tableau, Power BI, R, DuckDB, Spark, or another platform, the underlying analytical process remains the same.

---

# Philosophy

Technology changes quickly.

Analytical thinking does not.

SQL syntax evolves.

Visualization tools improve.

Programming languages gain new libraries.

Business problems, however, continue to require the same fundamental process:

- Understand the problem.
- Evaluate the available evidence.
- Select an appropriate analytical method.
- Validate the results.
- Communicate findings honestly.
- Support business decisions.

This playbook exists because professional analytics is not defined by knowing the most sophisticated algorithm.

Professional analytics is defined by consistently applying sound analytical reasoning, transparent methodology, and disciplined documentation.

---

# Guiding Principle

> **The objective is not to produce impressive analysis.**
>
> **The objective is to produce trustworthy analysis.**

Every decision made throughout a project should improve one or more of the following:

- Accuracy
- Transparency
- Reproducibility
- Interpretability
- Business usefulness

If a technique increases complexity without improving these qualities, it should be reconsidered.

---

# Version History

| Version | Date | Major Changes |
|----------|------|---------------|
| 1.0 | July 2026 | Initial five-phase workflow, documentation standards, technical standards |
| 2.0 | July 2026 | Added Analytical Language & Evidence Standards |
| 2.1 | July 2026 | Added Report Structure & Prose Standards |
| 2.2 | July 2026 | Added Oral Presentation Planning |
| 2.3 | July 2026 | Added Presentation Building & Delivery Standards |
| 3.0 | August 2026 | Major restructuring. Added Method Selection Framework, Model Validation Standards, Business Metric Design Framework, Cross-Track Thinking, Model Documentation Standards, Analytical Reference Map, improved workflow architecture, and reduced redundancy throughout the playbook. |
| 3.1 | August 2026 | Added Branching Strategy to Version Control Standards |
| **3.2** | October 2026 | Added decision rules fixed before data access (Phase 0), data provenance, raw and clean layers and raw-to-clean reconciliation (Phase 1), Single Source of Truth (Documentation Standards), the Not testable status (Assumption Register), and the Notebook Header and Code Comment Standards. Templates simplified to match, and the project scaffolding tool moved into the playbook repository. |

---

# Intended Audience

Although written primarily for my own work, this playbook is designed to remain useful in multiple environments.

It can be applied to:

- Portfolio projects
- Freelance engagements
- Business intelligence projects
- Product analytics
- CRM analytics
- Credit risk analytics
- Operational analytics
- Commercial analytics
- Production analytics teams

The terminology may differ across organizations, but the analytical process remains fundamentally the same.

---

# Scope

This playbook governs every stage of an analytics project, including:

- Business problem definition
- Project planning
- Data acquisition
- Data cleaning
- Exploratory analysis
- Business analysis
- Statistical analysis
- Predictive modelling
- Forecasting
- Experimentation
- Reporting
- Dashboard development
- Documentation
- Presentation
- Quality assurance
- Project publication

Domain-specific mathematical concepts, modelling techniques, and financial frameworks are intentionally documented separately in the **Financial Model Foundation**.

This document focuses on **how analytical work should be performed**, not on teaching every analytical technique.

---

# Core Principles

Every project should satisfy these principles regardless of industry, dataset, or technology stack.

## 1. Start with the business problem—not the data.

Every analysis begins with a business question.

Data exists to answer business questions—not the other way around.

---

## 2. Select the simplest method capable of answering the question.

Sophisticated techniques should only be used when the business problem requires them.

Complexity is never an objective by itself.

---

## 3. Make every analytical decision reproducible.

Another analyst should be able to reproduce the entire project using:

- the raw data,
- documented assumptions,
- project files,
- and repository documentation.

---

## 4. Preserve evidence before modifying data.

Original data should remain recoverable.

Cleaning decisions must always be documented.

Evidence should never be destroyed for convenience.

---

## 5. Treat data quality issues as analytical findings.

Missing values, duplicates, inconsistent records, unexpected categories, and extreme observations often reveal business problems rather than analytical problems.

Investigate before removing.

---

## 6. Document assumptions before drawing conclusions.

Every assumption introduces uncertainty.

Whenever assumptions are required, explicitly document:

- why they were necessary,
- what alternatives were considered,
- and how they may influence interpretation.

---

## 7. Match the certainty of conclusions to the strength of evidence.

Strong conclusions require strong evidence.

Descriptive statistics support descriptive claims.

Experiments support causal claims.

Avoid overstating what the analysis can legitimately demonstrate.

---

## 8. Prefer transparency over unnecessary sophistication.

An interpretable solution that stakeholders understand is often more valuable than a complex solution that nobody trusts.

---

## 9. Design analyses for decision-making.

Every analysis should answer one practical question:

> **"What decision becomes easier because this analysis exists?"**

If the answer is unclear, revisit the business objective.

---

## 10. Documentation is part of the analysis.

Code explains *how* the analysis was executed.

Documentation explains *why* it was performed.

Neither should exist without the other.

---

# The Analytics Mindset

Throughout every project, continually ask four questions:

1. **What does the data show?**
2. **What does the evidence actually support?**
3. **What does the evidence not support?**
4. **What additional information would strengthen this conclusion?**

These questions encourage disciplined reasoning and help prevent unsupported conclusions.

---

# Cross-Track Thinking

Although industries use different terminology, many analytical problems share the same underlying structure.

For example:

| Domain | Business Question | Shared Analytical Pattern |
|---------|-------------------|---------------------------|
| Credit Risk | Which borrowers may default? | Estimate probability of an adverse event |
| CRM | Which customers may churn? | Estimate probability of an adverse event |
| Product Analytics | Which users may disengage? | Estimate probability of an adverse event |
| Operations | Which deliveries may be delayed? | Estimate probability of an adverse event |
| Fraud Analytics | Which transactions may be fraudulent? | Estimate probability of an adverse event |

Likewise:

| Domain | Business Objective |
|---------|--------------------|
| Credit Risk | Minimize expected financial loss |
| CRM | Protect customer lifetime value |
| Product Analytics | Improve retention and engagement |
| Operations | Improve efficiency and reduce operational risk |

Recognizing these common analytical structures makes analytical knowledge transferable across industries.

One of the objectives of this playbook is to build reusable analytical thinking rather than project-specific procedures.

---

# Relationship to the Financial Model Foundation

This playbook defines **how analytical work is performed.**

The accompanying **Financial Model Foundation** documents **the analytical methods and modelling concepts themselves.**

Together they form a complementary system.

| Document | Primary Purpose |
|-----------|-----------------|
| **Data Analysis Playbook** | Workflow, documentation, reporting, communication, quality standards |
| **Financial Model Foundation** | Statistical methods, financial concepts, predictive modelling, experimentation, forecasting, and analytical frameworks |

Whenever an advanced analytical method is required, this playbook should guide **when** and **why** the method is used, while the Financial Model Foundation provides the conceptual reference for **how** the method works.

---

# What Follows

The remainder of this playbook translates these principles into a repeatable workflow covering every stage of an analytics project—from business scoping through technical implementation, communication, publication, and continuous improvement.

The objective is simple:

> **Produce analyses that are reproducible, technically defensible, and capable of supporting better business decisions.**

---

# Part II — The Analytics Workflow

Good analytical work is rarely the result of a single brilliant insight.

It is usually the result of a disciplined process.

Every project should progress through the same structured workflow, regardless of the industry, dataset, or analytical tools involved.

Each phase has:

- a clear objective,
- defined deliverables,
- quality checkpoints,
- and an exit condition.

A phase should only be considered complete when its exit condition has been satisfied.

---

# Workflow Overview

```
Business Problem
        │
        ▼
Phase 0 ─ Scoping & Project Setup
        │
        ▼
Phase 1 ─ Data Loading, Cleaning & Exploration
        │
        ▼
Phase 2 ─ Business Analysis
        │
        ▼
Phase 2.5 ─ Analytical Method Selection
        │
        ▼
Phase 3 ─ Advanced Analytics & Modelling
        │
        ▼
Phase 4 ─ Reporting, Communication & Publication
```

Although projects vary in complexity, they should follow this sequence unless there is a documented reason to do otherwise.

---

# Phase 0 — Scoping & Project Setup

## Objective

Define the business problem before performing any analysis.

Poorly defined questions produce poor analyses regardless of technical ability.

---

## Key Questions

Before loading any data, answer:

- What business problem are we solving?
- Who are the stakeholders?
- Why does this problem matter?
- What decision will this analysis support?
- What does success look like?
- What assumptions already exist?
- What constraints exist?

---

## Standard Tasks

### Business Understanding

Document:

- Business context
- Stakeholders
- Objectives
- Success criteria
- Known risks
- Expected deliverables

`PROJECT_INFO.md` is the project charter. It is the one place where these scoping decisions are recorded.

---

### Decision Rules for Experiments

When the project tests a change (an A/B test or another controlled experiment), the rules for reading the result are fixed and written into `PROJECT_INFO.md` before the data is downloaded or examined.

Record:

- Primary metric (one only), secondary metrics and guardrail metrics
- Hypotheses and whether each test is one-sided or two-sided
- Significance level (α)
- Minimum effect of interest (δ), or a statement that no business threshold could be justified
- What each possible result means for the decision, including "collect more evidence"
- Whether a guardrail can block the decision or is exploratory only
- Planned exclusions and sensitivity checks
- A statement of whether the author had seen published results for the same dataset

Rules written after seeing the data can be adjusted, even unintentionally, to fit the result. If a rule has to change later, record the change and the reason in the charter's revision history and report it in the findings.

---

### Project Setup

Create the project structure.

```
project/

├── data/
│   ├── raw/
│   └── processed/
│
├── docs/
│
├── notebooks/
│
├── sql/
│
├── outputs/
│
├── tableau/
│
├── README.md
│
└── .gitignore
```

---

### Environment

Configure:

- Git repository
- Virtual environment
- Dependencies
- Environment variables (`.env`, not committed, with a committed `.env.example` listing the variable names without values)
- Database connection
- Folder structure

---

### Documentation

Create an initial README containing:

- Business problem
- Objectives
- Scope
- Planned workflow
- Repository structure
- Expected deliverables

---

## Deliverables

- Repository created
- Environment configured
- README initialized
- Business problem documented
- Stakeholders identified
- Decision rules recorded (experiments)

---

## Exit Condition

Proceed only when:

- Business question is clearly defined.
- Success criteria are agreed.
- For experiments, decision rules are recorded before data access.
- Project structure is complete.
- Required data has been identified.

---

# Phase 1 — Data Loading, Cleaning & Exploration

## Objective

Understand the data before attempting to answer business questions.

The purpose of exploratory work is not to produce insights.

It is to understand the evidence available.

---

## Step 1 — Acquire Data

Load data into the analytical environment.

Possible sources include:

- SQL databases
- CSV files
- APIs
- Cloud warehouses
- Excel workbooks
- Parquet files
- DuckDB
- Spark

Document:

- Source
- Extraction date
- Refresh frequency
- Ownership
- Licence and terms of use
- Original publisher, where the data was re-uploaded by someone else

### Data Provenance

When the data arrives as a file, record its SHA-256 checksum at download and check it again before every load. A matching checksum shows that the file being analysed is the same file that was documented. A loading notebook should stop if the checksum differs.

Record the checksum, file name, download date and row count in the README and the Phase 1 document.

### Raw and Clean Layers

Keep two layers of the data:

- **Raw layer.** The source loaded unchanged. When the load would otherwise convert or reject values, load every column as text so nothing is altered before it has been profiled. The raw layer is never edited.
- **Clean layer.** Built from the raw layer by a script (for example a `CREATE TABLE ... AS SELECT` statement or a notebook), with types applied and any flag columns added.

Make loads repeatable: re-running a load replaces the table rather than appending to it, so either layer can be rebuilt from the repository at any time.

---

## Step 2 — Profile the Dataset

Before modifying anything, understand the dataset.

Minimum profiling includes:

- Row count
- Column count
- Variable types
- Missing values
- Duplicate records
- Cardinality
- Target balance
- Summary statistics

---

## Step 3 — Assess Data Quality

Evaluate:

- Missing values
- Invalid values
- Outliers
- Duplicate observations
- Inconsistent categories
- Impossible combinations
- Data leakage
- Timestamp integrity

Treat each issue as an analytical investigation.

Never assume it is simply "dirty data."

---

## Step 4 — Clean the Data

Every cleaning decision must answer four questions:

1. What problem exists?
2. How common is it?
3. What action was taken?
4. Why was that action appropriate?

Cleaning actions include:

- Standardization
- Type conversion
- Deduplication
- Missing value treatment
- Outlier handling
- Feature correction

Never silently:

- delete rows,
- remove columns,
- cap values,
- impute observations.

Document every decision.

Prefer flagging unusual records with a flag column over removing them. The decision to exclude belongs in the analysis, where it can be tested as a sensitivity check.

### Reconcile Raw and Clean

After building the clean layer, compare it with the raw layer:

- Row counts
- Distinct keys
- Category counts
- Totals of numeric columns
- Counts of values that failed type conversion

Every difference must be explained by a logged cleaning decision. Record the reconciliation result in the cleaning log.

---

## Step 5 — Build Supporting Documentation

During cleaning, begin:

- Data Dictionary
- Project Glossary
- Cleaning Log
- Assumption Register

Documentation should evolve alongside the analysis—not afterward.

---

## Step 6 — Exploratory Data Analysis

Explore:

- Distributions
- Relationships
- Trends
- Segments
- Correlations
- Business patterns

The objective is to generate hypotheses—not conclusions.

---

## Deliverables

- Raw and clean data layers
- Provenance record (source, licence, checksum)
- Raw-to-clean reconciliation
- Data dictionary
- EDA notebook
- Cleaning documentation
- Initial observations

---

## Exit Condition

Proceed only when:

- Dataset quality is understood.
- Cleaning decisions are documented.
- Variables are interpretable.
- Major data risks have been identified.

---

# Phase 2 — Business Analysis

## Objective

Translate business questions into measurable analytical questions.

At this stage, focus on understanding **what happened**, **where it happened**, and **to whom it happened**.

Avoid prematurely building predictive models.

---

## Typical Activities

- KPI development
- Segmentation
- Aggregation
- SQL analysis
- Cohort analysis
- Funnel analysis
- Trend analysis
- Cross-tabulation
- Business rule evaluation

---

## Guiding Questions

Examples include:

- Which customers generate the most revenue?
- Which borrower groups default most frequently?
- Which products underperform?
- Where is revenue concentrated?
- Which operational process creates delays?

---

## Deliverables

- Business findings
- Visualizations
- Supporting SQL
- Initial recommendations

---

## Exit Condition

Proceed only when:

- Primary business questions have been answered descriptively.
- Remaining questions require deeper analytical methods.

---

# Phase 2.5 — Analytical Method Selection

## Objective

Choose the simplest analytical method capable of answering the remaining business question.

This phase exists to prevent unnecessary complexity.

Models should never be selected because they are fashionable or technically impressive.

They should be selected because they answer the question.

---

## Method Selection Framework

| Business Question | Appropriate Methods |
|-------------------|---------------------|
| What happened? | Descriptive statistics, KPIs, dashboards, SQL |
| Where is the problem? | Segmentation, cohorts, trend analysis, correlation |
| Is the difference meaningful? | Hypothesis testing, confidence intervals, ANOVA, Chi-square |
| What is likely to happen? | Predictive modelling |
| When will it happen? | Forecasting, Survival Analysis |
| Did the intervention work? | A/B Testing, Quasi-experiments |
| What happens under uncertainty? | Scenario Analysis, Monte Carlo Simulation |

---

## Decision Checklist

Before selecting a method, ask:

- What decision depends on this analysis?
- What evidence is required?
- What assumptions does this method introduce?
- Can a simpler method answer the question?
- Will stakeholders understand the results?

If the answer to the final question is "no," reconsider the approach.

---

## Deliverables

- Selected analytical method
- Method justification
- Assumption register
- Validation plan

---

## Exit Condition

Proceed only when the selected method has been justified and documented.

---

# Phase 3 — Advanced Analytics & Modelling

## Objective

Apply advanced analytical methods only when descriptive analysis cannot fully answer the business question.

---

## Typical Activities

Depending on the problem, Phase 3 may include:

### Statistical Inference

- Hypothesis testing
- Confidence intervals
- ANOVA
- Chi-square tests
- Non-parametric tests

---

### Predictive Analytics

- Logistic regression
- Linear regression
- Decision trees
- Random forests
- Gradient boosting
- Classification models

---

### Forecasting

- Time-series decomposition
- ARIMA / SARIMA
- Exponential smoothing

---

### Customer Analytics

- RFM segmentation
- Churn modelling
- Customer lifetime value
- Revenue-at-risk analysis
- Survival analysis

---

### Risk Analytics

- Credit scoring
- Probability of default
- Behavioural segmentation
- Composite risk scores

---

### Experimentation

- A/B testing
- Controlled experiments
- Difference-in-differences
- Uplift modelling

---

## Model Development Workflow

```
Business Question
        │
        ▼
Method Selection
        │
        ▼
Feature Engineering
        │
        ▼
Model Development
        │
        ▼
Validation
        │
        ▼
Business Interpretation
        │
        ▼
Recommendation
```

---

## Deliverables

- Analytical model
- Validation results
- Assumptions
- Limitations
- Business interpretation

---

## Exit Condition

Proceed only when:

- Outputs have been validated.
- Assumptions are documented.
- Limitations are understood.
- Business implications are clearly explained.

---

# Phase 4 — Reporting, Communication & Publication

## Objective

Transform analytical work into decision-ready deliverables.

A technically excellent analysis has little value if stakeholders cannot understand or act upon it.

---

## Standard Deliverables

Every completed project should include, where appropriate:

- Executive summary
- README
- Technical documentation
- SQL scripts
- Python notebooks
- Dashboards
- Data dictionary
- Visualizations
- Supporting datasets
- Presentation materials

---

## Final Quality Review

Before publication, confirm that:

- Business questions have been answered.
- Evidence supports every conclusion.
- Assumptions are documented.
- Results are reproducible.
- Documentation is complete.
- Deliverables are internally consistent.

---

## Exit Condition

The project is complete only when another analyst could reproduce the analysis and a business stakeholder could confidently act on its findings.

---

# Part III — Analytical Standards

Analytical work is more than applying statistical techniques or producing dashboards.

It is the disciplined process of selecting appropriate methods, generating reliable evidence, validating findings, and communicating conclusions at the appropriate level of certainty.

This section establishes the standards that govern analytical reasoning throughout every project.

These standards apply regardless of industry, programming language, or analytical tool.

---

# The Analytical Decision Framework

Every analysis should begin by answering one question:

> **What decision will this analysis support?**

The business decision determines:

- the analytical question,
- the evidence required,
- the method selected,
- and the confidence with which conclusions can be communicated.

The framework is intentionally sequential.

```
Business Decision
        │
        ▼
Analytical Question
        │
        ▼
Evidence Required
        │
        ▼
Method Selection
        │
        ▼
Validation
        │
        ▼
Business Recommendation
```

Skipping any step weakens every step that follows.

---

# Principle 1 — Let the Business Question Drive the Method

Methods should be selected because they answer the business question—not because they are technically sophisticated.

For example:

| Business Question | Appropriate Method |
|-------------------|--------------------|
| What happened? | Descriptive analysis |
| Where is the problem? | Diagnostic analysis |
| Is the difference meaningful? | Statistical inference |
| What will happen? | Predictive modelling |
| What happens under different assumptions? | Scenario analysis |
| Did the intervention work? | Experimental or causal analysis |

The simplest method capable of answering the question should always be preferred.

---

# Principle 2 — Separate Observation from Explanation

Data often reveals patterns.

Patterns do not automatically explain themselves.

For example:

Observed:

> Borrowers with higher revolving utilization recorded higher default rates.

Supported conclusion:

> Higher revolving utilization was associated with higher observed default rates.

Unsupported conclusion:

> Higher utilization causes borrowers to default.

Unless causal evidence exists, describe relationships—not causes.

---

# Principle 3 — Evidence Before Assumptions

Every recommendation should be traceable to analytical evidence.

Evidence may include:

- SQL output
- Summary statistics
- Statistical tests
- Predictive models
- Experimental results
- Visualizations

Whenever assumptions are introduced, they should be documented separately from observed evidence.

Readers should always know:

- what was measured,
- what was inferred,
- what was assumed.

---

# Principle 4 — Match the Strength of the Claim to the Strength of the Evidence

The certainty of analytical language should never exceed the certainty of the supporting evidence.

This playbook defines six evidence levels.

| Level | Evidence | Appropriate Language |
|--------|----------|----------------------|
| 1 | Direct observation | recorded, measured, represented |
| 2 | Group comparison | higher than, lower than |
| 3 | Association | associated with, linked to |
| 4 | Statistical inference | statistically significant |
| 5 | Prediction | predicted probability |
| 6 | Causal evidence | caused, resulted in |

Claims should never exceed the highest level supported by the analysis.

---

# Evidence Calibration Examples

| Weak Statement | Better Statement |
|----------------|------------------|
| Month-to-month contracts cause churn. | Month-to-month customers recorded the highest observed churn rate. |
| High utilization causes default. | Higher utilization was associated with higher observed default rates. |
| The campaign increased sales. | Sales increased following the campaign. Experimental analysis would be required to establish causation. |

---

# Principle 5 — Treat Data Quality as Evidence

Unexpected observations frequently reveal business issues rather than analytical problems.

Examples include:

- missing values,
- duplicated records,
- inconsistent categories,
- unexpected timestamps,
- extreme observations.

Before correcting any issue, determine whether it reflects:

- genuine business behaviour,
- operational process failure,
- data collection problems,
- or legitimate variation.

Cleaning should preserve analytical evidence whenever possible.

---

# Principle 6 — Design Metrics Before Building Models

Business decisions rely on metrics—not algorithms.

Before developing a predictive model, clearly define:

- business objective,
- success metric,
- operational definition,
- calculation method,
- interpretation,
- limitations.

A well-designed metric often delivers more business value than a sophisticated model.

---

# Business Metric Design Framework

Every important metric should answer six questions.

| Question | Example |
|----------|---------|
| What is being measured? | Customer retention |
| Why is it important? | Revenue protection |
| How is it calculated? | Retained customers / starting customers |
| What assumptions exist? | Active customer definition |
| What are the limitations? | Doesn't measure customer satisfaction |
| How will decisions change? | Identify segments requiring retention efforts |

Metrics should exist because they support decisions—not because they are easy to calculate.

---

# Principle 7 — Validate Before Interpreting

Analytical outputs should never be interpreted before they have been validated.

Validation depends on the analytical method.

Examples include:

| Analysis Type | Validation |
|---------------|------------|
| SQL | Row counts, reconciliation |
| Dashboard | Manual KPI verification |
| Statistical model | Assumption checks |
| Predictive model | Hold-out evaluation, cross-validation |
| Forecast | Back-testing |
| Experiment | Balance checks, statistical testing |

Validation is part of the analysis—not an optional final step.

---

# Principle 8 — Communicate Business Meaning

Stakeholders rarely care about statistical techniques.

They care about decisions.

Instead of reporting only:

> Accuracy = 91%.

Explain:

> The model correctly classified approximately nine out of ten historical cases and could help prioritize high-risk customers for manual review.

Every analytical result should conclude with its business implication.

---

# Analytical Thinking Across Domains

Although industries differ, many analytical problems share identical structures.

| Domain | Typical Question |
|----------|-----------------|
| Credit Risk | Which borrowers may default? |
| CRM | Which customers may churn? |
| Product Analytics | Which users may disengage? |
| Marketing | Which campaign performs best? |
| Operations | Which deliveries are most likely to be delayed? |

The variables differ.

The analytical reasoning does not.

Strong analysts recognize these transferable patterns.

---

# Standard Analytical Workflow

Every major analysis should follow the same reasoning process.

```
Business Problem

↓

Business Question

↓

Business Metric

↓

Evidence Required

↓

Method Selection

↓

Analysis

↓

Validation

↓

Interpretation

↓

Recommendation

↓

Communication
```

Each step should be documented before moving to the next.

---

# Analytical Standard

Throughout every project, continually ask:

1. What does the data show?
2. What assumptions have been introduced?
3. What evidence supports this conclusion?
4. What evidence would strengthen this conclusion?
5. What business decision becomes easier because this analysis exists?

These questions define the analytical standard expected throughout this playbook.

---

# Part IV — Communicating Analytical Work

Analysis creates value only when its conclusions are understood and acted upon.

A technically excellent model that no stakeholder trusts is less valuable than a simple analysis that supports a better business decision.

Communication is therefore part of the analytical process—not something performed after it.

---

# Communication Principles

Every analytical deliverable should satisfy five objectives.

1. Explain the business problem.
2. Present trustworthy evidence.
3. Communicate appropriate certainty.
4. Recommend practical actions.
5. Enable informed decision-making.

If a stakeholder cannot answer:

> "What should we do next?"

then the communication is incomplete.

---

# Know Your Audience

Different audiences require different levels of detail.

| Audience | Primary Interest |
|-----------|------------------|
| Executive | Decisions, risks, recommendations |
| Business Manager | KPIs, trends, business impact |
| Technical Analyst | Methods, assumptions, reproducibility |
| Data Scientist | Model performance and validation |
| Operations Team | Process improvements |
| Customers | Outcomes and implications |

Do not communicate every detail to every audience.

Scale technical depth to stakeholder needs.

---

# Selecting the Appropriate Deliverable

Choose the communication format based on the decision being supported.

| Deliverable | Purpose |
|--------------|----------|
| Dashboard | Monitor business performance |
| Executive Summary | Support strategic decisions |
| Analytical Report | Explain evidence and recommendations |
| Technical Documentation | Ensure reproducibility |
| README | Introduce the project |
| Presentation | Explain findings interactively |

Each deliverable serves a different purpose.

Avoid using one deliverable to perform the role of another.

---

# Report Standards

Analytical reports should answer three questions.

## Why was the analysis performed?

Describe:

- business context
- objectives
- analytical questions

---

## What evidence supports the conclusions?

Present:

- data
- methods
- assumptions
- analysis
- validation

---

## What should happen next?

Conclude with:

- findings
- recommendations
- limitations
- future work

---

# Standard Report Structure

```
Introduction

↓

Business Context

↓

Analytical Questions

↓

Data

↓

Methodology

↓

Analysis

↓

Results

↓

Recommendations

↓

Limitations

↓

Conclusion
```

Every section should contribute directly to the business question.

---

# Executive Summary Standard

Decision-makers should understand the project without reading the full report.

A strong executive summary includes:

- Business problem
- Key findings
- Business impact
- Recommendations

Keep technical detail to a minimum.

---

# Dashboard Standards

Dashboards should support decisions rather than display data.

Every dashboard should answer one clearly defined business question.

Examples:

- Which customers require intervention?
- Which products underperform?
- Which regions drive revenue?
- Which loans present elevated risk?

If a dashboard attempts to answer several unrelated questions, split it.

---

# Dashboard Design Principles

Every dashboard should include:

- KPIs
- supporting visualizations
- filters
- clear titles
- concise annotations

Avoid unnecessary visual complexity.

Decorative elements should never compete with analytical information.

---

# Storytelling Framework

Every analytical presentation should tell a coherent story.

Recommended structure:

```
Situation

↓

Problem

↓

Evidence

↓

Insight

↓

Recommendation

↓

Expected Business Impact
```

Avoid presenting disconnected charts.

Every visualization should advance the narrative.

---

# Presentation Standards

Before building slides, determine:

- purpose,
- audience,
- time available,
- desired decision.

Slides exist to support the presenter—not replace them.

One slide should communicate one primary idea.

---

# Slide Design Principles

Prefer:

- simple layouts,
- large readable fonts,
- high contrast,
- limited colour palette,
- one or two charts per slide.

Avoid:

- paragraphs,
- clutter,
- decorative graphics,
- excessive animation.

Every visual element should support understanding.

---

# Writing Standards

Analytical writing should be:

- precise,
- concise,
- evidence-based,
- logically structured.

Avoid:

- vague pronouns,
- unsupported claims,
- unnecessary jargon,
- filler phrases,
- overly complex sentences.

Every sentence should contribute information.

---

# Recommendation Standard

Recommendations should always answer:

1. What should be done?
2. Why?
3. What evidence supports it?
4. What business value is expected?
5. What risks or assumptions remain?

Recommendations should be practical rather than theoretical.

---

# Communicating Uncertainty

Professional analysts communicate uncertainty explicitly.

Instead of writing:

> The model will identify future churn.

Write:

> The model estimates the probability of customer churn based on historical patterns and should be interpreted alongside business judgment.

Honest communication builds trust.

---

# Communication Checklist

Before publishing any deliverable, confirm:

- □ Business objective is clear.
- □ Audience is correctly identified.
- □ Evidence supports every claim.
- □ Visualizations answer a business question.
- □ Recommendations are actionable.
- □ Limitations are documented.
- □ Technical language matches audience knowledge.
- □ Conclusions reflect the strength of the evidence.

---

# Part V — Operational Standards

Professional analytics depends on more than sound methodology.

Projects must also be reproducible, maintainable, secure, and easy for others to understand.

This section defines the operational standards that govern how analytical work is organised, documented, reviewed, and published.

---

# Repository Standards

Every project should follow a consistent directory structure.

```
project/

├── data/
│   ├── raw/
│   └── processed/
│
├── docs/
│
├── notebooks/
│
├── outputs/
│
├── sql/
│
├── tableau/
│
├── README.md
│
├── PROJECT_INFO.md
│
├── .gitignore
│
├── .env.example
│
└── requirements.txt
```

Projects should remain organised from the first commit to the final publication.

New projects are created with `tools/new_project.py` in the playbook repository. It builds this structure from the templates in `templates/`, so the playbook, the templates and the tool are versioned together. Run it with `--dry-run` first.

---

# Documentation Standards

Documentation should evolve throughout the project rather than being reconstructed at the end.

Every project should include:

```
README.md

docs/

documentation_index.md

data_dictionary.md

project_glossary.md

assumption_register.md

cleaning_log.md

tableau_blueprint.md

security_notes.md

phase_00_setup.md

phase_01_data_preparation.md

phase_02_business_analysis.md

phase_025_method_selection.md

phase_03_advanced_analysis.md

phase_04_reporting.md
```

Documentation should explain both **what** was done and **why** it was done.

## Single Source of Truth

Each fact or decision is recorded in one authoritative document. Other documents link to it instead of repeating it, so copies cannot drift apart.

| Content | Authoritative document |
|---------|------------------------|
| Business question, hypotheses, metrics, decision rules, scope, risks | `PROJECT_INFO.md` |
| Assumptions and their validation status | `docs/assumption_register.md` |
| Variables, types and valid values | `docs/data_dictionary.md` |
| Data quality issues and cleaning decisions | `docs/cleaning_log.md` |
| Terms and definitions | `docs/project_glossary.md` |
| What happened in a phase: work done, issues, results | `docs/phase_NN_*.md` |
| How to reproduce the project | `README.md` |

Phase documents record what happened during the phase and link to the charter for the decisions themselves. `PROJECT_INFO.md` → Initial Assumptions is a Phase 0 snapshot; the assumption register is the version kept up to date.

When a fact changes, update the authoritative document and check the documents that link to it.

---

# Data Dictionary Standard

The data dictionary should be created during Phase 1 and updated whenever new variables are introduced.

Each variable should include:

- Name
- Data type
- Business meaning
- Valid values (where applicable)
- Missingness
- Cleaning decisions (with a pointer to the cleaning log entry)

Engineered variables should additionally document:

- Business objective
- Creation logic
- Assumptions
- Interpretation
- Limitations

---

# Assumption Register

Every analytical assumption should be recorded explicitly.

Each assumption should include:

| Field | Description |
|-------|-------------|
| Assumption | Statement being assumed |
| Category | Business / Data / Analytical / Technical |
| Reason | Why the assumption was necessary |
| Potential Impact | How results may change if the assumption is incorrect |
| Validation Status | One of the statuses below, with the date and evidence |

Validation statuses:

| Status | Meaning |
|--------|---------|
| Untested | Not yet evaluated |
| Partially Validated | Some supporting evidence exists, but uncertainty remains |
| Validated | Evidence supports the assumption within the scope of the project |
| Rejected | Evidence shows the assumption was incorrect |
| No Longer Applicable | No longer relevant after a change in scope or method |
| Not testable | A pre-specified decision, a framing choice, or a claim the available data cannot confirm or reject. Recorded for transparency, with the reason |

A status changes only after the check has been carried out. "Not testable" is not a weaker form of "Untested": it records that no check is possible, so the limitation must be carried into the findings.

Assumptions that would change the conclusion if wrong are listed separately as high-risk, each with a mitigation plan.

Separating assumptions from observations improves transparency and helps reviewers assess analytical risk.

---

# SQL Standards

SQL scripts should be modular, readable, and reproducible.

Recommended naming convention:

```
00_setup.sql

01_data_preparation.sql

02_business_analysis.sql

03_feature_engineering.sql

04_validation.sql
```

Each SQL script should begin with:

- Project
- Phase
- Purpose
- Author
- Last Updated
- Status

Comment SQL by the same standard as Python code (see Code Comment Standard below).

Where appropriate, use:

- indexes
- views
- stored procedures
- transactions
- execution plans
- query optimisation

Optimise queries only after correctness has been established.

---

# Python Standards

Each notebook should represent one major analytical phase.

Recommended structure:

```
Introduction

↓

Imports

↓

Configuration

↓

Data Loading

↓

Analysis

↓

Validation

↓

Outputs
```

General principles:

- Explain reasoning with Markdown before code.
- Use descriptive variable names.
- Keep notebooks reproducible.
- Avoid hidden state.
- Load secrets from `.env`.
- Never overwrite raw data.

Code should communicate intent as clearly as results.

## Notebook Header Standard

Every notebook opens with one Markdown cell:

```markdown
# [Project Title]

## [Project Subtitle]

**Notebook:** NN_name.ipynb  
**Phase:** N — [Phase name]  
**Source:** [Dataset name, file, row count and original publisher]  
**Author:** [Name]  
**Date:** YYYY-MM-DD  

## [Notebook purpose as a heading]

[One paragraph: what this notebook does, what it reads and what it produces.]
```

The header lets a reader identify the notebook, its phase and its data without running it. Keep step numbers from external workflow documents out of the header, since those documents are not part of the repository.

## Code Comment Standard

Comments explain **why** a step is done and what non-obvious calls do. They do not repeat what the code already says.

- Comment each import with what it is used for.
- Comment settings and constants with where the value comes from (for example, how an expected row count was confirmed).
- Explain parameters whose effect is not obvious from their name (for example, a load job's write disposition).
- Explain each check: what it tests and what a failure would mean.
- In SQL, give each query a numbered heading comment stating the question it answers.
- Where a tool or service is used for the first time in a project, explain the concept briefly, so a reader new to it can follow.

A reader who has not seen the project should be able to follow the code from the comments and Markdown alone.

---

# Dashboard Standards

Dashboards should answer one primary business question.

Each dashboard should contain:

- KPI summary
- Supporting charts
- Interactive filters
- Clear titles
- Business commentary
- Navigation (where multiple dashboards exist)

Every visual should support a decision.

If a chart does not influence understanding or decision-making, remove it.

---

# File Naming Standards

## SQL

```
00_setup.sql

01_cleaning.sql

02_customer_segmentation.sql

03_churn_analysis.sql

04_validation.sql
```

---

## Python

```
01_data_loading.ipynb

02_cleaning.ipynb

03_analysis.ipynb

04_modelling.ipynb
```

---

## Outputs

```
outputs/

chart_default_rate.png

table_customer_summary.csv

sql_risk_segments.csv
```

---

## Processed Data

```
processed/

customers_clean.csv

customers_features.csv

customers_final.csv
```

Consistent naming improves collaboration and reproducibility.

---

# Version Control Standards

Version control should document analytical progress rather than simply storing files.

Recommended commit style:

```
feat:

fix:

docs:

refactor:

test:
```

Examples:

```
feat: build customer segmentation logic

docs: update cleaning log

fix: correct missing value treatment

refactor: optimise SQL joins
```

## Branching Strategy

Work on new phases, features, or extensions should happen on a
dedicated branch — never directly on `main`.

This keeps `main` permanently in a clean, portfolio-ready state,
regardless of whether the repository is public or private.
Repository visibility controls who can see the repo; it does not
clean up commit history. Branching does.

Standard flow:

1. Create a feature branch before starting new work:
   `git checkout -b phase-N-description`
2. Commit normally while working on the branch.
3. Push the branch: `git push -u origin phase-N-description`
4. Open a Pull Request to merge into `main` once the work is
   complete and reviewed.
5. Squash commits during merge where useful, so `main` reflects
   one clean, descriptive commit per completed unit of work.

Recommended branch naming:

```
phase-7-inference-prediction
fix-tableau-color-mapping
docs-update-data-dictionary
```

`main` should always represent the current, complete, working
state of the project.

Commit messages should explain **why** the change was made.

---

# Reproducibility Standard

Another analyst should be able to reproduce the project using only:

- repository contents,
- documentation,
- raw data,
- dependency list,
- and project instructions.

Projects requiring undocumented manual steps are not considered reproducible.

---

# Security Standards

Never commit:

- passwords
- API keys
- database credentials
- access tokens
- confidential client data

Use:

- `.gitignore`, including credential file patterns (`*.pem`, `*.key`, service account JSON files)
- `.env` for local settings, with a committed `.env.example` that lists the variable names only
- the platform's own login (for example, application default credentials) instead of key files in the project folder
- anonymised datasets
- secure credential storage

Security is part of analytical professionalism.

---

# Quality Assurance

Before publication, verify:

## Analysis

- □ Business question answered
- □ Appropriate analytical method selected
- □ Assumptions documented
- □ Evidence supports conclusions
- □ Validation completed

---

## Code

- □ SQL executes without errors
- □ Notebooks run from top to bottom
- □ No hidden dependencies
- □ No temporary code remains

---

## Documentation

- □ README updated
- □ Data dictionary complete
- □ Cleaning log complete
- □ Assumption register complete
- □ Documentation index updated

---

## Dashboard

- □ KPIs verified
- □ Visuals consistent with analysis
- □ Filters functioning
- □ Business commentary accurate

---

## Repository

- □ Folder structure organised
- □ Credentials removed
- □ `.gitignore` verified
- □ Outputs exported
- □ Final datasets saved

---

# Standard Deliverables

Every completed analytics project should include, where appropriate:

- README
- SQL scripts
- Python notebooks
- Raw data
- Processed datasets
- Dashboard
- Dashboard screenshots
- Executive summary
- Data dictionary
- Assumption register
- Cleaning log
- Project glossary
- Technical documentation
- Presentation materials

Deliverables should reflect the needs of the intended audience.

---

# Portfolio-to-Workplace Mapping

| Portfolio | Workplace Equivalent |
|------------|----------------------|
| README | Executive Summary |
| Repository | Project Workspace |
| Notebook | Analytical Workbook |
| Dashboard | BI Report |
| Documentation | Technical Documentation |
| Business Questions | Stakeholder Requirements |
| Deliverables | Sprint Deliverables |
| Findings | Business Recommendations |

The terminology changes.

The analytical process does not.

---

# Lessons Learned

Across projects, several recurring lessons have emerged.

- Data quality issues often reveal business problems.
- Missing values may contain valuable information.
- Outliers deserve investigation before removal.
- Simple methods often answer business questions more effectively than complex ones.
- Documentation is as important as analysis.
- Reproducibility builds trust.
- Validation should precede interpretation.
- Communication determines whether analytical work creates business value.

These lessons should influence future projects unless new evidence suggests otherwise.

---

# Continuous Improvement

This playbook is a living document.

Whenever a project introduces:

- a better analytical method,
- a stronger documentation practice,
- an improved workflow,
- a reusable validation procedure,
- or a clearer communication technique,

the playbook should be updated and the change recorded in the Version History.

Continuous improvement should be intentional rather than reactive.

The objective is not to build a perfect process.

The objective is to build a better process with every project.

---

# Final Principle

Professional analytics is not defined by the complexity of its models.

It is defined by the consistency of its thinking.

A professional analyst:

- understands the business problem,
- selects an appropriate method,
- documents assumptions,
- validates results,
- communicates honestly,
- and supports better decisions.

That standard—not any individual tool, programming language, or statistical technique—is the foundation of this playbook.
