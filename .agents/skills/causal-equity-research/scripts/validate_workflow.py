"""Read-only checks of declared research readiness and deliverable completion.

Does not run agents, authenticate timestamps/hashes, or establish factual quality.
"""
import argparse, copy, hashlib, json, sys, unittest
from pathlib import Path
from datetime import datetime

STATES={'QUEUED','READY','RUNNING','RETURNED','ACCEPTED','REWORK','BLOCKED'}

def close_book(p, book_bytes, expected_hash):
    """Check declared close coverage against externally receipted bytes; content needs review."""
    if not book_bytes or not isinstance(expected_hash,str):
        return ['Missing discovery route book or its origin receipt hash']
    if hashlib.sha256(book_bytes).hexdigest()!=expected_hash.lower():
        return ['Route book differs from discovery receipt']
    try:
        book=json.loads(book_bytes)
        if not isinstance(book,dict):raise ValueError()
        rows,coverage=book.get('routes'),p['frontier'].get('coverage')
        filled=lambda v:isinstance(v,str) and bool(v.strip())
        def indexed(items):
            if not isinstance(items,list) or not items or not all(isinstance(r,dict) and filled(r.get('id')) for r in items):raise ValueError()
            by_id={r['id']:r for r in items}
            if len(by_id)!=len(items):raise ValueError()
            return by_id
        routes,close=indexed(rows),indexed(coverage)
    except (ValueError,TypeError,UnicodeError):
        return ['Malformed or duplicate discovery/close route records']
    errors=[]
    if set(routes)!=set(close):errors.append('Discovery/close coverage differs: '+str(sorted(set(routes)^set(close))))
    for rid in sorted(routes.keys() & close.keys()):
        r,c=routes[rid],close[rid];d=c.get('disposition');choice=p['frontier'].get('choice')
        if not filled(r.get('source')) or type(r.get('investable')) is not bool or ('check_now' in r and not filled(r['check_now'])):
            errors.append('Incomplete discovery basis: '+rid)
        if d not in ('modeled','bounded','contradicted','wait','open','evidence_only') or not filled(c.get('basis')):
            errors.append('Incomplete disposition: '+rid)
        if (d=='evidence_only' and r.get('investable') is not False) or (d=='modeled' and r.get('investable') is not True):
            errors.append('Venue/disposition mismatch: '+rid)
        if d in ('wait','open') and not all(filled(c.get(k)) for k in ('owner','next')):
            errors.append('Unowned or unspecified follow-up: '+rid)
        if r.get('check_now') and d!='open' and not filled(c.get('check_evidence')):
            errors.append('Available check unaccounted for: '+rid)
        if (d=='open' and (choice!='budget' or p['delivery'].get('status') not in ('PARTIAL','BLOCKED'))) or (d=='wait' and choice=='stop'):
            errors.append('Close conceals unfinished work: '+rid)
    return errors

def validate(p, require_frontier=False, book_bytes=None, expected_hash=None):
    errors=[]
    def need(ok,msg):
        if not ok: errors.append(msg)
    def instant(value,label):
        try:
            parsed=datetime.fromisoformat(value.replace('Z','+00:00'))
            if parsed.tzinfo is None:raise ValueError('Timezone missing')
            return parsed
        except (AttributeError,TypeError,ValueError):
            errors.append('Missing/invalid timestamp: '+label)
            return None
    tasks={t['id']:t for t in p['tasks']}
    artifacts={a['id']:a for a in p['artifacts']}
    need(len(tasks)==len(p['tasks']), 'Duplicate task IDs')
    need(len(artifacts)==len(p['artifacts']), 'Duplicate artifact IDs')
    for a in p['artifacts']:
        need(a['owner_task'] in tasks, 'Artifact owner missing: '+a['id'])
        if a.get('accepted'):
            need(bool(a.get('version') and a.get('sha256') and a.get('accepted_scope') and a.get('reviewer') and a.get('accepted_at')),
                 'Incomplete acceptance: '+a['id'])
            instant(a.get('accepted_at'),a['id']+' accepted_at')
    graph={tid:set() for tid in tasks}
    for t in p['tasks']:
        tid=t['id'];need(t['status'] in STATES, 'Invalid lifecycle state: '+tid)
        started=None
        if t['status'] in {'RUNNING','RETURNED','ACCEPTED'} or t.get('started_at'):
            started=instant(t.get('started_at'),tid+' started_at')
        for dep in t.get('requires',[]):
            a=artifacts.get(dep['artifact_id'])
            if a: graph[tid].add(a['owner_task'])
            if t['status'] in {'READY','RUNNING','RETURNED','ACCEPTED'}:
                need(a is not None, 'Missing prerequisite: '+tid)
                if a:
                    need(a.get('accepted') is True, 'Unaccepted prerequisite: '+tid)
                    need(dep['scope'] in a.get('accepted_scope',[]), 'Prerequisite scope mismatch: '+tid)
                    need(dep['version']==a.get('version') and dep['sha256']==a.get('sha256'), 'Prerequisite version mismatch: '+tid)
                    if started is not None:
                        at=instant(a.get('accepted_at'),a['id']+' accepted_at')
                        if at is not None:need(at<=started,'Input accepted after start: '+tid)
        if t['status']=='ACCEPTED':
            output=t.get('output_ids',[])
            need(bool(output),'Accepted task has no outputs: '+tid)
            for aid in output:
                a=artifacts.get(aid)
                need(a is not None and a.get('accepted') is True and a['owner_task']==tid,'Unsupported accepted output: '+tid)
        if t.get('independent_first_pass') and t['status'] in {'READY','RUNNING','RETURNED','ACCEPTED'}:
            need(bool(t.get('input_manifest_hash')),'Independent input manifest absent: '+tid)
            need(not t.get('peer_conclusion_ids'),'Peer conclusion in independent pass: '+tid)
    visited=set();active=set()
    def visit(tid):
        if tid in active: errors.append('Cyclic task prerequisites: '+tid);return
        if tid in visited:return
        active.add(tid)
        for parent in graph.get(tid,[]):visit(parent)
        active.remove(tid);visited.add(tid)
    for tid in tasks:visit(tid)
    for route in p.get('revisits',[]):
        need(route.get('trigger_status') in {'pending','met','not_met','unknown'},'Missing trigger disposition: '+route['id'])
        need(bool(route.get('checkpoint_id') and route.get('next_question') and route.get('owner')),'Incomplete revisit action: '+route['id'])
        if route.get('trigger_status')=='met':
            need(bool(route.get('evidence_ids') and route.get('queued_task_id') in tasks),'Met trigger has no evidence/task: '+route['id'])
    d=p['delivery']
    need(d['status'] in {'COMPLETE','PARTIAL','BLOCKED'},'Unknown delivery status')
    need(bool(d['required_scopes']),'Requested output scope not declared')
    if d['status']=='COMPLETE':
        need(not d.get('missing_components'),'Complete delivery still has missing components')
        for scope in d['required_scopes']:
            need(any(artifacts.get(aid,{}).get('accepted') is True and scope in artifacts[aid].get('accepted_scope',[]) for aid in d.get('artifact_ids',[])),
                 'Requested deliverable scope absent: '+scope)
    else:
        need(bool(d.get('missing_components')),'Partial/blocked delivery lacks exact missing component')
    if require_frontier or (p.get('work_mode')=='broad_search' and d['status']=='COMPLETE') or 'frontier' in p:
        f=p.get('frontier')
        if not isinstance(f,dict):
            return errors+['Broad allocation/close lacks a frontier comparison']
        instant(f.get('reviewed_at'),'frontier reviewed_at')
        options=f.get('options')
        if not isinstance(options,list) or not options or not all(isinstance(o,dict) for o in options):
            return errors+['Frontier comparison has no usable options']
        filled=lambda x:isinstance(x,str) and bool(x.strip())
        ids=[o.get('id') for o in options]
        need(all(filled(x) for x in ids) and len(set(map(str,ids)))==len(ids),'Frontier option IDs missing/duplicated')
        need(len(options)>1 or filled(f.get('comparison_limit')),'Single option without a comparison boundary')
        need(all(all(filled(o.get(k)) for k in ('question','source_or_limit','decision_effect'))
                 and o.get('state') in ('actionable','invariant','unavailable') for o in options),
             'Missing frontier discriminator, evidence boundary or effect')
        action=f.get('choice'); checkpoint=f.get('checkpoint')
        need(checkpoint in ('repeat','close') and filled(f.get('reason')), 'Missing allocation checkpoint/reason')
        need(action in ('work','wait','stop','budget'), 'Unknown frontier choice')
        can_act=[o.get('id') for o in options if o.get('state')=='actionable']
        if action=='work':
            need(checkpoint=='repeat' and f.get('selected') in can_act,'Work must select an actionable question before dispatch')
            tid=f.get('task_id')
            task=tasks.get(tid,{}) if isinstance(tid,str) else {}
            need(task.get('status') in ('QUEUED','READY','RUNNING') and task.get('frontier_option_id')==f.get('selected'),
                 'Selected question has no matching active task')
        else:
            need(checkpoint=='close','Repeat dispatch requires a chosen task')
        if action in ('wait','stop'):
            need(not can_act, 'Stopping despite an identified actionable discriminator')
        if action=='wait':
            need(any(o.get('state')=='unavailable' for o in options) and filled(f.get('reopen')),
                 'Waiting needs unavailable evidence and an observable checkpoint')
        if action=='stop':
            need(all(o.get('state')=='invariant' for o in options),'Unresolved evidence requires wait or explicit unfinished scope')
        if action=='budget':
            need(d['status'] in ('PARTIAL','BLOCKED') and any(isinstance(m,dict) and m.get('scope')=='discovery'
                 and filled(m.get('next_evidence')) for m in d.get('missing_components',[])),
                 'Resource limit must disclose unfinished discovery and its next question')
        if p.get('work_mode')=='broad_search' and checkpoint=='close':
            errors.extend(close_book(p,book_bytes,expected_hash))
    return errors

def fixture():
    return {'artifacts':[{'id':'DISC-v1','owner_task':'DISC','version':1,'sha256':'SYNTHETIC-HASH',
        'accepted':True,'accepted_scope':['discovery'],'reviewer':'O00','accepted_at':'2030-01-01T12:00:00Z'}],
        'tasks':[{'id':'DISC','status':'ACCEPTED','started_at':'2030-01-01T11:00:00Z','requires':[],'output_ids':['DISC-v1']},
                 {'id':'MODEL','status':'READY','requires':[{'artifact_id':'DISC-v1','version':1,'sha256':'SYNTHETIC-HASH','scope':'discovery'}]}],
        'revisits':[], 'delivery':{'status':'PARTIAL','required_scopes':['horizon_forecast'],'artifact_ids':['DISC-v1'],
        'missing_components':[{'scope':'horizon_forecast','owner':'A13','next_evidence':'accepted operating and recognition models'}]}}

class Tests(unittest.TestCase):
    def test_valid_partial_work_is_allowed(self): self.assertEqual(validate(fixture()),[])
    def test_unaccepted_or_wrong_scope_is_not_ready(self):
        for key,val in [('accepted',False),('accepted_scope',['conditional_value']),('version',2)]:
            p=fixture();p['artifacts'][0][key]=val;self.assertTrue(validate(p))
    def test_completion_requires_requested_output_type(self):
        p=fixture();p['delivery'].update(status='COMPLETE',missing_components=[])
        self.assertTrue(validate(p))
        p['artifacts'][0]['accepted_scope'].append('horizon_forecast')
        self.assertEqual(validate(p),[])
    def test_independence_and_acceptance_clock(self):
        p=fixture();p['tasks'][1].update(independent_first_pass=True,peer_conclusion_ids=['favored_target'])
        self.assertTrue(validate(p))
        p=fixture();p['tasks'][1]['started_at']='2030-01-01T11:00:00Z';self.assertTrue(validate(p))
    def test_revisit_requires_concrete_action(self):
        p=fixture();p['revisits']=[{'id':'R','trigger_status':'met','checkpoint_id':'comparison2','next_question':'new qualification','owner':'A06'}]
        self.assertTrue(validate(p))
        p['revisits'][0].update(evidence_ids=['S1'],queued_task_id='MODEL');self.assertEqual(validate(p),[])
    def test_task_cycle_rejected(self):
        p=fixture();p['tasks'][0]['requires']=copy.deepcopy(p['tasks'][1]['requires']);self.assertTrue(validate(p))
    def test_queued_independent_task_may_wait_for_manifest(self):
        p=fixture();p['tasks'][1].update(status='QUEUED',independent_first_pass=True)
        self.assertEqual(validate(p),[])
    def test_begun_task_and_accepted_input_require_valid_times(self):
        p=fixture();p['tasks'][1]['status']='RUNNING';self.assertTrue(validate(p))
        p['tasks'][1]['started_at']='2030-01-01T13:00:00Z';self.assertEqual(validate(p),[])
        p['artifacts'][0]['accepted_at']='not a date';self.assertTrue(validate(p))

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('packet',nargs='?');parser.add_argument('--self-test',action='store_true');parser.add_argument('--example',action='store_true');parser.add_argument('--frontier',action='store_true',help='Require a broad-search allocation or closeout comparison');parser.add_argument('--route-book');parser.add_argument('--book-sha256');a=parser.parse_args()
    if a.self_test:return 0 if unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(Tests)).wasSuccessful() else 1
    if a.example:print(json.dumps(fixture(),indent=2));return 0
    if not a.packet:parser.error('Provide a packet, --example or --self-test')
    try:errors=validate(json.loads(Path(a.packet).read_text(encoding='utf-8')),a.frontier,Path(a.route_book).read_bytes() if a.route_book else None,a.book_sha256)
    except (KeyError,TypeError,ValueError,OSError) as e:errors=['Malformed workflow record: '+str(e)]
    print(json.dumps({'structural_checks':'FAIL' if errors else 'PASS','errors':errors,'scope':'Declared workflow only, not evidence truth, complete execution trace or security.'},indent=2));return bool(errors)
if __name__=='__main__':sys.exit(main())
