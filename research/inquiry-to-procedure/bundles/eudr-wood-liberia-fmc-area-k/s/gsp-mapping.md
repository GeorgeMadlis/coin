---
type: Method
title: "GSP mapping"
fc-level: 2
fc-axis: S
fc-round: 4
fc-supersedes: "s/gsp-mapping.md@round-0003"
gsp-engine: gee
gsp-aoi: "liberia_fmc_area_k_contract_boundary"
---
# GSP Mapping

The verified round-4 GSP pipeline is inherited from the parent wood path:

1. Admit FMC Area K as concession-level AOI/context.
2. Pin boundary observation artifacts separately, including the contract-reconstructed GeoJSON and
   the Forest Atlas FMC query output; record the reconstruction/query process for each.
3. Clip or query baseline, forest-type, deforestation, degradation, alert and confirmation sources.
4. Preserve deforestation and degradation as separate streams.
5. Record production geometry and source linkage separately from map disturbance.
6. Emit evidence gaps when AOP, harvesting-block, tree/log or chain-of-custody records are absent.

The current counterpart run completed the raster/alert/report path for steps 1-6:

- JRC GFC2020 V3 is used as the 2020 forest baseline.
- Hansen GFC v1.13 lossyear is intersected with the JRC 2020 baseline for post-cutoff loss.
- Hansen treecover2000 >= 10% is retained as a parallel canopy-baseline comparison.
- JRC TMF v1_2025 deforestation and degradation are reported as separate process-family outputs.
- RADD Sentinel-1 alerts are frozen at acquisition time and separated into confirmed/high-confidence
  and low-confidence alert classes.
- Sentinel-2 baseline/recent/regional imagery is visual context and confirmation support, not a
  source-linkage substitute.

The report maps this pipeline explicitly: page 5 maps JRC forest 2020, page 6 maps Hansen/JRC loss,
TMF deforestation, TMF degradation and RADD alert classes, and page 7 maps Sentinel-2 before/after
visual context.
