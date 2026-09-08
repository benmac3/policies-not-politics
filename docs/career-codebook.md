# Parliamentary career codebook

Target population: all serving federally elected representatives in the House and Senate at the declared snapshot date. Include casual-vacancy appointees serving in an elected chamber, noting appointment status. Publish House and Senate totals separately. Vacancies and unknown biographies remain visible. No full roster is loaded in this edition.

One row per employment spell. Fields: person_id, name, chamber, party_at_snapshot, snapshot_date, employer, role, start_date, end_date, date_precision, category, government_control_at_time, public_funding_share, fte_fraction, source_url, source_locator, evidence_note, coding_status.

Categories: private_enterprise; public_service; public_corporation; political_staff; party_organisation; union; employer_association; nonprofit; university; elected_office; unpaid_work; study; unknown.

Occupation is not sector. A lawyer may work in a private practice, public legal service or union. A nurse or teacher may work for a public, private or nonprofit employer. A university role requires institutional treatment, not automatic coding as private enterprise. A bank's ownership at the time matters. Public funding alone does not prove public control. Political employment is shown independently even when the employing organisation is formally private.

Use complete source-backed career spells, not only the final occupation before parliament. Preserve inter-parliamentary work separately from first-entry experience. Education and honorary positions do not automatically count as paid employment.

For exact dates use half-open intervals [start, end). Merge overlapping intervals before computing total calendar time in a category and across all employment. Do not sum overlapping directorships as full-time years. If only year labels exist, retain year precision and publish minimum/maximum plausible durations; do not silently assume January 1. Missing FTE stays null.

Useful outputs after coding: share with any documented private-enterprise experience; distribution of documented years by category; mixed-career composition; proportion unknown; time in political roles before first federal entry. Shares across non-exclusive experience categories may sum above 100%; say so explicitly.

Do not infer zero experience from an omitted biography entry. Do not make a competence score from career history. Publish coding rationale, allow corrections and review disputed cases using the same standard for every party.
