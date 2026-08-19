---
type: Finding
title: "Report page audit"
fc-level: 2
fc-axis: R
fc-round: 7
fc-supersedes: "r/report-page-audit.md@round-0006"
gsp-provenance: pinned-not-reproduced
---
# Report page audit

The report PDF hash is
`e5c8da5dcf11afc2fae68129b59fa5c8c0fc48029df2ba528ba9c92a0666c87d`; page count is 12.
The derived contact sheet is `../reproduction/fazenda_sucuri_screening_aoi_contact_sheet.pdf`.

| page | title | audit note |
|---:|---|---|
| 1 | Cover | AOI context, report identity, and locality label `Coromandel, Minas Gerais`. |
| 2 | Executive Summary | Human-review status and headline metrics. |
| 3 | Assessment Workflow | Method flow. |
| 4 | Regional Overview | Regional context image is present from the local Sentinel-2 fallback; sidebar records state `Minas Gerais` and municipality `Coromandel`. |
| 5 | Forest Baseline 2020 | Baseline forest and available overlays render with layer-specific legend rows; coffee is labeled `Coffee plantations (2020)`. |
| 6 | Forest Loss After 2020 | Loss and current commodity overlap context renders; coffee is labeled `Coffee plantations (2024)`, preserving the baseline coffee footprint. |
| 7 | Satellite Evidence | Baseline/recent Sentinel-2 paired situation panel; round 2 fixed the previous half-black baseline panel. |
| 8 | Interpretation | Source-specific vs source-agreement distinction is carried into text. |
| 9 | Data And Methods | Dataset and method details. |
| 10 | Audit Trail | Commit, generated time, and artifact record. |
| 11 | Deterministic Artifacts | Manifest and reproducibility records. |
| 12 | Appendix | Supplemental metrics and limitations. |

The HTML report's interactive map includes both basemaps, baseline forest, loss, FDP new coffee,
MapBiomas new coffee, source-specific conversion, and source-agreement conversion if renderable.
For this AOI, source-agreement conversion is omitted and recorded as
`source_mask_contains_no_renderable_features`. Round 4 offsets the map title from the zoom controls.

The canonical HTML Area of Interest panel now selects a renderable evidence layer by default,
updates the legend to match the selected layer, and uses cover fitting for the AOI image so the
previous side black stripes are not presented in the report page.

Round 2 measured the corrected `evidence/06_before_after.png` directly: the left panel and full
image both have 0.0% black pixels after reacquiring Sentinel-2 visual rasters through the guarded
seasonal composite path.

Round 5 refreshes this audit against the canonical CLI rerun that explicitly included
`--enable-hansen-post-2020-loss`. Page count remains 12, provenance remains
`pinned-not-reproduced` until an independent rerun-for-determinism check is completed.

Round 6 refreshes the audit against the temporal-mask-corrected coffee layers. Page 5 is the
baseline coffee layer (`Coffee plantations (2020)`), and page 6 is the current 2024 coffee layer
with baseline-year coffee retained.

Round 7 refreshes the audit after the recurring page-4 regional-overview defect was fixed in the
counterpart renderer. The source report page 4 and the regenerated contact sheet were rendered to
PNG and visually checked; the page-4 map box is populated rather than showing the previous
"not available" gap panel.
