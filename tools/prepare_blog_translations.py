"""Explicit maintenance command: translate public blog text and save static catalogs.

Uses Google's public translation endpoint for automatic translations. Never runs during
the website build or in a visitor's browser. Existing catalog entries are reused.
"""
from concurrent.futures import ThreadPoolExecutor
from datetime import date
import json
from pathlib import Path
import re
import time
import urllib.parse
import urllib.request

from blog_i18n import CATALOGS, LANGUAGES, normalise, translatable, transform
from build import all_pages
from sitelib import render


def inventory():
    strings={}
    def collect(value):
        key=normalise(value)
        if translatable(key): strings[key]=None
        return value
    for page in all_pages():
        if page.language!='en' or not page.path.startswith('blog/'): continue
        page.alternates={}
        transform(render(page),collect)
    return list(strings)


KEEP = ['Learners Test Australia', 'BlueOrbit', 'Google Play', 'Service NSW', 'VicRoads', 'Transport Victoria',
        'PrepL', 'myLs', 'Plates Plus', 'NSW', 'VIC', 'QLD', 'TAS', 'ACT', 'NT', 'WA', 'SA', 'DKT', 'HPT', 'P1', 'P2', 'Premium']


def request(text,lang):
    params=urllib.parse.urlencode({'client':'gtx','sl':'en','tl':'zh-CN' if lang=='zh-Hans' else lang,'dt':'t','q':text})
    url='https://translate.googleapis.com/translate_a/single?'+params
    for attempt in range(4):
        try:
            req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
            with urllib.request.urlopen(req,timeout=45) as response: data=json.load(response)
            return ''.join(part[0] for part in data[0] if part[0])
        except Exception:
            if attempt==3: raise
            time.sleep(2**attempt)


def translate_batch(batch,lang):
    text='\n'.join(f'[[[{i}]]]\n{s}' for i,s in enumerate(batch))
    used={}
    for i,term in enumerate(KEEP):
        pattern=r'(?<!\w)'+re.escape(term)+r'(?!\w)'
        if re.search(pattern,text):
            token=f'ZXQKEEP{i}QXZ'
            text=re.sub(pattern,token,text)
            used[token]=term
    result=request(text,lang)
    for token,term in used.items(): result=result.replace(token,term)
    matches=list(re.finditer(r'\[\[\[\s*(\d+)\s*\]\]\]',result))
    if len(matches)!=len(batch) or [int(m[1]) for m in matches]!=list(range(len(batch))):
        if len(batch)>1:
            mid=len(batch)//2
            return translate_batch(batch[:mid],lang)+translate_batch(batch[mid:],lang)
        raise ValueError(f'{lang}: translation markers changed')
    out=[result[m.end():matches[i+1].start() if i+1<len(matches) else len(result)].strip() for i,m in enumerate(matches)]
    if any(not s or 'ZXQKEEP' in s for s in out): raise ValueError(f'{lang}: empty result or damaged protected term')
    return out


def run_language(lang,strings):
    dest=CATALOGS/(lang+'.json')
    data=json.loads(dest.read_text(encoding='utf-8')) if dest.exists() else {'language':lang,'method':'automatic translation; editorial spot checks only','strings':{}}
    missing=[s for s in strings if s not in data['strings']]
    batches=[]; batch=[]; size=0
    for s in missing:
        if batch and size+len(s)>3000: batches.append(batch); batch=[]; size=0
        batch.append(s); size+=len(s)+20
    if batch: batches.append(batch)
    for i,batch in enumerate(batches):
        values=translate_batch(batch,lang)
        data['strings'].update(zip(batch,values))
        data['updated']='2026-10-01'
        dest.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        print(f'{lang}: batch {i+1}/{len(batches)}; {len(data["strings"])} strings saved',flush=True)
        time.sleep(.15)
    return lang,len(data['strings'])


if __name__=='__main__':
    CATALOGS.mkdir(exist_ok=True)
    strings=inventory()
    print(f'{len(strings)} unique strings; {sum(map(len,strings))} source characters',flush=True)
    with ThreadPoolExecutor(max_workers=4) as pool:
        jobs=[pool.submit(run_language,lang,strings) for lang in LANGUAGES if lang!='en']
        for job in jobs: print(job.result(),flush=True)
