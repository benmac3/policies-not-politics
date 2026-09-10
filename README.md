# Policy not politics

An Australian economic education pack and static dashboard centred on productivity. Research snapshot: 10 September 2026.

## What is included

- Seven populated views: dashboard, productivity education, countries, NDIS, policy scenarios, parliamentary experience, and evidence.
- 18,016 annual WDI observations across 20 indicators and all 38 OECD countries (2000–2025 requested; missingness varies).
- 226 parliamentarians and 910 official occupation records, with source links and provisional sector hints.
- Australian fiscal history, Budget forecasts, NDIS costs/participants/outcomes, household-income history and earlier national-accounts extracts.
- 24 timestamped paraphrased transcript claims, reproducible import/build code, raw API snapshots and public contribution templates.

See [release notes](docs/data-release.md) for definitions, coverage and limitations. All pages contain data, but the original research agenda remains incomplete: full hourly productivity, several household/technology measures, verified career durations, causal NDIS impacts and independently costed policy alternatives are still outstanding. Missing data never becomes zero.

## Refresh official data

```sh
python scripts/import_worldbank.py
python scripts/import_parliament.py
```

These explicitly refresh source snapshots; builds use the committed data. Review definitions and source revisions before publishing. The WDI source layer is intergovernmental, with national offices and original organisations identified separately. Budget Table 11.4 can be reproduced using `python scripts/import_budget.py path/to/bp1_2026-27.pdf` (Poppler required).

## Reproduce locally

Python 3.10+ and Node 18+ are sufficient. No packages are required for the static site.

```sh
python scripts/build.py
python scripts/validate.py
node --check dist/app.js
node scripts/check-models.cjs
python -m http.server 8000 --directory dist
```

Open http://localhost:8000. Hash navigation and relative assets also support GitHub project Pages paths. There is no comment backend or analytics. Download links, filtering and scenario calculations run locally in the browser.

Data JSON is the maintained source. `scripts/build.py` regenerates CSVs, the browser data bundle, downloadable methods, and the source pack. The authored HTML/CSS/JS in `dist` are tracked. After changing authored assets or data, rerun the build and commit all outputs.

## Acquire the OECD panel

```sh
python scripts/import_oecd.py --download --start 2000 --end 2025
```

Alternatively export a CSV from OECD Data Explorer and run:

```sh
python scripts/import_oecd.py --input /path/to/oecd.csv
```

The importer writes a review-stage file and a raw-response checksum manifest; it does not silently replace approved observations. Inspect coverage, units, PPP year, annual frequency, status flags and methodology before merging into `data/observations.json`. Official API structures can change. No successful live import is claimed.

## GitHub publication

Source and contributions: https://github.com/benmac3/policies-not-politics . Use Issues to challenge data or models; issue templates are included.

The public website is https://benmac3.github.io/policies-not-politics/ . Pushes to main run the **Build and publish static pack** workflow. The workflow validates the data and calculators before publishing.


## Scrutiny

See [CONTRIBUTING.md](CONTRIBUTING.md), [research method](docs/research-method.md), [indicator map](docs/indicator-map.md), and [career codebook](docs/career-codebook.md). Correct a result with a primary source and reproducible explanation. Apply the same evidential standard to all parties. No composite political score or causal claim based solely on career background is used.

## Rights

Original project code: MIT licence. Original explanatory prose: CC BY 4.0, attributed to Policy not politics. Upstream data and documents retain their source terms; links are not relicensing. The supplied transcript is represented by paraphrased claims and a checksum, not redistributed in full. The original recording date and publisher URL remain unverified.
