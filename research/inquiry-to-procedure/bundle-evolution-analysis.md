---
inquiry: inquiry-to-procedure
title: Bundle evolution analysis — two committed trajectories
status: draft
updated: 2026-08-19
sources:
  - bundles/framework-self/            # observer-disagreement-framework, self-description bundle
  - bundles/eudr-wood-liberia-fmc-area-k/  # geospatial-evidence-framework, applied EUDR bundle
---

# Bundle evolution analysis

This note performs the evidence work for the *Inquiry to Procedure* article using two committed
bundles rather than links to the source repositories. It records the approach decision, then the
per-bundle evolution analysis, then the cross-bundle synthesis and its honest limits.

## 1. Approach decision: commit the bundles, do not link the repos

Both source repositories — `observer-disagreement-framework` and `geospatial-evidence-framework`
(local `Users/server/projects/...`) — are **private**. Linking them from a public research trail
would give the reader a 404 and defeat the trail's purpose. The alternative adopted here is to
commit **one self-contained bundle from each repository** into the public COIN repo, under
`research/inquiry-to-procedure/bundles/`, and cite in-repo paths.

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

### Caveats to handle before committing

- **Trim `_site/`.** The self bundle ships a full rendered `_site/` HTML tree that roughly doubles
  its size and duplicates the Markdown source. Commit the Markdown source tree only
  (`agent-contract.md`, `answer.md`, `log.md`, `index.md`, `inquiry/`, `r/*.csv`, `s/`, `pf/`,
  `reproduction/`). Keep the two CSVs; they carry the metrics and the retrospective classification.
- **Counterpart references are pins, not data.** The EUDR bundle references a private counterpart
  repo (`single-earth/eudr-dmi-gil@61285bd…`, and a `GeorgeMadlis/eudr-dmi-gil` remote) by commit
  and checksum only. Its own evidence discipline forbids copying counterpart artifacts into the
  source bundle. So committing it exposes **references**, not Single.Earth data. Given the
  Single.Earth Foundation council relationship and ConnectedNature's published critique of
  Single.Earth-connected work, this is a disclosure point to decide deliberately: keep the pins
  (recommended — they are provenance, not payload) and, if useful, add a one-line note in the trail
  that the counterpart repo is third-party and private.
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
    └── eudr-wood-liberia-fmc-area-k/      (Markdown source tree only)
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

## 3. Bundle B — eudr-wood-liberia-fmc-area-k (applied)

Source: `geospatial-evidence-framework`, EUDR wood/timber task bundle. 8 native rounds,
2026-08-14 → 2026-08-17, parties `codex` and `claude`, plus two imported lineage rounds from the
parent `eudr-gee` method-family.

### The coffee → wood correction, in the record

`reproduction/lineage.md` imports two parent rounds by reference (not renumbered):

- **`eudr-gee` round 30 (contestation, 2026-08-12):** "Liberia public-source discovery showed the
  coffee-shaped parent method could not represent wood without semantic distortion." The concrete
  reason: wood cannot be a coffee-style commodity mask because forest degradation and source
  geometry are separate evidence dimensions.
- **`eudr-gee` round 31 (consolidation, 2026-08-12):** the parent method gains separate wood
  deforestation/degradation streams and explicit production-geometry / source-linkage status.

This is the article's applied demonstration end to end: a commodity-specific (coffee) assumption
entered the parent method, applied wood evidence exposed it as contestation, and the method was
consolidated into a more general shape. The task bundle then **inherits** the corrected semantics
rather than re-deriving them.

### The reduction outputs, concretely

- **Deterministic procedure / schema.** `s/modeling.md` carries a `wood_evidence_state` schema with
  separate `deforestation`, `degradation`, `production_geometry`, `harvest_or_source_linkage`,
  `legal_provenance_context`, `evidence_conflicts`, `evidence_gaps`, and `manual_review_required`
  fields. Round 4 populates it with per-source areas (e.g. Hansen ≈ 10,914 ha, JRC-TMF ≈ 5,386 ha,
  RADD confirmed ≈ 13,502 ha) reported as **source/process disagreement, not averaged and not
  treated as automatic contradictions**. → This maps onto EUDR Layer A (commodity-independent land
  evidence) and Layer C (wood-specific degradation), with the schema keeping them separate.
- **AI instruction / guardrail.** `s/task-scope.md` is an explicit **Frame Declaration** with a
  Scope-Change Protocol: classify every proposed move as same-frame evidence evolution,
  task-boundary change, method-family/rule change, or unresolved; append a round only for the first;
  escalate unresolved cases to the human. Out-of-scope items explicitly include "silently
  generalizing Liberia-specific findings into the global wood method" and "coffee/cocoa
  commodity-mask semantics." → The scope-drift error of the parent method is now a standing
  instruction that prevents its recurrence. This is Layer-B thinking made procedural: production
  linkage and chain-of-custody are named as separate, currently-missing evidence rather than assumed.
- **Retained uncertainty.** `answer.md` sits at `human_review_required`; production plot, harvesting
  block, and chain-of-custody linkage are recorded as **unresolved / missing**, and provenance is
  `pinned-not-reproduced`. → The human-in-the-loop boundary is structural, not a temporary gap, and
  the bundle refuses to convert missing linkage into a zero-valued layer.

## 4. Cross-bundle synthesis

What the two committed bundles **jointly support**:

1. Recorded human–AI inquiry can be progressively reduced into the three outputs the article names —
   deterministic procedure (self rounds 12–13; EUDR `wood_evidence_state`), durable AI instruction
   (self Wolfram guardrail; EUDR Frame Declaration + Scope-Change Protocol), and explicitly retained
   uncertainty (self `fc-status: open`; EUDR `human_review_required` / missing linkage).
2. The human's own framing is a legitimate object of the inquiry, not a fixed input: the self bundle
   corrects a human scope-widening in-record (round 4); the EUDR line corrects a human/parent
   coffee-shaped decomposition (parent rounds 30–31).
3. Reproducibility is not correctness: the EUDR `pinned-not-reproduced` state and the self bundle's
   refusal to claim unmeasurable metrics both keep deterministic execution separate from epistemic
   warrant.

What they **do not** support (the honest negative, to keep in the synthesis):

- Two bundles, one of them self-referential, cannot establish a general law that recorded inquiry
  reduces error or transfers across problems. They make the compilation reading **demonstrable on
  these cases**; they do not make it general.
- No measurement here shows that compression reduces error *recurrence* — the self bundle's own
  observer-distance metrics are largely `NOT_MEASURABLE`, and no transfer experiment exists.
- The EUDR three-layer decomposition is coupled, not clean: Layer B (production linkage) is exactly
  the part recorded as missing, so the tidy A→B→C separation is an argued target, not a demonstrated
  pipeline.

## 5. Effect on the article and the research folder

- **Research trail:** replace the two "pending" placeholders with in-repo links to
  `bundles/framework-self/` and `bundles/eudr-wood-liberia-fmc-area-k/`, and add one line each noting
  the source repository is private and the bundle is the committed public evidence.
- **Claims ledger (V1, V2):** resolved — repos are private; the committed bundles are the evidence.
  Upgrade the previously generic `[sourced: repository state]` tags to specific bundle/round refs
  (done in `claims.md`).
- **Evidence Base / Source Evaluation:** can now cite the specifics above (frame-change 2/13, the
  coffee→wood parent rounds 30–31, the Wolfram validator guardrail, the `NOT_MEASURABLE` honesty,
  `human_review_required`).
- **Synthesis:** unchanged in direction — the strong general claim remains not established; the
  bundles strengthen the narrow, defensible result without inflating it.
