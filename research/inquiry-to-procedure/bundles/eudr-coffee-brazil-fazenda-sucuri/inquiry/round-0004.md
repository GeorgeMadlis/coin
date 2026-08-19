---
type: Event
title: "Round 4: add AOI admin labels and report map fixes"
fc-axis: INQUIRY
fc-round: 4
fc-move: fix
fc-stage: enrichment
fc-party: codex
fc-status: open
fc-touches: "s/specification.md, r/report-page-audit.md, r/artifact-inventory.md, reproduction/source-evidence.json, reproduction/fazenda_sucuri_screening_aoi_contact_sheet.pdf, reproduction/fazenda_sucuri_screening_aoi_contact_sheet.pdf.metadata.json, reproduction/code.md, reproduction/data.md, log.md, inquiry/index.md"
gsp-engine: gee
gsp-counterpart: single-earth/eudr-dmi-gil@246904d16e30870523c517fc33822d423ff7395c
---
# Move

Regenerate the Fazenda Sucuri report after adding AOI administrative labels and correcting the
HTML map presentation defects reported against `report.html`.

# Evidence added

- AOI administrative labels are now carried from the AOI GeoJSON into raw and canonical report JSON:
  state `Minas Gerais`, municipality `Coromandel`.
- Report PDF pages 1 and 4 now expose the locality context; the derived contact sheet was rebuilt
  from the regenerated 12-page PDF.
- `report.html` now uses a layer-specific AOI panel/legend, fits the AOI image without side
  black stripes, and shifts the interactive map title away from the Leaflet zoom controls.
- Refreshed root manifest hash:
  `16755334e16459ec9bb81236f35bfc8cf20e61154384e19e17214c32d0b89c48`.
- Refreshed report PDF hash:
  `b99e5d4dff8fc948ae44253eecb0b78d30383fa8d9f27f1ab380853d3b62eb60`, 12 pages.
- Refreshed contact sheet hash:
  `05d549de73de7d377cf1b616a041d8ef178cfac916ed3afdd6682bac9ab194b6`.

# Provenance note

The refreshed handoff records `counterpart_dirty: false` for counterpart commit
`246904d16e30870523c517fc33822d423ff7395c`. The Esri imagery refresh was not retried over the
network; existing local page 1/page 4 imagery was reused and checksum-recorded.

# Resulting revisions

- `s/specification.md` supersedes `s/specification.md@round-0002`.
- `r/report-page-audit.md` supersedes `r/report-page-audit.md@round-0002`.
- `r/artifact-inventory.md` supersedes `r/artifact-inventory.md@round-0002`.
- `reproduction/code.md` supersedes `reproduction/code.md@round-0002`.
- `reproduction/data.md` supersedes `reproduction/data.md@round-0002`.

# Classification rationale

**fc-stage: enrichment** - this round improves report labeling and presentation while preserving the
screening method, evidence bundle shape, and existing decision classification.
