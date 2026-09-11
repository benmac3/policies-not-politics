# Parallel Work orchestration plan

Version 1.1 — 11 September 2026

This document is the canonical coordination plan for continuing the **Policy not politics** research project across multiple ChatGPT Work conversations without recreating one oversized conversation. The GitHub repository is the durable source of truth. A Work conversation may use Project context, but it must verify repository state before assuming another conversation completed an action.

## Site-level workstreams

The published site has seven navigation views:

1. Economic dashboard (`#dashboard`)
2. Start with productivity (`#learn`)
3. Country comparisons (`#countries`)
4. NDIS & the economy (`#ndis`)
5. Policy & scenarios (`#scenarios`)
6. Parliament’s experience (`#representatives`)
7. Sources & scrutiny (`#evidence`)

Views 01 and 02 form one specialist workstream. Views 03–07 each form another. A seventh site-level conversation performs integration, QA and deployment. **Parliament’s experience is internally sharded into bounded member-research batches because a single Parliament Work conversation proved too large.**

## Operating model

- `main` is the released integration branch. GitHub Pages deploys automatically after a push to `main` and runs the repository build/validation workflow.
- Specialist Work conversations do **not** merge to `main` and do **not** deploy production.
- The site integration/release conversation is the only conversation that merges completed site-level specialist work to `main`.
- Before research or editing, inspect the assigned branch, recent commits, existing data/docs and this file. Do not infer completion from prior chat prose.
- Commit coherent checkpoints frequently enough that a replacement Work conversation can recover from the repository alone.
- Do not create claims or values merely to fill a gap. Missing or unverified remains missing or unverified.

## Shared research rules

The methodological authority is `docs/research-method.md`, supplemented by section-specific documentation such as `docs/career-codebook.md`, `docs/career-record-format.md` and `docs/data-release.md`.

Across all workstreams:

1. Prefer primary and authoritative sources. Retain the source URL, reference period, retrieved date and definition needed to reproduce a claim.
2. Keep official observations, official forecasts, party proposals/claimed costings, project calculations, causal hypotheses and unknowns distinct.
3. Distinguish sourced facts from calculated or inferred values. Record assumptions for every project calculation.
4. Do not convert missing evidence into zero.
5. Do not silently change an established methodology. If a method must change, update the relevant documentation and explain the effect on prior outputs.
6. Avoid broad formatting/reordering of shared files. Edit only relevant records/functions to reduce merge conflicts.
7. Treat public web pages as sources only when access is permitted. Do not bypass authentication, robots/access controls or site restrictions. Publicly accessible professional profiles may supplement career dates; gated LinkedIn content must not be scraped or bypassed.
8. Preserve enough provenance that another researcher can reproduce or challenge each material result.

## Repository conventions

Current UI code is compact: the page renderers live in `dist/app.js`. Source data/docs live under `data/` and `docs/`; `scripts/build.py` creates `dist/data.js`, mirrors source data/docs into `dist/`, and rebuilds the downloadable source pack.

- `dist/app.js`, `dist/index.html` and `dist/style.css` are currently hand-maintained UI assets.
- Do **not** hand-edit generated `dist/data.js`, mirrored `dist/data/*`, mirrored `dist/docs/*` or `dist/source-pack.zip`. Change source files and run `python scripts/build.py`.
- Run `python scripts/validate.py` after source/data changes.
- Run `node --check dist/app.js` after JavaScript changes.
- Run `node scripts/check-models.cjs` after model/scenario changes.
- Before handing a specialist branch to integration, run every relevant check and record the result in the branch checkpoint.

## Workstream 1 — Economy & productivity foundations

**Branch:** `work/economy-productivity`

**Owns:** views 01–02; `dashboard()` and `learn()` in `dist/app.js`; Australian productivity/living-standard observations and explanatory material.

**Goals:** improve Australian productivity and living-standard evidence; improve output-per-hour/multifactor-productivity coverage where authoritative sources permit; improve household-income context without mixing incompatible definitions/vintages; keep teaching examples separate from forecasts.

**Bootstrap:**

> You are Workstream 1: Economy & productivity foundations for the Policy not politics project. Work only on branch `work/economy-productivity`. Read `docs/work-plan.md`, `docs/research-method.md`, `docs/data-release.md`, inspect current repository state, then continue the scope defined there. Verify completed work from Git. Keep `docs/work-status/economy-productivity.md` current. Do not merge to main or deploy production.

## Workstream 2 — Country comparisons

**Branch:** `work/country-comparisons`

**Owns:** view 03; `countries()` and directly related table/history behaviour; international panel data and definitions.

**Goals:** improve internationally comparable productivity/living-standard evidence; pursue authoritative hourly/multifactor-productivity coverage; add high-value comparison families only when sourced consistently; preserve missingness and reference years.

**Bootstrap:**

> You are Workstream 2: Country comparisons for the Policy not politics project. Work only on branch `work/country-comparisons`. Read `docs/work-plan.md`, `docs/research-method.md`, `docs/data-release.md`, inspect current repository state, then continue the scope defined there. Verify completed work from Git. Keep `docs/work-status/country-comparisons.md` current. Do not merge to main or deploy production.

## Workstream 3 — NDIS & the economy

**Branch:** `work/ndis-economy`

**Owns:** view 04; `ndis()`; NDIS actuals, integrity evidence, workforce mechanisms, funding exposure and carefully scoped fiscal analysis.

**Goals:** keep participant costs/administration/Commonwealth-state/cash-accrual measures distinct; improve integrity evidence without treating detected cases as prevalence; research participant/carer labour outcomes and public-funding employment exposure; avoid attributing a standalone pool of government debt to NDIS.

**Bootstrap:**

> You are Workstream 3: NDIS & the economy for the Policy not politics project. Work only on branch `work/ndis-economy`. Read `docs/work-plan.md`, `docs/research-method.md`, `docs/data-release.md`, inspect current repository state, then continue the scope defined there. Verify completed work from Git. Keep `docs/work-status/ndis-economy.md` current. Do not merge to main or deploy production.

## Workstream 4 — Policy & scenarios

**Branch:** `work/policy-scenarios`

**Owns:** view 05; `scenarios()` and its calculators/model text; dated baseline-versus-alternative policy comparisons.

**Goals:** maintain a dated baseline; map alternatives to explicit changed parameters; improve independent costings/ranges where evidence exists; reconcile implementation/legislation/funding/behaviour assumptions; prevent double-counting baseline savings; present sensitivities rather than partisan forecasts.

**Bootstrap:**

> You are Workstream 4: Policy & scenarios for the Policy not politics project. Work only on branch `work/policy-scenarios`. Read `docs/work-plan.md`, `docs/research-method.md`, `docs/data-release.md`, inspect current repository state, then continue the scope defined there. Verify completed work from Git. Keep `docs/work-status/policy-scenarios.md` current. Do not merge to main or deploy production.

## Workstream 5 — Parliament’s experience

Workstream 5 now has **two levels**:

1. bounded batch research conversations, which create per-member research files only;
2. a Parliament aggregation/UI conversation on `work/parliament-experience`, which integrates completed batches and updates the page.

A Work conversation must **not** attempt to research the full 226-member Parliament.

### Parliament batch allocation

The frozen roster is `data/parliament.json` (retrieved 10 September 2026). Batch definitions are in `data/career-batch-plan.json`. Within each state/territory, roster rows are sorted by `name` and assigned using the documented zero-based half-open slices. Run:

```bash
python scripts/career_batches.py --check
python scripts/career_batches.py --batch <batch-id>
```

The plan currently defines these bounded batches:

| Batch | Branch | Expected members |
|---|---|---:|
| `nsw-1` | `work/parliament-nsw-1` | 20 |
| `nsw-2` | `work/parliament-nsw-2` | 19 |
| `nsw-3` | `work/parliament-nsw-3` | 19 |
| `vic-1` | `work/parliament-vic-1` | 25 |
| `vic-2` | `work/parliament-vic-2` | 25 |
| `qld-1` | `work/parliament-qld-1` | 21 |
| `qld-2` | `work/parliament-qld-2` | 21 |
| `wa-1` | `work/parliament-wa-1` | 14 |
| `wa-2` | `work/parliament-wa-2` | 14 |
| `sa` | `work/parliament-sa` | 22 |
| `tas` | `work/parliament-tas` | 17 |
| `act` | `work/parliament-act` | 5 |
| `nt` | `work/parliament-nt` | 4 |

The expected total is 226. `scripts/career_batches.py --check` is the authority; if it fails, stop and reconcile the roster/plan before research continues.

### Parliament batch ownership

Each batch conversation may write only:

- its assigned member files under `data/careers/members/<person_id>.json`;
- its checkpoint under `docs/work-status/parliament/<batch-id>.md`.

Batch conversations must **not** edit `data/parliament.json`, `dist/app.js`, shared source registers, `docs/career-codebook.md`, aggregate career output files, or another batch's member files. This makes merges almost entirely additive.

Each member record follows `docs/career-record-format.md`. The target is a sourced career timeline plus defensible headline totals for documented full-time public-sector and private-sector employment, with visible exclusions and uncertainty.

### Parliament research discipline

For each assigned member, sequentially:

1. inspect any existing `data/careers/members/<person_id>.json`;
2. research the career using official Parliament material and primary employer/government sources first;
3. supplement dates using legitimately public professional profiles or reliable secondary sources where useful;
4. classify each career spell using `docs/career-codebook.md` and `docs/career-record-format.md`;
5. write the member record, including sources and counting rationale;
6. validate the JSON and commit that member **before researching the next member**;
7. update the batch checkpoint.

A conversation must never hold completed research for multiple members only in chat context. If evidence remains inadequate after reasonable research, commit a `blocked`/partial member record describing what is missing rather than inventing dates or sector classifications.

### Parliament duration rules

- Use source-backed dates and employment status where available.
- Merge overlapping counted intervals before totals; simultaneous roles must not become double-counted full-time years.
- Count only sufficiently evidenced public/private employment in the two headline figures.
- Treat elected office, political staff, party organisations, unions/employer associations, nonprofits, study, unpaid work and unresolved cases separately unless the codebook explicitly establishes the employing entity as public/private employment for headline purposes.
- Classify universities, public corporations, nonprofits and mixed entities using employer control at the time, not job title or funding source alone.
- Do not turn undated occupation lists into years.
- Do not assume FTE fractions where evidence is ambiguous. Keep inferred values distinguishable from directly evidenced values.
- Preserve source URLs and concise coding rationale for every spell.

### Generic Parliament batch bootstrap

Replace `<batch-id>` and `<branch>` from the table above:

> You are a bounded Parliament career-research batch for the Policy not politics project. Work only on branch `<branch>`. Read `docs/work-plan.md`, `docs/career-codebook.md`, `docs/career-record-format.md`, `data/career-batch-plan.json` and `docs/data-release.md`. Run `python scripts/career_batches.py --check` and `python scripts/career_batches.py --batch <batch-id>` to resolve your assigned members. Process members sequentially. Complete, validate and commit `data/careers/members/<person_id>.json` for each member before researching the next. Resume from the first assigned member without a complete/blocked durable record. Keep `docs/work-status/parliament/<batch-id>.md` current. Do not edit shared Parliament UI/data files, merge to main or deploy production.

### Parliament aggregation/UI conversation

**Branch:** `work/parliament-experience`

This branch no longer performs bulk member research. It is the Workstream-5 integration branch. After batch branches report ready, it:

1. verifies `scripts/career_batches.py --check`;
2. merges completed Parliament batch branches;
3. checks that each member has at most one record and records conform to `docs/career-record-format.md`;
4. runs `python scripts/build_careers.py` to create aggregate career outputs;
5. reviews calculation consistency and resolves methodological issues without inventing missing evidence;
6. updates `docs/career-codebook.md` if an aggregation convention needs formal documentation;
7. updates `representatives()` and supporting site data so sourced timelines/headline public/private years are visible;
8. runs relevant validation/build checks;
9. records `docs/work-status/parliament-experience.md` and hands the branch to Workstream 7.

**Parliament aggregation bootstrap:**

> You are the Parliament aggregation/UI conversation for Workstream 5 of Policy not politics. Work only on `work/parliament-experience`. Do not conduct bulk member-by-member research. Read `docs/work-plan.md`, `docs/career-codebook.md`, `docs/career-record-format.md`, `data/career-batch-plan.json` and all `docs/work-status/parliament/*.md`. Integrate only completed Parliament batch branches, run the career aggregation/validation scripts, reconcile methodology, then update the Parliament’s Experience page and its aggregate datasets. Keep `docs/work-status/parliament-experience.md` current. Do not merge to main or deploy production.

## Workstream 6 — Sources & scrutiny

**Branch:** `work/sources-scrutiny`

**Owns:** view 07; `evidence()`; claim/source registers, provenance, reproducibility, correction pathways and release documentation.

**Goals:** audit source quality, retrieval dates and provenance; improve reproducibility/evidence-class labelling; maintain accurate research gaps; make corrections symmetric across parties and claims; perform a final pass after other specialist work is ready.

**Bootstrap:**

> You are Workstream 6: Sources & scrutiny for the Policy not politics project. Work only on branch `work/sources-scrutiny`. Read `docs/work-plan.md`, `docs/research-method.md`, `docs/data-release.md`, inspect current repository state, then continue the scope defined there. Verify completed work from Git. Keep `docs/work-status/sources-scrutiny.md` current. Do not merge to main or deploy production.

## Workstream 7 — Integration, QA & release

**Branch:** `work/integration-release`

**Owns:** cross-stream integration, conflict resolution, site-wide consistency, build/validation, merge to `main`, GitHub Pages deployment and production verification.

Responsibilities:

1. inspect `main`, specialist branch heads and checkpoint files;
2. merge one validated site-level workstream at a time;
3. reconcile shared-file changes while preserving domain work;
4. run `python scripts/build.py`, `python scripts/validate.py`, `node --check dist/app.js`, and `node scripts/check-models.cjs`;
5. review every navigation route and important interactive control;
6. update release/coverage language to match what actually ships;
7. merge/push to `main` only after checks pass;
8. verify the GitHub Pages workflow and inspect the deployed site;
9. leave inadequate/incomplete specialist work unmerged rather than manufacturing a resolution.

The site integration stream should not become another domain research conversation. Parliament batch branches should first be consolidated through `work/parliament-experience`; Workstream 7 integrates that consolidated Parliament branch, not thirteen research branches individually.

**Bootstrap:**

> You are Workstream 7: Integration, QA & release for the Policy not politics project. Work only on branch `work/integration-release` until an explicitly validated release is ready. Read `docs/work-plan.md` and available work-status files, compare completed site-level specialist branches with `main`, then integrate only validated workstreams. Run the full build/model/JavaScript validation suite, update release notes, merge the validated release to `main`, verify the GitHub Pages workflow and inspect the deployed site. Do not perform substantial domain research inside this integration conversation.

## Checkpoint contract

Each specialist/batch branch maintains its own status file. Site-level branches use `docs/work-status/<slug>.md`; Parliament batches use `docs/work-status/parliament/<batch-id>.md`.

Use this concise structure:

```markdown
# <Workstream or batch> status

Last updated: <ISO date/time>
Branch: <branch>
Branch HEAD: <commit SHA after checkpoint commit, or PRE-COMMIT while preparing>
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

When any Work conversation reaches maximum length, start a successor inside the same Project with only the relevant bootstrap prompt. The successor must inspect its assigned branch/status file, verify commits, load only files relevant to the next incomplete task, and resume from `Next action`.

For Parliament batches, durable progress is **one committed member at a time**. A replacement conversation starts from the first assigned member without a complete or explicitly blocked per-member record.

## Cross-workstream dependency rule

Do not ask specialist conversations to read one another’s full chat histories. Communicate dependencies through committed data/docs or concise checkpoint notes. The repository carries durable facts and decisions; conversations carry temporary working context.

## Suggested launch order

Site-level workstreams 1–4 and 6 can run in parallel with the Parliament batches. Parliament batches can also run in parallel because their file ownership is disjoint. Run the Parliament aggregation/UI conversation only after at least one batch is ready and preferably after all batches are complete. Run the site integration/release conversation after one or more site-level workstreams are ready, and again for the final release.
