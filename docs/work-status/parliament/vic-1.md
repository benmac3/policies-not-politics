# Parliament vic-1 status

Last updated: 2026-09-14
Branch: work/parliament-vic-1
Branch HEAD: PRE-COMMIT (this checkpoint is committed with the member record; use git log -1)
Main base observed: 8f7179c6accfe62d4c547bb8cfed1129e3dcf796
State: ready-for-integration

## Completed
- 316915 ABDO, Basem: blocked durable record.
- 11788 ALDRED, Mary: blocked durable record.
- 290544 ANANDA-RAJAH, Dr Michelle: blocked durable record.
- 300706 BABET, Ralph: blocked durable record.
- 309484 BELYEA, Jodie Anne: blocked durable record.
- 288713 BIRRELL, Samuel (Sam) James: blocked durable record.
- 263427 BRISKEY, Jo: blocked durable record.
- 278522 BURNS, Joshua (Josh) Solomon: blocked durable record.
- IPZ CHESTER, the Hon. Darren Jeffrey: blocked durable record.
- 249710 CHESTERS, Lisa Marie: blocked durable record.
- 281503 CICCONE, Raffaele (Raff): blocked durable record.
- 263547 COKER, Elizabeth (Libby) Ann: blocked durable record.
- 301128 DARMANIN, Lisa: blocked durable record.
- 299962 DOYLE, Mary: blocked durable record.
- HWG DREYFUS, the Hon. Mark Alfred, KC: blocked durable record.
- 299964 FERNANDO, Cassandra: blocked durable record.
- 295588 GARLAND, Dr Carina Mary Lindsay: blocked durable record.
- 243609 GILES, the Hon. Andrew James: blocked durable record.
- 315154 GREGG, Matt: blocked durable record.
- 282335 HAINES, Dr Helen Mary: blocked durable record.
- ZN4 HENDERSON, the Hon. Sarah Moya: blocked durable record.
- 86256 HILL, the Hon. Julian Christopher: blocked durable record.
- 310860 HODGINS-MAY, Steph: blocked durable record.
- 266499 HUME, the Hon. Edwina Jane (Jane): blocked durable record.
- 316021 JORDAN-BAIRD, Alice: blocked durable record.

## Evidence/data added or changed
- All 25 assigned members processed sequentially and individually committed: 205 career entries and 125 source entries. All 25 records are explicitly blocked; no complete full-time public/private headline totals were established.
- Per-member source-linked career spells, exclusions and explicit evidence gaps. Only assigned member files and this checkpoint changed.

## Validation run
- python scripts/career_batches.py --check — PASS (226 members, 13 batches).
- python scripts/career_batches.py --batch vic-1 — PASS (25 assigned members).
- JSON parse, source-reference/category/interval checks and scripts.build_careers.load_records() — PASS. Aggregation outputs are not written.
- python scripts/validate.py — PASS.

## Remaining
- Ready for integration of sourced partial timelines only. This is not completion of the requested numerical employment-years census.
- No unprocessed assigned members. Explicitly blocked records retain follow-up needs.

## Ambiguities / decisions needed
- Follow-up needs are recorded per member: appointment/cessation dates, substantive full-time hours, leave and overlap reconciliation, and historical employer control. Broad career-length statements and senior titles were not substituted for FTE evidence.
- Integration should review historical sector cases including TAB privatisation, pre-SBS NITV, AustralianSuper versus nonprofit trustee structures, and French public control of Transdev.
- Blocked means a sourced partial timeline is durable, but dates, employer control or full-time evidence remain insufficient for the requested headlines. It does not mean zero experience.
- Final evidence audit preserved unknown remuneration/control for Haines advisory and company-director roles, and unknown control across Jordan-Baird’s whole undated Transdev spell.
- No new month-conversion or FTE-inference convention has been introduced. Year-only dates remain year precision.

## Next action
- Parliament aggregation workstream may inspect and integrate the sourced partial timelines; preserve null headline totals and record-specific gaps. Obtain further evidence before publishing numerical headlines.
- All member commits are saved on the remote work/parliament-vic-1 branch. Final scope audit: exactly 25 assigned member files plus this checkpoint; no shared UI/data edits, main merge or deployment.
