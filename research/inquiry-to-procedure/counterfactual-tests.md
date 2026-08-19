---
inquiry: inquiry-to-procedure
title: Counterfactual Tests for Recorded Inquiry and Method Evolution
status: draft
updated: 2026-08-19
---

# Counterfactual tests

These are proposed experiments, not results. They are designed to test which value, if any,
recorded inquiry trajectories add beyond provenance and auditability.

## Test 1 - history-aware vs history-blind method formation

Give two comparable human-AI agents the same problem and final evidence.

- **Condition H+:** access to the recorded trajectory, including assumptions, corrections,
  supersessions, failed approaches, evidence changes, and unresolved questions.
- **Condition H-:** no trajectory; access only to the agreed final evidence and problem inputs.

Compare whether the two conditions derive equivalent:

- decomposition;
- procedures;
- validation rules;
- AI instructions;
- open questions;
- known guardrails.

This test must avoid leakage from artifacts that already encode the historical result. If the final
inputs include finished code, validators, specifications, or instructions produced by the trajectory,
then H- is no longer history-blind in the relevant sense. A clean version should give H- the final
evidence and problem, but not the already-compiled operational method being tested for derivability.

This test addresses method formation. It asks whether archived trajectory improves derivation of
operational method compared with final-state derivation.

## Test 2 - operational sufficiency

Give an agent only the current operational method plus new evidence.

The operational method should include the current specifications, code, tests, validators, AI
instructions, evidence semantics, decision procedures, and explicit unresolved questions required to
perform the task now.

Measure whether the task can be executed correctly without loading or replaying historical rounds.
This tests whether successful reduction has made history unnecessary for routine execution.

This does not test whether history was useful during discovery. A positive result is expected if the
method has been successfully compiled.

## Test 3 - revision under failure

Introduce a new contradiction, frame failure, source-authenticity problem, unexplained operational
constraint, or new class of case.

Compare two conditions:

- **M only:** access to the current operational method and the failure case.
- **M + H:** access to the current operational method, the failure case, and archived trajectory /
  provenance.

Measure whether provenance materially improves diagnosis, prevents reintroduction of superseded
assumptions, explains the origin of existing constraints, or produces a better revision to the
operational method.

This test addresses method revision. It asks whether archived provenance should be reactivated when
the current method fails or becomes unexplained.

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
