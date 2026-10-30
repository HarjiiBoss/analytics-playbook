# Phase 0 — Scoping & Project Setup

This document records what was done and decided during Phase 0. The scoping decisions themselves (business question, hypotheses, metrics, decision rules, scope, risks and assumptions) are kept in [PROJECT_INFO.md](../PROJECT_INFO.md) so they exist in one place only.

<!-- Record what happened here and link to PROJECT_INFO.md for the decisions. Do not copy charter content into this file. -->

---

# Phase Status

| Field | Value |
|--------|-------|
| Status | Not Started |
| Started | |
| Completed | |
| Owner | {{AUTHOR}} |
| Branch | `phase-0-scoping` |

---

# Decisions Made

<!-- One row per decision. State the decision in one line and point to the section of PROJECT_INFO.md that holds it. -->

| Decision | Where it is recorded |
|----------|----------------------|
| | PROJECT_INFO.md → |

<!-- For experiments, state whether all decision rules were set before the dataset was downloaded or examined. -->

---

# Environment Setup

| Component | Setting |
|-----------|---------|
| Repository | `{{PROJECT_SLUG}}`, created with `new_project.py` from Playbook v{{PLAYBOOK_VERSION}} |
| Branching | Work on `phase-N-description` branches, merged into `main` by pull request |
| Python | Version in a project virtual environment (`.venv`), packages from `requirements.txt` |
| Database / warehouse | |
| Authentication | |
| Configuration | `.env` (not committed) holds local settings. `.env.example` is committed as a template |
| Connection test | |

---

# Issues and Resolutions

<!-- Problems met during setup and how each was resolved. Delete the row if there were none. -->

| Issue | What happened | Resolution |
|-------|---------------|------------|
| | | |

---

# Concept Notes

<!-- Short explanations of concepts used for the first time in this project, written for a reader who has not met them. Delete this section if not needed. -->

---

# Methods Explained

<!-- The reasoning behind this phase's choices, written for a reviewer such as a hiring manager or a client's analyst (Playbook Part V → Reasoning in the Project Files). One block per method, rule or definition; state each point once, plainly. This is a decision record, not a tutorial: background on how a method works belongs in financial-model-foundation. Delete the example block if the phase used none. -->

### [Method, rule or definition]

- **Decision:** what was used, with its settings
- **Alternatives considered:** and why they were not used
- **How to read the result:** what the output means for the business question, and its limits

---

# Exit Checklist

## Business

- [ ] Business problem clearly defined
- [ ] Business question documented
- [ ] Success criteria agreed
- [ ] Stakeholders identified
- [ ] Project scope established
- [ ] Decision rules set before data access (experiments)
- [ ] Analysis rules set before any outcome data, each with its reason (observational projects)

## Data

- [ ] Required dataset identified
- [ ] Data ownership and licence confirmed
- [ ] Data availability verified

## Technical

- [ ] Repository structure created
- [ ] Development environment configured
- [ ] Version control initialised and pushed
- [ ] Database connection verified

## Documentation

- [ ] PROJECT_INFO.md completed
- [ ] README initialised
- [ ] Phase documentation updated
- [ ] Assumption register started
- [ ] Security notes started
- [ ] Methods Explained filled in for every method, rule or definition used in this phase
- [ ] `python3 tools/check_phase.py 0` passes

---

# Phase Outcome

<!-- Two to four sentences: what Phase 0 settled and whether the project is ready for Phase 1. Note any checklist item moved to a later phase and why. -->
