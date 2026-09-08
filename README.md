# Policy not politics

An Australian economic education pack and static dashboard centred on productivity. Research snapshot: 8 September 2026.

## What is included

- A seven-view static website with official Australian time series, selected OECD comparisons, NDIS spending and integrity evidence, and two interactive teaching calculators.
- 24 timestamped, paraphrased economic claims from the supplied Diary of a CEO transcript.
- 79 source-linked observations and historical projections, a 38-country source directory and a source register.
- Transparent equations, a career-history codebook, contribution templates and a GitHub Pages workflow.

## Coverage is incomplete

This is a research edition, not a completed OECD database or a costed party forecast. Only eight countries have selected comparable productivity levels; four have both 1995 and 2024 endpoints. The full House and Senate career census is not populated. NDIS workforce displacement, net benefits, and attributable debt have not been estimated. One Nation's headline savings are party claims, not verified model inputs.

The OECD API request returned HTTP 403 from this execution environment. A candidate import adapter is included but has not passed a live API run. Public source repository: https://github.com/benmac3/policies-not-politics . The private research preview is hosted separately.

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

To activate public website hosting, open Settings → Pages and choose GitHub Actions as the source, then run the **Build and publish static pack** workflow. The expected Pages address is https://benmac3.github.io/policies-not-politics/ once a deployment succeeds. The workflow validates the data and calculators before publishing.

The separately hosted private research preview is https://policy-not-politics.benmac853144.chatgpt.site . This public export excludes its hosting identity and credentials.

## Scrutiny

See [CONTRIBUTING.md](CONTRIBUTING.md), [research method](docs/research-method.md), [indicator map](docs/indicator-map.md), and [career codebook](docs/career-codebook.md). Correct a result with a primary source and reproducible explanation. Apply the same evidential standard to all parties. No composite political score or causal claim based solely on career background is used.

## Rights

Original project code: MIT licence. Original explanatory prose: CC BY 4.0, attributed to Policy not politics. Upstream data and documents retain their source terms; links are not relicensing. The supplied transcript is represented by paraphrased claims and a checksum, not redistributed in full. The original recording date and publisher URL remain unverified.
