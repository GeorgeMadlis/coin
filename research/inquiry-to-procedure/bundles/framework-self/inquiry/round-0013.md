---
type: Event
title: "Round 13: generator and validator completed"
description: Step 4 okf-fc generator, atomic round append, and validator completed; framework-self metadata aligned for validation demonstration.
fc-axis: INQUIRY
fc-round: 13
fc-move: evidence
fc-stage: enrichment
fc-party: codex
fc-touches: [agent-contract.md, reproduction/code.md, reproduction/data.md, reproduction/environment.md, reproduction/index.md, s/foundations/ait-compression.md, s/foundations/analytic-historiography.md, s/foundations/argumentation-theory.md, s/foundations/aumann-agreement.md, s/foundations/bayesian-agm-belief-revision.md, s/foundations/coarse-graining-statmech.md, s/foundations/peirce-inquiry.md, s/foundations/provenance-reproducibility.md, s/foundations/quine-duhem.md, s/foundations/second-order-cybernetics.md, s/foundations/simon-bounded-rationality.md]
fc-status: open
timestamp: 2026-07-21
---

# Move

Step 4's repository-level tooling deliverable is now implemented under
`tools/`: deterministic bundle generation, atomic round append, and validator
entry points have been added without replacing the existing render, snapshot,
publish, catalog, or visualization paths.

# Evidence added

- `tools/src/okf_fc/bundle.py` implements the generator and round-append API.
- `tools/src/okf_fc/validate.py` implements the validator against
  `spec/SPEC.md`.
- `tools/tests/test_bundle_step4.py` covers generation determinism, multi-round
  trajectories, parties, all five stages, contestation Type I/II/III
  transitions, invalid type placement, skipped rounds, old-round rewrites,
  duplicate supersession, unpinned evidence, transaction rollback,
  repo/bundle-round divergence, and derived-artifact staleness.
- `tools/README.md` records the Step 4 implementation matrix.

# Effect on state

Context window: added concrete implementation and test evidence for the Step 4
generator, append, and validator requirements.

Frame: unchanged. The bundle remains a self-description of the framework; this
round makes the validation contract executable and records the historical
migration boundary for older framework-self rounds.

# Resulting revisions

- `agent-contract.md` supersedes `agent-contract.md@r8` to add current
  `fc-status` metadata.
- `reproduction/code.md` supersedes `reproduction/code.md@r8` to record the
  new validation command and Step 4 tooling source.
- `reproduction/data.md` supersedes `reproduction/data.md@r8` to include the
  Step 3 specification as the normative input while explicitly avoiding a
  fabricated working-tree checksum.
- `reproduction/environment.md` is added with the Python/package environment
  now made concrete by Step 4.
- Current foundation pages under `s/foundations/` supersede their prior
  versions to add required `fc-status` metadata for full-profile validation.

# Classification rationale

This is an enrichment-stage evidence round: it adds executable tooling,
validation coverage, and metadata needed to demonstrate the completed
specification. It does not assert or maintain a rival position. `fc-type-at-round`
is intentionally omitted because this round is not contestation-stage.
