# Federal tax-policy timeline status

Review date: 2026-10-15
Branch: `work/federal-tax-policy-timeline`
Base main: `dc097ed4bcc865aa4ea00552ee8ef99b911df4ec`
Implementation commit before checkpoint: `0f26ff68bd10e9622f44f4491df36a16090ff04d`
Status: standalone review ready; not an exhaustive tax-law census or production release.

## Delivered

- Canonical data: `data/federal-tax-policy-timeline.psv`.
- Deterministic compiler and checks: `scripts/build_tax_policy_timeline.py`.
- Offline interactive template: `reviews/federal-tax-policy-timeline.template.html`.
- Browser checks: `scripts/test_tax_policy_timeline_ui.py`.
- Methodology, provenance, reproduction and limitations: `docs/federal-tax-policy-timeline.md`.
- Conversation package: generated HTML, JSON, three CSVs, screenshots and validation reports.

101 dated records: income 37; capital gains 11; negative gearing/rental deductions 8; GST/sales taxes 7; excise 23; trusts 15. There are 54 source records and nine selected basic resident rate schedules. Seven records are context, including the six 1960 starting positions. Four enacted-future records and one proposed-future record extend the view to 2028. Counts are milestones, not distinct tax increases.

## Verified checks

`python scripts/build_tax_policy_timeline.py` — PASS: structure, IDs, references, category coverage, partial dates, status coding, rate-band continuity and regressions.

`node --check` on the generated inline application JavaScript — PASS.

`python scripts/test_tax_policy_timeline_ui.py` — PASS: 38 checks, desktop 1440x1250 and mobile 390x844; zero JavaScript page errors and zero external requests. Filters, date ranges, related-event links, keyboard markers, exports and rate tables tested. Desktop and mobile screenshots inspected during development.

Git blob hashes of the remote data, compiler, template, test script and methodology match the locally tested files. Source SHA-256: `a715c5f3300874b0c85c04bff8bcf32cb40c3cf035e95e1b73bcbde118b2dc70`.

No released `dist` asset changed. Shared-site build/validation not run for this independent addon. No merge to main or deployment.

## Review priorities and boundaries

Early coverage, particularly 1960–82, remains sparse. Annual personal-rate/rebate history, historical sales-tax schedules, every trust amendment, GST ruling and routine excise indexation notice are not complete. Additional intra-April 2026 fuel adjustments are not fully reconstructed. Some ATO sources were available only in indexed excerpts; access limitations are recorded. There is no complete raw-source archive or independent legal audit.

Keep the June 2026 enacted core framework separate from the No.3 Bill introduced on 14 October, whose enactment was not verified at review. Do not present its proposed July 2028 trust minimum as current law. Preserve partial-date precision, legal status and the distinction between deductions, offsets and withholding.

Review the standalone visualization and documented gaps before any shared-site integration. Do not merge or deploy automatically.
