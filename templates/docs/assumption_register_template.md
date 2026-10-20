# Assumption Register

This register tracks every significant assumption in the project, from when it is made until it is validated, revised or retired. The Phase 0 snapshot is in [PROJECT_INFO.md](../PROJECT_INFO.md) → Initial Assumptions; this register is the version kept up to date. A status changes only after the check has actually been carried out.

<!-- Keep assumptions separate from observations. Each status entry gives the date and the evidence, for example the query or notebook cell that checked it. -->

| ID | Assumption | Category | Reason | Phase | Potential Impact | Validation Status | Owner |
|----|------------|----------|--------|-------|------------------|-------------------|-------|
| A-001 | | | | | | Untested | {{AUTHOR}} |

<!-- Category: Business, Data, Analytical or Technical. -->

---

# High-Risk Assumptions

<!-- Assumptions that would change the conclusion or recommendation if wrong. -->

| ID | Reason for High Risk | Mitigation Plan |
|----|----------------------|-----------------|
| | | |

---

# Validation Status Definitions

| Status | Meaning |
|---------|---------|
| Untested | The assumption has not yet been evaluated. |
| Partially Validated | Some supporting evidence exists, but uncertainty remains. |
| Validated | Evidence supports the assumption within the scope of the project. |
| Rejected | Evidence indicates the assumption was incorrect. |
| No Longer Applicable | The assumption is no longer relevant due to changes in scope or analysis. |
| Not testable | A pre-specified decision or framing that data cannot confirm or reject. Recorded for transparency. |

---

# Review Checklist

Before completing the project, confirm:

- [ ] Every major assumption has been documented.
- [ ] Assumptions are clearly distinguished from observations.
- [ ] Validation status has been updated where applicable.
- [ ] High-risk assumptions have been identified.
- [ ] Business recommendations acknowledge any unresolved assumptions.
