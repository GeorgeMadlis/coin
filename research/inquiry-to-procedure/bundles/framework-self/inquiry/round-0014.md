---
type: Event
title: "Round 14: observer-distance metrics completed"
description: Step 5 observer-distance metrics completed; framework-self pilot measurements recorded with explicit missing values.
fc-axis: INQUIRY
fc-round: 14
fc-move: evidence
fc-stage: enrichment
fc-party: codex
fc-touches: [r/index.md, r/results.md, r/full-results.md]
fc-status: open
timestamp: 2026-07-21
---

# Move

Step 5's repository-level metrics deliverable is now filled in
`docs/metrics.md`. It defines observer-distance, contestation-type, and
stage-trajectory metrics; separates mathematical definitions, measurement
protocols, repository-derived measurements, and speculative hypotheses; and
states failure modes and falsification uses for every metric.

# Evidence added

- `docs/metrics.md` defines measurable proxies for observer distance and
  trajectory behavior, including missing-data rules and framework proposition
  relationships.
- `r/full-results.md` records the framework-self pilot measurement over bundle
  rounds 1-13, excluding this round to avoid circular self-measurement.
- `r/metrics-rounds-0001-0013.csv` gives a machine-readable measurement table.

# Effect on state

Context window: added an operational metrics layer and reproducible
framework-self measurement values derived from recorded round files, ledgers,
and current concept metadata.

Frame: unchanged. The bundle remains a self-description of the framework; this
round adds measurement instruments and a demonstration, while explicitly
stating that one self-referential trajectory does not validate the framework.

# Resulting revisions

- `docs/metrics.md` - Step 5 stub replaced with the observer-distance metrics
  deliverable.
- `r/results.md` - supersedes `r/results.md@r11` to record that Step 5 is now
  filled and to point to the metric measurement artifacts.
- `r/index.md` - updated so `r/full-results.md` and the CSV measurement table
  are discoverable.
- `r/full-results.md` - added as the L3 reproducible result page for the
  framework-self measurement.
- `r/metrics-rounds-0001-0013.csv` - added as a simple machine-readable table.

# Classification rationale

This is an enrichment-stage evidence round: it adds metric definitions,
calculation protocols, and reproducible measurements to the existing
self-description. It does not assert or maintain a rival position.
`fc-type-at-round` is intentionally omitted because this round is not
contestation-stage.
