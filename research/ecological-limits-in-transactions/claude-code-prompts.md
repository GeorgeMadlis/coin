# Claude Code Prompts — Ecological Limits in Transactions

**Inquiry:** "Ecological limits will remain politically weak and economically secondary until they are built into transactions themselves rather than handled afterward by taxes, standards, and reporting."

**Source paper:** Valdsalu & Aaslaid (2026), *Ecological limits in economic systems: A regeneration-linked constraint mechanism*. Single.Earth Foundation Working Paper No. 1.

**Purpose:** These prompts are designed to be run in Claude Code. Each prompt is self-contained and tests a distinct aspect of the originating claim. They move from mechanism formalization, through empirical comparison, to simulation and governance analysis.

---

## Prompt 1 — Implement and run the Valdsalu-Aaslaid burn mechanism

```
Implement the regeneration-linked ecological accounting mechanism described in the
Valdsalu-Aaslaid (2026) Single.Earth working paper.

The core formula is:
  B_i = V_i × E_i × α

where:
  V_i  = transaction value (monetary)
  E_i  = ecological intensity (ecological impact per unit of transaction value)
  α    = system calibration factor

The system must also satisfy:
  Flow constraint:   B_t ≤ I_t       (total burn ≤ regeneration in each period)
  Stock constraint:  S_t ≤ C_t       (circulating ecological units ≤ ecological capacity)
  Dynamic:           S_{t+1} = S_t + I_t - B_t

Tasks:
1. Write a Python class `EcologicalAccountingSystem` that tracks:
   - Ecological unit stock S
   - Period-level regeneration I
   - Per-transaction burn B
   - Running deficit D when B > I
2. Simulate 52 weekly periods with:
   - Regeneration I_t drawn from N(100, 10) each period
   - 200 transactions per period with V ~ Uniform(1, 50) and E ~ Beta(2, 5)
   - α = 1.0 initially, then adaptive: α increases by 0.05 when 3 consecutive
     deficit periods occur, decreases by 0.02 when 5 consecutive surplus periods occur
3. Plot:
   a. Stock S_t over time with ecological capacity C = 1000 as a horizontal reference
   b. Period burn vs regeneration (B_t and I_t on same axis)
   c. Cumulative deficit over time
4. Print a summary: total periods in deficit, mean deficit size, final stock, final α
5. Save the plot to ecological_mechanism_simulation.png

Use numpy for sampling, matplotlib for plots. Seed random state to 42 for reproducibility.
```

---

## Prompt 2 — Retrieve and compare EU ETS carbon price history against emissions trajectories

```
Retrieve publicly available data on EU Emissions Trading System (EU ETS) carbon prices
and covered-sector CO2 emissions from 2005 to 2023. Use web search and fetch to find
the data.

Tasks:
1. Search for and retrieve:
   - Annual EU ETS carbon price (EUA spot or settlement price, €/tonne CO2)
   - Annual verified emissions from EU ETS Phase 1 through Phase 4 (covered sectors)
   - Comparison: total EU GDP over the same period (as a normalizer for economic activity)
   Sources to try: EEA, European Commission, Ember, Our World in Data, Sandbag/Carbon Tracker

2. Build a pandas DataFrame with columns:
   year, eua_price_eur, covered_emissions_mtco2, eu_gdp_eur_bn, emissions_per_gdp

3. Produce a dual-axis chart:
   - Left axis: EUA carbon price (bar chart, blue)
   - Right axis: covered-sector emissions intensity (emissions / GDP, line, red)
   Mark the years 2008 (financial crisis), 2013 (Phase 3 start), 2019 (Market Stability
   Reserve activation), 2021 (price recovery) as vertical reference lines with labels.

4. Run a Pearson correlation and a simple OLS regression of
   emissions_per_gdp ~ eua_price_eur. Report the coefficient, p-value, and R².

5. Write 3–5 sentences interpreting the result specifically in relation to this question:
   "Does the historical ETS record show that price-based ex post instruments can make
   ecological limits economically binding, or does the record support the claim that they
   are structurally weak?"

Save the chart to ets_price_vs_emissions.png and the DataFrame to ets_data.csv.
```

---

## Prompt 3 — Compare instrument categories: structural ex ante vs. ex post calibration

```
Design and run a comparative agent-based simulation to test whether a transaction-embedded
ecological constraint outperforms a price-based ex post tax in keeping aggregate
ecological consumption within regenerative limits.

Model setup (implement in Python with Mesa or plain numpy arrays):
- 500 economic agents, each making 1 transaction per period
- Each transaction has value V ~ LogNormal(3, 1) and ecological intensity E ~ Beta(2,4)
- Ecological regeneration budget per period: R = 5000 ecological units
- Run for 100 periods

Instrument A — Ex ante transaction burn (Valdsalu-Aaslaid mechanism):
  - Each transaction burns B = V × E × α units from a shared ecological pool
  - If pool reaches zero, high-intensity transactions (E > 0.6) are blocked that period
  - α is recalibrated every 10 periods to target B_total = R

Instrument B — Ex post carbon tax equivalent:
  - All transactions proceed regardless of ecological impact
  - At end of each period, agents with total ecological burn > threshold T pay a tax
  - Tax revenue is notional (does not reduce ecological burden, only monetary cost)
  - T and tax rate are recalibrated every 10 periods to target average compliance

Instrument C — Baseline (no constraint):
  - Transactions proceed with no ecological accounting

Metrics to track per period for each instrument:
  - Total ecological consumption vs regeneration (overshoot = consumption - R when > 0)
  - Cumulative overshoot
  - Number of periods in ecological deficit
  - Gini coefficient of transaction values (distributional effect of constraint)

Output:
1. Three-panel time-series plot: cumulative ecological overshoot per instrument
2. Bar chart: total overshoot across 100 periods, per instrument
3. Box plot: Gini coefficients per instrument across all periods
4. Markdown table summarising: mean overshoot per period, total deficit periods,
   mean Gini, and a one-sentence interpretation for each instrument

Save plots to instrument_comparison.png and summary to instrument_summary.md.
```

---

## Prompt 4 — Assess measurement feasibility: how coarse is sector-level ecological intensity?

```
The Valdsalu-Aaslaid mechanism assigns each transaction an ecological intensity
coefficient E_i derived from sector-level lifecycle assessment data. The paper
acknowledges this is coarse. Test how much intra-sector variation in ecological
intensity is masked by sector-level averaging.

Tasks:
1. Search for and retrieve publicly available data on ecological intensity or carbon
   intensity at firm or product level within at least two sectors where such data exists.
   Good candidates:
   - Steel production (BF-BOF vs EAF routes, CO2/tonne)
   - Cement production (clinker ratio variation, CO2/tonne)
   - Electricity generation (CO2/MWh by fuel type and plant efficiency)
   - Agricultural commodity production (CO2e/kg across production systems)
   
   Sources to try: IEA, IPCC AR6 WG3 annex data, European EPER/E-PRTR database,
   Our World in Data, peer-reviewed lifecycle assessment meta-analyses.

2. For each sector retrieved, compute:
   - Mean intensity (sector-level average, as would be used in the mechanism)
   - Standard deviation and coefficient of variation
   - Ratio of 90th percentile to 10th percentile intensity within the sector

3. Simulate what the burn mechanism would assign vs. actual burn for a set of 1000
   transactions drawn from the within-sector distribution:
   - Assigned burn: V × E_mean × α
   - Actual burn: V × E_actual × α
   - Compute mean absolute error, max overestimation, max underestimation

4. Produce a violin plot showing within-sector intensity distributions with the
   sector-level mean marked as a horizontal line.

5. Write a short paragraph (150–200 words) on what this implies for the practical
   equivalence of a transaction-level burn mechanism vs. a sector-level tax,
   given current data availability.

Save the violin plot to sector_intensity_variation.png.
```

---

## Prompt 5 — Political economy stress test: governance of the calibration parameter

```
The Valdsalu-Aaslaid mechanism includes a calibration parameter α that aligns aggregate
burn with ecological regeneration. The paper acknowledges that "the choice of adjustment
rule is a central governance question." This prompt tests how sensitive the mechanism's
ecological effectiveness is to political interference with α.

Tasks:
1. Implement the base mechanism from Prompt 1 (B_i = V_i × E_i × α).

2. Run four governance scenarios over 200 periods with regeneration I_t ~ N(100, 10)
   and 300 transactions per period:

   Scenario A — Ideal governance:
     α adjusted every 10 periods to keep E[B_t] = E[I_t] exactly.

   Scenario B — Delayed adjustment (simulating legislative lag):
     α adjusted every 30 periods, with a 20-period observation window before adjustment.

   Scenario C — Downward pressure (simulating industry lobbying):
     Every 20 periods, α is reduced by 0.1 regardless of ecological deficit, then
     partially corrected upward only if cumulative deficit exceeds 500 units.

   Scenario D — Abandonment (simulating political reversal):
     At period 80, α is set to 0 and held there for 40 periods, then reinstated
     at its period-79 value.

3. For each scenario, track:
   - Stock S_t over time
   - Cumulative ecological deficit
   - Number of periods where consumption exceeded regeneration by > 20%

4. Produce a four-panel plot (one per scenario) of stock S_t and cumulative deficit.
   Add a horizontal reference at S = 0 (ecological bankruptcy).

5. Write a paragraph (150–200 words) evaluating whether transaction-level embedding
   meaningfully reduces exposure to political economy risks compared to ex post instruments,
   given that α calibration itself requires governance decisions.

Save the plot to governance_stress_test.png.
```

---

## How to use these prompts

1. Open Claude Code in your terminal: `claude` (requires Claude Code installation).
2. Paste one prompt at a time. Each prompt is self-contained.
3. Claude Code will write, run, and iterate on the code until the outputs are produced.
4. Review the generated charts and summary files. Add your interpretation to
   `critical-overview.md` in this research folder.
5. Commit the outputs (charts, CSVs, summary markdown) to this folder on GitHub.

## Expected outputs

| Prompt | Primary output file(s) |
|--------|------------------------|
| 1 | `ecological_mechanism_simulation.png` |
| 2 | `ets_price_vs_emissions.png`, `ets_data.csv` |
| 3 | `instrument_comparison.png`, `instrument_summary.md` |
| 4 | `sector_intensity_variation.png` |
| 5 | `governance_stress_test.png` |

## Notes on interpretation

These simulations are designed to surface the structural strengths and weaknesses of
transaction-level ecological accounting relative to ex post instruments. They should not
be read as proofs. The mechanism is, as the paper itself states, exploratory and not
implementation-ready. The goal is to define what would need to be true for the claim in
the originating statement to be well-supported, and to identify where the evidence is
currently thinnest.
