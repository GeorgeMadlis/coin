---
inquiry: inquiry-to-procedure
title: From Inquiry to Procedure — Recorded Inquiry, Method Evolution, and Operational Method
status: draft
updated: 2026-08-24
---

# Claims ledger

Each claim is tagged:

- **[sourced]** — supported directly by a cited external source or by the recorded repository state.
- **[inferential]** — a defensible reading built on sourced material, but not stated by any source verbatim.
- **[flagged]** — asserted in the inquiry but not yet adequately verified; needs work before it can be relied on.

The originating proposition and its negative are recorded first so that later claims can be checked against them.

## Proposition under test

- **C0** *[inferential]* Recorded human–AI inquiry is primarily provenance of method formation: a historical record of observable assumptions, corrections, supersessions, frame changes, evidence changes, rejected approaches, and state transitions. Its methodological value, if any, lies in whether the explicitly recorded project-specific trajectory adds information needed for reliable continuation, correction, interpretation, revision, or transfer beyond participants' background knowledge, the established literature and other explicit scholarly compression, and a sufficiently explicit current project/problem state.
- **C0-neg** *[inferential]* The defensible negative: if observers with appropriate prior knowledge and an adequate current-state handoff can continue, detect errors, revise the method, and reach equivalent or better results without the recorded trajectory, then retaining the trajectory adds little methodological value beyond provenance, auditability, and exceptional forensic use. This negative has not been tested by the existing two-bundle analysis.
- **C0a** *[inferential]* The inquiry should distinguish three objects: recorded trajectory `H`; method-evolution protocol `P`, which decides what a finding becomes; and operational method `M`, consisting of the specifications, code, tests, validators, AI instructions, evidence semantics, decision procedures, and explicit unresolved questions required to perform the task now.
- **C0b** *[inferential]* Routine execution should normally use `M + current/new evidence E -> result`, not `H + M + E -> result`. Archived trajectory may become relevant again when revising `M`, for example after a contradiction, source-authenticity failure, frame change, unexplained constraint, scope drift, or evidence that the current method is inadequate.
- **C0c** *[inferential]* No human or AI observer starts from zero. For observer `i`, the available initial knowledge for a project handoff can be represented as `K_i^0 = B_i + L + S_0`, where `B_i` is the observer's partly latent background knowledge, learned competence, tacit framing, and biases; `L` is explicitly communicated prior knowledge such as literature, standards, documentation, established results, and current scholarly synthesis; and `S_0` is the current project/problem state at handoff.
- **C0d** *[inferential]* The local project trajectory is `H_{0:t}: S_0 -> S_1 -> ... -> S_t`. The key comparison for observer `j` is therefore `B_j + L + S_t` versus `B_j + L + S_t + H_{0:t}`, not "history" versus "no history" in general.
- **C0e** *[inferential]* The bundle cannot exhaustively serialize `B_i` or reproduce cognition. It can externalize only relevant observable consequences: assumptions, frame choices, transitions, corrections, evidence changes, supersessions, rejected interpretations, unresolved issues, and method changes.
- **C0f** *[inferential]* "History-blind" means blind to the project-specific recorded trajectory `H_{0:t}`, not devoid of prior knowledge. A history-blind observer still has `B_i + L`, and may also receive an explicit current-state handoff.

## Boundedness of inquiry

- **C1** *[inferential]* Human and AI inquiry are both bounded, and the bounds compound: a human's partial command of the relevant science produces an incomplete decomposition, and the model executing within that frame can amplify rather than question it.
- **C2** *[inferential]* Recording an inquiry is methodologically useful for method formation or revision only when a process can use the record to expose and repair framing errors, identify superseded assumptions, or explain why an operational constraint exists. Mere storage is provenance/auditability, not itself an operational rule.

## Evidence base — the two trajectories

- **C3** *[sourced: repository state]* Two recorded human–AI trajectories are used as evidence: the observer-disagreement framework (general, partly self-referential) and the EUDR geospatial evidence repository (applied).
- **C4** *[sourced: repository state]* The geospatial repository's early architecture was shaped around coffee; later work established that wood requires a materially different evidence structure — degradation, production geometry, source linkage.
- **C5** *[sourced: repository state]* The geospatial agent contract now requires agents to review sibling history while prohibiting silent generalisation of dataset-specific thresholds, commodity-specific inference, AOI assumptions, country source hierarchy, legal interpretation, and evidence semantics.

## EUDR regulatory decomposition

- **C6** *[sourced: EUR-Lex 32023R1115, consolidated 2025-12-26]* EUDR defines a deforestation-free condition common across the relevant commodities in terms of land not subject to deforestation after 31 December 2020.
- **C7** *[sourced: EUR-Lex 32023R1115, Art. 3]* Article 3 prohibits relevant commodities and products from being placed or made available on the Union market, or exported, unless the regulation's conditions are met.
- **C8** *[sourced: EUR-Lex 32023R1115]* EUDR due diligence requires geolocation of the plots where the relevant commodities were produced; a remote-sensing observation that deforestation occurred somewhere is not sufficient without production linkage.
- **C9** *[sourced: EU environment FAQ, 5th iteration]* Wood carries an additional condition concerning harvesting without inducing forest degradation after the cutoff.
- **C10** *[inferential]* Given C6–C9, the method decomposes more cleanly as Layer A (commodity-independent land evidence) → Layer B (production linkage) → Layer C (commodity-specific evidence) than as either a "coffee method" or a "wood method."
- **C11** *[inferential]* The deforestation test is not fully independent of commodity semantics, because the product must be connected to the relevant production geometry (Layer B couples A and C).

## Source evaluation

- **C12** *[sourced: repository state]* The logs record observable state transitions — supersessions, corrections, boundary changes, produced artefacts — but not the full human thought process or model internal reasoning.
- **C13** *[inferential]* Therefore the trajectories support claims about research-state evolution, not a complete cognitive reconstruction of either party.

## Competing interpretations

- **C14** *[inferential]* "Provenance," "external memory," and "compilation substrate" name roles at different conceptual levels rather than mutually exclusive interpretations. Provenance describes what the record is epistemically; external memory describes one possible access/use pattern; compilation substrate describes one possible role the record can play inside a transformation process.
- **C15** *[inferential]* The process that consumes recorded provenance and decides whether a finding becomes code, test, validator, specification, agent instruction, evidence-semantic rule, unresolved question, or provenance-only is best treated as a candidate method-evolution protocol, not as the recorded trajectory itself.

## Critical synthesis

- **C16** *[inferential]* The two bundles support a narrow empirical claim: recorded findings were observably transformed into later code, tests, specifications, instructions, evidence semantics, and explicit uncertainty. They do not establish that the recorded project trajectory was necessary to obtain those artifacts, that trajectory-aware derivation beats trajectory-blind derivation from an adequate current-state handoff, or that replaying history is necessary for routine execution.
- **C17** *[sourced: repository state — fabricated-input episode]* "Deterministic" is not "true": hashes and reruns preserved an invalid evidence state until later inquiry exposed a source-authenticity problem. Reproducibility preserves whatever it is given, including error.
- **C18** *[inferential]* A recorded trajectory should generally be archived rather than deleted, but once a finding has been successfully compiled into the operational method and independently scrutinized, unnecessary history can leave routine active context. Archived provenance should be reactivated for method revision when current practice fails or becomes unexplained.

## Terminology discipline

- **C19** *[flagged]* Wolfram's computational irreducibility and bounded-observer vocabulary is used as naming, not as demonstrated explanation. Claim to guard against: treating the mere absence of a discovered deterministic reduction as evidence of genuine irreducibility.

## Evidence provenance — committed bundles (resolves V1, V2)

The source `observer-disagreement-framework` repository is private; its public evidence is the
committed `framework-self` bundle. The applied EUDR evidence uses the public
`geospatial-evidence-framework` Fazenda Sucuri bundle, copied into COIN as a reading snapshot with
JSON, GeoJSON, PDF, and canonical `report.html` artifacts omitted. Bundle-sourced claims below
upgrade the earlier generic "repository state" tag to specific round/file references.

- **C3′** *[sourced: bundles/framework-self/log.md; bundles/eudr-coffee-brazil-fazenda-sucuri/log.md]* Two committed bundles: framework-self (20 rounds, parties codex/claude) and the Fazenda Sucuri EUDR coffee bundle (7 native rounds).
- **C4′** *[sourced: bundles/eudr-coffee-brazil-fazenda-sucuri/log.md; bundles/eudr-coffee-brazil-fazenda-sucuri/answer.md]* The applied trajectory records repeated conversion of review findings into corrected artifacts: Sentinel-2 visual repair, AOI label/report-map fixes, coffee temporal-mask correction, and page-4 regional-overview repair, while preserving the screening verdict class.
- **C5′** *[sourced: bundles/eudr-coffee-brazil-fazenda-sucuri/s/task-scope.md; bundles/eudr-coffee-brazil-fazenda-sucuri/s/gsp-mapping.md]* The task scope fixes EUDR coffee screening for Brazil/Minas Gerais/Fazenda Sucuri and keeps production/evidence linkage explicit rather than silently generalizing from a commodity mask alone.
- **C-schema** *[sourced: bundles/eudr-coffee-brazil-fazenda-sucuri/s/modeling.md; bundles/eudr-coffee-brazil-fazenda-sucuri/r/results.md]* The modeling and results separate FDP-only, MapBiomas-only, and both-source agreement signals; new coffee/post-2020 loss overlap is source-specific rather than averaged into a single warrant.
- **C-frame4** *[sourced: bundles/framework-self/inquiry/round-0004.md]* Round 4 records a human-instructed scope widening (observer disagreement → statement evolution) as a frame transition f(t)→f(t+1) with SHA256 hashes and fc-supersedes on answer/pf/s pages. Direct support for C1–C2 and the "human framing is itself under inquiry" claim.
- **C-wolfram** *[sourced: bundles/framework-self/inquiry/round-0019.md; s/specification.md]* Rounds 18–19 make Wolfram observer theory a mandatory `fc-foundation-role: formal-analogy` disclosure with validator rejection conditions; specification frontmatter records `fc-irreducibility: none`. Upgrades C19 from [flagged] to [sourced].
- **C-metrics** *[sourced: bundles/framework-self/r/metrics-rounds-0001-0013.csv]* Frame-change frequency 2/13; observer-handoff 2/12; observer-distance family NOT_MEASURABLE with stated reasons; round 14 excluded to avoid circular self-measurement. Support for C12–C13 and C16's honest-negative half.
- **C-review** *[sourced: bundles/eudr-coffee-brazil-fazenda-sucuri/answer.md]* Current answer is `human_review_required`, provenance `pinned-not-reproduced`; the bundle records a screening flag, not a legal non-compliance determination. Support for C17–C18 and the structural human-in-the-loop boundary.

## Items still to verify

- **V3** Re-check C6–C9 against the current consolidated EUDR text and latest environment FAQ iteration at publication time; the cutoff date and Article 3 wording are stable, but degradation-condition phrasing has moved across FAQ iterations.
- **V4** No measurement yet exists for C16's open part (does compression reduce error recurrence?); mark as unresolved, not supported. The framework-self metrics confirm this is NOT_MEASURABLE from the current record, not merely unmeasured.
- **V5** Resolved in the committed COIN snapshot: the framework-self `_site/` rendered tree is not present; Markdown source and CSVs are retained; the applied EUDR bundle is the Fazenda Sucuri reading snapshot, with JSON, GeoJSON, PDF, and canonical `report.html` artifacts omitted.
- **V6** Some framework-self commit refs read "NOT AVAILABLE until merge" (rounds 19–20); pin the committed snapshot to a resolved state or note them as pending.
- **V7** No controlled comparison has yet tested trajectory-aware derivation against trajectory-blind derivation: competent observers with normal prior knowledge, shared explicit prior knowledge, and a specified current project state, with only one condition receiving the project-specific recorded trajectory.
- **V8** No controlled method-revision experiment has yet tested whether archived provenance materially improves diagnosis and revision when the current operational method encounters a contradiction, unexplained rule, frame failure, source-authenticity problem, or new class of case.

## Additional claims

- **C20** *[inferential]* Operational reducibility does not imply epistemic disposability when a later research state materially contradicts, invalidates, or reframes an earlier conclusion: a bundle chain can be reducible for routine execution while remaining non-disposable for epistemic audit.
- **C21** *[inferential]* A determination changes as a function of at least evidence (E), frame/assumptions/scope (F), and procedure/instructions (P); distinguishing evidence-driven, frame-driven, and procedure-driven change requires retaining more than the final state — approximately a minimum reconstructible state {claim, evidence, frame, procedure, verdict, reason-for-transition}.
- **C22** *[inferential]* Retained bundle history is provenance; method appears only when rules govern what to do with a material contradiction between states — reconstruct, compare, discriminate, supersede, retain conflict, or reopen. Retention supplies the evidence for the method; the rules constitute the method.
- **C23** *[flagged]* The present two bundles do not yet demonstrate that typed, reconstructible archived history actually improves later conflict resolution or method revision.
- **C24** *[inferential]* Implicit accumulated history, explicit scholarly compression, and the local project trajectory are distinct. The first two are historically produced prior knowledge; the third is the candidate mechanism under test.
- **C25** *[inferential]* A conventional research paper is already a history-compression mechanism: it normally turns collective research history into current knowledge, an identified gap, methods, results, assumptions, evidence, and limitations while omitting most failed hypotheses, abandoned analyses, local mistakes, and intermediate interpretations.
- **C26** *[inferential]* The burden of proof for permanent active trajectory retention is incremental: what does `H_{0:t}` preserve that a well-written paper, specification, source archive, codebase, test suite, provenance record, and unresolved-issues list do not?
- **C27** *[flagged]* Cross-observer transfer remains untested. Differences in `B_i` can be confounders or experimental variables, and trajectory retention may help, add noise, or matter only under particular frame conflicts.
- **C28** *[inferential]* Trajectory retention is a candidate handoff mechanism, not automatically the correct handoff design; a richer current-state representation may be sufficient for many routine continuation and execution tasks.
- **C29** *[inferential]* A recorded inquiry is a source-grounded ordered record below formal OKF-FC bundle conformance. It is not a simplified bundle, a lightweight bundle, an automatic fact-check, or an automatic disagreement case.
- **C30** *[inferential]* Representation proportionality should govern this research folder: preserve enough structure for the intended future use of a trajectory, and promote to a formal bundle only when stronger provenance, validation, reproducibility, contestation, metrics, or repeated reuse justify it.
- **C31** *[inferential; MHS recorded inquiry]* The MHS/world-models sequence is retained as a supporting recorded inquiry because it illustrates knowledge enrichment before explicit fact-checking. It is not counted as a third formal bundle case.
- **C32** *[inferential; MHS recorded inquiry]* The final MHS/world-models fact-checking question became salient only after earlier conceptual inquiry into MHS, Digital Twin analogy, and Free Energy Principle framing. A record beginning directly with "Did MHS make world models unnecessary?" would preserve the final question but omit that path.
- **C33** *[sourced; MHS recorded inquiry]* The exact saved MHS human-Claude Q/A was supplied after the initial migration as the `mhs-world-models-claude-qa` attachment and is preserved at `recorded-inquiries/mhs-world-models/MHS-QA-source.md`. The record should now be read as source-backed, with later interpretation kept separate in `analysis.md`.
- **C34** *[inferential; MHS recorded inquiry]* The pre-insertion state was itself a provenance gap: the public Sixth post interpreted an MHS trajectory that was not yet publicly inspectable in COIN. After insertion, the intended chain is `saved Q/A -> recorded inquiry -> retrospective analysis -> public article`, so public-site correction can inspect a primary COIN artifact rather than treating the article as evidence for its own interpretation.
