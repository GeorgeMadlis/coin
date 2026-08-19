---
type: Event
title: "Round 12: OKF bundle specification completed"
description: Step 3 OKF-FC bundle specification completed; provisional bundle conventions made normative and validation-ready.
fc-axis: INQUIRY
fc-round: 12
fc-move: evidence
fc-stage: enrichment
fc-party: codex
fc-touches: [s/specification.md]
fc-status: open
timestamp: 2026-07-21
---

# Move

Step 3's repository-level OKF bundle specification deliverable is now filled
in `spec/SPEC.md`. The document targets upstream OKF v0.1 Draft, namespaces
project-specific metadata with `fc-`, defines the full and lightweight profiles,
states round and supersession rules, separates repository rounds from bundle
rounds, and gives validation behavior for fatal errors, warnings, and advisory
quality checks.

# Evidence added

The specification consolidates the provisional bundle conventions from
`docs/framework_v3.md`, the terminology from `docs/glossary.md`, the formal
round/stage model from `docs/formal-core.md`, the ledger distinction from
`docs/round-ledgers.md`, and the current `framework-self` bundle state. The
upstream OKF source checked for this round is GoogleCloudPlatform
`knowledge-catalog/okf/SPEC.md` at commit
`d44368c15e38e7c92481c5992e4f9b5b421a801d`.

# Effect on state

Context window: added a normative, implementable specification for the
repository's OKF fact-checking and statement-evolution bundles, including field
types, allowed values, applicability, profile rules, and validation outcomes.

Frame: unchanged. The framework still treats bundles as the recording function
for statement trajectories; this round makes the previously provisional bundle
format explicit enough for Step 4 tooling.

# Resulting revisions

- `spec/SPEC.md` - Step 3 stub replaced with the OKF-FC profile specification.
- `s/specification.md` - supersedes `s/specification.md@r8` so the
  framework-self bundle points to `spec/SPEC.md` rather than the provisional
  framework sections.

# Classification rationale

This is an enrichment-stage evidence round: it adds a normative specification
and updates the self-bundle pointer without opening a live counter-position.
`fc-type-at-round` is intentionally omitted because the round is not
contestation-stage.
