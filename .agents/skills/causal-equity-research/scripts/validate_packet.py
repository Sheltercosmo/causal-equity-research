"""Read-only structural guards for normalized v2 publication packets.

No network, file writes, forecasts, Excel recalculation or security enforcement.
--example prints a SYNTHETIC fixture describing the JSON interface.
Passing checks means only that these selected structural invariants hold.
"""
import argparse
import calendar
import copy
from datetime import date, datetime
import json
import math
from pathlib import Path
import sys
import unittest
from zoneinfo import ZoneInfo

GATES = {f"G{i:02d}" for i in range(25)}
TYPES = {"OBSERVED", "COMPANY_CLAIM", "DERIVED", "MODEL_ASSUMPTION",
         "UNRESOLVED", "CONTRADICTED"}
DISPOSITIONS = {"MAPPED", "EXCLUDED_REASONED", "CONFLICT_OPEN", "UNREADABLE", "UNREVIEWED"}


def timestamp(value):
    result = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if result.tzinfo is None or "T" not in value:
        raise ValueError("Exact timezone-aware timestamp required")
    return result


def finite(value):
    return isinstance(value, (float, int)) and not isinstance(value, bool) and math.isfinite(value)


def calendar_endpoint(start, months):
    d = date.fromisoformat(start)
    total = d.year * 12 + d.month - 1 + months
    year, month = divmod(total, 12)
    month += 1
    return date(year, month, min(d.day, calendar.monthrange(year, month)[1]))


def check_business_replay(candidate, facts):
    """Check reported interventions. Reviewer must replay the issuer's actual equations."""
    label = str(candidate.get("id", "?")) + ": "
    replay = candidate.get("business_replay")
    if not isinstance(replay, dict):
        return [label + "Missing business-first valuation replay"]
    errors = []
    def require(ok, message):
        if not ok:
            errors.append(label + message)

    def check_facts(key):
        ids = replay.get(key)
        valid = isinstance(ids, list) and bool(ids) and all(isinstance(i, str) and i in facts for i in ids)
        require(valid, "Missing or unknown replay evidence: " + key)
        return set(ids) if valid else set()

    require(replay.get("basis") in ("business", "contractual"), "Unsupported target basis")
    for field in ("operating_metric", "unit"):
        require(isinstance(replay.get(field), str) and replay[field].strip(), "Missing " + field)
    check_facts("driver_fact_ids")
    check_facts("recognition_fact_ids")
    quote_ids = check_facts("subject_quote_fact_ids")
    terms = check_facts("valuation_parameter_fact_ids")
    visited = set()
    frontier = list(terms)
    while frontier:
        fact_id = frontier.pop()
        if fact_id in visited or fact_id not in facts:
            continue
        visited.add(fact_id)
        frontier.extend(facts[fact_id]["ancestors"])
    require(visited.isdisjoint(quote_ids), "Valuation parameter depends on the cutoff subject quote")
    if replay.get("basis") == "contractual":
        check_facts("contract_fact_ids")
    rows = [replay.get(key) for key in ("base", "quote_only", "driver_low", "driver_high")]
    if not all(isinstance(row, list) and len(row) == 3 and all(finite(v) for v in row)
               and row[0] > 0 and row[2] >= 0 for row in rows):
        return errors + [label + "Each replay needs a positive quote, finite KPI and nonnegative target"]
    (q, k, t), (other_q, same_k, same_t), (lo_q, lo, lo_t), (hi_q, hi, hi_t) = rows
    close = lambda a, b: math.isclose(a, b, rel_tol=1e-9, abs_tol=1e-10)
    require(q == candidate.get("reference_price") and t == candidate.get("target_price"),
            "Base replay differs from published quote or target")
    require(not close(q, other_q) and close(k, same_k), "Quote-only intervention did not isolate the quote")
    require(close(t, same_t), "Horizon target follows the quote with business and beliefs held fixed")
    require(close(q, lo_q) and close(q, hi_q) and lo <= k <= hi and lo < hi,
            "Operating interventions did not bracket the fixed-origin KPI")
    if lo == k or hi == k:
        check_facts("boundary_fact_ids")
        require(bool(str(replay.get("boundary_reason") or "").strip()), "One-sided intervention lacks a feasible boundary")
        require((lo != k or close(lo_t, t)) and (hi != k or close(hi_t, t)),
                "Unchanged boundary state changed target")
    if (lo != k and close(lo_t, t)) or (hi != k and close(hi_t, t)):
        check_facts("invariance_fact_ids")
        reason = replay.get("invariance_reason")
        require(isinstance(reason, str) and reason.strip(), "Unexplained zero operating transmission")
    return errors


def validate(packet, *, archive=False):
    errors = []
    def require(ok, message):
        if not ok:
            errors.append(message)
    run = packet["run"]
    cutoff = timestamp(run["cutoff"])
    reference_time = timestamp(run["reference_time"])
    reference_zone = ZoneInfo(run["reference_timezone"])
    require(date.fromisoformat(run["reference_local_date"]) == reference_time.astimezone(reference_zone).date(),
            "Reference local date does not match timestamp/timezone")
    require(cutoff <= reference_time, "Cutoff exceeds reference-price time")
    require(run["ranking_metric"] == "target/reference-1", "Wrong ranking metric")
    require(run["probability_weighting"] is False, "Probability weighting is disallowed")
    require(run["data_mode"] in {"LIVE", "SYNTHETIC"}, "Unknown data mode")
    months = run["horizon_months"]
    require(isinstance(months, int) and not isinstance(months, bool) and months > 0,
            "Invalid calendar-month horizon")
    endpoint = calendar_endpoint(run["reference_local_date"], months)
    require(date.fromisoformat(run["calendar_endpoint"]) == endpoint, "Calendar-month endpoint mismatch")
    # The caller supplies verified calendars; this cannot verify completeness.
    calendars = run["exchange_calendars"]
    require(bool(calendars), "No exchange calendars supplied")
    for exchange, exchange_calendar in calendars.items():
        require(bool(exchange and exchange_calendar["source"]), "Missing exchange-calendar evidence")
        sessions = [date.fromisoformat(x) for x in exchange_calendar["sessions"]]
        eligible_sessions = [x for x in sessions if x <= endpoint]
        require(bool(eligible_sessions), "No supplied eligible exchange session: " + exchange)
        if eligible_sessions:
            require(date.fromisoformat(exchange_calendar["target_session"]) == max(eligible_sessions),
                    "Target is not last supplied exchange session on/before endpoint: " + exchange)

    facts = packet["facts"]
    ids = [x["id"] for x in facts]
    require(len(ids) == len(set(ids)), "Duplicate fact IDs")
    by_id = {x["id"]: x for x in facts}
    visited, active = set(), set()
    def visit(fid):
        if fid in active:
            errors.append("Cyclic fact lineage: " + fid)
            return
        if fid in visited:
            return
        if fid not in by_id:
            errors.append("Missing fact ancestor: " + fid)
            return
        f = by_id[fid]
        active.add(fid)
        require(f["type"] in TYPES, "Invalid fact classification: " + fid)
        # Authored assumptions/derivations have no invented public-release date.
        # Their admissibility follows their evidence ancestors and recorded basis.
        if f["type"] in {"OBSERVED", "COMPANY_CLAIM"}:
            require(timestamp(f["first_public_at"]) <= cutoff, "Future source: " + fid)
            require(timestamp(f["provider_available_at"]) <= cutoff, "Late provider availability: " + fid)
        else:
            for key in ("first_public_at", "provider_available_at"):
                if f.get(key):
                    require(timestamp(f[key]) <= cutoff, "Future dated input: " + fid)
        require(not f["is_target_label"], "Target label in feature packet: " + fid)
        require(f["partition"] == "FEATURES", "Invalid feature partition: " + fid)
        require(bool(f["unit"]), "Missing unit: " + fid)
        require(f["source_kind"] not in {"ANALYST_TARGET", "ANALYST_REVENUE_EPS_FORECAST"},
                "Disallowed analyst forecast: " + fid)
        require(not (run["data_mode"] == "LIVE" and f["synthetic"]), "Synthetic live evidence: " + fid)
        if f["type"] in {"OBSERVED", "COMPANY_CLAIM"}:
            require(bool(f["source_id"] and f["locator"] and f["origin_id"]),
                    "Missing source provenance: " + fid)
        if f["type"] == "DERIVED":
            require(bool(f["ancestors"] and f["formula"]), "Untraceable derivation: " + fid)
        if f["type"] == "MODEL_ASSUMPTION":
            require(bool(f.get("mechanism") and f["ancestors"]) and f.get("break_even") is not None,
                    "Unsupported modeled assumption: " + fid)
        for parent in f["ancestors"]:
            visit(parent)
        active.remove(fid)
        visited.add(fid)
    for fid in ids:
        visit(fid)

    for item in packet["census"]:
        disposition = item["disposition"]
        require(disposition in DISPOSITIONS, "Unknown census disposition")
        require(disposition != "UNREVIEWED", "Unreviewed scoped disclosure")
        if disposition == "EXCLUDED_REASONED":
            require(bool(item.get("reason")), "Unreasoned disclosure exclusion")
        if item["critical"]:
            require(disposition in {"MAPPED", "EXCLUDED_REASONED"}, "Critical census gap")

    for cohort in packet["cohorts"]:
        counts = [cohort[k] for k in ("economic", "funded", "qualified", "integrator", "complement", "supply", "deployed")]
        require(all(finite(v) and v >= 0 for v in counts), "Invalid cohort quantity")
        if all(finite(v) for v in counts):
            require(counts[-1] <= min(counts[:-1]), "Deployment exceeds a physical/economic cap")
        require(cohort["intersection_verified"] is True, "Cohort intersection not verified")
    for balance in packet["balances"]:
        values = [balance[k] for k in ("opening", "inflows", "outflows", "closing")]
        require(all(finite(v) and v >= 0 for v in values), "Invalid stock-flow quantity")
        units = balance["units"]
        require(isinstance(units, list) and len(units) == 4
                and all(isinstance(unit, str) and bool(unit.strip()) for unit in units)
                and len(set(units)) == 1, "Mismatched balance units/cardinality")
        require(finite(balance["tolerance"]) and balance["tolerance"] >= 0, "Invalid balance tolerance")
        if all(finite(v) for v in values):
            require(abs(values[0] + values[1] - values[2] - values[3]) <= balance["tolerance"],
                    "Stock-flow conservation failure")

    evaluation = packet["evaluation"]
    single_score = isinstance(evaluation["score_count"], int) and not isinstance(evaluation["score_count"], bool) \
        and evaluation["score_count"] == 1
    require(evaluation["status"] in {"PENDING", "COMPLETE", "DESCRIPTIVE"}, "Unknown evaluation status")
    require(evaluation["method"] in {"SEALED_HISTORICAL", "PROSPECTIVE_SHADOW", "DESCRIPTIVE"},
            "Unknown evaluation method")
    if evaluation["claims_sealed"]:
        require(evaluation["access_enforced"] is True and bool(evaluation["access_evidence"]),
                "Sealed claim lacks verified access enforcement")
        require(timestamp(evaluation["frozen_at"]) < timestamp(evaluation["label_access_at"]),
                "Forecast not locked before label access")
        require(single_score, "Sealed test not scored exactly once")
        require(evaluation["retuned_after_test"] is False, "Retuned test is development data")
    require(not (evaluation["retrospective_llm"] and evaluation["claims_pristine"]),
            "Pristine retrospective LLM claim unsupported")

    candidates = packet["candidates"]
    candidate_ids = [c["id"] for c in candidates]
    require(len(candidate_ids) == len(set(candidate_ids)), "Duplicate candidate IDs")
    for c in candidates:
        # Integrity checks depend on the data/claim supplied, not ranking status.
        require(type(c.get("publish_rank")) is bool, "publish_rank must be boolean")
        mode = c.get("publication_mode", "STRICT_RANK" if c.get("publish_rank") else "RESEARCH_ONLY")
        require(mode in {"RESEARCH_ONLY", "PROVISIONAL_UNVALIDATED", "STRICT_RANK"}, "Unknown publication mode")
        require((mode == "STRICT_RANK") == (c.get("publish_rank") is True), "Publication mode/ranking mismatch")
        published = mode in {"PROVISIONAL_UNVALIDATED", "STRICT_RANK"}
        supplied_price = any(c.get(k) is not None for k in ("reference_price", "target_price", "upside"))
        if supplied_price:
            require(finite(c.get("reference_price")) and c["reference_price"] > 0, "Invalid reference price")
            if c.get("target_price") is not None:
                require(finite(c["target_price"]) and c["target_price"] >= 0, "Invalid target price")
                if finite(c.get("reference_price")) and c["reference_price"] > 0 and finite(c["target_price"]):
                    require(finite(c.get("upside")) and abs(c["upside"]-(c["target_price"]/c["reference_price"]-1)) < 1e-10,
                            "Upside formula mismatch")
            else:
                require(c.get("upside") is None, "Upside supplied without a target")
        if c.get("exchange") is not None or published:
            require(c.get("exchange") in calendars, "Missing candidate exchange calendar")
        if c.get("target_session") is not None or published:
            require(c.get("exchange") in calendars and c.get("target_session") == calendars.get(c.get("exchange"), {}).get("target_session"),
                    "Candidate horizon mismatch")
        if c.get("reference_time") is not None or published:
            require(timestamp(c["reference_time"]) == reference_time, "Candidate price-clock mismatch")
        if published:
            if not archive or "business_replay" in c or run.get("business_contract") is not None:
                errors.extend(check_business_replay(c, by_id))
            require(run["data_mode"] == "LIVE", "Synthetic run cannot publish a live forecast")
            require(all(c.get(k) for k in ("issuer", "share_class", "currency", "share_basis")), "Missing security identity")
            require(bool(c.get("recognition_ids") and c.get("model_ids") and c.get("valuation_method")), "Missing recognition/model route")
            require(finite(c.get("target_price")) and c["target_price"] >= 0, "Missing/invalid horizon target")
            require(c.get("forecast_kind") == "HORIZON_PRICE", "Published forecast must distinguish horizon price from intrinsic value")
            require(not c.get("blocking_unknowns", ["undeclared"]), "Candidate has decisive unresolved factual/model blockers")
        if mode == "PROVISIONAL_UNVALIDATED":
            require(bool(run.get("provisional_authorization_ids")), "Provisional permission not recorded")
            require(c.get("accuracy_status") == "UNESTABLISHED", "Provisional accuracy label missing")
            gates = c.get("gates", [])
            require(len(gates) == 25 and {g["id"] for g in gates} == GATES, "Incomplete/duplicate candidate gates")
            for g in gates:
                require(g.get("status") in {"NOT_STARTED", "NEEDS_REVIEW", "BLOCKED", "FAIL", "PASS"}, "Unknown gate status")
                require(bool(g.get("reviewer") and (g.get("evidence_ids") or g.get("rationale"))), "Unadjudicated provisional gate")
                if g.get("status") == "PASS":
                    require(bool(g.get("evidence_ids")), "PASS gate lacks evidence references")
        if not c["publish_rank"]:
            continue
        require(run["data_mode"] == "LIVE", "Synthetic run cannot publish a live ranking")
        require(c["exchange"] in calendars, "Missing candidate exchange calendar")
        if c["exchange"] in calendars:
            require(c["target_session"] == calendars[c["exchange"]]["target_session"], "Candidate horizon mismatch")
        require(timestamp(c["reference_time"]) == reference_time, "Candidate price-clock mismatch")
        require(bool(c["issuer"] and c["share_class"] and c["currency"] and c["share_basis"]), "Missing security identity")
        require(bool(c["recognition_ids"] and c["model_ids"] and c["valuation_method"]), "Missing recognition/model route")
        require(not c["blocking_unknowns"], "Candidate has decisive unresolved questions")
        require(c["evaluation_id"] == evaluation["id"] and c["id"] in evaluation["candidate_ids"],
                "Candidate not covered by evaluation record")
        require(evaluation["status"] == "COMPLETE", "Publication requires completed evaluation")
        require(evaluation["method"] != "DESCRIPTIVE", "Descriptive work cannot establish validated ranking")
        require(bool(evaluation["protocol_receipt_ids"] and evaluation["prediction_receipt_ids"]
                     and evaluation["score_evidence_ids"]), "Missing evaluation receipts/results")
        require(single_score and evaluation["retuned_after_test"] is False,
                "Publication requires one untouched evaluation")
        require(timestamp(evaluation["frozen_at"]) < timestamp(evaluation["label_access_at"])
                <= timestamp(evaluation["scored_at"]) <= cutoff,
                "Evaluation chronology does not support as-of publication")
        require(timestamp(evaluation["label_first_public_at"]) <= timestamp(evaluation["label_access_at"]),
                "Evaluation uses an outcome before first public release")
        if evaluation["method"] == "SEALED_HISTORICAL":
            require(evaluation["claims_sealed"] is True and evaluation["access_enforced"] is True
                    and bool(evaluation["access_evidence"]), "Historical evaluation is not access-enforced")
        if evaluation["method"] == "PROSPECTIVE_SHADOW":
            require(timestamp(evaluation["frozen_at"]) < timestamp(evaluation["label_first_public_at"])
                    <= timestamp(evaluation["label_access_at"]), "Prospective forecast was not frozen before outcome")
        gates = c["gates"]
        require(len(gates) == 25 and {g["id"] for g in gates} == GATES, "Incomplete/duplicate candidate gates")
        for g in gates:
            require(g["status"] == "PASS" and bool(g["reviewer"] and g["evidence_ids"]),
                    "Unsupported gate: " + g["id"])
    return errors


def example():
    return {
        "run": {"id": "SYNTHETIC-INTERFACE-ONLY", "data_mode": "SYNTHETIC", "cutoff": "2030-01-31T16:00:00Z",
                "reference_time": "2030-01-31T16:00:00Z", "reference_timezone": "UTC",
                "reference_local_date": "2030-01-31", "horizon_months": 2, "calendar_endpoint": "2030-03-31",
                "exchange_calendars": {"DEMO_EXCHANGE": {
                    "source": "SYNTHETIC fixture, not a real exchange calendar",
                    "sessions": ["2030-03-28", "2030-03-29"], "target_session": "2030-03-29"}},
                "ranking_metric": "target/reference-1", "probability_weighting": False},
        "facts": [{"id": "F1", "type": "OBSERVED", "first_public_at": "2030-01-30T12:00:00Z",
                   "provider_available_at": "2030-01-30T12:00:00Z", "is_target_label": False,
                   "partition": "FEATURES", "synthetic": True, "unit": "units", "source_id": "S1",
                   "source_kind": "SYNTHETIC", "locator": "fixture", "origin_id": "O1", "ancestors": [], "formula": ""}],
        "census": [{"critical": True, "disposition": "MAPPED"}],
        "cohorts": [{"economic": 400, "funded": 200, "qualified": 150, "integrator": 120,
                     "complement": 130, "supply": 140, "deployed": 120, "intersection_verified": True}],
        "balances": [{"opening": 10, "inflows": 5, "outflows": 4, "closing": 11,
                      "units": ["units"] * 4, "tolerance": 1e-9}],
        "evaluation": {"id": "EV1", "status": "PENDING", "method": "PROSPECTIVE_SHADOW",
                       "candidate_ids": ["DEMO"], "protocol_receipt_ids": [], "prediction_receipt_ids": [],
                       "score_evidence_ids": [], "claims_sealed": False, "access_enforced": False, "access_evidence": [],
                       "frozen_at": "2030-01-31T16:00:00Z", "label_access_at": "2030-04-01T12:00:00Z",
                       "label_first_public_at": "2030-04-01T12:00:00Z", "scored_at": "2030-04-01T13:00:00Z",
                       "score_count": 0, "retuned_after_test": False, "retrospective_llm": True,
                       "claims_pristine": False},
        "candidates": [{"id": "DEMO", "issuer": "Synthetic example", "share_class": "common",
                        "exchange": "DEMO_EXCHANGE", "evaluation_id": "EV1",
                        "currency": "USD", "share_basis": "consistent diluted", "publish_rank": False,
                        "reference_time": "2030-01-31T16:00:00Z", "target_session": "2030-03-29",
                        "reference_price": 100, "target_price": 120, "upside": 0.2,
                        "valuation_method": "SYNTHETIC", "recognition_ids": [], "model_ids": [],
                        "blocking_unknowns": ["Demonstration only"],
                        "gates": [{"id": g, "status": "NOT_STARTED", "reviewer": "", "evidence_ids": []} for g in sorted(GATES)]}]
    }


def publication_test_fixture():
    """Fabricated metadata for unit tests only; not evidence or a real forecast."""
    p = example()
    p["run"]["data_mode"] = "LIVE"
    p["facts"][0].update(synthetic=False, source_kind="PRIMARY")
    quote = copy.deepcopy(p["facts"][0])
    quote.update(id="TEST_QUOTE", source_id="EXCHANGE", unit="USD/share", source_kind="REFERENCE_QUOTE")
    p["facts"].append(quote)
    p["candidates"][0]["business_replay"] = {
        "basis": "business", "operating_metric": "Test accepted units", "unit": "units",
        "driver_fact_ids": ["F1"], "recognition_fact_ids": ["F1"],
        "subject_quote_fact_ids": ["TEST_QUOTE"], "valuation_parameter_fact_ids": ["F1"],
        "base": [100, 5, 120], "quote_only": [90, 5, 120],
        "driver_low": [100, 4, 96], "driver_high": [100, 6, 144]}
    p["evaluation"].update(status="COMPLETE", protocol_receipt_ids=["TEST_PROTOCOL"],
                           prediction_receipt_ids=["TEST_PREDICTION"], score_evidence_ids=["TEST_SCORE"],
                           frozen_at="2029-10-01T16:00:00Z", label_first_public_at="2030-01-30T12:00:00Z",
                           label_access_at="2030-01-30T12:01:00Z", scored_at="2030-01-30T13:00:00Z",
                           score_count=1, retrospective_llm=False)
    p["candidates"][0].update(publish_rank=True, forecast_kind="HORIZON_PRICE", recognition_ids=["TEST_EVENT"], model_ids=["TEST_MODEL"],
                               blocking_unknowns=[], gates=[{"id": g, "status": "PASS", "reviewer": "TEST_ONLY",
                                                            "evidence_ids": ["TEST_ONLY"]} for g in sorted(GATES)])
    return p


class GuardsTest(unittest.TestCase):
    def test_fixture_and_calendar(self):
        self.assertEqual(validate(example()), [])
        self.assertEqual(str(calendar_endpoint("2032-01-31", 1)), "2032-02-29")

    def test_mutations(self):
        mutations = [
            lambda p: p["facts"][0].update(first_public_at="2030-02-01T00:00:00Z"),
            lambda p: p["facts"][0].update(provider_available_at="2030-02-01T00:00:00Z"),
            lambda p: p["facts"][0].update(ancestors=["MISSING"]),
            lambda p: p["facts"][0].update(ancestors=["F1"]),
            lambda p: p["facts"][0].update(is_target_label=True),
            lambda p: p["facts"][0].update(source_kind="ANALYST_TARGET"),
            lambda p: p["run"].update(data_mode="LIVE"),
            lambda p: p["run"].update(probability_weighting=True),
            lambda p: p["run"].update(calendar_endpoint="2030-04-01"),
            lambda p: p["run"]["exchange_calendars"]["DEMO_EXCHANGE"].update(target_session="2030-03-28"),
            lambda p: p["run"].update(reference_local_date="2031-01-31", calendar_endpoint="2031-03-31"),
            lambda p: p["run"].update(reference_time="2030-01-31T15:00:00Z"),
            lambda p: p["census"][0].update(disposition="UNREVIEWED"),
            lambda p: p["census"][0].update(disposition="UNREADABLE"),
            lambda p: p["cohorts"][0].update(deployed=121),
            lambda p: p["cohorts"][0].update(intersection_verified=False),
            lambda p: p["balances"][0].update(closing=-1),
            lambda p: p["balances"][0].update(units=["units", "tonnes", "units", "units"]),
            lambda p: p["balances"][0].update(units=["units"]),
            lambda p: p["balances"][0].update(units="uuuu"),
            lambda p: p["evaluation"].update(claims_sealed=True),
            lambda p: p["evaluation"].update(claims_pristine=True),
            lambda p: p["candidates"][0].update(publish_rank=True),
            lambda p: p["candidates"].append(copy.deepcopy(p["candidates"][0])),
        ]
        for index, change in enumerate(mutations):
            with self.subTest(mutation=index):
                packet = example()
                change(packet)
                self.assertTrue(validate(packet))

    def test_publication_requires_completed_linked_evaluation(self):
        self.assertEqual(validate(publication_test_fixture()), [])
        mutations = [
            lambda p: p["evaluation"].update(status="PENDING"),
            lambda p: p["evaluation"].update(method="DESCRIPTIVE"),
            lambda p: p["evaluation"].update(method="SEALED_HISTORICAL"),
            lambda p: p["evaluation"].update(score_count=0),
            lambda p: p["evaluation"].update(score_count=True),
            lambda p: p["evaluation"].update(retuned_after_test=True),
            lambda p: p["evaluation"].update(protocol_receipt_ids=[]),
            lambda p: p["evaluation"].update(prediction_receipt_ids=[]),
            lambda p: p["evaluation"].update(score_evidence_ids=[]),
            lambda p: p["evaluation"].update(candidate_ids=[]),
            lambda p: p["evaluation"].update(label_first_public_at="2029-09-30T12:00:00Z"),
            lambda p: p["evaluation"].update(scored_at="2030-02-01T00:00:00Z"),
            lambda p: p["candidates"][0].update(evaluation_id="OTHER"),
            lambda p: p["candidates"][0].update(exchange="OTHER"),
        ]
        for index, change in enumerate(mutations):
            with self.subTest(mutation=index):
                p = publication_test_fixture()
                change(p)
                self.assertTrue(validate(p))

    def test_historical_evaluation_requires_released_outcome(self):
        p = publication_test_fixture()
        p["evaluation"].update(method="SEALED_HISTORICAL", claims_sealed=True,
                               access_enforced=True, access_evidence=["TEST_ONLY"])
        self.assertEqual(validate(p), [])
        p["evaluation"]["label_first_public_at"] = "2031-01-01T00:00:00Z"
        self.assertTrue(any("before first public release" in error for error in validate(p)))

    def test_exchange_specific_sessions(self):
        p = publication_test_fixture()
        p["run"]["exchange_calendars"]["SECOND_EXCHANGE"] = {
            "source": "SYNTHETIC holiday fixture", "sessions": ["2030-03-27", "2030-03-28"],
            "target_session": "2030-03-28"}
        second = copy.deepcopy(p["candidates"][0])
        second.update(id="SECOND", exchange="SECOND_EXCHANGE", target_session="2030-03-28")
        p["candidates"].append(second)
        p["evaluation"]["candidate_ids"].append("SECOND")
        self.assertEqual(validate(p), [])

    def test_reference_date_uses_declared_timezone(self):
        p = example()
        p["run"].update(cutoff="2030-01-31T00:30:00Z", reference_time="2030-01-31T00:30:00Z",
                         reference_timezone="America/New_York", reference_local_date="2030-01-30",
                         calendar_endpoint="2030-03-30")
        p["candidates"][0]["reference_time"] = p["run"]["reference_time"]
        self.assertEqual(validate(p), [])

    def test_recursive_future_ancestor(self):
        p = example()
        future = copy.deepcopy(p["facts"][0])
        future.update(id="F2", first_public_at="2030-02-01T00:00:00Z")
        p["facts"].append(future)
        p["facts"][0].update(type="DERIVED", ancestors=["F2"], formula="F2*2")
        self.assertTrue(any("Future source: F2" in x for x in validate(p)))

    def test_assumption_uses_ancestors_without_invented_release(self):
        p = example()
        assumption = copy.deepcopy(p["facts"][0])
        assumption.update(id="A1", type="MODEL_ASSUMPTION", ancestors=["F1"],
                          mechanism="Synthetic supported cost threshold", break_even=0)
        del assumption["first_public_at"]
        del assumption["provider_available_at"]
        p["facts"].append(assumption)
        self.assertEqual(validate(p), [])


    def test_unranked_supplied_values_do_not_bypass_integrity(self):
        for change in [dict(upside=.8), dict(target_session="2040-01-01"),
                       dict(reference_time="2030-01-31T15:00:00Z"), dict(exchange="UNKNOWN"),
                       dict(target_price=float("nan")), dict(reference_price=0),
                       dict(target_price=-1), dict(publish_rank=0)]:
            p=example();p["candidates"][0].update(change)
            self.assertTrue(validate(p),change)

    def test_research_without_target_is_not_forced_to_forecast(self):
        p=example();c=p["candidates"][0]
        for key in ("reference_price","target_price","upside","reference_time","target_session","exchange"):
            del c[key]
        self.assertEqual(validate(p),[])

    def test_provisional_forecast_keeps_integrity_without_false_validation(self):
        p=publication_test_fixture();c=p["candidates"][0]
        c.update(publish_rank=False,publication_mode="PROVISIONAL_UNVALIDATED",accuracy_status="UNESTABLISHED")
        p["run"]["provisional_authorization_ids"]=["SYNTHETIC_USER_PERMISSION"]
        p["evaluation"].update(status="PENDING",score_count=0)
        c["gates"][18].update(status="BLOCKED",rationale="No enforced isolation")
        self.assertEqual(validate(p),[])
        for change in [dict(issuer=""),dict(forecast_kind="INTRINSIC_VALUE"),dict(accuracy_status="VALIDATED"),
                       dict(blocking_unknowns=["unresolved identity"]),dict(gates=[])]:
            q=copy.deepcopy(p);q["candidates"][0].update(change)
            self.assertTrue(validate(q),change)
        q=copy.deepcopy(p);q["run"]["provisional_authorization_ids"]=[]
        self.assertTrue(validate(q))
        q=copy.deepcopy(p);q["run"]["data_mode"]="SYNTHETIC"
        self.assertTrue(validate(q))

    def test_loss_forecast_and_zero_target_are_valid(self):
        p=publication_test_fixture()
        for target in (90,0):
            p["candidates"][0].update(target_price=target,upside=target/100-1)
            replay=p["candidates"][0]["business_replay"]
            for key in ("base", "quote_only"):
                replay[key][2]=target
            replay["driver_low"][2]=max(0,target-10)
            replay["driver_high"][2]=target+10
            replay.update(invariance_fact_ids=["F1"], invariance_reason="Synthetic equity floor")
            self.assertEqual(validate(p),[])

    def test_quote_only_and_archive_boundaries(self):
        p = publication_test_fixture()
        c = p["candidates"][0]
        c["business_replay"]["quote_only"][2] = 108
        self.assertTrue(any("follows the quote" in error for error in validate(p)))
        del c["business_replay"]
        self.assertTrue(validate(p))
        self.assertEqual(validate(p, archive=True), [])
        p["run"]["business_contract"]="2.8"
        self.assertTrue(validate(p, archive=True))

    def test_operating_interventions_and_contract_evidence(self):
        p = publication_test_fixture()
        replay = p["candidates"][0]["business_replay"]
        replay.update(basis="contractual", contract_fact_ids=["F1"])
        for key in ("driver_low", "driver_high"):
            replay[key][2] = replay["base"][2]
        self.assertTrue(validate(p))
        replay.update(invariance_fact_ids=["F1"], invariance_reason="Synthetic fixed consideration under closing assumption")
        self.assertEqual(validate(p), [])
        replay["driver_high"][1] = replay["base"][1]
        self.assertTrue(validate(p))
        replay["driver_high"][1] = 6
        replay["contract_fact_ids"] = ["missing"]
        self.assertTrue(validate(p))

    def test_hidden_quote_calibration_and_binding_capacity(self):
        p = publication_test_fixture()
        c = p["candidates"][0]
        replay = c["business_replay"]
        term = dict(p["facts"][0], id="EXIT_PE", type="DERIVED", unit="times",
                    formula="subject cutoff quote / private EPS", ancestors=["TEST_QUOTE", "F1"])
        p["facts"].append(term)
        replay["valuation_parameter_fact_ids"] = ["EXIT_PE"]
        self.assertTrue(any("depends on the cutoff" in err for err in validate(p)))
        term.update(formula="matched peer value / its normalized earnings", ancestors=["F1"])
        self.assertEqual(validate(p), [])
        replay["driver_high"] = list(replay["base"])
        replay.update(invariance_fact_ids=["F1"], invariance_reason="Line is at capacity")
        self.assertTrue(validate(p))
        replay.update(boundary_fact_ids=["F1"], boundary_reason="All available slots already used")
        self.assertEqual(validate(p), [])

    def test_declared_modes_cannot_waive_strict_checks(self):
        p=publication_test_fixture();p["candidates"][0]["publication_mode"]="RESEARCH_ONLY"
        self.assertTrue(validate(p))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("packet", nargs="?")
    parser.add_argument("--example", action="store_true")
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--archive-v27", action="store_true",
                        help="Replay the historical schema for preserved, unversioned v2.7-or-earlier packets only")
    args = parser.parse_args()
    if args.self_test:
        result = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(GuardsTest))
        return 0 if result.wasSuccessful() else 1
    if args.example:
        print(json.dumps(example(), indent=2))
        return 0
    if not args.packet:
        parser.error("Provide a packet path, --example, or --self-test")
    try:
        errors = validate(json.loads(Path(args.packet).read_text(encoding="utf-8-sig")), archive=args.archive_v27)
    except (KeyError, TypeError, ValueError, IndexError) as exc:
        errors = ["Malformed required data: " + str(exc)]
    print(json.dumps({"structural_checks": "FAIL" if errors else "PASS", "errors": errors,
                      "scope": "Selected structural checks only; not factual, economic, security or predictive validation"}, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
