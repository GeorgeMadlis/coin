# Migration Brief: Recorded Inquiries Architecture

Status: design/discovery only
Created: 2026-08-29

This brief designs a coordinated migration across four repositories:

1. `GeorgeMadlis/observer-disagreement-framework`
2. `GeorgeMadlis/coin`
3. `GeorgeMadlis/connectednature-site`
4. `GeorgeMadlis/connectedinfo-site`

Do not perform the implementation from this brief directly. Later implementation prompts must follow the dependency order above, read repository-local instructions first, validate against current source, and avoid pushing changes unless explicitly instructed.

## Inspection Basis

The common VS Code workspace file found at `observer-disagreement-framework/docs/paper/observer-disagreement-framework.code-workspace` includes `observer-disagreement-framework` and `okf-bundle-snapshots`, not all four target repositories. The writable shared-workspace-root condition was therefore not satisfied, so this brief is placed in the prompt's fallback location: `coin/research/inquiry-to-procedure/MIGRATION-recorded-inquiries-architecture.md`.

Repositories and source states inspected:

| Repository | HEAD inspected | Working-tree note |
|---|---:|---|
| `observer-disagreement-framework` | `f93664bb147115a32862e7ee2b2c2fd48c3adeaf` | One untracked workspace file under `docs/paper/` was present before this task. |
| `coin` | `6cae51af66ff4cb01ff836a1606f707004a9af17` | Existing uncommitted edits and untracked inquiry-to-procedure files were present before this brief. Treat them as user work. |
| `connectednature-site` | `0cd4f6a8b6411ed2170ecbde956dce6098553d32` | Untracked workspace files were present before this task. |
| `connectedinfo-site` | `4a5c67626c3b8dba74231a235198324efd3972d9` | Clean when inspected. |

The search for MHS material across the four repositories found public article prose in `connectednature-site/site/posts/inquiry-to-procedure.html` and its Estonian counterpart, but did not find an exact saved MHS human-AI transcript file in the inspected repositories. Later implementation must not invent transcript content.

## Problem Statement

The current Inquiry to Procedure research uses two formal bundle trajectories as its principal evidence:

- `framework-self`
- `eudr-coffee-brazil-fazenda-sucuri`

The planned MHS example is valuable, but it should not be promoted into a formal OKF-FC bundle merely because its trajectory is worth preserving. The repositories need a cleaner distinction among:

- recorded research trajectory
- recorded inquiry
- formal bundle

The migration should let COIN preserve smaller source-grounded inquiry sequences without pretending that every useful trajectory is a fact-checking bundle, a lightweight bundle, or a formal OKF-FC profile instance.

## Terminology

### Recorded Research Trajectory

The underlying evolution of questions, claims, evidence, frames, procedures, interpretations, determinations, corrections, or understanding. This is the epistemic phenomenon, not a filesystem format.

### Recorded Inquiry

A source-grounded ordered record preserving enough of an inquiry trajectory to reconstruct materially relevant transitions later, without requiring all formal OKF-FC bundle machinery.

A recorded inquiry is not:

- a simplified bundle
- a malformed bundle
- a lightweight bundle
- automatically an OKF-FC profile
- automatically a fact-check
- necessarily a disagreement trajectory

It may contain formation, enrichment, critique, fact-checking, reframing, consolidation, or combinations of these.

### Lightweight Bundle

The existing formal lightweight OKF-FC profile defined by the observer-disagreement framework. Do not silently redefine it.

### Full Bundle

The existing formal full OKF-FC profile defined by the observer-disagreement framework. Do not silently redefine it.

## Target Artifact Hierarchy

```text
recorded research trajectory
|
+-- recorded inquiry
|   `-- minimal reconstructible record
|       no formal OKF-FC bundle required
|
`-- formal bundle
    +-- lightweight OKF-FC bundle
    `-- full OKF-FC bundle
```

This hierarchy should be general in `observer-disagreement-framework`, then adopted in COIN, then reflected in the public sites.

## Representation Proportionality

Representation proportionality: preserve enough structure to support the intended future use of an inquiry trajectory; do not require full bundle machinery merely because the trajectory is worth retaining.

Recording structure should depend on expected future use and epistemic risk. Reasons to promote a recorded inquiry into a formal bundle may include:

- repeated or long-running observer interaction
- structured supersession or reopening relations
- unresolved contestation
- need for reproducibility contracts
- machine validation
- formal round ledgers
- repeated use by independent observers
- controlled history-aware or history-blind experiments
- quantitative trajectory analysis
- high-stakes or research-critical provenance requiring stronger guarantees

These are decision considerations unless a later framework change adopts them as formal criteria.

## MHS Classification

The MHS sequence should be represented as a supporting recorded inquiry, not as a formal bundle and not as a claim-first fact-check.

The faithful structure is closer to:

```text
question -> knowledge enrichment -> reframing -> claim becomes salient -> fact-check -> consolidation
```

Compactly:

```text
Q0 -> K1 -> K2 -> C3 -> V3
```

where:

- `Q0` is the initial inquiry/question.
- `K1` and `K2` are enriched states of understanding.
- `C3` is the external claim that becomes an explicit object of checking.
- `V3` is the resulting determination.

The current public article prose says the saved exchange moved through the newsletter headline, Digital Twin comparison, interface/control-infrastructure interpretation, and Free Energy Principle frame before the stronger world-model claim was rejected. It also says source classification became salient after the human explicitly raised sensationalism. Because no transcript file was found in the inspected repositories, later implementation must verify that wording against the saved exchange before retaining it. If the exchange cannot be found, use a clearly labelled retrospective summary and remove unsupported claims of explicit wording or intent.

The external publisher/headline is a source or claim object, not a participating observer in the human-AI trajectory merely because its claim is evaluated.

Do not apply Type I/II/III disagreement labels to the MHS inquiry unless there is an actual contestation stage satisfying the framework's own definition.

## Target COIN Directory Tree

Adopt this shape under `coin/research/inquiry-to-procedure/`:

```text
research/
`-- inquiry-to-procedure/
    |-- README.md
    |-- claims.md
    |-- critical-overview.md
    |-- bundle-evolution-analysis.md
    |-- counterfactual-tests.md
    |
    |-- recorded-inquiries/
    |   |-- README.md
    |   `-- mhs-world-models/
    |       |-- README.md
    |       |-- inquiry-record.md
    |       |-- analysis.md
    |       `-- sources.md
    |
    `-- bundles/
        |-- framework-self/
        `-- eudr-coffee-brazil-fazenda-sucuri/
```

Do not move `framework-self` or `eudr-coffee-brazil-fazenda-sucuri` under `recorded-inquiries/`.

Do not create `fact-checking/` as the parent of both formal bundles. Fact-checking is one possible function or stage of inquiry, not the superclass of the two formal research trajectories.

Recorded-inquiry metadata should stay neutral, for example:

```yaml
inquiry: inquiry-to-procedure
record_type: recorded-inquiry
formal_bundle: false
status: archived
role_in_parent_inquiry: supporting-example
```

Do not use `fc-*` frontmatter merely to make a recorded inquiry resemble an OKF-FC bundle.

## ConnectedNature, ConnectedInfo, and COIN

The public architecture should become explicit and symmetrical:

```text
                         COIN
                research / provenance
                         |
             +-----------+-----------+
             |                       |
      ConnectedNature         ConnectedInfo
      broad/systemic          focused claim-
      inquiries               by-claim checks
             |                       |
             +---- can feed one another ----+
```

COIN is the shared research/provenance engine behind both public-output modes. ConnectedNature is the broad/systemic inquiry site. ConnectedInfo is the focused claim-by-claim checking site. Publication site and research artifact are separate layers; not every COIN inquiry must be published on either site.

The MHS example crosses this conceptual boundary:

```text
ConnectedNature-like broad inquiry
"What is MHS?"
        |
"How does MHS relate to a Digital Twin?"
        |
"How does FEP change the interpretation?"
        |
a stronger external claim becomes questionable
        |
ConnectedInfo-like focused fact-check
"Did MHS make world models unnecessary?"
```

ConnectedInfo already communicates the sibling-site relationship prominently on its landing page with "A pair of sites", "Two projects, one method", a ConnectedNature sibling row, and a ConnectedInfo focused fact-check row. Later implementation should preserve and lightly align that presentation, not duplicate it with another card.

ConnectedNature currently has COIN relationship language, but it does not yet give the larger ConnectedNature / ConnectedInfo / COIN symmetry the same prominence.

## Evidence-Status Distinction

The two committed formal bundles remain the stronger formal evidence for claims about bundle evolution and method formation.

The MHS inquiry should be framed as a smaller supporting recorded inquiry showing that:

- knowledge enrichment can precede fact-checking
- a fact-checking question may emerge through an inquiry trajectory
- preserving the sequence can expose how the final question became salient
- a history-blind reconstruction beginning directly with the final claim would omit that development

Do not revise the Inquiry to Procedure article from "two formal bundle cases" into "three equivalent bundle cases."

## Observer Versus Source/Claim

Maintain the framework distinction among:

- participating observers or actors who extend the trajectory
- observer instances or processes, where relevant to framework analysis
- external sources
- external claims/headlines

A source can contribute a claim object without becoming a participating observer in the recorded human-AI inquiry. A headline can be the object of source weighting or fact-checking without being a party in the trajectory.

## Migration Invariants

All later implementation prompts must preserve these invariants:

1. Existing historical bundle rounds are not retrospectively rewritten.
2. Existing formal bundles remain formal bundles.
3. MHS is not falsely described as an OKF-FC bundle.
4. A recorded inquiry is not automatically a fact-check.
5. A fact-check can emerge after prior knowledge enrichment.
6. Type I/II/III labels apply only to genuine contestation under the framework definitions.
7. External sources/claims are not automatically participating observers.
8. ConnectedInfo's existing sibling-site card is preserved rather than duplicated.
9. ConnectedNature and ConnectedInfo both remain backed by COIN, but publication site and research artifact are separate layers.
10. The two formal bundles remain distinguishable from MHS in evidentiary strength.
11. No invented transcript, source, commit hash, round, or provenance state is permitted.
12. Repository-local agent instructions and validation rules override guessed workflow assumptions.
13. Do not push changes.
14. Do not fabricate commit identifiers in bundle provenance.
15. If repository rules require recording framework changes as a new bundle round, append a new round through the existing mechanism rather than editing old rounds.

## Dependency Order

Implementation order must remain:

```text
observer-disagreement-framework
-> coin
-> connectednature-site
-> connectedinfo-site
```

Reason:

- The framework must define the general concepts without COIN or site branding.
- COIN then adopts the new artifact class and directory structure.
- ConnectedNature then revises public broad-inquiry language and the Inquiry to Procedure article in both English and Estonian where applicable.
- ConnectedInfo then receives only alignment edits needed after COIN and ConnectedNature are updated.

## Per-Repository File-Impact Matrix

### `observer-disagreement-framework`

| File or area | Exists? | Likely impact |
|---|---:|---|
| `README.md` | yes | Update overview so framework distinguishes recorded research trajectory, recorded inquiry, lightweight bundle, and full bundle without making the repo dependent on COIN or the public sites. |
| `docs/glossary.md` | yes | Add neutral definitions for recorded research trajectory, recorded inquiry, representation proportionality, and promotion to formal bundle. Clarify recorded inquiry is not a lightweight bundle. |
| `docs/framework_v3.md` | yes | Add the conceptual hierarchy and proportionality principle to the general framework. Keep statement trajectory and contestation-specific Type I/II/III rules intact. |
| `docs/formal-core.md` | yes | Check whether formal notation should name the broader recorded research trajectory separately from formal bundles; avoid over-formalizing recorded inquiries if proportionality is conceptual only. |
| `spec/SPEC.md` | yes | Add a boundary note: OKF-FC full/lightweight profiles are formal bundle profiles; recorded inquiries outside the profile must not use `fc-*` metadata to imply conformance. Consider promotion criteria if made normative. |
| `docs/agent-guide.md` | yes | Usually no change unless framework changes require workflow clarification. Current rules already require one PR, append-only ledgers, and no silent edits. |
| `docs/limitations.md` | yes | Add proportionality and maintenance-burden risks: over-recording can create noise; not every inquiry can afford full profile machinery. |
| `docs/paper/paper.md` | yes | Update paper language if needed to distinguish recorded inquiries from OKF-FC bundles and to correct any stale OKF version references. |
| `bundles/framework-self/` | yes | If repository rules treat the framework change as material to the self-description bundle, append a new bundle round and ledger entry. Do not edit old rounds. |
| `tools/src/okf_fc/validate.py`, `bundle.py`, `render.py`, `catalog.py`, `cli.py` | yes | Change only if the framework explicitly makes promotion criteria or recorded-inquiry detection machine-validated. Avoid validator scope creep in the first framework PR. |

Framework independence rule: this repo may mention MHS only as an optional example where appropriate. It must not depend on ConnectedNature, ConnectedInfo, or COIN branding.

Workflow conflict to handle: `AGENTS.md` and `docs/agent-guide.md` require work on a short-lived `work/<slug>` branch, one PR per change, and a root `log.md` line for each merged PR. If a framework bundle is affected, bundle-local round discipline may also apply.

### `coin`

| File or area | Exists? | Likely impact |
|---|---:|---|
| `README.md` | yes | Update COIN's project description if it currently implies all retained inquiry products are formal bundles. |
| `STRUCTURE.md` | yes | Add `research/inquiry-to-procedure/recorded-inquiries/` and distinguish it from `bundles/`. |
| `research/INDEX.md` | yes | Keep inquiry-to-procedure as draft unless status changes. Consider noting source type includes formal bundles plus supporting recorded inquiry after migration. |
| `research/inquiry-to-procedure/README.md` | yes | Add recorded-inquiries as a peer to formal bundles, not as a replacement. |
| `research/inquiry-to-procedure/claims.md` | yes | Add claims for recorded inquiry / proportional representation / MHS support while preserving the two-formal-bundle evidence distinction. |
| `research/inquiry-to-procedure/critical-overview.md` | yes | Add caveats: MHS supports a smaller sequence-preservation claim and does not demonstrate bundle evolution. |
| `research/inquiry-to-procedure/bundle-evolution-analysis.md` | yes | Preserve two committed formal bundle cases as formal evidence. Add a separate section only if it clearly marks MHS as supporting recorded inquiry, not a third bundle. |
| `research/inquiry-to-procedure/counterfactual-tests.md` | yes | Optionally add tests for representation proportionality and for when recorded inquiry should be promoted to bundle. |
| `research/inquiry-to-procedure/bundles/` | yes | Leave `framework-self/` and `eudr-coffee-brazil-fazenda-sucuri/` in place. Do not move them under recorded-inquiries. |
| `research/inquiry-to-procedure/recorded-inquiries/` | no | Create this directory in the COIN implementation step. |
| `research/inquiry-to-procedure/recorded-inquiries/README.md` | no | Define recorded-inquiry rules, metadata, and non-bundle status. |
| `research/inquiry-to-procedure/recorded-inquiries/mhs-world-models/README.md` | no | Introduce the MHS example as supporting inquiry, with no fake bundle conformance. |
| `research/inquiry-to-procedure/recorded-inquiries/mhs-world-models/inquiry-record.md` | no | Preserve the exact exchange if found; otherwise write only a retrospective structured summary labelled as such. |
| `research/inquiry-to-procedure/recorded-inquiries/mhs-world-models/analysis.md` | no | Analyze Q0 -> K1 -> K2 -> C3 -> V3 and the late emergence of source/claim checking. |
| `research/inquiry-to-procedure/recorded-inquiries/mhs-world-models/sources.md` | no | Cite the primary MHS announcement and the secondary headline as sources/claim objects, not participating observers. |
| `research/inquiry-to-procedure/log.md` | yes, untracked when inspected | Treat carefully. If COIN adopts its own inquiry ledger rules, append rather than rewrite. |

COIN working tree warning: multiple relevant files were already modified or untracked when inspected. Later agents must read the then-current working tree and avoid overwriting user changes.

### `connectednature-site`

| File or area | Exists? | Likely impact |
|---|---:|---|
| `README.md` | yes | Add or adjust architecture language so ConnectedNature is broad/systemic public inquiry backed by COIN and sibling to ConnectedInfo. |
| `site/index.html` | yes | Add the larger symmetry only where useful for discoverability; current homepage already has ConnectedNature and COIN language but not the full sibling-site architecture. |
| `site/et/index.html` | yes | Mirror substantive English changes accurately in Estonian. |
| `site/about.html` | yes | Update COIN relationship to mention the two-public-site architecture if needed. |
| `site/et/about.html` | yes | Mirror substantive English changes with established terminology. |
| `site/method.html` | yes | Distinguish broad inquiry, recorded inquiry, and fact-checking stages if method language changes. |
| `site/et/method.html` | yes | Mirror method changes carefully; avoid rejected translations. |
| `site/posts/evidence-first-consensus-later.html` | yes | Review for any framework-language assumptions affected by recorded inquiry / bundle distinction. |
| `site/et/posts/evidence-first-consensus-later.html` | yes | Mirror any substantive English changes. |
| `site/posts/inquiry-to-procedure.html` | yes | Major public article update: distinguish recorded inquiry, lightweight bundle, full bundle; preserve two formal bundle evidence cases; reclassify MHS as supporting recorded inquiry; remove unsupported "explicitly raised sensationalism" wording unless transcript supports it. |
| `site/et/posts/inquiry-to-procedure.html` | yes | Mirror the article update accurately in Estonian. Avoid terms rejected in the prompt such as `sõelumine` for screening, `remont` for repair, `torujuhe` for deterministic pipeline, and `esmaklassiline` for first-class. |
| `site/style.css` | yes | Change only if the public architecture needs new visual treatment. |
| Navigation/footer/index discoverability | yes | Update only where needed. Do not turn the task into a site redesign. |

ConnectedNature language parity rule: any substantive English changes affecting About, Method, Evidence First Consensus Later, or Inquiry to Procedure must be mirrored in corresponding Estonian pages where they exist.

### `connectedinfo-site`

| File or area | Exists? | Likely impact |
|---|---:|---|
| `README.md` | yes | Already defines ConnectedNature as broad inquiry, ConnectedInfo as focused fact-checks, and COIN as shared research engine. Minor alignment may be enough. |
| `site/index.html` | yes | Preserve existing sibling presentation: "A pair of sites", "Two projects, one method", ConnectedNature sibling row, ConnectedInfo focused fact-check row. Do not duplicate it. |
| `site/airport-rules-for-seniors.html` | yes | Probably no change unless shared method/footer wording is updated. |
| `site/style.css` | no | CSS is currently inline in `site/index.html`; do not assume a global stylesheet exists. |
| Method/footer sections | yes, inline in `site/index.html` | Align wording after ConnectedNature changes, keeping the focused claim-by-claim identity. |
| Existing sibling-site UI | yes | Preserve. Lightly adjust copy if needed for COIN/recorded-inquiry hierarchy. |

## Referenced Files or Paths Not Found

The following prompt-target paths do not currently exist in the inspected source trees:

- `coin/research/inquiry-to-procedure/recorded-inquiries/`
- `coin/research/inquiry-to-procedure/recorded-inquiries/README.md`
- `coin/research/inquiry-to-procedure/recorded-inquiries/mhs-world-models/README.md`
- `coin/research/inquiry-to-procedure/recorded-inquiries/mhs-world-models/inquiry-record.md`
- `coin/research/inquiry-to-procedure/recorded-inquiries/mhs-world-models/analysis.md`
- `coin/research/inquiry-to-procedure/recorded-inquiries/mhs-world-models/sources.md`
- `connectedinfo-site/site/style.css`

No exact saved MHS transcript file was found in the four inspected repositories.

## Implementation Risks

- Over-promotion risk: treating every valuable trajectory as an OKF-FC bundle would erase the new recorded-inquiry category.
- Under-specification risk: recorded inquiries may become vague prose unless the minimal reconstructible record is defined well enough.
- Evidence inflation risk: MHS could be accidentally presented as a third formal bundle case.
- Transcript integrity risk: article prose may assert details not supported by a saved exchange.
- Metadata leakage risk: using `fc-*` frontmatter in recorded inquiries may imply bundle conformance.
- Taxonomy leakage risk: applying Type I/II/III to non-contestation stages would contradict the framework.
- Branding leakage risk: the framework repo could become coupled to COIN or public-site branding.
- Site duplication risk: ConnectedInfo's existing sibling-site card could be duplicated rather than preserved.
- Translation risk: ConnectedNature Estonian pages could drift from English revisions or use rejected terminology.
- Dirty-tree risk: COIN already contains uncommitted and untracked work in relevant paths.
- Workflow risk: observer-disagreement-framework requires branch, PR, and ledger discipline; implementation prompts must not skip that.

## Validation Checklist

Before any implementation PR is considered complete:

- The implementation followed the order `observer-disagreement-framework -> coin -> connectednature-site -> connectedinfo-site`.
- Repository-local instructions were read and obeyed.
- No old bundle round was rewritten.
- Any required new framework-self bundle round was appended through the existing mechanism.
- `recorded inquiry` is defined as separate from lightweight and full bundles.
- Representation proportionality is present in the framework and COIN language.
- COIN keeps `bundles/framework-self/` and `bundles/eudr-coffee-brazil-fazenda-sucuri/` under `bundles/`.
- COIN creates `recorded-inquiries/mhs-world-models/` only as a non-bundle recorded inquiry.
- MHS metadata uses neutral fields and `formal_bundle: false`.
- MHS source sequence is preserved; no verbatim Q/A is invented.
- Retrospective MHS summaries are labelled retrospective when no source is
  available; after the 2026-08-29 `mhs-world-models-claude-qa` attachment,
  source-backed summaries point to
  `recorded-inquiries/mhs-world-models/MHS-QA-source.md`.
- The public article still says the two formal bundles are the formal evidence base.
- MHS is described as supporting recorded inquiry, not as a third equivalent case.
- Type I/II/III labels appear only where a genuine contestation stage exists.
- External sources/headlines are not described as participating observers.
- ConnectedNature English changes are mirrored in existing Estonian pages.
- ConnectedInfo's existing "Two projects, one method" UI is preserved and not duplicated.
- No fabricated commit ids, source states, rounds, or provenance claims are introduced.
- No changes are pushed unless explicitly requested.

## Acceptance Criteria

The migration is complete only when:

1. `observer-disagreement-framework` defines the general hierarchy and proportionality principle independently of COIN and the public sites.
2. Existing OKF-FC lightweight and full profiles remain intact and are not redefined as recorded inquiries.
3. COIN contains a `recorded-inquiries/` area under `research/inquiry-to-procedure/` with MHS represented as a non-bundle supporting recorded inquiry.
4. COIN's Inquiry to Procedure research files preserve the evidentiary distinction between the two formal bundles and the MHS supporting example.
5. ConnectedNature's Inquiry to Procedure article and relevant site pages explain the recorded inquiry / lightweight bundle / full bundle distinction and the ConnectedNature / ConnectedInfo / COIN relationship.
6. ConnectedNature Estonian pages mirror substantive English changes with established terminology.
7. ConnectedInfo remains focused on claim-by-claim fact-checking and preserves its existing sibling-site presentation.
8. No implementation fabricates missing transcripts, old rounds, commit ids, or provenance states.
9. Validation and review can trace every substantive claim back to inspected source files, saved transcript content if found, or clearly labelled retrospective analysis.
