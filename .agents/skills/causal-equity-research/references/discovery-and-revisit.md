# Discovery, advancement and revisit decisions

This implementation revision follows the user's 2026-10-28 feedback and v2 sections 0–7, 12–15, 19–24. It changes scheduling and research decisions, not the default investment objective or the original gates. A research priority is not an investment rank.

## Compare opportunities before perfecting accounts

Start with changing customer needs and market potential. Split broad themes into economically distinct applications, products/grades, customer cohorts, geographies and bottlenecks; then expand one edge outward to suppliers, substitutes, infrastructure and less obvious beneficiaries. For example, an accelerator cluster can expose separate markets for optical modules, lasers, DSPs, fiber, switching, memory, packaging and power. These are search directions, not automatic investment picks. Seek unrelated pools too, within the mandate. A small high-value constraint can matter more than a large headline TAM.

O00 runs the following funnel. Work can overlap across markets; depth follows the decision, not a universal serial document queue.

| Stage | Minimum useful result | Decision and next work |
|---|---|---|
| Discovery | Source-linked change, affected customer/job, market segment, feasible alternatives, named value-chain exposures, why forward economics could differ | Open a route, exclude it with evidence, or record a missing discriminator. No DCF or full filing census prerequisite. |
| Comparable screen | Opportunity card below, next-quarter/half/year direction, rival response, rough financial transmission and conditional expectations test | Compare all covered routes at the same depth before deepening a favorite. Keep incompatible return mechanisms visible. |
| Mechanism sprint | Resolve one or a few decisive unknowns, quantify threshold/sensitivity, obtain independent counter-case | Advance, defer with a reopen condition, or reject an evidenced premise. Recompare the frontier after each sprint. |
| Finalist diligence | Accepted customer/supply/share path, full scoped disclosures, statements, valuation, recognition and independent review | Adjudicate all 25 gates. Publish a strict eligible ranking or an expressly authorized provisional judgment with limitations. |

For a broad search, preserve the v2 planning breadth of 12 pools/about 60 names/about six finalists, adjusted transparently to scope. Before a full multi-year issuer reconstruction, produce the comparative screen for the agreed discovery breadth. If a time-sensitive event or data access justifies an exception, O00 records the exception and the uncompleted breadth. A solvency or identity check can occur immediately; it must not become a general current-FCF filter.

Default execution cadence: one bounded initial evidence batch per pool; then comparable opportunity cards; then normally one mechanism sprint per advancing route before a second sprint on one issuer. Batch size and sprint length belong on the task card. O00 can depart when one fact is decisive, but records why the next call beats another route or a revisit. This is a scheduling default, not a fixed call quota.

## Opportunity card

Use the same compact fields for every screened route:
- `route_id`, market/application/grade, company exposures and mandate fit; evidence depth and source/claim IDs.
- Customer job, incremental value versus best feasible alternative, purchase/integration/switching burden, who pays, and supplier ability to capture value.
- Structural change or transient shock; next quarter, six months, twelve months and normalized direction; demand, qualified supply, inventory and price mechanism separately.
- Candidate advantage/erosion; funded adoption and rival response; existing versus new customers.
- Present growth and hidden improvement: what restrains weak/flat/ordinary performance; what is changing beneath the headline; when the restraint eases or a threshold is crossed; incremental earnings/cash potential and evidence against recovery. If none is supported, state the examined cause and why it persists.
- Plausible earnings/cash transmission, required investment and funding/dilution. Use bounded ranges or break-even thresholds for screening; do not invent a precise early target or arbitrary PE.
- Current-price requirement or an explicit `VALUATION_NOT_YET_TESTED`; possible information event and reason pessimism could be justified. Missing price work is a next task, not a negative conclusion.
- Strongest counter-case, decisive unknown, cheapest discriminating source, advance/defer/reject reason and revisit record.

Historical financials anchor costs, funding and current conditions. They do not define the future opportunity. Neither high current PE, low current FCF, a cautious management outlook, nor lack of an exact private contract alone disproves an economically supported future path. Conversely, growth or attractive technology does not excuse funding gaps, dilution or implausible value capture.

### Discover the turn before selecting reported growers (v2.4)

A03 examines both strong reported growth and depressed/ordinary economics in each relevant market pool. Search from underlying states: funded demand versus underused capacity; orders versus delayed acceptance; gross contribution versus launch spending; improving segment/cohort economics versus a flat total; expiring cost vintages or contracts; learning and replacement cycles. A12 can perform an early bounded cause bridge for a promising anomaly without starting a full issuer reconstruction. A19 dates the removal of the restraint or threshold crossing; A08/A09/A18 test whether product/customer economics support it.

O00 compares these routes on forward incremental profit/cash, funding, competitive duration and horizon recognition. Do not require positive current earnings, accelerating headline growth, an already reported recovery or a formally announced catalyst as an admission rule. Keep the strongest evidenced adverse explanation alongside the improvement path. There is no quota for turnaround names and no presumption of mean reversion. Record the actual weak/ordinary routes examined and their causal disposition; a generic statement that reversals were considered is insufficient.

## Revisit queue and state transitions

Keep canonical candidate states `DISCOVERY`, `DILIGENCE`, `WATCHLIST`, `REJECTED`, `ELIGIBLE`. Add `stage`, `decision_reason`, and `revisit` rather than treating every unfinished case as rejected. An authorized provisional opinion is a publication label, not a fabricated `ELIGIBLE` state.

For every promising deferred route record:

```text
route_id; current_state; last_review_at; premise_and_version
reason: missing_evidence | timing | valuation | funding | contradicted_mechanism | mandate
decision_evidence_ids; unresolved_parameter; affected_nodes
next_discriminator; owner_role; bounded_next_task
reopen_trigger: observable event/threshold/source or a dated review checkpoint
trigger_status: pending | met | not_met | unknown
expiry_or_review_at; invalidation_trigger; opportunity_cost_reason
```

Missing evidence uses WATCHLIST, not REJECTED. Rejection requires an evidenced failure or mandate exclusion with scope and conditions; a future change can reopen it. A known event with unknown outcome remains pending. Do not invent certainty or continuously retry an inaccessible source.

O00 reviews the queue at each frontier comparison, after a relevant new source or shared-node change, and before concluding that no candidate is attractive. A23 checks whether early screens discarded high-upside routes for shallow evidence, stale inputs or a single pessimistic assumption. A price change can reopen valuation work without rewriting the business; a competitor qualification can reopen business work across multiple issuers. No scheduled monitoring is implied: pending triggers are checked during authorized research/resumption only.

Use the event-to-route dependency map in [evidence-memory.md](evidence-memory.md). Reopen only affected questions, preserving accepted unaffected work. Do not repeat full diligence or recycle failed speculative paths without a new discriminator. Report the best open routes, why they are open, and what would change the decision.

## Early and final cross-validation

Commission independent first passes with raw cutoff-legal evidence, not the favored name/target or peer conclusions. Early work challenges market opportunity and customer/supply mechanism before detailed accounts. Later work challenges the integrated statements and price bridge. Shared primary documents are shared evidence origins even when conclusions are independently derived.

The inner loop tests technology → customer incremental value → adoption/share against wins, losses, retention, usage and rival behavior. The outer loop tests funded downstream demand → qualified supply/inventory → price/cost → future company earnings and cash. Divergence returns to the responsible mechanism; neither a DCF nor an arbitrary multiple resolves it.

O00's final decision records why remaining routes were less compelling or insufficiently established. An incomplete route is not a proven loser. Compare forward economics and horizon recognition before authorizing more accounting refinement.

## v2.2 reversal search

Apply `forecast-commitment-and-causal-audit.md`. The comparable frontier explicitly considers poor/flat reported performance with a dated improvement mechanism as well as continuing growth. Record the underlying cause, expected removal/threshold, incremental earnings/cash and recognition date. Do not merely extrapolate weak results or demand that a recovery already appear in reported accounts. A route cannot be rejected solely because a supported future assumption is uncertain; a structural failure cannot be called temporary without evidence.
