---
type: Event
title: "Round 11: formal core completed"
description: Step 2 formal core completed; static and dynamic models connected, stage/type trajectories separated, and proposition statuses sharpened.
fc-axis: INQUIRY
fc-round: 11
fc-move: evidence
fc-stage: enrichment
fc-party: codex
fc-touches: [pf/formal.md, s/method.md, r/results.md]
fc-status: open
timestamp: 2026-07-21
---

# Move

Step 2's repository-level formal-core deliverable is now filled in
`docs/formal-core.md`. The document formalizes the static two-stage observer
model, the dynamic round-transition model, the sequential multi-observer party
assignment, the diagonal single-observer case, supersession, consolidation,
bottoming-out, and the relationship between `fc-move` and `fc-stage`.

# Evidence added

The formal core reconstructs P1-P5 and P4' from `docs/framework_v3.md`, using
the terminology fixed in `docs/glossary.md` and the literature boundaries
recorded in `docs/related-work.md`. It explicitly marks P2 as derivable under
the Type III assumptions and keeps P1, P3, P4, P4'(b), and P5 provisional to
varying degrees rather than describing them as established universal theorems.

# Effect on state

Context window: added a completed formal model for the framework's
self-description, including definitions, assumptions, counterexamples,
boundary cases, and revision conditions.

Frame: unchanged. The framework still treats statement evolution as bounded
observer compression over a surviving record. This round sharpens the formal
status of the existing v3 propositions and records where theorem language is
not yet justified.

# Resulting revisions

- `docs/formal-core.md` - Step 2 stub replaced with the formal-core
  deliverable.
- `README.md` and `docs/repository-structure-audit.md` - status language
  updated so the repository distinguishes the filled Step 0, Step 1, and Step 2
  deliverables from remaining stubs.
- `pf/formal.md` - supersedes `pf/formal.md@r7` to point to and summarize the
  completed formal core.
- `s/method.md` - supersedes `s/method.md@r7` to summarize the current method
  and proposition statuses.
- `r/results.md` - supersedes `r/results.md@r7` to record that Step 2 is filled
  and that P1-P5/P4' remain mixed in status.

# Classification rationale

This is an enrichment-stage evidence round: it adds formal definitions,
assumptions, and status analysis to the framework's self-description without a
live counter-position. `fc-type-at-round` is intentionally omitted because the
round is not contestation-stage.
