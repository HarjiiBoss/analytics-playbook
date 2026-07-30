# Data Analysis Playbook
### A Personal Standard Operating Procedure for End-to-End Analytics Projects

**Author:** Taofeek Salami  
**First Formalized:** July 2026 (Project 08 — Fintech Credit Risk Analysis)  
**Version:** 2.0  
**Purpose:** Establish a repeatable, well-documented workflow for approaching any analytics project—from portfolio work to production environments. This playbook is tool-agnostic and can be applied across industries, datasets, and business domains.

---

# Version History

| Version | Date | Change |
|---|---|---|
| 1.0 | July 2026 | Initial playbook — five-phase workflow, core analysis principles, technical and documentation standards |
| 2.0 | July 2026 | Added the Analytical Language & Evidence Standards section  |
| 2.1 | July 2026 | Added the Report Structure & Prose Standards |
| 2.2 | July 2026 | Added the Oral Presentation Planning |

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

## Phase 3 — Advanced Analysis & Analytical Modelling

### Objective

Develop higher-level analytical outputs when the business question requires analysis beyond basic descriptive summaries.

Possible activities include:

- Composite scores
- Behavioral segmentation
- Financial indices
- Feature engineering
- Statistical inference
- Predictive modelling
- Forecasting
- Experimental evaluation

Not every project requires every technique.

The method should be selected based on the analytical question, data structure, and evidence required.

### Exit Condition

Advanced outputs are:

- Methodologically justified
- Reproducible
- Validated where possible
- Clearly documented
- Interpreted at the appropriate level of certainty

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

**See the [Analytical Language & Evidence Standards](#analytical-language--evidence-standards) section below for the full framework governing how to calibrate insight language to the strength of the underlying evidence.**

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

# Analytical Language & Evidence Standards

A strong data analyst does not only calculate the correct numbers. They also describe those numbers at the level of certainty the analysis actually supports.

The strength of the language used in an insight must match the strength of the evidence behind it.

---

## 1. Separate Association from Causation

When an analysis compares two variables or groups, it may reveal a relationship between them. However, a relationship does not automatically prove that one variable caused the other.

For example, if a dataset shows:

- Customers on month-to-month contracts churn at a higher rate.
- Borrowers with higher utilization have higher observed default rates.
- A particular region generates a large share of revenue.
- A route has both high maintenance costs and poor profitability.

The analysis has identified an observed relationship or pattern.

It has not necessarily proven that:

- Month-to-month contracts cause churn.
- High utilization causes default.
- The region causes the business to become dependent on it.
- Maintenance costs cause the route to become unprofitable.

Unless the analysis uses an appropriate statistical, experimental, or causal methodology, causal language should be avoided.

### Core Principle

> **Describe what the data demonstrates, not what the analyst assumes caused it.**

---

## 2. Use Evidence-Calibrated Language

The language used in a business insight should reflect the analytical method used to produce it.

### When reporting a direct observation

Use:

- `recorded`
- `observed`
- `measured`
- `represented`
- `accounted for`
- `contained`
- `generated`

Example:

> Borrowers with zero open credit lines recorded the highest observed default rate at 25.64%.

This is a direct descriptive finding.

---

### When describing a relationship or pattern

Use:

- `associated with`
- `corresponded with`
- `was linked to`
- `coincided with`
- `was observed among`
- `was more common among`
- `showed a relationship with`
- `was concentrated in`

Example:

> Higher revolving utilization was associated with higher observed default rates.

This communicates a relationship without claiming that one variable caused the other.

---

### When describing concentration

Use:

- `concentrated in`
- `dominated by`
- `accounted for a disproportionate share of`
- `was heavily dependent on`
- `represented the majority of`
- `was disproportionately represented in`

Example:

> Revenue was heavily concentrated in the UK, which accounted for 84.42% of total revenue.

This is stronger and more accurate than saying:

> The UK drives revenue.

The word "drives" may imply a causal mechanism that the analysis has not established.

---

### When describing a business risk

Use:

- `creates exposure to`
- `represents a concentration risk`
- `signals potential risk`
- `warrants further investigation`
- `may indicate`
- `could expose the business to`
- `is a potential vulnerability`

Example:

> The concentration of revenue in one market creates geographic exposure and represents a potential concentration risk.

This is more analytically defensible than:

> The UK causes geographic risk.

---

## 3. A Practical Causation Language Test

Before writing an insight, ask:

> **Could another factor explain the observed relationship?**

If the answer is yes, causal language should be avoided unless the analysis has specifically controlled for those alternative explanations.

For example:

### Observed data

| Contract Type | Churn Rate |
|---|---:|
| Month-to-month | 42% |
| One year | 11% |
| Two year | 3% |

### Weak conclusion

> Month-to-month contracts cause customers to churn.

### Evidence-calibrated conclusion

> Month-to-month customers recorded the highest churn rate, indicating a strong association between contract structure and observed churn risk.

### Stronger statistical conclusion

> After controlling for tenure, service type, and customer demographics, contract type remained a statistically significant predictor of churn.

The third conclusion requires a much stronger analytical method than the first two.

---

## 4. When Statistical Modelling Is Actually Necessary

Statistical modelling should not be added simply to make a project appear more advanced.

The analytical method should be selected based on the business question.

### Descriptive questions

> What happened?

Use:

- Counts
- Sums
- Averages
- Percentages
- Rates
- KPIs
- Group comparisons
- Trend analysis

Examples:

- What was the total revenue?
- Which category had the highest loss rate?
- Which borrower segment had the highest default rate?

No statistical model is necessarily required.

---

### Diagnostic questions

> Where is the problem, and what patterns are associated with it?

Use:

- Segmentation
- Cohort analysis
- Cross-tabulation
- Correlation analysis
- Trend analysis
- Outlier analysis
- Comparative analysis

Examples:

- Which customer groups have the highest churn?
- Which routes have poor profitability?
- Which borrower characteristics are associated with higher observed default rates?

A model may be useful, but it is not automatically required.

---

### Inferential questions

> Is the observed difference likely to represent a meaningful difference beyond random variation?

Use methods such as:

- Hypothesis testing
- Confidence intervals
- t-tests
- Chi-square tests
- ANOVA
- Non-parametric tests

Example:

> Did the treatment group perform significantly better than the control group?

This is where statistical testing becomes relevant.

---

### Predictive questions

> Can we predict what is likely to happen next?

Use methods such as:

- Linear regression
- Logistic regression
- Time-series forecasting
- Decision trees
- Other predictive models

Examples:

- Which customers are most likely to churn?
- What is the expected sales volume next month?
- Which borrowers are most likely to default?

Prediction requires a model because the question moves beyond describing the existing data.

---

### Causal questions

> Did X cause Y?

This requires the strongest evidence.

Possible approaches include:

- Randomized experiments
- A/B testing
- Difference-in-differences
- Controlled experiments
- Quasi-experimental methods
- Carefully designed causal inference methods

Example:

> Did the new store layout cause sales to increase?

This was the type of question explored in the Quantium project through trial-store and control-store comparisons.

---

## 4.1 The Method Selection Decision Framework

Before selecting an analytical method, identify the type of question being asked.

### Question 1 — Am I describing what already happened?

Examples:

- What was total revenue?
- Which segment had the highest churn?
- How many borrowers defaulted?
- Which category had the highest margin?

Use:

- Descriptive statistics
- Aggregations
- Group comparisons
- Rates and percentages
- Dashboards

Statistical modelling is usually unnecessary.

---

### Question 2 — Am I investigating where a pattern or problem exists?

Examples:

- Which customers are most exposed to churn?
- Which borrower segments have higher observed default rates?
- Which routes have poor profitability?
- Where is revenue concentrated?

Use:

- Segmentation
- Cross-tabulation
- Cohort analysis
- Correlation analysis
- Trend analysis
- Outlier analysis

Statistical modelling may be useful, but is not automatically required.

---

### Question 3 — Am I asking whether a difference is statistically meaningful?

Examples:

- Is the difference between two groups likely to be more than random variation?
- Did the treatment group outperform the control group?
- Is there evidence of a meaningful difference between regions?

Use:

- Hypothesis testing
- Confidence intervals
- t-tests
- Chi-square tests
- ANOVA
- Non-parametric tests

This is where inferential statistics become appropriate.

---

### Question 4 — Am I trying to predict an unknown or future outcome?

Examples:

- Which customer is likely to churn?
- What will next month's revenue be?
- Which borrower is likely to default?

Use:

- Logistic regression
- Linear regression
- Decision trees
- Random forests
- Gradient boosting
- Time-series forecasting

A predictive model is required because the question is about estimating an unknown outcome.

---

### Question 5 — Am I asking whether an intervention caused an outcome?

Examples:

- Did the new store layout increase sales?
- Did the pricing change improve conversion?
- Did the retention campaign reduce churn?

Use:

- Randomized experiments
- A/B testing
- Difference-in-differences
- Matched control designs
- Quasi-experimental methods

Causal language requires a design capable of addressing alternative explanations.

---

### The Rule

> **Do not choose a method because it is technically impressive. Choose it because it answers the question being asked.**

---

## 5. The Portfolio Standard

Every project does not need statistical modelling.

A strong Data Analyst portfolio should demonstrate that the analyst can:

1. Understand the business question.
2. Select an appropriate analytical method.
3. Clean and validate the data.
4. Calculate meaningful metrics.
5. Identify patterns and risks.
6. Communicate findings clearly.
7. Match the certainty of the conclusion to the strength of the evidence.

The goal is not:

> "Use the most advanced method available."

The goal is:

> **Use the simplest method that answers the business question reliably.**

A descriptive business question does not require a regression model.

A predictive question requires predictive modelling.

A causal question requires an appropriate causal design.

---

## 6. The Evidence & Claim Calibration Framework

The following hierarchy should guide the strength of analytical language:

### Level 1 — Direct observation

> "Segment A recorded a 25.64% default rate."

Evidence:

- Descriptive statistics

---

### Level 2 — Group comparison

> "Segment A had a higher default rate than Segment B."

Evidence:

- Comparative analysis

---

### Level 3 — Association

> "Higher utilization was associated with higher observed default rates."

Evidence may include:

- Correlation analysis
- Cross-tabulation
- Structured group comparisons
- Regression analysis used for association rather than causal identification

The method should match the data structure and business question.

---

### Level 4 — Statistical inference

> "The difference was statistically significant."

Evidence:

- Appropriate statistical test

---

### Level 5 — Prediction

> "The model predicts that this customer has a high probability of churn."

Evidence:

- Validated predictive model

---

### Level 6 — Causation

> "The intervention caused the observed increase in sales."

Evidence:

- Experimental or credible causal design

---

### Rule

> **Do not use Level 6 language when your evidence only supports Level 1, 2, or 3.**

---

## 7. Applying This to the Portfolio

The current portfolio contains different types of analytical work.

The appropriate standard is therefore not to force every project to use statistical modelling.

For example:

### Fintech Credit Risk

Appropriate:

> Higher utilization was associated with higher observed default rates.

Avoid:

> Higher utilization causes borrowers to default.

---

### Telco Churn

Appropriate:

> Month-to-month customers recorded the highest churn rate.

Avoid:

> Month-to-month contracts cause churn.

---

### Superstore

Appropriate:

> Furniture generated $5.18M in sales but recorded only a 2.3% margin.

Avoid:

> High sales volume causes low profitability.

---

### Logistics

Appropriate:

> The fleet recorded a 55.7% on-time rate, materially below the stated benchmark.

Avoid:

> Poor driver performance causes the low on-time rate.

---

### Quantium Data Analytics

Because the project compared trial stores against matched control stores, it used a quasi-experimental evaluation framework.

The analysis can support stronger claims about the relationship between the trial intervention and observed sales uplift than a simple descriptive comparison.

However, causal conclusions still depend on assumptions including:

- The control store was a credible counterfactual.
- The trial and control stores followed sufficiently similar pre-intervention trends.
- No major external event affected the stores differently during the trial period.
- The observed uplift was not driven by another simultaneous intervention.

Therefore, the strength of the causal claim should reflect the quality of the control design and validation performed.

---

## Final Playbook Principle (Language & Evidence)

> **Methodology should follow the question.**
>
> Do not add statistical modelling merely because it appears sophisticated.
>
> Do not make causal claims merely because two variables move together.
>
> Use descriptive analysis to describe.
>
> Use comparative analysis to compare.
>
> Use statistical inference to test.
>
> Use predictive modelling to predict.
>
> Use experimental or causal methods to evaluate cause and effect.

A professional analyst is not the person who uses the most complicated method.

A professional analyst is the person who can explain:

> **What does the data show?**
>
> **What does it suggest?**
>
> **What does it not prove?**
>
> **What additional analysis would be required to make a stronger claim?**

---

# Report Structure & Prose Standards

A well-calibrated insight can still fail to land if it's buried in the wrong report type, poorly structured, or written imprecisely. This section governs the *container* the analysis goes in — separate from the *evidence-calibration* rules that govern the language of the insight itself.

---

## 1. Choose the Right Report Type

Before writing, classify the report along two independent axes.

### Axis A — Content type

| Type | Purpose | Structure | Length |
|---|---|---|---|
| **Informational** | States facts only, no analysis | No strict structure | Usually short |
| **Analytical** | Includes analysis, relationships, recommendations | Strict structure (see below) | Varies |

### Axis B — Depth

| Type | Purpose | Audience | Length |
|---|---|---|---|
| **Final report** | Full technical detail, methods, visuals | Technical stakeholders who need to validate the work | Long |
| **Summary report** | Key findings + recommendations, links back to the final report | Decision-makers who don't need technical detail | Short — under 5 pages |

### Default for this portfolio

Almost every project here (Telco, Fintech, Superstore, Logistics, Quantium) is **analytical** work aimed at a **decision-maker** audience. Default assumption going forward:

> **Produce a summary analytical report as the primary deliverable, with the notebook/SQL/dashboard serving as the "final report" backup for technical readers who want to validate the work.**

Only build a full final-report writeup when a technical stakeholder is the explicit audience.

---

## 2. Standard Report Structure

For any analytical (final or summary) report, follow this structure:

### Introduction
- **Purpose** — one or two sentences on what the report shows.
- **Context** — what motivated the analysis (e.g. "an increase in negative reviews," "a rise in defaulting customers over 5 years").
- **Analysis question(s)** — the specific question(s) being answered.

### Body
- **Data** — description of the most relevant data used; tables where helpful.
- **Method** — how the data was gathered/analyzed and which model or technique was used.
- **Analysis** — selected data/model shown via visuals (e.g. distribution of key variables).
- **Results** — the actual findings, described and explained, with supporting visuals.

### Conclusion
- Restate the analysis question(s).
- Summarize the most important results.
- State recommendations for next steps.

**Note:** a *summary* report keeps Data down to essentials and puts most of the weight on Results and Recommendations, with a link to the full notebook/dashboard for anyone who wants the Method/Analysis detail.

---

## 3. Sizing Rule — the 1-3-25 Approach

For business-context reports (as opposed to academic/journal-style reports), size the document as:

- **1 page** — abstract
- **3 pages max** — executive summary (findings + recommendations)
- **25 pages max** — full detail

The executive summary alone should be enough for a reader to understand the conclusions and decide whether the full report is worth reading.

---

## 4. Match the Report to How the Audience Actually Reads It

| Reader type | Reading pattern | What to front-load for them |
|---|---|---|
| Time-limited but interested | Reads intro + conclusion, scans body for specific points | Make intro/conclusion self-contained |
| Executive / decision-maker | Skims intro + conclusion looking for recommendations | Recommendations must be visible without reading the body |
| Technical stakeholder | Focuses on the body | Method/Analysis sections must be complete enough to validate the work |

Practical implication: **write the conclusion and recommendations first, then work backward** — if those two sections can't stand alone, the report isn't done yet.

---

## 5. Prose & Clarity Checklist

This governs sentence-level writing quality — distinct from the Evidence Ladder rules, which govern the *certainty* of a claim. A claim can be perfectly evidence-calibrated and still be badly written. Check every report draft against these five rules:

### a. Cut empty phrases
Phrases that add no information should be removed outright: *"it is interesting to note that," "the fact that," "it should be pointed out that," "it is well known that," "it is obvious that."*

> Weak: *It is interesting to note that the model shows an accuracy of 80%.*
> Better: *The model shows an accuracy of 80%.*

### b. Use concrete nouns, not vague pronouns
Avoid overusing "this," "that," "it" when the referent isn't immediately clear — it adds cognitive load and can be genuinely ambiguous.

> Weak: *This shows an accuracy of 80% when predicting customer churn.*
> Better: *The model shows an accuracy of 80% when predicting customer churn.*

### c. Prefer active voice in business reports
Passive voice is standard in academic writing but reads as stuffy and indirect in a business report. Active voice puts the emphasis on the finding, not on hedging around who found it.

### d. Cut redundant adjectives and adverbs
Filler modifiers used for emphasis add words without adding meaning: *"the new," "done previously,"* etc. Remove them to keep the report concise.

### e. Fix run-on sentences
A run-on is two or more independent clauses connected or punctuated incorrectly (commonly joined by a comma where they shouldn't be). Fix by either:
- splitting into two separate sentences, or
- properly subordinating with a connector like *because* or *so*.

---

# Oral Presentation Planning

Just as it's a mistake to start writing code before deciding what the analysis needs to answer, it's a mistake to start writing slides before planning the presentation. Before opening a deck tool, decide: **purpose, audience, message, structure, outline** — in that order.

---

## 1. Define the Purpose

Classify the presentation as one of three types before deciding content:

| Purpose | Goal | Example |
|---|---|---|
| **Informative** | Share current findings/facts | Report current negative/positive rating split and the words associated with negative reviews |
| **Instructional** | Teach colleagues how something was built | Explain how the sentiment analysis model was built |
| **Persuasive** | Convince stakeholders to act | Convince stakeholders that action is needed on the volume of negative ratings |

The purpose determines depth and content — an instructional deck leans into method; a persuasive deck leans into impact and recommendation.

---

## 2. Define the Audience — Role and Size

Two separate dimensions to plan for:

**Role** — technical colleague, manager/executive, or customer. Determines vocabulary and how much methodology to show.

**Size/setting** — determines pacing, interactivity, and depth:

| Setting | Example |
|---|---|
| Small meeting | ~10 people, e.g. the finance team |
| Large meeting/conference | ~100 people, e.g. a software dept. all-hands |
| Workshop/training | ~30 people, hands-on technical training for a customer's team |

---

## 3. Decide the Message — Before Building Any Slides

Assumption to plan around: **the audience will forget ~90% of the presentation within a week.** So decide the one thing they should retain first, then work backward to decide what the deck needs to include to get them there.

Three components, decided in this order:

1. **Opening statement** — hooks the audience and previews the one takeaway. *e.g. "Negative ratings are scaring customers away from our website."*
2. **Central message** — one sentence, the single thing the whole deck exists to support. *e.g. "Delayed shipping is the main cause of negative reviews, and immediate action is needed."*
3. **Closing statement** — restates the arc and reinforces the central message. *e.g. "Sales are down. Negative reviews are climbing. Delayed shipping is the driver. Action is needed now."*

Do not proceed to structure/outline until this one sentence exists.

---

## 4. Structure

| Section | Content | Notes |
|---|---|---|
| **Introduction** | Background info, hook, glimpse of what's coming | Sets the opening statement |
| **Methods / Analysis / Model outputs** | Technical detail | Depth scales to audience — **can be skipped entirely for non-technical audiences** |
| **Conclusion** | Ties back to the introduction, call-to-action or next-step recommendations | Reinforces the central message |

Attention is highest at the beginning and end — this structure is built to exploit that, not fight it.

---

## 5. Outline — Section Count and Timing

- Aim for **~5 sections**, no more. Too many sections dilutes attention.
- Typical shape (adapt names to the project): reason for the analysis → exploratory analysis → core analysis/model → conclusions → follow-up actions.
- **Time budget drives scope, not the reverse** — decide how long you have before deciding how much to include, not after the deck is built.

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

Stronger use case of the following in SQL where necessary. 

- indexes
- query optimization
- execution plans
- views
- stored procedures
- transactions

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
- [ ] Insight language matches the Evidence Ladder level actually supported by the analysis.
- [ ] Report type (informational/analytical, final/summary) matches the actual audience and content.
- [ ] Report follows the standard Introduction → Body (Data/Method/Analysis/Results) → Conclusion structure.
- [ ] Executive summary alone (1-3 pages) is sufficient for a decision-maker to act.
- [ ] Prose checked against the Clarity Checklist (empty phrases, vague pronouns, active voice, redundant modifiers, run-on sentences).
- [ ] Presentation purpose (informative / instructional / persuasive) is explicit before slides are built.
- [ ] Audience role and setting size are identified and content is scaled accordingly.
- [ ] A single central message sentence exists before slide-building starts, with matching opening/closing statements.
- [ ] Methods/Analysis depth is scaled to (or skipped for) a non-technical audience.
- [ ] Deck has ~5 sections max, sized to the actual time slot.

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
- **The strength of the language used to describe a finding must match the strength of the evidence behind it — a well-calculated number can still be misrepresented by an overclaiming sentence.**

---

# Continuous Improvement

This playbook is intended to evolve.

Whenever a project introduces a new analytical technique, documentation practice, or workflow improvement worth repeating, update this document — and log the change in the **Version History** table at the top of this file.

The objective is not to create a perfect process—it is to build a better one with every project completed.
