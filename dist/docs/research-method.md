# Research method

Version 0.1 — 8 September 2026

The pack explains how policy may change productive capacity, household living standards and fiscal resilience. It tests the supplied interview's economic propositions rather than adopting its conclusions. The transcript contains automated transcription errors; its timestamps are used as supplied. Twenty-four representative economic claims have been paraphrased. Advertising, personal investment prescriptions, medical speculation and election predictions are outside the economic indicator extraction.

## Evidence classes

1. **Official observation:** a published statistic, with source, unit, reference period and vintage. Statistics remain estimates and can be revised.
2. **Official forecast:** a conditional projection with its policy and economic assumptions.
3. **Party proposal or claimed costing:** evidence of what the party proposes; not proof of effects or deliverability.
4. **Project calculation:** a formula applied to specified inputs, reproducible from code.
5. **Causal hypothesis:** a mechanism requiring evidence against alternative explanations.
6. **Unknown:** missing or unverified; never entered as zero.

Government statistics can have measurement limitations and institutional incentives. Source quality depends on transparent definitions, independent scrutiny and reproducibility, not simply a government logo.

## Productivity and living standards

The accounting identity is real output per person = real output per hour × hours worked per person, provided definitions and populations match. Labour productivity is not an individual worker-effort rating. It reflects technology, capital, organisation, skills and industry composition. Multifactor productivity is a separate residual-based measure.

A labour-productivity improvement can raise the capacity for higher pay, lower prices, better service or leisure. Distribution depends on competition, bargaining, taxes and institutions. GDP is not a comprehensive measure of wellbeing, quality, environmental costs or unpaid work. Track real disposable income, its distribution and service access alongside it.

Reference sources: OECD productivity compendium; ABS national accounts; OECD household disposable income. URLs are in `data/sources.json`.

## Comparability

- Use the same calendar or financial year, sector scope, hours concept, and price basis within a comparison.
- Retain reference year and PPP vintage; do not mix current-price USD with constant PPP output per hour.
- Indexes track change; an indexed house-price-to-income series is not an absolute price/income multiple.
- Retain seasonal-adjustment and annual/quarterly definitions. A year-to-June rate is not the change in annual averages.
- Mark latest available years explicitly. Do not make a rank from a selected subset.
- Flag multinational income effects, especially Ireland. GDP, national income and household income answer different questions.
- Keep vintage revisions separate. The annual Australia table preserves October 2025 data; the quarterly table uses the June 2026 release.

## NDIS analysis

Scheme participant costs, agency administration, cash payments, accrual expenses and Commonwealth contributions are different quantities. The initial chart uses actual nominal participant costs from NDIA AFSR Table 6.11, not agency administration or Commonwealth-only expenditure. Older projections are visibly labelled and never joined to a newer baseline without reconciliation.

Decompose spending into participants × average support cost, and then eligibility, intensity, prices, utilisation, administration and payment integrity. Use average active participants for annual per-participant costs; end-year enrolment is not equivalent.

Do not extrapolate fraud from risk-targeted audits. Publish intentional fraud, alleged fraud, rule non-compliance, errors, court-ordered returns, actual recoveries and seized assets separately. A cumulative conviction count is not a prevalence rate. Broader integrity leakage cannot be labelled proven fraud.

Employer control, government funding and industry classification are separate dimensions. A private NDIS provider can have publicly funded revenue without being public-sector employment under ABS definitions. An additional exposure estimate could be sum(provider FTE × NDIS-funded revenue share), but only if revenue share is an appropriate labour-use proxy. Multi-service providers, contractors, labour-cost shares and pass-through costs require adjustment. This estimate is not direct government employment.

For workforce effects, estimate participant/carer work enabled minus displacement from other employment, with entrants from unemployment, migration and extra hours shown separately. Prefer linked longitudinal labour and scheme records to a simple before–after industry comparison. Output effects require valuation of care delivered and the alternative activities. Financial costs alone cannot measure social value.

For a fiscal counterfactual, specify the alternative: reduced leakage, different eligibility, different prices, or replacement services. For Commonwealth debt use Commonwealth net expenditure and revenue changes; do not charge state scheme contributions twice. Include implementation costs, other-service substitution, participant/carer tax receipts, interest, and financing assumptions. General equilibrium effects should be separate from first-round accounting.

## Policy comparison

Use a dated 2026–27 Budget/PBO baseline; distinguish enacted, announced, funded and contingent measures. Map each One Nation proposal to an explicit change in a baseline parameter. Record missing thresholds, costings, start dates and administrative requirements. Apply identical macroeconomic assumptions to both paths unless a separately evidenced behavioural channel changes them.

Report at 5, 10, 20 and 30 years: real GDP per person, real median household disposable income, labour productivity, hours/participation, government debt/GDP, net interest/revenue, distributional effects and service outcomes. Use low/central/high sensitivities for productivity, migration, participation, interest, inflation, uptake and implementation; do not claim statistical confidence intervals without an estimation method.

Avoid double-counting an existing Budget saving as a new alternative-policy saving. Gross spending cuts do not equal net fiscal savings. The party's claimed $90bn annual savings have not been independently established in this pack. No electoral recommendation or quantified ranking of the two packages is supported.

## Models included

Teaching productivity index: P(t) = 100 × (1 + g)^t. This isolates compounding; it is not a prediction for wages or GDP.

Illustrative financing: D(0) = 0; D(t) = D(t−1) × (1 + r) + s × f. Here s is an assumed constant annual net nominal saving, f the share used to reduce borrowing, and r a fixed interest rate. End-year savings. It assumes no changes to growth, interest rates or other policy. It is not an NDIS attribution model or a One Nation forecast.

Cross-country endpoint growth: CAGR = (value_2024 / value_1995)^(1/29) − 1. Rounded published inputs imply approximate results.

## Reproducibility and release gates

Every row has a source ID resolved through the source register. The current numeric extracts were manually transcribed from accessible official webpages/PDF tables. The raw supplied transcript has a SHA-256 fingerprint. Full raw government snapshots and independent transcription checks are not yet complete. The importer retains raw file hashes when run.

Before a full public launch, complete the OECD panel, validate representative source rows independently, populate household/fiscal indicators and the full parliamentary roster, reconcile current policy implementation, and review any causal estimates. Publish all gaps and revisions. Public contributors should be able to propose replacement assumptions as well as correct numbers.
