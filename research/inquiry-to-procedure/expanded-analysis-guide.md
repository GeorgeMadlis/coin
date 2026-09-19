# Expanded analysis guide

The public ConnectedNature article is a synthesis, not the whole research trail. Expanded analysis
requires a reader to separate:

1. the originating research question and the status of each claim;
2. the two formal bundle cases committed in COIN;
3. the supporting MHS recorded inquiry;
4. the counterfactual tests that have not yet been run;
5. EUDR regulation, scientific publications, dataset documentation, and their uncertainties;
6. private-framework observations that are summarized publicly but whose underlying private
   repository state must not be misrepresented as public primary evidence.

The central discipline is source role. A public article can summarize an interpretation, a bundle
can document a public research state, a dataset page can document source semantics, and private
repository history can motivate a caution. These are not interchangeable evidence classes.

## Recommended reading order

1. [critical-overview.md](critical-overview.md) - Start here for the sceptical synthesis. It answers:
   what does the article's case actually support, and where does it overstate?
2. [claims.md](claims.md) - Read the claim ledger next. It answers: which claims are sourced,
   inferential, flagged, or unresolved?
3. [bundle-evolution-analysis.md](bundle-evolution-analysis.md) - Then read the two formal bundle
   analysis. It answers: what observable transitions in the committed formal cases became code,
   tests, specifications, instructions, evidence semantics, or retained uncertainty?
4. [bundles/framework-self/](bundles/framework-self/) - Inspect the general formal bundle. It
   answers: how did the observer-disagreement / statement-evolution framework describe and revise
   itself over twenty rounds?
5. [bundles/eudr-coffee-brazil-fazenda-sucuri/](bundles/eudr-coffee-brazil-fazenda-sucuri/) - Inspect
   the applied formal bundle. It answers: how did the Fazenda Sucuri EUDR coffee screening case
   preserve source-specific evidence, repairs, and a human-review boundary?
6. [recorded-inquiries/mhs-world-models/](recorded-inquiries/mhs-world-models/) - Read the supporting
   recorded inquiry. It answers: how can a focused fact-checking question emerge after earlier
   conceptual enrichment, without becoming a third formal bundle case?
7. The Estonian forest-management section of *Evidence First, Consensus Later* - Read it as a
   public conflict-analysis example, not as a COIN bundle trajectory. It answers: how can endpoint
   sustainability claims diverge because accounting objects, boundaries, indicators, time horizons,
   definitions, and normative criteria differ?
8. [recorded-inquiries/mhs-world-models/MHS-QA-source.md](recorded-inquiries/mhs-world-models/MHS-QA-source.md)
   - Read the saved Q/A source when the MHS sequence itself matters. It answers: what source-backed
   exchange is preserved, and which citation placeholders are merely part of that exchange?
9. [recorded-inquiries/mhs-world-models/analysis.md](recorded-inquiries/mhs-world-models/analysis.md)
   - Read the retrospective analysis after the source. It answers: what interpretation is drawn from
   the saved sequence, and what is not inferred?
10. [counterfactual-tests.md](counterfactual-tests.md) - Finish with the proposed tests. It answers:
   what evidence would be needed to establish incremental trajectory value beyond a rich current-state
   handoff?

For the EUDR example, also read the Fazenda Sucuri bundle's local
[bundle reading guide](bundles/eudr-coffee-brazil-fazenda-sucuri/EUDR_COFFEE_BRAZIL_FAZENDA_SUCURI_BUNDLE_READING_GUIDE.md),
then descend into [answer.md](bundles/eudr-coffee-brazil-fazenda-sucuri/answer.md),
[s/modeling.md](bundles/eudr-coffee-brazil-fazenda-sucuri/s/modeling.md),
[s/data-sources.md](bundles/eudr-coffee-brazil-fazenda-sucuri/s/data-sources.md),
[r/results.md](bundles/eudr-coffee-brazil-fazenda-sucuri/r/results.md), and
[reproduction/data.md](bundles/eudr-coffee-brazil-fazenda-sucuri/reproduction/data.md).
Read [round 10](bundles/eudr-coffee-brazil-fazenda-sucuri/inquiry/round-0010.md) before using round
8's motivation in a causal narrative: it verifies the Sucuri execution but classifies the
observation origin as underdetermined.

## What each evidence class can answer

| Evidence class | Read | Question it can answer | Status boundary |
|---|---|---|---|
| Originating question and claim status | [claims.md](claims.md), [critical-overview.md](critical-overview.md) | What is the proposition, negative, and current evidential status? | Claims remain sourced, inferential, flagged, or unresolved as marked. |
| Formal bundle case A | [bundles/framework-self/](bundles/framework-self/) | What public formal trajectory records framework self-revision? | Source repository is private; the committed COIN bundle is the public evidence. |
| Formal bundle case B | [bundles/eudr-coffee-brazil-fazenda-sucuri/](bundles/eudr-coffee-brazil-fazenda-sucuri/) | What public applied trajectory records EUDR coffee screening repairs? | The public bundle now includes inspection material: the reading guide, derived contact-sheet PDF and metadata, contact-sheet/artifact guide, machine manifest, and copied evidence-package artifacts. The contact sheet is derived convenience material, not canonical evidence. |
| Supporting recorded inquiry | [recorded-inquiries/mhs-world-models/](recorded-inquiries/mhs-world-models/) | How did an MHS/world-model fact-checking question emerge from prior conceptual work? | It is not a formal bundle and should not be counted as a third bundle case. |
| Public conflict analysis | *Evidence First, Consensus Later*, Estonian forest-management section | How can apparently opposed sustainability claims depend on different accounting objects, boundaries, indicators, time horizons, definitions, or normative criteria? | It motivates a possible trajectory-aware conflict bundle; it does not prove one is necessary or already exists. |
| Proposed experiments | [counterfactual-tests.md](counterfactual-tests.md) | What would test `X_state` versus `X_traj`? | Proposed tests are not results. |
| EUDR law and datasets | This guide, the Fazenda Sucuri bundle, and cited external sources | What must be read before stronger EUDR claims? | Screening evidence is not a legal non-compliance determination. |
| Private-framework observations | Public article summaries plus [claims.md](claims.md) and [critical-overview.md](critical-overview.md) | What methodological caution is publicly documented? | Do not present private source-repository state as public primary evidence. |

## EUDR publications, evidence, and uncertainty

Before making stronger claims from the EUDR example, read legal authority first, then implementation
guidance, then the public claim source, then the committed bundle, then dataset and scientific
evidence.

### Legal and implementation sources

- **Regulation (EU) 2023/1115**, consolidated current version exposed through EUR-Lex under CELEX
  `32023R1115`: <https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX%3A32023R1115>. Use this
  for binding definitions, Article 3 market/export conditions, due-diligence information
  requirements, geolocation requirements, commodity scope, and the 31 December 2020 cutoff.
- **European Commission EUDR implementation page**:
  <https://environment.ec.europa.eu/topics/forests/deforestation/regulation-deforestation-free-products_en>.
  As checked on 2026-08-31, the Commission page states current application dates of 30 December 2026
  for large and medium operators, 30 June 2027 for most micro and small operators, and 30 December
  2026 for micro and small operators already covered by the EU Timber Regulation.
- **Commission Notice, Guidance document for Regulation (EU) 2023/1115 on deforestation-free
  products**, C/2026/3896, OJ C, 20 July 2026:
  <https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ%3AC_202603896>. Use this for current
  Commission guidance on implementation, while preserving its own boundary: it informs application
  but does not replace or amend the regulation.
- **FAQ on EUDR Implementation**, Directorate-General for Environment, publication page dated
  21 August 2026, file titled "Implementation of the EU Deforestation Regulation - Frequently Asked
  Questions - April 2026":
  <https://environment.ec.europa.eu/publications/faq-eudr-implementation_en>. Use this for current
  Commission FAQ material, especially where degradation, operator obligations, information-system
  details, or implementation timing have shifted across iterations.

### Public Fazenda Sucuri source and committed bundle

- **ConnectedNature public synthesis**:
  <https://connectednature.org/posts/inquiry-to-procedure>. It is a narrative synthesis and should
  not be used as primary evidence for the bundle's own state.
- **Coffee Watch / AidEnvironment case profile linked by the article**:
  <https://coffeewatch.org/documents/33/JDE_Peets_Company_Profile.pdf>. The article characterizes it
  as describing native-vegetation clearing at Fazenda Sucuri between August and December 2024 and
  reporting that part of the affected area fell within an FAO forest definition. Treat this as a
  public claim/source used for screening context, not as a legal finding, not as production-geometry
  proof, and not as validation of the COIN bundle's raster outputs.
- **Committed Fazenda Sucuri bundle**:
  [bundles/eudr-coffee-brazil-fazenda-sucuri/](bundles/eudr-coffee-brazil-fazenda-sucuri/). Its
  current bundle verdict is `possible_relevant_deforestation` with provenance
  `pinned-not-reproduced`; the counterpart report requires human review. It records a screening flag,
  not legal non-compliance. The source-specific conversion signal is FDP 1.17 ha while MapBiomas and
  both-source agreement are 0.0 ha for the same new-coffee/post-2020-loss overlap.

### Dataset and scientific sources to read

- **JRC Global Forest Cover 2020 V3**, Earth Engine asset `JRC/GFC2020/V3`:
  <https://developers.google.com/earth-engine/datasets/catalog/JRC_GFC2020_V3>. Use this for GFC2020
  V3 source semantics: 10 m 2020 forest/non-forest baseline, EUDR-aligned intended use, exclusion of
  agricultural plantations including coffee, and the explicit non-mandatory, non-exclusive,
  non-legally-binding boundary.
- **Bourgoin, Clement; Verhegghen, Astrid; Ameztoy, Iban; Carboni, Silvia; Achard, Frederic;
  Colditz, Rene (2026), "Global map of forest cover 2020 - version 3"**, European Commission, Joint
  Research Centre dataset, DOI <https://doi.org/10.2905/JRC.354CG88>, PID
  <http://data.europa.eu/89h/8c561543-31df-4e1b-9994-e529afecaf54>. This is the dataset citation
  listed by the JRC Data Catalogue and Earth Engine catalog.
- **Bourgoin, C., Verhegghen, A., Ameztoy, I., Beuchle, R., Carboni, S. et al. (2026), "Maps of
  Global Forest Cover 2020 Version 3 and Global Forest Type 2020 Version 1 Supporting the EU
  Deforestation Regulation - Methodology, Accuracy Assessment and Comparison"**, Publications Office
  of the European Union, JRC146622, DOI <https://data.europa.eu/doi/10.2760/9982436>. Use this for
  GFC2020 V3 methodology and accuracy, where available.
- **Colditz, Rene et al. (2025), "Accuracy Assessment of the Global Forest Cover Map for the Year
  2020: Assessment Protocol and Analysis"**, Publications Office of the European Union, JRC141231,
  DOI <https://data.europa.eu/doi/10.2760/7632707>. The JRC record reports 21,752 interpreted sample
  units, 91% overall accuracy, 18% forest commission error, 8% forest omission error, and lower
  accuracy clusters in open dry forests including eastern Brazil. Do not convert these global
  validation results into AOI-specific accuracy.
- **Hansen Global Forest Change v1.13 (2000-2025)**, Earth Engine asset
  `UMD/hansen/global_forest_change_2025_v1_13`:
  <https://developers.google.com/earth-engine/datasets/catalog/UMD_hansen_global_forest_change_2025_v1_13>.
  The catalog cites Hansen, M. C. et al. (2013), "High-Resolution Global Maps of 21st-Century Forest
  Cover Change," *Science* 342, 850-853, DOI <https://doi.org/10.1126/science.1244693>. Also read
  the v1.13 user notes: <https://storage.googleapis.com/earthenginepartners-hansen/GFC-2025-v1.13/download.html>.
  Use Hansen as stand-replacement/tree-cover-loss evidence, not as commodity-causation evidence.
- **Forest Data Partnership coffee model 2026a**, Earth Engine asset
  `projects/forestdatapartnership/assets/coffee/model_2026a`:
  this is the asset/version pinned by the current Sucuri evidence package. The older public
  `model_2025b` catalog material can supply general product-family context, but it is not a
  version-specific source for 2026a.
- **Forest Data Partnership model documentation.** The current pinned Sucuri evidence identifies
  `model_2026a`; retain the provider asset/version and local checksums from the bundle. The earlier
  `model_2025b` README remains background for shared probability-model caveats only and must not be
  presented as the current asset's version-specific documentation.
- **MapBiomas Land Use and Land Cover - Brazil V1.0**, Earth Engine asset
  `projects/mapbiomas-public/assets/brazil/lulc/v1`:
  <https://developers.google.com/earth-engine/datasets/catalog/projects_mapbiomas-public_assets_brazil_lulc_v1>.
  Use this for MapBiomas Collection 10/v1 semantics: annual 30 m discrete classification, not
  probability; coffee is class 46. The catalog cites Souza et al. (2020), "Reconstructing Three
  Decades of Land Use and Land Cover Changes in Brazilian Biomes with Landsat Archive and Earth
  Engine," *Remote Sensing* 12(17), DOI <https://doi.org/10.3390/rs12172735>.
- **Berger, Katja; Herold, Martin; Szantoi, Zoltan (2025), "Earth observation as enabler for
  implementing the EU regulation on deforestation-free products"**, *npj Climate Action* 4, article
  68: <https://www.nature.com/articles/s44168-025-00276-9>. Use this as general EO/EUDR context,
  including the need for independent, verifiable, long-term EO evidence and the limits of EO alone
  for traceability and small-scale/agroforestry cases.
- **van Noordwijk, Meine; Dewi, Sonya; Minang, Peter A.; Harrison, Rhett D.; Leimona, Beria;
  Ekadinata, Andre; Burgers, Paul; Slingerland, Maja; Sassen, Marieke; Watson, Cathy; Sayer, Jeffrey
  (2025), "Beyond imperfect maps: Evidence for EUDR-compliant agroforestry"**, *People and Nature*
  7(7), 1713-1723, DOI <https://doi.org/10.1002/pan3.70088>. Use this for agroforestry and
  forest/non-forest ontology limitations, especially the distinction between observable tree cover
  and land-use/legal evidence.

Other names suggested during prompt construction, including Lambiel, Kussul, and Anisimov, should not
be added unless a future source record identifies the exact publication and its role in this inquiry.
No such exact work was found in the inspected COIN and related local source records during this run.

### Uncertainty classes to keep explicit

- **Omission and commission error in remote-sensing products.** JRC GFC2020 validation reports global
  omission and commission errors; Hansen, FDP, and MapBiomas each have separate product-specific
  error modes.
- **Forest-definition uncertainty.** EUDR forest status depends on canopy, height, area, and
  predominant land use. A mapped forest pixel is evidence, not a definitive legal forest-status
  finding.
- **Agroforestry / tree-crop ontology uncertainty.** Coffee agroforestry can contain tree cover while
  still being agricultural land use; forest/non-forest maps can misrepresent that distinction.
- **Commodity-attribution uncertainty.** Coffee evidence from FDP probability and MapBiomas discrete
  class semantics is not proof that coffee caused a mapped disturbance.
- **Production-geometry and production-linkage uncertainty.** EUDR due diligence requires production
  geolocation. A loss/coffee overlap inside a screening polygon does not itself prove shipment,
  plot, establishment, or legal-production linkage.
- **Spatial-resolution and spatial-support mismatch.** JRC and FDP are 10 m products; Hansen and
  MapBiomas are coarser/different supports in the inspected method. Intersections inherit alignment,
  resampling, mixed-pixel, and boundary effects.
- **Temporal mismatch.** Baseline forest date, loss year, coffee observation year, public clearing
  claim dates, and supply-chain production dates need not align.
- **Probability-threshold sensitivity.** FDP is a probability product. Area and overlap can change
  with the operating threshold; the chosen threshold is a procedural state, not ground truth.
- **Disagreement between FDP and MapBiomas.** In the Fazenda Sucuri bundle, FDP reports 1.17 ha of
  new-coffee/post-2020-loss overlap while MapBiomas and both-source agreement report 0.0 ha.
  Preserve that disagreement rather than averaging it away.
- **Task-formation provenance uncertainty.** The Sucuri diagnostic execution is verified, but the
  task-forming visual observation's geographic origin is underdetermined. The identical earlier
  Ibiá / Patrocínio rectangle supplies compatible imagery, not proof of transfer. Keep observation
  origin, diagnostic transfer, target execution, and ledger attribution separate.
- **Component accuracies cannot simply be multiplied.** A three-layer intersection does not become an
  AOI-specific decision accuracy by multiplying published component accuracies without assumptions
  about independence, common definitions, common spatial support, common reference periods, local
  representativeness, and fixed thresholds.
- **Source-authenticity uncertainty.** A pinned artifact can be reproducible while still failing to be
  authentic provider-derived source evidence.
- **Screening result versus legal EUDR determination.** The Fazenda Sucuri bundle records a screening
  flag and human-review status. It is not a legal non-compliance determination.
- **Regulatory and implementation-context uncertainty.** Application dates, guidance, FAQ wording,
  information-system rules, benchmarking, operator role, producer-country law, competent-authority
  practice, and traceability requirements can affect a downstream disposition without changing the
  technical raster result.

This literature can strengthen the descriptive premise that the EUDR evidence problem contains
consequential uncertainty and methodological choices. It does not establish the article's stronger
causal hypothesis that access to a recorded human-AI trajectory improves method formation beyond an
equivalently rich current-state handoff.

## Fabricated-input / source-authenticity episode

The public article says that earlier Brazil rasters were pinned and deterministically reproduced, but
later investigation found that the pinned inputs were not authentic provider-derived acquisitions:
hashes reproduced the wrong inputs.

The publicly documented COIN trail currently supports that episode as an interpretation and
methodological warning, not as public primary evidence for every underlying source event.

Publicly inspectable in COIN:

- [claims.md](claims.md) records **C17** as the source-authenticity counterexample:
  reproducibility preserved an invalid evidence state until later inquiry exposed a
  source-authenticity problem.
- [critical-overview.md](critical-overview.md) treats the fabricated-input episode as the standing
  counterexample to wording that lets deterministic reduction imply correctness.
- [counterfactual-tests.md](counterfactual-tests.md) uses source-authenticity failure as a candidate
  trigger for method revision.

Not publicly inspectable in COIN:

- the underlying private source-repository state that established the full raster-authenticity
  episode;
- any full private transcript, uncommitted state, or provider-acquisition audit record not copied
  into the public research folder.

Therefore, references to this episode should say "publicly documented interpretation in COIN" or
"private-framework observation summarized publicly" when discussing the episode's basis. They should
not imply that COIN contains a public primary-source URL proving every underlying raster acquisition
event.

The methodological conclusion is still valid and important: reproducibility of a pinned artifact
does not establish source authenticity. A verification trail must distinguish provider event,
acquired record, pinned artifact, computation, and interpretation.

## Status of the five subsidiary questions

1. **Historical learning already compiled into current artifacts:** partially answered. Observable
   compilation is demonstrated, but how much useful history is captured is not measured.
2. **Incremental value of explicit trajectory access:** unanswered. No controlled `X_state` versus
   `X_traj` comparison has been run.
3. **When history can leave routine active context:** provisional methodological answer. The article
   proposes a reduction rule, but no universal promotion/removal threshold is validated.
4. **When archived trajectory should be reopened:** conceptually/provisionally answered.
   Contradiction, source failure, frame/framework change, regulation change, transfer failure, and
   similar triggers are candidates, but the incremental benefit of reopening history has not been
   experimentally demonstrated.
5. **Compensation for different human-AI backgrounds versus anchoring/noise:** unanswered.
   Cross-observer generality and harmful trajectory effects remain untested.

## Final guardrails

- Keep the MHS recorded inquiry below formal-bundle level.
- Keep the two committed formal bundles as the two primary bundle cases.
- Keep the Estonian forest-management example below formal-bundle level until a versioned
  trajectory-aware conflict bundle actually exists.
- Treat the Estonian case as motivation for testing whether a recorded trajectory of disagreement
  improves diagnosis or contestation beyond a rich current-state dossier, not as evidence that such
  necessity has been demonstrated.
- Keep EUDR evidence at screening level unless independent legal and evidentiary authority supports
  a stronger status.
- Do not upgrade `pinned-not-reproduced` to reproduced.
- Mark sourced, inferential, unresolved, and private-source observations separately.
