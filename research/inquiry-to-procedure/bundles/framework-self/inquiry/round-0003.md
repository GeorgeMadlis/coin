---
type: Event
title: "Round 3: second-observer validation of rounds 1-2"
description: Claude Code validates the self-bundle and HTML renderer against docs/framework_v2.md section 3; fixes two mechanical defects, records two judgment differences and two spec gaps for human reconciliation.
fc-axis: INQUIRY
fc-round: 3
fc-move: objection
fc-party: claude
fc-type-at-round: II
fc-touches: [reproduction/code.md]
fc-status: open
timestamp: 2026-07-16
---

# Move

Structural validation of `bundles/framework-self/` and `tools/src/okf_fc/render.py` against the provisional bundle spec in `docs/framework_v2.md` section 3, run programmatically (tree conformance, frontmatter parsing, link resolution, provenance hashing, ledger append-only-ness, renderer determinism) rather than by inspection. Two objective (SPEC-MECH) defects were found and fixed by supersession; two labeling choices are recorded as JUDGMENT (Type II) differences and left untouched; two spec silences are recorded as SPEC-GAP with proposed conventions.

Process note, corrected after checking the remote (my first pass judged this from a stale unfetched local `main` and got it wrong): `main` does contain both pilots' content, but not via "two merged PRs" as the task assumed. Round 1's self-bundle content was never its own PR — `codex/pilot-self-bundle` never diverged from `main`; that content shipped as part of `a1fc43c "Initial observer disagreement framework"`, pushed directly to `main` with no PR (repo bootstrap), per `reproduction/code.md`'s own note about predating git init. Round 2's renderer content merged via the repo's one and only PR, `#1` (`codex/pilot-html-renderer` -> `main`, merge commit `d699396`). This branch is based on `codex/pilot-html-renderer`'s tip (`3d9f217`), whose tree is byte-identical to `origin/main`'s (confirmed via `git diff origin/main 3d9f217`), so branching point is not in question.

# Evidence added

- Recomputed `sha256sum docs/framework_v2.md`: `c5240cdfcf1f22948f9ece4d1b778195415e64c83c56737e385773bf50102de8` — matches the hash already recorded in `reproduction/data.md` and `inquiry/round-0001.md`. No provenance defect there.
- `git diff a1fc43c -- bundles/climate-repro-pilot bundles/eudr-estonia-aoi bundles/historical-type-iii bundles/self-inquiry-eudr-docs` is empty: the four Step-7 stub READMEs are untouched.
- All 30 relative `.md` links in the bundle source resolve on the filesystem (checked programmatically); tree matches the specified layout exactly (no missing/extra files outside `_site/`); all mandated frontmatter keys (`fc-level`, `fc-axis`, `fc-round` on axis concept files; `fc-group` on all 11 foundations files; `type: Event`, `fc-move`, `fc-party`, `fc-type-at-round`, `fc-touches`, `fc-status` on round files) are present and parse; root and bundle `log.md` are append-only (verified via `git log -p`, round 0's line is byte-identical across both commits that touch the file).
- Renderer bug (SPEC-MECH, fixed): `_rewrite_href` in `tools/src/okf_fc/render.py` could not resolve relative `.md` links that escape the bundle root — exactly the links section 3 requires into `docs/framework_v2.md` (e.g. `reproduction/data.md`'s `[docs/framework_v2.md](../../../docs/framework_v2.md)`). It left such hrefs byte-for-byte unchanged and marked them `⚠ unresolved`, even though the target exists. Unchanged is wrong regardless: the rendered page lives one directory level deeper (under `_site/`) than the source markdown file, so the correct href needs one more `../` than the source. Confirmed broken in the committed `_site/` in 6 files / 8 link instances: `r/results.html`, `inquiry/round-0001.html`, `s/specification.html` (×2), `reproduction/data.html`, `reproduction/code.html`, `pf/full-context.html` (×2) — each resolving to `bundles/docs/framework_v2.md` (nonexistent) instead of `docs/framework_v2.md`.
  PR #1's description states this was intentional: "Out-of-bundle Markdown references... are left as written and marked with the visible unresolved indicator so inspection stays honest without failing the render." I still classify this SPEC-MECH, not JUDGMENT, for two reasons: (1) the task's Phase-1 Links check is explicit and unconditional — "every relative .md link in the bundle resolves (including links into docs/framework_v2.md)... unresolved -> SPEC-MECH" — leaving no room for an intentional-unresolved exception; (2) the stated rationale doesn't actually hold even on its own terms — "left as written" implies the link stays clickable-if-unflagged, but it was never clickable from the rendered page's actual location (off by one directory), so the design didn't achieve "honest inspection," it produced a warning label on top of a link that was simply wrong.
- Fix: `_rewrite_href` now falls back to real-filesystem resolution for any `.md` target outside the bundle's own concept set, and computes the rewritten href relative to the *actual* rendered-page location rather than assuming it matches the source location. Verified: regenerating `bundles/framework-self/_site/` now produces zero `⚠ unresolved` spans, `reproduction/data.html` links to `../../../../docs/framework_v2.md` which resolves on disk, running the documented regen command (`okf-fc render bundles/framework-self`, no `--out`) twice in a row is byte-identical, and the diff against the previously-committed `_site/` touches exactly the 6 affected files. Added a regression test, `test_link_escaping_bundle_to_an_existing_file_resolves_correctly`, to `tools/tests/test_render.py`; full suite (8 tests) passes.
- Placeholder bug (SPEC-MECH, fixed): `reproduction/code.md`'s pinned-commit field was still the literal placeholder `PINNED-AT-MERGE: <fill on merge>`. Filled with `a1fc43cc83a6f223843f8318f2f92886b6769eb5` — not a `codex/pilot-self-bundle` merge commit (none exists; see Move above), but the actual commit that introduced this bundle content, which is the closest honest referent.

# Effect on state

Context window: added the actual git history of this repository (branch topology, per-file first-introducing commit) to what round 1-2 assumed (a linear "two merged PRs" history).

Frame: unchanged for bundle content; the renderer's link-resolution frame was corrected from "only resolve links inside the bundle's own file set" to "resolve any relative `.md` link against the real filesystem, adjusting for output nesting depth."

# Resulting revisions

- `tools/src/okf_fc/render.py` — `_rewrite_href` (and its callers `_rewrite_links`, `_markdown_to_html`, `_render_page`, `_render_site_index`, `render_bundle`) now thread `bundle` and `out` absolute paths through so out-of-bundle links can be resolved and rewritten correctly. Not a bundle concept file, so no `fc-supersedes` entry; ledgered here in prose per the "No Silent Edits" rule.
  - `tools/tests/test_render.py` — added `test_link_escaping_bundle_to_an_existing_file_resolves_correctly`.
  - `bundles/framework-self/_site/{r/results,inquiry/round-0001,s/specification,reproduction/data,reproduction/code,pf/full-context}.html` — regenerated; these are derived files, not source concepts, so likewise no `fc-supersedes`.
- `reproduction/code.md` — `fc-supersedes: reproduction/code.md@r1`; `fc-round` bumped 1 -> 3; pinned-commit placeholder filled as described above.

# Classification rationale

The two fixed items are Type I in nature: mechanical/data defects (a wrong relative path computation; an unfilled placeholder) resolvable by correcting the mechanism or supplying the missing data, with no framing dispute involved — now resolved. What remains open after this round is Type II: two labeling choices where Codex's frontmatter tagging is spec-permitted but I would have tagged differently (see Findings below), and two points where the spec itself is silent and each agent would need to invent a convention (also below). Per the task's finding-class discipline, JUDGMENT and SPEC-GAP items are recorded, not fixed — unilaterally resolving them would erase the dual-observer signal this repository exists to collect. `fc-status: open` because those items are unresolved pending human reconciliation.

# Findings

## JUDGMENT (Type II — not fixed)

1. **`agent-contract.md` frontmatter axis.** Codex did: tagged `fc-axis: INQUIRY`. I would: omit `fc-axis` entirely, since `agent-contract.md` is a bundle-level policy file alongside `index.md`/`answer.md`/`log.md` (section 3.2's top-level tier), not itself a concept on the PF/S/R/REPRO/INQUIRY axes that 3.3's template defines. Why it matters: minor — doesn't break the Phase-1 checks, but could mislead an agent doing axis-based routing per the contract's own Consumption rule ("a question about revisions asks for INQUIRY" — `agent-contract.md` isn't a revision record).
2. **`answer.md` frontmatter axis.** Codex did: tagged `fc-axis: R`. I would: omit `fc-axis`, since `answer.md` is explicitly the cross-axis L0 root ("links to axes" per 3.2), not confined to Results. Why it matters: cosmetic; doesn't affect navigation, since `agent-contract.md`'s Consumption rule already routes "broad question -> L0/L1" to `answer.md` by file identity, not by frontmatter.

## SPEC-GAP (not fixed — proposed convention for `spec/SPEC.md`, Step 3)

1. **`fc-touches` scope.** `inquiry/round-0002.md`'s `fc-touches` lists `_site/ (generated)` and `bundles/README.md` alongside what round-0001.md uses as bundle-relative concept paths. Section 3.4 shows `fc-touches` as a list of bundle concept-file paths ("concepts updated in consequence") but doesn't define behavior for touches outside the bundle or to non-concept generated output. I did not edit `round-0002.md` — round files are append-only history, not concept files subject to supersession, and rewriting one after the fact would itself violate the ledger-discipline this validation is checking for. Proposed convention: `fc-touches` values must be bundle-relative paths to existing concept files only; touches to files outside the bundle or to generated/derived output belong in prose under "Effect on state," not in `fc-touches`.
2. **`fc-irreducibility` mandate scope.** Section 3.3's worked example lists `fc-irreducibility` on every PF/S/R/REPRO concept file, but the task's restated Phase-1 checklist for this validation only mandates `fc-level`, `fc-axis`, `fc-status`, `fc-round` "where the spec mandates them" — and `fc-status` itself is a round-file/inquiry-level field per 3.4, not a concept-file field per 3.3's own template. In this bundle only `s/specification.md` sets `fc-irreducibility` (to `none`); the other ~24 concept files omit it. I did not add values to the other files: most of this bundle's claims are explicitly "not yet proven" (see `r/results.md`), so there is no established result yet to classify as computationally vs. factually irreducible, and inventing a classification would risk exactly the kind of unfounded content addition the SPEC-CONTENT class exists to catch. Proposed convention: `fc-irreducibility` is mandatory only once a concept file states a result or claim that could plausibly be re-derived (i.e., is a candidate for the P4/P5 machinery), not on every concept file unconditionally.
