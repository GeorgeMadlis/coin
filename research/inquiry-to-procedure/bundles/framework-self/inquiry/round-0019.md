---
type: Event
title: "Round 19: Wolfram foundation requirement specified"
description: Step 3 specification repaired so every future bundle must disclose the Wolfram observer-theory foundation as formal analogy with separated attribution.
fc-axis: INQUIRY
fc-round: 19
fc-move: evidence
fc-stage: enrichment
fc-party: codex
fc-touches: [s/specification.md, s/foundations/wolfram-observer-theory.md, inquiry/index.md, log.md]
fc-status: open
timestamp: 2026-07-23
---

# Move

Step 3 specification is repaired after the Step 1 Wolfram foundation repair.
The repository specification now makes `s/foundations/wolfram-observer-theory.md`
a mandatory, validator-visible concept for every future full or lightweight
bundle generated under the framework.

# Evidence added

- `spec/SPEC.md` version 0.1.1 defines the mandatory Wolfram foundation page,
  required frontmatter, required sections, attribution classes, minimum source
  policy, analogy guardrails, template drift-control fields, full/lightweight
  profile behavior, worked examples, and validator rejection conditions.
- `s/foundations/wolfram-observer-theory.md` is superseded to match the
  mandatory section contract and to record `fc-foundation-*` metadata.
- `s/specification.md` is superseded to point at the current Step 3
  specification and summarize the new foundation requirement.
- `r/retrospective-round-classification.csv` is extended through round 19 so
  the inquiry index's current-table pointer remains accurate.

# Effect on state

Context window: added the completed Step 3 foundation-disclosure rules and
examples, using the Step 1 source map as the supporting context.

Frame: unchanged at the theory level. The framework still treats Wolfram
observer theory as formal analogy, not literal social physics. The bundle frame
is tightened operationally: future generated bundles must make that analogy and
the source/translation/extension boundary explicit.

# Resulting revisions

- `s/specification.md` supersedes `s/specification.md@r12` to point to the
  current 0.1.1 specification and summarize the mandatory Wolfram disclosure.
- `s/foundations/wolfram-observer-theory.md` supersedes
  `s/foundations/wolfram-observer-theory.md@r18` to add the required
  foundation frontmatter, exact required sections, source-map attribution
  classes, analogy guardrails, and bundle-specific relevance.
- `r/retrospective-round-classification.csv` is updated through round 19; it is
  a CSV record rather than a frontmatter-bearing concept file.
- `inquiry/index.md`, bundle `log.md`, root `log.md`, and rendered `_site/`
  files are updated without supersession frontmatter because they are
  navigation, ledger, repository, or derived artifacts.

# Classification rationale

This is an enrichment-stage evidence round. It adds normative specification
detail and strengthens attribution discipline for future bundles without
maintaining a rival position and without declaring the framework resolved.
Because the round is not contestation-stage, `fc-type-at-round` is
intentionally omitted.
