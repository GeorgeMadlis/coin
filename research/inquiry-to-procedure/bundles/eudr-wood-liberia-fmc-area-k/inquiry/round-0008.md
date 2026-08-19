---
type: Event
title: "Round 8: fix"
fc-axis: INQUIRY
fc-round: 8
fc-move: fix
fc-stage: consolidation
fc-party: claude
fc-status: open
fc-touches: "answer.md, r/results.md, r/artifact-inventory.md, r/overview.md, reproduction/code.md, reproduction/data.md, reproduction/environment.md, reproduction/index.md, s/data-sources.md, s/modeling.md, s/report-structure.md, s/specification.md"
---
# Move
Re-pinned to counterpart commit 61285bd (branch work/tmf-radd-evidence-observers), which fixes two report-generator completeness defects rather than re-running the analysis. (1) The canonical report's datasets registry (report.html 'Datasets' table) only ever appended aoi_geometry_input, Hansen GFC, JRC GFC2020 and hansen_lossyear; when TMF/RADD support landed no matching datasets.append() was added, so the Methods section documented JRC TMF deforestation/degradation and RADD alerts (with real checksums/source URLs) while the Datasets table silently omitted all three plus the Hansen-canopy secondary baseline. (2) _canonical_metrics() hardcoded provenance to the placeholder string 'source_report.metrics' for every metric outside an 8-name legacy allowlist, discarding the real per-metric MetricRow.source value (e.g. jrc_tmf, radd, hansen_treecover2000+hansen_lossyear) that analysis stages already compute and that _metrics_from_rows() was dropping before it reached report.json. Fixed both in the counterpart (report.json's metrics schema gained an optional source property) and reproduced: report.json now lists 8 datasets (was 4) and 0 of 63 metrics carry the placeholder (was most). All 63 metric values and all 8 mapped evidence PNGs are byte-identical to the round-4 (696ca85/area-k-real-004) run, confirming this is a provenance-completeness fix, not a re-analysis; human_review_required / pinned-not-reproduced is unchanged. Regenerated the derived contact sheet from the new report.pdf and refreshed every handoff/report/manifest/contact-sheet hash referenced from this bundle's current-state files.

# Evidence added
- eudr-dmi-gil@61285bd: schemas/reports/aoi_report_v2.schema.json, src/eudr_dmi_gil/reports/cli.py, src/eudr_dmi_gil/reports/report_model.py (full eudr-dmi-gil test suite: 244 passed).
- Reproduced area-k-real-005 at eudr-dmi-gil/audit/evidence/2026-08-17/area-k-real-005 from the same pinned local inputs as area-k-real-004; jq diff of report.json metrics values against area-k-real-004: 0 differences across 63 metrics; sha256 of all 8 mapped evidence PNGs unchanged.
- reproduction/source-evidence.json#counterpart_fix_round_005 records the fix, the verification method and verdict_unchanged: true.

# Effect on state
This consolidation round records `fix` and keeps provenance bounded by pinned evidence.

# Resulting revisions
- `answer.md` supersedes `answer.md@round-0004`.
- `r/results.md` supersedes `r/results.md@round-0004`.
- `r/artifact-inventory.md` supersedes `r/artifact-inventory.md@round-0004`.
- `r/overview.md` supersedes `r/overview.md@round-0004`.
- `reproduction/code.md` supersedes `reproduction/code.md@round-0004`.
- `reproduction/data.md` supersedes `reproduction/data.md@round-0004`.
- `reproduction/environment.md` supersedes `reproduction/environment.md@round-0004`.
- `reproduction/index.md` supersedes `reproduction/index.md@round-0004`.
- `s/data-sources.md` supersedes `s/data-sources.md@round-0004`.
- `s/modeling.md` supersedes `s/modeling.md@round-0004`.
- `s/report-structure.md` supersedes `s/report-structure.md@round-0004`.
- `s/specification.md` supersedes `s/specification.md@round-0004`.

# Classification rationale
**fc-stage: consolidation** - recorded by `okf-gsp round` for the stated move.
