---
type: Finding
title: "Artifact inventory"
fc-level: 2
fc-axis: R
fc-round: 8
fc-supersedes: "r/artifact-inventory.md@round-0007"
gsp-aoi: fazenda_sucuri_screening_aoi
gsp-provenance: pinned-not-reproduced
---
# Artifact inventory

All 117 artifacts declared in the refreshed evidence-bundle manifest are recorded in
`../reproduction/source-evidence.json`. Root evidence manifest hash:
`a0cc46dc310751c082f659b3e9682218a45bc4fed92162503207e7a67aa65e6e`.

| role | source path | sha256 (truncated) | mime | bytes | required |
|---|---|---|---|---:|---|
| `aoi_geometry` | `inputs/aoi.geojson` | `59f53c1d0ca30b55...` | application/geo+json | 1458 | yes |
| `satellite_baseline_raster` | `inputs/satellite_baseline.tif` | `d609b915e89e0efb...` | image/tiff | 1175083 | no |
| `satellite_recent_raster` | `inputs/satellite_recent.tif` | `0d562745341aa000...` | image/tiff | 1172519 | no |
| `commodity_debug` | `reports/aoi_report_v2/fazenda_sucuri_screening_aoi/commodity/coffee/coffee_commodity_debug.json` | `9a0c11691d2b8ddf4d...` | application/json | 3097 | yes |
| `commodity_mask` | `reports/aoi_report_v2/fazenda_sucuri_screening_aoi/commodity/coffee/coffee_commodity_mask.geojson` | `622bc2dbf808bc09b1...` | application/geo+json | 213009 | yes |
| `commodity_summary` | `reports/aoi_report_v2/fazenda_sucuri_screening_aoi/commodity/coffee/coffee_commodity_summary.json` | `bfd6a0737e3288ee47...` | application/json | 15377 | yes |
| `commodity_post2020_loss_overlap_mask` | `reports/aoi_report_v2/fazenda_sucuri_screening_aoi/commodity/coffee/coffee_post2020_loss_overlap_mask.geojson` | `d148b935d5d2f6eeb0...` | application/geo+json | 8731 | yes |
| `aoi_satellite_basemap` | `reports/aoi_report_v2/fazenda_sucuri_screening_aoi/evidence/01_aoi_satellite.png` | `56903ee63025cb42...` | image/png | 589480 | no |
| `aoi_satellite_evidence_map_basemap_png` | `reports/aoi_report_v2/fazenda_sucuri_screening_aoi/evidence/01b_aoi_satellite_evidence_map.png` | `01d48a73a782b1d8...` | image/png | 902957 | no |
| `aoi_satellite_interactive_map_html` | `reports/aoi_report_v2/fazenda_sucuri_screening_aoi/evidence/01c_aoi_satellite_map.html` | `64bbd8f5d3b491e116...` | text/html | 474489 | no |
| `jrc_forest_2020_mask_png` | `reports/aoi_report_v2/fazenda_sucuri_screening_aoi/evidence/02_jrc_forest_2020.png` | `b820df6aed5a0e7210...` | image/png | 866328 | no |
| `post_2020_loss_on_2020_forest_mask_png` | `reports/aoi_report_v2/fazenda_sucuri_screening_aoi/evidence/03_forest_loss_2021_2025.png` | `11a2392e325d270123...` | image/png | 850198 | no |
| `commodity_mask_png` | `reports/aoi_report_v2/fazenda_sucuri_screening_aoi/evidence/04_commodity_layer.png` | `46ee24d96e37cec668...` | image/png | 865759 | no |
| `commodity_post2020_loss_overlap_mask_png` | `reports/aoi_report_v2/fazenda_sucuri_screening_aoi/evidence/05_intersection.png` | `023eb082c73a9b8789...` | image/png | 903125 | no |
| `before_after_satellite_png` | `reports/aoi_report_v2/fazenda_sucuri_screening_aoi/evidence/06_before_after.png` | `25103bbbaf173d3d...` | image/png | 1835617 | yes |
| `regional_overview_png` | `reports/aoi_report_v2/fazenda_sucuri_screening_aoi/evidence/07_regional_overview.png` | `3742da15bb7b15efe4...` | image/png | 915638 | yes |
| `map_legend_png` | `reports/aoi_report_v2/fazenda_sucuri_screening_aoi/evidence/legend.png` | `515508244040c839...` | image/png | 658 | no |
| `post_2020_loss_on_2020_forest_mask` | `reports/aoi_report_v2/fazenda_sucuri_screening_aoi/jrc_gfc2020/forest_loss_2021_2025_on_jrc_forest_2020_mask.geojson` | `742e0d43ac67f167...` | application/geo+json | 4395 | no |
| `jrc_forest_2020_mask` | `reports/aoi_report_v2/fazenda_sucuri_screening_aoi/jrc_gfc2020/jrc_forest_2020_mask.geojson` | `30bce79af03596ea...` | application/geo+json | 21702 | no |
| `post_2020_loss_on_2020_forest_summary` | `reports/aoi_report_v2/fazenda_sucuri_screening_aoi/jrc_gfc2020/jrc_post2020_loss_2021_2025_summary.json` | `0d82e3cd0e22ce789a...` | application/json | 3305 | no |
| `post_2020_loss_on_2020_forest_debug` | `reports/aoi_report_v2/fazenda_sucuri_screening_aoi/jrc_gfc2020/jrc_post2020_loss_debug.json` | `f40bb1bebb6de4f8...` | application/json | 1238 | no |
| `canonical_manifest` | `reports/aoi_report_v2/fazenda_sucuri_screening_aoi/manifest.sha256` | `63b91afc4f59888aad...` | text/plain | 2804 | yes |
| `canonical_metrics_csv` | `reports/aoi_report_v2/fazenda_sucuri_screening_aoi/metrics.csv` | `c072cf7d1f0bf9fa3a...` | text/csv | 8911 | yes |
| `canonical_report_html` | `reports/aoi_report_v2/fazenda_sucuri_screening_aoi/report.html` | `41768a7f3d6b8a47cc...` | text/html | 699638 | yes |
| `canonical_report_json` | `reports/aoi_report_v2/fazenda_sucuri_screening_aoi/report.json` | `46b188c64c89c709b6...` | application/json | 178128 | yes |
| `canonical_report_pdf` | `reports/aoi_report_v2/fazenda_sucuri_screening_aoi/report.pdf` | `dc519f6bfb730c793...` | application/pdf | 7128915 | yes |
| `fdp_jrc_diagnostic_artifact` | `reports/aoi_report_v2/fazenda_sucuri_screening_aoi/evidence/coffee_jrc_diagnostics/fdp_jrc_threshold_metrics.csv` | `6c0d1790d09b115ba...` | text/csv | 619 | no |
| `fdp_jrc_diagnostic_artifact` | `reports/aoi_report_v2/fazenda_sucuri_screening_aoi/evidence/coffee_jrc_diagnostics/fdp_jrc_morphology_diagnostics.json` | `94f8627832221dd9...` | application/json | 16143 | no |
| `fdp_jrc_diagnostic_artifact` | `reports/aoi_report_v2/fazenda_sucuri_screening_aoi/evidence/coffee_jrc_diagnostics/morphology_current_overlap_composite_t0025.png` | `1fac93cc188455ad...` | image/png | 10734 | no |
| `fdp_jrc_diagnostic_artifact` | `reports/aoi_report_v2/fazenda_sucuri_screening_aoi/evidence/coffee_jrc_diagnostics/morphology_new_overlap_composite_t0025.png` | `a87c5b866d493360...` | image/png | 10089 | no |

The new diagnostic set contains 64 declared `fdp_jrc_diagnostic_artifact` entries, including 60 PNGs
and the threshold/morphology JSON/CSV outputs. Some PNGs are present in both the commodity diagnostic
folder and the report evidence folder with identical hashes; the manifest paths remain authoritative.

The omitted table rows are additional source-specific GeoJSON/PNG support artifacts also listed in
`../reproduction/source-evidence.json`; the full machine-readable manifest remains authoritative.
The handoff records `counterpart_dirty: false`, so these hashes identify a clean-pinned counterpart
evidence state. Provenance remains `pinned-not-reproduced` until an independent rerun-for-determinism
check is completed.
