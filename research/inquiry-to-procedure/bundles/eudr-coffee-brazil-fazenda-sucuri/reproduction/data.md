---
type: Runbook
title: "Asset versions and checksums"
fc-axis: REPRO
fc-round: 8
fc-supersedes: "reproduction/data.md@round-0007"
---
# Pinned assets

| gsp-asset-id | version tag | access date | checksum / snapshot | notes |
|--------------|-------------|-------------|---------------------|-------|
| `aoi_geometry_input` | user_supplied | 2026-09-11 | `59f53c1d0ca30b55b3b4a8af5cb9761841cb9a3a2ffafb38b7c4dce2f8879f88` | AOI GeoJSON config hash stored beside report outputs |
| `JRC/GFC2020/V3` | V3 | 2026-09-11 | see `source-evidence.json` | forest baseline |
| `UMD/hansen/global_forest_change_2025_v1_13` | 2025-v1.13 | 2026-09-11 | see `source-evidence.json` | lossyear and canopy cross-check |
| `projects/forestdatapartnership/assets/coffee/model_2026a` | 2026a | 2026-09-11 | see `source-evidence.json`; acquired 2024 probability raster checksum `f4a40871a8c12f09bbed15974664e75f2a0b5156e4d4b8523bd14908cb453366` | FDP coffee probability, 2020/2024, threshold sensitivity, morphology diagnostics |
| `projects/mapbiomas-public/assets/brazil/lulc/v1` | collection10-v1 | 2026-09-11 | see `source-evidence.json` | MapBiomas coffee class, 2020/2024 |
| `COPERNICUS/S2_SR_HARMONIZED` | sentinel-2-l2a | 2026-09-11 | see `source-evidence.json` | Sentinel-2 context and scene diagnostics; round 2 visual rasters pass 100% valid coverage overall and in the left half |

Round 4 records AOI administrative labels from the AOI GeoJSON properties: state
`Minas Gerais` and municipality `Coromandel`.

The root evidence manifest hash for the regenerated clean-pinned round-7 evidence is
`a481ea836ad47bd5d4fc56c68f0191d58b24637d27674aafaeea8d5389b927de`; the report PDF hash is
`e5c8da5dcf11afc2fae68129b59fa5c8c0fc48029df2ba528ba9c92a0666c87d`; the page-4 regional overview
PNG hash is `3742da15bb7b15efe4ddf56de2cca55e66eead71f814056f45a4ca6a7b40eca1`; the handoff
records 59 artifacts and `counterpart_dirty: false`.

The root evidence manifest hash for the regenerated clean-pinned round-8 evidence is
`a0cc46dc310751c082f659b3e9682218a45bc4fed92162503207e7a67aa65e6e`; the report PDF hash is
`dc519f6bfb730c79368f03c43a7e07891e6724c5bc1764a081bb0131ec1734e7`; the threshold metrics CSV
hash is `6c0d1790d09b115ba229c804b6551ef8402d4e339e1778f7ecf9a3b1a911dc39`; the morphology JSON
hash is `94f8627832221dd95d7779604a67a7b5817ee717669251036df496c0df8260e7`; the handoff records
117 artifacts and `counterpart_dirty: false`.

The FDP provider metadata records asset identifier
`projects/forestdatapartnership/assets/coffee/model_2026a`, dataset version `2026a`, provider id
`forestdatapartnership`, and source URL `https://dataforgood.facebook.com/dfg/tools/forest-data-partnership`.
No separate provider-side task receipt is present in the handoff/report metadata.
