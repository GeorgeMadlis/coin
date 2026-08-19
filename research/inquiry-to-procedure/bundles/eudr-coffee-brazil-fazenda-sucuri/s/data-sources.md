---
type: Method
title: "Dataset registry"
fc-level: 2
fc-axis: S
fc-round: 1
gsp-engine: gee
---
# Dataset registry

| dataset | gsp-asset-id | gsp-dataset-role | update policy | mandatory |
|---------|--------------|------------------|---------------|-----------|
| AOI geometry input | `aoi_geometry_input` | AOI boundary | user supplied at run | yes |
| JRC Global Forest Cover 2020 V3 | `JRC/GFC2020/V3` | 2020 forest baseline | versioned Earth Engine asset | yes |
| Hansen Global Forest Change 2025 v1.13 | `UMD/hansen/global_forest_change_2025_v1_13` | post-2020 loss year and Hansen canopy baseline | annual release | yes |
| Forest Data Partnership coffee model | `projects/forestdatapartnership/assets/coffee/model_2025b` | FDP baseline/latest coffee probability | provider release | yes |
| MapBiomas Brazil LULC collection 10 | `projects/mapbiomas-public/assets/brazil/lulc/v1` | MapBiomas baseline/latest coffee class | collection release | yes |
| Sentinel-2 L2A harmonized | `COPERNICUS/S2_SR_HARMONIZED` | baseline/recent satellite context and scene diagnostics | rolling archive | yes |

Per-file checksums are recorded in `../reproduction/source-evidence.json`; source evidence is
referenced by hash and counterpart path, not copied into this source bundle.
