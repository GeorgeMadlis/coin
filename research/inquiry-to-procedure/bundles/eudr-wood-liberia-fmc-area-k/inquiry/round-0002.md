---
type: Round
fc-level: 3
fc-axis: INQUIRY
fc-round: 2
fc-move: enrichment
fc-stage: enrichment
fc-party: codex
fc-touches:
  - answer.md
  - r/overview.md
  - r/results.md
  - r/artifact-inventory.md
  - reproduction/code.md
  - reproduction/data.md
  - reproduction/source-evidence.json
---
# Round 0002 - Real Area K Evidence-Only Report

## Move

Ran the canonical evidence-only Area K report against real pinned local rasters and alert exports,
then added the resulting report, event clustering, Tier-2 confirmation, handoff, and contact sheet
to this task bundle's reproduction record.

## Evidence Added

- Counterpart: `GeorgeMadlis/eudr-dmi-gil@abf832c9df17e7f1476fde5a3d34ab88647dec4e`, tracked
  status clean for the handoff.
- Evidence bundle: `area-k-real-003`.
- Handoff SHA-256: `f66a9f42bd9ff18dda8b9a15dc86fbe9c781a7bbd807815b7d55e12bff906199`.
- Evidence manifest SHA-256: `00203ac9d92d5d6a1674252fc06496ed8d6c826238abd6e9b832390b1e01c94d`.
- Report JSON/HTML/PDF SHA-256:
  `a0b1c0f1b962e3999a50af0293a68d86e0607d67aae3d95f84bb04f080956b70`,
  `0f9360f59fd1205eef2ba78b75f5efda13b17780f3ecbee20a27bb654d1b28ad`,
  `b0200de13a75c7add4cb207161d9f654057ccf9bc1c6af747011f8352511f9b8`.
- Report page count: `12`; manifest artifact count: `46`; all manifest artifact hashes were
  independently recomputed from bytes on disk.
- Event clustering: `11,492` candidate footprints; top five events are detected by all five
  observers used for clustering.
- Tier-2 Sentinel-2 confirmation: `20` dated crops exported for the top five events; confirmation
  JSON SHA-256 `0ccea3cd1feed07d9658197d98400eb8530916b48ca884dc0475ef729bc08362`.
- Contact sheet: private derived artifact removed from the public bundle.

## Effect On State

The task moves from formation-only `underdetermined` / `UNVERIFIED` to an evidence-only
`human_review_required` screening state with `pinned-not-reproduced` provenance. The report detects
post-cutoff forest disturbance and alerts, but does not establish production plot, harvesting block,
shipment source linkage, chain of custody, or a legal compliance outcome.

## Resulting Revisions

Current R-axis and REPRO-axis files now reference `area-k-real-003`; `source-evidence.json` records
the final handoff, report hashes, event-cluster hash, Tier-2 confirmation hash, and the remaining
page-4 regional-view limitation.

## Classification Rationale

`fc-stage: enrichment` because this round adds reproduced evidence and inspection artifacts to an
already formed task bundle without replacing the parent method contract. It does not consolidate a
new method-family rule; the residual regional overview limitation is recorded locally for this
task's visual inspection history.
