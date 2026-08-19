---
inquiry: inquiry-to-procedure
title: Bundle evolution analysis — two committed trajectories
status: draft
updated: 2026-08-19
sources:
  - bundles/framework-self/            # observer-disagreement-framework, self-description bundle
  - bundles/eudr-coffee-brazil-fazenda-sucuri/  # geospatial-evidence-framework, applied EUDR bundle
---

# Bundle evolution analysis

This note performs the evidence work for the *Inquiry to Procedure* article using two committed
bundles rather than links to the source repositories. It records the approach decision, then the
per-bundle evolution analysis, then the cross-bundle synthesis and its honest limits.

## 1. Approach decision: commit the bundles, do not link the repos

The `observer-disagreement-framework` source repository is private, while the applied EUDR evidence
is now drawn from the public `geospatial-evidence-framework` Fazenda Sucuri bundle. The adopted
public trail commits one readable bundle snapshot for each trajectory into the COIN repo under
`research/inquiry-to-procedure/bundles/`, and cites in-repo paths.

This is not a workaround; it is the more faithful option, for three reasons.

1. **The bundle already is the trajectory object.** Each bundle is a gitingest-style flattened
   export carrying its own directory tree, a full round ledger (`log.md`), an inquiry folder of
   per-round records, and — for the self bundle — a retrospective round classification and a
   metrics table. The article's unit of analysis is the recorded trajectory; the bundle contains
   exactly that, so the whole repository is not needed to make the case.
2. **It is inspectable and citable.** The bundles carry commit hashes, manifest references, and
   `fc-supersedes` lineage, so each claim in the article can point to a specific file and round.
3. **It demonstrates the thesis instead of asserting it.** The article claims a trajectory is an
   observable substrate from which code, instructions, and retained uncertainty can be read off.
   Committing the substrate lets the reader do that reading.

### Committed-state caveats

- **`_site/` is trimmed.** The public COIN snapshot keeps the framework-self Markdown source tree
  (`agent-contract.md`, `answer.md`, `log.md`, `index.md`, `inquiry/`, `r/*.csv`, `s/`, `pf/`,
  `reproduction/`) and omits the rendered `_site/` tree. The two CSVs are retained because they
  carry the metrics and retrospective classification.
- **The applied snapshot omits machine/data artifacts.** The Fazenda Sucuri copy keeps the Markdown
  trajectory, method, and result summaries, while omitting JSON, GeoJSON, PDF, and canonical
  `report.html` artifacts. It links back to the public source bundle for repository context without
  republishing those files through COIN.
- **"pinned-not-reproduced" is the honest provenance state.** The EUDR `answer.md` is
  `human_review_required` with provenance `pinned-not-reproduced`: hashes and artifacts were
  independently checked, but no qualifying independent rerun was performed. The trail should state
  this rather than imply the evidence is reproduced.
- **Some self-bundle refs read `NOT AVAILABLE until merge`** (rounds 19–20). Either pin the
  committed snapshot to a state where they resolve, or note them as pending. Do not silently drop
  them.

Recommended layout:

```
research/inquiry-to-procedure/
├── claims.md
├── critical-overview.md
├── bundle-evolution-analysis.md          (this file)
└── bundles/
    ├── framework-self/                    (Markdown source tree only)
    └── eudr-coffee-brazil-fazenda-sucuri/ (Markdown source tree only; no JSON/PDF/GeoJSON/report.html)
```

## 2. Bundle A — framework-self (general, self-referential)

Source: `observer-disagreement-framework`, self-description bundle. 20 recorded rounds,
2026-07-16 → 2026-08-16, two parties (`codex`, `claude`).

### Ledger shape

Move distribution across the 13 measured rounds (metrics target excludes round 14 to avoid circular
self-measurement): evidence 0.69, frame-change 0.15 (2 of 13), objection present at rounds 3 and 7,
observer-handoff frequency 0.17 (2 of 12 adjacent pairs change party). Retrospective stage counts
over rounds 1–13: formation 1, enrichment 8, critique 1, contestation 1, consolidation 2.

### Key transitions, mapped to the three reduction outputs

- **Frame-change, round 4 (claude) — human reframing corrected in-record.** The round file states
  plainly: "The human instruction widened the project's object of study," from observer
  *disagreement* to *statement evolution*, with disagreement demoted to the contestation stage of a
  five-stage trajectory. The transition is recorded as `f(t) → f(t+1)` with SHA256 hashes for the
  new and prior framework documents and `fc-supersedes` bumps on `answer.md`, `pf/overview.md`,
  `s/overview.md`. → **This is the article's central move**: the human's own decomposition was one
  of the things the inquiry had to revise, and the revision is inspectable rather than narrated.
- **Frame-change, round 8 (codex) — a governance rule.** Repository rounds and bundle rounds are
  fixed as separate counters, recorded in manifests/catalogs. → **AI instruction / durable
  convention.**
- **Rounds 12–13 — provisional made normative, then executable.** Bundle conventions become a
  normative specification (round 12), then a generator, atomic-append tool, and validator (round
  13). → **Deterministic procedure**: the reduction reaches code and tests.
- **Rounds 18–19 — the Wolfram guardrail.** After a foundation audit, the specification is repaired
  so every future bundle must disclose the Wolfram observer-theory foundation as
  `fc-foundation-role: formal-analogy`, with separated attribution, minimum-source policy, analogy
  guardrails, and **validator rejection conditions**. The specification frontmatter records
  `fc-irreducibility: none`. → **A recurring reasoning failure compressed into a validator-enforced
  instruction** — and precisely the discipline the article's Limits section argues for: Wolfram
  vocabulary is retained as analogy, not asserted as explanation.
- **Round 20 — observer/observation and actor/observer identity separated.** → **Retained
  conceptual clarification**, not a claim of closure; `fc-status` stays `open`.

### Honest measurement gaps (Source Evaluation material)

The bundle's own metrics table marks the observer-distance family `NOT_MEASURABLE` with reasons:
only one contestation round exists (type-descent/stall/reversal rates undefined); no timestamped
competing predictions were recorded (predicted-continuation divergence unavailable); no independent
paired labels over a shared item set (forced-classification disagreement unavailable);
re-litigation rate not measurable for lack of stable issue identifiers. The description-length ratio
(claude/codex ≈ 4.0 mean) is flagged "representation-dependent demonstration only." → The bundle
supports claims about **research-state evolution**, and explicitly refuses claims its record cannot
support. That refusal is itself evidence for the article's Source Evaluation section.

## 3. Bundle B — eudr-coffee-brazil-fazenda-sucuri (applied)

Source: `geospatial-evidence-framework`, EUDR coffee task bundle. 7 native rounds,
2026-08-11 → 2026-08-12, party `codex`.

### The coffee screening correction, in the record

The applied trajectory shows the same reduction pattern in a public coffee-screening case. Review
findings become concrete repairs: a Sentinel-2 visual defect is fixed (round 2), the AOI
administrative labels and report map behavior are corrected (round 4), the coffee temporal mask is
repaired so current coffee preserves baseline-year coffee while "new commodity since baseline"
remains a separate layer (round 6), and the page-4 regional overview gap is fixed at the
renderer/publish-contract level (round 7).

The bundle therefore supports the article through a public EUDR coffee screening case: a sequence of
observed defects is converted into corrected artifacts, tighter source semantics, and an explicitly
limited screening verdict.

### The reduction outputs, concretely

- **Deterministic procedure / schema.** `s/modeling.md` and `r/results.md` keep FDP-only,
  MapBiomas-only, and both-source agreement evidence distinct. New coffee/post-2020 loss overlap is
  reported source-specifically (FDP 0.27 ha; MapBiomas 0.0 ha; both-source agreement 0.0 ha), not
  averaged into a single warrant. → This maps onto EUDR Layer A (land/forest-loss evidence), Layer B
  (AOI/production linkage), and Layer C (coffee evidence) without pretending those layers are
  interchangeable.
- **AI instruction / guardrail.** `s/task-scope.md` fixes the task as EUDR coffee screening for
  Brazil / Minas Gerais / Fazenda Sucuri, and `s/gsp-mapping.md` records the evidence flow from AOI
  admission through forest baseline, post-2020 loss, coffee masks, overlap metrics, and human
  review. → Repeated review issues are absorbed as standing method constraints rather than kept only
  as historical commentary.
- **Retained uncertainty.** `answer.md` sits at `human_review_required` with provenance
  `pinned-not-reproduced`. It explicitly says the result is a screening flag, not a legal
  non-compliance determination. → The human-in-the-loop boundary is structural, not a temporary gap.

## 4. Cross-bundle synthesis

What the two committed bundles **jointly support**:

1. Recorded human–AI inquiry can be progressively reduced into the three outputs the article names —
   deterministic procedure (self rounds 12–13; EUDR source-specific mask/overlap reporting), durable
   AI instruction (self Wolfram guardrail; EUDR scope and mapping constraints), and explicitly
   retained uncertainty (self `fc-status: open`; EUDR `human_review_required`).
2. The human's own framing is a legitimate object of the inquiry, not a fixed input: the self bundle
   corrects a human scope-widening in-record (round 4); the EUDR line corrects visual, map,
   temporal-mask, and publish-contract defects in-record.
3. Reproducibility is not correctness: the EUDR `pinned-not-reproduced` state and the self bundle's
   refusal to claim unmeasurable metrics both keep deterministic execution separate from epistemic
   warrant.

What they **do not** support (the honest negative, to keep in the synthesis):

- Two bundles, one of them self-referential, cannot establish a general law that recorded inquiry
  reduces error or transfers across problems. They make the compilation reading **demonstrable on
  these cases**; they do not make it general.
- No measurement here shows that compression reduces error *recurrence* — the self bundle's own
  observer-distance metrics are largely `NOT_MEASURABLE`, and no transfer experiment exists.
- The EUDR three-layer decomposition is coupled, not clean: the Fazenda Sucuri record is still a
  screening case, so A→B→C is an argued structure for evidence discipline rather than a legal
  determination pipeline.

## 5. Effect on the article and the research folder

- **Research trail:** link to `bundles/framework-self/` and
  `bundles/eudr-coffee-brazil-fazenda-sucuri/`, noting that the applied public copy omits JSON,
  GeoJSON, PDF, and canonical `report.html` artifacts.
- **Claims ledger (V1, V2):** resolved — the committed bundles are the evidence.
  Upgrade the previously generic `[sourced: repository state]` tags to specific bundle/round refs
  (done in `claims.md`).
- **Evidence Base / Source Evaluation:** can now cite the specifics above (frame-change 2/13, the
  Fazenda Sucuri visual/mask/publish-contract fixes, the Wolfram validator guardrail, the
  `NOT_MEASURABLE` honesty, `human_review_required`).
- **Synthesis:** unchanged in direction — the strong general claim remains not established; the
  bundles strengthen the narrow, defensible result without inflating it.
