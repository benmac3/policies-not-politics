# Parliament vic-1 status

Last updated: 2026-09-12
Branch: work/parliament-vic-1
Branch HEAD: PRE-COMMIT (this checkpoint is committed with the member record; use git log -1)
Main base observed: 8f7179c6accfe62d4c547bb8cfed1129e3dcf796
State: in-progress

## Completed
- 316915 ABDO, Basem: blocked durable record.
- 11788 ALDRED, Mary: blocked durable record.
- 290544 ANANDA-RAJAH, Dr Michelle: blocked durable record.
- 300706 BABET, Ralph: blocked durable record.
- 309484 BELYEA, Jodie Anne: blocked durable record.
- 288713 BIRRELL, Samuel (Sam) James: blocked durable record.
- 263427 BRISKEY, Jo: blocked durable record.

## Evidence/data added or changed
- Per-member source-linked career spells, exclusions and explicit evidence gaps. Only assigned member files and this checkpoint changed.

## Validation run
- python scripts/career_batches.py --check — PASS (226 members, 13 batches).
- python scripts/career_batches.py --batch vic-1 — PASS (25 assigned members).
- JSON parse, source-reference/category/interval checks and scripts.build_careers.load_records() — PASS. Aggregation outputs are not written.
- python scripts/validate.py — PASS.

## Remaining
- 278522 BURNS, Joshua (Josh) Solomon
- IPZ CHESTER, the Hon. Darren Jeffrey
- 249710 CHESTERS, Lisa Marie
- 281503 CICCONE, Raffaele (Raff)
- 263547 COKER, Elizabeth (Libby) Ann
- 301128 DARMANIN, Lisa
- 299962 DOYLE, Mary
- HWG DREYFUS, the Hon. Mark Alfred, KC
- 299964 FERNANDO, Cassandra
- 295588 GARLAND, Dr Carina Mary Lindsay
- 243609 GILES, the Hon. Andrew James
- 315154 GREGG, Matt
- 282335 HAINES, Dr Helen Mary
- ZN4 HENDERSON, the Hon. Sarah Moya
- 86256 HILL, the Hon. Julian Christopher
- 310860 HODGINS-MAY, Steph
- 266499 HUME, the Hon. Edwina Jane (Jane)
- 316021 JORDAN-BAIRD, Alice

## Ambiguities / decisions needed
- Blocked means a sourced partial timeline is durable, but dates, employer control or full-time evidence remain insufficient for the requested headlines. It does not mean zero experience.
- No new month-conversion or FTE-inference convention has been introduced. Year-only dates remain year precision.

## Next action
- Research 278522 BURNS, Joshua (Josh) Solomon, validate and commit before moving on.
