# Codex orchestration contract

## Runtime and ownership

O00 is the primary GPT. It owns the mandate, task DAG, source registry, accepted model versions, gate decisions and final ranking. Use `causal_a01`–`causal_a23` as defined in the project `.codex/agents/` directory. Omit model overrides so workers inherit the active GPT model and reasoning setting. These role files are also usable as prompt contracts if the current session has not loaded new custom agents: send the exact role instructions to a fresh `default` worker and log the fallback. Never substitute an old equity role with a conflicting methodology.

Normally run two workers; allow three prerequisite-ready independent tasks within the runtime cap. This is a local scheduling choice, not a research sufficiency rule. There is no fixed total-call quota. Roles may be called repeatedly for different coherent markets, source batches, issuers and periods. Do not ask one worker to research the entire universe. Workers cannot delegate. When a worker finishes, collect its packet and release it with the available lifecycle tool; if no close tool exists, leave it inactive and do not claim closure. Reuse context only for narrow follow-ups that do not require independence.

Workers return proposed deltas and never edit canonical files. O00 verifies each delta before writing. Gate owners recommend decisions; O00 records reviewer evidence and accepts or rejects. A16 numerically checks independently of the model builder. A15 first sees the causal thesis and sources without a favored target/rank, then performs a full-view comparison after its initial critique freezes.

## Task card issued before each call

```text
task_id: unique run-local instance; checklist_ids: [Txx, ...]
role: Axx; agent: causal_axx; run_id; candidate_ids; market_ids
question: one decision-relevant question
stage: discovery | comparable_screen | mechanism_sprint | finalist | update | workflow_test
decision_to_unlock; route_id; existing_library_snapshot; revisit_trigger_if_deferred
method_version; source_snapshot; cutoff_utc; forecast_lane
scope: product/grade, geography, cohort, period, units, currency, share basis
required_inputs: accepted artifact IDs, versions and hashes
source_scope: required documents/sections and permitted discovery families
permitted_partitions; excluded_partitions; excluded_peer_outputs
allowed_tools; verified_access_controls; independence_status
required_outputs; equations/units; blocking_gates; affected_nodes
effort_budget: bounded question/search batch; stop conditions
receiver; reviewer; acceptance_conditions
```

Fresh independent passes use `fork_turns="none"` and a frozen input packet that contains no peer conclusions or favored target. Instructional independence can prevent anchoring; it cannot enforce a sealed historical test. Do not describe two GPTs using one press release as two evidence origins. Use separate-source cross-checks where the specification requires them. Commission additional replicas when a disputed decisive calculation or discovery omission could change eligibility or ranking; the new sources do not require universal paired calls for every task.

## Scheduling waves and acceptance

At wave 1/1B use [frontier-tech-events.md](frontier-tech-events.md). O00 checks which independent demand pools and neglected exposures were actually compared before assigning a repeat diligence sprint; dispatch an early clean A08 pass if product/process evidence could change admission or deferral. A14/A01 reconstruct a material price event before accepting a story about investor beliefs. Record tested, unavailable and unsearched evidence separately. These receiver checks change research priority; no new publication gate or automatic rank follows.

Read `discovery-and-revisit.md` for admission, comparison cadence and revisit records, `business-dynamics-and-turns.md` for economic handoffs, and `evidence-memory.md` for reuse. The table is a dependency map, not a requirement to complete every company's accounting before examining forward opportunities. O00 publishes a comparative frontier after each discovery round and mechanism sprint.

The catalog IDs are source checklist labels, not chronological execution order. Later v2 tasks often precede earlier financial/valuation tasks.

When instantiating T03, apply the reset override in `source-map.md`: exclude retired assistant material rather than extracting its claims as leads. Record the override on the task card. Distinguish the research `work_mode` from `data_mode` (`LIVE`/`SYNTHETIC`); the normalized validator consumes the latter.

| Wave | Roles and work | Required acceptance before dependent work |
|---|---|---|
| 0: mandate and validation design | O00 locks scope; A01 checks quote/calendar; A20 preregisters protocol; A22 inspects access/lineage | G00; G01 as prices are obtained; G19 protocol; explicit G18/G20 feasibility record |
| 1: broad discovery | A02 macro channels; A03 decomposed and unrelated market pools; A04 chain/unit maps; A23 library lookup/coverage | Source-linked hypotheses, comparable opportunity cards and open routes; no completed valuations claimed |
| 1B: admission and forward comparison | A05/A06 demand/supply sketches; A08/A09/A18 customer-value thresholds; A19 forward states; A13/A14 initial expectation/turning-point hypotheses; A23 comparison/revisit | Next-quarter/half/year mechanism, strongest counter-case and a useful discriminator before full issuer reconstruction. Research admission passes no final gate. |
| 2: scoped evidence, expanding with depth | A17 inventory/census for declared scope; A01 claims/diffs; A22 as-of versions; A23 missing evidence | G02/G16/G18 for dependent input sets; full finalist corpus before final publication. Material unknowns block dependent conclusions, not unrelated discovery. |
| 3: independent mechanism research | A08 technical dossier; A06 supply/projects; A05 customer deployments; A11 incentives | Accepted matched technical inputs, source-backed supply/customer records, identified unknowns |
| 4: customer choice and clearing | A09 lifecycle TCO; A18 cohort choice/adoption; A05 final demand; A07 pricing; A11 actions; A19 dynamic reconciliation; A10 constrained share | G03–G08, G15/G17/G21; no share output before necessary customer/supply evidence |
| 5: accounts and forecasts | A12 reconstructs historical financials and driver forecasts; A16 ties out; A15 tests both causal loops; A19/A23 forward-factor sweep | G09/G10/G17/G21; factor dispositions before model/input/prompt/forecast lock; no target solving through EPS |
| 6: evaluation | A20 locked protocol; A22 feature boundary; A21 evaluator-only scoring when feasible | G19/G20/G22/G24 evidence; disclose contamination and incomplete prospective outcomes |
| 7: final recognition and price | A14 refines early information map; A13 business/belief separation, fixed-year valuation and cash cross-check | G11/G12 with accepted operating model, appropriate validation posture and dated incremental recognition route |
| 8: adversarial review and publication | A15 counter-model; A16 numerical/comparability audit; A23 sufficiency; O00 candidate gate adjudication | G00–G24 reviewed globally and per candidate; only all-pass candidates enter ranking |

Discovery can proceed while validation feasibility is unresolved; no dependency may pretend the unresolved gate passed. A preliminary supply/price hypothesis may orient technical/customer research. Final pricing, adoption and share must be solved together using accepted inputs. Feedback opens a new artifact version and rechecks affected gates. Report non-convergence or underidentification instead of inventing elasticity.

## Role boundaries that prevent duplicated models

- A01 verifies source authenticity/chronology; A17 inventories and extracts the declared corpus; A22 checks recursive availability and actual access controls; A23 decides the next useful evidence question.
- A08 owns matched technical performance and system resource inputs; A09 owns lifecycle dollar economics; A18 owns choice, affordability and deployment intersections. Supplier value capture is resolved with A07, not assumed from customer surplus.
- A05 owns consumption/procurement; A06 qualified output; A07 contract/price formation; A11 actor incentives/actions; A19 time-state integration and shock transmission; A10 final share allocations.
- A12 owns financial statements, operating forecasts and diluted share counts; A13 owns investor beliefs and price mapping; A14 owns the information clock. They cannot alter upstream assumptions to reach a desired target.
- A20 designs and freezes evaluation; A21 scores; A22 controls access where enforceable. Model developers do not receive hidden labels or interim test-error feedback. A15/A16 challenge evidence and arithmetic; O00 decides.

## Packet acceptance and versioning

The universal packet fields are specified in source section 24.1 and repeated in worker configurations. Status is `COMPLETE`, `BLOCKED` or `NEEDS_REVIEW`. O00 serializes a packet deterministically, computes its SHA-256, and records the artifact path, returned status, sources actually read and receiving reviewer. A hash identifies bytes; it proves neither truth nor immutable storage.

For every handoff, check cutoff/versions, definitions, source origins, classification, formula lineage, physical constraints, parameter sensitivity and whether the assigned question is answered. Reject inadequate handoffs to their owning role. Preserve incompatible historical facts and block affected factual claims until resolved; never average them. For unknown future outcomes, apply v2.2: O00 chooses a supported continuation/transition assumption and completes the provisional forecast, retaining the strongest alternative as a separate stress.

Maintain task states `QUEUED`, `READY`, `RUNNING`, `RETURNED`, `ACCEPTED`, `REWORK`, `BLOCKED`. A returned COMPLETE packet becomes ACCEPTED only after the receiver's review. Candidate states are `DISCOVERY`, `DILIGENCE`, `WATCHLIST`, `REJECTED`, `ELIGIBLE`. Missing research is WATCHLIST with an exact question; REJECTED requires an evidenced exclusion/failure.

Each deferred promising route also has the trigger, review checkpoint, affected nodes and bounded next task specified in `discovery-and-revisit.md`. At a new accepted source, frontier comparison or resumption, A23 checks which triggers are met; O00 queues only affected work. No background polling is implied. A rejected premise can be reopened by a relevant changed fact; unrelated positive headlines do not qualify.

Instantiate all G00–G24 for every finalist with status `NOT_STARTED`, `NEEDS_REVIEW`, `BLOCKED`, `FAIL` or `PASS`, evidence IDs, reviewer, version and time. A global readiness row cannot substitute for candidate evidence. A claimed non-applicable gate needs a preregistered scope decision and remains unpassed until the source-defined requirement is met or the user explicitly changes the mandate; do not create a silent waiver.

Use run-local append-only versions for mandate, DAG, ledgers, forecasts and decisions. Recommended records: `mandate.json`, `tasks.json`, `sources.jsonl`, `claims.jsonl`, `documents.jsonl`, `census.jsonl`, `vintages.jsonl`, `graph.json`, `models/`, `packets/`, `receipts/`, `gates.json`, `decision.md`. These paths are organization, not access security. Never put sealed labels in a shared run folder.

## Research budget and stop rules

Plan full broad discovery around 12 pools/about 60 names/six comparable finalists, then allocate each call to a coherent question. For narrow mandates, record the explicit narrower scope. Preserve screened and rejected names. Do not pad counts, batch unrelated finalists to fit an inherited ceiling, or assume equal document counts imply equal diligence.

A23 prioritizes major operating-direction changes, a route's plausible material upside mechanism, decisive contradictions and the cost of resolving them. Before targets exist, use these causal questions rather than fabricated target sensitivities. After modeling, add eligibility changes, rank reversals and material target changes (default 3 percentage points). After each bounded sprint, recompare advancing and deferred routes before extending one issuer. Stop repeating one-origin searches; log dead ends and the next discriminator. Safe independent work may continue while one candidate is blocked.

## Allocating the next call

For a repeat diligence sprint or the decision to end broad search, compare the best use of one more call on the current route with the strongest challenger (including an unexamined market when allowed). Name **the economic decision that could flip**, as specifically as the evidence permits: which customer/cohort would switch, which constraint binds, who keeps the contribution, or what investors can learn by the horizon. State the best competing explanation, the finding that would separate them and its consequence in either direction. Use a bound when possible; a larger number that leaves the decision unchanged is not a discriminator. Separate when the business changes, when evidence becomes public, and when it can change the investment judgment. An aggregate result or later formal release is not a substitute for checking whether a timely component, contract or counterparty source can already discriminate.

A23 identifies an accessible source (or lack of one), cost and affected routes. O00 assigns the bounded question to the role that owns the disputed link. Choose the consequential timely check over repeated confirmation. The best action can also be to wait or stop: competing answers may imply the same disposition, a feasible upper bound may rule it out, or genuinely new evidence may first arrive later. Keep the affected premise and dated reopening condition. If actionable work remains but resources actually end, report that part of the search as unfinished; don't reclassify opportunity cost as adverse business evidence. No forced reversal, specialist call, target or assertion of missing evidence from an unsearched source.

For **broad search only**, include the latest comparison in the existing normalized workflow packet at both checkpoints. Run `scripts/validate_workflow.py <packet> --frontier` before repeat dispatch and broad closeout; retain each dated decision in the run. `frontier` has a timezone-aware `reviewed_at`, `checkpoint` (repeat or close), `choice` (work, wait, stop or budget), `reason`, and `options`: an entry per compared question with unique `id`, `question`, `source_or_limit`, `decision_effect` (the two implications, or the bound), and `state`: **actionable** (a feasible cutoff-legal check could change the decision), **invariant** (no plausible answer changes it), or **unavailable** (no timely observable discriminates). For work, set `selected` and link a queued/ready/running `task_id` carrying that `frontier_option_id`; for wait give `reopen`; if fewer than two distinct options can be compared explain `comparison_limit`. Budget close records the unfinished search component under partial/blocked delivery. The check catches contradictory declarations; O00 must judge whether the compared questions were the strongest and the evidence supports their labels. Do not reconstruct decisions after the fact. Single-issuer or attribution work needs no artificial competitor queue.

## Delivery and resumption

Full research returns the dossier described in specification sections 16/25 and Appendix F, with one eligible price path and separate sensitivity/risk disclosures. If no candidate qualifies, publish the strongest open routes, blocking questions and coverage limits. Do not equate an incomplete search with proof that every stock fails. Explicit user permission for a provisional selection is recorded once in the run mandate and persists for that run; use the separate publication posture in `validation.md` rather than asking again or claiming strict eligibility.

An update versions the changed source, invalidates dependent nodes and gates, recomputes only affected work, and explains every target/rank change. A request to create this skill is not a request to launch research or monitoring. A future research request authorizes its ordinary in-scope evidence gathering and local outputs; no repeated permission is needed for those steps.

## v2.2 forecast acceptance

Use `forecast-commitment-and-causal-audit.md`. Add `unknown_type`, `chosen_path`, `anchor_ids`, `selection_reason`, `transition_date`, and `falsifier` to material assumption handoffs. A12 adds metric cause/forward dispositions including flat lines and reversible weakness; A05/A06/A07/A19 add local usable-buffer, constraint-date and price-response reconciliation. A13/A14 return a horizon price forecast separately from intrinsic value. Rank sensitivity alone does not reject an anchored provisional path. Hard factual contradictions, physical impossibility and absent indispensable evidence retain their existing gates. Do not load peer conclusions into independent first-pass packets.

## Economic reconciliation before valuation (v2.4)

At comparable screening, A03/A12 bring forward weak or ordinary metrics with an evidenced improving mechanism, as well as reported growers. O00 checks that these routes were actually examined before commissioning more refinement of current leaders. Use discovery-and-revisit.md; no full-accounting prerequisite or forced recovery quota.

Independent first passes remain free of peer conclusions. After they freeze, O00 compares their decision-driving inputs on the same period and accounting basis. Reconcile differences into demand/volume, price/mix, cost, cash, capital claims and recognition. Send the owning role one bounded discriminator, then choose the best-supported operating path; preserve the rejected alternative and reason. Do not average incompatible paths, leave both unadjudicated in the final decision, or let A13 silently invent a third business model.

Receiver acceptance concerns the requested economics: A19 returns populated market states and transition calculations; A12 returns financial cause bridges plus their forward effects; A13 consumes that accepted operating path and A14's forecast of incremental information. Discovery maps, accounting normalization and break-even hurdles remain useful narrower outputs, but do not complete those forecast tasks. Where a decisive link lacks any defensible anchor, state the exact incomplete component and retain the route; ordinary forecast uncertainty is not that condition.

A15 checks symmetry: are adverse normalization and positive recovery both justified by cause, scale and timing? A16 checks remaining-period implications of annual inputs, comparable definitions, and whether advances/operating reserves are already reflected in forecast cash requirements. O00 resolves these before using valuation to conclude that upside is inadequate. Risk sensitivity is disclosed separately from selection of the central path.

## Acceptance scope and completion (v2.3)

Keep task `status` in the declared state vocabulary. Record accepted use separately in `accepted_scope` (for example discovery, causal input, accounting tie-out, operating forecast, or horizon forecast), with accepted artifact version/hash, limitations and reviewer. Every dependent task states the input scope it requires. A discovery-only COMPLETE/ACCEPTED packet cannot satisfy an operating-forecast prerequisite. Mark READY only after the required version and scope are accepted; an exploratory task may instead explicitly return a hypothesis.

Before extra refinement, compare frontier/revisit tasks by the decision they unlock and prerequisite readiness. Preserve the approved breadth or record the specific time-sensitive exception. At the end distinguish `work_completed`, `requested_deliverable`, `deliverable_status=COMPLETE|PARTIAL|BLOCKED`, and each missing component with owner/next evidence. A conditional value or completed research session cannot be labeled a completed horizon prediction. State partial completion plainly without withholding the usable findings.

Adjudicate gates with gate-specific evidence and an action for the failed dependency. Shared issue IDs may recur, but do not paste one candidate-wide generic concern into every unrelated gate. Graphs must link accepted claim versions to model outputs, gate decisions and revisit routes; a drawing of industry connections alone does not automate invalidation.

Before advancing or deferring a route, record a bounded latest-material-release check, its source and cutoff. A route links its actual opportunity-card version, and revisit records include trigger status, last assessed evidence, a dated or uniquely identified comparison checkpoint and next bounded task. Do not count an old accepted task as a pending revisit.

G19 tests whether the required protocol was preregistered; G20 tests forecast locks and completed scoring. A sufficient protocol can pass G19 while future outcomes leave G20 unpassed. Do not make protocol completion depend on an outcome that has not happened. These are distinct predicates, not a relaxation of strict-ranking eligibility.

Use scripts/validate_workflow.py on the normalized readiness/completion record before dispatching dependent work and before final delivery. Its --example describes the interchange. It checks declared scope/version acceptance, task cycles, peer-conclusion exclusion, revisit actions and output-type completeness. It does not authenticate evidence, hashes or complete runtime execution; disclose missing trace fields rather than invent them.
## Discovery through valuation

Apply at discovery, first disposition and publication, not as an after-the-fact narrative. The original gates still govern. O00 owns the following reconciliations:

1. **Keep the original field in view.** Freeze a dated inventory from the union of a contemporaneous directory (including listings since its vintage) and an independent procurement/value-chain search before narrowing. Partition requested themes by buyer, application and distinct bottleneck. Widen into unrelated opportunities without replacing the requested field. Keep off-exchange peers as evidence only when the mandate excludes their securities. Never seed discovery from former rankings. Add later discoveries through a dated, linked inventory revision, retaining existing IDs. Record where enumeration could be incomplete.
2. **Explain each subtraction.** At broad close reconcile every material route in that inventory with a model, an evidence-backed bound or contradiction, a true timed wait, a comparator role or owned unfinished research. Include the strongest still-researchable route beside the marginal admitted one under comparable assumptions. A future report alone cannot justify waiting when a present filing, customer annex, capacity schedule or technical comparison can already discriminate. Dispatch it or label the coverage partial with the question and owner. Sector counts and lists of names are not dispositions. Summarize missing coverage in the user-facing conclusion; distinguish “not researched” from “unattractive.”
3. **Show where the market clears.** Before a balance claim moves a route in or out, A05 and A06 estimate funded end consumption and usable, qualified supply independently. A07/A19 reconcile them by grade, location and delivery period: starting usable stock, withdrawals/additions, reserve, allocated deliveries, ending usable stock and unserved orders or idle slots. For non-storable services use funded jobs, qualified service hours, queues and cancellations instead. Distinguish pushed shipments, inventory, take-or-pay and double orders from consumption. Include buyer inventory release/substitution, rival qualification and supplier production response at feasible prices. Carry one consistent path across next quarter, half and year; do not sum overlapping windows. Change one demand input and one supply input separately: trace the first affected output through contract reset, allocated units/ASP, incremental cost, share, profit and cash when material. A calculated bound suffices for early triage; if the sign or advancement can still flip and evidence is obtainable, return the work. Retain limits when a grade split or price elasticity is unknown; a headline shortage does not set ASP.
4. **Separate the operating and share-price tests.** A13/A14 freeze the independently supported cutoff belief, reference quote, share count, fiscal denominator and capital/distribution assumptions. A16 replays an improvement and its mirror holding that origin fixed, identifying what new information can reach investors before T. Then hold economics fixed and change only the quote/recalibration. Separate changed operating value, multiple or duration, carry, cash and dividends; do not count a cash flow twice. If P0 divided by the revised private forecast is multiplied by that same forecast at T, it cancels. Use quote carry solely to benchmark the locked forecast. Where little in-window change is expected, value the independently supported business and belief path and explain the resulting return. Use the user’s [quantitative research and execution contract](quantitative-market-research.md) for acceptance. A fixed consideration conditional on close, a binding hedge, or unused capacity can legitimately absorb a shock; document the binding term/window and where the shock still appears. Keep deal-break/approval risk separate. If timing or beliefs cannot be identified, state the actual assumption/bound instead of inventing a multiple or promising a large return.

**Machine check for broad closeouts.** Store the pre-narrowing book separately as UTF-8 JSON: `{"routes":[{"id":"…","source":"…","investable":true,"check_now":"…"}]}`; omit `check_now` only when no specific cutoff-available discriminator has been identified. O00 receipts the exact bytes/SHA-256 at discovery, checks provenance, and preserves later versions. The close packet's `frontier.coverage` has one record per book ID: `id, disposition, basis` and, for an available check resolved, `check_evidence`; `wait/open` also require `owner,next`. Dispositions: `modeled,bounded,contradicted,wait,open,evidence_only`. Evidence references must actually answer the question; syntax cannot prove that. Run `validate_workflow.py PACKET --frontier --route-book BOOK --book-sha256 DISCOVERY_RECEIPT_HASH`. Do not derive the expected hash from a rewritten close-time book. Only a partial/budget close may leave an actionable route open. A receipt in a shared workspace is not an access-control or completeness guarantee.
