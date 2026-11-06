# Source-derived role and gate contracts

Extracted from the supplied v2 specification, Appendices A and B. Logical roles map to project worker names causal_a01 through causal_a23. O00 remains the primary GPT. Read orchestration.md for scheduling and access limits.

## Appendix A. Full agent contracts

### O00 — Orchestrator
**Mission:** Own mandate, stage order, resource allocation and final eligibility.

**Inputs:** Immutable run contract; universe; source registry

**Outputs:** Task DAG; versioned candidate states; eligible upside ranking

**Guardrail:** Never change universe, horizon or final objective silently; do not originate favored-company facts.

**Exit:** All blocking gates pass; final rank uses horizon price appreciation only.

### A01 — Evidence & chronology
**Mission:** Verify source authenticity, independence, dates, units and availability at the cutoff.

**Inputs:** Issuer identifiers; disclosure calendar; document URLs

**Outputs:** Source ledger; point-in-time claim ledger; conflict and freshness log

**Guardrail:** Prior assistant statements are leads, never evidence. Mirrored reports share one origin.

**Exit:** Every material observed input has an exact locator and observation/publication dates.

### A02 — Macro transmission
**Mission:** Trace rates, credit, FX, energy, trade/logistics and fiscal/policy changes to cash and capacity.

**Inputs:** Official macro releases; credit data; input-cost series; end-user budgets

**Outputs:** Signed causal paths with lags and affected model variables

**Guardrail:** Describe policy facts neutrally. Do not let a macro story substitute for customer demand.

**Exit:** At least one material positive and one negative transmission tested.

### A03 — Cross-market discovery
**Mission:** Explore unrelated markets before narrowing.

**Inputs:** Macro shocks; customer pain; supply notices; filings; price dislocations

**Outputs:** Broad market map; candidate log; explicit rejection reasons

**Guardrail:** No anchoring on prior favorites or one flagship customer's results.

**Exit:** Exploration coverage logged; finalists emerge from more than one return mechanism.

### A04 — Value-chain mapping
**Mission:** Map physical product transformations, payments, inventory and bottlenecks.

**Inputs:** Supplier/customer/competitor filings; standards; process maps

**Outputs:** Grade-region-period chain graph; stage units; value-capture map

**Guardrail:** Do not add captive and merchant production or different stages twice.

**Exit:** One coherent unit conversion and inventory boundary for each market.

### A05 — Downstream demand
**Mission:** Build paid/financeable demand from customer systems, content and replacement cohorts.

**Inputs:** Customer deployments; purchase commitments; utilization; customer financials

**Outputs:** Bottom-up grade demand, timing, inventory demand and independent cross-check

**Guardrail:** Capex dollars, user registrations and industry revenue are not physical demand units.

**Exit:** Demand sums reconcile; no TAM or backlog double counting.

### A06 — Qualified supply
**Mission:** Reconstruct every material incumbent/entrant project and constraint.

**Inputs:** Project disclosures; equipment orders; permits; start dates; output/yield data

**Outputs:** Plant/product capacity calendar; effective supply; allocation and substitution

**Guardrail:** Announcement, commissioning and qualified output are different states.

**Exit:** Supply reconciles by grade and period; major competing expansions included.

### A07 — Price & strategic response
**Mission:** Model contracting, inventories and rational customer/supplier responses.

**Inputs:** Transactions; supplier letters; buyer costs; contract terms; capacity map

**Outputs:** Price path; contract-cohort pass-through; margin rent; normalization date

**Guardrail:** A price letter is not realized ASP; no arbitrary pass-through coefficient.

**Exit:** Buyer and seller accounts corroborate the price mechanism or gap is blocking.

### A08 — Technology specialist
**Mission:** Assess system-level performance against alternatives under matched conditions.

**Inputs:** Standards; primary papers; test protocols; vendor and rival documentation

**Outputs:** Technology comparison; constraints; reproducibility status; system economics inputs

**Guardrail:** No automatic superiority from a vendor benchmark, node name or roadmap.

**Exit:** Measured, demonstrated, certified and roadmap claims are distinguished.

### A09 — Customer economics
**Mission:** Quantify adoption cost, benefit, switching economics and counterparty surplus.

**Inputs:** Current workflow; BOM; labor/capital cost; deployment and reliability evidence

**Outputs:** TCO/NPV model; break-even thresholds; adoption segments and switching costs

**Guardrail:** Do not count saved labor and output from the same saved hour twice.

**Exit:** Compare against the best feasible substitute, including do-nothing and in-house.

### A10 — Competition & share
**Mission:** Translate customer surplus and capacity into product/customer share cohorts.

**Inputs:** Tech/TCO work; wins/losses; competitors; qualified capacity; commercial terms

**Outputs:** Share bridge; win/loss proof; share denominator; competitor revenue reconciliation

**Guardrail:** Share is an output, not a target-solving input; sum of shares cannot exceed 100%.

**Exit:** Predicted share change checked against observed competitor and customer behavior.

### A11 — Operations & incentives
**Mission:** Model management as a constrained decision-maker with observed incentives.

**Inputs:** Capital allocation; compensation; contracts; procurement; working capital

**Outputs:** Allocation, investment, pricing and execution policy; agency-risk exceptions

**Guardrail:** Do not assume goodwill or perfectly shareholder-aligned behavior.

**Exit:** Actions explained by marginal economics, constraints and recorded incentives.

### A12 — Financial reconstruction
**Mission:** Build multi-period statements and cohort-based forward financials.

**Inputs:** Target and peer filings; validated driver paths

**Outputs:** Reported/recurring bridges; financial model; earnings and cash attribution

**Guardrail:** Accounting is a measurement layer, not the thesis generator; no balancing plugs.

**Exit:** Statements reconcile; prior-cycle and latest-quarter comparisons completed.

### A13 — Expectations & valuation
**Mission:** Separate operating forecast from market beliefs and horizon recognition.

**Inputs:** Point-in-time prices/earnings; public beliefs; history; driver model

**Outputs:** Conditional reverse valuation; target-date earnings/multiple; method cross-check

**Guardrail:** Do not infer unique beliefs from one price or confuse trailing and forward PE.

**Exit:** Explicit expectation delta and benchmark dates; no double-counted optionality.

### A14 — Catalyst & timing
**Mission:** Identify what becomes knowable before the price horizon.

**Inputs:** Calendars; production milestones; competitor updates; preannouncements

**Outputs:** Recognition map; already-public test; event-to-belief-to-price bridge

**Guardrail:** Economic realization can occur after the horizon; information must arrive within it.

**Exit:** Each target needs an identifiable recognition route, not a generic story.

### A15 — Independent red team
**Mission:** Try to overturn the candidate and its lead over alternatives.

**Inputs:** Source-linked thesis and model; initial review without favored target

**Outputs:** Counter-model; contradictions; hidden supply; fatal evidence gaps

**Guardrail:** No consensus averaging of incompatible facts; weakest decisive premise first.

**Exit:** Material objections resolved or candidate remains on research watchlist.

### A16 — Model QA & reconciliation
**Mission:** Audit units, formulas, dates, accounting, market sums and comparable targets.

**Inputs:** All agent artifacts and model versions

**Outputs:** Pass/fail tests; reconciled candidate package; change attribution

**Guardrail:** Never repair a failed model by an unexplained residual or multiple.

**Exit:** No blocking test failure; same mandate and cutoff across ranked finalists.

### A17 — Disclosure census
**Mission:** Inventory every scoped filing, table, footnote, numeric narrative and meaningful omission.

**Inputs:** Original filings, exact page/table/row, version manifests, prior-period corpus

**Outputs:** Document census; numeric fact register; mapped/excluded/conflicted/unreadable dispositions

**Guardrail:** Do not silently omit small or awkward numbers; an empty disclosure is not zero.

**Exit:** All primary statements and decision-relevant notes reconciled; every scoped numeric item has a disposition.

### A18 — Adoption and customer choice
**Mission:** Convert incremental customer value into economically viable, funded, qualified and deployable cohorts.

**Inputs:** Matched technical dossier; alternatives; budgets; procurement windows; integrations and support

**Outputs:** Per-cohort incremental NPV; best alternative; switching burden; bottleneck-limited deployment and replacements

**Guardrail:** Positive ROI is necessary, not sufficient; sunk costs are not incremental costs; use contribution not gross revenue.

**Exit:** Economics, budget, willingness and physical deployment separately supported.

### A19 — Dynamics and shocks
**Mission:** Maintain long-run state transitions and short-run shocks on linked calendars.

**Inputs:** Demand, installed stock, capacity, inventory, contracts, macro paths, rival decisions and event ledger

**Outputs:** Multi-resolution operating path; structural/transitory event channels; rational response; accounting lags

**Guardrail:** Never truncate economics at the price horizon or use a later realized shock as an ex-ante input.

**Exit:** Stocks conserve; lagged transmissions reconcile; known new factors included before forecast lock.

### A20 — Validation protocol designer
**Mission:** Pre-register objectives, baseline models, chronological splits, purges, metrics and pass criteria.

**Inputs:** Available vintages and history; forecast lanes; chain groups; cutoff and horizon

**Outputs:** Signed protocol; train/validation/test manifest; permitted updates; test budget

**Guardrail:** No random row split, test-informed feature choice, secret metric changes or retrospective winner selection.

**Exit:** Protocol frozen before any sealed-test outputs are accessible.

### A21 — Sealed evaluator
**Mission:** Score immutable forecasts against separately stored target outcomes.

**Inputs:** Frozen predictions and hashes; isolated labels; protocol; baselines

**Outputs:** Line-item errors; predeclared metrics; contamination flags; released postmortem after test closes

**Guardrail:** Do not send hidden outcomes or test-error feedback to researchers during model development.

**Exit:** Every target scored once under the frozen protocol; disclosed reruns labeled exploratory.

### A22 — Point-in-time data custodian
**Mission:** Enforce vintage, access and source-lineage boundaries across all agent tools.

**Inputs:** Archived documents; timestamps; provider availability; source/claim DAG; allowed data partitions

**Outputs:** Cutoff-filtered feature packets; quarantined labels; access log; hashes

**Guardrail:** A filename or access date is not evidence of historical availability; prompts alone do not seal labels.

**Exit:** No future ancestors; no mixed access; model-known historical outcomes flagged.

### A23 — Research coverage planner
**Mission:** Allocate retrieval to coverage gaps, contradictions and ranking-sensitive parameters.

**Inputs:** Document matrix; market/chain graph; source independence; costs; unresolved parameter sensitivity

**Outputs:** Question-driven search batches; incremental requests; saturation/stopping record

**Guardrail:** Do not equate long tool sessions or repeated search results with evidence depth.

**Exit:** Critical unknowns are resolved or block eligibility; all stopping decisions explain remaining exposure.

## Appendix B. Research gates

### G00 — Mandate locked
Owner: **O00**. Evidence: Universe, share class, price timestamp, two-month target calendar and ranking metric fixed.

Pass condition: No mutable or missing core mandate field.

### G01 — Identity and price
Owner: **A01**. Evidence: Issuer/share class, FX, current price, dilution and corporate actions verified.

Pass condition: Quote is current to the run; denominator and share class consistent.

### G02 — Source provenance
Owner: **A01**. Evidence: Material facts have primary locator, dates, units and independent-origin IDs.

Pass condition: No fabricated, stale, mirrored-as-independent or future-leaked evidence.

### G03 — Customer surplus
Owner: **A08/A09**. Evidence: Matched technical comparison and full adoption cost support a customer benefit.

Pass condition: No unsupported performance-to-TAM leap or double-counted savings.

### G04 — Downstream demand
Owner: **A05**. Evidence: Customer/program demand model with independent aggregate cross-check.

Pass condition: No substitution of capex dollars or backlog face value for shipments.

### G05 — Qualified supply
Owner: **A06**. Evidence: Incumbents, entrants, cancellations, conversions, yield and qualification modeled.

Pass condition: Material competing capacity and shared bottlenecks accounted for.

### G06 — Price formation
Owner: **A07**. Evidence: Grade-specific price history; buyer/seller evidence; contract and inventory lags.

Pass condition: Realized prices and cost recovery are not sentiment assertions.

### G07 — Competitive share
Owner: **A10**. Evidence: Customer wins/losses and constraints explain share path.

Pass condition: Share denominator valid; competitor allocations sum correctly.

### G08 — Rational execution
Owner: **A11**. Evidence: Capacity/pricing/procurement actions are economically and incentive-consistent.

Pass condition: No 'hope management does X' assumption in a load-bearing variable.

### G09 — Financial tie-out
Owner: **A12/A16**. Evidence: Multi-period statements, quarterly subtraction and earnings-quality bridge reconcile.

Pass condition: No missing-cost plug, cash double count, EPS or dilution inconsistency.

### G10 — Two validation loops
Owner: **A15/A16**. Evidence: Technology/share loop and industry/financial loop both tested.

Pass condition: Contradictions classified, not automatically blamed on execution.

### G11 — Expectation delta
Owner: **A13/A14**. Evidence: Specific information before horizon changes a multi-year belief.

Pass condition: Already-priced/preannounced information is not counted again.

### G12 — Valuation discipline
Owner: **A13/A16**. Evidence: Fixed fiscal denominator, historical PE bridge and independent valuation checks.

Pass condition: No arbitrary peak PE, un-discounted distant FCF comparison or option duplication.

### G13 — Adversarial review
Owner: **A15**. Evidence: Counter-case, earlier supply response and cash conversion reviewed.

Pass condition: No unresolved premise whose break-even changes eligibility/ranking.

### G14 — Comparability and publication
Owner: **O00/A16**. Evidence: All candidates share cutoff, price convention and target horizon.

Pass condition: Ranking is upside-only among eligible names; other risks disclosed separately.

### G15 — Adoption is budget- and deployment-constrained
Owner: **A18**. Evidence: Cohort-specific alternatives, customer NPV, cash affordability, renewal/qualification and integrator capacity.

Pass condition: Demand cannot exceed the funded, qualified, deployable and economically eligible intersections.

### G16 — Quantitative disclosure census
Owner: **A17**. Evidence: Scoped corpus manifest, page/table coverage, numeric and qualitative-clue dispositions, footnote reconciliation.

Pass condition: Every scoped quantitative item is mapped, excluded with reason, conflicted or unreadable; no unresolved critical omission.

### G17 — Linked timescales and shock mechanics
Owner: **A19**. Evidence: Event-time, monthly, quarterly and full-cycle paths; inventories, installed base and rival-capacity state transitions.

Pass condition: Flows aggregate correctly; known long-run changes and short-run shocks are included regardless of target horizon.

### G18 — Point-in-time lineage and access isolation
Owner: **A22**. Evidence: First-public timestamps, immutable raw versions, original/revised outcomes and access logs.

Pass condition: No future ancestor, label contamination, date-only intraday inference or mixed training/test packets.

### G19 — Pre-registered validation protocol
Owner: **A20**. Evidence: Train/validation/sealed-test split, outcome definitions, baselines, metrics, tuning budget and model version.

Pass condition: No sealed-test feedback used for feature selection; short histories explicitly limited.

### G20 — Forecast locks and genuine holdout scoring
Owner: **A21**. Evidence: Immutable forecasts, hashes, cutoff-filtered features and evaluator-only targets.

Pass condition: Original predictions scored once; guidance-assisted work labeled separately; no back-solving revealed actuals.

### G21 — Anticipated-factor coverage
Owner: **A19/A23**. Evidence: Calendar of announced changes, inferred structural shifts and adversarial unannounced stresses with state channels.

Pass condition: Known relevant new factors are modeled ex ante; unforecastable shocks remain diagnostic stresses, never fabricated facts.

### G22 — Error attribution and competing explanations
Owner: **A12/A21**. Evidence: Revenue, margin, tax, cash and price error bridges; material residual owners; compensating-error checks.

Pass condition: Observed surprises are not automatically assigned to management or rescued by a valuation plug.

### G23 — Research sufficiency and independent validation
Owner: **A15/A23**. Evidence: Exposure-weighted chain coverage, original source clusters, contradiction resolution and saturation log.

Pass condition: Critical missing facts that can reverse ranking block advancement; breadth counts do not confer eligibility.

### G24 — Contamination-aware publication
Owner: **O00/A21/A22**. Evidence: Model-knowledge limits, shadow-forward results, intact manifests and candidate-specific gates.

Pass condition: No claim of pristine historical forecasting with a contaminated LLM; synthetic checks never establish investability.
