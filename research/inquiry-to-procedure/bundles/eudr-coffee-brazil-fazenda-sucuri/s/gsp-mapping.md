---
type: Method
title: "GSP mapping"
fc-level: 2
fc-axis: S
fc-round: 7
fc-supersedes: "s/gsp-mapping.md@round-0006"
gsp-engine: gee
---
# GSP mapping

The conceptual method engine remains `gee`, because the inputs were acquired from Earth Engine
datasets. The execution engine for this pinned run is `local-pinned-raster`: the canonical CLI
processed local GeoTIFF/GeoJSON inputs and emitted a deterministic report bundle under
`audit/evidence/2026-08-12/fazenda_sucuri_screening_aoi_evidence_freeze_20260812T121500Z`.

The current commodity mask is computed from source inputs as `latest_2024_coffee OR
baseline_2020_coffee`; the new-commodity mask remains `latest_2024_coffee AND NOT
baseline_2020_coffee`.

All raster intersections are materialized through the counterpart report generator. This OKF bundle
does not recalculate or copy evidence rasters; it records the pinned paths and hashes in
`../reproduction/source-evidence.json`.

Page 4 regional context is also materialized by the counterpart report generator. In this round it
uses the local recent Sentinel-2 raster fallback because no dedicated regional raster was supplied.
