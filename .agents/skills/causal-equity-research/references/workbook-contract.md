# Workbook integration contract

The bundled `assets/Causal_Equity_Research_Workbook_v2.xlsx` is the original 50-sheet template. Do not edit that original. When the user requests a workbook deliverable, create a separate run-specific working copy and use the available spreadsheet workflow. A text research request may use equivalent JSON/CSV/text records; preserve the schema meanings and source lineage.

## Sheet routing

Exact field names/coordinates for every sheet are in `workbook-schema.json`.

| Workstream | Sheets | Owner |
|---|---|---|
| Run and task control | 00_Start, 01_Run_Contract, 02_Agents, 03_Checklist, 04_Universe | O00/A03 |
| Provenance and causal clues | 05_Sources, 06_Claims, 07_Clue_Graph, 38_Data_Vintages | A01/A22 |
| Macro and chain | 08_Macro, 09_Chain_Map | A02/A04 |
| Historical accounting | 10_Period_Panel | A12 |
| Demand, supply and price | 11_Demand, 12_Capacity, 13_Grade_Balance, 14_Contracts | A05/A06/A07 |
| Actions and rivals | 15_Rational_Response, 43_Rival_Reactions | A11/A19 |
| Technology and economics | 16_Technology, 17_Customer_TCO | A08/A09 |
| Share and financial model | 18_Share_Cohorts, 19_Model_Drivers, 20_Financial_Model | A10/A12 |
| Expectations, value and events | 21_Market_Beliefs, 22_PE_History, 23_Catalysts, 24_Targets | A13/A14/O00 |
| Review and updates | 25_Red_Team, 26_Monitor_Log, 27_Postmortem | A15/O00/A16 |
| Census and coverage | 31_Document_Map, 32_Number_Census, 44_Research_Coverage | A17/A23 |
| Customer adoption | 33_Customer_Choices, 34_Adoption_Funnel, 35_Demand_Sources | A18/A05 |
| Dynamics | 36_Event_Shocks, 37_Time_Bridges | A19 |
| Validation and handoffs | 39_Validation_Plan, 40_Forecast_Locks, 41_Holdout_Scores, 42_Error_Attribution, 45_Agent_Handoffs | A20/A21/A22/A12 |
| Method and publication controls | 29_Quality_Gates, 30_V2_Upgrade, 46_Method_Sources, 47_V2_Gates | O00/A16 |
| Synthetic examples only | 28_Synthetic_Demo, 48_V2_Synthetic, 49_Dynamics_Demo | A16 |

Workbook rows are registers and calculation examples. Live modules are not an automatically connected causal graph. Bind each accepted input/formula to source/claim/model-node IDs; reconcile the connected model independently. Preserve original and normalized units, scope, timestamps and formulas.

## Publication controls outside spreadsheet status strings

`24_Targets!M6:M25` already checks all 15 old gates (`29_Quality_Gates!E6:E20`), all ten added gates (`47_V2_Gates!B6:B15`), and one matching candidate PASS (`47_V2_Gates!A20:B39`). K suppresses target values while M is blocked; L computes upside and N ranks it. Keep these checks intact in any working copy, but independently establish their evidence.

The formulas check status text, not source quality, reviewer work or mandatory target metadata. Enforce unique candidate IDs, all 25 candidate gate records, reference/target timestamps, issuer/share class, currency and share basis, source-backed reference price, common earnings year or appropriate alternate valuation method, catalyst IDs and model IDs. A duplicate candidate row cannot be accepted merely because one duplicate says PASS. Never mark the entire universe eligible from global completion.

There are stale overlapping data validations in `03_Checklist!I6:I69` and `I6:I119`; canonical task completion uses v2 `NOT_STARTED/IN_PROGRESS/NEEDS_REVIEW/BLOCKED/COMPLETE`. Runtime DAG states in orchestration.md map to this display vocabulary. Old PASS is not accepted task completion without receiver review. `24_Targets!M6:M25` also retains an editable dropdown on formula cells. Verify formula integrity before using a working copy; typed PASS must not override the publication calculation.

For a non-EPS valuation, preserve the appropriate sector method and causal/cash bridge in canonical records; do not force a negative/meaningless P/E into K=EPS×PE. If a workbook is requested, explicitly adapt the working copy within scope and retain the same eligibility rule.

## Numeric, calendar and lineage checks

- Most live formulas guard missing numeric inputs. Retain those guards and real zeros, and carry the specific error/blocking reason when a downstream formula becomes blank. No zero imputation for unavailable inputs.
- Validate units, nonnegative physical quantities, fractions in [0,1], period scaling, serial/shared bottlenecks, cohort intersections, stock conservation, shipment capacity limits and mutually exclusive shares. `18_Share_Cohorts!I6` only divides units; it does not enforce all these constraints.
- `34_Adoption_Funnel!J6` trusts a YES nesting flag. Verify actual cohort membership or treat MIN of unrelated totals as an upper bound. Never infer overlap from the flag alone.
- `01_Run_Contract!B11` is blank; no exchange-calendar computation is implemented. Resolve from the published exchange calendar and record source and month-addition convention. Never use 60 days or weekdays as a substitute.
- `38_Data_Vintages!G6:G20` only checks version-public time E against cutoff F. A22 must separately check provider-available K, lineage H, partition J, label L, exact timezone and all required ancestors.
- `40_Forecast_Locks` records hashes and times but does not verify or secure them. Preserve independently frozen receipts and disclose the actual access model. A mutable spreadsheet cell is not an immutable forecast receipt.
- Historical cells in `22_PE_History` need contemporaneously available earnings and consistent corporate actions; current data cannot fill an old denominator without vintage proof.
- `20_Financial_Model!B5:I5` contains only Q+0 through Q+7. Extend the run model in sidecars or an authorized working copy to the justified long-run horizon. Refer to source-map.md for the 12-versus-28 history and five-versus-ten-year defaults.

## Synthetic separation and validation claims

The three synthetic sheets remain in a demonstration partition. Their values, sample multiples and targets never become live priors. `29_Quality_Gates!E24:E39` and `48_V2_Synthetic!E58:E69` are arithmetic/template checks, separate from research gates. Empty-template tests E38/E39 can cease to pass after valid live population; they are not persistent eligibility criteria.

`48_V2_Synthetic!C17` returns zero for nonpositive benefits in a demonstration payback expression; do not copy that fallback into live economics. `48_V2_Synthetic!B71` reports 47 external Python safeguards and refers to a test log that was not supplied. Do not repeat it as executed validation.

When authoring a requested working workbook, verify changed values/formulas and dependencies, recalculate in a supported engine, test boundaries and render affected views. Cached results and formula counts alone are not recalculation proof. Record unresolved template limitations; never silently modify original reference files.
