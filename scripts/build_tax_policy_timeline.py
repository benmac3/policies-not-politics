#!/usr/bin/env python3
"""Compile the offline Australian federal tax-policy review (Python 3.10+, stdlib).
Run from any directory: python scripts/build_tax_policy_timeline.py [--check-only].
No network requests. The source PSV is a curated transcription, not a raw-source archive.
"""
from __future__ import annotations
import argparse
import calendar
import csv
import hashlib
import json
import re
from collections import Counter
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AS_OF = '2026-10-15'
CATEGORIES = {'income':'Income tax & levies','cgt':'Capital gains tax','gearing':'Negative gearing & rental deductions','consumption':'GST & sales taxes','excise':'Fuel, alcohol & tobacco excise','trusts':'Trust taxation'}
STAGES = {'baseline':'Starting position / benchmark','announcement':'Announcement','enactment':'Legislative milestone','effective':'Application begins','expiry':'Expiry / reversal','judgment':'Court judgment','guidance':'ATO interpretation','proposal':'Introduced proposal','scheduled':'Future application'}
STATUSES = {'context':'Context — not a new law','historical_law':'Historical law event','enacted':'Enacted / implemented','enacted_future':'Enacted — future application','interpretation':'Judgment / guidance','proposed':'Proposal — enactment not verified'}
RELATED = {'reform2026-act':['gearing','income'],'reform2026-budget':['gearing'],'reform2026-details':['cgt','trusts'],'cgt-discount':['trusts'],'trust-stream':['cgt','income'],'trust-bendel':['income'],'wine-wet':['excise']}
LINKS = [('gearing-quarantine','gearing-restored'),('cgt-start','cgt-discount'),('reform2026-budget','reform2026-act'),('reform2026-act','cgt-2027'),('reform2026-act','gearing-2027'),('reform2026-act','worker-deduction'),('reform2026-act','wato-2027'),('trust2026-bill','trust-2028'),('trust2026-bill','reform2026-details'),('income-2024','income-2026'),('income-2026','income-2027'),('fuel-2022-cut','fuel-2022-end'),('fuel-2026-announcement','fuel-2026-start'),('fuel-2026-start','fuel-2026-july'),('fuel-2026-july','fuel-2026-end'),('trust-s100a','trust-s100a-guidance'),('div7a-start','trust-bendel'),('trust-loss-cutoff','trust-ftdt'),('lmito-start','lmito-2022'),('lmito-2022','lmito-end'),('repair-start','repair-end'),('flood-start','flood-end')]

def require(condition: bool, message: str) -> None:
    if not condition: raise ValueError(message)

def parse_sections(path: Path) -> dict:
    sections={}; section=None; header=None
    for n,line in enumerate(path.read_text(encoding='utf-8').splitlines(),1):
        if not line.strip() or line.startswith('#'): continue
        if line.startswith('@'):
            section=line[1:]; require(section not in sections,f'Duplicate section at line {n}')
            sections[section]=[]; header=None; continue
        require(section is not None,f'Row outside section at line {n}')
        fields=[x.strip() for x in line.split('|')]
        if header is None: header=fields; continue
        require(len(fields)==len(header),f'Column mismatch at line {n}: {len(fields)} != {len(header)}')
        sections[section].append(dict(zip(header,fields)))
    require(set(sections)=={'sources','events','rate_schedules'},'Unexpected or missing section')
    return sections

def date_info(value: str | None) -> dict | None:
    if not value: return None
    require(bool(re.fullmatch(r'\d{4}(-\d{2}(-\d{2})?)?',value)),f'Invalid partial date {value}')
    parts=[int(x) for x in value.split('-')]; y=parts[0]
    if len(parts)==1:
        start,end,plot=date(y,1,1),date(y,12,31),date(y,7,1); precision='year'
    elif len(parts)==2:
        m=parts[1]; start,end,plot=date(y,m,1),date(y,m,calendar.monthrange(y,m)[1]),date(y,m,15); precision='month'
    else:
        start=end=plot=date(*parts); precision='day'
    return {'value':value,'precision':precision,'earliest':str(start),'latest':str(end),'plot_date':str(plot)}

def basic_tax(schedule: dict, income: float) -> float:
    """Basic scale only. No deductions, offsets, Medicare, other levies or residency tests."""
    require(income>=0,'Negative income')
    return round(sum(max(0,min(income,b['upper'] if b['upper'] is not None else income)-b['lower'])*b['rate_percent']/100 for b in schedule['bands']),2)

def compile_data(path: Path) -> dict:
    raw=parse_sections(path)
    sources={s['id']:{**s,'retrieved':AS_OF} for s in raw['sources']}
    require(len(sources)==len(raw['sources']),'Duplicate source ID')
    events=[]
    for row in raw['events']:
        e={k:(v or None) for k,v in row.items() if k!='sources'}
        e['source_ids']=row['sources'].split(';')
        e['date_info']=date_info(e['date'])
        e['future_at_review']=e['date_info']['earliest']>AS_OF
        e['related_categories']=RELATED.get(e['id'],[])
        e['related_event_ids']=[b if a==e['id'] else a for a,b in LINKS if e['id'] in (a,b)]
        e['evidence_class']='project historical synthesis linked to identified sources'
        e['access_limited']=any('indexed' in sources[s]['access'] for s in e['source_ids'])
        events.append(e)
    events.sort(key=lambda e:(e['date_info']['earliest'],e['id']))
    schedules={}
    for row in raw['rate_schedules']:
        bounds=[int(x) for x in row['lower_bounds_aud'].split()]
        rates=[float(x) for x in row['marginal_rates_percent'].split()]
        require(len(bounds)==len(rates) and bounds==sorted(set(bounds)) and bounds[0]==0,'Invalid rate boundaries')
        bands=[]; base=0.0
        for i,(lower,rate) in enumerate(zip(bounds,rates)):
            upper=bounds[i+1] if i+1<len(bounds) else None
            bands.append({'lower':lower,'upper':upper,'rate_percent':rate,'basic_tax_at_lower':round(base,2)})
            if upper is not None: base+=(upper-lower)*rate/100
        schedules[row['id']]={'event_id':row['id'],'label':row['label'],'bands':bands,'source_ids':row['source_ids'].split(';'),'note':row['note'],'currency':'AUD nominal','measure':'Basic resident marginal-rate schedule; not total tax liability'}
    return {'schema_version':'1.0.0-review','as_of':AS_OF,'start_year':1960,'title':'Australian federal tax-policy timeline','scope':'Selected major federal changes, not an exhaustive annual tax-law or tax-rate census. Known future applications are shown separately.','source_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'categories':CATEGORIES,'stages':STAGES,'statuses':STATUSES,'sources':sources,'events':events,'rate_schedules':schedules,'coverage_notes':['The six 1960 starting positions are baselines, not six changes enacted that year.','1960–82 coverage is sparse. Early annual income-tax rate changes and wholesale sales-tax item schedules remain incomplete.','Nine basic resident schedules are supplied; missing years must not be filled forward as verified annual rates.','Routine excise indexation is represented by regime changes and selected steps, not every tariff notice. Additional intra-April 2026 fuel adjustments are not fully reconstructed.','Sources include legislation, official retrospectives, administrative guidance and original historical research. Some ATO material was available only in indexed excerpts, as marked.','Judgments and ATO guidance are interpretations, not new statutes. Announcements, passage, assent and application dates are distinct.','No complete company, superannuation, state payroll, land, stamp duty, carbon or resource-tax history is provided. FBT and imputation are included as adjacent remuneration/investment reforms.','Proposals are not current law. Summaries are for research review, not personal tax advice.'],'date_convention':'Only known precision is stored. Year-only markers are plotted at 1 July and month-only markers at the 15th solely for layout; these are not asserted event dates.','status_convention':'Status is assessed at the review date. Historical law event does not mean the provision is still operative. Proposed means no enactment was verified, not a prediction of passage.'}

def validate(data: dict) -> dict:
    E=data['events']; S=data['sources']; R=data['rate_schedules']; ids={e['id'] for e in E}
    require(len(ids)==len(E),'Duplicate event ID')
    require(len(E)>=100,'Unexpected loss of coverage')
    require(set(e['category'] for e in E)==set(CATEGORIES),'Missing tax category')
    require(len([e for e in E if e['date']=='1960' and e['stage']=='baseline'])==6,'Missing 1960 baseline')
    for s in S.values(): require(s['url'].startswith('https://'),'Non-HTTPS source URL')
    for e in E:
        require(e['category'] in CATEGORIES and e['stage'] in STAGES and e['status'] in STATUSES,f'Invalid coding: {e["id"]}')
        require(e['date_info']['earliest']>='1960-01-01','Event before scope')
        require(e['source_ids'] and all(s in S for s in e['source_ids']),'Unresolved event source')
        require(all(x in ids for x in e['related_event_ids']),'Broken related-event link')
        for k in ['announced','assent','effective','end']: date_info(e[k])
        require(not e['future_at_review'] or e['status'] in {'enacted_future','proposed'},'Future event mislabelled as historic')
        require(e['status']!='enacted_future' or e['future_at_review'],'Future-law status without future event')
        require(e['status']!='proposed' or e['assent'] is None,'Proposal has asserted assent')
    require(len(R)==9,'Rate-schedule coverage mismatch')
    for k,r in R.items():
        require(k in ids and all(s in S for s in r['source_ids']),'Unresolved rate reference')
        require(all(0<=b['rate_percent']<=100 for b in r['bands']),'Invalid rate')
        for b in r['bands']: require(basic_tax(r,b['lower'])==b['basic_tax_at_lower'],'Discontinuous schedule')
    lookup={e['id']:e for e in E}
    require(lookup['reform2026-act']['assent']=='2026-06-26','Act assent regression')
    require(lookup['trust2026-bill']['status']=='proposed','Trust Bill incorrectly enacted')
    require(lookup['trust-2028']['status']=='proposed','Future trust proposal incorrectly enacted')
    require(lookup['gearing-2027']['status']=='enacted_future','Core NG reform status regression')
    require(lookup['trust-bendel']['stage']=='judgment','Court judgment treated as statute')
    require(lookup['trust-s100a-guidance']['stage']=='guidance','Ruling treated as statute')
    require(lookup['cgt-discount']['effective']=='1999-09-21','CGT commencement regression')
    require(lookup['tobacco-awote']['date']=='2014-03-01','Tobacco wage-indexation date regression')
    require(basic_tax(R['income-2024'],45000)==4288,'2024 basic-scale regression')
    require(basic_tax(R['income-2026'],45000)==4020,'2026 basic-scale regression')
    require(basic_tax(R['income-2027'],45000)==3752,'2027 basic-scale regression')
    return {'passed':True,'as_of':AS_OF,'event_count':len(E),'source_count':len(S),'rate_schedule_count':len(R),'by_primary_category':dict(Counter(e['category'] for e in E)),'by_status':dict(Counter(e['status'] for e in E)),'by_date_precision':dict(Counter(e['date_info']['precision'] for e in E)),'future_event_count':sum(e['future_at_review'] for e in E),'baseline_count':sum(e['stage']=='baseline' for e in E),'source_sha256':data['source_sha256'],'limits':'Schema, dates, references, rate arithmetic and regression checks; not an independent legal or completeness audit.'}

def write_csv(path: Path, rows: list[dict], fields: list[str]) -> None:
    with path.open('w',newline='',encoding='utf-8') as f:
        writer=csv.DictWriter(f,fieldnames=fields); writer.writeheader()
        for row in rows:
            writer.writerow({k:json.dumps(row.get(k),ensure_ascii=False) if isinstance(row.get(k),(list,dict)) else row.get(k) for k in fields})

def write_outputs(data: dict,report: dict,output: Path) -> None:
    output.mkdir(parents=True,exist_ok=True)
    for name,payload in [('federal-tax-policy-timeline.json',data),('validation-report.json',report)]:
        (output/name).write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    write_csv(output/'tax-events.csv',data['events'],['id','date','category','stage','status','title','before','after','affected','announced','assent','effective','end','source_ids','note','future_at_review'])
    write_csv(output/'tax-sources.csv',list(data['sources'].values()),['id','title','publisher','kind','access','url','locator','retrieved'])
    rows=[{'event_id':r['event_id'],'label':r['label'],**b,'source_ids':r['source_ids'],'note':r['note']} for r in data['rate_schedules'].values() for b in r['bands']]
    write_csv(output/'income-tax-bands.csv',rows,['event_id','label','lower','upper','rate_percent','basic_tax_at_lower','source_ids','note'])
    template=(ROOT/'reviews/federal-tax-policy-timeline.template.html').read_text(encoding='utf-8')
    require(template.count('__TIMELINE_DATA__')==1,'Template placeholder mismatch')
    payload=json.dumps(data,ensure_ascii=False,separators=(',',':')).replace('<','\\u003c')
    (output/'federal-tax-policy-timeline.html').write_text(template.replace('__TIMELINE_DATA__',payload),encoding='utf-8')

def main() -> None:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--check-only',action='store_true')
    p.add_argument('--output-dir',type=Path,default=ROOT/'reviews/generated')
    args=p.parse_args();data=compile_data(ROOT/'data/federal-tax-policy-timeline.psv');report=validate(data)
    if not args.check_only: write_outputs(data,report,args.output_dir)
    print(json.dumps(report,indent=2))
if __name__=='__main__': main()
