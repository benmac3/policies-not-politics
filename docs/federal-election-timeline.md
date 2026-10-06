# Australian federal election timeline — review edition

As of 6 October 2026. Branch: `work/federal-election-timeline`.
This is an additive, standalone review, not a production release or an exhaustive live parliamentary membership ledger.

## Review and reproduce

From the repository root, with Python 3.10 or later:

```sh
python scripts/build_election_timeline.py --check-only
python scripts/build_election_timeline.py
```

Open `reviews/generated/federal-election-timeline.html` in a browser. The generated HTML embeds the entire dataset and needs no server, network access, external JavaScript or fonts. Do not open the `.template.html` directly: it needs the build step.

The build also produces `federal-election-timeline.json`, `election-seats.csv`, `event-index.csv` and `validation-report.json` in `reviews/generated/`. Generated outputs are delivered in the conversation review package; the repository stores the reproducible source data, compiler and visualization template. No shared `dist` asset or existing build pipeline is changed.

Optional browser checks require Playwright and Chromium:

```sh
python scripts/test_election_timeline_ui.py
```

Set `CHROMIUM_EXECUTABLE` to a local browser path when necessary. Without it, the test tries a system Chromium and then Playwright's installed Chromium.

## Coverage

285 dated records: 48 general elections (1901–2025), 165 House by-elections (through Farrer, 9 May 2026), four Senate-only elections, the 1908 South Australian Senate supplementary poll, the 2014 WA Senate rerun, three supplementary House polls, 38 PM events and 25 formal DPM events. The leadership totals comprise 37 PM appointments covering 31 people plus one vacancy; 22 DPM appointments plus three vacancies. The four Senate casual-vacancy contests held alongside the 1963, 1966, 1969 and 1972 House elections are included within those general-election records.

## Data and provenance

`data/federal-election-timeline.psv` is the canonical UTF-8 source. It has named pipe-delimited sections: sources, parties, general elections, Senate contests, leadership, House by-elections and supplementary polls. Seat maps use `CODE:INTEGER`. Blank fields remain null; they do not mean zero.

The source register retains URLs, source authority and relevant table/page descriptions. The compiler supplies the retrieval date, source IDs, source-file SHA-256, stable event IDs and derived fields. AEC tables and the Parliamentary Library's historical results compilation are the principal electoral sources. Explicitly labelled secondary compilations supplement candidate names, day-level leadership chronology and some full-Senate projections. This is not a complete primary-source audit. Original web/PDF bytes are not bundled; the source file is a documented transcription, not an archived raw-source snapshot.

## Definitions

**House:** final aggregate election results, including separately dated deferred division polls. Early territory members with restricted voting rights are counted as members, not automatically as votes on confidence.

**Senate elected:** only the places filled in that contest. **Senate full:** a separately labelled full-chamber snapshot or result projection. Historical reporting bases differ. Modern projections use election-date affiliations and exclude subsequent defections. They must not be presented as current membership or mechanically assigned to 1 July.

**By-election change:** subtract one from the outgoing member's party before the vacancy and add one to the winner's party; a hold is zero. The resulting 40 party transfers include the later-annulled 1992 Wills return and flagged historical classifications. Modern Coalition-family arithmetic is separate from party transfers. These deltas do not establish an absolute government majority, a confidence agreement or the balance during the vacancy. Ordinary Senate appointments, all defections, recounts and intervening vacancies are not exhaustively modelled.

**Leadership:** substantive appointments, with PM at polling and after government formation distinguished. Initial appointments and returning office-holders are retained. DPM begins with the formal office in January 1968; earlier de facto deputies and routine acting arrangements are excluded. A PM's party is recorded at accession, not asserted constant for the whole term.

**Annulments and supplementary polls:** the invalidated 2013 WA return is flagged and linked to its 2014 replacement; those six places are not added to the national total. The 1992 Wills return is flagged as later annulled. Supplementary House polls are already included in their general-election totals. Four unopposed House returns use actual declaration dates and separately retain scheduled polling dates.

## Outstanding review issues

Fourteen historical House election results retain an unresolved `OTH` source category. It is not a party. Historical state affiliates and factions are not uniformly disaggregated, and the 2010 House and Senate sources use different LNP/caucus groupings. Three by-election classifications require reconciliation: Echuca 1907, Wakefield 1909 and Wimmera 1946. Their notes preserve the competing source interpretations.

Full-Senate counts for the 1963 and 1969 special contests are explicitly marked reconstructions from earlier benchmarks and election deltas, requiring independent review. The 1966 snapshot uses a secondary table. Full-chamber snapshots for 1908 and 1972 have not been independently verified and remain missing; the UI links to earlier benchmarks without silently forward-filling them. Original 2016 returns are retained rather than replacing them with later disqualification recounts.

## Checks and release boundary

The compiler checks section structure, party/source references, unique IDs, dates, all 48 House totals, Senate places and full-chamber totals, zero-sum transfer deltas, leadership coverage and key historical regressions. The optional browser test checks filtering, selection, annulment warnings, JSON export and desktop/mobile layout. These are arithmetic and software checks, not proof of every historical classification.

The shared site build, shared validation and production deployment have not been run for this isolated addon. Integration must review the outstanding data issues and decide how to expose the new view before merging to `main`.
