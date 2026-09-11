# Parliament career research data

Parallel Parliament research is stored one member at a time under `data/careers/members/<person_id>.json` using `docs/career-record-format.md`.

The batch assignment is defined in `data/career-batch-plan.json` and resolved against the frozen `data/parliament.json` roster by `scripts/career_batches.py`.

Rules for batch Work conversations:

- write only assigned member files plus the batch's own status file;
- do not edit `data/parliament.json`, `dist/app.js`, shared source registers, or another batch's member files;
- commit each completed or explicitly blocked member before moving to the next member;
- keep sources inside the member record so branch merges are additive and low-conflict;
- use `python scripts/career_batches.py --check` to verify that the batch plan covers the frozen roster exactly once.

`work/parliament-experience` is the Parliament aggregation/UI branch. After batch branches are completed, that branch merges the per-member records, builds aggregate outputs, updates methodology/UI as required, and then hands the result to the site-wide integration branch.
