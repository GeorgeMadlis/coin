---
type: Finding
title: "Artifact inventory"
fc-level: 2
fc-axis: R
fc-round: 7
fc-supersedes: "r/artifact-inventory.md@round-0006"
gsp-aoi: fazenda_sucuri_screening_aoi
gsp-provenance: pinned-not-reproduced
---
# Artifact inventory

All 59 artifacts declared in the refreshed evidence-bundle manifest are recorded in
`../reproduction/source-evidence.json`. Root evidence manifest hash:
`a481ea836ad47bd5d4fc56c68f0191d58b24637d27674aafaeea8d5389b927de`.

| role | source path | sha256 (truncated) | mime | bytes | required |
|---|---|---|---|---:|---|
| `aoi_geometry` | `inputs/aoi.geojson` | `59f53c1d0ca30b55...` | application/geo+json | 1458 | yes |
| `satellite_baseline_raster` | `inputs/satellite_baseline.tif` | `d609b915e89e0efb...` | image/tiff | 1175083 | no |
| `satellite_recent_raster` | `inputs/satellite_recent.tif` | `0d562745341aa000...` | image/tiff | 1172519 | no |
| `commodity_debug` | `reports/aoi_report_v2/fazenda_sucuri_screening_aoi/commodity/coffee/coffee_commodity_debug.json` | `605641c316242e7bdc...` | application/json | 3073 | yes |
| `commodity_mask` | `reports/aoi_report_v2/fazenda_sucuri_screening_aoi/commodity/coffee/coffee_commodity_mask.geojson` | `d3c7e595a552a03bd8...` | application/geo+json | 35127 | yes |
| `commodity_summary` | `reports/aoi_report_v2/fazenda_sucuri_screening_aoi/commodity/coffee/coffee_commodity_summary.json` | `9425228ccb59c835c8...` | application/json | 10986 | yes |
| `commodity_post2020_loss_overlap_mask` | `reports/aoi_report_v2/fazenda_sucuri_screening_aoi/commodity/coffee/coffee_post2020_loss_overlap_mask.geojson` | `34bd26c980e689d982...` | application/geo+json | 1474 | yes |
| `aoi_satellite_basemap` | `reports/aoi_report_v2/fazenda_sucuri_screening_aoi/evidence/01_aoi_satellite.png` | `56903ee63025cb42...` | image/png | 589480 | no |
| `aoi_satellite_evidence_map_basemap_png` | `reports/aoi_report_v2/fazenda_sucuri_screening_aoi/evidence/01b_aoi_satellite_evidence_map.png` | `01d48a73a782b1d8...` | image/png | 902957 | no |
| `aoi_satellite_interactive_map_html` | `reports/aoi_report_v2/fazenda_sucuri_screening_aoi/evidence/01c_aoi_satellite_map.html` | `396736ff055c3e01df...` | text/html | 89024 | no |
| `jrc_forest_2020_mask_png` | `reports/aoi_report_v2/fazenda_sucuri_screening_aoi/evidence/02_jrc_forest_2020.png` | `379a92eb622340619f...` | image/png | 868328 | no |
| `post_2020_loss_on_2020_forest_mask_png` | `reports/aoi_report_v2/fazenda_sucuri_screening_aoi/evidence/03_forest_loss_2021_2025.png` | `c03aa1ba270c027cbd...` | image/png | 860034 | no |
| `commodity_mask_png` | `reports/aoi_report_v2/fazenda_sucuri_screening_aoi/evidence/04_commodity_layer.png` | `78b7ea1a3c59d7c4dd...` | image/png | 875913 | no |
| `commodity_post2020_loss_overlap_mask_png` | `reports/aoi_report_v2/fazenda_sucuri_screening_aoi/evidence/05_intersection.png` | `6db7bcd5609d356181...` | image/png | 903044 | no |
| `before_after_satellite_png` | `reports/aoi_report_v2/fazenda_sucuri_screening_aoi/evidence/06_before_after.png` | `25103bbbaf173d3d...` | image/png | 1835617 | yes |
| `regional_overview_png` | `reports/aoi_report_v2/fazenda_sucuri_screening_aoi/evidence/07_regional_overview.png` | `3742da15bb7b15efe4...` | image/png | 915638 | yes |
| `map_legend_png` | `reports/aoi_report_v2/fazenda_sucuri_screening_aoi/evidence/legend.png` | `515508244040c839...` | image/png | 658 | no |
| `post_2020_loss_on_2020_forest_mask` | `reports/aoi_report_v2/fazenda_sucuri_screening_aoi/jrc_gfc2020/forest_loss_2021_2025_on_jrc_forest_2020_mask.geojson` | `742e0d43ac67f167...` | application/geo+json | 4395 | no |
| `jrc_forest_2020_mask` | `reports/aoi_report_v2/fazenda_sucuri_screening_aoi/jrc_gfc2020/jrc_forest_2020_mask.geojson` | `30bce79af03596ea...` | application/geo+json | 21702 | no |
| `post_2020_loss_on_2020_forest_summary` | `reports/aoi_report_v2/fazenda_sucuri_screening_aoi/jrc_gfc2020/jrc_post2020_loss_2021_2025_summary.json` | `0d82e3cd0e22ce789a...` | application/json | 3305 | no |
| `post_2020_loss_on_2020_forest_debug` | `reports/aoi_report_v2/fazenda_sucuri_screening_aoi/jrc_gfc2020/jrc_post2020_loss_debug.json` | `f40bb1bebb6de4f8...` | application/json | 1238 | no |
| `canonical_manifest` | `reports/aoi_report_v2/fazenda_sucuri_screening_aoi/manifest.sha256` | `63b91afc4f59888aad...` | text/plain | 2804 | yes |
| `canonical_metrics_csv` | `reports/aoi_report_v2/fazenda_sucuri_screening_aoi/metrics.csv` | `99596e7e559463be84...` | text/csv | 9191 | yes |
| `canonical_report_html` | `reports/aoi_report_v2/fazenda_sucuri_screening_aoi/report.html` | `19008f783fd55738fb...` | text/html | 489987 | yes |
| `canonical_report_json` | `reports/aoi_report_v2/fazenda_sucuri_screening_aoi/report.json` | `0679004210ab81b554...` | application/json | 112818 | yes |
| `canonical_report_pdf` | `reports/aoi_report_v2/fazenda_sucuri_screening_aoi/report.pdf` | `e5c8da5dcf11afc2fa...` | application/pdf | 6063631 | yes |

The omitted table rows are additional source-specific GeoJSON/PNG support artifacts also listed
in `../reproduction/source-evidence.json`; the full machine-readable manifest remains authoritative.
The handoff records `counterpart_dirty: false`, so these hashes identify a clean-pinned counterpart
evidence state. Provenance remains `pinned-not-reproduced` until an independent rerun-for-determinism
check is completed.
