---
type: Finding
title: Retrospective case-study method
description: Method used to classify and analyze the framework-self trajectory without rewriting history.
fc-level: 2
fc-axis: S
fc-status: open
fc-round: 20
fc-supersedes: s/method.md@r18
timestamp: 2026-08-16
---

This pilot uses the current framework to classify the repository's own recorded
history without changing prior round files. The method is:

1. Treat the current bundle tree, round files, bundle ledger, repository
   ledger, concept frontmatter, git commits, and published manifests as the
   recording substrate for `R` ([reproduction/data.md](../reproduction/data.md)).
   The current tree is the current projection; complete prior concept bodies
   are recovered from Git history or pinned snapshots rather than from current
   round files alone.
2. Treat [Wolfram observer theory](foundations/wolfram-observer-theory.md) as
   the cross-cutting foundation for the bounded-observer analogy, while using
   [Algorithmic information theory and compression](foundations/ait-compression.md)
   only as the established mathematical counterpart for compression/description
   length. Do not infer project extensions such as `r`, factual irreducibility,
   or Type I/II/III from Wolfram sources.
3. Keep actor identity (`fc-party`) separate from theoretical observer
   identity. Treat `codex` and `claude` as authorship labels unless prompt,
   tool, retrieved-record, model/version, and time context justify a more
   specific observer instance or family.
4. Read contemporaneous `fc-move`, `fc-party`, `fc-stage`, and
   `fc-type-at-round` directly from each `inquiry/round-NNNN.md` file.
5. For rounds 1-3, which predate `fc-stage`, infer stage under
   [docs/framework_v3.md section 2.2](../../../docs/framework_v3.md#22-the-dynamic-model-observer-trajectories-rounds-and-stages)
   and mark the inference as retrospective in
   [r/retrospective-round-classification.csv](../r/retrospective-round-classification.csv).
6. Treat `fc-type-at-round` as applicable only to contestation-stage rounds
   under [spec/SPEC.md section 5.2](../../../spec/SPEC.md#52-round-fields);
   legacy non-contestation type values remain in their original round files but
   are excluded from the retrospective type trajectory.
7. Count stalls, reversals, and oscillations only where the record supplies
   enough repeated states to measure them. This pilot can measure stage
   persistence and stage returns, but not type stalls or type oscillations
   because round 3 is the only contestation-stage round.
8. Use [docs/observer-theory-audit.md](../../../docs/observer-theory-audit.md)
   as the round-20 audit record for Wolfram attribution, observer ontology, and
   reconstruction limits.

The case account deliberately does not claim external validity. Its role is to
test inspectability and reproduction on one self-referential trajectory before
the four external Step 7 validation cases are attempted.
