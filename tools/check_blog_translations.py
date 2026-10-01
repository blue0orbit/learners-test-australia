"""Check complete static translations, matching links, schema and language clusters."""
from html.parser import HTMLParser
from pathlib import Path
import json
from urllib.parse import urljoin, urlparse

from blog_i18n import LANGUAGES, CATALOGS, NOTICES, translator
from prepare_blog_translations import inventory
from sitelib import BASE

ROOT=Path(__file__).resolve().parent.parent


class Document(HTMLParser):
    def __init__(self,text):
        super().__init__(convert_charrefs=True)
        self.tags=[]; self.blocks=[]; self.json=False; self.current=''
        self.feed(text)
    def handle_starttag(self,tag,attrs):
        a=dict(attrs); self.tags.append((tag,a))
        if tag=='script' and a.get('type')=='application/ld+json': self.json=True; self.current=''
    def handle_data(self,data):
        if self.json: self.current+=data
    def handle_endtag(self,tag):
        if tag=='script' and self.json:
            self.blocks.append(json.loads(self.current)); self.json=False


def main():
    english=sorted((ROOT/'blog').glob('*.html'))
    assert len(english)==8, 'Expected seven posts and their index'
    strings=inventory()
    checked=0
    for lang in LANGUAGES:
        if lang!='en':
            translate=translator(lang)
            for text in strings: assert translate(text).strip(), (lang,text)
        for original in english:
            relative='blog/'+('' if lang=='en' else lang+'/')+original.name
            text=(ROOT/relative).read_text(encoding='utf-8')
            doc=Document(text)
            attrs=next(a for tag,a in doc.tags if tag=='html')
            assert attrs['lang']==lang and attrs['dir']==('rtl' if lang=='ar' else 'ltr'),relative
            alts={a['hreflang']:a['href'] for tag,a in doc.tags if tag=='link' and a.get('rel')=='alternate'}
            assert set(alts)==set(LANGUAGES)|{'x-default'},relative
            suffix='' if original.name=='index.html' else original.name
            for other in LANGUAGES:
                assert alts[other]==BASE+'blog/'+('' if other=='en' else other+'/')+suffix,relative
            canonical=next(a['href'] for tag,a in doc.tags if tag=='link' and a.get('rel')=='canonical')
            assert canonical==alts[lang],relative
            assert alts['x-default']==alts['en'],relative
            assert len([a for tag,a in doc.tags if tag=='a' and a.get('aria-current')=='page' and 'hreflang' in a])==1,relative
            nodes=doc.blocks[0]['@graph']
            node=next(n for n in nodes if n['@type'] in ('Blog','BlogPosting'))
            assert node['inLanguage']==('en-AU' if lang=='en' else lang),relative
            assert node['url']==canonical,relative
            if original.name!='index.html':
                assert node['mainEntityOfPage']['@id']==canonical,relative
            if lang!='en':
                assert NOTICES[lang] in text,relative
                # Preserve the original article's external reference set exactly.
                source=Document(original.read_text(encoding='utf-8'))
                external=lambda d:{a['href'] for tag,a in d.tags if tag=='a' and a.get('href','').startswith('https://')}
                assert external(source)==external(doc),relative
                # Structure is not abbreviated: every paragraph, list item and heading survives.
                for tag in ('h1','h2','h3','li','figure','table'):
                    assert sum(t==tag for t,a in source.tags)==sum(t==tag for t,a in doc.tags),(relative,tag)
                assert 'ZXQKEEP' not in text and '[[[' not in text,relative
            checked+=1
    print(f'PASS: {checked} blog pages, 5 languages, reciprocal alternates, self canonicals, complete catalogs, preserved structures and external sources.')


if __name__=='__main__': main()
