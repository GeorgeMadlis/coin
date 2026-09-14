---
type: Method
title: "Dataset registry"
fc-level: 2
fc-axis: S
fc-round: 8
fc-supersedes: "s/data-sources.md@round-0001"
gsp-engine: gee
---
# Dataset registry

| dataset | gsp-asset-id | gsp-dataset-role | update policy | mandatory |
|---------|--------------|------------------|---------------|-----------|
| AOI geometry input | `aoi_geometry_input` | AOI boundary | user supplied at run | yes |
| JRC Global Forest Cover 2020 V3 | `JRC/GFC2020/V3` | 2020 forest baseline | versioned Earth Engine asset | yes |
| Hansen Global Forest Change 2025 v1.13 | `UMD/hansen/global_forest_change_2025_v1_13` | post-2020 loss year and Hansen canopy baseline | annual release | yes |
| Forest Data Partnership coffee model | `projects/forestdatapartnership/assets/coffee/model_2026a` | FDP baseline/latest coffee probability and task-specific FDP/JRC morphology/threshold diagnostics | provider release | yes |
| MapBiomas Brazil LULC collection 10 | `projects/mapbiomas-public/assets/brazil/lulc/v1` | MapBiomas baseline/latest coffee class | collection release | yes |
| Sentinel-2 L2A harmonized | `COPERNICUS/S2_SR_HARMONIZED` | baseline/recent satellite context and scene diagnostics | rolling archive | yes |

Per-file checksums are recorded in `../reproduction/source-evidence.json`; source evidence is
referenced by hash and counterpart path, not copied into this source bundle.

Round 8 verifies FDP coffee model `2026a` for this task. The acquired FDP probability rasters are
checksum-pinned in the counterpart evidence package and then aligned to the task grid before
thresholding. This records provider observation -> acquired raster -> checksum-pinned artifact ->
computation -> interpretation; the successful hash verification is not treated as proof that the
remote provider record is semantically correct. The handoff/report metadata records the FDP asset id
and local raster checksum, but no separate provider-side task receipt beyond that asset reference.
