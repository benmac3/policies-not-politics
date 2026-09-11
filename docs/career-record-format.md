# Per-member parliamentary career record format

Version 1.0 — 11 September 2026

The Parliament research workstream is intentionally sharded. Each research conversation writes one durable JSON file per parliamentarian under `data/careers/members/<person_id>.json`. Batch conversations must not edit `data/parliament.json`, the Parliament UI renderer, or another batch's member files.

The purpose of the per-member record is to make the source trail, classification and duration logic survive conversation limits and parallel execution.

## Required top-level shape

```json
{
  "person_id": "11788",
  "name": "ALDRED, Mary",
  "snapshot_state": "Vic",
  "snapshot_chamber": "Member",
  "snapshot_party": "Liberal Party of Australia",
  "snapshot_source": "https://handbook.aph.gov.au/parliamentarians/11788",
  "research_status": "complete",
  "last_reviewed": "2026-09-11",
  "headline": {
    "public_full_time_years": null,
    "private_full_time_years": null,
    "calculation_status": "partial",
    "note": "Only spells with sufficiently supported dates and full-time status are counted."
  },
  "career_spells": [],
  "sources": [],
  "research_notes": []
}
```

`research_status` is one of `not_started`, `in_progress`, `complete`, or `blocked`. `calculation_status` is one of `complete`, `partial`, or `not_calculable`.

## Career-spell fields

Each spell should use:

```json
{
  "spell_id": "11788-fujitsu",
  "employer": "Fujitsu Asia Pacific",
  "role": "Head of Corporate Affairs",
  "start_date": "YYYY-MM-DD or YYYY-MM or YYYY",
  "end_date": "YYYY-MM-DD or YYYY-MM or YYYY",
  "date_precision": "day|month|year|mixed|unknown",
  "employment_status": "full_time|part_time|self_employed|unknown",
  "fte_fraction": null,
  "category": "private_enterprise",
  "headline_sector": "private|public|excluded|unknown",
  "government_control_at_time": "private|public|mixed|unknown",
  "counting_status": "counted|excluded|insufficient_evidence",
  "source_ids": ["src-1"],
  "evidence_note": "Why these dates, employer and classification are supported.",
  "counting_note": "Why this spell is or is not included in the public/private full-time headline."
}
```

The category vocabulary is defined in `docs/career-codebook.md`. `headline_sector` is deliberately narrower than category: only sufficiently evidenced public-sector and private-sector employment contributes to the headline totals. Elected office, political staff, party organisations, unions, employer associations, nonprofits, study, unpaid work and unresolved cases are excluded from those two headline totals unless the codebook explicitly establishes that the employing entity belongs in one of the two sectors.

## Source fields

Each source entry should include:

```json
{
  "source_id": "src-1",
  "url": "https://...",
  "publisher": "Australian Parliament",
  "title": "...",
  "retrieved": "2026-09-11",
  "source_type": "official_biography|employer|government_record|professional_profile|news|other",
  "locator": "page/section/quoted heading where useful",
  "note": "What this source establishes."
}
```

Prefer official parliamentary biographies, employer/organisation records, government records and other primary sources. A publicly accessible professional profile may supplement missing dates. Do not bypass authentication or access controls to obtain LinkedIn data.

## Headline calculation rules

The headline is **documented full-time employment years in the public sector** and **documented full-time employment years in the private sector**. It is not total adult working life and is not a competence score.

- Count only spells whose employer classification, dates and full-time status are sufficiently supported for the stated precision.
- Merge overlapping counted intervals within a sector before calculating elapsed time. Do not double-count simultaneous roles.
- Do not add public and private durations across overlapping calendar intervals as though a person worked two full-time years in one year.
- Part-time work is excluded from the headline unless a defensible FTE fraction is available and the project explicitly elects to report FTE-adjusted totals separately.
- Self-employment may count as private-sector work when the dates and substantive full-time nature of the work are supported.
- Year-only dates remain year-precision evidence. Do not silently invent January/December boundaries. If a bounded estimate is later calculated, label it as a range rather than an exact total.
- Month-level professional-profile dates may be retained at month precision. Any conversion convention used for a duration calculation must be documented consistently in the aggregation script and visible in the site methodology.
- Unknown or ambiguous periods remain unknown; they do not become zero.

## Commit discipline

A batch Work conversation must complete one member record, validate its JSON, commit that member and update its checkpoint before researching the next member. The conversation must never hold a completed member's only durable evidence in chat context.

A member may be committed with `research_status: blocked` if meaningful primary/secondary source work has been exhausted and the missing evidence is documented. This is preferable to speculative filling.
