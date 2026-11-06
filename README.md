# Causal Equity Research

A business-first equity research skill for Codex, using GPT specialists to connect customer value, market dynamics and future earnings to investor expectations.

**Core concept.** Start with the customer's benefit against purchase, implementation, operating and switching costs. Explain competitiveness and moat through technical evidence and customer choices. Model funded demand, qualified supply, inventory, pricing, market share and management execution before valuing future earnings and cash.

**Method.** Search broadly, split markets into specific applications and map upstream, downstream and substitute relationships. The main GPT orchestrates 23 specialist responsibilities in small batches, normally two workers and at most three. Independent demand, supply, technology, financial and valuation passes cross-check the thesis. Reuse dated evidence, preserve promising routes with revisit triggers, and identify the information that can change investor expectations by the forecast horizon.

**Application.** Use for stock discovery, company diligence, earnings and industry forecasts, thesis updates and research audits. Default ranking is two-calendar-month price appreciation, with one operating path and point target per eligible company. Risks and sensitivities are reported separately; the user can change the universe and horizon.

**Scope.** Works across listed equities and their private or public value chains. Runs inside Codex with GPT subagents and research tools; no OpenAI API application or key is needed. Outputs are text and inspectable evidence/models. Provisional forecasts require explicit authorization; structural checks do not establish investment performance. Trading and background monitoring require separate instructions.

## Use

Open this repository as a Codex project. It includes the skill, project instructions, all 23 specialist roles, the original v2 specification and workbook template, and the current v2.8 execution contract.

For an existing workspace, copy `.agents/skills/causal-equity-research/` and `.codex/agents/`, then merge `AGENTS.md` and `.codex/config.toml` with existing instructions. Keep the project-relative layout. Roles inherit the active GPT model and reasoning setting.

Example prompt:

> Use $causal-equity-research to start a fresh Nasdaq selection. Compare broad opportunities before deepening, forecast the next quarter and year, and rank two-month price upside. Allow provisional selections with unestablished predictive accuracy clearly disclosed.

Start with [SKILL.md](.agents/skills/causal-equity-research/SKILL.md). Optional validators require Python 3.9+ and IANA timezone data (`tzdata` on systems without it):

```sh
python .agents/skills/causal-equity-research/scripts/validate_packet.py --self-test
python .agents/skills/causal-equity-research/scripts/validate_workflow.py --self-test
python .agents/skills/causal-equity-research/scripts/research_memory.py --self-test
```
