"""Rebuild static data and downloadable source pack using only the standard library."""
import csv
import json
import shutil
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    raw_files=sorted((ROOT/'data/raw').glob('*.json.gz'))
    if raw_files:
        with zipfile.ZipFile(ROOT/'data/raw-snapshots.zip','w',compression=zipfile.ZIP_STORED) as z:
            for p in raw_files:
                info=zipfile.ZipInfo(p.name,date_time=(2026,9,10,0,0,0))
                z.writestr(info,p.read_bytes())
    bundle = {}
    for name in ('sources', 'observations', 'claims', 'countries', 'panel', 'metrics', 'budget', 'extensions'):
        values = json.loads((ROOT / 'data' / f'{name}.json').read_text())
        bundle[name] = values
        with (ROOT / 'data' / f'{name}.csv').open('w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=list(values[0]))
            writer.writeheader()
            writer.writerows(values)
    bundle['parliament'] = json.loads((ROOT/'data/parliament.json').read_text())
    with (ROOT/'data/parliament.csv').open('w', newline='') as f:
        writer=csv.writer(f)
        writer.writerow(['id','name','chamber','party','state','electorate','occupation','sector_hint','source'])
        for r in bundle['parliament']['roster']:
            for role,hint in zip(r['occupations'] or ['Not recorded'],r['sector_hints'] or ['Unknown']):
                writer.writerow([r['id'],r['name'],r['chamber'],r['party'],r['state'],r['electorate'],role,hint,r['source']])
    (ROOT / 'dist/data.js').write_text('const DATA = ' + json.dumps(bundle, ensure_ascii=False, separators=(',',':')) + ';\n')
    for folder in ('data', 'docs'):
        destination = ROOT / 'dist' / folder
        destination.mkdir(exist_ok=True)
        for item in (ROOT / folder).iterdir():
            if item.is_file():
                shutil.copyfile(item, destination / item.name)
    # Deterministic ZIP. Includes original code/data/docs, excludes credentials,
    # service identity, Git internals, raw transcript and the ZIP itself.
    zip_path = ROOT / 'dist/source-pack.zip'
    paths = []
    for folder in ('data', 'docs', 'scripts', '.github'):
        paths.extend(p for p in (ROOT / folder).rglob('*') if p.is_file()
                     and '__pycache__' not in p.parts and 'raw' not in p.parts
                     and 'staging' not in p.parts)
    paths.extend(ROOT / name for name in ('README.md', 'CONTRIBUTING.md', 'LICENSE', '.gitignore'))
    paths.extend(ROOT / 'dist' / name for name in ('index.html', 'style.css', 'app.js', 'data.js'))
    with zipfile.ZipFile(zip_path, 'w', compression=zipfile.ZIP_DEFLATED) as z:
        for p in sorted(paths):
            info = zipfile.ZipInfo(str(p.relative_to(ROOT)), date_time=(2026, 9, 8, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(info, p.read_bytes())
    print(f'Built {len(bundle["observations"])} observations; source pack {zip_path.stat().st_size:,} bytes')


if __name__ == '__main__':
    main()
