---
type: Finding
title: Retrospective case-study reconstruction problem
description: Formal target for reconstructing the repository's own statement trajectory.
fc-level: 2
fc-axis: PF
fc-status: open
fc-round: 16
fc-supersedes: pf/formal.md@r11
timestamp: 2026-07-21
---

The formal target for this pilot is the repository's own statement trajectory:
a bundle-local sequence of rounds `q(1)..q(16)` whose records are
[inquiry/round-0001.md](../inquiry/round-0001.md) through
[inquiry/round-0016.md](../inquiry/round-0016.md), embedded in a repository
ledger sequence whose current prior entry is repository round 17 in
[log.md](../../../log.md). Round 8 records why the two counters are different
and why snapshots use bundle round while manifests/catalogs also record
`source_repo_round` ([round 8](../inquiry/round-0008.md);
[docs/round-ledgers.md](../../../docs/round-ledgers.md)).

The reconstruction distinguishes three fields for each earlier round:
contemporaneous metadata from the round file, retrospective classification
added later, and uncertainty. The current machine-readable classification is
[r/retrospective-round-classification.csv](../r/retrospective-round-classification.csv).
Its rule column cites [docs/framework_v3.md section 2.2](../../../docs/framework_v3.md#22-the-dynamic-model-observer-trajectories-rounds-and-stages)
for inferred stage assignments and [spec/SPEC.md section 5.2](../../../spec/SPEC.md#52-round-fields)
for inferred type applicability. Historical round files are not edited.

The resulting stage sequence for rounds 1-15 is:
formation, enrichment, contestation, consolidation, enrichment, enrichment,
critique, consolidation, then enrichment through round 15. The type trajectory
has one confidently usable contestation point: round 3, where the body records
resolved Type I mechanical defects and an open Type II residue
([round 3](../inquiry/round-0003.md)). Because there is only one
contestation-stage round, type stalls, type reversals, and type oscillations
are not measurable for this pilot; that limitation is recorded in
[r/full-results.md](../r/full-results.md).
