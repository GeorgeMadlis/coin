---
type: Event
title: "Round 20: observer ontology and recording-function audit"
description: Observer theory audit completed; observer/observation, actor/observer identity, and Git-backed recording substrate clarified.
fc-axis: INQUIRY
fc-round: 20
fc-move: evidence
fc-stage: enrichment
fc-party: codex
fc-touches: [answer.md, agent-contract.md, s/overview.md, s/method.md, s/specification.md, s/foundations/wolfram-observer-theory.md, r/results.md, log.md, inquiry/index.md]
fc-status: open
timestamp: 2026-08-16
---

# Move

The observer-theory foundation was critically audited against primary Wolfram
sources, the current formal model, the repository implementation, and the
framework-self reconstruction record. The audit tests rather than simply
confirms the prior theory.

# Evidence added

- `docs/observer-theory-audit.md` records the search inventory, Wolfram
  attribution audit table, observer ontology decision, formal-model decision,
  reconstruction experiment, corrected recording-function interpretation, and
  bundle-identity rule.
- Primary Wolfram sources inspected for attribution boundaries: "Observer
  Theory" (2023), "The Concept of the Ruliad" (2021), "Exploring Rulial
  Space" (arXiv:2101.10907), "On the Nature of Time" (2024), "Computational
  Foundations for the Second Law of Thermodynamics" (2023), *A New Kind of
  Science* chapter 12 section 6, and the 2024 biological-evolution analogy.
- Repository implementation checked under `tools/src/okf_fc/` and
  `tools/tests/`.
- Reconstruction test checked `s/method.md` and `r/results.md` against the
  current bundle tree, Git history, and published framework-self snapshots.

# Effect on state

Context window: expanded to include the explicit audit table, search inventory,
Wolfram source recheck, and reconstruction experiment.

Frame: narrowed and corrected. The framework now distinguishes observer
processes from observations/outputs; actor identity from theoretical observer
identity; observer instances/runs from observer families; and current bundle
projection from Git/snapshot-backed historical materialization. The static
`O_i = (C_i, f_i)` model is retained for cross-sections, with optional dynamic
state notation only when persistence, memory, context drift, or feedback is
material.

# Resulting revisions

- `docs/observer-theory-audit.md` is added as the repository-level audit
  record.
- `docs/framework_v3.md` is revised to qualify Wolfram attribution, add the
  observer/observation distinction, clarify participation as feedback, and
  correct the recording-function claim.
- `docs/formal-core.md` is revised to add observer process, observation/output,
  instance/run, family, record, and participation categories; retain
  `O_i = (C_i, f_i)` as the static model; and add minimal dynamic state
  notation.
- `docs/glossary.md` is revised to separate observer process, observation,
  observer instance, observer family, and actor identity.
- `spec/SPEC.md` is revised to profile 0.1.2, separating actor identity from
  observer identity and requiring reconstruction claims to identify whether
  they rely on current tree, Git history, snapshots, or explicit archived
  concepts.
- `tools/src/okf_fc/foundation.py`, `tools/src/okf_fc/validate.py`, and
  `tools/README.md` now make the observer/observation distinction a
  validator-visible Wolfram foundation requirement; `tools/tests/test_bundle_step4.py`
  adds the regression test.
- `answer.md` supersedes `answer.md@r4`.
- `agent-contract.md` supersedes `agent-contract.md@r13`.
- `s/overview.md` supersedes `s/overview.md@r18`.
- `s/method.md` supersedes `s/method.md@r18`.
- `s/specification.md` supersedes `s/specification.md@r19`.
- `s/foundations/wolfram-observer-theory.md` supersedes
  `s/foundations/wolfram-observer-theory.md@r19`.
- `r/results.md` supersedes `r/results.md@r17`.
- `r/retrospective-round-classification.csv`, `inquiry/index.md`, bundle
  `log.md`, and root `log.md` are updated as ledger/navigation records rather
  than frontmatter-bearing concepts.

# Classification rationale

This is an enrichment-stage evidence round. It adds audit evidence and narrows
the framework's concepts where the current wording was too coarse, but it does
not maintain a rival framework position and does not declare the framework
resolved. Because the round is not contestation-stage, `fc-type-at-round` is
intentionally omitted.
