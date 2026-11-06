# Causal Equity Research Orchestrator
## Broad-to-narrow discovery, evidence-first modeling, horizon-specific stock ranking

**Version:** 2.0  
**Template revised:** 2026-10-25  
**Status:** Research architecture, not a completed market screen. No live prices, company forecasts, or prior recommendation numbers are imported.  
**Default mandate:** Find the evidence-qualified listed equity with the greatest modeled share-price appreciation over two calendar months. The operating model must extend beyond that window.

---


## Version 2 upgrade map

This version preserves the original upside-only mandate and broad-to-narrow workflow, and adds:
- an explicit customer-choice/adoption engine (Section 19);
- linked long-run states and short-run shock transmissions (Section 20);
- a complete scoped quantitative-disclosure census (Section 21);
- leakage-controlled train/validation/sealed-test and live-shadow evaluation (Section 22);
- an anticipated-new-factor registry and postmortem rules (Section 23);
- enforceable agent handoffs, coverage planning and access isolation (Section 24).

Sections 19–26 operationalize and strengthen the earlier sections. All live rankings remain blocked until the combined research gates pass. The code in the kit is a reference validator and synthetic demonstration, not an autonomous research service.

## 0. Research constitution

### The only final objective
For security i, use one consistent share basis and market-data cutoff:

    Horizon price upside_i = TargetPrice_i(T) / ReferencePrice_i(t0) - 1

Rank **eligible** candidates by this measure alone. Do not silently replace it with business quality, probability-weighted upside, downside protection, dividend yield, or a subjective composite score. Those can determine evidence requirements or be reported separately; they are not the ranking formula.

T is the last exchange session on or before the date two calendar months after t0, unless the mandate specifies otherwise. Use the relevant exchange's published calendar, not a weekday approximation. Record the timezone, quote timestamp, currency, share class, corporate actions and eligibility rules.

The target is a forecast of a market price at T, not an assertion that intrinsic value must be recognized by T. A high long-term valuation without an in-window information-recognition mechanism is not sufficient.

### Four different objects
1. **Economic reality:** customer needs, technology, funded deployment, effective supply, prices and competitors.
2. **Corporate realization:** qualification, production, procurement, delivery, costs, working capital, capital allocation and management incentives.
3. **Financial measurement:** recognition rules, consolidation, taxes, financing, depreciation, inventories and reported/recurring earnings.
4. **Investor beliefs and price:** what future state investors currently capitalize, what new information changes that state, and how valuation responds.

Do not collapse them. Financial reports are measurements of the first two through accounting rules. Prices are observations of valuation and beliefs, not direct measurements of the correct future.

### The user-specific operating principles retained
- Discover across unrelated markets before narrowing. Slower market growth can create more near-term price upside when expectations are too low.
- Start from product and business value, not current EPS or a thematic stock list.
- Research upstream and downstream separately. A good product does not eliminate a supply-cycle or input-cost problem.
- Treat the company and its customers/competitors as economically motivated actors with constraints and incentives.
- Test technical superiority independently and convert component advantages into whole-system economics.
- Derive market share from customer decisions, qualification, distribution and supply readiness.
- Give a strong report meaningful weight when it proves several operating links together; neither ignore it nor extrapolate one quarter.
- Model multiple periods and the entire relevant supply response. Prices can peak before volumes.
- Do not reject a company merely because the current P/E is high. Compute the future outcome required by the price and compare it with the independently modeled opportunity.
- Do not assume public information is fully understood, or assume that it is unpriced merely because it supports the thesis.
- Use one explicit operating path and one point target per eligible candidate. Counterfactuals diagnose dependencies; they are not probability-weighted recommendations.
- Do not import public analyst target prices or direct revenue/EPS forecasts into the investment model. Indirect industry observations may be used with original-source attribution.
- Previous assistant answers are unverified leads. Every reused numeric claim requires original-source verification.

### Evidence discipline, not false certainty
The goal is **no hidden material assumptions**, not pretending that private contracts or future market prices are known. Classify each input as:
- OBSERVED: directly disclosed or measured;
- COMPANY_CLAIM: management/vendor statement not independently established;
- DERIVED: arithmetic from identified inputs;
- MODEL_ASSUMPTION: explicit, reasoned and testable forward input;
- UNRESOLVED: important information not established;
- CONTRADICTED: conflicts with verified evidence.

If an unresolved parameter can change the winner, research it, narrow the claim, or keep the candidate on a watchlist. Do not replace the missing information with a made-up technology probability or an arbitrary execution haircut.

---

## 1. Orchestration architecture

### Dependency order
The orchestrator launches broad macro and market discovery first. For each surviving market:

    Macro transmission + value-chain map
        -> downstream demand || qualified supply
        -> price formation and rational responses
        -> technical review || customer economics
        -> competition and market-share cohorts
        -> company operating model
        -> financial measurement and validation
        -> expectations + information events
        -> horizon-price model
        -> independent red team + numerical audit
        -> eligibility gate
        -> upside-only ranking

The graph has feedback edges. Technical changes can alter content per system, substitute demand, production yield and capacity allocation. Financial discrepancies can force reopening upstream research. Investor expectations do not change the operating model merely to support a desired target.

### Independent workstreams
The technical specialist first evaluates matched workloads and adoption costs without seeing a desired stock price. The market-size agent first estimates addressable physical or economic activity without being given a requested company revenue. The red team first receives the causal thesis and source pack, not an instruction to defend the favored name.

An implementation may use actual specialist subagents. If no separate agents or human experts are available, label the work as separate analytical workstreams; do not claim external expert consultation.

### Default breadth and depth
These are proposed research standards, not guarantees that document volume proves a thesis:
- Explore at least 12 distinct market pools in a full broad search.
- Plan a first pass of about 60 names, adjusting to the permitted universe; record actual coverage rather than padding it.
- Advance roughly 6 finalists for comparable deep diligence.
- For finalists, reconstruct five annual periods and preferably 28 usable quarters for chronology-safe calibration and holdout evaluation. At least 12 quarters can support a descriptive panel, not automatically a validated predictive model; extend through a complete prior cycle.
- Include the target, two material upstream suppliers, two downstream customers or credible customer proxies, and two direct competitors. Use all material competitors in a concentrated industry.
- For a new listing or new technology, use all available history and explicitly lower the scope of historical claims.
- A proxy must be labeled a proxy. Never imply that an observed downstream company's orders belong to the target unless the link is disclosed.

### Resource allocation
Give priority to the question whose resolution can change:
1. candidate eligibility;
2. the leading candidate;
3. target price materially;
4. the direction of a key operating forecast.

The default routing threshold is a 3-percentage-point change in modeled horizon upside, or any ranking reversal. This is configurable research triage, not an investment probability.

Stop adding broad documents when the bottleneck is a specific contract, grade, cost or customer parameter. Maintain a long-tail clue inbox, but promote a clue only after linking it to a causal parameter and a test.

---

## 2. Source, chronology and clue infrastructure

### Source record
Every source record contains:
- source ID and original URL/path;
- entity and role in the chain;
- exact document title, page/table/paragraph locator;
- observation period;
- publication timestamp;
- retrieval timestamp;
- first public availability;
- original-origin cluster;
- revision/supersedes link;
- primary/secondary designation;
- access limitation and freshness status.

A news story, an analyst note and three syndicated copies of the same release are one evidence origin, not five independent confirmations.

### The eight clocks
1. Physical event or order date.
2. First public disclosure date.
3. Contract price-effective date.
4. Procurement and inventory-cost date.
5. Delivery/acceptance and revenue-recognition date.
6. Cash settlement date.
7. Investor recognition date.
8. Reference and target share-price dates.

Do not use a Q4 realized value as if it were known at a Q3 valuation date. Do not count an earnings result as a new surprise when it was already preannounced. Do not infer immediate cost recognition from a commodity spot-price move.

### Clue record
For every potentially meaningful detail, record:

    clue -> mechanism -> intermediate variable -> financial effect
         -> time lag -> belief effect -> possible price effect

Also record the strongest alternative explanation and the next discriminating source.

Examples worth investigating:
- a price letter covering only new orders;
- equipment already reserved before an industry lead-time extension;
- a cancelled project that was never operating capacity;
- a product with higher price per metre but lower output per machine-hour;
- customer advances financing working capital;
- new shipping terms moving revenue recognition;
- a patent settlement generating royalties not product sales;
- capitalized R&D or a tax credit lifting reported margin;
- a contract manufacturer changing the apparent customer concentration;
- an ADR ratio, stock split or rights issue distorting the per-share denominator.

Do not automatically interpret these clues as bullish or bearish.

### Conflict procedure
Do not average incompatible facts. Check, in order:
1. unit and currency;
2. tax/freight basis;
3. grade or product definition;
4. geography;
5. fiscal versus calendar period;
6. standalone versus consolidated scope;
7. transaction versus list price;
8. revision and publication chronology.

Escalate unresolved material conflicts to the orchestrator and block the dependent calculation.

---

## 3. Macro research: trace mechanisms, not narratives

Create a macro-to-business transmission map for each finalist. Every variable needs an exposure, sign, lag, source and affected equation.

### Rates and credit
Research:
- risk-free curves and real rates;
- customer credit spreads and project borrowing terms;
- loan/ABS availability, collateral and covenants;
- issuer maturities, floating debt and refinance schedule;
- leasing or vendor financing that makes customer demand feasible.

Separate:
- lower financing costs increasing customer project NPV;
- lower issuer interest expense;
- lower equity discount rates;
- market sentiment toward long-duration earnings.

Do not count one rate change three times without mapping the distinct cash flows.

### Inflation, energy and logistics
Research the relevant feedstock grade, utility tariff, energy contract, transport route, freight basis, insurance and hedging. Determine who owns inventory when the cost changes and when it enters COGS.

Distinguish operating input costs from capital expenditures. Buying metal for production equipment, for example, is not the same as consuming that metal in every unit sold.

### FX
Map:
- invoice currency;
- sourcing currency;
- monetary assets/liabilities;
- hedges;
- transaction gains/losses;
- consolidation translation and OCI;
- pricing competitiveness.

Never apply an exchange-rate percentage to all overseas revenue and call the result net profit.

### Policy and regulation
Use enacted rules, effective dates, appropriations, eligibility and actual implementation. Describe policy transmission neutrally. Do not infer procurement from an announcement that has no funding or implementation.

### End-market conditions
Separate industrial production, capacity utilization, equipment investment, retail sell-through and inventory cycles. More customer output does not automatically require more machines if utilization was low.

Deliverable: a small set of material macro paths, not a lengthy economic essay.

---

## 4. Market and value-chain decomposition

Before estimating a TAM, define:
- product/service function;
- grade/specification;
- geography;
- merchant versus captive supply;
- physical/economic unit;
- annual flow versus installed stock;
- current period and forecast periods.

Map each stage's input/output conversion, inventory owner, contract mechanism, qualification, gross contribution and limiting resource.

Identify:
- true bottlenecks;
- suppliers benefiting from higher prices;
- downstream companies bearing the same increases;
- complements whose absence caps deployment;
- substitutes that become economic after prices rise.

Record where a technology shift moves value. The removal of one bottleneck can expand another market or eliminate an incumbent revenue pool.

Use separate modules for:
- commodities/materials;
- equipment;
- semiconductor components and IP;
- SaaS/platforms;
- networks/logistics/space;
- clinical/regulatory businesses.

A generic margin or demand equation cannot be imposed on all six.

---

## 5. Downstream demand model

### Physical-product model
For grade g, application j, period t:

    Consumption[g,t] =
      sum over j(
        deployed systems[j,t]
        * attachment[j,g,t]
        * content per system[j,g,t]
        / downstream good-output yield[j,t]
      )
      + non-duplicated replacement demand[g,t]

    Procurement need[g,t] =
      consumption[g,t]
      + desired ending inventory[g,t]
      - opening usable inventory[g,t]

Use a signed inventory change. Restocking is not final consumption.

### Customer/project ledger
For each named downstream customer or representative cohort, gather:
- end demand and utilization;
- funded budget, not only aspirational capex;
- binding/nonbinding orders and cancellation rights;
- supplier allocation;
- delivery, installation and acceptance schedules;
- project complements such as power, labor, permits or memory;
- replacement and repair requirements.

Count the same customer order only once across OEM, contract manufacturer and supplier disclosures.

### Content per system
Derive content from actual architecture:
- layers, channels, links and ports;
- wattage, conversion stages and current;
- board area, material grade and scrap;
- tests per die, package and wafer;
- software workloads, active seats and paid usage;
- medical procedures, eligibility and reimbursable utilization.

Do not multiply a headline dollar capex growth rate by supplier revenue without separating land, construction, compute, memory, networking, maintenance and price inflation.

### Adoption thresholds
Calculate customer break-even economics by application. A price reduction may make a new application viable and expand demand nonlinearly.

Use a segmented adoption curve:
- technically feasible users;
- users with positive customer NPV;
- users with funding;
- users that can complete qualification;
- users deployable in the forecast period.

Do not force a logistic or exponential curve merely because the technology is promising. Estimate the timing from customer cohorts and observed conversion.

### Cross-check
Reconcile the bottom-up model against at least one independent physical-demand series and one downstream financial/operating source. An industry market forecast and the same forecast repeated by a supplier are not independent.

---

## 6. Qualified supply and rational capacity response

### Project-state ledger
For every material producer and substitute, track:
- announced;
- approved/funded;
- equipment ordered/reserved;
- under construction;
- mechanically complete;
- commissioned;
- qualification underway;
- first qualified shipment;
- ramping;
- mature;
- paused/cancelled/retired.

Record original and revised dates, not just the latest optimistic schedule.

### Effective capacity
For a single stage:

    effective output =
      annual nameplate / periods per year
      * active-period fraction
      * grade allocation
      * uptime
      * yield
      * qualified fraction

For stages in series, total output is constrained by the **minimum equivalent throughput**, not the sum of stage capacities.

Avoid multiplying two factors that both describe the same loss. If disclosed capacity already means good output, do not apply the same yield deduction again.

### Shared resources
When products compete for looms, wafers, foundry slots, test hours, power or skilled engineers, use a shared-resource constraint:

    sum_g(output[g] / throughput_per_hour[g]) <= available hours

A higher selling price per unit is not necessarily a higher profit opportunity if the product runs more slowly.

### Rational producer response
Model contribution per binding resource:

    contribution per bottleneck hour =
      (realized price - incremental unit cost)
      * good output per hour

Then test feasible actions:
- increase uptime;
- improve yield;
- redirect production by grade;
- debottleneck;
- expand;
- acquire capacity;
- lock in customers;
- postpone shutdown/repair;
- reduce output when contribution deteriorates.

For new investment, use full-cycle incremental NPV and financing constraints. Do not assume today's peak margin throughout the project life.

### Rational customer response
Model:
- price acceptance;
- cost pass-through;
- dual sourcing;
- inventory drawdown;
- lower-spec substitution;
- redesign;
- internal production;
- project delay;
- demand destruction.

Behavior follows the best feasible alternative and switching cost, not a blanket assertion that customers will accept higher prices.

### Management is not assumed perfect
Document compensation, related-party transactions, strategic mandates, financing limits, empire-building incentives and other agency issues. Rationality means the response follows stated incentives and constraints; it does not mean every decision maximizes minority-shareholder value.

---

## 7. Market clearing, bargaining power and price paths

### Inventory identity
By grade, region and period:

    ending inventory =
      opening inventory
      + production
      + imports
      - exports
      - consumption

A negative inventory result is an infeasible model. Resolve it through supply changes, substitution, rationing, deferred demand or corrected assumptions; do not leave it in the forecast.

### A deficit is not a price forecast
Price depends on:
- inventory availability and desired stock;
- buyers' alternative costs;
- supply elasticity;
- substitute qualification time;
- contract coverage;
- market concentration;
- financing and distress;
- feasible rival response.

If elasticity or contract transmission is not identified, publish a break-even requirement or blocked price parameter—not a precise unsupported selling-price path.

### Evidence of bargaining power
Require paired evidence, preferably across several periods:
- seller realized comparable price;
- seller volume and order retention;
- seller contribution or unit margin;
- buyer procurement cost;
- buyer margin and pass-through;
- delivery time and inventory;
- receivables, advances and payment terms.

Higher supplier profit alone can reflect mix, lower costs or a one-off. Higher ASP alone can reflect a different product.

### Exact revenue bridge
For matched grades:

    revenue change =
      sum_g(volume change[g] * old price[g])
      + sum_g(old volume[g] * price change[g])
      + sum_g(volume change[g] * price change[g])

Separate FX, new products, acquisitions and scope changes. A sequential bridge is also valid when stated explicitly; never mix decompositions silently.

### Contract cohorts
For each delivery cohort, track:
- order date;
- old/new price schedule;
- index/fixed/spot terms;
- discounts;
- taxes/freight;
- customer region;
- delivery/acceptance;
- reporting currency;
- renewal date and cancellation rights.

Recognized price is the delivery-weighted price of those cohorts, not the latest published quotation.

### Supply-cycle phases
Model discovery/tightening, shortage realization, funded expansion, qualification/ramp, balance and normalization separately. The share price can recognize normalization before the peak quarter is reported.

---

## 8. Technology specialist and customer economics

### Technology dossier
For each candidate and credible alternative, require:
- the function and physical constraint;
- system architecture and interfaces;
- standards compliance;
- workload;
- process and operating conditions;
- energy/power;
- performance/accuracy/latency;
- reliability and failure modes;
- qualification maturity;
- manufacturing/servicing feasibility;
- patents, freedom-to-operate and licensing;
- independent validation;
- next-generation substitutes.

A vendor's best benchmark, a rival's typical benchmark and a laboratory paper are not directly comparable.

### Convert component benefit into system benefit
If a fraction f of workload is accelerated by k:

    full-system speedup = 1 / ((1-f) + f/k)

Do not multiply the entire system's economic value by a component's maximum performance claim.

For energy, specify watts, utilization, hours, facility overhead, electricity price and whether cooling savings are already included. For material shrink, include peripheral area, yield, optics, packaging and reliability.

### Full lifecycle TCO
Include:
- product price;
- redesign and integration;
- tooling, software and certification;
- training and data migration;
- downtime;
- maintenance and replacement;
- financing;
- royalties;
- energy and cooling;
- vendor concentration;
- decommissioning.

Benefits must use incremental contribution, measurable cost savings or separately justified risk reduction. Freed employees who are not removed from payroll are not automatically a cash saving; value their redeployment separately.

    Customer NPV =
      PV(incremental contribution + avoided cost + supported risk reduction)
      - PV(product and adoption/lifecycle costs)

### Switching costs in both directions
Distinguish:
- friction to adopt the challenger;
- friction to leave the incumbent;
- friction to leave the challenger after deployment.

Open standards and open source can reduce adoption resistance while also limiting lock-in. Do not classify every ecosystem as permanent pricing power.

### Evidence that better technology is actually winning
A superior technical result is only one input. Verify:
- repeat production wins;
- lost designs at rivals;
- customer qualification breadth;
- retention and successor-product reuse;
- relative shipment growth;
- price and margin retention;
- competitor response.

“Better technology gradually wins” must be modeled through these conversion mechanisms, not asserted as instantaneous or universal.

---

## 9. Competitive dynamics and market-share cohorts

### Define the contestable market
Exclude:
- captive internal supply that cannot yet be displaced;
- incompatible protocols/grades;
- geographies blocked by regulation or support;
- customer programs already awarded to a non-interchangeable architecture;
- low-value applications where the superior product does not pay for itself.

Keep unit share and revenue share distinct.

### Cohort conversion
Track each program through:

    opportunity -> nomination -> qualification -> pilot
    -> production award -> shipment -> acceptance
    -> collection -> renewal/successor reuse

An expected-lifetime revenue opportunity is not firm backlog, and neither is the same as next year's sales.

Calculate annual company revenue from:
- new wins that reach production;
- existing-program units;
- retained successor programs;
- price/content changes;
- losses and cancellations;
- available qualified supply.

### Share reconciliation
The market-share model must:
- sum to 100% across mutually exclusive competitors and residual supply;
- fit each supplier's qualified output;
- fit customer procurement;
- account for private competitors;
- reflect deliberate competitor pricing and capacity choices.

### Relative-growth diagnostic
When definitions are matched:

    relative share growth = (1 + company growth) / (1 + market growth) - 1

This is not absolute percentage-point share gain. It is invalid if company growth includes acquisitions or product mix excluded from the market denominator.

### Inner validation loop
Technology -> customer surplus -> commercial decisions -> shipments -> observed share.

If the company has a technical advantage but no qualified wins, investigate adoption friction and customer economics. If it wins programs but cannot ship, investigate execution. Do not label both situations the same generic risk.

---

## 10. Multi-period financial reconstruction

### Required panel
Reconstruct the target and material supply-chain peers across:
- sequential quarters;
- year-over-year quarters;
- annual periods;
- a previous peak and trough where applicable;
- disclosed project and product generations.

Do not rely on the latest earnings release alone.

### Data normalization
Keep distinct:
- reported and recurring;
- constant currency and reported currency;
- organic and acquired growth;
- gross and net revenue;
- company versus group;
- point-in-time and weighted-average shares;
- fiscal and calendar periods;
- tax-inclusive and tax-exclusive prices;
- GAAP and adjusted metrics.

Derive a quarter from cumulative reports only after checking restatements and consolidation changes.

### Bottom-up P&L
Revenue is generated by the customer/share/order models.

COGS is generated by:
- quantities;
- input-cost vintages;
- inventory-cost method;
- good-output yield and scrap;
- labor;
- freight and tariffs;
- manufacturing depreciation;
- startup costs.

Operating expenses are generated by hiring, compensation, programs, selling channels, support and R&D—not a convenient percentage chosen to reach EPS.

Taxes require a bridge from statutory rates to credits, R&D deductions, geographic mix, losses and one-offs. Share-based compensation is not removed from economic costs just because it is noncash.

### Cash and balance sheet
Reconcile:

    CFO =
      net income
      + noncash items
      - inventory increase
      - receivables increase
      + payables increase
      + customer advances increase
      + other legitimate timing differences

    FCF = CFO - cash capital expenditure

Model acquisition payments, financing, leases and buybacks separately. Customer deposits are financing of operations, not proof of final economic margin.

Use converted-share and if-converted earnings treatment consistently. Do not add back convertible interest while forgetting new shares.

### Earnings quality
Screen every period for:
- investment gains;
- asset sales;
- tax credits and refunds;
- royalties or settlement income;
- subsidies;
- FX;
- capitalized costs;
- acquisition accounting;
- minority interests;
- changes in useful life;
- share-count changes.

Do not remove an adverse recurring operating cost while retaining a favorable recurring subsidy without explaining the asymmetry.

### Outer validation loop
Macro/demand/supply/price/share -> operating forecast -> reported revenue, margin, profit and cash.

A good report receives greater weight when it independently confirms several links. A preannounced EPS figure must not be counted again as a new surprise.

---

## 11. Discrepancy diagnosis

When observed results differ from the frozen model, classify the cause before changing the target.

| Pattern | First diagnostic branch |
|---|---|
| Industry deployments miss, several suppliers miss | Downstream-demand model |
| Demand is strong but the candidate loses orders | Competitive/customer-surplus model |
| Orders are strong but deliveries slip | Capacity, qualification, component supply or acceptance |
| Revenue meets but gross profit misses | Price, mix, recognized input costs, yield or ramp |
| Gross profit meets but net income misses | Expenses, financing, tax or impairments |
| Profit meets but CFO misses | Receivables, inventories, payables, advances and tax timing |
| Headline profit beats without operating improvement | Earnings-quality adjustment |
| Operations meet but price disappoints | Expectations, valuation, recognition timing or liquidity |

Keep the residual e as a visible unexplained amount. Do not use e to make every failed forecast appear directionally correct.

Use the full train/validation/sealed-test and prospective-shadow protocol in Section 22. A single withheld quarter is not enough to establish forecast reliability; do not reuse a test after tuning to its errors.

---

## 12. Expectations, historical PE and the price horizon

### Business state versus belief state
Let x_t be the modeled business state and b_t the market's beliefs about its future.

    financial observations = accounting_map(x_t, execution) + residual
    share price = valuation_map(b_t, required return, positioning)

The business can be correctly modeled while the price forecast is wrong. This is an unavoidable distinction, not a reason to hide the price forecast.

### Point-in-time history
For each historical price:
- use only earnings and disclosures public at that moment;
- adjust prices and shares for splits/bonuses/rights consistently;
- distinguish ex-dividend declines from selling pressure;
- preserve the same earnings definition;
- record the quarter embedded in TTM;
- keep a fixed fiscal-year forward comparison alongside rolling metrics.

A PE decline caused by a new earnings denominator is not entirely a derating.

### Conditional reverse valuation
A price is one observation with many possible explanations. Reverse-engineer combinations of:
- units;
- content;
- share;
- prices;
- margins;
- duration;
- required return.

Label them conditional. Never state “the market assumes exactly X” solely because one chosen multiple gives X.

### Information-recognition model
For each event before T:
1. What is already public?
2. What genuinely new information can arrive?
3. Which long-term operating variable changes?
4. Why might investors consider it credible?
5. What is the read-across from related companies?
6. What competing interpretation could prevent repricing?

A 2027 commissioning update can affect a two-month price by changing 2028 margins. The economic event need not be inside the price window.

### Momentum and positioning
Do not assume investors are perfectly informed or perfectly rational. However, do not add an arbitrary momentum premium.

Only incorporate momentum/flow effects when supported by documented turnover, ownership, positioning, issuance, short interest, index flows or comparable event reactions. Keep that component separate from fundamental value so it cannot silently rescue a weak model.

---

## 13. Valuation and target construction

### EPS multiple model
For a fixed earnings year Y:

    target price = target-belief EPS[Y] * target PE[Y]

    target/reference price =
      (target-belief EPS[Y] / current-belief EPS[Y])
      * (target PE[Y] / current PE[Y])

Show the EPS, multiple and interaction contributions. Do not compare current TTM PE with a target forward PE and call the target “no rerating.”

### Selecting the multiple
Use three evidence sources:
- the issuer's own point-in-time valuation under comparable growth, margin, duration and capital conditions;
- matched peers with different business models excluded or normalized;
- economic sustainability of growth, reinvestment, cash conversion and return on capital.

Historical peak multiples are observations, not entitlements.

Growth and reinvestment must coexist. Do not assume very high growth, minimal reinvestment and near-total cash payout indefinitely.

### DCF
Use DCF as a cross-check on the explicit operating path, not as the discovery engine.

Discount distant FCF properly. Current EV divided by undiscounted 2030 FCF is a scale comparison, not proof of cheapness.

Terminal value must include maintenance capex, replacement costs and a coherent normalized cycle. Use FCFF with WACC and EV; use FCFE with cost of equity and equity value. Do not mix them.

### Platform and early-stage businesses
Value awarded designs and technical platforms only through:
- customer conversion;
- production timing;
- retention;
- unit/content economics;
- funding and dilution;
- necessary operating investment.

Do not add “option value” for a product already included in the revenue forecast.

### Comparable ranking
The same cutoff and target date apply to every finalist. A higher-priced or higher-PE stock can rank first when independently supported future outcomes justify it.

Publish one target path per eligible candidate. Show deterministic break-even and one-factor perturbations separately; do not convert them into hidden probability weighting.

A candidate without a defensible expectation-change route remains a watchlist name, even if long-term business value is high.

---

## 14. Hard research gates and stopping rules

A candidate is rank-eligible only when all required gates pass.

A numerical parameter may remain an explicit assumption if:
- it has a stated mechanism;
- evidence supports its scale and direction;
- alternatives and substitutes have been considered;
- a break-even threshold is shown;
- a reasonable counterfactual does not reveal an unexamined ranking reversal.

If an inaccessible parameter determines whether the candidate wins, the output is “not established,” not a fabricated point estimate.

Recommended stop conditions:
- the strongest alternative explanation survives;
- the supposed shortage is removed by already-funded competitor capacity;
- customer surplus disappears after complete adoption cost;
- the reported beat is mainly nonrecurring;
- the price already requires the modeled outcome and no further in-window information delta exists;
- data coverage is insufficient for a comparable target.

A search can end with no eligible stock. Do not force a winner.

---

## 15. Query playbook

Search questions should be entity-, product- and period-specific.

### Filings and projects
- [issuer] [period] annual/interim/quarterly report original filing
- [competitor] [product grade] capacity commissioning qualification cancellation
- [project] original announced date versus current delivery schedule
- [customer] procurement price inventory supplier dependence payment terms
- [issuer] recurring profit reconciliation inventory cost method tax R&D credit

### Technology
- [function] [standard] specification
- [candidate product] [competitor product] matched benchmark operating conditions
- [architecture] peer-reviewed paper failure mode
- [customer] production deployment versus pilot
- [product] second source interoperability qualification

### Price and cycle
- [grade] transaction price contract price tax freight basis [month]
- [supplier] price letter new orders existing orders effective date
- [buyer] input-cost margin pass-through [quarter]
- [equipment supplier] lead time reserved orders deliveries
- [producer] cold repair restart debottleneck grade conversion

### Expectations
- [company] announcement timestamp preannouncement results call
- historical split-adjusted close and shares outstanding at [date]
- earnings revisions and management wording available at [date]
- [event] comparable historical stock response with market/sector control

Secondary reporting is a discovery tool. Return to original evidence for material numbers. Report inability to retrieve it instead of substituting an invented citation.

---

## 16. Output packet

Every completed candidate package contains:
1. One-page causal thesis.
2. Market-definition and unit dictionary.
3. Downstream demand model.
4. Qualified capacity and competitor-project ledger.
5. Price, contract and input-cost cohorts.
6. Technical comparison and customer TCO.
7. Customer-level share-conversion model.
8. Multi-period financial reconstruction.
9. Forward operating/financial model.
10. Market-belief and recognition map.
11. Historical valuation audit and target bridge.
12. Cash, dilution and capital-allocation review.
13. Contradictions, break-even tests and red-team verdict.
14. Source ledger with exact locators.
15. Versioned final target and ranking eligibility.

The public conclusion must distinguish:
- reported fact;
- company claim;
- derived value;
- forward assumption;
- model output;
- expectation judgment.

Never use a citation to a supplier release as if it independently validated a performance claim.

---

## 17. Change control and postmortem

When a source changes:
- update the source/claim version;
- identify dependent model nodes;
- recalculate affected demand/supply/price/share/financial variables;
- re-run all dependent gates;
- update targets only after reconciliation;
- preserve the previous target and explain the change.

Every ranking change must be attributable to one or more of:
- new source evidence;
- changed reference price;
- changed operating model;
- changed recognition timing;
- changed valuation assumption;
- changed mandate.

Do not call the ranking stable merely because the narrative still sounds similar.

Postmortem the forecast in two parts:
1. Was the business path correct?
2. Did the expected information change investor beliefs and price on time?

A correct earnings forecast with an incorrect price forecast is not a fully successful investment prediction.

---

## 18. Synthetic workbook demonstration

The workbook includes a clearly labeled synthetic example. It is not calibrated to a real issuer or used for a recommendation.

It demonstrates:
- physical demand, not capex dollars;
- nameplate-to-qualified capacity conversion;
- inventory-constrained fulfillment;
- announced versus realized pricing;
- inventory-cost cohorts;
- earnings-to-cash conversion;
- customer TCO;
- fixed-year EPS and multiple decomposition;
- blocking of live rankings while evidence gates remain incomplete.

The machine-readable JSON contains role prompts, task dependencies, gates, schemas and research rules. It is a specification for an agent system, not a deployed autonomous system and not a promise of background monitoring.

---



## 19. Customer value must generate adoption cohorts, not a decorative ROI paragraph

### 19.1 Economic choice, customer by customer
Define the actual decision maker, budget owner, operator, beneficiary, payer, channel and any regulator. They may be different entities. A hospital can create societal value without receiving reimbursement; an OEM can pass a component saving to end customers; a cloud buyer can gain throughput but lack power to deploy it.

For customer cohort c, alternative a, and decision time t:

    IncrementalNPV[c,a,t] =
      - incremental cash introduction and switching costs[c,a,t]
      + sum_h(
          incremental contribution from useful output[c,a,t+h]
          + actually avoidable cash operating costs[c,a,t+h]
          + supported avoided-loss value[c,a,t+h]
          - incremental recurring cash costs[c,a,t+h]
          - incremental working-capital cash need[c,a,t+h]
        ) / (1 + customer financing hurdle[c,t])^h
      + discounted residual asset value and working-capital recovery

Compare with the best feasible alternative, not an intentionally weak incumbent. The choice set must include keep/repair, defer, alternative vendor, in-house build, redesign and dual sourcing. Historical sunk costs are not incremental cash costs. Lost resale value, termination fees, migration and dual-running are incremental.

Use cash contribution rather than top-line revenue when valuing output. A faster machine creates value only if another bottleneck, labor availability, energy connection or end-customer demand does not prevent useful output. A full-system speedup must respect workload fractions and total capacity.

Create a benefit ledger so each mechanism has a distinct physical basis. Do not value the same saved hour as both payroll eliminated and incremental production. Do not count energy savings once in operating costs and again in a separate efficiency benefit. Avoided failure uses supported frequency/severity evidence; otherwise disclose a break-even failure threshold, not a fabricated expected saving.

### 19.2 A positive NPV is necessary, not sufficient
Adoption occurs only when all relevant gates clear:
1. Technical and safety fitness.
2. Positive incremental NPV versus the best alternative.
3. Customer-specific payback/return hurdle.
4. Available funding and working capital.
5. Procurement and renewal window.
6. Organizational authority and implementation resources.
7. Qualification and certification.
8. Physical deployment complements.
9. Available supplier output and support.

Track each cohort through disjoint stages. Never multiply unrelated aggregate percentages and imply they describe the same customers. At the individual-cohort level, the feasible set is the intersection of these conditions.

    deployable_new_units[c,t] =
      min(economically_eligible_and_due[c,t],
          funded_and_approved[c,t],
          qualified_and_ready[c,t],
          integrator_slots[c,t],
          complementary_infrastructure_slots[c,t],
          allocated_supplier_good_output[c,t])

Where the populations are not nested, compute the intersection from cohort IDs; the minimum of unrelated totals is only an upper bound.

A buying intention is not an installed system. A signed contract is not funded delivery. A production award is not immediate revenue. A nominal addressable customer is not a paying user.

### 19.3 Explicit affordability and switching tests
Record separately:
- economic NPV;
- upfront cash affordability;
- annual budget availability;
- payback period;
- financing cost and covenant constraints;
- time until renewal;
- cost to leave the incumbent;
- cost to introduce the challenger;
- future exit cost after adopting the challenger.

A lower total cost over five years can still fail a two-year customer payback rule. Reducing upfront cost through leasing can accelerate adoption while shifting credit or asset risk back to the supplier; include that cost.

### 19.4 Price ceiling and value capture
Let S0 be the customer's incremental NPV before the supplier's price premium. Then S0 is an upper economic bound on the present value of the total premium, not a forecast of the supplier's realized pricing.

The price actually paid also depends on rival alternatives, purchasing concentration, performance guarantees, contracts, qualification and supplier capacity. Do not assign an arbitrary fraction of customer surplus to the supplier.

For each customer, estimate the highest feasible price that preserves NPV and payback requirements. Combine reservation-price schedules with qualified supply to test pricing power. Customers below the economic threshold can defer or substitute.

### 19.5 Adoption, learning and substitution are endogenous
As cumulative production rises, yield or unit cost can improve. Estimate the learning slope from earlier product generations or engineering evidence, with regime limitations.

    UnitCost_t = material_cost_t + conversion_cost(cumulative_good_output_t, yield_t)
    CustomerNPV_t = f(price_t, substitute_price_t, integration_cost_t, performance_t)
    NewAdoption_t = g(CustomerNPV_t, budget_t, qualification_t, deployment_capacity_t)

A price reduction can expand the market but reduce revenue per unit. A superior new architecture can cannibalize the company's old products. Model old and new installed stocks separately, including retirements and upgrades.

New cohorts arise when cost crosses a threshold; do not assume a logistic curve without program-level evidence. If fitting an adoption curve, its parameters and asymptote are selected only in training/validation, not to make a target price attractive.

### 19.6 Demand-source map
Every modeled revenue pool must be traceable to:
- named buyer or representative cohort;
- buyer's own customer/end-use need;
- eligible units and physical definition;
- funded expenditure and schedule;
- product attachment and content;
- customer value/alternative comparison;
- qualification;
- current program state;
- assigned suppliers;
- inventory owner;
- expected consumption, shipment, acceptance and collection dates;
- direct-disclosed relationship versus proxy.

Triangulate top-down totals and bottom-up cohorts independently. Do not force their agreement with an unexplained scaling factor. Differences can reveal missing private suppliers, captive supply, inventory or a mistaken unit definition.

---

## 20. Long dynamics and short shocks operate on linked clocks

### 20.1 Never truncate economics at the stock-price horizon
The stock target may be two months away. The operating model must still include:
- product life and replacement cycles;
- next-generation substitutes;
- competitor capacity and customer qualification;
- capital maturity, refinancing and maintenance;
- price normalization;
- ecosystem lock-in and later commoditization.

Default resolution:
- event-time/daily or weekly: prices, shutdowns, contracts, freight and disclosure timing;
- monthly for the next 24 months: shipments, procurement, inventories and contract repricing;
- quarterly through year 5: financial reporting, capacity ramps and cohort conversion;
- annual through years 6–10, extended until the main economic cycle normalizes.

Do not use all grids mechanically. Choose resolution to match the actual decision lag. Aggregate flows by SUM, period-end stocks by LAST, rates by economically relevant weights and realized ASP by shipment-weighting. Never average annual capacity and call it period production.

### 20.2 State variables
Maintain opening and closing states for:
installed systems by age; undecided economic customers; contracted backlog; qualified capacity by grade; available bottleneck hours; cumulative good output; inventories by owner and cost vintage; receivables; payables; customer advances; hedges; debt maturities; and investor beliefs about later cash flows.

A schematic state update is:

    x[t+1] = F(x[t], customer_choices[t], rival_actions[t], macro_path[t], shocks[t])
    financials[t] = H(x[t], accounting_policy[t], recognition_dates[t]) + unexplained_residual[t]
    market_beliefs[t+1] = G(market_beliefs[t], newly_public_evidence[t], credibility, positioning)

This is an architecture, not an identified universal equation. Each sector requires its own mechanisms.

### 20.3 Feedback loops to solve
At minimum test:
- falling input or integration cost -> more positive-NPV customers -> higher demand;
- higher supplier price -> lower customer NPV -> substitution/deferment;
- higher profit -> investment -> later supply -> price normalization;
- long lead times -> precautionary orders -> inventory accumulation -> later order correction;
- more deployments -> learning/yield -> lower cost -> price/share response;
- a bottleneck moving from compute to memory, power, integration or service;
- new products displacing the company's own old products;
- expected future supply changing current customer ordering and investor valuation.

The solution must conserve stock and flow. Use a constrained allocation/equilibrium procedure if sufficiently identified. Otherwise report feasible thresholds and the unresolved parameter; do not force one answer by choosing a convenient elasticity.

### 20.4 Shock register
Every factor has:
knowledge class, source and first-public timestamp, announcement time, economic start, ramp, duration, recovery or permanence, exposed share, grade/geography, financial transmission lags, customer/competitor response, and a falsifier.

Knowledge classes:
- OBSERVED_AT_CUTOFF;
- ANNOUNCED_FUTURE_EVENT;
- STRUCTURAL_INFERENCE;
- STRESS_ONLY_UNANNOUNCED;
- POST_ORIGIN_REALIZATION.

Examples: energy prices, FX, tariffs, financing costs, price letters, scheduled maintenance, known competitor projects, customer product launches, deferred tax changes, patent licenses, contract renewals, software inference costs, procurement freezes, freight disruption, abnormal weather and legal restrictions.

An announced event can enter the base forecast with its then-known terms. A not-yet-known event cannot be described as forecast fact; use an explicit stress test or exposure threshold. The observed value of a later shock can be used only in ex-post explanation.

### 20.5 Transmission is a convolution, not instant pass-through
For an externally observed shock z, the financial effect depends on exposure and lags:

    effect[t] = exposure[t] * sum_l(kernel[l] * shock[t-l])

Use separate kernels for customer prices, procurement, COGS, inventory financing, accounts receivable, hedges and investor recognition. Kernel weights come from contracts, observed cohorts or pre-cutoff calibration. They are not arbitrary haircut percentages.

Preserve temporary versus permanent effects. A one-off port closure can defer revenue; a permanently closed factory changes future capacity. A tax refund does not alter repeat customer value.

### 20.6 Rational responses
Model firms as constrained actors, not perfectly informed or perfectly aligned agents. Evaluate feasible actions at marginal economics:
- producer allocation by contribution per bottleneck-hour;
- customer adoption by surplus relative to feasible alternatives;
- investment by full-cycle return and financing;
- pricing by contracts, retention, rival capacity and lifetime account value;
- inventory by lead time, shortage cost and financing;
- maintenance/shutdown by contribution and reliability;
- buyback versus capex by per-share value and balance-sheet obligations.

Record incentive conflicts, strategic obligations, related parties and financing constraints. Preserve alternative best responses when private information prevents a unique game outcome.

---

## 21. Research depth: an explicit coverage system

### 21.1 Build a source corpus before summarizing it
For the target, collect five annual periods, preferably 28 quarterly observations, all available notes, management discussions, earnings releases, investor Q&A, material amendments, bond/convertible documents, compensation and related-party disclosures, major capital projects and acquisition material.

For short-history issuers, collect all available records. Do not invent missing history or claim statistically validated long-cycle prediction from a handful of quarters.

For related companies, cover material customers, direct rivals, private/captive substitutes, equipment vendors and key upstream suppliers. Start with two material nodes per chain direction; expand until additional nodes cannot change the material economic conclusions. Concentrated industries require all material competitors, not merely two convenient ones.

Keep Chinese A/H consolidated issuers as one economic entity with separate securities. Match parent/subsidiary and contract-manufacturer identities. A listed-company filing can reveal a private rival through customer procurement or project permits.

### 21.2 Three-pass source work
Pass A — complete document inventory:
record every page, table and note in scope, periods, revisions and extraction status.

Pass B — number and clue census:
extract all statement lines, numeric narrative, operational KPIs, commitments, maturity schedules, capacities, prices, percentages, dates, concentrations and material qualitative conditions.

Pass C — targeted causal investigation:
follow changed/contradictory items across periods and counterparties; acquire technical/customer/market sources to resolve the implied mechanism.

Search snippets locate evidence. They do not replace reading the relevant complete tables, notes and surrounding paragraphs. Read an embedded image or table visually when text extraction is incomplete; do not silently guess numbers.

### 21.3 Every scoped number has a disposition
Allowed states:
MAPPED; EXCLUDED_REASONED; CONFLICT_OPEN; UNREADABLE; UNREVIEWED.

Examples of reasoned exclusions: telephone number, page number, legal-registration identifier, duplicate with a canonical fact ID. Small financial amounts are not automatically irrelevant: an apparently small rebate, threshold, covenant or ownership change can be decisive.

Preserve original and normalized forms with:
entity; security; document/version; exact page/table/row; raw text; numeric value; unit/currency; observation and publication dates; consolidated scope; accounting standard; original/revised status; causal node; reviewer.

The requirement is 100% disposition of the declared corpus, not a false promise that no undisclosed or public detail anywhere can be missed. An unavailable document or unreadable table stays visible and can block a dependent conclusion.

### 21.4 Notes requiring deliberate review
Revenue gross/net and acceptance terms; segment changes; geographic versus customer-address differences; inventory costing and write-downs; supplier rebates; purchase commitments; capacity prepayments; capitalized development; useful-life changes; finance leases; factoring and supplier finance; receivable bills; customer advances; warranty; pension; tax assets; R&D deductions; subsidies; FX hedges; minority interests; related parties; covenants; convertible conversion; warrants and stock compensation.

Review the same item in several periods. A declining allowance ratio during increasing receivable age is a different clue from declining receivables with stable collections.

### 21.5 Contradiction-driven search
For each leading claim ask for its strongest falsifier.
- Tight supply: identify already-reserved equipment, rival commissioning and substitution.
- Superior ROI: identify installation failures, support cost and customers selecting alternatives.
- Pricing power: locate buyer procurement costs, discounts, volume losses and payment terms.
- Strong orders: inspect cancellations, duplicate bookings and financial ability to accept delivery.
- Profit quality: examine tax, capitalized costs, delayed accruals, related-party revenue and cash.
- Underpricing: determine what was announced before the rally and whether a denominator update caused apparent P/E compression.

Do not average facts with incompatible units. Resolve the definition or block the calculation.

### 21.6 Effort allocation and stop rules
Research effort is prioritized by decision sensitivity:
1. Does resolving the question change eligibility?
2. Could it reverse finalist order?
3. Does it materially change the target, margin or peak date?
4. Can an accessible source distinguish competing explanations?

The default 3-percentage-point upside sensitivity is a task-priority trigger, not a statistical confidence claim.

Continue retrieving until critical causal links have independent support or explicit blocking limitations. Stop repetitive searches when all results trace to one press release. Log dead ends, denied access and what alternative source could resolve them.

A final dossier must show sources read, not merely results returned; primary/secondary mix; time/grade coverage; dependence on management claims; unresolved materialities; and why the stopping point is defensible.

---

## 22. Forecast validation: train, validation, sealed test and live shadow

### 22.1 What is being trained?
Training can mean calibrating elasticities, lags, cohort conversion, cost slopes, yields, normal collection days, or choosing an agent prompt/model. It does not require training a neural network.

Report the fitted parameter count and economic identification. A 12-quarter sample cannot support a free parameter for every product, cost, lag and season. Use externally supported structure, matched-peer evidence and parsimonious models when history is short.

Fitting historical financials is not proof of causality. Compare alternative mechanisms that explain the same accounts. A precise EPS fit achieved by offsetting incorrect revenue and tax forecasts is not an identified business model.

### 22.2 Four distinct forecast lanes
A. STRUCTURAL_PRE_GUIDANCE:
forecast before company-specific preannouncement or guidance about the target result; evidence must precede that cutoff. State what management information is excluded.

B. GUIDANCE_ASSISTED_NOWCAST:
use legally available guidance or preannouncements as constraints. Score value added relative to that guidance; do not claim independent prediction of a disclosed number.

C. POST_RELEASE_ATTRIBUTION:
decompose a known result using the complete report. This is explanatory work, not predictive accuracy.

D. PROSPECTIVE_SHADOW:
freeze an actual forward forecast before the real event; score after it happens. No trade execution is implied.

Preserve separate rows, cutoffs and metrics. Retrofitting a revenue/margin bridge to a disclosed profit midpoint belongs in lane B or C.

### 22.3 Publication-time splits
A point-in-time data record has:
observation interval; first_public_at; issuer publication time; provider availability time; archive proof; retrieval time; version ID; and lineage.

A fact observed in March but first published in May is not available to an April forecast. A late restatement does not rewrite what was knowable in April.

Use the latest historically public version as of each origin, not today's latest database value. SEC XBRL frames can select last-filed facts and differing fiscal periods; SEC data therefore needs filing-level timestamp/version handling [M5]. ALFRED explicitly retains real-time vintages for revised economic observations [M3, M4].

Unknown time-of-day is not permission to assume pre-market availability. Use a conservative verified availability rule and store it.

### 22.4 Suggested chronological design
For an issuer with at least 28 usable quarters:
- 20 quarters: training;
- next 4 quarters: rolling validation for structure and hyperparameter selection;
- final 4 quarters: sealed test;
- next real disclosures: prospective shadow evaluation.

Illustration: 2019–2023 training, 2024 validation, 2025 sealed test. This is a protocol example, not an already-run backtest.

Twenty-eight quarters are not a universal sufficient sample. Cyclical industries may require a full prior peak, trough and recovery. New businesses may not permit a credible sealed historical test; mark historical accuracy unestablished and use prospective tests.

Within development, use rolling or expanding forecast origins, respecting legal feature and label availability. Multi-step forecasts must be evaluated at the intended 1-, 2- and 4-quarter horizons [M1].

### 22.5 Purging, embargo and grouping
Remove any training sample whose target outcome was not public at the fit cutoff. Remove training target intervals overlapping the held-out target interval when they would leak outcome information.

A fixed one-quarter embargo is not automatically correct. Determine the actual release/overlap path; use an embargo when needed, not as a ritual. TimeSeriesSplit's gap is a convenience, not full leakage control [M2].

For transfer tests, group parent/subsidiaries, cross-listed securities, tightly shared programs and duplicate documents. Do not train on a subsidiary's identical result while claiming its parent is an unseen company.

Using a supplier's earlier-public report to forecast a later-reporting customer can be legitimate live information. Disclose the cutoff and distinguish that operational nowcast from a deliberately strict chain-held-out generalization test.

### 22.6 Freeze what can be tuned
Before validation, register:
- structural equations and candidate variants;
- feature definitions and source versions;
- preprocessing and imputation fitted only in training;
- parameters, tuning budget and model complexity;
- agent model/version, prompts, tools and decoding settings;
- baseline forecasts;
- primary metrics and thresholds;
- handling of failed retrievals;
- allowed rolling update procedure;
- data groups, release calendars and test access policy.

After validation, freeze one procedure for the final test. Repeatedly inspecting test performance and adjusting the model converts the test into development data. Mark it honestly and reserve a new untouched period.

### 22.7 A seal is an access boundary
The evaluator and data custodian own the outcome store. Researchers receive only cutoff-filtered packets. Agent prompts saying 'do not look at Q4' do not constitute a seal.

Use separate stores, permissions, tool allowlists and immutable access logs. Keep tool caches, retrieval indexes and context summaries partitioned. A summary of future results is still leakage.

The included reference code validates timestamps and metadata. It is not an operating-system security boundary and does not enforce a hosted service's permissions. The production orchestrator must do so.

### 22.8 LLM memory contamination
A language model may know historical outcomes from pretraining even when the retrieval packet is clean. No instruction or filename partition erases that knowledge.

Label retrospective LLM evaluations as contamination-sensitive unless model/data provenance genuinely excludes the outcomes. Entity/date masking can reduce obvious cues but does not certify independence. Use deterministic numerical models on point-in-time packets and prospective shadow runs for stronger evidence. Research on financial LLM evaluation explicitly identifies look-ahead and related biases [M6].

Never describe a reconstructed 2023 forecast generated by a later-trained model as pristine out-of-sample prediction merely because current retrieval was time-filtered.

### 22.9 Score more than EPS
Predeclare:
- revenue MAE or scaled error;
- volume and comparable-price error;
- gross/operating margin error in basis points;
- operating expense and tax error;
- diluted-share error;
- EPS absolute error, with care around losses;
- CFO/FCF error;
- inventory and receivable error;
- forecast direction and turning-point timing;
- price-target error, recognition timing and ranking performance, scored separately.

Avoid MAPE when denominators are zero or near zero. MASE scales must be computed from training data only. Use simple seasonal-naive, run-rate and lane-appropriate guidance baselines [M7].

Financial accuracy does not validate a share-price forecast. Report whether earnings were right, the recognition event occurred, and valuation responded as expected.

### 22.10 No universal synthetic pass threshold
Synthetic checks verify arithmetic and safeguards. They do not validate investment prediction.

For real models, set thresholds from the business's historical noise, economic materiality and a predeclared baseline. Do not demand a fabricated universal 95% forecast accuracy. A primary error improvement and no material deterioration in critical subordinate drivers is more defensible than a single opaque quality score.

---

## 23. New factors inside the forecast period

Historical fit is insufficient when the operating system changes.

### 23.1 Register them before the forecast
At every origin run a forward-factor sweep:
- price-effective dates and renewals;
- cost index resets and inventory age;
- launches and qualifications;
- capacity startups, cold repairs and equipment delivery;
- announced customer funding or cancellations;
- patent licenses, litigation and royalty changes;
- acquisitions/divestitures and consolidation dates;
- foreign exchange and hedge maturities;
- interest refinancing;
- new tariffs, taxes, subsidies or reimbursement;
- warranty/failure evidence;
- working-capital terms;
- capital issues and convertibles.

Each factor gets an evidence date, causal channel, exposure, unit, earliest effect, maximum feasible effect, duration and reversal condition.

A known future event belongs in the live path even if historical training never contained it. Set its parameter from engineering or contractual evidence rather than estimating it from an unrelated historical regression.

### 23.2 Keep announced, inferred and unforeseen factors separate
For announced factors, model the disclosed terms and plausible operational lags.
For inferred structural changes, show the mechanism, precedent and unsupported parameters.
For unannounced shocks, run deterministic exposure/threshold tests; do not insert a convenient imagined event into the main forecast.
For realized surprises, create a post-origin attribution version. Never change the original forecast file.

### 23.3 Diagnose surprise without erasing the forecast error
The postmortem decomposes:
- end-demand miss;
- adoption-economics miss;
- competitor/share miss;
- supplied quantity/yield miss;
- contract price/mix miss;
- input-cost recognition miss;
- expense/tax/accounting miss;
- cash-timing miss;
- event arrival/timing miss;
- investor-belief/valuation miss;
- unexplained residual.

An announced factory opening that the analyst failed to include is an omission, not an unforeseeable shock.
A new regulation published after the origin is an unforeseen event for that forecast; its realized effect does not make the original numerical error disappear.
A missed customer loss is not automatically 'management execution'; it may invalidate the technology or cost-surplus comparison.

### 23.4 Report the contribution of new information
Versioned updates show:

    original target
      + changed long-run economics
      + changed event timing
      + changed expected accounting/cash transmission
      + changed market-belief or valuation assumption
      + interaction
      = revised target

Choose an exact decomposition convention and disclose interaction terms. For nonlinear models, a Shapley-style attribution or order-averaged bridge may be used, but only as attribution, not causal proof.

---

## 24. Agent instructions, access rules and handoffs

### 24.1 Universal agent response contract
Return a structured object containing:
task_id; role; run/candidate IDs; cutoff; permitted partitions; question; sources actually read; source and claim IDs; calculations; findings; conflicting evidence; unobserved values; requested follow-ups; affected model nodes; artifact hash; reviewer; and status.

Status is COMPLETE, BLOCKED or NEEDS_REVIEW. No agent may promote its own unsupported premise to 'observed' to finish a task.

### 24.2 Tool and retrieval discipline
- Read/search native company/exchange/regulator material first for financial numbers.
- Use industry research for external prices, shipment estimates and technical context, preserving attribution.
- Use news to discover events and counterparty links; return to original documents for load-bearing numbers.
- Read the relevant contiguous report section, not only a snippet.
- Store original files, text and selected page images with hashes; record extraction errors.
- Query by entity, product grade, period, event and counterparty; search both supportive and adverse formulations.
- Do not claim an external specialist has been consulted if the work is only performed by a separate analytical lane.

### 24.3 Coverage budget
Suggested starting coverage remains 12 market pools, roughly 60 first-pass names and six deeply comparable finalists. These are research-planning defaults, not quotas proving completion.
For each finalist, require the full target corpus, major rivals, at least two relevant upstream and two downstream entities or proxies, and all known market-changing projects.

Increase effort where a missing datum can change ranking. Stop broad exploration when the deciding issue is narrow. Preserve rejected names and why they failed so the universe does not become a retrospective selection of winners.

### 24.4 Handoff acceptance
The receiving agent checks:
- correct cutoff and source versions;
- units and product boundaries;
- facts versus claims versus assumptions;
- independence and conflicts;
- formula lineage;
- execution constraints;
- parameter sensitivity;
- whether the handoff actually resolves its assigned question.

A handoff rejected for missing evidence returns to its owning role. It is not silently patched by the valuation agent.

### 24.5 Update propagation
A changed fact invalidates all downstream dependencies:
customer NPV -> adoption -> demand -> supply/price -> share -> financials -> expectations -> target -> rank.

Recompute only affected nodes, but rerun dependent gates and preserve the prior version. A new rival qualification can matter more than the target company's earnings release.

### 24.6 Avoid long-run scope drift
The final eligible ranking remains two-month price appreciation by default. Long-run modeling supports the future state being repriced; it does not replace the ranking with company quality, terminal value or a five-year target.

The target must distinguish what is public now, what may become public before the horizon and what economics will occur afterward. Never assume every public fact is fully priced or every favorable fact is ignored.

---

## 25. Required operational deliverables and honest limitations

For each finalist publish:
1. Source and document census with complete dispositions.
2. Demand-source and funding map.
3. Matched technology/alternative dossier.
4. Customer choice and adoption cohorts.
5. Competitor capacity and strategic-response ledger.
6. Grade/period balance and realized-price/cost model.
7. Multi-timescale operating and cash model.
8. Anticipated-factor and unannounced-stress register.
9. Chronological validation protocol and frozen forecast receipts.
10. Out-of-sample and prospective performance, or a clear 'not established' label.
11. Financial-driver residual bridge.
12. Fixed-year expectations and P/E decomposition.
13. Two-month information-recognition path and one point target.
14. Candidate-specific gates, red-team objections and stopping justification.

The full numeric census is an audit record, not a requirement to print every disclosure in the executive summary. The public summary highlights decisive evidence and provides the audit trail.

The protocol seeks no hidden load-bearing assumptions, not false certainty. Private prices, undisclosed yields, non-public project delays and unannounced shocks may remain unknown. A model can be economically reasoned and still empirically underidentified. Block or narrow the claim where that affects the winner.

---

## 26. Worked synthetic design principles

All workbook demonstrations are invented and cannot support a real investment recommendation.

### Customer example
An installation costs 18,000 including integration. It produces 15,000 annual contribution/energy benefits, with 3,000 additional annual service costs. Over five years at a 10% customer hurdle rate:
- net annual benefit: 12,000;
- payback: 1.5 years;
- NPV: approximately 27,489.

A second cohort with only 6,000 annual net benefit has positive NPV but a three-year payback. If that cohort's budget rule requires two years, demand remains blocked until economics or financing change.

The first cohort can still deploy only as many systems as its funding, qualification and integrator slots permit. An economically eligible population of 400 is not 400 installations if only 120 slots are available.

### Contract example
A price increase from 100 to 120 applies to only 30% of delivered units. Recognized ASP is 106, not 120. Cost inflation flows through inventory vintages on a different schedule. The resulting margin must be calculated, not inferred from the headline price letter.

### Holdout example
A model is frozen before each quarterly result. The evaluator scores both the causal estimate and a seasonal baseline. An after-origin realized input price can explain the miss afterward but cannot be inserted into the original forecast features.

### Price example
A late-quarter disclosure can change next year's capacity belief before production arrives. The observed operating event and its public information event are modeled as different dates. The two-month target uses the information date without pretending future revenue has already been earned.

---

## 27. Source notes for the validation design

This framework is an authored methodology. The following external references support specific data-handling and forecast-validation safeguards; they do not validate a stock-picking strategy.

[M1] Hyndman & Athanasopoulos, rolling forecasting origins: https://otexts.com/fpp3/tscv.html
[M2] scikit-learn, TimeSeriesSplit: https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html
[M3] Federal Reserve Bank of St. Louis, ALFRED: https://fred.stlouisfed.org/docs/api/fred/alfred.html
[M4] FRED API real-time periods: https://fred.stlouisfed.org/docs/api/fred/realtime_period.html
[M5] SEC EDGAR APIs: https://www.sec.gov/search-filings/edgar-application-programming-interfaces
[M6] Kong et al., Evaluating LLMs in Finance Requires Explicit Bias Consideration, research preprint: https://arxiv.org/abs/2602.14233
[M7] Hyndman & Athanasopoulos, forecast accuracy: https://otexts.com/fpp3/toolbox.html

References checked 2026-10-25. Retrospective model-memory contamination remains a limitation even with carefully versioned retrieval.


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

## Appendix C. Executable research checklist

- **T01 | Mandate | O00 | G00: Freeze the final objective.** Resolve universe, A/ADR/H class rules, horizon, currency, dividends, liquidity constraints and source cutoff. Output: Run contract.

- **T02 | Mandate | A01 | G01: Validate the clock.** Record quote time, timezone, last completed exchange session, target exchange session and report availability. Output: Clock map.

- **T03 | Evidence | A01 | G02: Quarantine prior work.** Extract prior claims as hypotheses; reopen original filings before reusing any numeric claim. Output: Quarantine log.

- **T04 | Evidence | A01 | G02: Preserve source lineage.** Store publication and observation dates, original author, archive/hash and exact page/table. Output: Source ledger.

- **T05 | Evidence | A01 | G02: Distinguish fact types.** Tag observed fact, company claim, derivation, model assumption, unresolved or contradicted. Output: Claim ledger.

- **T06 | Discovery | A03 | G00: Explore independently.** Map at least 12 distinct market pools before narrowing; include slower markets with valuation dislocations. Output: Market-pool inventory.

- **T07 | Discovery | A03 | G14: Record rejection logic.** Log every screened name, evidence depth and reason; a shallow screen is not a completed valuation. Output: Universe log.

- **T08 | Discovery | A03 | G04: Seek adjacent beneficiaries.** Trace where customer spend and supplier profit move after each bottleneck is relieved. Output: Beneficiary graph.

- **T09 | Macro | A02 | G04: Decompose rates.** Separate risk-free rates, credit spreads and refinancing exposure; distinguish demand-financing from valuation effects. Output: Rate transmission.

- **T10 | Macro | A02 | G09: Trace FX.** Separate revenue translation, input currency, monetary balances, hedges and OCI. Output: FX exposure map.

- **T11 | Macro | A02 | G06: Trace energy and logistics.** Map electricity, fuel, feedstock, freight and route/insurance changes to specific stages and lags. Output: Input transmission.

- **T12 | Macro | A02 | G04: Trace policy mechanically.** Record enacted rules, dates and affected geography; separate announcements from effective implementation. Output: Policy transmission.

- **T13 | Macro | A02 | G04: Separate real demand from inflation.** Split nominal growth into units, price, mix and currency; distinguish bookings and installed utilization. Output: Macro-to-units bridge.

- **T14 | Chain | A04 | G05: Define the unit.** Choose grade, specification, width/area/weight, voltage/rate, geography and period before counting supply. Output: Unit dictionary.

- **T15 | Chain | A04 | G05: Draw physical and cash flows.** Record buyer/supplier links, captive use, inventory owners, payment terms and revenue recognition. Output: Chain map.

- **T16 | Chain | A04 | G05: Find shared bottlenecks.** Identify common foundries, tooling, skilled labor, power, qualification and equipment vendors. Output: Constraint map.

- **T17 | Demand | A05 | G04: Build end-customer deployment cohorts.** Start with named projects/customers and funded units; separate orders, cancellations, installations and utilization. Output: Demand cohorts.

- **T18 | Demand | A05 | G04: Model content.** Derive material/device content from BOM, layers, channels, links, compute or service workloads. Output: Content model.

- **T19 | Demand | A05 | G03: Model economic adoption.** Calculate break-even thresholds by customer type; estimate the addressable subset, not all nominal units. Output: Adoption map.

- **T20 | Demand | A05 | G04: Model replacement and inventory.** Track product lifetime, installed base, stock drawdowns, restocking and channel duplication. Output: Consumption/order bridge.

- **T21 | Demand | A05 | G04: Check funding and complements.** Cap deployments by financing, permits, power, skilled labor, supporting components or reimbursement. Output: Feasible-demand cap.

- **T22 | Demand | A05 | G04: Independent demand cross-check.** Compare bottom-up units with physical output/shipments and competitor/customer reports. Output: Demand reconciliation.

- **T23 | Supply | A06 | G05: Inventory every material project.** Track announced, funded, equipment secured, built, commissioned, qualified and ramping capacity. Output: Capacity ledger.

- **T24 | Supply | A06 | G05: Reconcile dates across periods.** Compare original schedules, revisions, actual starts, cancellations and delays. Output: Project change log.

- **T25 | Supply | A06 | G05: Convert nameplate to effective output.** Convert annual capacity to period output; apply stage limits, uptime, yield and customer qualification. Output: Qualified supply.

- **T26 | Supply | A06 | G05: Model grade allocation.** Use machine-hours or equivalent constraints; faster growth of one grade can reduce another grade's supply. Output: Allocation model.

- **T27 | Supply | A06 | G08: Include rational competitor response.** Model output increases, cold repairs, debottlenecking, substitution, imports and new entrants. Output: Response paths.

- **T28 | Supply | A06 | G05: Avoid double counting.** Remove captive/intermediate duplication; reconcile parent/subsidiary and OEM/foundry quantities. Output: Supply audit.

- **T29 | Price | A07 | G06: Build comparable price series.** Match grade, unit, tax/freight basis, region, currency, order size and contract duration. Output: Price ledger.

- **T30 | Price | A07 | G06: Separate announced and realized pricing.** Build order cohorts with effective dates, renegotiation scope, discounts and delivery lags. Output: Realized ASP model.

- **T31 | Price | A07 | G09: Trace input cost into COGS.** Match procurement cohorts, inventory method, production and sale timing; separate capex inputs. Output: Cost-roll-through model.

- **T32 | Price | A07 | G06: Prove bargaining power.** Compare seller price/cost/volume with buyer procurement costs, margins, retention and payment terms. Output: Surplus-allocation bridge.

- **T33 | Price | A07 | G06: Find normalization mechanism.** Determine marginal supplier, substitutable capacity, customer alternatives and expected inventory balance. Output: Multi-period price path.

- **T34 | Technology | A08 | G03: Compare like for like.** Control workload, process, reach, power, accuracy, reliability, environment and system boundary. Output: Benchmark matrix.

- **T35 | Technology | A08 | G03: Convert component to system gain.** Apply workload fractions and other constraints; do not extrapolate a component maximum to the full system. Output: System benefit model.

- **T36 | Technology | A08 | G07: Include alternatives and future roadmaps.** Compare do-nothing, internal design, incumbents, substitutes and feasible rival roadmaps. Output: Counter-technology map.

- **T37 | Technology | A08 | G03: Classify maturity.** Separate simulation, prototype, qualification, pilot shipment, volume production and fleet results. Output: Maturity ledger.

- **T38 | Customer economics | A09 | G03: Build full lifecycle TCO.** Include redesign, integration, downtime, training, certification, support, financing and replacement. Output: Customer TCO.

- **T39 | Customer economics | A09 | G03: Prevent benefit double counting.** Do not count freed labor as both cash saving and incremental output; use contribution, not gross revenue. Output: Economic audit.

- **T40 | Customer economics | A09 | G07: Model switching symmetrically.** Measure cost to adopt and cost to leave; assess multisourcing, contract renewal and open-source ownership. Output: Switching-cost map.

- **T41 | Competition | A10 | G07: Construct the real denominator.** Define merchant versus captive, geography, applications, value share and unit share. Output: Contestable SAM.

- **T42 | Competition | A10 | G07: Build design-win/retention cohorts.** Track eligible programs, nominations, qualification, production units, losses, cancellations and renewal. Output: Share conversion model.

- **T43 | Competition | A10 | G10: Validate share independently.** Check wins/losses, market-normalized shipments, gross profit per unit and competitor response. Output: Share validation.

- **T44 | Operations | A11 | G08: Model rational resource allocation.** Optimize contribution per constrained hour/unit, not price per item; include commitments and financing. Output: Management response.

- **T45 | Operations | A11 | G08: Test management incentives.** Examine compensation, related parties, acquisitions, dilution, capitalized costs and reinvestment returns. Output: Incentive exceptions.

- **T46 | Financials | A12 | G09: Build multi-period panel.** Default: 12 quarters plus five annual periods; include a complete prior supply cycle where material. Output: Comparable panel.

- **T47 | Financials | A12 | G09: Normalize reporting.** Reconcile fiscal calendars, units, share changes, consolidations, tax, acquisition mix and recurring items. Output: Normalization bridge.

- **T48 | Financials | A12 | G09: Decompose revenue and gross profit.** Separate volume, like-for-like price, mix, FX, acquisitions and new products; leave no invented residual. Output: Price-volume-mix bridge.

- **T49 | Financials | A12 | G09: Build cost and expense cohorts.** Map materials, inventory, yield, labor, depreciation, freight, R&D, SBC and financing separately. Output: Forward statements.

- **T50 | Financials | A12 | G09: Reconcile cash and dilution.** Bridge NI to CFO, capex, acquisitions, debt, leases, convertibles, buybacks and period-end cash. Output: Cash/share bridge.

- **T51 | Validation | A15 | G10: Freeze a holdout quarter.** Calibrate with earlier data; test a withheld quarter before incorporating it into the model. Output: Backtest residuals.

- **T52 | Validation | A15 | G10: Classify deviations.** Separate demand, supply, price, mix, share, execution, timing, tax and one-offs. Output: Error attribution.

- **T53 | Expectations | A13 | G12: Build point-in-time valuation history.** Use price and earnings available on that date; handle splits, rights, dividends and updated denominators. Output: Historical PE bridge.

- **T54 | Expectations | A13 | G11: Keep business and belief states separate.** Construct several conditional belief vectors compatible with today's price, not a unique implied consensus. Output: Belief-state map.

- **T55 | Expectations | A13 | G11: Test already-public information.** Identify preannouncements, scheduled events and prior price response; distinguish fact availability from investor understanding. Output: Known/unknown ledger.

- **T56 | Catalyst | A14 | G11: Map information to recognition.** For each in-window event, name the later operating variable and expectation it changes. Output: Catalyst bridge.

- **T57 | Valuation | A13 | G12: Keep a common earnings denominator.** Show price-change decomposition using the same future fiscal year and explicit dilution. Output: Target bridge.

- **T58 | Valuation | A13 | G12: Cross-check price, cash and market share.** Use demand/share economics, suitable multiples and properly discounted cash; reconcile discrepancies. Output: Valuation reconciliation.

- **T59 | Valuation | A13 | G12: Test cycle/terminal consistency.** Growth, reinvestment, ROIC, payout, capex and margins must coexist economically. Output: Duration audit.

- **T60 | Red team | A15 | G13: Attack the winning premise.** Find earlier rival capacity, weaker customer surplus, channel inventory, false exposure and double-counted options. Output: Counter-thesis.

- **T61 | QA | A16 | G14: Run hard numerical checks.** Check mass balance, shares, dates, period subtraction, units, cash and forecast timestamp availability. Output: Audit report.

- **T62 | Publication | O00 | G14: Publish one point path per eligible candidate.** Rank horizon appreciation only; show risks and break-even thresholds separately, without probability weighting. Output: Decision worksheet.

- **T63 | Monitoring | O00 | G14: Update only changed inputs.** Propagate new source facts through dependency graph; log target/rank changes and causes. Output: Versioned change log.

- **T64 | Postmortem | A16 | G14: Assess without hindsight.** Compare operational forecasts, expected belief changes, multiple changes and actual price separately. Output: Learning ledger.

- **T65 | Corpus | A17 | G16: Create the disclosure universe** List target filings, corrections, acquisition documents, subsidiaries, bonds, notes and all material chain peers by period. Output: Document manifest.

- **T66 | Corpus | A17 | G16: Enumerate every quantitative disclosure** Capture every amount, ratio, unit, schedule and numeric narrative in scoped documents; record exclusions, unreadable cells and duplicates. Output: Number census.

- **T67 | Corpus | A17 | G16: Read notes that alter small denominators** Review taxes, inventory provisions, rebates, SBC, receivable terms, guarantees, covenants, leases, factoring and capitalized costs even when small. Output: Footnote-to-driver map.

- **T68 | Corpus | A01 | G18: Preserve original and restated versions** Store first release and each correction; never replace original forecast labels silently with restated financials. Output: Vintage ledger.

- **T69 | Corpus | A17 | G16: Diff consecutive report wording** Compare changes in delivery language, price terms, capacity milestones, customer concentrations and removed disclosures. Output: Text and table change log.

- **T70 | Coverage | A23 | G23: Expand related-company coverage adaptively** Start with buyers, suppliers and rivals; recursively follow any newly revealed material dependencies or substitute capacities. Output: Exposure graph.

- **T71 | Coverage | A23 | G23: Document original source independence** Group syndicated reports, repeated management quotes and commissioned research under their originating evidence cluster. Output: Origin map.

- **T72 | Customer | A18 | G15: Segment the economic decision maker** Separate operator, budget holder, OEM, channel, end user and regulator; identify who gains and who pays. Output: Customer decision map.

- **T73 | Customer | A18 | G15: Compare feasible alternatives** Price incumbent renewal, defer, internal build, substitute product and best challenger under identical workload and lifecycle. Output: Choice set.

- **T74 | Customer | A18 | G15: Model adoption and switching separately** Separate initial introduction, incumbent-exit friction and future exit cost; include dual-running, financing, certification and retraining. Output: Incremental NPV.

- **T75 | Customer | A18 | G15: Derive willingness-to-pay ceilings** Solve price that leaves hurdle NPV/payback satisfied; distinguish total ecosystem surplus from supplier pricing capture. Output: Reservation-price schedule.

- **T76 | Customer | A18 | G15: Translate ROI to fundable cohorts** Identify budgets, capex cycles, procurement deadlines, minimum return and cash affordability before allocating adoption. Output: Funded demand cohorts.

- **T77 | Customer | A18 | G15: Apply physical deployment bottlenecks** Cap economic demand by integrators, power, permits, reliability validation, personnel, components and allowed commissioning slots. Output: Deployable demand.

- **T78 | Customer | A18 | G17: Model replacement, deferral and cannibalization** Track installed stock age, early replacement, reuse, competing generations and retirements; count each opportunity once. Output: Stock-flow model.

- **T79 | Dynamics | A19 | G17: Choose timescales by economics** Use event/daily clocks for shocks, monthly near-term operations, quarterly finances and annual lifecycle; never stop at price horizon. Output: Calendar and bridge.

- **T80 | Dynamics | A19 | G17: Link learning curves to adoption** Estimate cost/yield learning from pre-cutoff history; let price declines expand addressable cohorts without assuming perfect supplier capture. Output: Endogenous adoption curve.

- **T81 | Dynamics | A19 | G17: Model rivals' constrained responses** Allocate shared capacity by contribution per bottleneck-hour and funded expansion NPV, with contracts and incentive constraints. Output: Response ledger.

- **T82 | Dynamics | A19 | G17: Check equilibrium and conservation** Reconcile supplies, purchases, stocks and consumption; rerun customer choice after pricing changes; report no-convergence instead of forcing a price. Output: Balance audit.

- **T83 | Shocks | A19 | G21: Register anticipated new factors** Before each forecast, enumerate announced price letters, contract renewals, shutdowns, capacity starts, funding maturities, subsidies, FX hedges and taxes. Output: New-factor register.

- **T84 | Shocks | A19 | G21: Separate expectation from physical effect** Store announcement, effective date, delivery, COGS recognition, cash and investor-recognition dates independently. Output: Transmission schedule.

- **T85 | Shocks | A19 | G21: Model amplitude, duration and recovery** Specify evidence-based intensity, exposure, decay/ramp and management response; distinguish transitory levels from structural slope changes. Output: Shock kernel.

- **T86 | Shocks | A15 | G21: Stress events not forecastable ex ante** Apply deterministic exposure tests for unannounced interruptions or customer loss; label them stresses, not primary-path predictions. Output: Fragility tests.

- **T87 | Validation | A20 | G19: Declare forecast lanes** Separate unguided structural forecast, guidance-assisted nowcast, post-release attribution and forward paper test. Output: Lane registry.

- **T88 | Validation | A22 | G18: Enforce source lineage recursively** An input is unavailable if any required ancestor or revised version became public after forecast origin. Output: Availability graph.

- **T89 | Validation | A20 | G19: Design chronological splits** With adequate history use a 20-quarter training, 4-quarter validation, 4-quarter sealed test illustration; adjust to real economic cycle. Output: Split manifest.

- **T90 | Validation | A20 | G19: Define grouped and regime holdouts** Group issuer families and tightly linked programs when testing transfer; reserve entire adverse and expansion regimes rather than isolated lucky quarters. Output: Group/regime map.

- **T91 | Validation | A20 | G19: Purge overlapping target information** Exclude training labels not available by each origin and remove overlaps in target intervals; use embargo only for identified leakage paths. Output: Purged split audit.

- **T92 | Validation | A20 | G19: Select benchmarks and metrics in advance** Use seasonal naive, run-rate and guidance baselines; define revenue errors, margin-bps errors, EPS dollar errors and cash-flow errors. Output: Metric contract.

- **T93 | Validation | A20 | G19: Lock the feature and prompt search budget** Record every tried structural model, prompt version and hyperparameter choice; do not select retrospectively on the final test. Output: Experiment registry.

- **T94 | Validation | A22 | G18: Seal target access** Enforce separate input and label paths, evaluator-only permissions and redacted tool responses; do not trust prompt instructions as an access boundary. Output: Access manifest.

- **T95 | Validation | A21 | G20: Freeze and hash each forecast** Save source versions, model code, prompts, parameters, seed, horizon and predictions before a target result is accessible. Output: Forecast receipt.

- **T96 | Validation | A21 | G20: Score once and preserve the result** Evaluate sealed targets under registered metrics; any later retuning begins a new experiment and cannot reuse the same test as pristine. Output: Blind evaluation.

- **T97 | Validation | A22 | G24: Audit LLM historical contamination** Mark all retrospective LLM tests as contamination-sensitive unless historical outcomes could not be known; prefer prospective shadow tests. Output: Contamination disclosure.

- **T98 | Validation | A21 | G24: Run prospective paper forecasts** Before each future release, archive predictions and input packet; score when public results arrive without respecifying the old forecast. Output: Forward record.

- **T99 | Validation | A12 | G20: Separate as-reported and restated error** Score first-public actuals for announcement prediction and subsequently restated outcomes for economic truth, with separate series. Output: Dual-label score.

- **T100 | Validation | A21 | G22: Detect compensating errors** Check volume/price/cost/tax/share forecasts individually even when aggregate EPS is accurate. Output: Driver error bridge.

- **T101 | Validation | A21 | G22: Attribute shocks without hindsight rescue** Explain post-release changes in an attribution notebook only; keep the original blind loss and label new evidence after-origin. Output: Postmortem.

- **T102 | Finance | A12 | G16: Build a change driver for every material line** Map price, units, FX, tax, useful lives, rebates, cost cohorts, cash timings and consolidation; residuals stay explicit. Output: Line-item driver tree.

- **T103 | Finance | A12 | G22: Reconcile cash with commercial timing** Use payment contracts and actual collection history; advances, factoring and notes are not revenue or automatic bargaining power. Output: Cash mechanism.

- **T104 | Finance | A12 | G23: Audit incentives and related entities** Follow parent/subsidiary value capture, transfer pricing, external contracts, minority interests and capital allocation. Output: Entity economics.

- **T105 | Expectations | A13 | G22: Maintain identical-year expectations bridges** Keep current inferred and target beliefs on the same fiscal EPS year; distinguish earnings revisions, discounting, multiple changes and interaction. Output: Price bridge.

- **T106 | Expectations | A14 | G17: Test information beyond the price window** Identify pre-horizon disclosures about late-period capacity or adoption; do not discard later economics because realized revenue is outside window. Output: Recognition map.

- **T107 | Coverage | A23 | G23: Rank remaining research questions** Prioritize missing inputs by eligibility effect, target sensitivity and ability to reverse finalist ordering—not source volume. Output: Search queue.

- **T108 | Coverage | A23 | G23: Log negative and absent disclosures** Capture discontinued KPIs, denials, cancellations, contradictions and searched-but-unavailable fields with scope and dates. Output: Missingness audit.

- **T109 | QA | A16 | G16: Audit source-to-cell traceability** Every reported numeric input maps to a fact and source locator; every modeled number maps to an assumption, formula and sensitivity. Output: Lineage check.

- **T110 | QA | A16 | G24: Run synthetic mutation tests** Reject future sources, derived leakage, unsealed tests, material untriaged numbers, adoption over deployment capacity and invalid units. Output: Validator report.

- **T111 | QA | A15 | G23: Re-evaluate the decision boundary** Do not allow best-looking model fit to override missing material economics; compare eligibility and target separately. Output: Challenge verdict.

- **T112 | Publication | O00 | G24: Publish evidence coverage and test posture** Show corpus scope, coverage limitations, forecast lane, holdout performance and contamination status next to the point target. Output: Research packet.

- **T113 | Publication | A16 | G22: Produce a change-attribution release** Explain how new source evidence changed demand, prices, margins, cash, expectations and target; preserve all prior versions. Output: Version delta.

- **T114 | Publication | O00 | G24: Retain a no-winner outcome** Do not force a ranked winner when a missing fact or failed validation decides ordering; publish the blocking question. Output: Eligibility decision.

## Appendix D. Sector-specific operating modules

The orchestrator selects a module after defining the customer's problem. It must not force a manufacturing template onto a software or regulated-service business.

| Business type | Demand unit and denominator | Effective supply / constraint | Pricing and margin mechanism | Special financial cross-check |
|---|---|---|---|---|
| Memory and commodity materials | Bits, tonnes or standardized grade/area consumed; inventory separately | Good output by generation/grade; conversion trade-offs; shutdowns and new equipment | Marginal supply, contract/spot lag, customer inventory and substitution | Inventory gains versus replacement costs; capitalized costs; full prior price cycle |
| Semiconductor components | Qualified sockets, channels, links or packages per system | Foundry/assembly/test bottlenecks plus customer qualification | Content mix, design retention, competitive bids and integration value | Customer concentration, sell-in/sell-through, inventory and distributor rebates |
| Semiconductor IP | New designs, reusable programs, licensed content, production units for royalties | Engineering support and qualified ecosystem rather than fab capacity | License terms, royalty bases, reuse, switching cost, customer in-house alternative | Design starts versus recognized ACV/revenue/royalty cohorts; SBC and deferred revenue |
| Industrial equipment | Funded customer capacity additions and replacements | Order engineering, skilled labor, machining, testing, installation and acceptance | Qualified scarcity, warranties, total lifecycle cost and service | Backlog cancellations, advances, milestone recognition, warranty provisions and working capital |
| Software / AI workflow | Active workloads, retained customers, paid usage and conversion | Product reliability, permissions/data integration, distribution and support | Measured customer surplus, competition, bundling and deployment cost | Organic ARR, retention, billings/RPO, deferred revenue, SBC and cash timing |
| Advertising platform | Advertiser spend that meets incremental-return hurdles | Qualified inventory, outcome data, attribution and advertiser access | Incremental advertiser profit, auction alternatives and platform rules | Gross/net presentation, pass-through traffic costs, concentration and model-release effects |
| Credit / underwriting platform | Creditworthy funded originations, not applications | Lender approval, warehouse funding, investor risk appetite and securitization | Borrower/lender/investor surplus; losses by vintage; funding spread | Retained credit exposure, restricted cash, gain-on-sale, loan performance and financing availability |
| Clinical technology / diagnostics | Eligible procedures/tests multiplied by reimbursed adoption | Clinical workflow, approvals, payer coverage, laboratories and trained staff | Clinical utility, reimbursement, avoided treatment costs and competition | Collection rates, payer denials, billing lag, evidence by indication and amortized acquisition costs |
| Space / physical networks | Serviceable users/workloads under link/coverage constraints | Operational assets, launches, spectrum, geography, ground infrastructure and replacement | Capacity per service area, utilization, retail/wholesale terms and competitive reach | Treat partner subscriber bases as distribution reach, not paying users; capex, replenishment and dilution |
| Robotics / perception | Economically justified deployed workcells/devices by task | Integrator throughput, reliability, workforce training and customer qualification | Installed TCO, intervention rate, uptime, payload/task fit and fleet learning | Product versus services revenue, acceptance delays, hardware price deflation and mix |

For all modules, model future customer alternatives. Lower input cost can expand final demand while reducing supplier ASP; rising unit shipments alone do not prove expanding profits.



## Appendix E. Reference orchestration pseudocode

    mandate = lock_mandate_and_common_price_clock()
    protocol = preregister_forecast_lanes_splits_metrics_and_allowed_updates()
    custodian = create_partitioned_source_and_label_access()
    hypotheses = quarantine_prior_assistant_claims()
    markets, candidates = explore_unrelated_markets_with_recorded_rejections()
    for market in markets:
        documents = census_original_filings_and_material_chain_entities(market)
        facts = extract_all_scoped_numbers_and_qualifiers(documents)
        facts = as_of_filter_with_recursive_lineage(facts, mandate.cutoff)
        chain = define_grade_units_inventory_owners_and_entity_links(facts)
        technology, supply, customers = independent_parallel_research(chain)
        economics = compare_customer_choices_and_adoption_costs(technology, customers)
        demand = build_funded_qualified_deployable_cohorts(economics)
        events = preregister_known_factors_and_stress_only_unknowns()
        dynamics = solve_demand_supply_prices_and_rival_responses(demand, supply, events)
        for company in comparable_finalists(market):
            forecasts = build_financials_from_operating_states(dynamics, company)
            receipt = freeze_hash_sources_model_prompts_and_forecasts(forecasts)
            scores = evaluator_score_without_modeler_test_access(receipt, protocol)
            if scores_or_evidence_block_the_claim:
                return_to_owning_research_task_without_target_retrofit()
            expectations = map_information_to_multi_year_market_beliefs()
            target = construct_common_year_price_bridge(expectations, forecasts)
            red_team_and_auditor_check_every_material_dependency()
            if every_required_candidate_gate_passes:
                publish_one_point_target_and_separate_sensitivities()
    rank_eligible_candidates_only_by_horizon_share_price_upside()
    preserve_as_original_every_receipt_source_and_rejection()
    # New evidence requires a new explicitly invoked run or authorized task.
    # This specification itself performs no background monitoring.

## Appendix F. Final publication requirements

State: reference price/time, target session, operating model years, point target/upside, current source vintage, corpus coverage, unobserved decisive parameters, forecast lane, holdout/forward-test status, customer economic threshold, qualified supply and competitor response, pricing/cost lags, financial tie-out, expectation revision, fixed-year multiple decomposition, and falsifying observations.

Never call hypothetical values reported facts, call a reconstruction a forecast, claim a source count proves economic identification, or call a synthetic validator result predictive success.
