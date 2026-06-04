# Conflict Bundle Design Notes - Evidence First, Consensus Later

**Purpose:** define the minimum record needed for a conflict over environmental governance to become inspectable without pretending that the record resolves the conflict.

---

## Minimum record per conflict

1. **Conflict object**
   The forest, river, land-use decision, ecosystem service, climate claim, or policy intervention under dispute.

2. **Claim set**
   Each asserted position, including who asserted it, when, and under which institutional role.

3. **Evidence references**
   The evidence bundle, dataset, report, model output, legal document, or submission that each claim references.

4. **Model state**
   Model family, version, parameters, spatial resolution, time horizon, scenario assumptions, and uncertainty treatment.

5. **Disagreement dimension**
   Classify whether the disagreement is empirical, model-based, legal, economic, value-based, or mixed.

6. **Boundary choices**
   Record spatial boundary, temporal boundary, accounting convention, stakeholder scope, and omitted externalities.

7. **Review state**
   Record whether a claim is submitted, reviewed, challenged, updated, deprecated, or superseded.

8. **Governance decision**
   If a governance body acts on the conflict bundle, record the decision separately from the evidence and model outputs.

## Design prohibitions

1. Do not compress the conflict into a single dashboard score unless the weighting method is explicit and separately reviewable.
2. Do not treat blockchain anchoring as peer review.
3. Do not treat AI summaries as findings.
4. Do not place settled scientific findings and manufactured controversy in symmetrical conflict slots.
5. Do not hide value choices inside model parameters.

## Example application: Estonian forestry

A conflict bundle should record short-term carbon accounting, long-term timber-substitution accounting, biodiversity indicators, legal restrictions, rural-economic claims, and ownership/land-category differences as separate dimensions. It should also type the increment number being used:

1. Eurostat/Statistics Estonia: net annual increment on forest available for wood supply, 9.1 million m3 in 2023, compared with 11.6 million m3 removals.
2. IEA Bioenergy: average annual increment of growing stock in managed forests, 12.8 million m3/year for 2007-2017.
3. Estonian Climate Ministry: average annual increment, 16.2 million m3/year for 2011-2019.
4. Carbon-stock/LULUCF frame: business-as-usual felling around 11.5 million m3/year may reduce 2050 growing stock, while 9.4-9.8 million m3/year is associated with stable or increasing stock in the cited additional-measures scenario.

A digital twin can show what follows under each framework, but the trade-off remains a governance decision.

## Example application: climate attribution

A conflict bundle should include open scientific questions around feedbacks, regional effects, and scenario uncertainty. It should not treat the basic attribution of recent global warming to human activity as an unresolved symmetrical dispute.

---

*Last updated: 4 June 2026*
