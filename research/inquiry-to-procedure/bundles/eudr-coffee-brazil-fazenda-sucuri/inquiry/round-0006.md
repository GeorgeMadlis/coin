---
type: InquiryRound
title: "Round 6 - coffee temporal-mask correction"
fc-round: 6
fc-stage: enrichment
date: 2026-08-12
party: codex
move: fix
gsp-aoi: fazenda_sucuri_screening_aoi
gsp-verdict-class: possible_relevant_deforestation
gsp-provenance: pinned-not-reproduced
gsp-counterpart: GeorgeMadlis/eudr-dmi-gil@e46d9a4c833c22805dc17e50315fd814e25043a0
fc-touches: "answer.md, pf/formal.md, s/overview.md, s/modeling.md, s/gsp-mapping.md, s/specification.md, s/task-scope.md, r/overview.md, r/results.md, r/report-page-audit.md, r/artifact-inventory.md, reproduction/code.md, reproduction/data.md, reproduction/source-evidence.json, reproduction/fazenda_sucuri_screening_aoi_contact_sheet.pdf, reproduction/fazenda_sucuri_screening_aoi_contact_sheet.pdf.metadata.json, bundle.json, index.md, log.md, inquiry/index.md"
---
# Round 6 - coffee temporal-mask correction

This round incorporates the coffee commodity-mask fix already established in the Ibia/Patrocinio
sibling bundle: a latest/current commodity observation is not clearing evidence for a baseline-year
coffee plantation.

Evidence package transition:

- Old evidence bundle id:
  `fazenda_sucuri_screening_aoi_evidence_freeze_20260811T102000Z`.
- New evidence bundle id:
  `fazenda_sucuri_screening_aoi_evidence_freeze_20260812T104000Z`.
- Counterpart used:
  `GeorgeMadlis/eudr-dmi-gil@e46d9a4c833c22805dc17e50315fd814e25043a0`, with
  `counterpart_dirty: false`.
- Root manifest SHA256:
  `5e52311b1111042a01d4845bdff0351deb9bfdd62858bae88c07647eef4b1bc4`.
- Report PDF SHA256:
  `47b47a0164d15bda0665c847f5b7ed6472ac3ecbc9f21bfd7ca2db80a1769709`.
- Contact-sheet PDF SHA256:
  `80a9f62808ef952582a1a1bbbd7ede7794cfd748cf0782ce49dd5a0589fe3097`.

Commodity temporal-mask correction:

- Baseline coffee layer = coffee plantations in 2020.
- Current coffee layer = latest observed coffee (2024 for this bundle) plus 2020 baseline coffee,
  unless an explicit clearing/removal evidence layer proves the baseline coffee was cleared.
- New commodity since baseline remains latest observed coffee AND NOT baseline coffee.

Verification completed:

- Counterpart tests passed: the focused handoff/PDF regression suite reported 24 passed, and the
  full `.venv/bin/python -m pytest` suite reported 196 passed, 3 skipped.
- OKF/GSP bundle validation passed:
  `.venv/bin/python tools/okf_gsp.py validate eudr-coffee-brazil-fazenda-sucuri` reported `ok`.
- The OKF/GSP handoff verifier recomputed the authoritative evidence manifest, report PDF, and 58
  handoff-declared artifact hashes successfully.
- The report PDF text labels page 5 as `Coffee plantations (2020)` and page 6 as
  `Coffee plantations (2024)`.
- Geometry check passed exactly at the vector-mask level:
  `baseline_commodity_mask - current_commodity_mask = 0`; and
  `current_commodity_mask - baseline_commodity_mask = new_commodity_since_baseline`.
- The derived contact sheet was regenerated from the new report PDF and visually checked for the
  current coffee layer preserving the baseline coffee footprint.

Verdict effect:

The verdict remains `possible_relevant_deforestation` / `pinned-not-reproduced`. Current coffee
area changes from the stale disappearing-baseline value to 355.86 ha, and current coffee/post-2020
loss overlap is now 1.08 ha. The new-commodity signal remains source-specific: FDP new coffee/loss
overlap is 0.27 ha, while MapBiomas and both-source-agreement new coffee/loss overlap are 0.0 ha.

Supersedes ledger for current concept files:

- `answer.md@round-0001`
- `pf/formal.md@round-0001`
- `s/overview.md@round-0005`
- `s/modeling.md@round-0001`
- `s/gsp-mapping.md@round-0005`
- `s/specification.md@round-0005`
- `r/overview.md@round-0001`
- `r/results.md@round-0001`
- `r/report-page-audit.md@round-0005`
- `r/artifact-inventory.md@round-0005`
- `reproduction/code.md@round-0005`
- `reproduction/data.md@round-0005`
