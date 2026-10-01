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


## Nationwide follow-up pass — 2026-10-01

- Active writer: original 2026-10-01 12:00 Brisbane cycle, continuation 0. Started 2026-10-01T12:03:48+10:00. Latest checkpoint 2026-10-01T20:18:12+10:00; attempt end not observed. No active remote conflict observed.
- Nationwide initial audit at 2026-10-01T16:36:18+10:00: 226/226 initial, 0 unstarted, 226 unresolved, 0 research-complete. Day initial additions 80; this attempt initial additions 73, deduplicated from remote member additions. No completed research restarted.
- Follow-up pass follows plan/batch/member order, preserving recorded gaps and last-review dates; current batch records retain their individual prior review dates. All batches remain in the unresolved queue; this is not completion.
- Starting follow-up branch head: c1d7fe74ec61b56e3420250cc0541c6e1d2fa50b; starting batch initial count 25, complete 0. Starting execution national baseline153/226; WA-1 head79b1d5c96ee3dde69dd2f5453e96a2aa434baae2.
- Isolated checkout tracks the assigned remote branch at detached HEAD because an older local worktree has unrelated modified shared outputs; those files and its local branch are untouched. Commits update only work/parliament-vic-1 without force. Local branch-switch error was recovered by this isolated checkout.
- Next follow-up member: 290544 ANANDA-RAJAH, Dr Michelle.
- This attempt/cycle:73 new initial, 60 materially enriched existing, 0 newly complete. Brisbane-day:80 new initial, 60 enriched existing, 0 newly complete. Counts include current member only after remote verification; checkpoint-only/repeated IDs excluded.
- OUTCOME: ongoing. STOPPING REASON: none; continue sequential research after remote verification. Successor not requested. Scheduler terminal status unavailable; predecessor successor execution unverified.
- Validation: batch check226/13, individual JSON/source/date/enums and build_careers.load_records; only assigned member and this checkpoint changed.
- Verified national branch heads at initial-pass completion: {"act": "a9c47f619aa170d9df024231e0c3d6631e346837", "nsw-1": "c0dae12c0ce41288b38d3f02f9b661e532b91b24", "nsw-2": "a9be3e613ae49d0fb64ff0c8ea67e67645c18fc8", "nsw-3": "7298fa554d277b48374af242a87c75060258f4b0", "nt": "20e78c5f0d2d2069ead95b0df85fbe49e722fb6b", "qld-1": "af1095e7dc40095c4c2ec7b98363e6d1985c7080", "qld-2": "ee72cfae982567c09bd31c4b2181a4e76882dd9b", "sa": "bdc9586a439bcc400f537a39c7d6ffa305b3e307", "tas": "133fa5642fc57d1046ada547da70105ee64fc4a1", "vic-1": "c1d7fe74ec61b56e3420250cc0541c6e1d2fa50b", "vic-2": "8095f70c11c614d88c38f21a55e5f2306e9f3178", "wa-1": "9a20df4c6e839ed9230b14aeb0deb67d2b548e37", "wa-2": "eb43b3048789389ecba2de0eb34f52a6123ef5f9"}

### Follow-up results in this batch

- 316915; 2026-10-01; materially enriched=True: Added teenage Brighton car-washing job from first speech and preserved two distinct Vamvakinou staff periods from employer-interview reporting. Teaching employment and MHEC name-index lead remain unverified; all dates/hours unknown, no totals manufactured.

- 11788; 2026-10-01; materially enriched=True: Added hospital/Lifeline dates and four government advisory appointments from public profile; independently corroborated basketball chair and Fujitsu exit. Recorded ViPlus2021 end versus2022 biography conflict and retained Fujitsu start conflict. Farm pay/dates, working hours, energy control and remaining governance tenure unresolved.

- Recovered GitHub error in preceding Farley save: github_create_tree error_code UNKNOWN, "RemoteProtocolError: Server disconnected without sending a response." Remote head was unchanged; a subsequent attempt succeeded and commit 2c2b6b0b0cd894c10f4afed73bb417203976c641 and both files were remotely verified. Not a terminal error.
