# Federal election timeline status

Last updated: 2026-10-06
Branch: `work/federal-election-timeline`
Base main: `8f7179c6accfe62d4c547bb8cfed1129e3dcf796`
Implementation commit before this checkpoint: `f6aacfc9512941e52ddc090db3638572d2091125`
Status: review edition ready for user inspection; not a production-ready historical audit.

## Delivered

- Canonical source data: `data/federal-election-timeline.psv`.
- Compiler and validators: `scripts/build_election_timeline.py`.
- Offline interactive review template: `reviews/federal-election-timeline.template.html`.
- Optional browser checks: `scripts/test_election_timeline_ui.py`.
- Definitions, provenance, reproduction and unresolved cases: `docs/federal-election-timeline.md`.
- Conversation review package: built standalone HTML, JSON, two CSVs, screenshots and test reports.

Coverage: 285 records, comprising 48 general elections, 165 House by-elections, 4 Senate-only elections, 1 Senate supplementary poll, 1 Senate rerun, 3 supplementary House polls, 38 PM events and 25 DPM events. Appointments: 37 PM, 22 DPM. The 1963/1966/1969/1972 Senate vacancy polls are within general-election records, not duplicate national elections.

## Checks performed

`python scripts/build_election_timeline.py` — PASS: schema, IDs, references, chamber totals, transfer arithmetic, coverage and regression cases. Source SHA-256: `4cb59025a423e4498a8b8204efac164d7f76abf99d3ad8b87772a3994cd2262e`.

`python scripts/test_election_timeline_ui.py` — PASS: 15 assertions, desktop 1440px and mobile 390px, no JavaScript page errors. Screenshots inspected. Export, filters, event selection and annulment warnings tested.

Remote Git blob SHAs matched local bytes for the data, compiler and visualization template. No production files changed, no merge to main, no deployment. Shared application build/validation were not run: this additive review has its own independent compiler and tests.

## Remaining work before release

Resolve the 14 historical House results with source-grouped Other seats and 3 flagged by-election affiliation discrepancies; audit special full-Senate reconstructions and secondary chronology; fill the unverified 1908/1972 full-Senate snapshots where defensible. Do not silently convert missing data to zero or advertise a continuous live balance-of-power ledger. Review the standalone visualization, then integrate through the project's release workstream.
