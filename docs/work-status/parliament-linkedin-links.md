# Parliament LinkedIn link enrichment

Checked: 2026-10-14
Branch: work/parliament-linkedin-links
Base: 8f7179c6accfe62d4c547bb8cfed1129e3dcf796
State: ready-for-integration

## Completed

- Searched all 226 existing career-record identities across thirteen research branches.
- Added a `linkedin` object to every record on its owning research branch. Existing career fields preserved.
- 177 single identity matches (174 personal profiles; 3 office pages), 7 multiple-profile cases, 1 unverified candidate, 41 not found.
- Added consolidated register, interpretation documentation and summary URL/status columns.
- Used public search indexes and external websites; no direct LinkedIn fetches or scraping.

## Validation

- Full-record preservation and unique-ID checks: PASS, 226 records.
- Remote file hashes: PASS for all 226 initial enrichment writes; subsequent Templeman evidence-note clarification fetched and compared.
- `python scripts/build_careers.py`: PASS, 226 summaries and 3507 spells on assembled research snapshot.
- All 226 summary URL/status values agree with the register: PASS.
- `python scripts/build.py`, `python scripts/validate.py`, `node --check dist/app.js`, `node scripts/check-models.cjs`: PASS on the assembled snapshot with main's unchanged supporting data/assets.

## Research branch commits

- [work/parliament-act](https://github.com/benmac3/policies-not-politics/commit/863605913761765b5d53ea5f82fe0f8ae9b7da1d): 5 records.
- [work/parliament-vic-1](https://github.com/benmac3/policies-not-politics/commit/31611291763edffc33e09aa2aae4443aecfab83d): 25 records.
- [work/parliament-nsw-1](https://github.com/benmac3/policies-not-politics/commit/4e867a2390078558e215c1412c084c783dd21ca8): 20 records.
- [work/parliament-qld-1](https://github.com/benmac3/policies-not-politics/commit/d4ae396843b45759a983079271bba2bd52aa6294): 21 records.
- [work/parliament-wa-1](https://github.com/benmac3/policies-not-politics/commit/e5a302c8ab0ea2d437c9f6b8d75dcb6e576a6285): 14 records.
- [work/parliament-sa](https://github.com/benmac3/policies-not-politics/commit/b991e331f9c3f1b73c0f34cb0602242d490170f2): 22 records.
- [work/parliament-tas](https://github.com/benmac3/policies-not-politics/commit/c32069c4484d7e33ad992b685a4b51292b29021c): 17 records.
- [work/parliament-nsw-2](https://github.com/benmac3/policies-not-politics/commit/c4c5a071208baffdff72af19c96e735c29a692a3): 19 records.
- [work/parliament-nt](https://github.com/benmac3/policies-not-politics/commit/0beffcb5d27fa831de3f51227a86ab994ba1d3c3): 4 records.
- [work/parliament-vic-2](https://github.com/benmac3/policies-not-politics/commit/225891e6ceffde053b0322105d63966be45021ea): 25 records.
- [work/parliament-qld-2](https://github.com/benmac3/policies-not-politics/commit/98d8508ec3b69df5d34071ca228f8c7c9a57972b): 21 records.
- [work/parliament-wa-2](https://github.com/benmac3/policies-not-politics/commit/59c24659fccc4ca8db78de7f5add0bebd665bb3d): 14 records.
- [work/parliament-nsw-3](https://github.com/benmac3/policies-not-politics/commit/490db69a907e663a501132ecf65a88871b36d0b4): 19 records.

## Remaining / integration

- Review 8 uncertain cases and 41 unmatched identities; no guessed profile URLs were added.
- Merge this register/documentation/summary change into work/parliament-experience. The member enrichments accompany their owning batch branches during integration; this PR does not duplicate or merge those branches.
- Regenerate the aggregate and deployment outputs after integrating the research branches, through the existing release process. No main merge or production deployment performed.
