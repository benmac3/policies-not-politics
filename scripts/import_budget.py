"""Extract Budget Paper 1 Table 11.4 from pdftotext -layout output.
Usage: python scripts/import_budget.py path/to/bp1_2026-27.pdf
"""
import hashlib,json,re,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def main():
    path=Path(sys.argv[1]);text=subprocess.check_output(['pdftotext','-layout',str(path),'-']).decode()
    start=text.index('Table 11.4: Australian Government general government sector net debt')
    end=text.index('Table 11.5:',start)
    rows=[]
    for m in re.finditer(r'^(\d{4}-\d{2})\s*(\(e\))?\s+([\d,.-]+)\s+([\d.-]+)\s+([\d,.-]+)\s+([\d.-]+)\s*$',text[start:end],re.M):
        year,est,*vals=m.groups()
        if int(year[:4])<2000:continue
        for name,val,unit in zip(['budget_net_debt','budget_net_debt_gdp','budget_net_interest','budget_net_interest_gdp'],vals,['AUD million','% GDP','AUD million','% GDP']):
            rows.append(dict(country='AUS',indicator=name,period=year,value=float(val.replace(',','')),unit=unit,source='budget26',status='Budget estimate' if est else 'Budget historical actual'))
    assert len(rows)==120, len(rows)
    (ROOT/'data/budget.json').write_text(json.dumps(rows,indent=2))
    (ROOT/'data/budget-provenance.json').write_text(json.dumps(dict(url='https://budget.gov.au/content/bp1/download/bp1_2026-27.pdf',sha256=hashlib.sha256(path.read_bytes()).hexdigest(),table='11.4',pages='432–433',retrieved='2026-09-10'),indent=2))
    print(len(rows),'fiscal observations extracted')
if __name__=='__main__':main()
