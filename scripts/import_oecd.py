"""Candidate OECD CSV adapter. Live download was blocked here; no automatic promotion."""
import argparse
import csv
import hashlib
import io
import json
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://sdmx.oecd.org/public/rest/v1/data/OECD.SDD.TPS,DSD_PDB@DF_PDB,2.0/'
# Key observed in OECD Data Explorer; validate against the live structure before use.
KEY = '.A.GDPHRS._T.USD_PPP_H.LR.N..'


def parse_csv(raw):
    text = raw.decode('utf-8-sig')
    reader = csv.DictReader(io.StringIO(text))
    required = {'REF_AREA', 'TIME_PERIOD', 'OBS_VALUE', 'FREQ', 'MEASURE', 'UNIT_MEASURE'}
    missing = required - set(reader.fieldnames or ())
    if missing:
        raise ValueError(f'Not the expected OECD CSV schema; missing {sorted(missing)}')
    members = {x['code'] for x in json.loads((ROOT / 'data/countries.json').read_text())}
    rows = []
    seen = set()
    for row in reader:
        if row['REF_AREA'] not in members:
            continue
        if row['FREQ'] != 'A' or row['MEASURE'] != 'GDPHRS' or row['UNIT_MEASURE'] != 'USD_PPP_H':
            raise ValueError('Unexpected measure, frequency or unit; do not combine unlike series')
        if row.get('ACTIVITY', '_T') != '_T':
            raise ValueError('Expected total-economy activity')
        value = row['OBS_VALUE'].strip()
        if value in ('', '..'):
            continue
        number = float(value)
        if not (0 < number < 10000):
            raise ValueError('Non-finite or implausible productivity level')
        key = (row['REF_AREA'], row['TIME_PERIOD'])
        if key in seen:
            raise ValueError('Duplicate country-year: select one price, adjustment and reference-base series')
        seen.add(key)
        rows.append({'country': key[0], 'indicator': 'productivity_level', 'period': key[1],
                     'value': number, 'unit': 'USD PPP/hour; price and base year require review',
                     'source': 'oecd_api', 'status': 'staging; not approved', 'source_dimensions': row})
    if not rows:
        raise ValueError('No observations; do not publish an empty import as successful')
    return rows


def main():
    p = argparse.ArgumentParser(description=__doc__)
    group = p.add_mutually_exclusive_group(required=True)
    group.add_argument('--download', action='store_true')
    group.add_argument('--input', type=Path)
    p.add_argument('--start', type=int, default=2000)
    p.add_argument('--end', type=int, default=2025)
    args = p.parse_args()
    if args.start > args.end:
        p.error('start must not be after end')
    url = BASE + KEY + '?' + urllib.parse.urlencode({'startPeriod': args.start, 'endPeriod': args.end})
    if args.download:
        request = urllib.request.Request(url, headers={'Accept': 'csvfile'})
        with urllib.request.urlopen(request, timeout=60) as response:
            raw = response.read()
    else:
        raw = args.input.read_bytes()
    rows = parse_csv(raw)
    timestamp = datetime.now(timezone.utc).isoformat()
    digest = hashlib.sha256(raw).hexdigest()
    for folder in ('raw', 'staging'):
        (ROOT / 'data' / folder).mkdir(exist_ok=True)
    (ROOT / 'data/raw' / f'oecd-{digest[:12]}.csv').write_bytes(raw)
    (ROOT / 'data/staging/oecd.json').write_text(json.dumps(rows, indent=2))
    (ROOT / 'data/staging/provenance.json').write_text(json.dumps({
        'retrieved': timestamp, 'requested_url': url if args.download else None,
        'input_filename': args.input.name if args.input else None, 'sha256': digest,
        'rows': len(rows), 'countries': len({r['country'] for r in rows}),
        'review_required': ['price basis', 'reference year', 'unit multiplier', 'method breaks',
                            'provisional flags', 'coverage', 'source licence']}, indent=2))
    print(f'{len(rows)} rows staged for review; approved observations unchanged')


if __name__ == '__main__':
    main()
