---
type: Runbook
title: Code and regeneration
description: Repository pin and regeneration instructions for the framework-self pilot bundle.
fc-level: 2
fc-axis: REPRO
fc-irreducibility: none
fc-status: open
fc-round: 16
fc-supersedes: reproduction/code.md@r13
timestamp: 2026-07-21
---

Repository: [GeorgeMadlis/observer-disagreement-framework](https://github.com/GeorgeMadlis/observer-disagreement-framework).

Initial bundle pin: `a1fc43cc83a6f223843f8318f2f92886b6769eb5` (`Initial observer disagreement framework`). No separate PR merge commit exists for the self-bundle content: it was authored before this workspace was git-initialized and shipped as part of the initial scaffold commit rather than through its own PR, so the initial pin points at that commit rather than a `codex/pilot-self-bundle` merge (see [inquiry/round-0003.md](../inquiry/round-0003.md)).

Current regeneration: this bundle is hand-maintained from
[docs/framework_v3.md](../../../docs/framework_v3.md),
[docs/round-ledgers.md](../../../docs/round-ledgers.md), the historical
[docs/framework_v2.md](../../../docs/framework_v2.md),
[spec/SPEC.md](../../../spec/SPEC.md), the recorded inquiry rounds, current
concept metadata, and published framework-self manifests. Rendered `_site/`
output is derived; regenerate it with `okf-fc render bundles/framework-self`
after source edits. Validate source with
`okf-fc validate bundles/framework-self --grandfather-before-round 13`; add
`--check-render-determinism` when validating the renderer path. Published
viewer snapshots are generated with
`okf-fc publish bundles/framework-self --dest ../okf-bundle-snapshots`;
snapshot names use the bundle round, and manifests/catalog rows record the
source repository round separately.

Retrospective classification reproduction:

1. Read `fc-round`, `timestamp`, `fc-party`, `fc-move`, `fc-stage`, and
   `fc-type-at-round` from `bundles/framework-self/inquiry/round-0001.md`
   through `round-0015.md`.
2. For missing historical stages in rounds 1-3, apply the stage rules in
   `docs/framework_v3.md` section 2.2 and record `stage_source:
   retrospective`.
3. For type applicability, apply `spec/SPEC.md` section 5.2: only
   contestation-stage rounds enter the type trajectory.
4. Compare the result to
   `bundles/framework-self/r/retrospective-round-classification.csv`.

The CSV is intentionally small enough to diff by inspection. Its rule columns
are part of the reproduction path, not narrative decoration.
