"""Fetch a dated WDI panel for the OECD membership directory. No interpolation."""
import gzip
import concurrent.futures
import hashlib
import json
import math
import urllib.request
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
METRICS = {
 'NY.GDP.PCAP.KD': ('Real GDP per person', 'constant 2015 US$'),
 'NY.GDP.PCAP.PP.KD': ('Real GDP per person, PPP', 'constant 2021 international $'),
 'NY.GDP.MKTP.KD.ZG': ('Real GDP growth', '% annual change'),
 'NY.GDP.PCAP.KD.ZG': ('Real GDP per person growth', '% annual change'),
 'SL.GDP.PCAP.EM.KD': ('Output per employed person, PPP', 'constant 2021 international $'),
 'FP.CPI.TOTL.ZG': ('Consumer price inflation', '% annual change'),
 'SL.UEM.TOTL.ZS': ('Unemployment, modelled ILO estimate', '% of labour force'),
 'SL.TLF.CACT.ZS': ('Labour force participation, modelled ILO estimate', '% of population aged 15+'),
 'NE.GDI.FTOT.ZS': ('Gross fixed capital formation', '% of GDP'),
 'GB.XPD.RSDV.GD.ZS': ('Research and development expenditure', '% of GDP'),
 'SI.POV.GINI': ('Income or consumption Gini', 'index 0–100'),
 'GC.DOD.TOTL.GD.ZS': ('Central government debt', '% of GDP'),
 'GC.XPN.TOTL.GD.ZS': ('Government expense, GFS reporting scope', '% of GDP'),
 'GC.TAX.TOTL.GD.ZS': ('Tax revenue excluding most social contributions', '% of GDP'),
 'GC.XPN.INTP.RV.ZS': ('Interest payments', '% of revenue'),
 'FS.AST.PRVT.GD.ZS': ('Domestic credit to private sector', '% of GDP'),
 'EG.IMP.CONS.ZS': ('Net energy imports', '% of energy use'),
 'EG.FEC.RNEW.ZS': ('Renewable energy consumption', '% of final energy consumption'),
 'SP.POP.TOTL': ('Population', 'people'),
 'SP.POP.65UP.TO.ZS': ('Population aged 65+', '% of population'),
}

def fetch(code, countries):
    url = ('https://api.worldbank.org/v2/country/' + ';'.join(countries) + '/indicator/' + code +
           '?format=json&date=2000:2025&per_page=20000')
    raw = urllib.request.urlopen(url, timeout=60).read()
    doc = json.loads(raw)
    if not isinstance(doc, list) or len(doc) != 2 or doc[0]['pages'] != 1:
        raise ValueError('Incomplete or invalid response: ' + code)
    meta_url = 'https://api.worldbank.org/v2/indicator/' + code + '?format=json'
    meta_raw = urllib.request.urlopen(meta_url, timeout=60).read()
    meta = json.loads(meta_raw)[1][0]
    rows = []
    for r in doc[1]:
        if r['value'] is None:
            continue
        assert r['countryiso3code'] in countries and math.isfinite(r['value'])
        rows.append(dict(country=r['countryiso3code'], indicator=code, period=r['date'],
                         value=r['value'], unit=METRICS[code][1], source='wdi_'+code,
                         status='published observation / estimate; see metadata'))
    (ROOT/'data/raw'/('wdi_'+code+'.json.gz')).write_bytes(gzip.compress(raw,mtime=0))
    (ROOT/'data/raw'/('metadata_'+code+'.json.gz')).write_bytes(gzip.compress(meta_raw,mtime=0))
    return rows, dict(id='wdi_'+code, agency='World Bank WDI; '+meta.get('sourceOrganization',''),
                     title=METRICS[code][0], url=url,
                     note=meta.get('sourceNote',''), retrieved=datetime.now(timezone.utc).date().isoformat()), dict(
                     code=code, name=METRICS[code][0], unit=METRICS[code][1], url=url,
                     metadata_url=meta_url, sha256=hashlib.sha256(raw).hexdigest(),
                     lastupdated=doc[0].get('lastupdated'), observations=len(rows),
                     countries=len({r['country'] for r in rows}))

def main():
    countries=[c['code'] for c in json.loads((ROOT/'data/countries.json').read_text())]
    (ROOT/'data/raw').mkdir(exist_ok=True)
    results=[]
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
        pending={pool.submit(fetch, code, countries):code for code in METRICS}
        for future in concurrent.futures.as_completed(pending):
            result=future.result() # Fail rather than silently publish partial retrieval.
            results.append(result)
            print(pending[future], len(result[0]), 'observations', flush=True)
    rows=[r for result in results for r in result[0]]
    rows.sort(key=lambda r:(r['indicator'],r['country'],r['period']))
    (ROOT/'data/panel.json').write_text(json.dumps(rows,indent=2))
    (ROOT/'data/metrics.json').write_text(json.dumps(sorted([r[2] for r in results],key=lambda r:r['code']),indent=2))
    sources=json.loads((ROOT/'data/sources.json').read_text())
    sources=[s for s in sources if not s['id'].startswith('wdi_')]+[r[1] for r in results]
    (ROOT/'data/sources.json').write_text(json.dumps(sources,indent=2))
    print('TOTAL',len(rows),'countries',len({r['country'] for r in rows}))

if __name__=='__main__': main()
