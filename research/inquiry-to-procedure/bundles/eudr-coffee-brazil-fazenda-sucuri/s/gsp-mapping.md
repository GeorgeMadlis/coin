---
type: Method
title: "GSP mapping"
fc-level: 2
fc-axis: S
fc-round: 8
fc-supersedes: "s/gsp-mapping.md@round-0007"
gsp-engine: gee
---
# GSP mapping

The conceptual method engine remains `gee`, because the inputs were acquired from Earth Engine
datasets. The execution engine for this pinned run is `local-pinned-raster`: the canonical CLI
processed local GeoTIFF/GeoJSON inputs and emitted a deterministic report bundle under
`audit/evidence/2026-08-12/fazenda_sucuri_screening_aoi_evidence_freeze_20260812T121500Z`.
The current verified evidence bundle is
`audit/evidence/2026-09-11/fazenda_sucuri_screening_aoi_evidence_freeze_20260911T130900Z`.

The current commodity mask is computed from source inputs as `latest_2024_coffee OR
baseline_2020_coffee`; the new-commodity mask remains `latest_2024_coffee AND NOT
baseline_2020_coffee`.

All raster intersections are materialized through the counterpart report generator. This OKF bundle
does not recalculate or copy evidence rasters; it records the pinned paths and hashes in
`../reproduction/source-evidence.json`.

Round 8 adds task-specific FDP/JRC threshold and morphology products to the materialized artifact
set. The diagnostic grid is EPSG:6933 at 10 m, using `rasterize_polygon_all_touched`; JRC forest is
nearest-resampled, FDP probability is bilinear-resampled before thresholding, and FDP masks require
valid observations in both 2020 and 2024 within the AOI.

The new PNG products include FDP 2020 masks, FDP 2024 masks, FDP-new-coffee masks,
`JRC2020 AND FDP2024` overlaps, `JRC2020 AND FDP-new-coffee` overlaps at all five thresholds,
FDP probability surfaces, a JRC forest diagnostic, and two morphology composites at 0.025. The
machine-readable diagnostic outputs are
`evidence/coffee_jrc_diagnostics/fdp_jrc_threshold_metrics.csv` and
`evidence/coffee_jrc_diagnostics/fdp_jrc_morphology_diagnostics.json` in the published evidence
package.
