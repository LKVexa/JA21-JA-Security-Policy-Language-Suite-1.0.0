#!/usr/bin/env python3
import csv,gzip,hashlib,json,re,sys
from collections import Counter
from pathlib import Path
LEVELS=['beginner', 'intermediate', 'advanced', 'expert', 'compiler', 'runtime', 'optimization', 'validation', 'certification', 'deployment']; EXPECTED={'positive': 400, 'negative': 150, 'boundary': 100, 'integration': 100, 'security': 75, 'performance': 50, 'determinism': 50, 'interoperability': 25, 'recovery': 25, 'certification': 25}
def sha(s): return hashlib.sha256(s.encode('utf-8')).hexdigest()
def balance(s):
    q=re.sub(r'"(?:\\.|[^"\\])*"','""',s); return q.count('{')-q.count('}')
def main():
    root=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path(__file__).resolve().parents[1]; errors=[]
    with gzip.open(root/'corpus/technical/JA21_JASEC_TECHNICAL_CORPUS_10000.jsonl.gz','rt',encoding='utf-8') as f: rec=[json.loads(x) for x in f if x.strip()]
    if len(rec)!=10000: errors.append('corpus count')
    if len({r['record_id'] for r in rec})!=10000: errors.append('unique IDs')
    if [r['sequence'] for r in rec]!=list(range(1,10001)): errors.append('sequence')
    for r in rec:
        if sha(r['source'])!=r['ast']['origin_hash']: errors.append('source hash '+r['record_id'])
        if not r.get('_suite_publication',{}).get('source_sha256_verified'): errors.append('publication hash '+r['record_id'])
    scripts=list((root/'scripts').rglob('*.jasec'))
    if len(scripts)!=1000: errors.append('script count')
    with (root/'catalogs/SCRIPT_CATALOG.csv').open(encoding='utf-8',newline='') as f: rows=list(csv.DictReader(f))
    if len(rows)!=1000: errors.append('catalog count')
    if Counter(r['validation_class'] for r in rows)!=Counter(EXPECTED): errors.append('class distribution')
    if Counter(r['level'] for r in rows)!=Counter({x:100 for x in LEVELS}): errors.append('level distribution')
    if len({r['feature'] for r in rows})!=32: errors.append('feature coverage')
    mp={r['record_id']:r for r in rec}
    for row in rows:
        p=root/row['file'];
        if not p.is_file(): errors.append('missing '+row['file']); continue
        src=p.read_text(encoding='utf-8')
        if src!=mp[row['record_id']]['source']: errors.append('source mismatch '+row['record_id'])
        if sha(src)!=row['source_sha256']: errors.append('script hash '+row['record_id'])
        for token in ('ja source','module ','use Security','policy ','principal ','resource ','emit mcrt'):
            if token not in src: errors.append('missing '+token+' '+row['record_id'])
        if balance(src)!=0: errors.append('brace '+row['record_id'])
    tb=(root/'textbook/JA21_JA_SECURITY_POLICY_LANGUAGE_TEXTBOOK.md').read_text(encoding='utf-8')
    ch=len(re.findall(r'^# Chapter \d+:',tb,flags=re.M))
    if ch!=22: errors.append('chapters '+str(ch))
    result={'suite':'JA21_JASEC_1.0.0','records':len(rec),'scripts':len(scripts),'catalog_rows':len(rows),'features':len({r['feature'] for r in rows}),'textbook_chapters':ch,'max_relative_path':max(len(p.relative_to(root).as_posix()) for p in root.rglob('*')),'errors':errors,'status':'pass' if not errors else 'fail'}
    print(json.dumps(result,indent=2)); return 0 if not errors else 1
if __name__=='__main__': raise SystemExit(main())
