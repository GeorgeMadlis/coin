---
type: Runbook
title: "GEE auth"
fc-level: 2
fc-axis: REPRO
fc-round: 4
fc-supersedes: "reproduction/gee-auth.md@round-0001"
gsp-engine: gee
---
# GEE Auth

The parent method-family engine is `gee`. The round-4 report itself was generated from local pinned
rasters, but those rasters were produced from GEE-backed acquisitions recorded in the counterpart
input manifests.

Recorded acquisition fields:

- acquisition manifest timestamp: `2026-08-15T10:35:15Z`;
- AOI buffer: `2000 m`;
- AOI GeoJSON SHA-256:
  `db386f478d9b461418155cb5db4ed9bd70d26d0b554786d61e76aad6280a210b`;
- Sentinel-2 scene diagnostics: 2020 scene count `44`; recent scene count `23`;
- least-cloudy Sentinel-2 dates: `2020-02-15` and `2026-01-09`;
- RADD freeze timestamp: `2026-08-15T09:12:17Z`.

No independent qualifying rerun was performed for this round, so provenance remains
`pinned-not-reproduced`.
