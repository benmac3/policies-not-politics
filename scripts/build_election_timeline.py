#!/usr/bin/env python3
"""Build and validate the standalone federal-election review. Python 3.10+, stdlib only.
Run: python scripts/build_election_timeline.py [--check-only] [--output-dir PATH]
No network requests, no writes to the released app or shared data bundles.
"""
from __future__ import annotations
import argparse
import csv
import hashlib
import json
import re
from collections import Counter
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AS_OF = '2026-10-06'
COALITION = {'LIB','CP','NCP','NP','LNP','CLP'}
ELECTION_TYPES = {'general','senate_only','senate_rerun','senate_special'}
HOUSE_TOTALS = [75,75,75,75,75,75,75,75,76,76,76,76,76,75,75,75,75,75,123,123,123,124,124,124,124,124,125,125,127,127,124,125,125,148,148,148,147,148,148,150,150,150,150,150,150,151,151,150]
# Independently specified expected numbers of places filled at each Senate contest.
SENATE_WON = dict(zip([1901,1903,1906,1910,1913,1914,1917,1919,1922,1925,1928,1931,1934,1937,1940,1943,1946,1949,1951,1953,1955,1958,1961,1963,1964,1966,1967,1969,1970,1972,1974,1975,1977,1980,1983,1984,1987,1990,1993,1996,1998,2001,2004,2007,2010,2013,2016,2019,2022,2025], [36,19,18,18,18,36,18,19,19,22,19,18,18,19,19,19,19,42,60,32,30,32,31,1,30,6,30,2,32,1,60,64,34,34,64,46,76,40,40,40,40,40,40,40,40,40,76,40,40,40]))
UNOPPOSED = {'1956-04-11':'1956-04-28','1928-09-03':'1928-09-22','1915-05-06':'1915-05-15','1913-12-22':'1914-01-17'}
FORMATION = {1910:'1910-04-29',1913:'1913-06-24',1914:'1914-09-17',1922:'1923-02-09',1929:'1929-10-22',1931:'1932-01-06',1949:'1949-12-19',1972:'1972-12-05',1983:'1983-03-11',1996:'1996-03-11',2007:'2007-12-03',2013:'2013-09-18',2022:'2022-05-23'}
SPECIAL_DELTAS = {1963:{'ALP':-1,'LIB':1},1966:{'LIB':-1,'ALP':1},1969:{'LIB':-1,'ALP':1},1972:{'LIB':0}}

def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)

def read_sections(path: Path) -> dict:
    sections, section, header = {}, None, None
    for n, raw in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
        if not raw.strip() or raw.startswith('#'):
            continue
        if raw.startswith('@'):
            section, header = raw[1:], None
            require(section not in sections, f'Duplicate section at line {n}')
            sections[section] = []
            continue
        require(section is not None, f'Row outside section at line {n}')
        fields = [x.strip() for x in raw.split('|')]
        if header is None:
            header = fields
        else:
            require(len(fields)==len(header), f'Column mismatch at line {n}: {len(fields)} != {len(header)}')
            sections[section].append(dict(zip(header, fields)))
    return sections

def seat_map(text: str, parties: dict) -> dict | None:
    if not text:
        return None
    output = {}
    for token in text.split():
        code, number = token.split(':')
        require(code in parties and code not in output, f'Unknown or duplicate party: {code}')
        output[code] = int(number)
        require(output[code] > 0, f'Non-positive seat count: {token}')
    return output

def slug(text: str) -> str:
    return re.sub(r'[^a-z0-9]+','-',text.lower()).strip('-')

def holder(leadership: list, office: str, on_date: str) -> dict | None:
    return next((x for x in reversed(leadership) if x['office']==office and x['date']<=on_date), None)

def compile_data(path: Path) -> dict:
    sections = read_sections(path)
    sources = {r['id']:{**r,'retrieved':'2026-10-06'} for r in sections['sources']}
    parties = {r['code']:r for r in sections['parties']}
    leadership = []
    for r in sections['leadership']:
        leadership.append({'id':f"{r['office'].lower()}-{r['date']}", 'date':r['date'], 'type':r['office'].lower(), 'office':r['office'], 'person':r['person'] or None, 'party_at_accession':r['party'] or None, 'title':f"{r['office']}: {r['person'] or 'office vacant'}", 'note':r['note'], 'source_ids':['PM_LIST','NMA_PM'] if r['office']=='PM' else ['DPM_LIST'], 'evidence':'sourced_chronology'})
        if r['date'] in {'1945-07-05','1945-07-06'}:
            leadership[-1]['source_ids']=['NAA_FORDE']
        if r['date']=='2022-05-23':
            leadership[-1]['source_ids'].append('MINISTRY')
    leadership.sort(key=lambda e:(e['date'],e['id']))
    events = list(leadership)
    elections = []
    for kind in ['general','senate_only','senate_rerun','senate_special']:
        for r in sections[kind]:
            year = int(r['date'][:4])
            h = seat_map(r['house'],parties)
            sw = seat_map(r['senate_elected'],parties)
            sf = seat_map(r['senate_full'],parties)
            hs = 'H2013' if year in (2010,2013) else 'H2019' if year in (2016,2019) else f'H{year}' if year in (2022,2025) else 'PL2010'
            ss = f'S{year}' if year in (1908,1963,1966,1969,1972,2013,2014,2016,2019,2022,2025) else 'PL2010'
            fs = f'C{year}' if year in (2019,2022,2025) else 'S2013' if year in (2013,2014) else ss if year in (1963,1966,1969,2016) else 'PL2010'
            pm = holder(leadership,'PM',r['date'])
            deputy = holder(leadership,'DPM',r['date'])
            result_pm = holder(leadership,'PM',FORMATION.get(year,r['date'])) if kind=='general' else None
            labels = {'general':f'{year} federal election','senate_only':f'{year} Senate-only election','senate_rerun':'2014 WA Senate rerun','senate_special':'1908 SA Senate supplementary poll'}
            basis = 'as_reported_after_elected_senators_take_places' if year<=2010 else 'outcome_projection_not_live_membership'
            if year in (1963,1969): basis = 'reconstructed_benchmark_plus_election_delta_review_required'
            if year==1966: basis='secondary_reported_composition_review_required'
            if year==2016: basis='original_full_senate_election_returns'
            if year==2013: basis='superseded_projection_WA_return_annulled'
            ev = {'id':f'{kind}-{year}', 'date':r['date'], 'type':kind, 'title':labels[kind], 'house':h, 'senate_elected':sw, 'senate_full':sf, 'house_total':sum(h.values()) if h else None, 'senate_elected_total':sum(sw.values()) if sw else None, 'senate_full_total':sum(sf.values()) if sf else None, 'senate_full_basis':basis if sf else 'not_verified' if sw else 'not_contested', 'senate_contest':'casual_vacancy' if year in SPECIAL_DELTAS else 'supplementary' if kind=='senate_special' else 'rerun' if kind=='senate_rerun' else 'regular' if sw else 'not_contested', 'house_source_ids':[hs] if h else [], 'senate_source_ids':[ss] if sw else [], 'senate_full_source_ids':[fs] if sf else [], 'pm_at_poll':pm['person'] if pm else None, 'deputy_at_poll':deputy['person'] if deputy else None, 'pm_after_formation':result_pm['person'] if result_pm else None, 'pm_appointment_date':FORMATION.get(year) if kind=='general' else None, 'note':r['notes'], 'source_ids':list(dict.fromkeys(['AEC_DATES']+([hs] if h else [])+([ss] if sw else [])+([fs] if sf else [])+['PM_LIST'])), 'status':'partially_annulled' if year==2013 else 'original_return', 'historical_other_seats':h.get('OTH',0) if h else 0}
            if year==2025: ev['source_ids'].append('D2025')
            if year==1901: ev['poll_end_date']='1901-03-30'
            if year in SPECIAL_DELTAS:
                ev['senate_party_delta']=SPECIAL_DELTAS[year]
                if year in (1963,1969): ev['senate_full_source_ids'].append('PL2010')
                if year==1969: ev['source_ids'].append('S1969V')
            if year==2014: ev['replaces_event_component']={'event_id':'general-2013','state':'WA','places':6}
            elections.append(ev)
    elections.sort(key=lambda e:e['date'])
    for ev in elections:
        for chamber in ['house','senate_full']:
            if ev[chamber] is None:
                ref = next((x for x in reversed(elections) if x['date']<ev['date'] and x[chamber] is not None), None)
                ev[chamber+'_last_benchmark_id'] = ref['id'] if ref else None
    events.extend(elections)
    for r in sections['by_elections']:
        changed = r['before'] != r['after']
        delta = {r['before']:-1,r['after']:1} if changed else {r['after']:0}
        coalition_delta = sum(v for k,v in delta.items() if k in COALITION) if r['date']>='1949-01-01' else None
        pm = holder(leadership,'PM',r['date'])
        govt_delta = None
        if coalition_delta is not None and pm:
            govt_delta = delta.get('ALP',0) if pm['party_at_accession']=='ALP' else coalition_delta if pm['party_at_accession'] in COALITION else None
        ev = {'id':f"by-{r['date']}-{slug(r['division'])}", 'date':r['date'], 'type':'by_election', 'title':f"{r['division']} by-election", 'chamber':'House', 'division':r['division'], 'before_party':r['before'], 'after_party':r['after'], 'outgoing':r['outgoing'], 'incoming':r['incoming'], 'party_delta':delta, 'changed_party':changed, 'coalition_family_delta':coalition_delta, 'government_bloc_delta':govt_delta, 'delta_basis':'outgoing_affiliation_before_vacancy_vs_elected_party; not empty-seat baseline', 'pm_at_poll':pm['person'] if pm else None, 'note':r['note'], 'source_ids':['AEC_BY','BY_DETAIL'], 'status':'later_annulled' if r['division']=='Wills' and r['date']=='1992-04-11' else 'returned', 'needs_affiliation_review':'requires review' in r['note']}
        if r['date'] in UNOPPOSED:
            ev.update(date_basis='unopposed_return',poll_date=None,scheduled_poll_date=UNOPPOSED[r['date']])
        else: ev.update(date_basis='polling',poll_date=r['date'])
        if r['date']=='2026-05-09': ev['source_ids'].append('FARRER2026')
        events.append(ev)
    for r in sections['supplementary']:
        events.append({'id':f"supplementary-{slug(r['division'])}-{r['date'][:4]}", 'date':r['date'], 'type':'supplementary', 'title':f"{r['division']} supplementary poll", 'general_event_id':r['general_id'], 'note':r['note'], 'source_ids':['AEC_BY'], 'already_in_general_total':True})
    events.sort(key=lambda e:(e['date'],e['id']))
    return {'schema_version':'1.0.0-review','as_of':AS_OF,'title':'Australian federal elections & leadership','source_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'scope':'1901–2026; 48 general elections, Senate-only and supplementary contests, House by-elections, PM appointments, formal DPM office from 1968','sources':sources,'parties':parties,'events':events,'definitions':{'senate_elected':'Places filled in this contest only; not the full chamber.','senate_full':'Historical reporting basis varies and is recorded per row. Not live membership.','null':'Not contested or not verified, as stated; never replace with zero.','by_election_delta':'Compare party before vacancy with winner. An election-related delta, not a continuous confidence or majority ledger.','dpm':'Formal office from 1968; no routine acting appointments or pre-1968 de facto deputies.','other':'OTH is an unresolved source bucket, not a political party. Historical faction/state affiliate grouping is not uniform across eras.'}}

def validate(data: dict) -> dict:
    events=data['events']; parties=data['parties']; sources=data['sources']
    require(len({e['id'] for e in events})==len(events),'Duplicate event IDs')
    counts=Counter(e['type'] for e in events)
    require(counts['general']==48 and counts['senate_only']==4 and counts['senate_rerun']==1 and counts['senate_special']==1,'Election coverage mismatch')
    require(counts['by_election']==165, f"Expected 165 House by-elections, got {counts['by_election']}")
    generals=[e for e in events if e['type']=='general']
    require([e['house_total'] for e in generals]==HOUSE_TOTALS,'House totals do not reconcile to independent expected series')
    for e in events:
        require(date.fromisoformat(e['date'])<=date.fromisoformat(AS_OF),f"Future event {e['id']}")
        for sid in e['source_ids']: require(sid in sources, f'Unresolved source {sid}')
        if e['type'] in ELECTION_TYPES:
            year=int(e['date'][:4]); sw=e['senate_elected']; sf=e['senate_full']
            if sw:
                expected=6 if e['type']=='senate_rerun' else 1 if e['type']=='senate_special' else SENATE_WON[year]
                require(sum(sw.values())==expected,f"Senate places mismatch {year}")
            if sf:
                expected=36 if year<1949 else 60 if year<1975 else 64 if year<1984 else 76
                require(sum(sf.values())==expected,f"Full Senate mismatch {year}: {sum(sf.values())}")
            if e.get('senate_party_delta'): require(sum(e['senate_party_delta'].values())==0,'Senate delta imbalance')
        if e['type']=='by_election':
            require(e['before_party'] in parties and e['after_party'] in parties,'Unknown by-election party')
            require(sum(e['party_delta'].values())==0,'By-election delta imbalance')
        if e['type'] in {'pm','dpm'} and e['party_at_accession']:
            require(e['party_at_accession'] in parties,'Unknown leadership party')
    lookup={e['id']:e for e in events}
    require(lookup['general-2025']['house']['ALP']==94,'2025 ALP House regression')
    require(lookup['general-2025']['senate_elected']['ALP']==16,'2025 ALP Senate regression')
    require(lookup['general-2013']['status']=='partially_annulled','Lost WA annulment flag')
    require(lookup['by-1992-04-11-wills']['status']=='later_annulled','Lost Wills annulment flag')
    require(lookup['general-1966']['senate_elected_total']==6,'Lost special Senate contests')
    require(lookup['by-2018-07-28-mayo']['changed_party'] is False,'Party rename treated as transfer')
    require(lookup['general-1922']['pm_after_formation']=='Stanley Bruce','1922 formation regression')
    pm_people={e['person'] for e in events if e['type']=='pm' and e['person']}
    require(len(pm_people)==31,'PM roster mismatch')
    return {'passed':True,'as_of':AS_OF,'event_count':len(events),'counts':dict(counts),'pm_people':len(pm_people),'pm_appointments':sum(e['type']=='pm' and bool(e['person']) for e in events),'dpm_appointments':sum(e['type']=='dpm' and bool(e['person']) for e in events),'house_by_election_party_transfers':sum(e['type']=='by_election' and e['changed_party'] for e in events),'unresolved_house_groupings':sum(e.get('historical_other_seats',0)>0 for e in events),'affiliation_review_cases':sum(e.get('needs_affiliation_review',False) for e in events),'limits':'Arithmetic, schema and coverage checks passed; these do not constitute an independent source-by-source historical audit.'}

def write_outputs(data: dict, report: dict, output: Path) -> None:
    output.mkdir(parents=True, exist_ok=True)
    payload=json.dumps(data,ensure_ascii=False,separators=(',',':'))
    (output/'federal-election-timeline.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    (output/'validation-report.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    rows=[]
    for e in data['events']:
        for chamber in ['house','senate_elected','senate_full']:
            for party,seats in (e.get(chamber) or {}).items():
                rows.append({'event_id':e['id'],'date':e['date'],'measure':chamber,'party':party,'party_name':data['parties'][party]['name'],'seats':seats,'basis':e.get('senate_full_basis','') if chamber=='senate_full' else 'original_election_result','source_ids':';'.join(e.get('house_source_ids' if chamber=='house' else 'senate_source_ids' if chamber=='senate_elected' else 'senate_full_source_ids',[]))})
    with (output/'election-seats.csv').open('w',encoding='utf-8',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
    with (output/'event-index.csv').open('w',encoding='utf-8',newline='') as f:
        fields=['id','date','type','title','pm_at_poll','pm_after_formation','before_party','after_party','party_delta','note','source_ids']
        writer=csv.DictWriter(f,fieldnames=fields);writer.writeheader()
        for e in data['events']:
            writer.writerow({k:json.dumps(e[k],ensure_ascii=False) if isinstance(e.get(k),(dict,list)) else e.get(k,'') for k in fields})
    template=(ROOT/'reviews/federal-election-timeline.template.html').read_text(encoding='utf-8')
    require(template.count('__TIMELINE_DATA__')==1,'Template must contain exactly one data placeholder')
    html=template.replace('__TIMELINE_DATA__',payload.replace('<','\\u003c'))
    (output/'federal-election-timeline.html').write_text(html,encoding='utf-8')

def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check-only',action='store_true')
    parser.add_argument('--output-dir',type=Path,default=ROOT/'reviews/generated')
    args=parser.parse_args()
    data=compile_data(ROOT/'data/federal-election-timeline.psv')
    report=validate(data)
    print(json.dumps(report,indent=2))
    if not args.check_only: write_outputs(data,report,args.output_dir)

if __name__=='__main__':
    main()
