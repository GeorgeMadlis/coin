---
type: Event
title: "Round 5: self-contained snapshot renderer and structure visualization"
description: okf-fc gains a zip-portable self-contained render mode, a manifest recording function, and a deterministic bundle-structure SVG/HTML visualization; no bundle concept file content changed.
fc-axis: INQUIRY
fc-round: 5
fc-move: evidence
fc-stage: enrichment
fc-party: claude
fc-type-at-round: resolved
fc-touches: []
fc-status: open
timestamp: 2026-07-19
---

# Move

Infrastructure round, mirroring round-0002: evidence added to the bundle's tooling rather than
its content. `docs/framework_v3.md` §3.7 (Canonical state and derived artifacts) states that
rendered/exported artifacts are derived, commit-pinned copies of the committed HEAD; this round
makes one such artifact — the self-contained snapshot — actually zip-portable, which the
existing renderer (as of round-0003) was not: `_rewrite_href`'s round-3 fix correctly resolves
out-of-bundle links (e.g. into `docs/framework_v2.md`) against the real filesystem, but the
resulting href still points at that real filesystem location, which breaks the moment the
rendered output is copied or zipped and opened somewhere else. `bundles/README.md`'s existing
`_site/` inspection flow is unaffected: this round's constraint was that the default
(non-self-contained) render output must stay byte-identical unless a test proves it wrong, and
no such test was introduced.

# Evidence added

- `tools/src/okf_fc/render.py` gains `self_contained: bool` on `render_bundle`. Every relative
  link target resolving to a real file outside the bundle root is now vendored into the output
  under `_refs/<repo-relative-path>` (rendered through the same page template for Markdown,
  wrapped in a minimal `<pre>` page for other textual extensions, copied verbatim for binaries)
  and the link rewritten to the vendored copy, one level deep — links inside a vendored page
  that would require vendoring a second time are left as unresolved spans (the existing
  round-3 convention) rather than recursing. `render_bundle` also gains `write_manifest` (writes
  `manifest.json`: every bundle source file's SHA256, the source repo's `git rev-parse HEAD`
  or `"unknown"`, and the bundle's current highest round/`fc-status` read from its
  `inquiry/round-*.md` frontmatter) and `create_snapshot_zip` (a deterministic zip: fixed
  per-entry timestamps and a fixed `create_system`, so identical input trees produce
  byte-identical archives).
- New `tools/src/okf_fc/structure_viz.py`: `render_structure` writes `structure.svg` and
  `structure.html` (the same SVG embedded inline) at a snapshot's root — a deterministic
  columnar diagram (no external renderer, no randomness) of the bundle's concept files, grouped
  by axis (Root, PF, S, R, REPRO, INQUIRY, inferred from the top-level path segment) and stacked
  by `fc-level`, with solid edges for the markdown link graph, dashed for `fc-supersedes`, and
  dotted for `fc-touches` (restricted to entries naming an existing concept file, per the
  fc-touches SPEC-GAP recorded in `inquiry/round-0003.md`). Each node links to its rendered page.
- `tools/src/okf_fc/cli.py`: `okf-fc render` gains `--self-contained`; new `okf-fc snapshot
  <bundle_dir> -o <out_dir> [--zip <zipfile>]` composes self-contained render + structure
  visualization + manifest + optional deterministic zip.
- Verified against this bundle: `okf-fc render bundles/framework-self` (no flags) reproduces the
  committed `_site/` byte-for-byte (diff empty). `okf-fc snapshot bundles/framework-self -o
  <tmp> --zip <tmp>.zip` run twice produces byte-identical `manifest.json`, `structure.svg`, and
  zip archives; the zip, unzipped to a fresh directory with no relation to this checkout, opens
  `reproduction/data.html` and `reproduction/code.html` via `file://` and both pinned links to
  `docs/framework_v2.md` resolve to a working local copy at `_refs/docs/framework_v2.html`.
- `tools/tests/test_render.py` gains three tests (out-of-bundle Markdown link vendored with a
  working relative href; non-Markdown textual target wrapped in a `<pre>` page; self-contained
  double-render byte-identity). New `tools/tests/test_snapshot.py` covers the manifest's file
  list/SHA256/round-state fields, zip byte-identity across two builds, and the structure SVG's
  node count and a known link edge, also checked for byte-identity across two builds. Full suite
  (14 tests) passes.
- `bundles/README.md` — one paragraph added documenting `okf-fc snapshot`, the zip-portability
  contract, and the structure visualization; not a bundle concept file, so no `fc-supersedes`
  entry, ledgered here per "No Silent Edits."

# Effect on state

Context window: added the requirement (stated directly, not contested) that the inspection
artifact be a zip-portable, `file://`-safe snapshot, plus a structure visualization as a
required deliverable.

Frame: unchanged for bundle content. The renderer's frame gains a second output mode
(self-contained vendoring) alongside the existing real-filesystem-linking mode from round 3;
the default mode's behavior and output are untouched.

# Resulting revisions

None to bundle concept files — this round adds tooling (`tools/src/okf_fc/render.py`,
`tools/src/okf_fc/structure_viz.py`, `tools/src/okf_fc/cli.py`, their tests) and one paragraph
to `bundles/README.md`, none of which are bundle concepts subject to `fc-supersedes`. `fc-touches`
is therefore empty per the convention proposed in `inquiry/round-0003.md`'s SPEC-GAP finding
(touches to non-concept, out-of-bundle, or generated files belong in this prose, not in
`fc-touches`).

# Classification rationale

This is an **evidence** move about inspection infrastructure, mirroring round-0002 exactly: it
adds tooling capability without revising any bundle claim or adjudicating a disagreement, so it
carries no live counter-position and is not contestation. Unlike round-0002 (pre-`fc-stage`, left
unclassified until back-assigned as enrichment in `inquiry/index.md`), this round sets
`fc-stage: enrichment` directly at authoring time, per `docs/framework_v3.md` §2.2: it adds
capability to the record (a new, more robust derived-artifact mode) with no standing rival
position to resolve.
