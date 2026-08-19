---
type: Event
title: "Round 2: fix contact-sheet guide and Sentinel-2 before panel"
fc-axis: INQUIRY
fc-round: 2
fc-move: fix
fc-stage: enrichment
fc-party: codex
fc-status: open
fc-touches: "index.md, EUDR_COFFEE_BRAZIL_FAZENDA_SUCURI_BUNDLE_READING_GUIDE.md, fazenda_sucuri_contact_sheet_guide.html, s/specification.md, r/report-page-audit.md, r/artifact-inventory.md, reproduction/*, log.md, inquiry/index.md"
gsp-engine: gee
gsp-counterpart: single-earth/eudr-dmi-gil@34184b5bb0ff1df7d533f62dd21ca69c778802b2
---
# Move

Fix two package defects reported after round 1:

1. The source/published package lacked `fazenda_sucuri_contact_sheet_guide.html`.
2. The Satellite Evidence before/after image had a half-black/nodata baseline panel.

# Evidence added

- Counterpart commit:
  `single-earth/eudr-dmi-gil@34184b5bb0ff1df7d533f62dd21ca69c778802b2`.
- Evidence bundle:
  `fazenda_sucuri_screening_aoi_evidence_freeze_20260811T102000Z`.
- Root manifest hash:
  `8f7d63ac29930e5b36f767028444aef8eb6da8be53c4a06f8f3c83ad9e568678`.
- Report PDF hash:
  `341dc42dd0c9be4c657739001bf3347de21dc9f313e84f91fa1a931ea3b8d255`, 12 pages.
- Derived contact sheet:
  `reproduction/fazenda_sucuri_screening_aoi_contact_sheet.pdf`.
- Contact-sheet guide:
  `fazenda_sucuri_contact_sheet_guide.html`.

# Result

The verdict and headline metrics are unchanged. The corrected baseline Sentinel-2 visual raster
measures 100% valid coverage overall and 100% valid coverage in the left half; the generated
`evidence/06_before_after.png` measures 0.0% black pixels in the left panel and 0.0% black pixels
overall.

# Resulting revisions

- `s/specification.md` supersedes `s/specification.md@round-0001`.
- `r/report-page-audit.md` supersedes `r/report-page-audit.md@round-0001`.
- `r/artifact-inventory.md` supersedes `r/artifact-inventory.md@round-0001`.
- `reproduction/code.md` supersedes `reproduction/code.md@round-0001`.
- `reproduction/data.md` supersedes `reproduction/data.md@round-0001`.

# Classification rationale

**fc-stage: enrichment** - this round fixes packaging and visual-evidence presentation while
preserving the task's existing verdict class and decision rules.
