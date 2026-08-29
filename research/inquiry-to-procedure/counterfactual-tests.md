---
inquiry: inquiry-to-procedure
title: Counterfactual Tests for Recorded Inquiry and Method Evolution
status: draft
updated: 2026-08-24
---

# Counterfactual tests

These are proposed experiments, not results. They are designed to test which value, if any, recorded
project-specific inquiry trajectories add beyond prior knowledge, explicit scholarly compression,
adequate current-state handoff, provenance, and auditability.

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
X_state = {L, S_t, A_t, U_t, M_t}
```

where `A_t` is explicit assumptions and framing constraints, `U_t` is unresolved issues / known
uncertainty, and `M_t` is the current operational method.

```text
X_traj = X_state + H_{0:t}
```

The empirical question is not whether history matters in general. It is whether, for observer `j`,
trajectory access improves relevant outcomes beyond a sufficiently explicit current-state handoff:

```text
Q_j(X_traj) > Q_j(X_state)
```

`Q` may include continuation quality, error detection, correction quality, avoidance of superseded
assumptions, transfer quality, robustness to frame differences, or convergence toward an independent
external reference `G` when such a reference is defensible. These measures should not be assumed to
collapse into one universal scalar score.

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
handoff inputs include finished code, validators, specifications, or instructions produced by the
trajectory, then H- is no longer trajectory-blind in the relevant sense. A clean method-formation
version should not give H- already-compiled operational artifacts whose derivation is the target of
the experiment.

This test addresses method formation. It asks whether archived trajectory improves derivation of
operational method compared with derivation from prior knowledge plus an explicit current-state
handoff.

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

## External-reference convergence

Preserve the distinction between observer agreement and correctness. Observer-to-observer agreement
can measure handoff convergence, but it is not evidence of correctness by itself. When a defensible
independent reference state or observation `G` exists, a separate question is whether the resulting
determination moves closer to that reference:

```text
epsilon_t = d(D_t, G)
```

The two questions are distinct:

1. Does trajectory access improve observer-to-observer handoff, method quality, diagnosis, or
   transfer?
2. Does the resulting inquiry move closer to `G` where such a reference exists?

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
