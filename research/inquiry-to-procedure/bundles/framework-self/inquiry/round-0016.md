---
type: Event
title: "Round 16: framework-self longitudinal case-study pilot"
description: Framework-self-only Step 7 retrospective case-study pilot completed; external validation cases remain deferred.
fc-axis: INQUIRY
fc-round: 16
fc-move: evidence
fc-stage: enrichment
fc-party: codex
fc-touches: [pf/full-context.md, pf/formal.md, s/method.md, r/index.md, r/results.md, r/full-results.md, reproduction/code.md, reproduction/data.md, inquiry/index.md, log.md]
fc-status: open
timestamp: 2026-07-21
---

# Move

The Step 7 execution is intentionally restricted to `bundles/framework-self/`.
This round turns the self-bundle into a longitudinal case-study pilot over its
own recorded statement trajectory while preserving a visible distinction from
the four external case-study bundles originally planned for Step 7.

# Evidence added

- `r/retrospective-round-classification.csv` records rounds 1-15 with
  contemporaneous metadata, later inferred stage/type classifications,
  confidence, rule citations, round references, and commit or manifest
  references.
- `r/results.md` now gives the framework-self-only case-study account, with
  assertions tied to round files, concept versions, commits, or published
  manifests.
- `r/full-results.md` records compact counts for the retrospective
  classification and preserves the earlier Step 5 and Step 6 measurement
  boundaries.
- `pf/full-context.md`, `pf/formal.md`, `s/method.md`, `reproduction/code.md`,
  and `reproduction/data.md` state the scope boundary and reproduction path.
- `tools/src/okf_fc/render.py` now copies non-Markdown bundle assets such as
  CSV files into `_site/`, so rendered links to machine-readable artifacts are
  inspectable through the static site.

# Effect on state

Context window: added a retrospective classification layer over the existing
round sequence and published snapshot manifests. The four external bundle
stubs remain outside this PR's evidence window.

Frame: unchanged. The framework still treats this as a statement trajectory
whose stage classifications are separate from contestation types. The new work
applies that frame to the repository's own history without editing earlier
round records.

# Resulting revisions

- `pf/full-context.md` supersedes `pf/full-context.md@r1` to state the
  framework-self-only case-study scope and known reconstruction limits.
- `pf/formal.md` supersedes `pf/formal.md@r11` to define the retrospective
  reconstruction target.
- `s/method.md` supersedes `s/method.md@r11` to document the classification
  method and stage/type applicability rules.
- `r/results.md` supersedes `r/results.md@r15` to add the case-study account
  and current Step 7 status.
- `r/full-results.md` supersedes `r/full-results.md@r15` to add Step 7
  classification counts and non-measurability notes.
- `r/retrospective-round-classification.csv` is added as the compact
  machine-readable retrospective classification artifact.
- `reproduction/code.md` supersedes `reproduction/code.md@r13` to document the
  CSV reproduction procedure.
- `reproduction/data.md` supersedes `reproduction/data.md@r13` to list the
  current case-study inputs and published manifest references.
- `tools/src/okf_fc/render.py` and `tools/tests/test_render.py` are updated so
  non-Markdown bundle assets are copied to rendered output.
- `inquiry/index.md`, bundle `log.md`, `README.md`, `bundles/README.md`, and
  `docs/repository-structure-audit.md` are updated to distinguish the
  completed framework-self pilot from deferred external validation cases.

# Classification rationale

This is an enrichment-stage evidence round: it adds a retrospective analysis
layer and reproduction artifact to the existing self-description. It does not
assert a rival position against the current framework and does not claim
external validity. Because the round is not contestation-stage,
`fc-type-at-round` is intentionally omitted.
