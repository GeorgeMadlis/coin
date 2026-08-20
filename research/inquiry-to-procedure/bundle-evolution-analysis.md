---
inquiry: inquiry-to-procedure
title: Bundle evolution analysis — two committed trajectories
status: draft
updated: 2026-08-20
sources:
  - bundles/framework-self/            # observer-disagreement-framework, self-description bundle
  - bundles/eudr-coffee-brazil-fazenda-sucuri/  # geospatial-evidence-framework, applied EUDR bundle
---

# Bundle evolution analysis

This note performs the evidence work for the *Inquiry to Procedure* article using two committed
bundles rather than links to the source repositories. It records the approach decision, the
per-bundle evolution analysis, and the cross-bundle synthesis with its limits.

The corrected interpretation separates four things:

- the bundle as a historical/provenance record;
- the transformations recorded in that history;
- the process that performed or could systematize those transformations;
- the current outputs of those transformations.

The evidence can establish that `historical finding -> later code/test/instruction/specification`
occurred. It cannot establish from these cases alone that recorded history was necessary to obtain
the later artifact, or that replaying history is necessary to execute the resulting artifact.

## 1. Approach decision: commit the bundles, do not link the repos

The `observer-disagreement-framework` source repository is private, while the applied EUDR evidence
is now drawn from the public `geospatial-evidence-framework` Fazenda Sucuri bundle. The adopted
public trail commits one readable bundle snapshot for each trajectory into the COIN repo under
`research/inquiry-to-procedure/bundles/`, and cites in-repo paths.

This remains the more faithful option, for three reasons.

1. **The bundle is the provenance object.** Each bundle is a gitingest-style flattened export
   carrying its own directory tree, full round ledger (`log.md`), an inquiry folder of per-round
   records, and, for the self bundle, a retrospective round classification and a metrics table. The
   article's evidence is the recorded trajectory, and the bundle contains that record.
2. **It is inspectable and citable.** The bundles carry commit hashes, manifest references, and
   `fc-supersedes` lineage, so each claim can point to a specific file and round.
3. **It preserves the state being interpreted.** Committing the provenance lets readers inspect the
   historical record without requiring the source repositories or rewriting the bundle evidence to
   fit the current interpretation.

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
- **Some self-bundle refs read `NOT AVAILABLE until merge`** (rounds 19-20). Either pin the
  committed snapshot to a state where they resolve, or note them as pending. Do not silently drop
  them.

Recommended layout:

```text
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
2026-07-16 -> 2026-08-16, two parties (`codex`, `claude`).

### Ledger shape

Move distribution across the 13 measured rounds (metrics target excludes round 14 to avoid circular
self-measurement): evidence 0.69, frame-change 0.15 (2 of 13), objection present at rounds 3 and 7,
observer-handoff frequency 0.17 (2 of 12 adjacent pairs change party). Retrospective stage counts
over rounds 1-13: formation 1, enrichment 8, critique 1, contestation 1, consolidation 2.

### Key transitions and later operational destinations

- **Frame-change, round 4 (claude): human reframing corrected in-record.** The round file states
  plainly: "The human instruction widened the project's object of study," from observer
  *disagreement* to *statement evolution*, with disagreement demoted to the contestation stage of a
  five-stage trajectory. The transition is recorded as `f(t) -> f(t+1)` with SHA256 hashes for the
  new and prior framework documents and `fc-supersedes` bumps on `answer.md`, `pf/overview.md`, and
  `s/overview.md`. This shows that human framing became an object of recorded method formation.
- **Frame-change, round 8 (codex): governance rule.** Repository rounds and bundle rounds are fixed
  as separate counters, recorded in manifests/catalogs. Later destination: AI instruction / durable
  convention.
- **Rounds 12-13: provisional made normative, then executable.** Bundle conventions become a
  normative specification (round 12), then a generator, atomic-append tool, and validator (round
  13). Later destination: code, tests, and validation machinery.
- **Rounds 18-19: Wolfram guardrail.** After a foundation audit, the specification is repaired so
  every future bundle must disclose the Wolfram observer-theory foundation as
  `fc-foundation-role: formal-analogy`, with separated attribution, minimum-source policy, analogy
  guardrails, and validator rejection conditions. The specification frontmatter records
  `fc-irreducibility: none`. Later destination: validator-enforced instruction and evidence-semantics
  guardrail, while preserving the warning that Wolfram vocabulary is analogy, not explanation.
- **Round 20: observer/observation and actor/observer identity separated.** Later destination:
  retained conceptual clarification; `fc-status` stays `open`.

These observations show recorded findings becoming later operational artifacts. They do not prove
that the same artifacts could not have been derived from the final evidence and problem without the
round history.

### Honest measurement gaps (Source Evaluation material)

The bundle's own metrics table marks the observer-distance family `NOT_MEASURABLE` with reasons:
only one contestation round exists (type-descent/stall/reversal rates undefined); no timestamped
competing predictions were recorded (predicted-continuation divergence unavailable); no independent
paired labels over a shared item set (forced-classification disagreement unavailable);
re-litigation rate not measurable for lack of stable issue identifiers. The description-length ratio
(claude/codex about 4.0 mean) is flagged "representation-dependent demonstration only." The bundle
supports claims about research-state evolution, and explicitly refuses claims its record cannot
support.

## 3. Bundle B — eudr-coffee-brazil-fazenda-sucuri (applied)

Source: `geospatial-evidence-framework`, EUDR coffee task bundle. 7 native rounds,
2026-08-11 -> 2026-08-12, party `codex`.

### The coffee screening correction, in the record

The applied trajectory records concrete repairs: a Sentinel-2 visual defect is fixed (round 2), the
AOI administrative labels and report map behavior are corrected (round 4), the coffee temporal mask
is repaired so current coffee preserves baseline-year coffee while "new commodity since baseline"
remains a separate layer (round 6), and the page-4 regional overview gap is fixed at the
renderer/publish-contract level (round 7).

The bundle therefore supports a public EUDR coffee screening example of method formation
provenance: observed defects were converted into corrected artifacts, tighter source semantics, and
an explicitly limited screening verdict.

### The current operational outputs, concretely

- **Layered EUDR evidence semantics.** `s/modeling.md` and `r/results.md` keep FDP-only,
  MapBiomas-only, and both-source agreement evidence distinct. New coffee/post-2020 loss overlap is
  reported source-specifically (FDP 0.27 ha; MapBiomas 0.0 ha; both-source agreement 0.0 ha), not
  averaged into a single warrant. This operationalizes Layer A (land/forest-change evidence), Layer
  B (production linkage), and Layer C (commodity-specific evidence) without pretending those layers
  are interchangeable.
- **AI instruction / guardrail.** `s/task-scope.md` fixes the task as EUDR coffee screening for
  Brazil / Minas Gerais / Fazenda Sucuri, and `s/gsp-mapping.md` records the evidence flow from AOI
  admission through forest baseline, post-2020 loss, coffee masks, overlap metrics, and human
  review. Repeated review issues become standing method constraints.
- **Retained uncertainty.** `answer.md` sits at `human_review_required` with provenance
  `pinned-not-reproduced`. It explicitly says the result is a screening flag, not a legal
  non-compliance determination. The human-in-the-loop boundary is structural, not a temporary gap.

The useful substantive result is the EUDR decomposition: Layer A, Layer B, and Layer C. The rounds
leading to it are provenance of method formation rather than part of the current EUDR operational
method.

## 4. Cross-bundle synthesis

What the two committed bundles jointly support:

1. Recorded human-AI inquiry can show observable transformation from historical findings into
   operational outputs: deterministic procedure (self rounds 12-13; EUDR source-specific
   mask/overlap reporting), durable AI instruction (self Wolfram guardrail; EUDR scope and mapping
   constraints), and explicitly retained uncertainty (self `fc-status: open`; EUDR
   `human_review_required`).
2. The human's own framing is a legitimate object of recorded method formation: the self bundle
   records a human scope-widening in round 4; the EUDR line records visual, map, temporal-mask, and
   publish-contract defects being corrected.
3. Reproducibility is not correctness: the EUDR `pinned-not-reproduced` state and the self bundle's
   refusal to claim unmeasurable metrics both keep deterministic execution separate from epistemic
   warrant.

What they do not support:

- They do not establish that recorded history was necessary to obtain the later operational
  artifacts.
- They do not establish that replaying or loading the historical trajectory is necessary for routine
  execution once the method has been successfully compiled.
- They do not compare history-aware derivation with history-blind derivation from final evidence.
- They do not test whether archived provenance improves later method revision under failure.
- They do not establish a general law that recorded inquiry reduces error or transfers across
  problems. Two bundles, one self-referential, can support a disciplined case study, not a general
  law.

## 5. Bundle evolution mechanics

Bundle evolution should not collapse transitions into a linear `supersedes` chain. The minimum
typed relation set needs to distinguish at least:

- **`supersedes`**: a later state replaces an earlier state within the same relevant frame,
  assumptions, scope, definitions, and procedure.
- **`contradicts`**: two states cannot both hold under the reconstructed evidence, frame, and
  procedure.
- **`reframes`**: the later state changes the governing assumptions, scope, definitions, or problem
  object.
- **`reopens`**: a settled or provisionally settled state is returned to contestation because new
  evidence, a procedural correction, or a frame change makes the prior resolution unstable.
- **`supersedes-under-assumptions`**: the later state replaces the earlier one only under stated
  assumptions, scope limits, evidence versions, or procedure versions.

A bare `supersedes` link silently encodes the latest observer's frame as epistemic progress, which
is exactly the failure the retention argument is meant to prevent.

The determination at time `t` should be treated as a function:

```text
D_t = f(E_t, F_t, P_t)
```

where `E` is the evidence and its versions, `F` is the frame / assumptions / scope / definitions,
and `P` is the procedure / method / instruction version. A result can change with the same evidence
and nominal frame if the procedure was corrected, such as after scope-drift repair or correction of
an earlier AI-generated conceptualization. Observer identity matters only through the operationally
relevant differences it introduces: prompt or instruction version, method version, assumptions,
scope, and dataset versions. Bare identity is not itself an explanatory variable.

As a candidate answer to the article's open retention question, the minimum reconstructible state is:

```text
R_t = {C_t, E_t, F_t, P_t, V_t, Δ_t}
```

Here `C_t` is the claim state, `E_t` the referenced evidence, `F_t` the relevant
frame/assumptions, `P_t` the procedure/version, `V_t` the verdict or determination, and `Δ_t`
the stated reason for transition. What must survive is enough to reconstruct the contested
transition, not every prompt, transcript, or temporary artifact.

The symmetric resolution procedure is:

```text
contradiction -> reconstruct competing claims -> isolate differing evidence, assumptions, and
procedure -> seek discriminating evidence -> confirm supersession, retain conflict, or reopen the
earlier state
```

This deliberately does not instruct agents to find arguments for either side. The work is to
reconstruct the competing states, identify the operative differences, and then decide whether the
record warrants supersession, retained conflict, or reopening.

The boundary between provenance and method must stay explicit. Retention supplies the evidence for
the method; the rules governing reconstruction, comparison, discrimination, supersession, conflict
retention, and reopening constitute the method.

The historical record is provenance; the disciplined use of that record to reconstruct, compare, discriminate, supersede, retain conflict, or reopen is method.

## 6. Effect on the article and the research folder

- **Research trail:** link to `bundles/framework-self/` and
  `bundles/eudr-coffee-brazil-fazenda-sucuri/`, noting that the applied public copy omits JSON,
  GeoJSON, PDF, and canonical `report.html` artifacts.
- **Claims ledger:** keep bundle-sourced empirical claims specific, while marking the ontology
  (`H`, `P`, `M`) and counterfactual interpretation as inferential.
- **Evidence Base / Source Evaluation:** cite specifics above (frame-change 2/13, the Fazenda
  Sucuri visual/mask/publish-contract fixes, the Wolfram validator guardrail, the `NOT_MEASURABLE`
  honesty, `human_review_required`).
- **Synthesis:** revise direction: the bundles demonstrate observed transformation into operational
  artifacts, but not the counterfactual advantage of recording the trajectory.
