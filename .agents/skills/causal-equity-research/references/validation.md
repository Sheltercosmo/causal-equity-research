# Forecast validation and honest access limits

Read source specification section 22, sections 23–25, and G18–G24 for the full contract.

## Four lanes

| Lane | Allowed information and claim |
|---|---|
| STRUCTURAL_PRE_GUIDANCE | Only inputs available before company-specific guidance/preannouncement of the target result; disclose excluded management information |
| GUIDANCE_ASSISTED_NOWCAST | Guidance available at origin may constrain the forecast; score incremental value against guidance |
| POST_RELEASE_ATTRIBUTION | Explain known outcomes; make no predictive-accuracy claim |
| PROSPECTIVE_SHADOW | Freeze real forward forecasts before future public outcomes; evaluate when outcomes arrive through a subsequent authorized run |

Use separate records, origins and scores. A later-trained LLM reconstructing old forecasts remains contamination-sensitive even with filtered retrieval. Clean-context workers, masking, hashes and separate filenames cannot erase model memory.

## Protocol before evaluation

A20 registers structural variants, features and recursive source versions, training-only preprocessing, parameter count, economic identification, model/prompt/tool versions and settings, tuning/trial budget, update policy, failed-retrieval handling, baselines, metrics/thresholds, groups and release calendars. Record unsupported or unavailable runtime settings honestly rather than inventing model versions or random seeds.

Prefer five annual periods and 28 usable quarters/full relevant cycle. The 20 train / 4 validation / 4 test example is illustrative. Twelve quarters is descriptive history, and one withheld quarter cannot establish reliable prediction. Short-history issuers receive explicit limits, parsimonious models and prospective evidence where possible. An accuracy-unestablished disclosure permits a descriptive dossier; it does not automatically pass validation for ranking.

Use expanding/rolling origins and 1/2/4-quarter horizons where relevant. Filter by public and provider availability, not quarter-end or retrieval date. Remove unreleased training labels and overlapping target intervals; use embargo only for an actual leakage mechanism. Group issuer families, shared programs and duplicated documents in transfer tests. Preserve both first-public and restated outcomes.

Score volume, comparable price, revenue, margin basis points, expenses, tax, diluted shares, EPS, inventories/receivables and cash. Use predeclared seasonal-naive/run-rate/guidance baselines, training-only scale for MASE, and no MAPE near zero. Price error, event recognition and ranking success are separate from financial accuracy. Detect offsetting driver errors even when EPS matches.

## What this Codex skill can enforce

It can organize fresh GPT contexts; filter and version allowed packets; hash inputs/model/prompts/predictions; keep an append-only receipt history; run deterministic lineage/numeric checks; and refuse unsupported claims. The bundled validator covers a limited set of metadata, dependency and publication guards. It does not provide OS isolation, a secure outcome store, an immutable timestamp service or complete predictive evaluation.

The current runtime may give all agents the same filesystem identity and broad retrieval tools. In that configuration, evaluator-only labels cannot be sealed merely by using another agent or directory. A22 records actual denied-access evidence, tool allowlists, partitioned caches/indexes/summaries and immutable access logs before claiming enforced isolation. Do not alter host security or invent an inaccessible store to satisfy a gate.

If isolation cannot be demonstrated, mark `UNSEALED` and G18/G20 `BLOCKED` for sealed historical claims. Continue allowed causal research/descriptive reconstruction with explicit limits. A prospective forecast can be frozen now, but its scoring remains pending until future outcomes arrive; no synthetic pass or promise substitutes for that evidence. Strict all-gate ranking remains blocked unless the relevant requirements are actually met or the user changes the evaluation mandate.

## Provisional decisions and workflow tests

When the user explicitly authorizes a provisional selection despite unestablished predictive accuracy, preserve that permission in the run mandate. Do not ask again merely because G18/G20 remain unpassed. Report a distinct `PROVISIONAL_UNVALIDATED` opinion, its operating/valuation assumptions, remaining gates and falsifiers. It does not enter the strict eligible ranking (`publish_rank` remains false in the existing validator). Apply v2.2 to distinguish anchored future assumptions (allowed in the chosen provisional forecast even when ranking-sensitive) from unresolved decisive factual contradictions, which still require research or a narrower claim; the permission does not turn missing facts into evidence. No validated-return or sealed-test claim is allowed.

Skill behavior tests belong outside live research, for example `research/skill-revision-<date>/`. Freeze the request, supplied facts, cutoff, rubric and allowed tools before execution. Give fresh agents the skill and raw case inputs without the expected answer or peer conclusions. Assess observable decisions: stage order, customer choice, supply/inventory constraints, early recognition, reuse and revisit behavior. Include a plausible negative case and irrelevant evidence so positivity is not the success criterion. Retain failures and distinguish fresh tests from retests.

A synthetic exercise tests reasoning/implementation on its stated assumptions. A historical demonstration using primary documents published before the cutoff tests whether the mechanism can be reconstructed; user-selected success stories, model memory and shared tool access prevent a pristine backtest claim. Do not answer “we would have picked this winner” from such a demonstration. Actual predictive validation still requires the original protocol, intact prospective forecasts and later outcomes. No autonomous future scoring or monitoring is authorized by creating a receipt.

## Receipt and evaluation lifecycle

Before outcomes are accessible, freeze run ID, origin UTC, target interval and expected release UTC, lane, source/feature hashes, model/code/prompt hashes, protocol hash, settings and predictions. O00 computes packet hashes and stores receipts without overwriting previous versions. Label a local receipt honestly; hashing alone cannot certify a historical freeze time.

A21 receives outcomes only after development closure and permitted release. Score once against the frozen metrics/baselines. Never stream test errors back into tuning. If the model is retuned, start a new experiment and label the old test developmental; use a new untouched test for new validation claims.

After release, explain misses in separate attribution versions: demand, adoption, share, supply/yield, price/mix, recognized costs, expenses/tax, cash, timing, beliefs/valuation and residual. After-origin inputs may explain errors, but original losses and forecasts stay intact.

## Safeguard checks

Before publication, A16/A22 should test rejection of future sources and future ancestors, unsealed historical claims, missing candidate gates, untriaged census items, invalid units, deployment above qualified/funded/intersection limits, nonconserving balances, stale prices, and synthetic evidence entering live models. Use real business tolerances registered in the protocol. Synthetic checks test the implementation only.

Run `python scripts/validate_packet.py --self-test` for the bundled structural mutation tests. Run `python scripts/validate_packet.py path/to/packet.json` for a normalized publication packet following the script's `--example` shape. Successful structural validation does not replace the source, causal, numerical and gate reviews in the framework.

The packet uses `run.data_mode` (`LIVE`/`SYNTHETIC`), distinct from the research work mode. It declares an IANA `reference_timezone`; its local date must match the reference instant. `run.exchange_calendars` contains each exchange's source, sessions and endpoint session. Candidates bind to their own exchange while sharing the calendar horizon. Four stock-flow quantities require four matching unit entries. Calendar completeness remains an evidence-review responsibility.

Every ranked candidate explicitly references the packet's completed evaluation record and is listed in its scope. The record identifies a sealed historical or completed prospective evaluation, protocol/prediction receipts, score evidence, one untouched scoring pass and as-of chronology. Historical evaluation requires demonstrated access enforcement; prospective evaluation requires freezing before the outcome's first public release. Pending or descriptive evaluation cannot be promoted by writing PASS in gate fields. Receipt IDs and declared statuses are checked for presence and consistency, not authenticated by this script; A16/A21/A22 still inspect the underlying evidence. Separate packets may be used for separately validated candidate groups.

## Provisional publication and process development

Use [process-evaluation.md](process-evaluation.md) when changing the method. Do not tune to user-named winners or call a few matching examples general validation.

Normalized candidates declare `publication_mode`: `RESEARCH_ONLY`, `PROVISIONAL_UNVALIDATED`, or `STRICT_RANK`; `publish_rank` is true only for the last. Supplied prices, return formulas, clocks and calendars are checked even for research-only records. Research without a supported target may omit target/upside. Published forecasts require `forecast_kind=HORIZON_PRICE`, security identity, model/recognition references and no unresolved hard factual/model blockers. A zero target with -100% upside is admissible; losses are not validation failures.

Provisional publication additionally records run-level `provisional_authorization_ids`, candidate `accuracy_status=UNESTABLISHED` and all 25 gate dispositions with reviewer/evidence or an explicit rationale. It does not require all gates PASS or a completed predictive evaluation. `blocking_unknowns` means unresolved hard facts or infeasible/unsupported indispensable model links, not every forecastable future parameter. Anchored future assumptions retain the v2.2 ledger. Strict publication keeps its original evaluation/all-pass requirements. The helper validates declarations, not their truth; source and economic review remain necessary.
