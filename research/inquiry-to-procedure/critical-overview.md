---
inquiry: inquiry-to-procedure
title: From Inquiry to Procedure — Critical Overview
status: draft
updated: 2026-08-24
---

# Critical overview

This note records what the evidence supports, where the proposition overstates, and which parts of
the case remain contested. It is the working evaluation behind the public article, and it is
deliberately more sceptical than the public prose.

## What the case is

The inquiry is no longer best framed as asking whether the trajectory itself is the method. The
corrected ontology separates three objects:

- **Recorded trajectory `H`:** provenance of method formation, including observable assumptions,
  corrections, supersessions, frame changes, rejected approaches, evidence changes, and state
  transitions.
- **Method-evolution protocol `P`:** the procedure that consumes such provenance and decides what a
  finding should become: code, test, validator, specification, agent instruction,
  evidence-semantic rule, unresolved question, or provenance-only record.
- **Operational method `M`:** the current specifications, code, tests, validators, AI instructions,
  evidence semantics, decision procedures, and explicit unresolved questions needed to perform the
  task now.

Routine execution should normally be `M + current/new evidence E -> result`. Historical provenance
can become relevant again when revising `M`, but that does not make the whole trajectory part of the
routine operational method.

This correction still needs one more distinction. No observer begins from zero. The relevant
starting point for observer `i` can be represented as:

```text
K_i^0 = B_i + L + S_0
```

where `B_i` is the observer's background knowledge, prior learning, tacit competence, learned
regularities, and relevant prior framing; `L` is explicitly communicated prior knowledge such as
literature, standards, documentation, established results, and current scholarly synthesis; and
`S_0` is the current project/problem state at handoff. `B_i` is partly latent and cannot be
exhaustively serialized by a bundle.

The local project trajectory is instead:

```text
H_{0:t}: S_0 -> S_1 -> ... -> S_t
```

The non-trivial comparison for another observer `j` is therefore:

```text
B_j + L + S_t
```

versus:

```text
B_j + L + S_t + H_{0:t}
```

In this note, "history-blind" means blind to the project-specific recorded trajectory, not devoid of
prior knowledge. The first two forms of historical dependence are not novel here: implicit
accumulated history is embodied in human education, experience, disciplinary convention, tacit
knowledge, biases, and in AI model training/capabilities; explicit scholarly compression is embodied
in papers, reviews, standards, documentation, code, and accepted methods. The experiment concerns
the third: the local project trajectory.

The evidence has two tiers:

- **Formal bundle cases:** the observer-disagreement framework (general and
  partly self-referential) and the EUDR geospatial evidence repository
  (applied). These are the stronger evidence for claims about bundle evolution
  and method formation.
- **Supporting recorded inquiries:** smaller, source-grounded records below
  bundle conformance. The MHS/world-models record illustrates knowledge
  enrichment before explicit fact-checking, but it does not demonstrate bundle
  evolution and is not a third formal case.

The Fazenda Sucuri coffee screening sequence remains the applied formal-bundle
example.

## What the evidence supports

1. **The bundles demonstrate provenance of observable method formation.** They record changes in
   assumptions, scope, evidence semantics, artifacts, validation expectations, and unresolved
   questions. This supports claims about recorded research-state evolution, not a full cognitive
   reconstruction of either the human or the model.

2. **The records show transformation into operational artifacts.** Inquiry findings were in fact
   converted into code, tests, specifications, validators, AI instructions, source-semantics
   constraints, and explicit uncertainty. This demonstrates transformation. It does not demonstrate
   that the historical record itself constitutes method.

3. **A candidate meta-method is visible.** Across the two cases, findings are classified, routed to
   operational destinations, checked, and then either compiled into current method or left as
   provenance. That transformation procedure can be described as a provisional method-evolution
   protocol, but it is not yet validated as best practice.

4. **A regulation-grounded EUDR decomposition remains a durable result.** Layers A
   (land/forest-change evidence), B (production linkage), and C (commodity-specific evidence) follow
   from the EUDR evidence problem and are more precise than a single commodity-mask method. The
   historical rounds that led to this decomposition are provenance of method formation; the current
   decomposition is part of the operational EUDR method.

## Where the proposition overstates

1. **Historical dependence of discovery is not operational dependence of execution.** The fact that
   a trajectory contributed causally to discovering a method does not imply that the trajectory is
   required to execute the resulting method. A laboratory notebook can show how a procedure was
   discovered without being part of the procedure. A build trace can help produce an executable
   without being needed to run it.

2. **The incremental trajectory value has not been tested.** The two bundles do not compare
   trajectory-aware derivation against trajectory-blind derivation by observers who still have
   background knowledge, shared explicit prior knowledge, and a sufficiently specified current
   project state. They therefore cannot show whether access to `H_{0:t}` improves method formation
   beyond what a competent investigator could derive from `B_j + L + S_t`.

3. **Operational sufficiency is a separate question.** If an agent can apply the current method to
   new evidence without replaying historical rounds, that is expected after successful reduction. It
   does not show that the trajectory lacked value during discovery.

4. **Method revision is another untested question.** The evidence does not yet show whether archived
   provenance materially improves diagnosis when the current method fails, contains an unexplained
   constraint, encounters a source-authenticity problem, or faces a new class of case.

5. **"Deterministic" is quietly doing too much work unless checked.** The fabricated-input episode is
   the standing counter-example: reproducibility preserved an invalid evidence state. Determinism and
   epistemic correctness are separate properties. Any wording that lets "reduced to code" imply
   "verified as correct" is an overstatement and should be caught in review.

6. **Wolfram terminology risks smuggling in an explanation.** Computational irreducibility and the
   bounded observer are used as vocabulary. The failure mode to guard against is treating the absence
   of a discovered reduction as proof of irreducibility. As motivation this is fine; as a claim about
   the research process it is unsupported.

7. **A conventional paper is a strong comparison class.** This is an analytical comparison, not a
   source-established empirical result. A scientific paper is already a deliberate compression of
   history:

   ```text
   collective research history
       -> current state of knowledge
       -> identified gap
       -> method/result
   ```

   Papers normally omit failed hypotheses, abandoned analyses, every prompt or conversation, most
   local mistakes, and many intermediate interpretations. This omission is generally not treated as
   a methodological defect if the relevant result, method, assumptions, evidence, and limitations are
   adequately communicated. The burden of proof for permanent active trajectory retention is
   therefore: what does the explicit local inquiry trajectory preserve that a well-written paper,
   specification, source archive, codebase, test suite, provenance record, and explicit
   unresolved-issues list do not?

## Roles, not forced alternatives

"Provenance," "external memory," and "compilation substrate" should not be treated as three mutually
exclusive interpretations.

- **Provenance** describes what the record is epistemically: evidence of what happened in the
  inquiry.
- **External memory** describes one way an agent can access or use the record: loading past states to
  guide present work.
- **Compilation substrate** describes one possible role the record can play inside a transformation
  process: material that a method-evolution protocol reads when deciding what to compile into `M`.

The corrected claim is therefore not that provenance was defeated by compilation. It is that
recorded provenance can be used by a method-evolution protocol, and successful outputs of that
process belong to the operational method.

## What remains contested

- **Trajectory-aware vs trajectory-blind formation.** Could a competent human-AI investigator, given
  appropriate background knowledge, explicit prior knowledge, and a sufficiently specified current
  project state but no recorded trajectory, derive substantially the same operational method,
  instructions, guardrails, and unresolved questions? This has not been tested.
- **Revision value of archived provenance.** When `M` fails, does access to `H` improve diagnosis,
  prevent reintroduction of superseded assumptions, or produce better revisions? This has not been
  tested.
- **Cross-observer transfer.** Whether recorded project history compensates for differences in
  observer background knowledge or framing beyond what a rich current-state handoff provides is
  still unresolved.
- **Coupling in the EUDR decomposition.** Layer B couples A and C: the deforestation test is not
  fully independent of commodity semantics because production linkage is required. Whether the clean
  three-layer picture survives messy supply-chain data is not yet tested.

## Editorial cautions for the public draft

- Do not describe the trajectory as itself the method merely because it helped produce the method.
- Keep the negative conclusion visible: the existing two cases demonstrate transformation, not
  incremental trajectory value beyond a rich current-state handoff.
- Present EUR-Lex / FAQ facts as drawn from the regulation with citations; re-verify degradation
  wording against the latest FAQ iteration at publication (see claims V3).
- Evidence is provided as two bundles committed into COIN (`bundles/framework-self/`,
  `bundles/eudr-coffee-brazil-fazenda-sucuri/`). The framework-self source is private; the applied
  EUDR source is mirrored as a public reading snapshot with JSON, GeoJSON, PDF, and canonical
  `report.html` artifacts omitted. See `bundle-evolution-analysis.md`. The remaining open
  provenance caveat is the framework-self "NOT AVAILABLE until merge" refs (claims V6), which are
  flagged rather than silently removed.
- MHS is supporting recorded-inquiry evidence only. Do not describe it as a
  bundle, do not give it `fc-*` metadata, and do not infer observer
  disagreement merely because an external headline becomes the claim object
  under examination.
- The EUDR bundle's own state is `human_review_required` / `pinned-not-reproduced`. Do not let the
  public prose imply the evidence is reproduced or that a legal compliance verdict has been reached;
  it has not.

## Verdict (draft)

The inquiry demonstrates observable conversion of recorded findings into operational artifacts:
code, tests, specifications, validators, instructions, evidence semantics, and retained uncertainty.
It does not demonstrate the incremental advantage of `H_{0:t}` beyond prior knowledge and a rich
current-state handoff, either for initial method formation or for later method revision. The
publishable result is narrower and cleaner: recorded trajectories are provenance of method
formation, a candidate method-evolution protocol may use that provenance to revise operational
method, and successfully compiled lessons need not remain in routine active context.
