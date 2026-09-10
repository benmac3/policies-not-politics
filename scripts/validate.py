"""Validate data provenance, coherence and deployed local assets."""
import csv
import json
import math
import re
import zipfile
import gzip
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
load = lambda name: json.loads((ROOT / 'data' / f'{name}.json').read_text())
sources, obs, countries, claims = (load(n) for n in ('sources', 'observations', 'countries', 'claims'))
source_ids = {s['id'] for s in sources}
assert len(source_ids) == len(sources)
assert len(countries) == 38 and len({c['code'] for c in countries}) == 38
seen = set()
for r in obs:
    assert r['source'] in source_ids and math.isfinite(r['value'])
    key = (r['country'], r['indicator'], r['period'], r['source'])
    assert key not in seen, key
    seen.add(key)
    if r['indicator'] == 'ndis_old_projection':
        assert r['status'] == 'superseded projection'
assert len({c['id'] for c in claims}) == len(claims)
assert all(not c['source'] or c['source'] in source_ids for c in claims)
for name in ('sources', 'observations', 'claims', 'countries'):
    with (ROOT / 'dist/data' / f'{name}.csv').open() as f:
        assert len(list(csv.DictReader(f))) == len(load(name))
for name in ('index.html', 'app.js'):
    text = (ROOT / 'dist' / name).read_text()
    for link in re.findall(r'(?:href|src)="([^"$]+)"', text):
        if link.startswith(('http', '#', '${')):
            continue
        assert (ROOT / 'dist' / link.split('?')[0]).is_file(), f'Missing local asset: {link}'
assert (ROOT / 'dist/data.js').stat().st_size > 1000
for name in ('panel','budget','extensions'):
    rows=load(name)
    assert rows and all(r['source'] in source_ids and math.isfinite(r['value']) for r in rows)
panel=load('panel')
assert len({r['country'] for r in panel})==38
assert len({(r['country'],r['indicator'],r['period']) for r in panel})==len(panel)
assert all(2000<=int(r['period'])<=2025 for r in panel)
parliament=load('parliament')
assert len({r['id'] for r in parliament['roster']})==226
assert sum(len(r['occupations']) for r in parliament['roster'])==910
assert sum(r['chamber']=='Member' for r in parliament['roster'])==150
assert sum(r['chamber']=='Senator' for r in parliament['roster'])==76
snapshot_archive=zipfile.ZipFile(ROOT/'data/raw-snapshots.zip')
for metric in load('metrics'):
    raw=gzip.decompress(snapshot_archive.read('wdi_'+metric['code']+'.json.gz'))
    assert hashlib.sha256(raw).hexdigest()==metric['sha256']
    assert sum(r['value'] is not None for r in json.loads(raw)[1])==metric['observations']
for item in parliament['manifest']:
    raw=gzip.decompress(snapshot_archive.read('aph_'+item['name']+'.json.gz'))
    assert hashlib.sha256(raw).hexdigest()==item['sha256']
assert sum(r['value'] for r in load('extensions') if r['indicator']=='ndis_payment_category')==51451
with zipfile.ZipFile(ROOT / 'dist/source-pack.zip') as z:
    assert z.testzip() is None
    assert not any(n.startswith(('.git/', '.openai/')) or n.endswith('.rtf') for n in z.namelist())
    assert 'scripts/build.py' in z.namelist()
print('PASS: provenance, uniqueness, coverage, projection labels, CSVs, local links and source archive')
