# REPRO - Reproduction

- [gee-auth.md](gee-auth.md) - authentication and acquisition context.
- [code.md](code.md) - counterpart code, pinned commit, run command.
- [data.md](data.md) - asset pins and checksums.
- [environment.md](environment.md) - runtime.
- [lineage.md](lineage.md) - why this bundle imports no legacy lineage.

The source bundle's machine-readable manifest, GeoJSON masks, contact sheet PDF, generated PDF, and
canonical `report.html` are intentionally omitted from this public COIN copy.

The counterpart, evidence bundle, and report artifacts referenced here live in
`GeorgeMadlis/eudr-dmi-gil`'s `audit/evidence/**`; this source bundle records hashes and paths
without copying evidence content.

## Publish history

Round 1 published snapshot `2026-08-11-r0001-4ba9827`. Round 2 supersedes it because the pinned
before/after Sentinel-2 baseline panel contained a half-black/nodata left image and because the
package lacked `fazenda_sucuri_contact_sheet_guide.html`.

Round 7 supersedes snapshot `2026-08-12-r0006-b969a23` because page 4 still showed a missing
regional-overview image. The regenerated report/contact sheet are pinned to the round-7 handoff.

Expected publish command:

`python3 tools/okf_gsp.py publish eudr-coffee-brazil-fazenda-sucuri --dest /Users/server/projects/okf-bundle-snapshots --evidence-handoff /Users/server/projects/eudr-dmi-gil/out/okf_handoffs/eudr-coffee-brazil-fazenda-sucuri.json`
