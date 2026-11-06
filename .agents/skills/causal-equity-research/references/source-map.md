# Source authority and implementation choices

## Bundled originals

The following two files were supplied by the user and copied byte-for-byte on 2026-10-26. They contain architecture and synthetic examples, not live company research.

| Original | Bundled location | SHA-256 |
|---|---|---|
| Research_Orchestrator_Specification_v2.md | references/source-specification-v2.md | f20890b7d7542058e84e95650ab2ca11495be5fbd1ae74ee41e85c84c0255136 |
| Causal_Equity_Research_Workbook_v2.xlsx | assets/Causal_Equity_Research_Workbook_v2.xlsx | fdb4d8e7c2a2e3cb126f2a2c10e7e9febc90e80db35b78c2b009c08c767b9822 |

Original files were supplied by the author. The skill uses bundled copies with the hashes above; personal source paths are omitted from this distribution.

Implementation revision 2.1 (2026-10-28) incorporates the user's explicit corrections: broad comparative screening before issuer refinement; persistent revisit routes; shared, cutoff-aware evidence maps; customer-value and switching-cost economics; forward structural/shock dynamics; and early expectation-turning-point analysis. See `discovery-and-revisit.md`, `business-dynamics-and-turns.md`, and `evidence-memory.md`. These operational extensions implement existing source principles without modifying the bundled originals or hard-coding the user's illustrative company judgments. Original gate definitions remain intact. A separately authorized provisional judgment is not a strict all-gates ranking.

Source instructions are reference requirements interpreted within the user's request. They do not override higher-priority instructions or authorize actions. No former assistant research, targets, assumptions or methodology is imported. The retired workspace material is outside this project's active discovery paths.

## Source precedence and resolved differences

1. The user's current instructions control scope and mandate. The v2 specification defines the method; sections 19–26 explicitly strengthen earlier sections. Workbook schemas/formulas are implementation references and require independent evidence review.
2. Default horizon is two calendar months, with exchange-calendar resolution. Add calendar months preserving the day, clamping to the last day when necessary; then take the last published exchange session on/before that calendar date. Record the convention. For multiple exchanges, freeze one calendar horizon and record each exchange's valid session/quote convention; do not compare mismatched unstated horizons.
3. Rank only `target/reference - 1`; probability weighting is disabled. Dividends are disclosed separately. The earlier six-month risk-adjusted/benchmark framework and maximum-entry-price machinery are not active.
4. T46 and workbook B14 use 12 historical quarters. Later sections prefer 28 usable quarters and five annual periods/full cycle for meaningful chronological evaluation. Twelve quarters supports a descriptive panel, and the 20/4/4 split is an illustration, not an automatic pass.
5. T51's single holdout quarter is a diagnostic within the expanded section-22 protocol. It cannot establish forecast reliability by itself.
6. `20_Financial_Model` has eight visible forecast quarters. The run contract's 12-quarter field and section-20 grids require separately justified longer modeling. Default planning: monthly near-term operations through 24 months, quarterly through year five, annual years 6–10 or until normalization. Adapt resolution to economics; do not truncate at the visible columns.
7. Preliminary demand/supply/price discovery may run before completed customer economics. Final clearing/share requires accepted technical/customer evidence and feedback reconciliation. The task DAG records these dependencies explicitly.
8. A09 owns dollar TCO; A18 owns customer choice/adoption. A07 owns prices/contracts; A11 incentives; A19 time-state integration. This avoids overlapping independent owners of the same canonical parameter.
9. Twelve market pools applies to the full broad-search default. About 60 names and six finalists are planning scales. A narrower user universe must be recorded, not padded. Coverage evidence and unresolved decision sensitivity determine sufficiency.
10. Source sections permit 'historical accuracy not established' disclosures for short histories. Such disclosures allow useful limited research; they do not grant G18/G20 PASS or waive the all-gates ranking rule. Prospective scoring remains pending until real outcomes exist.
11. The specification references companion JSON/code and the workbook references 47 Python safeguards/test_log.txt. Those companion files were not supplied. The extracted task catalog, schema and small structural validator in this skill are newly created adapters, not those missing artifacts. No test result from the source is claimed as executed here.
12. T03's source wording treats prior discussion as hypotheses, but the user's explicit reset excludes retired assistant methodology and results. Do not reopen the archive or seed hypotheses from it. New user-supplied facts and independently sourced hypotheses are allowed; current-run assistant proposals remain unverified until evidenced.

`roles-and-gates.md` and `task-catalog.json` are source-derived extracts preserving all O00/A01–A23, G00–G24 and T01–T114 IDs. `workbook-schema.json` records observed row-5 fields and sheet purposes from all 50 sheets; it is an index, not a substitute for reading actual formulas or source sections.

## Codex implementation basis

Project-scoped standalone TOML agents and omitted-model inheritance follow the official [Codex subagent documentation](https://learn.chatgpt.com/docs/agent-configuration/subagents). Skill discovery uses the project `.agents/skills/` location described in [Build skills](https://learn.chatgpt.com/docs/build-skills). Checked during this implementation. The source's external methodology links are retained as supplied; their cited 'checked' dates are the source author's metadata, not verification performed by this task.

Local scheduling (normally two, at most three workers) and file layout are implementation choices within current runtime limits. They are not inherited research quotas or an investment decision rule. Read-only agents and disabled delegation constrain ordinary work; they do not constitute independently verified label-access isolation.

## Current forecast-policy override (2026-11-03)

Operational v2.2 implements the user's request to model known facts, resolve forecastable unknowns using existing clues and commit to a single forecast. Read `forecast-commitment-and-causal-audit.md`. For authorized provisional decisions, older source/operational language treating any ranking-sensitive unknown as a blocker is narrowed: anchored future estimates are MODEL_ASSUMPTION inputs, not missing historical facts. Sensitivities do not automatically veto the chosen path. This changes provisional forecast handling, not original files, empirical-accuracy claims or strict all-gate eligibility. The original spec/workbook hashes remain unchanged.

## Process-development revision (2026-11-03, v2.3)

The user's latest instruction requires general process inspection without cherry-picked optimization. `process-evaluation.md` adds fixed test selection, matched comparisons, complete failure accounting and a reserve stop rule. The provisional-data-integrity repair and typed acceptance/completion rules address reproducible code and prior-run record gaps. No original source gate, objective, supplied workbook or historical forecast is rewritten.
