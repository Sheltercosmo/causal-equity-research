# Reusable evidence and causal maps

O00 owns a project-level library at `research/library/` and each run's frozen references under `research/runs/<run-id>/`. Create library records when actual research is accepted; do not populate live evidence with the bundled synthetic examples. The retired pre-v2 archive remains excluded. Prior active-run analysis is a locator and hypothesis; verify original material before promoting a numeric claim to reusable evidence.

## Store once; reuse by scope and vintage

Keep immutable/versioned source material and accepted claim versions rather than repeatedly summarizing company stories. Minimal records:

| Record | Fields that prevent unsafe reuse |
|---|---|
| Source | Stable source ID, original URL/file/hash, issuer/origin cluster, publication and provider availability, period, revision, locator and extraction limits |
| Claim | ID/version, classification, value/unit/definition, source and ancestor IDs, observation interval, product/grade/geography/cohort, conflicts, first availability, review/expiry rule |
| Entity/node | Issuer/security distinction; product, facility/resource, customer cohort, program, inventory owner, contract or event; aliases and scope |
| Edge | IDs/from/to, relation, physical/payment/information layer, units/conversion, time/lag, claim support, direct disclosure versus proxy/inference, validity interval |
| Route | Candidate/market, decision/stage, affected nodes, linked claims, open parameters, revisit trigger/owner and decision history |

Map three connected layers: physical products/workflows; payments, inventories and value capture; public information and investor recognition. Name who owns inventory and who pays whom. A supplier's revenue and its customer's spending are the same transaction, not two independent demand pools. Model private/captive rivals as nodes even without a listed security.

Claim lineage is a directed acyclic dependency graph. Economic relationships may contain feedback loops across time. Label the distinction so cycle checking does not reject legitimate competitive feedback or permit circular factual support.

## Reuse protocol

Before retrieval, A23 searches the library by entity/product/grade/customer/event and one-hop neighbors. Build a run snapshot listing exact source/claim versions and hashes. An existing primary-source capture can be reused after checking authenticity, completeness, definition and date; it need not be downloaded on every issuer call. Query only missing, changed or disputed facts. Duplicate issuer releases and their mirrors share one origin cluster.

For each reuse decide `REUSE_AS_EVIDENCE`, `REVALIDATE`, `LEAD_ONLY`, or `EXCLUDE`:
- All source ancestors must have been public and available by the run cutoff. Record uncertainty conservatively; quarter-end or retrieval date is not a release date. Later restatements never overwrite the earlier vintage.
- Match scope, units and definitions. A capacity claim for one grade is not qualified output for another; a geographic result is not global. Transfer requires an explicit conversion or labeled proxy with its own test.
- Separate durable facts from changing state. Recheck price, capacity qualification, customer commitments, product quality and competitive alternatives at decision-relevant freshness. Historical facts remain historical; forecasts, inferred elasticities and old targets are never automatically fresh.
- Every reused model assumption is reauthorized for the current task with mechanism, scale, alternatives and sensitivity. If its review deadline or condition has passed, use `REVALIDATE`; do not smuggle it into a snapshot as an observed fact.
- Preserve conflicting claims side by side. A newer document is not automatically the correction to an older period. Resolve the dependent conclusion or leave it open.

Independent agents may receive identical raw facts but not each other's estimates or conclusions. Log common evidence origins; distinguish independent reasoning from independent corroboration. Do not give an “independent” market-demand agent a target company revenue to reproduce.

## Changes and revisits

Record `changed_node/claim`, old/new versions, effective date and change classification. Traverse claim/model/route dependencies to produce the affected set; follow time-specific economic edges when their mechanism supports transmission. A shared laser bottleneck, wafer-allocation change or downstream funding cut can reopen several companies at once. Do not invalidate unrelated models or blindly copy the same impact coefficient into each issuer.

O00 marks affected conclusions/gates stale, assigns the next discriminating task and updates the revisit queue. Reuse unaffected accepted inputs. Preserve old targets and exact attribution; never silently rewrite them. A library update cannot retroactively repair an old forecast or import post-cutoff evidence into a historical snapshot.

The optional read-only helper `scripts/research_memory.py` audits normalized reuse records and computes dependency impact from supplied edges. It does not authenticate sources, infer economic links, schedule work, or establish causal/forecast validity. Its synthetic self-tests are implementation checks only. Use `--example` for the small interchange shape; richer ledgers can be adapted to it without changing their meaning.

In that interchange, sources and claims both declare data mode and retirement status; missing source admissibility requires review. Bindings declare `required_scope`, `required_unit` and a canonical `required_definition_id`. A conversion is a separate accepted derived claim with original ancestors and an explicit formula; merely matching a product name cannot convert mass units, time periods or nameplate capacity into qualified output. The helper checks declared compatibility, not whether the conversion's economics are true.

## v2.3 structural propagation

The normalized helper requires every DERIVED claim to declare a nonempty transformation formula and supporting ancestors. This checks presence, not correctness of engineering or arithmetic. Dependency impact includes declared source-to-claim, ancestor-to-derived-claim and claim-to-bound-model-node edges as well as explicit dependencies. It returns conservative review candidates, not automatically changed economic values. Time-specific economic links and materiality remain O00 review tasks; preserve unaffected nodes and old snapshots.
