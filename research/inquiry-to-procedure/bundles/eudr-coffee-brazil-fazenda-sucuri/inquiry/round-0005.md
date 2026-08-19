---
type: InquiryRound
title: "Round 5 - canonical Hansen-flag handoff hygiene"
fc-round: 5
fc-stage: enrichment
date: 2026-08-12
party: codex
move: fix
gsp-aoi: fazenda_sucuri_screening_aoi
gsp-verdict-class: possible_relevant_deforestation
gsp-provenance: pinned-not-reproduced
gsp-counterpart: single-earth/eudr-dmi-gil@80192bcdbde9329f1a64a60901a52a11d5fcfca8
---
# Round 5 - canonical Hansen-flag handoff hygiene

This round addresses the still-relevant review gaps after the Fazenda Sucuri bundle had already
been formed.

- The counterpart regression-test fix was committed as
  `80192bcdbde9329f1a64a60901a52a11d5fcfca8`; the focused regression suite
  `.venv/bin/python -m pytest tests/test_generate_okf_gsp_handoff.py tests/test_brazil_coffee_report_pdf_structure.py`
  reported 24 passed.
- The evidence bundle was regenerated through the canonical
  `python -m eudr_dmi_gil.reports.cli` entry point with `--enable-hansen-post-2020-loss` recorded
  literally in the handoff command.
- The refreshed handoff records `counterpart_dirty: false`, 59 artifacts, manifest hash
  `a4663ba4659e2689462f522e2f2fff3d97dcbe25a34d7bf17ba3d61986b4a446`, and report PDF hash
  `1ca879da2898941971f07ed6c369b2a245556d7814cacc110c27b0bb3cbd4d83`; page count remains 12.
- The derived contact sheet was rebuilt from that report; metadata records output hash
  `de3afe470566e411b5cc824dd50de3980922c5d273dfbf0cac7ea478d65414a3`.
- PF now records the AOI as an approximate screening polygon, not a cadastral farm boundary.

Supersedes ledger for current concept files:

- `pf/full-context.md@round-0001`
- `s/overview.md@round-0001`
- `s/gsp-mapping.md@round-0001`
- `s/specification.md@round-0004`
- `r/artifact-inventory.md@round-0004`
- `r/report-page-audit.md@round-0004`
- `reproduction/code.md@round-0004`
- `reproduction/data.md@round-0004`

Verdict class remains `possible_relevant_deforestation`: the report metrics are still small but
nonzero for source-specific coffee/loss overlap, with no both-source-agreement overlap. Provenance
remains `pinned-not-reproduced` because no independent rerun-for-determinism check was completed in
this round.
