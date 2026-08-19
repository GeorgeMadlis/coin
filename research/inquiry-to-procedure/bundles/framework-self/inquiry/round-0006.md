---
type: Event
title: "Round 6: publish command, metadata catalog, and evolution visualization"
description: okf-fc gains publish/catalog/evolution-visualization commands; bundles/framework-self published as the first real snapshot into the new ../okf-bundle-snapshots viewer repository.
fc-axis: INQUIRY
fc-round: 6
fc-move: evidence
fc-stage: enrichment
fc-party: claude
fc-type-at-round: resolved
fc-touches: []
fc-status: open
timestamp: 2026-07-19
---

# Move

Infrastructure round, mirroring round-0002 and round-0005: evidence added to tooling and to the
project's derived-artifact record, not to bundle content. `docs/framework_v3.md` §3.7 calls for
derived artifacts (rendered HTML, exported zips, cross-bundle catalogs) to be commit-pinned; this
round is the first to populate a durable, human-facing archive of those artifacts, rather than a
throwaway local `_site/`/snapshot directory: a new sibling repository, `../okf-bundle-snapshots`,
versions published snapshots, a searchable SQLite metadata catalog, and per-bundle evolution
visualizations.

# Evidence added

- New `../okf-bundle-snapshots` repository (ordinary git repo, `main` branch): scaffolded with a
  `README.md` (purpose, the `file://` usage contract, the repo layout, and two rules -- snapshots
  are append-only; the repo holds only okf-fc-generated artifacts, never hand-authored sources or
  Python) and a `.gitattributes` marking `*.html`/`*.svg` as text and `*.zip`/`catalog.db` as
  binary.
- `tools/src/okf_fc/render.py`: `write_manifest` now also extracts, from the frontmatter already
  parsed for every markdown file, a `rounds` list (one entry per `inquiry/round-*.md`: round,
  date, party, move, stage, type-at-round, status, summary, record path -- backfilled from the
  bundle's own `log.md` table where a frontmatter field is absent) and a `concepts` list (one
  entry per remaining concept file carrying a `type` key: path, type, title, description, level,
  axis, round, supersedes). This makes `manifest.json` self-sufficient for catalog rebuilding: no
  source-repository access is needed to reconstruct the catalog from snapshots already on disk.
- New `tools/src/okf_fc/catalog.py`: a stdlib-`sqlite3` metadata catalog, `<dest>/catalog.db`
  (tables `bundles`, `snapshots`, `rounds`, `concepts`) plus the same content as a flat, sorted
  `catalog.json`. `rebuild(dest)` scans every `<bundle-id>/<snapshot>/manifest.json` under `dest`
  and regenerates the catalog, each bundle's `index.html` (snapshot table + embedded evolution
  graph), and the top-level `index.html` (all bundles, latest snapshot, catalog links) from
  scratch every time -- there is no separate incremental-upsert path, so `okf-fc publish` and
  `okf-fc catalog rebuild` cannot drift apart. `okf-fc catalog query` runs read-only `SELECT`
  statements only (refusing anything else) against `catalog.db`; `okf-fc catalog show
  <bundle-id>` prints a bundle's metadata and round table.
- New `tools/src/okf_fc/evolution_viz.py`: a deterministic, dependency-free SVG
  (`evolution.svg`, embedded inline in the per-bundle `index.html`) with one horizontal swimlane
  per party, in first-appearance order, so the sequential multi-observer realization
  (`docs/framework_v3.md` §2.2) is visible directly; one node per round, colored by `fc-stage`
  and labelled with `fc-move` (contestation rounds additionally show `fc-type-at-round`); a
  supersession marker on any round at which a concept's `fc-supersedes` was set; and, below the
  lanes, a stage-trajectory strip plus a type-trajectory strip restricted to contestation rounds.
  Every round node links to that round's rendered page in the newest snapshot.
- New `tools/src/okf_fc/publish.py`: `okf-fc publish <bundle_dir> --dest <snapshots_repo>`
  renders a self-contained snapshot + structure visualization + manifest into
  `<dest>/<bundle-id>/<date>-r<NNNN>-<shorthash>/` (round = the bundle's highest inquiry round;
  shorthash = the source repo's `HEAD`), zips it deterministically, and calls the same
  `catalog.rebuild` used by `okf-fc catalog rebuild`. Refuses to run against a dirty git worktree
  unless `--allow-dirty` is passed (`docs/agent-guide.md`'s Canonical-State Rule: only committed
  HEAD is publishable; an unpinned snapshot is a future Type III dispute about its own
  provenance), and refuses to overwrite an existing snapshot directory or zip. Does not commit in
  the destination repo -- it prints the `git add`/`git commit` commands to run there.
- `bundles/framework-self` published as the first real snapshot into `../okf-bundle-snapshots`
  at this round's commit, committed there as the repository's initial content commit (after the
  scaffold commit); see the root `log.md` line for this round for the pinned commit hash of that
  repository.
- New `tools/tests/test_publish.py`, `test_catalog.py`, `test_evolution_viz.py`: dirty-worktree
  refusal; publishing twice leaves the first snapshot and zip byte-for-byte untouched while the
  indexes and catalog come to reflect the newer one; `catalog rebuild` reproduces `catalog.json`
  byte-identically across repeated runs with no source changes; the `rounds` table matches the
  bundle's `inquiry/round-*.md` frontmatter exactly; `evolution.svg` has one node per round, one
  lane per distinct party, and is byte-identical across runs; `catalog query` rejects
  non-`SELECT` SQL. Full suite passes (31 tests: 16 pre-existing + 15 new).

# Effect on state

Context window: added the requirement (stated directly, not contested) that published snapshots
accumulate in a durable, queryable, human-facing archive outside this repository, with a
metadata catalog and an evolution visualization as required deliverables.

Frame: unchanged for bundle content. `okf-fc` gains a fourth output surface (publish + catalog +
evolution) alongside render/snapshot; the existing render/snapshot code paths and their tests are
untouched.

# Resulting revisions

None to bundle concept files -- this round adds tooling
(`tools/src/okf_fc/{catalog,evolution_viz,publish}.py`, `render.py`'s manifest extension,
`cli.py`'s new subcommands, and their tests), one section to `bundles/README.md`, and the new
`../okf-bundle-snapshots` sibling repository, none of which are bundle concepts subject to
`fc-supersedes`. `fc-touches` is therefore empty, per the convention from
`inquiry/round-0003.md`'s SPEC-GAP finding (touches to non-concept, out-of-bundle, or generated
files belong in this prose, not in `fc-touches`).

# Classification rationale

An **evidence** move about inspection/archival infrastructure, mirroring round-0002 and
round-0005 exactly: it adds capability (a durable, queryable, cross-session archive and its
metadata catalog) with no standing rival position to resolve, so it carries no live
counter-position and is not contestation. `fc-stage: enrichment` per `docs/framework_v3.md` §2.2.
