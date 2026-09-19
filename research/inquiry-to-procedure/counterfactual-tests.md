---
inquiry: inquiry-to-procedure
title: Counterfactual Tests for Recorded Inquiry and Method Evolution
status: draft
updated: 2026-09-19
---

# Counterfactual tests

These are proposed experiments, not results. They are designed to test which value, if any, recorded
project-specific inquiry trajectories add beyond prior knowledge, explicit scholarly compression,
adequate current-state handoff, provenance, and auditability.

The public synthesis's three examples should not be read as three completed counterfactual tests or
as three formal recorded bundle trajectories. Fazenda Sucuri and framework-self provide descriptive
bundle-backed evidence of correction and frame revision. Estonian forest management supplies a
non-bundle conflict-analysis comparison for interpretation and contestation. None of the three
settles the stronger causal question of whether explicit trajectory access outperforms a sufficiently
rich current-state handoff.

The Fazenda Sucuri round-10 audit adds a design constraint for every proposed test below: a ledger's
task motivation is **recorded provenance**, not automatically **verified provenance** of the
originating observation. If an experiment studies diagnostic transfer, it must capture the source
AOI/artifact, observation time, transfer decision, target execution, and recorded attribution as
distinct events. Retrospective visual similarity must not substitute for those links.

## Terminology and handoff classes

No observer begins from zero. For observer `i`, the available starting knowledge can be represented
as:

```text
K_i^0 = B_i + L + S_0
```

where `B_i` is the observer's background knowledge, prior learning, tacit competence, learned
regularities, relevant framing, and biases; `L` is explicitly communicated prior knowledge such as
literature, standards, documentation, established results, and current scholarly synthesis; and
`S_0` is the project/problem state at handoff. `B_i` is partly latent and cannot be exhaustively
serialized by the bundle.

The project-specific inquiry trajectory is:

```text
H_{0:t}: S_0 -> S_1 -> ... -> S_t
```

"History-blind" therefore means blind to the recorded local project trajectory, not devoid of prior
knowledge. A history-blind participant still has `B_i + L`, and the experiment must specify how much
of the current project state is handed over.

Useful handoff classes:

```text
X_min = {L, S_t}
```

```text
X_state = {L, S_t, E_t, A_t, U_t, M_t, V_t}
```

where `S_t` is the current project/problem state, `E_t` is the current evidence state and relevant
source versions, `A_t` is explicit assumptions and framing constraints, `U_t` is unresolved issues /
known uncertainty, `M_t` is the current operational method, and `V_t` is queryable verification
provenance: citations, hashes, artifact paths, source references, procedure/version references, and
other inspectable links needed to verify why the current state says what it says.

```text
X_traj = X_state + H_{0:t}
```

Their intended nesting is:

```text
X_{\min} \subset X_{\mathrm{state}} \subset X_{\mathrm{traj}}
```

`X_traj` therefore adds the recorded project-specific trajectory to the sufficiently explicit
current-state handoff. The `X_min -> X_state` comparison concerns the value of compiled/current-state
knowledge; the `X_state -> X_traj` comparison concerns the remaining incremental value, if any, of
explicit trajectory access.

For conflict interpretation, the representation choice should remain proportional:

- **Current-state evidence record:** enough when present definitions, assumptions, evidence,
  transformations, and verification links are explicit and recoverable.
- **Conflict bundle:** useful when competing claims must be compared across evidence, frames,
  accounting objects, boundaries, indicators, time horizons, or normative criteria.
- **Trajectory-aware conflict bundle:** useful when the interpretation depends on reconstructing how
  claims, frames, evidence selections, definitions, boundaries, counterarguments, assumptions, or
  normative criteria changed through time.

These are not universal promotion rules. More recorded history is valuable only when it improves the
task relative to a lighter representation.

The empirical question is not whether history matters in general. It is whether, for observer `j`,
trajectory access improves relevant outcomes beyond a sufficiently explicit current-state handoff:

```text
Q_j(X_traj) > Q_j(X_state)
```

`Q` may include continuation quality, error detection, correction quality, avoidance of superseded
assumptions, transfer quality, robustness to frame differences, contestation quality, or convergence
toward an independent external reference `G` when such a reference is defensible. These measures
should not be assumed to collapse into one universal scalar score.

A technical or evidentiary determination can be represented as:

```text
T_t = f(E_t, F_t, P_t)
```

where `F_t` is the active frame / assumptions / scope / definitions and `P_t` is the procedure /
method / instruction version. Where the project has the evidence and institutional authority to
represent one, a downstream legal or operational disposition can be represented separately as:

```text
D_t = g(T_t, L_t, J_t)
```

where `L_t` is the applicable legal/operational rule set and `J_t` is the relevant jurisdictional or
institutional context. A challenged "result" may be `T_t`, a screening result, a classification, a
human-review flag, or `D_t`; "decision" should not be automatically equated with `D_t`.

## Test 1 - trajectory-aware vs trajectory-blind method formation

Give comparable human-AI agents the same problem, explicit prior knowledge `L`, and project state
`S_t`, while treating each observer's `B_i` as either a controlled matching criterion or an
experimental variable.

- **Condition H+:** access to `X_traj`, including the recorded project trajectory: assumptions,
  corrections, supersessions, failed approaches, evidence changes, frame changes, method changes,
  and unresolved questions.
- **Condition H-:** access to `X_min` or a carefully specified subset of `X_state`, but no
  `H_{0:t}`.

Compare whether the two conditions derive equivalent:

- decomposition;
- procedures;
- validation rules;
- AI instructions;
- open questions;
- known guardrails.

This test must avoid leakage from artifacts that already encode the historical result. If the
handoff inputs include finished code, validators, specifications, reading guides, prompts,
instructions, tests, or other artifacts produced by the trajectory, then H- is no longer
trajectory-blind in the relevant sense. A clean method-formation version should not give H-
already-compiled operational artifacts whose derivation is the target of the experiment.

This test addresses method formation. It asks whether archived trajectory improves derivation of
operational method compared with derivation from prior knowledge plus an explicit current-state
handoff.

For diagnostic-task formation, pre-register and preserve the chain `observation origin -> diagnostic
transfer -> target execution -> recorded provenance`. Score an origin or transfer claim only when
the corresponding contemporaneous artifact exists; otherwise classify it as underdetermined.

## Test 2 - operational sufficiency

Give an agent with normal prior knowledge the current operational method plus new evidence.

The operational method should include the current specifications, code, tests, validators, AI
instructions, evidence semantics, decision procedures, and explicit unresolved questions required to
perform the task now.

Measure whether the task can be executed correctly without loading or replaying historical rounds.
This tests whether successful reduction has made history unnecessary for routine execution.

This does not test whether the trajectory was useful during discovery. A positive result is evidence
of successful reduction into `M_t`, not evidence that history played no role in method formation.

## Test 3 - revision under failure

Introduce a new contradiction, frame failure, source-authenticity problem, unexplained operational
constraint, or new class of case.

Compare two conditions:

- **Current-state revision:** observer has normal prior knowledge plus `X_state` and the failure
  case.
- **Trajectory-aware revision:** observer has normal prior knowledge plus `X_traj` and the failure
  case.

Measure whether provenance materially improves diagnosis, prevents reintroduction of superseded
assumptions, explains the origin of existing constraints, or produces a better revision to the
operational method.

This test addresses method revision. It asks whether archived provenance should be reactivated when
the current method fails or becomes unexplained.

## Test 4 - cross-observer handoff / transfer

Test whether project-specific history compensates for differences in prior observer knowledge or
framing:

```text
B_A != B_B
```

Observer A forms or revises a method in one project context. Observer B receives either `X_state` or
`X_traj` and attempts to continue, adapt, audit, or transfer the method.

Possible outcomes include:

- trajectory materially improves transfer;
- current-state documentation is sufficient despite different backgrounds;
- trajectory helps only for certain frame changes or conflicts;
- trajectory adds noise, stale assumptions, or misleading local context.

For human studies, avoid naive within-person H+/H- comparisons that leak trajectory knowledge.
Prefer matched, counterbalanced, or independent-observer designs as appropriate.

## Test 5 - recorded-inquiry trajectory versus final-claim start

The MHS/world-models record suggests a future, controlled test design; it is not
itself a completed experiment.

- **Condition A:** participant receives only the final MHS/world-models claim
  plus the relevant primary and secondary sources.
- **Condition B:** participant receives the recorded inquiry trajectory plus the
  same final sources.

The question is whether access to the earlier conceptual path changes source
weighting, claim formulation, or evaluation quality. A valid experiment would
need controlled inputs, comparable participants or agents, and predeclared
evaluation criteria. The present MHS record must not be reported as evidence
that recorded trajectory generally improves fact-checking.

## Test 6 - contestation of a determination or disposition

External contestation is a reopening trigger, not itself method revision. The proposed test is
whether explicit trajectory access improves the quality of a challenge beyond an equivalently rich
current-state handoff:

```text
Q_C(X_traj) > Q_C(X_state)
```

The negative is equally meaningful:

```text
Q_C(X_traj) <= Q_C(X_state)
```

where `Q_C` denotes quality of contestation or challenge and need not be reducible to a single
universal scalar score.

Give independent comparable challengers the same contested result and underlying source access.

- **Condition A:** contested `T_t`, or where applicable `D_t`, plus `X_state`.
- **Condition B:** contested `T_t`, or where applicable `D_t`, plus `X_traj`.

The only intended difference should be explicit access to the project-specific trajectory
`H_{0:t}`. `X_state` must remain information-rich: it includes the current operational method,
current evidence/project state, assumptions and frame, unresolved issues, and queryable verification
provenance `V_t`.

The trajectory object is the recorded research-state vocabulary: claims and counterclaims, evidence,
assumptions, frames, procedures, interpretations, transition rationales, rejected alternatives,
supersessions, conflicts, and unresolved questions. It is not private cognition or chain-of-thought.

Possible outcome dimensions include whether the challenger can:

- identify a material evidentiary weakness;
- identify omitted or differently weighted evidence;
- identify frame or scope dependence;
- identify procedure dependence;
- reconstruct a rejected but previously defensible alternative;
- locate the transition that materially produced the current result;
- distinguish an evidence change from a frame or procedure change;
- where `D_t` is involved, distinguish a change in `T_t` from a change in `L_t` or `J_t`;
- identify discriminating evidence or analysis that could resolve the disagreement;
- avoid merely producing more criticism without stronger grounding.

Prefer independent observers or otherwise controlled designs. Avoid naive within-person tests where
the participant cannot unlearn the trajectory.

If a controlled comparison finds:

```text
Q_C(X_state) ≈ Q_C(X_traj)
```

that would be evidence in favor of stronger compression into the current-state handoff, not a failed
experiment.

### Estonian forest-management variant

The Estonian case should be tested as a proposed conflict-interpretation experiment, not reported as
a completed result. Compare investigators or agents given:

- **Condition A:** a sufficiently rich current-state dossier of the Estonian forest-management
  disagreement, including the endpoint claims, cited sources, accounting objects, system boundaries,
  indicators, time horizons, definitions, assumptions, uncertainty, and relevant normative criteria.
- **Condition B:** the same dossier plus a structured trajectory of how the relevant claims,
  evidence selections, accounting boundaries, definitions, counterarguments, interpretation of
  indicators, normative criteria, and revisions developed.

Possible outcome measures include the ability to:

- identify whether the claims genuinely contradict;
- identify hidden frame changes;
- reconstruct why previous conclusions were defensible at the time;
- detect changed definitions or accounting objects;
- separate evidence disagreement from frame, scale, time-horizon, or normative disagreement;
- improve the quality of contestation;
- avoid falsely collapsing different questions into one binary verdict.

This test directly addresses the corrected Estonian interpretation. The case provides a strong
reason to construct and study a trajectory-aware conflict bundle, but it does not establish that an
equivalently rich current-state dossier could not resolve or adequately diagnose the disagreement.

## External-reference convergence

Preserve the distinction between observer agreement and correctness. Observer-to-observer agreement
can measure handoff convergence, but it is not evidence of correctness by itself. When a defensible
independent empirical reference state or observation `G` exists, a separate question is whether the
resulting technical/evidentiary determination `T_t` moves closer to that reference:

```text
delta_t = d(T_t, G)
```

Here `G` is an independently defensible empirical/reference state, and `d` is a task-appropriate
distance or error measure. Decreasing `delta_t` indicates movement toward that reference only within
the validity of `G` and `d`; it does not by itself validate the selected reference, distance measure,
legal interpretation, or operational disposition.

Keep three validation axes separate:

1. **Incremental trajectory value:** does explicit trajectory access improve formation,
   continuation, diagnosis, revision, or transfer beyond a sufficiently explicit current-state
   handoff?
2. **External-reference correspondence:** does the technical/evidentiary determination move closer
   to a defensible independent reference `G` where such a reference exists?
3. **Inter-observer agreement or convergence:** do different observers reach similar results?

Agreement does not establish correctness. External-reference correspondence does not by itself
establish the value of recorded trajectory. Conversely, a downstream legal or operational disposition
`D_t` should not be silently substituted for `T_t` unless `G` itself is specifically a defensible
legal/operational disposition reference.

## Provisional method-evolution protocol

The current inquiry suggests a candidate protocol, not an empirically validated best practice:

1. Record a finding or state transition.
2. Classify what changed: evidence, frame, assumption, procedure, semantics, instruction,
   uncertainty, or source authenticity.
3. Decide whether the finding is local, generalizable, or unsafe to generalize.
4. Select its operational destination:
   - code;
   - test;
   - validator;
   - specification;
   - agent instruction;
   - evidence-semantic rule;
   - unresolved question;
   - provenance only.
5. Verify the reduction independently enough to avoid turning a reproducible error into a durable
   rule.
6. Once compiled and verified, remove unnecessary history from routine active context.
7. Preserve the historical record as provenance.
8. Reactivate provenance when later failure provides a reason to revisit how the current method
   arose.

The fabricated-input/source-authenticity case remains an important warning: compilation into
deterministic machinery does not establish epistemic correctness.
