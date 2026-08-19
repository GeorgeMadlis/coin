---
type: Runbook
title: "Asset versions and checksums"
fc-axis: REPRO
fc-round: 7
fc-supersedes: "reproduction/data.md@round-0006"
---
# Pinned assets

| gsp-asset-id | version tag | access date | checksum / snapshot | notes |
|--------------|-------------|-------------|---------------------|-------|
| `aoi_geometry_input` | user_supplied | 2026-08-12 | `59f53c1d0ca30b55b3b4a8af5cb9761841cb9a3a2ffafb38b7c4dce2f8879f88` | AOI GeoJSON config hash stored beside report outputs |
| `JRC/GFC2020/V3` | V3 | 2026-08-12 | see `source-evidence.json` | forest baseline |
| `UMD/hansen/global_forest_change_2025_v1_13` | 2025-v1.13 | 2026-08-12 | see `source-evidence.json` | lossyear and canopy cross-check |
| `projects/forestdatapartnership/assets/coffee/model_2025b` | 2025b | 2026-08-12 | see `source-evidence.json` | FDP coffee probability, 2020/2024 |
| `projects/mapbiomas-public/assets/brazil/lulc/v1` | collection10-v1 | 2026-08-12 | see `source-evidence.json` | MapBiomas coffee class, 2020/2024 |
| `COPERNICUS/S2_SR_HARMONIZED` | sentinel-2-l2a | 2026-08-12 | see `source-evidence.json` | Sentinel-2 context and scene diagnostics; round 2 visual rasters pass 100% valid coverage overall and in the left half |

Round 4 records AOI administrative labels from the AOI GeoJSON properties: state
`Minas Gerais` and municipality `Coromandel`.

The root evidence manifest hash for the regenerated clean-pinned round-7 evidence is
`a481ea836ad47bd5d4fc56c68f0191d58b24637d27674aafaeea8d5389b927de`; the report PDF hash is
`e5c8da5dcf11afc2fae68129b59fa5c8c0fc48029df2ba528ba9c92a0666c87d`; the page-4 regional overview
PNG hash is `3742da15bb7b15efe4ddf56de2cca55e66eead71f814056f45a4ca6a7b40eca1`; the handoff
records 59 artifacts and `counterpart_dirty: false`.
