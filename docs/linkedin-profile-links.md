# LinkedIn links in parliamentary career data

Checked 14 October 2026. Scope: the 226 existing per-member career records on the thirteen Parliament research branches, using their frozen roster identities.

Every member record has an optional `linkedin` object. The cross-branch register at `data/careers/linkedin-profiles.json` records the source path, branch and immutable commit used for each member. This register covers records that have not yet been merged into the Parliament integration branch.

## Results

| Status | Members | Meaning |
| --- | ---: | --- |
| `identity_matched` | 177 | One URL matched by indexed name plus political role or documented career context: 174 personal profiles and 3 office pages. |
| `ambiguous` | 7 | Multiple profiles match political or career context; URLs retained, primary URL null. |
| `unverified` | 1 | A plausible name/location match lacks sufficient career evidence; primary URL null. |
| `not_found` | 41 | No attributable URL found in reviewed public results. This does not establish absence of an account. |

## Fields and interpretation

- `url`: selected URL only when status is `identity_matched`; otherwise null.
- `status`, `checked`, `note`: attribution outcome, link-check date and limits.
- `profiles`: discovered URLs, `page_type` (`personal_profile` or `office_page`), discovery URL/method, indexed title, date and evidence note.
- `search_terms`: member name and platform used for discovery; not a transcript of every search query.

`identity_matched` means the public index supports attribution to the roster person. It does **not** authenticate account ownership, verify that a page remains live, or establish that the politician personally operates it. Office pages use LinkedIn's `/company/` route and are labelled separately. Directory, staff, unrelated namesake, job and share links are not substitutes for a member profile.

Discovery used public search indexes, existing source trails, and other public websites. No LinkedIn profile, post or directory was opened or fetched in this enrichment task; no signed-in session, scraping, authentication bypass or access-control workaround was used. External-site fallback searches were used for unresolved names. Generic social-sharing controls on official sites were rejected. External access errors were left unresolved rather than bypassed.

Names and career context were cross-checked against the existing records. For example, the nurse named Julie-Ann Campbell and the Tasmanian care manager named Leah Blyth were excluded as namesakes. A previously noted professional-profile lead is not automatically accepted.

This is URL enrichment only. Existing sources, career spells, research statuses, review dates, exclusions and employment-year headlines remain unchanged. Link discovery does not establish employment dates, full-time status or employer ownership. `scripts/build_careers.py` carries the selected URL and status into summary JSON/CSV after the research branches are integrated; uncertain links remain accessible in the member record and register.

The enrichment commits remain on research branches. The published website is unchanged until the established integration/release workflow merges and builds them.
