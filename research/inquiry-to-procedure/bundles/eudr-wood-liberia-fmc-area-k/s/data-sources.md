---
type: Method
title: "Data sources"
fc-level: 2
fc-axis: S
fc-round: 8
fc-supersedes: s/data-sources.md@round-0004
gsp-engine: gee
gsp-aoi: liberia_fmc_area_k_contract_boundary
---
# Data Sources

Primary source registry:

- `inputs/liberia-eudr-wood-data-source-assessment.md`
- `inputs/liberia-eudr-wood-data-source-registry.json`

Current source roles:

| source | gsp-asset-id | role | state |
|---|---|---|---|
| European Commission / EUR-Lex and due-diligence guidance | `EUR-Lex/32023R1115` | legality context | legal/guidance context, not spatial evidence |
| Liberia Forest Atlas open data | `Liberia_Forest_Atlas/MapServer` | allocation / legal-provenance context | source family queried in formation |
| Forest Atlas FMC layer 36 | `Liberia_Forest_Atlas/MapServer/36` | concession allocation | Area K query verified; queried boundary is an allocation observation artifact, not a replacement for the contract-reconstructed boundary |
| Forest Atlas compartments layer 37 | `Liberia_Forest_Atlas/MapServer/37` | harvest-attribution context | candidate; Area K completeness unresolved |
| Forest Atlas annual coupe layer 38 | `Liberia_Forest_Atlas/MapServer/38` | production-geometry candidate | candidate; Area K completeness unresolved |
| JRC GFC2020 V3 | `JRC/GFC2020/V3` | 2020 baseline | pinned local Area K raster in `area-k-real-005` |
| Hansen GFC v1.13 through 2025 | `UMD/hansen/global_forest_change_2025_v1_13` | deforestation / tree-cover loss | pinned local Area K lossyear/treecover rasters |
| JRC TMF v2025 | `projects/JRC/TMF/v1_2025` | deforestation and degradation | pinned local Area K deforestation/degradation/duration/intensity rasters |
| RADD alerts | `projects/radar-wur/raddalert/v1` | alert / degradation context | frozen local Area K Alert/Date rasters |
| Sentinel-2 visual context | `COPERNICUS/S2_SR_HARMONIZED` | confirmation | pinned AOI/regional visual rasters and Tier-2 event crops |
| LLA cadastre, Area K AOP/block maps, LiberTrace/CoC | `_pending_` | source/tenure/linkage | required evidence gaps |

The final counterpart handoff at
`/Users/server/projects/eudr-dmi-gil/out/okf_handoffs/eudr-wood-liberia-fmc-area-k.json` references
manifest hash `bef58f2d0c372231d76e8b213eb929884f6acd60a8a01de476998fb78f457084` for the
`area-k-real-005` evidence package. That package is referenced, not copied.

The round-4 report does not admit coffee, cocoa, palm, rubber or any other non-wood commodity mask
as wood attribution. The concession AOI is source context and a screening area, not a production
plot. Production-geometry and chain-of-custody sources remain unresolved evidence gaps.

For process/artifact semantics, use the primary registry's observer metadata fields:
`observation_target`, `observer_process`, `observer_family`, `observation_artifact_role`,
`upstream_dependencies`, and `independence_notes`. Those fields distinguish a source record, an
observation-generating process, a configured run, and an emitted artifact.
