"""Read-only evidence-reuse audit and dependency-impact helper.

Input timestamps/provenance are declarations, not authenticated facts. A reusable
candidate still requires human/GPT source and economic review. No network/writes.
"""
import argparse
import copy
from datetime import datetime
import json
from pathlib import Path
import sys
import unittest


def instant(value):
    result = datetime.fromisoformat(value.replace('Z', '+00:00'))
    if result.tzinfo is None:
        raise ValueError('Timezone-aware timestamps required')
    return result


def indexed(items, kind):
    result = {item['id']: item for item in items}
    if len(result) != len(items):
        raise ValueError('Duplicate ' + kind + ' IDs; use explicit version IDs')
    return result


def review(packet):
    """Return structural reuse decisions, including recursive source lineage."""
    cutoff = instant(packet['cutoff'])
    sources = indexed(packet['sources'], 'source')
    claims = indexed(packet['claims'], 'claim')
    allowed = {'OBSERVED', 'COMPANY_CLAIM', 'DERIVED', 'MODEL_ASSUMPTION'}
    memo = {}

    def inspect(cid, active):
        if cid in active:
            return {'decision': 'EXCLUDE', 'reasons': ['Circular claim lineage: ' + cid], 'origins': []}
        if cid in memo:
            return memo[cid]
        if cid not in claims:
            return {'decision': 'EXCLUDE', 'reasons': ['Missing ancestor: ' + cid], 'origins': []}
        claim = claims[cid]
        reasons, origins = [], set()
        level = 0  # 0 reusable candidate; 1 revalidate; 2 lead only; 3 exclude
        def issue(severity, reason):
            nonlocal level
            level = max(level, severity)
            reasons.append(reason)
        if claim.get('data_mode') != packet['data_mode']:
            issue(3, 'Data-mode mismatch')
        if claim.get('retired', False):
            issue(3, 'Retired material')
        if claim.get('status') != 'ACCEPTED':
            issue(2, 'Not accepted evidence')
        if claim.get('type') not in allowed:
            issue(2, 'Unresolved or contradicted claim')
        if not claim.get('scope') or not claim.get('unit') or not claim.get('definition_id') or not claim.get('locator'):
            issue(2, 'Incomplete scope/unit/definition/locator')
        if claim.get('conflict_ids'):
            issue(2, 'Open conflict: ' + ', '.join(claim['conflict_ids']))
        if claim.get('review_by') and instant(claim['review_by']) < cutoff:
            issue(1, 'Review checkpoint passed')
        if claim.get('type') == 'MODEL_ASSUMPTION':
            if packet['run_id'] not in claim.get('authorized_runs', []):
                issue(1, 'Assumption not reauthorized for this run')
            if not claim.get('mechanism') or not claim.get('sensitivity'):
                issue(2, 'Assumption lacks mechanism/sensitivity')
        if claim.get('type') in {'OBSERVED', 'COMPANY_CLAIM'} and not claim.get('source_ids'):
            issue(3, 'Observed/vendor claim lacks original sources')
        if claim.get('type') in {'DERIVED', 'MODEL_ASSUMPTION'} and not claim.get('ancestors'):
            issue(2, 'No identified supporting ancestors')
        if claim.get('type') == 'DERIVED' and not (isinstance(claim.get('formula'), str) and claim['formula'].strip()):
            issue(2, 'Derived claim lacks an explicit transformation formula')
        for sid in claim.get('source_ids', []):
            source = sources.get(sid)
            if source is None:
                issue(3, 'Missing source: ' + sid)
                continue
            if source.get('data_mode') not in ('LIVE', 'SYNTHETIC') or type(source.get('retired')) is not bool:
                issue(1, 'Unknown source admissibility: ' + sid)
            if source.get('data_mode') and source['data_mode'] != packet['data_mode']:
                issue(3, 'Source data-mode mismatch: ' + sid)
            if source.get('retired') is True:
                issue(3, 'Retired source: ' + sid)
            if not source.get('origin_cluster') or not source.get('url') or not source.get('version'):
                issue(2, 'Incomplete source provenance: ' + sid)
            else:
                origins.add(source['origin_cluster'])
            for key in ('first_public_at', 'available_at'):
                if not source.get(key):
                    issue(1, 'Unknown ' + key + ': ' + sid)
                elif instant(source[key]) > cutoff:
                    issue(3, 'Future source ancestor: ' + sid)
        for parent in claim.get('ancestors', []):
            result = inspect(parent, active | {cid})
            origins.update(result['origins'])
            parent_level = {'REUSE_CANDIDATE': 0, 'REVALIDATE': 1, 'LEAD_ONLY': 2, 'EXCLUDE': 3}[result['decision']]
            if parent_level:
                issue(parent_level, 'Ancestor ' + parent + ': ' + '; '.join(result['reasons']))
        result = {'decision': ['REUSE_CANDIDATE', 'REVALIDATE', 'LEAD_ONLY', 'EXCLUDE'][level],
                  'reasons': reasons, 'origins': sorted(origins)}
        memo[cid] = result
        return result

    output = {}
    for binding in packet['bindings']:
        bid = binding['id']
        if bid in output:
            raise ValueError('Duplicate binding ID: ' + bid)
        cid = binding['claim_id']
        result = copy.deepcopy(inspect(cid, set()))
        actual = claims.get(cid, {}).get('scope', {})
        required = binding.get('required_scope', {})
        mismatches = [key for key, value in required.items() if actual.get(key) != value]
        if not required or mismatches:
            result['decision'] = 'EXCLUDE'
            result['reasons'].append('Scope mismatch or missing applicability: ' + ', '.join(mismatches))
        for required_key, claim_key in [('required_unit', 'unit'), ('required_definition_id', 'definition_id')]:
            if not binding.get(required_key) or binding[required_key] != claims.get(cid, {}).get(claim_key):
                result['decision'] = 'EXCLUDE'
                result['reasons'].append('Unit/definition mismatch; bind an accepted converted claim: ' + required_key)
        result.update(claim_id=cid, node_id=binding['node_id'])
        output[bid] = result
    return {'bindings': output, 'limitation': 'Structural candidate reuse only; source truth, economic applicability and security are not verified'}


def impact(packet, changed):
    """Conservative reachability on explicitly supplied dependency edges."""
    adjacency = {}
    for edge in packet.get('dependencies', []):
        adjacency.setdefault(edge['from'], set()).add(edge['to'])
    # Declared provenance/bindings are dependencies even if omitted from a diagram.
    for claim in packet.get('claims', []):
        for parent in claim.get('source_ids', []) + claim.get('ancestors', []):
            adjacency.setdefault(parent, set()).add(claim['id'])
    for binding in packet.get('bindings', []):
        adjacency.setdefault(binding['claim_id'], set()).add(binding['node_id'])
    affected, queue = set(changed), list(changed)
    while queue:
        node = queue.pop()
        for child in adjacency.get(node, set()):
            if child not in affected:
                affected.add(child)
                queue.append(child)
    routes = [r['id'] for r in packet.get('routes', []) if affected.intersection(r['depends_on'])]
    return {'affected_nodes': sorted(affected), 'routes_to_review': sorted(routes),
            'limitation': 'Review candidates only. Does not decide trigger truth, materiality, new values or eligibility.'}


def example():
    return {
        'data_mode': 'SYNTHETIC', 'run_id': 'TEST-R1', 'cutoff': '2030-01-15T21:00:00Z',
        'sources': [{'id': 'S1-v1', 'origin_cluster': 'ISSUER_RELEASE', 'url': 'synthetic://source',
                     'data_mode': 'SYNTHETIC', 'retired': False,
                     'version': 'v1', 'first_public_at': '2030-01-01T10:00:00Z', 'available_at': '2030-01-01T10:00:00Z'}],
        'claims': [{'id': 'C1-v1', 'type': 'COMPANY_CLAIM', 'status': 'ACCEPTED', 'data_mode': 'SYNTHETIC',
                    'scope': {'product': 'R', 'geography': 'GLOBAL', 'period': '2030Q1'},
                    'unit': 'qualified modules/quarter', 'definition_id': 'qualified_good_output',
                    'locator': 'S1-v1 table1', 'source_ids': ['S1-v1'], 'ancestors': []}],
        'bindings': [{'id': 'B1', 'claim_id': 'C1-v1', 'node_id': 'shared_capacity',
                      'required_scope': {'product': 'R', 'geography': 'GLOBAL', 'period': '2030Q1'},
                      'required_unit': 'qualified modules/quarter', 'required_definition_id': 'qualified_good_output'}],
        'dependencies': [{'from': 'C1-v1', 'to': 'shared_capacity'}, {'from': 'shared_capacity', 'to': 'issuer_A'},
                         {'from': 'shared_capacity', 'to': 'issuer_B'}],
        'routes': [{'id': 'A', 'depends_on': ['issuer_A']}, {'id': 'B', 'depends_on': ['issuer_B']},
                   {'id': 'UNRELATED', 'depends_on': ['issuer_C']}]
    }


class MemoryTests(unittest.TestCase):
    def decision(self, p):
        return review(p)['bindings']['B1']['decision']

    def test_valid_shared_evidence_and_mirror(self):
        p = example()
        mirror = dict(p['sources'][0], id='MIRROR', url='synthetic://mirror')
        p['sources'].append(mirror)
        p['claims'][0]['source_ids'].append('MIRROR')
        result = review(p)['bindings']['B1']
        self.assertEqual(result['decision'], 'REUSE_CANDIDATE')
        self.assertEqual(result['origins'], ['ISSUER_RELEASE'])

    def test_future_recursive_ancestor(self):
        p = example()
        p['sources'][0]['first_public_at'] = '2030-01-20T10:00:00Z'
        derived = dict(p['claims'][0], id='D1', type='DERIVED', formula='identity(C1-v1)', source_ids=[], ancestors=['C1-v1'])
        p['claims'].append(derived)
        p['bindings'][0]['claim_id'] = 'D1'
        self.assertEqual(self.decision(p), 'EXCLUDE')

    def test_assumption_requires_new_authorization(self):
        p = example()
        p['claims'].append(dict(p['claims'][0], id='A1', type='MODEL_ASSUMPTION', source_ids=[],
            ancestors=['C1-v1'], mechanism='Synthetic supply ramp', sensitivity='Slower qualification', authorized_runs=['OLD']))
        p['bindings'][0]['claim_id'] = 'A1'
        self.assertEqual(self.decision(p), 'REVALIDATE')
        p['claims'][1]['authorized_runs'] = ['TEST-R1']
        self.assertEqual(self.decision(p), 'REUSE_CANDIDATE')
        p['claims'][1]['review_by'] = '2030-01-10T00:00:00Z'
        self.assertEqual(self.decision(p), 'REVALIDATE')

    def test_scope_conflict_retirement_and_synthetic_separation(self):
        p = example()
        p['bindings'][0]['required_scope']['product'] = 'OTHER_GRADE'
        self.assertEqual(self.decision(p), 'EXCLUDE')
        p = example()
        p['claims'][0]['conflict_ids'] = ['CONFLICT']
        self.assertEqual(self.decision(p), 'LEAD_ONLY')
        p['claims'][0]['retired'] = True
        self.assertEqual(self.decision(p), 'EXCLUDE')
        p = example()
        p['data_mode'] = 'LIVE'
        self.assertEqual(self.decision(p), 'EXCLUDE')

    def test_shared_change_reopens_two_routes_not_unrelated(self):
        p = example()
        p['dependencies'].append({'from': 'issuer_B', 'to': 'shared_capacity'})
        self.assertEqual(impact(p, ['C1-v1'])['routes_to_review'], ['A', 'B'])

    def test_fact_cycle_and_missing_parent(self):
        p = example()
        p['claims'][0]['ancestors'] = ['C1-v1']
        self.assertEqual(self.decision(p), 'EXCLUDE')
        p['claims'][0]['ancestors'] = ['MISSING']
        self.assertEqual(self.decision(p), 'EXCLUDE')

    def test_unknown_availability_and_duplicate_ids(self):
        p = example()
        del p['sources'][0]['available_at']
        self.assertEqual(self.decision(p), 'REVALIDATE')
        p['claims'].append(copy.deepcopy(p['claims'][0]))
        with self.assertRaises(ValueError):
            review(p)

    def test_source_flags_propagate_to_derived_claim(self):
        for mutation in [{'retired': True}, {'data_mode': 'LIVE'}]:
            p = example()
            p['sources'][0].update(mutation)
            p['claims'].append(dict(p['claims'][0], id='D1', type='DERIVED', formula='identity(C1-v1)', source_ids=[], ancestors=['C1-v1']))
            p['bindings'][0]['claim_id'] = 'D1'
            self.assertEqual(self.decision(p), 'EXCLUDE')
        p = example()
        del p['sources'][0]['retired']
        self.assertEqual(self.decision(p), 'REVALIDATE')

    def test_target_unit_and_definition_require_explicit_conversion(self):
        p = example()
        p['claims'][0]['unit'] = 'kg/quarter'
        p['bindings'][0]['required_unit'] = 'tonnes/quarter'
        self.assertEqual(self.decision(p), 'EXCLUDE')
        p['claims'].append(dict(p['claims'][0], id='D1', type='DERIVED', unit='tonnes/quarter',
            source_ids=[], ancestors=['C1-v1'], formula='C1-v1 / 1000'))
        p['bindings'][0]['claim_id'] = 'D1'
        self.assertEqual(self.decision(p), 'REUSE_CANDIDATE')
        p['bindings'][0]['required_definition_id'] = 'annual_nameplate_capacity'
        self.assertEqual(self.decision(p), 'EXCLUDE')

    def test_null_source_admissibility_propagates(self):
        for invalid in [{'data_mode': None, 'retired': None}, {'retired': 'false'}, {'retired': 0}]:
            p = example()
            p['sources'][0].update(invalid)
            p['claims'].append(dict(p['claims'][0], id='D1', type='DERIVED', formula='identity(C1-v1)', source_ids=[], ancestors=['C1-v1']))
            p['bindings'][0]['claim_id'] = 'D1'
            self.assertEqual(self.decision(p), 'REVALIDATE')


    def test_derived_conversion_requires_formula(self):
        p=example()
        p['claims'].append(dict(p['claims'][0],id='D1',type='DERIVED',source_ids=[],ancestors=['C1-v1']))
        p['bindings'][0]['claim_id']='D1'
        self.assertEqual(self.decision(p),'LEAD_ONLY')
        p['claims'][1]['formula']='C1-v1 / 1000'
        p['claims'][1]['unit']='tonnes/quarter'
        p['claims'][0]['unit']='kg/quarter'
        p['bindings'][0]['required_unit']='tonnes/quarter'
        self.assertEqual(self.decision(p),'REUSE_CANDIDATE')

    def test_source_and_derived_lineage_invalidate_only_descendants(self):
        p=example()
        self.assertEqual(impact(p,['S1-v1'])['routes_to_review'],['A','B'])
        p['claims'].append(dict(p['claims'][0],id='D1',type='DERIVED',source_ids=[],ancestors=['C1-v1'],formula='identity(C1-v1)'))
        p['bindings'][0]['claim_id']='D1'
        p['dependencies']=[e for e in p['dependencies'] if e['from']!='C1-v1']
        result=impact(p,['S1-v1'])
        self.assertEqual(result['routes_to_review'],['A','B'])
        self.assertIn('D1',result['affected_nodes'])
        self.assertNotIn('issuer_C',result['affected_nodes'])
        self.assertEqual(impact(p,['irrelevant'])['routes_to_review'],[])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('packet', nargs='?')
    parser.add_argument('--changed', nargs='+', help='Return dependency impact for these supplied node IDs')
    parser.add_argument('--example', action='store_true')
    parser.add_argument('--self-test', action='store_true')
    args = parser.parse_args()
    if args.self_test:
        result = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(MemoryTests))
        return 0 if result.wasSuccessful() else 1
    if args.example:
        print(json.dumps(example(), indent=2))
        return 0
    if not args.packet:
        parser.error('Provide packet, --example or --self-test')
    try:
        packet = json.loads(Path(args.packet).read_text(encoding='utf-8'))
        result = impact(packet, args.changed) if args.changed else review(packet)
        print(json.dumps(result, indent=2))
        return 0
    except (KeyError, TypeError, ValueError, OSError) as exc:
        print(json.dumps({'error': str(exc)}))
        return 1


if __name__ == '__main__':
    sys.exit(main())
