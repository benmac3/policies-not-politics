"""Extract the current roster and occupation records from Parliament's public API.

Occupational categories are official. Sector hints are conservative, provisional
project labels; a job title alone does not determine employer ownership.
"""
import gzip
import json, re, urllib.parse, urllib.request, hashlib
from datetime import datetime, timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
BASE='https://handbookapi.aph.gov.au/api/'

def sector(role):
    t=role.lower()
    if re.search(r'trade union|union organis|union official|\bunion\b',t): return 'Union / worker organisation'
    if re.search(r'party official|electorate officer|political advis|policy advis.*premier|advis.*minister|research officer.*minister|ministerial|chief of staff.*minister|electorate advis',t): return 'Political employment'
    if re.search(r'public servant|public service|australian (army|navy|air force)|police officer',t): return 'Public service / defence (explicit role)'
    if re.search(r'self.employed|small business owner|business owner|sole trader',t): return 'Private enterprise (explicit role)'
    return 'Employer sector not determined'

def main():
    day=datetime.now(timezone.utc).date().isoformat()
    query={'$select':'PHID,DisplayName,MPorSenator,StateAbbrev,Electorate,Party,ServiceHistory_Start,ServiceHistory_End,Occupations,SecondaryOccupations,RepresentedParliaments','$count':'true'}
    urls={'individuals':BASE+'individuals?'+urllib.parse.urlencode(query),
          'occupations':BASE+'StatisticalInformation/PreviousOccupations?parliamentariantype=',
          'prior':BASE+'StatisticalInformation/PriorService?parliamentariantype='}
    docs={};manifest=[]
    for name,url in urls.items():
        raw=urllib.request.urlopen(url,timeout=60).read();docs[name]=json.loads(raw)
        (ROOT/'data/raw'/('aph_'+name+'.json.gz')).write_bytes(gzip.compress(raw,mtime=0))
        manifest.append(dict(name=name,url=url,retrieved=day,sha256=hashlib.sha256(raw).hexdigest()))
    d=docs['individuals'];assert '@odata.nextLink' not in d and len(d['value'])==d['@odata.count']
    # API substitutes retrieval date for ongoing service; newly added records may have empty end dates.
    current=[r for r in d['value'] if 48 in r['RepresentedParliaments'] and (not r['ServiceHistory_End'] or r['ServiceHistory_End']>=day)]
    records=[]
    for r in current:
        records.append(dict(id=r['PHID'],name=r['DisplayName'],chamber='Member' if r['Electorate'] else 'Senator', chamber_history=' / '.join(r['MPorSenator']),
                            party=r['Party'],state=r['StateAbbrev'],electorate=r['Electorate'],
                            first_service=r['ServiceHistory_Start'],source= 'https://handbook.aph.gov.au/parliamentarians/'+r['PHID'],
                            occupations=r['Occupations'],sector_hints=[sector(x) for x in r['Occupations']],
                            record_status='Official occupation text; sector hints provisional; dates not complete'))
    total=next(r['TotalNumberOfMembers'] for r in docs['prior'] if r['Party']=='Total')
    assert len(records)==total, ('Roster and official aggregate disagree',len(records),total)
    out={'retrieved':day,'roster':records,'occupations':docs['occupations'],'prior':docs['prior'],'manifest':manifest}
    (ROOT/'data/parliament.json').write_text(json.dumps(out,indent=2))
    print(len(records),'parliamentarians;',sum(len(r['occupations']) for r in records),'occupation records')

if __name__=='__main__': main()
