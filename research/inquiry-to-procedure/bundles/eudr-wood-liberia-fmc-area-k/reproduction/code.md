---
type: Runbook
title: "Counterpart code"
fc-level: 2
fc-axis: REPRO
fc-round: 8
fc-supersedes: reproduction/code.md@round-0004
gsp-counterpart: single-earth/eudr-dmi-gil@61285bd6ac2ef45708dee660620bd9db4181d3c2
---
# Counterpart Code

Counterpart: `single-earth/eudr-dmi-gil@61285bd6ac2ef45708dee660620bd9db4181d3c2`.

The clean handoff records the full canonical CLI command in
`/Users/server/projects/eudr-dmi-gil/out/okf_handoffs/eudr-wood-liberia-fmc-area-k.json`.
In short, it runs:

```sh
EUDR_DMI_GENERATED_AT_UTC=2026-08-17T09:30:00+00:00 EUDR_DMI_GIT_COMMIT=61285bd6ac2ef45708dee660620bd9db4181d3c2 EUDR_DMI_EVIDENCE_ROOT=audit/evidence PYTHONPATH=src .venv/bin/python -m eudr_dmi_gil.reports.cli --aoi-id liberia_fmc_area_k_contract_boundary --aoi-geojson aoi_json_examples/liberia_fmc_area_k_contract_boundary.geojson --bundle-id area-k-real-005 --out-format both --evidence-only-assessment --enable-hansen-post-2020-loss --loss-dataset-end-year 2025 --end-year 2025 --analysis-target-resolution-m 30 ...
```

Tracked counterpart status is clean for the handoff (`counterpart_dirty: false`). Untracked local
acquisition outputs remain derived evidence payload, not source.

Round 8 re-pins the counterpart to `61285bd`, which fixes two report-generator defects rather than
re-running the analysis: the `datasets` registry previously omitted JRC TMF/RADD/Hansen-canopy even
though the Methods section already documented them, and per-metric `provenance` was hardcoded to a
placeholder for every metric outside an 8-name legacy allowlist instead of the real dataset/process
that computed it. All 63 metric values and all 8 mapped evidence PNGs are byte-identical to the
`696ca85` / `area-k-real-004` run; report.json/html/pdf/metrics.csv hashes changed only because their
dataset-table and provenance-column content changed. See
`reproduction/source-evidence.json#counterpart_fix_round_005` for the verification detail.
