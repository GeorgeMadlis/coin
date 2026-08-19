---
type: Runbook
title: "Data and checksums"
fc-level: 2
fc-axis: REPRO
fc-round: 8
fc-supersedes: reproduction/data.md@round-0004
gsp-aoi: liberia_fmc_area_k_contract_boundary
---
# Data And Checksums

Framework-side source registry:

- `inputs/liberia-eudr-wood-data-source-assessment.md`
- `inputs/liberia-eudr-wood-data-source-registry.json`

Counterpart-side formation references:

| item | sha256 |
|---|---|
| committed Area K GeoJSON at counterpart HEAD | `7cf3be43d78edb01a764310b24bedb8d3f55660bd81ba06503b5e19603eb1bfc` |
| current working-tree Area K GeoJSON observed during formation | `db386f478d9b461418155cb5db4ed9bd70d26d0b554786d61e76aad6280a210b` |
| source-inventory handoff JSON | `ac4b29157a25fb8aff2414c54d995b8ad1f012d1d3fb442174c7c1b54fbd8985` |
| source-inventory manifest JSON | `7cb778d42d14ddfe18770d27367238dbffb257a55e95890ced9a51eeeaafb45b` |
| final evidence handoff JSON | `1658fc3fde056d0a154f50dd8b36c78974185323115e863f766951920b50a142` |
| final evidence manifest JSON | `bef58f2d0c372231d76e8b213eb929884f6acd60a8a01de476998fb78f457084` |
| final report JSON | `5e67f0e069d97ebbb1a44c5ff6691df9888bb872dbfe94068cd70f90f2a05922` |
| final report HTML | `db115bf4829b98c6e0703d98e110929d05c6a84edc93859757ecc814f1e95a42` |
| final report PDF | `8a065c495ead890082948e48a0c913dae9c84de9ef02ddf4269d13dbad50ebc1` |
| final metrics CSV | `c890c51427d5c2024f9d0a5a8412791975b3a85852333d2057155b2d8e73c13c` |
| Area K acquisition manifest | `7eceb3d1e0a2a6c7e7aaec9269b3c93d89a117ce8e0cc50c4d72ebf1252e5e4b` |
| event clusters JSON | `999c4640aaa1093108ead05e8100ab4b3f0d1ea1c7b26a086199f186b3fc808f` |
| Tier-2 event Sentinel confirmation JSON | `0ccea3cd1feed07d9658197d98400eb8530916b48ca884dc0475ef729bc08362` |

The current working-tree GeoJSON contains metadata additions not present in the committed object.
This bundle records that difference and uses the clean handoff/commit as the source reference.

## Asset Pins

| gsp-asset-id | pinned version |
|---|---|
| `EUR-Lex/32023R1115` | `Regulation (EU) 2023/1115, OJ L 150, 2023-06-09` |
| `Liberia_Forest_Atlas/MapServer` | `currentVersion 10.9, queried 2026-08-12/2026-08-15` |
| `Liberia_Forest_Atlas/MapServer/36` | `Layer id 36, currentVersion 10.9, Area K queried 2026-08-12` |
| `Liberia_Forest_Atlas/MapServer/37` | `Layer id 37, currentVersion 10.9, candidate/unresolved for Area K` |
| `Liberia_Forest_Atlas/MapServer/38` | `Layer id 38, currentVersion 10.9, candidate/unresolved for Area K` |
| `JRC/GFC2020/V3` | `V3, local raster sha256 00e59adfd855b7b79693ffec38b485feacee64a5c2c471705844c7b0f48ac5ac` |
| `UMD/hansen/global_forest_change_2025_v1_13` | `2025-v1.13, lossyear sha256 d4cdb9d3426e0b4e371b5af694db7d0f8c7e421a8353e37b8bfc6bac0bf7af1c, treecover2000 sha256 117803b6657a9c9bf081215a3c5d5b47136ae578f0163a251ef18b3e2d3b9024` |
| `projects/JRC/TMF/v1_2025` | `v1_2025, deforestation sha256 76d6b1657735a7eade01c593ec789008fde27b0ca266e90fe60021d4e2274274, degradation sha256 469fc82fcf1d3f54264c06c4d1dcbd9b5c9698811e055ff2ffc524b098d7ecb3, duration sha256 0ca9d52d4daa28835f3dd8edc8613f6fe9b43b2a18fea45389cc9a3abc0398e7, intensity sha256 3be18e4e4cdd4790819d9b7b4692d9b26bc08bd8aa6cd202a12c1812251ca86e` |
| `projects/radar-wur/raddalert/v1` | `frozen 2026-08-15T09:12:17Z, Alert sha256 691ff92c4790d91643e10046b7fe826c43c1d6661826edae76f79581ab8800bb, Date sha256 a416bc69a3b8f47d83cdb9ad1741ef4f5047dc099ec6674c66c2a1807950402a` |
| `COPERNICUS/S2_SR_HARMONIZED` | `baseline 2020 sha256 97e711dd8a50f917b9324c62886e8a658e8956c537ee66304ccabe8007ff59cb, recent 2026 sha256 fc64fa7f9f6894bd44f0ad0ea0889058694ee0d1557e0dff04a88fbfa38ba212, regional sha256 b9cf0d3c08c45660144df31e69764106268874ac255e19ae81c07eb0cf592ca8, Tier-2 confirmation JSON sha256 0ccea3cd1feed07d9658197d98400eb8530916b48ca884dc0475ef729bc08362` |
