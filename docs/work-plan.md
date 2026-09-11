# Parallel Work orchestration plan

Version 1.0 — 11 September 2026

This document is the canonical coordination plan for continuing the **Policy not politics** research project across multiple ChatGPT Work conversations without recreating one oversized conversation. The GitHub repository is the durable source of truth. A Work conversation may use Project context, but it must verify repository state before assuming another conversation completed an action.

## Why the project is split this way

The published site currently has seven navigation views:

1. Economic dashboard (`#dashboard`)
2. Start with productivity (`#learn`)
3. Country comparisons (`#countries`)
4. NDIS & the economy (`#ndis`)
5. Policy & scenarios (`#scenarios`)
6. Parliament’s experience (`#representatives`)
7. Sources & scrutiny (`#evidence`)

The first two views are tightly coupled around productivity, living standards and the same Australian observations, so they form one workstream. The remaining five views each form their own workstream. A seventh Work conversation performs integration, QA and deployment only.

## Operating model

- `main` is the released integration branch. GitHub Pages deploys automatically after a push to `main` and runs the repository build and validation workflow.
- Each specialist Work conversation owns exactly one branch and one workstream.
- Specialist Work conversations do **not** merge to `main` and do **not** deploy production.
- The integration/release Work conversation is the only conversation that merges completed specialist branches to `main`.
- Before research or editing, inspect the current branch, recent commits, existing data/docs and this file. Do not infer completion from prior conversation prose.
- Commit coherent checkpoints frequently enough that a replacement Work conversation can recover from the repository alone.
- Do not create claims or values merely to fill a gap. Missing or unverified remains missing or unverified.

## Shared research rules

The methodological authority is `docs/research-method.md`, supplemented by section-specific codebooks such as `docs/career-codebook.md` and the current release notes in `docs/data-release.md`.

Across all workstreams:

1. Prefer primary and authoritative sources. Retain the source URL, reference period, retrieved date and definition needed to reproduce a claim.
2. Keep official observations, official forecasts, party proposals/claimed costings, project calculations, causal hypotheses and unknowns distinct.
3. Distinguish sourced facts from calculated or inferred values. Record assumptions for every project calculation.
4. Do not convert missing evidence into zero.
5. Do not silently change an established methodology. If a method must change, update the relevant documentation and explain the effect on prior outputs.
6. Avoid broad formatting/reordering of shared files. Edit only the relevant records or renderer function to reduce merge conflicts.
7. Treat public web pages as sources only when access is permitted. Do not bypass authentication, robots/access controls or site restrictions. For career research, LinkedIn may be used as a secondary source when the relevant public page is legitimately accessible, but do not automate scraping of gated LinkedIn content.
8. Preserve enough provenance that another researcher can reproduce or challenge each material result.

## Repository conventions

Current UI code is compact: the seven page renderers are functions in `dist/app.js`. The data and methodology sources live under `data/` and `docs/`; `scripts/build.py` creates `dist/data.js`, mirrors top-level source data/docs into `dist/`, and rebuilds the downloadable source pack.

Therefore:

- `dist/app.js`, `dist/index.html` and `dist/style.css` are current hand-maintained UI assets.
- Do **not** hand-edit generated `dist/data.js`, mirrored `dist/data/*`, mirrored `dist/docs/*` or `dist/source-pack.zip`. Change the source file and run `python scripts/build.py`.
- Run `python scripts/validate.py` after source/data changes.
- Run `node --check dist/app.js` after JavaScript changes.
- Run `node scripts/check-models.cjs` after model/scenario changes.
- Before handing a specialist branch to integration, run every check relevant to that branch and record the result in the branch checkpoint.

## Workstream 1 — Economy & productivity foundations

**Branch:** `work/economy-productivity`

**Owns:** navigation views 01 and 02; `dashboard()` and `learn()` in `dist/app.js`; Australian productivity/living-standard observations and explanatory material.

**Primary files:** `data/observations.*`, relevant `data/sources.*` entries, relevant `data/extensions.*`, `docs/research-method.md`, `dist/app.js` (`dashboard`, `learn`).

**Goals:**

- Improve the Australian productivity and living-standards evidence behind the dashboard and explainer.
- Complete or improve output-per-hour and multifactor-productivity coverage where authoritative sources permit.
- Improve harmonised household-income/living-standard context without mixing incompatible vintages or definitions.
- Keep teaching examples visibly separate from forecasts.
- Remove stale coverage statements when a gap has actually been closed.

**Do not:** take ownership of the international country explorer, NDIS causal estimates, party costings or parliamentary career research.

**Bootstrap prompt:**

> You are Workstream 1: Economy & productivity foundations for the Policy not politics project. Work only on branch `work/economy-productivity`. Read `docs/work-plan.md`, `docs/research-method.md`, `docs/data-release.md`, inspect current repository state, then continue the workstream scope defined there. Verify completed work from Git rather than assuming prior Work conversations finished it. Keep a branch checkpoint at `docs/work-status/economy-productivity.md`. Do not merge to main or deploy production.

## Workstream 2 — Country comparisons

**Branch:** `work/country-comparisons`

**Owns:** navigation view 03; `countries()` and country-history/table behaviour in `dist/app.js`; internationally comparable panel data and definitions.

**Primary files:** `data/panel.*`, `data/metrics.*`, `data/countries.*`, relevant `data/sources.*`, `scripts/import_worldbank.py`, `scripts/import_oecd.py`, `dist/app.js` (`countries` and directly related helpers).

**Goals:**

- Improve international productivity and living-standard comparability.
- Pursue authoritative hourly-productivity and multifactor-productivity coverage where practical.
- Add high-value missing comparison families only when they can be sourced and defined consistently (for example household income, housing affordability, wealth/liquid buffers, effective tax burden, business formation, energy prices or technology adoption).
- Preserve country/year coverage and missingness; never rank countries using mixed-year values without making that method explicit.

**Do not:** turn this into a general country-ranking score or infer policy causation from cross-sectional correlations.

**Bootstrap prompt:**

> You are Workstream 2: Country comparisons for the Policy not politics project. Work only on branch `work/country-comparisons`. Read `docs/work-plan.md`, `docs/research-method.md`, `docs/data-release.md`, inspect current repository state, then continue the workstream scope defined there. Verify completed work from Git. Keep a branch checkpoint at `docs/work-status/country-comparisons.md`. Do not merge to main or deploy production.

## Workstream 3 — NDIS & the economy

**Branch:** `work/ndis-economy`

**Owns:** navigation view 04; `ndis()` in `dist/app.js`; NDIS actuals, integrity evidence, workforce mechanisms, funding exposure and carefully scoped fiscal analysis.

**Primary files:** relevant rows in `data/observations.*`, `data/extensions.*`, `data/budget.*`, `data/sources.*`, `docs/research-method.md` NDIS section, `dist/app.js` (`ndis`).

**Goals:**

- Keep participant costs, administration, Commonwealth/state contributions, cash/accrual measures and projections distinct.
- Improve integrity evidence without presenting detected cases as a prevalence estimate.
- Research credible participant/carer labour outcomes, provider/workforce data and the distinction between public-sector employment and publicly funded private employment.
- Where evidence permits, develop transparent scenarios for workforce opportunity cost or public-funding employment exposure; label them as estimates rather than official employment classifications.
- Avoid attributing a standalone pool of government debt to the NDIS.

**Bootstrap prompt:**

> You are Workstream 3: NDIS & the economy for the Policy not politics project. Work only on branch `work/ndis-economy`. Read `docs/work-plan.md`, `docs/research-method.md`, `docs/data-release.md`, inspect current repository state, then continue the workstream scope defined there. Verify completed work from Git. Keep a branch checkpoint at `docs/work-status/ndis-economy.md`. Do not merge to main or deploy production.

## Workstream 4 — Policy & scenarios

**Branch:** `work/policy-scenarios`

**Owns:** navigation view 05; `scenarios()` and its calculators/model text in `dist/app.js`; dated baseline-versus-alternative policy comparisons.

**Primary files:** `data/budget.*`, relevant `data/sources.*`, relevant observations/extensions, `docs/research-method.md` policy/model sections, `scripts/check-models.cjs`, `dist/app.js` (`scenarios` and its calculator logic).

**Goals:**

- Maintain a dated current-policy baseline and explicitly map alternative proposals to changed parameters.
- Improve independent costings or defensible ranges where authoritative costings exist; otherwise retain proposals as proposals.
- Reconcile implementation dates, legislation/funding status, behavioural assumptions and replacement costs.
- Prevent double-counting of savings already in the baseline.
- Present 5/10/20/30-year scenarios as transparent sensitivities rather than partisan forecasts.

**Do not:** convert a party headline saving into a verified fiscal saving without a reproducible net-cost method.

**Bootstrap prompt:**

> You are Workstream 4: Policy & scenarios for the Policy not politics project. Work only on branch `work/policy-scenarios`. Read `docs/work-plan.md`, `docs/research-method.md`, `docs/data-release.md`, inspect current repository state, then continue the workstream scope defined there. Verify completed work from Git. Keep a branch checkpoint at `docs/work-status/policy-scenarios.md`. Do not merge to main or deploy production.

## Workstream 5 — Parliament’s experience

**Branch:** `work/parliament-experience`

**Owns:** navigation view 06; `representatives()` in `dist/app.js`; parliament roster, sourced career timelines, duration calculations and career methodology.

**Primary files:** `data/parliament.*`, new career-spell datasets created by this stream, relevant `data/sources.*`, `scripts/import_parliament.py`, `docs/career-codebook.md`, `dist/app.js` (`representatives`).

**Immediate product goal:** for each parliamentarian where evidence is sufficient, publish a sourced career timeline and headline totals for documented full-time employment in the **public sector** and **private sector**, with a visible byline/footnote explaining the calculation and exclusions.

**Duration logic:**

- Use source-backed start/end dates and employment status where available.
- Calculate elapsed time from employment spells, merge overlapping intervals before totals, and prevent simultaneous roles from becoming double-counted full-time years.
- Count public/private **employment** separately from elected office, party/political staff, unions/employer associations, nonprofits, universities, study, unpaid work and unknown unless the documented employer-control rule in the codebook explicitly places the role in public or private employment.
- For universities, public corporations, nonprofits and mixed entities, classify employer control at the time rather than inferring from job title or funding source.
- Do not convert undated occupation lists into years.
- Do not assume full-time-equivalent fractions where the evidence is genuinely ambiguous. If the project adopts a conservative inference rule for apparently continuous full-time employment, document that rule and confidence level before using it, apply it consistently across parties, and keep inferred totals distinguishable from directly evidenced totals.
- Preserve source URLs and a short coding rationale for every counted spell.
- Use official parliamentary biographies, employer/organisation records and other primary sources first. Publicly accessible professional profiles may supplement missing dates; gated LinkedIn content must not be scraped or bypassed.

**Bootstrap prompt:**

> You are Workstream 5: Parliament’s experience for the Policy not politics project. Work only on branch `work/parliament-experience`. Read `docs/work-plan.md`, `docs/career-codebook.md`, `docs/data-release.md`, inspect current repository state and any existing career research, then resume from the first incomplete member rather than restarting completed work. The target output is sourced career timelines plus documented full-time public-sector and private-sector employment years, with transparent calculation logic and exclusions. Keep a branch checkpoint at `docs/work-status/parliament-experience.md`. Do not merge to main or deploy production.

## Workstream 6 — Sources & scrutiny

**Branch:** `work/sources-scrutiny`

**Owns:** navigation view 07; `evidence()` in `dist/app.js`; claim/source registers, provenance, reproducibility, correction pathways and release documentation.

**Primary files:** `data/claims.*`, `data/sources.*`, `docs/research-method.md`, `docs/data-release.md`, `docs/indicator-map.md`, `CONTRIBUTING.md`, `dist/app.js` (`evidence`).

**Goals:**

- Audit source-register quality, retrieval dates, broken links, source/claim IDs and provenance.
- Improve reproducibility and explain what is observation, model, proposal or unknown.
- Maintain an accurate list of remaining research gaps based on actual repository state.
- Make challenge/correction pathways usable and symmetric across political parties and policy claims.
- Keep release notes accurate after specialist work is integrated.

**Do not:** independently rewrite another workstream’s substantive conclusion without coordinating through integration and the relevant methodology.

**Bootstrap prompt:**

> You are Workstream 6: Sources & scrutiny for the Policy not politics project. Work only on branch `work/sources-scrutiny`. Read `docs/work-plan.md`, `docs/research-method.md`, `docs/data-release.md`, inspect current repository state, then continue the workstream scope defined there. Verify completed work from Git. Keep a branch checkpoint at `docs/work-status/sources-scrutiny.md`. Do not merge to main or deploy production.

## Workstream 7 — Integration, QA & release

**Branch:** `work/integration-release`

**Owns:** cross-stream integration, conflict resolution, site-wide consistency, build/validation, merge to `main`, GitHub Pages deployment and production verification.

**Responsibilities:**

1. Inspect `main`, all specialist branch heads and their checkpoint files before merging anything.
2. Merge one completed specialist workstream at a time. Resolve conflicts by preserving the specialist’s domain changes while retaining already integrated changes from other workstreams.
3. Reconcile shared-file changes in `dist/app.js`, `data/sources.*`, `docs/research-method.md` and release documentation.
4. Run:
   - `python scripts/build.py`
   - `python scripts/validate.py`
   - `node --check dist/app.js`
   - `node scripts/check-models.cjs`
5. Review every navigation route and important interactive control after integration.
6. Update `docs/data-release.md` and coverage/gap language to match what is actually shipped.
7. Merge/push the integrated result to `main` only after the checks pass.
8. Verify the GitHub Pages workflow and inspect the deployed site. A successful commit alone is not proof that production is correct.
9. If a specialist branch is incomplete or its evidence is not adequate, leave it unmerged and record the reason rather than manufacturing a resolution.

The integration stream should not become a seventh research stream. When it finds a substantive domain problem, return the issue to the relevant specialist branch unless a small mechanical correction is clearly sufficient.

**Bootstrap prompt:**

> You are Workstream 7: Integration, QA & release for the Policy not politics project. Work only on branch `work/integration-release` until an explicitly validated release is ready. Read `docs/work-plan.md` and every available `docs/work-status/*.md`, compare all specialist branches with `main`, then integrate only completed and validated workstreams. Run the full build/model/JavaScript validation suite, update release notes, merge the validated release to `main`, verify the GitHub Pages workflow and inspect the deployed site. Do not perform substantial domain research inside this integration conversation.

## Checkpoint contract for every specialist Work conversation

Each specialist branch maintains its own file at `docs/work-status/<slug>.md`. This avoids six parallel conversations editing the same status file. Create it if it does not yet exist. At each meaningful checkpoint, replace it with a concise record containing:

```markdown
# <Workstream name> status

Last updated: <ISO date/time>
Branch: <branch>
Branch HEAD: <commit SHA after checkpoint commit, or PRE-COMMIT while preparing the commit>
Main base observed: <main SHA>
State: not-started | in-progress | blocked | ready-for-integration | integrated

## Completed
- ...

## Evidence/data added or changed
- ...

## Validation run
- command — PASS/FAIL

## Remaining
- ...

## Ambiguities / decisions needed
- ...

## Next action
- ...
```

The status file is a handoff artifact, not a diary. Keep it short and overwrite stale detail rather than appending an ever-growing transcript.

## Recovery after a conversation-length limit

When a specialist Work conversation reaches its maximum length, start a successor Work conversation in the same Project and give it only the corresponding bootstrap prompt above. The successor must:

1. inspect its assigned branch and checkpoint file;
2. verify the most recent commit and validation state;
3. inspect only the source files relevant to the next incomplete task;
4. resume from `Next action`;
5. avoid loading unrelated workstream history unless a concrete dependency requires it.

This is the intended mechanism for keeping conversation context bounded while retaining durable project state.

## Cross-workstream dependency rule

Do not ask specialist conversations to read one another’s full chat histories. If one workstream needs a result from another, communicate it through committed data/docs or a short checkpoint note. The repository carries durable facts and decisions; conversations carry temporary working context.

## Suggested launch order

The six specialist workstreams can run in parallel. Parliament’s experience is particularly suitable for an independent long-running research conversation because it has a large per-member source trail. Sources & scrutiny can audit existing material immediately but should perform a final pass after the other specialist branches are ready. The integration/release conversation should normally run after one or more specialist branches declare `ready-for-integration`, and again for the final site-wide release.