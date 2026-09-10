# Data release — 10 September 2026

This release populates all seven views with source-linked content and expands the comparison tools. It does not establish a causal ranking of political parties or complete every indicator family in the original research brief.

## Acquired data

- World Bank World Development Indicators: 18,016 non-null observations, 20 indicators, all 38 OECD countries, requested years 2000–2025. Sixteen series have some data for every country; tax revenue, interest/revenue and Gini cover 37 countries, and central-government debt covers 15. Consult metrics.json for exact coverage (including any subsequent corrections to this prose).
- Australian Treasury: 120 net-debt and net-interest observations/estimates from 2000–01 to 2029–30, plus Budget macroeconomic and NDIS program forecasts. Tables 1.1, 1.2, 6.9.2 and 11.4 retain their Budget vintage.
- NDIA: June 2026 participant, accrual expenditure, administration and outcome data; July 2026 monthly statistics. Cash payment categories and accrual costs are separate.
- Australian Parliament: 226 current parliamentarians and 910 official occupation records, plus official occupation-category and prior-government-service tables.
- ABS: historical mean and median real equivalised disposable household income, 11 survey cycles from 2000–01 through 2019–20; June 2026 wage growth.
- Earlier transcript claim extracts, Australian national accounts, Federal Reserve survey observations and selected OECD hourly-productivity observations remain available.

## Definitions and limits

The WDI panel is an intergovernmental compilation, not direct national-office retrieval for each row. Metadata identifies original organisations; some labour series are modelled ILO estimates. Original national offices are linked separately. Statistical estimates are not policy forecasts. An API publication date is not the observation's reference period.

PPP measures compare purchasing power, while constant-price measures compare volumes through time. Output per employed person includes working-time effects and must not be labelled output per hour. The existing constant-2020-PPP hourly extract is not spliced into WDI's constant-2021-PPP per-worker series.

Government finance coverage differs by source reporting: central government and general government, cash and accrual, gross and net debt are distinct concepts. WDI tax revenue excludes most social contributions. Gini income/consumption concepts and survey methods require country-level checking. These measures support exploration, not an automatic ranking of policy quality.

Missing data is not zero. Country tables compare only the chosen year; latest available years are shown separately. Charts break across missing annual observations. No interpolation or backfilling occurs.

Parliament's ongoing service records use the retrieval date, with some new records using an empty end date. The importer selects 48th Parliament records with ongoing service and reconciles its roster count with the official prior-service aggregate. The roster can change; this is a dated snapshot. The current chamber uses the current electorate field (Member where populated, Senator otherwise), reconciled with the first chamber in the API list: 150 Members and 76 Senators. Full chamber history is retained separately.

Sector hints are provisional, conservative pattern rules in import_parliament.py. They are not a verified employer-ownership census. An unclassified role does not mean no private/public experience. Official occupation text, source links and hints are all exposed. Complete employment dates, overlapping spells, ownership changes and years/FTE by sector remain unverified.

NDIS employment outcomes compare entry and reassessment survey results; ageing, selection, attrition and other factors prevent attributing the entire difference to the scheme. Care delivered and carer/participant work enabled must be included in any displacement analysis. Provider counts are not worker counts. Scheme expenditure is not automatically additional Commonwealth debt. Court orders and asset seizures are not a prevalence estimate of fraud.

The Budget NDIS program expense measure includes Commonwealth and state contributions and departmental program costs. It differs from participant-only supports and is not appended to their actual series. Earlier AFSR forecasts remain identified as superseded forecasts.

## Reproduce and inspect

Run `python scripts/import_worldbank.py` and `python scripts/import_parliament.py` to request new official snapshots. These are explicit refreshes, not part of every deployment. They fail on incomplete responses rather than silently completing a partial import. Raw API responses (in data/raw-snapshots.zip, containing losslessly gzip-compressed files; hashes refer to decompressed bytes), series identifiers, URLs and SHA-256 hashes are retained. Inspect changes before publication.

Download the linked Budget PDF and run `python scripts/import_budget.py path/to/bp1_2026-27.pdf` (requires Poppler pdftotext). The deterministic extractor checks the expected count for Table 11.4. Other Australian extensions are identified table extracts in extensions.json; values and definitions should be independently checked when revising them.

Run build.py, validate.py and check-models.cjs to regenerate CSVs, charts and the downloadable source archive. Raw responses are bundled in data/raw-snapshots.zip and included in the downloadable source package.

## Remaining research

Full OECD hourly productivity and multifactor productivity; harmonised real household income, housing affordability, liquid buffers, poverty and wealth shares; effective tax burdens; public-funding employment exposure; business formation and AI adoption; detailed university/graduate outcomes and energy prices; causal NDIS labour/debt estimates; independently costed One Nation alternatives; and verified career durations by employer sector. The site labels the available evidence and does not manufacture these missing results.
