# Australian federal tax-policy timeline — review edition

Review date: **15 October 2026**. Branch: `work/federal-tax-policy-timeline`.
Scope starts in 1960. This is an additive, standalone review of selected major federal changes, not a production release or an exhaustive tax-law census.

## Review and reproduce

Python 3.10 or later, standard library only:

```sh
python scripts/build_tax_policy_timeline.py --check-only
python scripts/build_tax_policy_timeline.py
```

Open `reviews/generated/federal-tax-policy-timeline.html`. It embeds all data and works without a server, internet connection, external scripts or fonts. Do not open the template directly. The build also exports the complete JSON, `tax-events.csv`, `tax-sources.csv`, `income-tax-bands.csv` and a validation report.

Optional browser tests require Playwright and Chromium:

```sh
python scripts/test_tax_policy_timeline_ui.py
```

Set `CHROMIUM_EXECUTABLE` when necessary. Tests otherwise try system Chromium. Generated review outputs and screenshots are supplied in the conversation package; the repository stores reproducible source, template, compiler, tests and documentation. No existing `dist` asset or shared deployment pipeline is modified.

## Coverage

101 dated records, classified once by primary category:

| Category | Records |
|---|---:|
| Income tax, offsets, levies and adjacent remuneration/investment measures | 37 |
| Capital gains tax | 11 |
| Negative gearing and rental deductions | 8 |
| GST and sales taxes | 7 |
| Fuel, alcohol and tobacco excise | 23 |
| Trust taxation | 15 |

These are **events, not 101 distinct policy changes or tax increases**. Six 1960 starting positions and a 1994 rate-threshold benchmark are context. A reform may have separate announcement, legislative and application milestones. Cross-cutting records have related categories; category-filter results may therefore exceed the primary-category counts.

There are 54 source records and nine selected basic resident income-tax schedules: 2009–10, 2010–11, 2012–13, 2016–17, 2018–19, 2020–21, 2024–25, 2026–27 and legislated 2027–28. They are not a verified continuous annual series.

## Provenance and source limitations

`data/federal-tax-policy-timeline.psv` is the canonical UTF-8 transcription. Its named sections contain sources, events and selected rate schedules. Every event resolves to source IDs. Source records retain title, publisher, source type, access basis, URL, locator and a build-supplied review/retrieval date.

The compiler records a SHA-256 of the exact source bytes. The source is a synthesis of legislation, official histories, Budget explanations, ATO guidance, court records and original historical research. An official explanation is not the operative statutory text. Some ATO sources were accessible only through search-indexed extracts, not full direct retrieval; these limitations are visible in both data and interface. No authentication or access restriction was bypassed. Original remote page/PDF bytes are not archived in this package.

## Dates and legal status

A record's `date` is the milestone named by its `stage`. Separate fields retain announcement, Royal Assent, effective/application and end/transition dates when verified. Blanks mean unknown or inapplicable, never zero. Retrospective application can precede assent. A parliamentary-passage milestone must not be relabelled Royal Assent.

22 records have year precision, three month precision and 76 day precision. For chart placement alone, year-only records use 1 July and month-only records the 15th. The underlying partial date and precision are retained; no exact historical day is inferred.

Status is assessed at 15 October 2026. `historical_law` means a historical law event, not necessarily a provision still operating. `enacted` means enactment/implementation verified at review. `enacted_future` identifies four future application records. `proposed` identifies three proposal milestones whose enactment has not been verified; one is the proposed July 2028 commencement. Judgment/guidance records are not newly enacted statutes.

The June 2026 Tax Reform No.1 Act and its later application dates are kept separate from the No.3 Bill introduced on 14 October. Do not silently incorporate pending trust/technical provisions into the June Act. The 2027 and 2028 markers describe known scheduled/conditional dates, not later observed events.

## Rates, deductions, offsets and withholding

Rate schedules contain nominal AUD lower bounds, marginal percentages and project-calculated basic tax at each boundary. The formula sums each completed band times its rate. This is not a personal tax calculator: residency tests, deductions, LITO/LMITO and other offsets, Medicare and temporary levies are excluded. There is no inflation adjustment or inference for missing years.

A deduction reduces taxable income; an offset reduces assessed tax. A CGT discount reduces the taxable gain, not the marginal tax rate. Foreign-resident property withholding is a collection mechanism, not final CGT. Wine Equalisation Tax is value-based and distinguished from volume-based alcohol excise. GST-free and input-taxed supplies are not interchangeable.

## Remaining review gaps

Early coverage, especially 1960–82, is sparse. The full annual personal-rate/rebate history, wholesale-sales-tax schedules, all trust-loss/election amendments, every GST base ruling and every excise tariff/indexation notice are not yet transcribed. Early trust enactment years are distinguished from incompletely reconstructed retrospective application boundaries.

Additional intra-April 2026 fuel-relief adjustments are not fully reconstructed: the initial announcement, broad commencement, July reduction and August end are recorded without asserting an unchanging absolute April–June rate. Refer to official tariff notices for transaction calculations.

This is not a full company, superannuation, payroll, state land/stamp, carbon or resource-tax timeline. FBT and dividend imputation are included as adjacent income-tax reforms. The review does not attribute causal effects, score policy quality or rank governments.

## Validation and release boundary

The compiler checks structure, unique IDs, references, categories, partial dates, future/proposal coding, selected rate-band continuity and historical/current regression cases. Browser smoke tests cover rendering, filters, searches, related-event links, keyboard selection, sources, exports, rate tables and desktop/mobile overflow. These software checks do not establish historical completeness or an independent legal audit.

The separate source hash and test reports are included in the review package. Shared-site build/validation and deployment have not been run for this isolated addon. Integration should review the data and outstanding gaps before exposing the new view on the released site. Do not merge or deploy automatically.
