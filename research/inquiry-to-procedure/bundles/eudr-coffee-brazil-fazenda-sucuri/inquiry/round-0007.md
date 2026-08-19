---
type: InquiryRound
title: "Round 7 - page 4 regional overview repair"
fc-round: 7
fc-stage: enrichment
date: 2026-08-12
party: codex
move: fix
gsp-aoi: fazenda_sucuri_screening_aoi
gsp-verdict-class: possible_relevant_deforestation
gsp-provenance: pinned-not-reproduced
gsp-counterpart: GeorgeMadlis/eudr-dmi-gil@ebb74d93889b7114c629230d198ebd662044bc47
fc-touches: "index.md, s/overview.md, s/specification.md, s/gsp-mapping.md, r/report-page-audit.md, r/artifact-inventory.md, reproduction/code.md, reproduction/data.md, reproduction/index.md, reproduction/source-evidence.json, reproduction/fazenda_sucuri_screening_aoi_contact_sheet.pdf, reproduction/fazenda_sucuri_screening_aoi_contact_sheet.pdf.metadata.json, tools/okf_gsp.py, tests/test_okf_gsp.py, log.md, inquiry/index.md"
---
# Round 7 - page 4 regional overview repair

User-directed fix: snapshot `2026-08-12-r0006-b969a23` still showed the page-4 Regional Overview
map box as a missing-image panel.

Root cause:

- The Sucuri canonical CLI command supplied baseline/recent Sentinel-2 rasters but no dedicated
  `--satellite-regional-raster`.
- The report renderer could fall through to a live Esri fallback; when that did not materialize,
  page 4 rendered the gap panel instead of using already-pinned local satellite context.

Counterpart fix:

- Committed `GeorgeMadlis/eudr-dmi-gil@ebb74d93889b7114c629230d198ebd662044bc47`.
- `report_model.py` now uses the dedicated regional raster first, then falls back to the locally
  pinned recent satellite raster, and only then tries live Esri for reports with no local imagery.
- `scripts/generate_okf_gsp_handoff.py` marks `regional_overview_png` as required when present.
- Focused counterpart tests passed:
  `.venv/bin/python -m pytest tests/test_canonical_report_model.py::test_regional_overview_falls_back_to_local_recent_raster tests/test_generate_okf_gsp_handoff.py`
  reported 4 passed.

Framework/publish-contract fix:

- `tools/okf_gsp.py` now requires `regional_overview_png` for Brazil/coffee handoffs, alongside
  commodity mask, commodity/loss overlap, and before/after imagery.
- The focused framework publish tests passed:
  `.venv/bin/python -m pytest tests/test_okf_gsp.py -k "publish or evidence_handoff or required"`
  reported 10 passed, 1 skipped.

Evidence package transition:

- Old evidence bundle id:
  `fazenda_sucuri_screening_aoi_evidence_freeze_20260812T104000Z`.
- New evidence bundle id:
  `fazenda_sucuri_screening_aoi_evidence_freeze_20260812T121500Z`.
- Root manifest SHA256:
  `a481ea836ad47bd5d4fc56c68f0191d58b24637d27674aafaeea8d5389b927de`.
- Report PDF SHA256:
  `e5c8da5dcf11afc2fae68129b59fa5c8c0fc48029df2ba528ba9c92a0666c87d`.
- Page-4 regional overview PNG SHA256:
  `3742da15bb7b15efe4ddf56de2cca55e66eead71f814056f45a4ca6a7b40eca1`.
- Contact-sheet PDF SHA256:
  `f8f94775e4297bc7894283f861daa701e18f759fe06f62aea27aff7f0bcb9d6c`.

Verification completed:

- New handoff records `counterpart_dirty: false`, 59 artifacts, 12 report pages, and required
  `regional_overview_png`.
- The regenerated source report page 4 was rendered to PNG and visually checked: the map box is
  populated with satellite imagery and the AOI outline.
- The regenerated contact sheet was rendered to PNG and visually checked: the page-4 thumbnail is
  populated and no longer shows the missing-image panel.
- Pixel check on the rendered page-4 map area measured `nonwhite_ratio=0.7968`; the contact-sheet
  page-4 thumbnail crop measured `nonwhite_ratio=0.3595`, confirming nonblank visual content.

Verdict effect:

No metric or verdict changed. The verdict remains `possible_relevant_deforestation` /
`pinned-not-reproduced`; this round repairs presentation/provenance completeness for page 4 and the
publish gate that let the gap recur.

Supersedes ledger for current concept files:

- `s/overview.md@round-0006`
- `s/specification.md@round-0006`
- `s/gsp-mapping.md@round-0006`
- `r/report-page-audit.md@round-0006`
- `r/artifact-inventory.md@round-0006`
- `reproduction/code.md@round-0006`
- `reproduction/data.md@round-0006`
