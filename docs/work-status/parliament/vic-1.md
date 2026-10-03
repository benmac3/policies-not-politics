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

- Active writer: original 2026-10-01 12:00 Brisbane cycle, continuation 0. Started 2026-10-01T12:03:48+10:00. Latest checkpoint 2026-10-01T20:36:59+10:00; attempt end not observed. No active remote conflict observed.
- Nationwide initial audit at 2026-10-01T16:36:18+10:00: 226/226 initial, 0 unstarted, 226 unresolved, 0 research-complete. Day initial additions 80; this attempt initial additions 73, deduplicated from remote member additions. No completed research restarted.
- Follow-up pass follows plan/batch/member order, preserving recorded gaps and last-review dates; current batch records retain their individual prior review dates. All batches remain in the unresolved queue; this is not completion.
- Starting follow-up branch head: c1d7fe74ec61b56e3420250cc0541c6e1d2fa50b; starting batch initial count 25, complete 0. Starting execution national baseline153/226; WA-1 head79b1d5c96ee3dde69dd2f5453e96a2aa434baae2.
- Isolated checkout tracks the assigned remote branch at detached HEAD because an older local worktree has unrelated modified shared outputs; those files and its local branch are untouched. Commits update only work/parliament-vic-1 without force. Local branch-switch error was recovered by this isolated checkout.
- Next follow-up member: 278522 BURNS, Joshua (Josh) Solomon.
- This attempt/cycle:73 new initial, 65 materially enriched existing, 0 newly complete. Brisbane-day:80 new initial, 65 enriched existing, 0 newly complete. Counts include current member only after remote verification; checkpoint-only/repeated IDs excluded.
- OUTCOME: ongoing. STOPPING REASON: none; continue sequential research after remote verification. Successor not requested. Scheduler terminal status unavailable; predecessor successor execution unverified.
- Validation: batch check226/13, individual JSON/source/date/enums and build_careers.load_records; only assigned member and this checkpoint changed.
- Verified national branch heads at initial-pass completion: {"act": "a9c47f619aa170d9df024231e0c3d6631e346837", "nsw-1": "c0dae12c0ce41288b38d3f02f9b661e532b91b24", "nsw-2": "a9be3e613ae49d0fb64ff0c8ea67e67645c18fc8", "nsw-3": "7298fa554d277b48374af242a87c75060258f4b0", "nt": "20e78c5f0d2d2069ead95b0df85fbe49e722fb6b", "qld-1": "af1095e7dc40095c4c2ec7b98363e6d1985c7080", "qld-2": "ee72cfae982567c09bd31c4b2181a4e76882dd9b", "sa": "bdc9586a439bcc400f537a39c7d6ffa305b3e307", "tas": "133fa5642fc57d1046ada547da70105ee64fc4a1", "vic-1": "c1d7fe74ec61b56e3420250cc0541c6e1d2fa50b", "vic-2": "8095f70c11c614d88c38f21a55e5f2306e9f3178", "wa-1": "9a20df4c6e839ed9230b14aeb0deb67d2b548e37", "wa-2": "eb43b3048789389ecba2de0eb34f52a6123ef5f9"}

### Follow-up results in this batch

- 316915; 2026-10-01; materially enriched=True: Added teenage Brighton car-washing job from first speech and preserved two distinct Vamvakinou staff periods from employer-interview reporting. Teaching employment and MHEC name-index lead remain unverified; all dates/hours unknown, no totals manufactured.

- 11788; 2026-10-01; materially enriched=True: Added hospital/Lifeline dates and four government advisory appointments from public profile; independently corroborated basketball chair and Fujitsu exit. Recorded ViPlus2021 end versus2022 biography conflict and retained Fujitsu start conflict. Farm pay/dates, working hours, energy control and remaining governance tenure unresolved.

- 290544; 2026-10-01; materially enriched=True: Added Austin Health registrar observation in2004 with historical public control, Monash fellowship host connection and undated adjunct/medtech roles, plus healthcare-worker advocacy. Full-time fractions, early rotations, appointment boundaries and overlaps unresolved; no totals fabricated.

- 300706; 2026-10-01; materially enriched=True: Resolved business legal/trading names and historical rename via ABR; recovered primary agency history/team and Deej identity; distinguished director and party roles. Foundation/declaration dates do not establish personal FT employment; primary register and earlier work remain gaps.

- 309484; 2026-10-01; materially enriched=True: Added Chisholm teaching and Mordialloc/Kingston/Glen Eira council work from own summit speech; recovered contemporaneous Connectus appointment/association and May2018 CfC coordinator evidence. Frankston employer mapping, salary fractions and precise intervals unresolved; secondary early-retail claim not adopted.

- 288713; 2026-10-01; materially enriched=True: Resolved Wayne Skinner Rural Supplies/Croptec employer from2005 report and own profile, preserved month-date conflict, added pre-degree Ardmona farm and family-vineyard work and MBA2017 context. FT work testimonial remains unallocated; employer/leave boundaries still block totals.

- 263427; 2026-10-01; materially enriched=True: Recovered Parenthood2014–15 succession and2014 executive observation; added separate2020 board role, distinguished Queensland UWU2020 and national2024 roles, and recorded2008–2010 study context without inventing university employment dates. Clinical pay/hours and job boundaries unresolved.

- Recovered GitHub error in preceding Farley save: github_create_tree error_code UNKNOWN, "RemoteProtocolError: Server disconnected without sending a response." Remote head was unchanged; a subsequent attempt succeeded and commit 2c2b6b0b0cd894c10f4afed73bb417203976c641 and both files were remotely verified. Not a terminal error.

























## Active follow-up — 2026-10-02

- Cycle: 2026-10-02 08:00 Brisbane; continuation 0. Attempt start: 2026-10-02T07:56:50+10:00; latest checkpoint: 2026-10-02T18:28:54+10:00; end not yet observed.
- Previous execution reconstructed from remote checkpoints and member commits: 2026-10-01 12:00 continuation 0, started12:03:48; last member commit20:37:12 (648f4c83d549b4e179ee664a8cb0d9ff1c28d216). 73 new initial,65 materially enriched existing,0 newly complete; day80 new,65 enriched,0 complete. Final time/elapsed unknown. OUTCOME: Unknown — final execution status unavailable. STOPPING REASON: unknown. No terminal error or successor request evidenced; no allocation exhaustion inferred. Recovered Farley error is documented above. Later scheduled-message timestamps do not prove separate research executions.
- Remote audit at 2026-10-02T07:58:14+10:00:226 initial,0 unstarted,226 unresolved,0 complete. No member commits on this Brisbane day at invocation start. All13 batch heads plus integration/main inspected; no additional member IDs outside assigned records. No intervening branch change or competing writer observed; previous active marker is stale.
- Starting branch heads: {"act": "a9c47f619aa170d9df024231e0c3d6631e346837", "nsw-1": "2c2b6b0b0cd894c10f4afed73bb417203976c641", "nsw-2": "e83f60591ad234aefd349f909f8f382daf729512", "nsw-3": "80608e5c774a84a7cde1a000bdac589cf02025c9", "nt": "20e78c5f0d2d2069ead95b0df85fbe49e722fb6b", "qld-1": "af1095e7dc40095c4c2ec7b98363e6d1985c7080", "qld-2": "ee72cfae982567c09bd31c4b2181a4e76882dd9b", "sa": "bdc9586a439bcc400f537a39c7d6ffa305b3e307", "tas": "133fa5642fc57d1046ada547da70105ee64fc4a1", "vic-1": "648f4c83d549b4e179ee664a8cb0d9ff1c28d216", "vic-2": "8095f70c11c614d88c38f21a55e5f2306e9f3178", "wa-1": "9a20df4c6e839ed9230b14aeb0deb67d2b548e37", "wa-2": "eb43b3048789389ecba2de0eb34f52a6123ef5f9"}
- Starting vic-1 count:25 initial,0 complete. Current attempt/cycle/day:0 new,200 materially enriched existing,0 newly complete. Counts conditional on remote verification; checkpoint-only commits excluded.
- Next follow-up: 278522 BURNS, Joshua (Josh) Solomon. Continue all batches; blocked is unresolved, not completion.
- OUTCOME: ongoing. STOPPING REASON: none; continue after remote verification. Successor not requested. Scheduler terminal status unavailable; predecessor successor execution unverified.
- Validation: career_batches --check226/13 and --batch vic-1; individual JSON/source/date/enums and build_careers.load_records; only assigned member and batch checkpoint modified.
- Recovered transport error on2October at06:31UTC: exec_command git fetch exited128, `fatal: unable to access https://github.com/benmac3/policies-not-politics.git/: CONNECT tunnel failed, response 403`. Authenticated GitHub connector remained operational; remote branch ref, file bytes, tree SHA and exact commit SHA independently verified through connector. CLI network route not retried. This is recovered, not a terminal error. Subsequent commits use connector verification.
- Recovered source access error: APH first-speech open returned `(403) Forbidden`; accessible transcript and primary organisation material used. Not a terminal error.

### This attempt's member results
- 278522: Resolved Danby chief-of-staff employer and2014 campaign boundary; established teaching during university and separate SKIF chair role. School/printing identity, calendar intervals, working hours and campaign leave unresolved; no headline total invented.
- IPZ: Split journalism into Gippsland Times, Latrobe Valley Express and WIN Television; added July2024 surf-club deputy presidency and explicit volunteer roles. Employer transitions, historical payroll/control and consultancy name/hours remain gaps.
- 249710: Recovered previously omitted family-business delivery/till work and casual bar employment during university from own2025 speech; added primary-confirmed Endometriosis Australia ambassador role. Employer names/dates/hours remain unknown; no age-derived dates or full-time assumption.
- 281503: Recovered exact Link vice-chair interval2011-11-28–2017-12-05 and finance-committee chair, independently verified2019 board resignation; documented finance/study/Collins chronology conflict. Financial employer and full-time work intervals remain unresolved.
- 263547: Recovered2016 council-service break and27 May2019 resignation, mayoral subterms and Frankston/Geelong teaching localities. Employment names/dates/hours remain unresolved.
- 301128: Added part-time Safeway job, ASU start2000, department/Trades Hall secondment evidence, advisory and deputy-chair roles; exact Vision director6 March2018–10 May2024 and chair1 July2021–10 May2024 dates. Public FT interval still unresolved.
- 299962: Resolved HBA historical private commercial classification; recovered15 August1994 TAB privatisation milestone,1995 casual-work/two-month break evidence and1990s singing activity. Early-role hours remain unknown; no totals invented.
- HWG: Added AIAS commissioned papers1980–1981; identified gerontology fellowship project, funders and joint hospital/university affiliation; primary2003/04 Bar council/executive/ethics membership corroboration. Employment hours and institutional control remain unresolved.
- 299964: Identified AMES Noble Park volunteer host and SDA Victorian branch via primary material; documented early part-time retail, multiple Woolworths sites, delegate/HSR role and explicit full-time organiser evidence. Retail FT intervals remain unresolved.
- 295588: Recovered Young Workers Centre committee entry2018 and secretary role, ALP senior vice-presidency2016–2018, lecturer/electorate/communications role details. Academic and other insecure-work employers/dates/hours remain unresolved.
- 243609: Recovered Holding Redlich litigation observations2000–2001 and D’Ambrosio chief-of-staff observationApril2010; clarified Jennings chief-of-staff title. Exact employment boundaries, electorate-office employer and legal full-time hours unresolved.
- 315154: Recovered Youthlaw secretary observation2012–13 and departure13 November2016; identified private-school teaching among unresolved employers. Legal/teaching dates and hours still unknown. LinkedIn429 source error, no retry; alternative annual reports used.
- 282335: Refined Karolinska fellowship toApril–November2014; recovered Melbourne lecturer affiliation fromSeptember2006 and Uppsala title/date discrepancy; resolved Chiltern private community control, retaining nonprofit classification and full-time gaps.
- ZN4: Independently verified1994 3AW work on27 May and22 June using government transcript and broadcaster archive; added January1994 hosting announcement. BroadABC overlap and exact contracts/hours remain unresolved.
- 86256: Resolved councillor1999–2004 and mayor31 March2000–20 March2002 exclusive successor boundary; identified final departmental International Education and Migration portfolio and separate party offices. Public-service FTE/boundaries unresolved.
- 310860: Added self-confirmed Richard Di Natale political work, recovered dated Greenpeace campaigner observation30 October2020 and narrowed UN mission archival context from first-person AMA. Legal employer, business identity and paid/FTE boundaries remain unresolved.
- 266499: Resolved hospital resignation9 May2016 and committee roles; documented prospective Fed Square2014 appointment conflict with official2015. Banking/policy FTE and leave boundaries remain unresolved.
- 316021: Added paid teenage hospitality and bus-depot customer work; identified hospital volunteer context; dated Transdev parent public sole-control transition21 December2016. Names/hours/overlaps and2022–23 gap unresolved.
- 316915: Added named student teaching placement, distinct from paid employment; resolved MHEC2023 mention as association membership rather than staff or board role. Employment dates/hours remain unresolved.
- 11788: Added previously omitted Broadbent electorate-officer work and family equestrian-business context; identified July2016 Harvard study/leave question. Dates, hours and control gaps remain.
- 290544: Resolved medtech institute name and contemporary associate-director title; added resignation context and fungalAi founder activity. Separate paid employment, hours, dates and control remain unresolved.
- 300706: Established @realty partnership and personal sales activity by31August2020; distinguished platform relationship from employment and rejected brother’s sales chronology. Hours and boundaries remain unresolved.
- 309484: Recovered primary Glen Eira Youth Services staff evidence in1997/1999 and Coordinator title byMarch2001. Personal endpoints, continuity and hours remain unverified.
- 288713: Narrowed MBA study to2015–2017 using public profile; added primary-confirmed2020 volunteer leadership teaching, keeping FT allocation unresolved.
- 263427: Added omitted Phil Reeves electorate-officer role from2007 Queensland Hansard and resolved earlier United Voice organiser title. QUT research acknowledgement remains a lead.

## Active follow-up — 2026-10-03 12:00 Brisbane cycle

- Cycle:2026-10-03 12:00 Brisbane; continuation0. Start observed12:03:05+10:00; entered VIC-1 after remotely verifying the completed NSW-3 pass. Starting VIC-1 remote head:92d4379cd285de58c5dc3d29968b5d873a96d659; no competing branch change observed.
- Starting national audit:226/226 initial records,226 unresolved,0 complete. This run/cycle:0 new,13 materially enriched existing,0 newly complete after remote verification;25 distinct member files saved, twelve nonmaterial. Brisbane-day cumulative:0 new,23 materially enriched distinct records,0 newly complete. Morning08:00 results remain separate and are deduplicated by member ID.
- Member316915 Abdo: a primary House committee media release issued21November2011 lists him as alternate media contact for chair Maria Vamvakinou, anchoring their otherwise undated professional association at that date. It does not establish payroll title, hours, appointment/cessation or which of two reported staff periods it belongs to. Teaching searches remained study-only; material point-in-time enrichment.
- Member11788 Aldred: the now-accessible full Fujitsu departure post supplies Corporate Affairs ANZ role scope across cybersecurity, AI, defence and national security; the regional CEO's public reply corroborates her strategic engagement across academia, government and industry peak bodies. It does not resolve exact dates or hours; material role/source enrichment.
- Member290544 Ananda-Rajah: registrar, CV, hospital, professional-profile and publication-affiliation searches found no new bounded pre-2009 employer or rotation beyond the recorded2004 Austin observation. A Royal Darwin phrase belongs another author and was rejected; medtech, fungalAi, fractions, leave and hours remain unresolved. Nonmaterial follow-up with repeated avenues documented.
- Next follow-up:300706 BABET, Ralph. Continue in batch and plan order; blocked records remain unresolved.
- OUTCOME:ongoing. STOPPING REASON:none; continue after remote verification. Successor not requested. Scheduler terminal status unavailable.
- Validation:career_batches --check226/13 and --batch vic-1; individual JSON/source/date/enums and build_careers.load_records. Only assigned member/checkpoint changed.
