"""Static blog localisation. Builds use checked-in catalogs; no network requests."""
from copy import deepcopy
from html import escape
from html.parser import HTMLParser
import json
from pathlib import Path
import re

LANGUAGES = {'en': 'English', 'zh-Hans': '简体中文', 'ar': 'العربية', 'vi': 'Tiếng Việt', 'es': 'Español'}
OG_LOCALES = {'en': 'en_AU', 'zh-Hans': 'zh_CN', 'ar': 'ar_AR', 'vi': 'vi_VN', 'es': 'es_ES'}
CATALOGS = Path(__file__).parent / 'translations'
PROTECTED = {'Learners Test Australia', 'Learners Test', 'Australia', 'BlueOrbit', 'Premium', 'Google Play',
             'NSW', 'VIC', 'QLD', 'SA', 'WA', 'TAS', 'ACT', 'NT', 'DKT', 'HPT', 'PrepL', 'myLs', 'L', 'P1', 'P2'}
NOTICES = {
 'zh-Hans': '此页面为自动翻译，尚未经专业译者审核。英语原文及各州官方资料可供核对；网站其他页面和官方链接可能为英语。',
 'ar': 'هذه ترجمة آلية لم يراجعها مترجم محترف. يمكنك الرجوع إلى النص الإنجليزي والمصادر الرسمية للتحقق. قد تكون صفحات الموقع الأخرى والروابط الرسمية باللغة الإنجليزية.',
 'vi': 'Đây là bản dịch tự động, chưa được biên dịch viên chuyên nghiệp rà soát. Hãy đối chiếu với bản gốc tiếng Anh và nguồn chính thức; các trang khác và liên kết chính thức có thể bằng tiếng Anh.',
 'es': 'Esta es una traducción automática, sin revisión de un traductor profesional. Consulta el original en inglés y las fuentes oficiales para verificar la información. Otras páginas y enlaces oficiales pueden estar en inglés.',
}
LABELS = {'en':'Read in', 'zh-Hans':'阅读语言', 'ar':'لغة القراءة', 'vi':'Ngôn ngữ', 'es':'Leer en'}


def normalise(value):
    return re.sub(r'\s+', ' ', value).strip()


def translatable(value):
    return bool(value and re.search(r'[A-Za-z]', value) and value not in PROTECTED
                and not re.fullmatch(r'[\w.+-]+@[\w.-]+', value)
                and not value.startswith(('https://', 'http://')))


class LocaliseHTML(HTMLParser):
    """Translate text and accessibility metadata while preserving HTML and URLs."""
    def __init__(self, translate, lang='en', blog_paths=()):
        super().__init__(convert_charrefs=False)
        self.translate, self.lang, self.blog_paths = translate, lang, set(blog_paths)
        self.output=[]
        self.skip=[]
        self.json_script=False

    def url(self, value):
        from sitelib import BASE
        if self.lang == 'en': return value
        for prefix in ('@/', BASE):
            if value.startswith(prefix):
                tail=value[len(prefix):]
                path, sep, fragment=tail.partition('#')
                source=path+'index.html' if path.endswith('/') else path
                if source in self.blog_paths:
                    path='blog/'+self.lang+'/'+path[len('blog/'):]
                    return prefix+path+(sep+fragment if sep else '')
        return value

    def handle_starttag(self, tag, attrs):
        attrs=dict(attrs)
        if tag == 'script':
            self.skip.append(tag)
            self.json_script=attrs.get('type') == 'application/ld+json'
        elif tag in ('style','svg'): self.skip.append(tag)
        for key in ('alt', 'aria-label', 'title'):
            if attrs.get(key): attrs[key]=self.translate(attrs[key])
        if tag == 'meta' and (attrs.get('name') in ('description','twitter:title','twitter:description','twitter:image:alt') or
                             attrs.get('property') in ('og:title','og:description','og:image:alt')):
            attrs['content']=self.translate(attrs['content'])
        if tag == 'meta' and attrs.get('property') == 'og:locale': attrs['content']=OG_LOCALES[self.lang]
        if tag == 'a' and 'href' in attrs:
            attrs['href']=self.url(attrs['href'])
            if self.lang != 'en' and attrs['href'].startswith('@/') and not attrs['href'].startswith('@/blog/'+self.lang+'/'):
                attrs['hreflang']='en'
        self.output.append('<'+tag+''.join(' '+k+('="'+escape(v,quote=True)+'"' if v is not None else '') for k,v in attrs.items())+'>')

    def handle_endtag(self,tag):
        if self.skip and self.skip[-1] == tag:
            self.skip.pop()
            if tag == 'script': self.json_script=False
        self.output.append('</'+tag+'>')

    def structured(self,obj,key=''):
        if isinstance(obj,dict): return {k:self.structured(v,k) for k,v in obj.items() if not (k=='wordCount' and self.lang!='en')}
        if isinstance(obj,list): return [self.structured(v,key) for v in obj]
        if isinstance(obj,str):
            if key == 'inLanguage': return self.lang if self.lang != 'en' else obj
            if key in ('name','headline','description','articleSection','keywords','caption'): return self.translate(obj)
            if key in ('url','@id','item'): return self.url(obj)
        return obj

    def handle_data(self,data):
        if self.json_script:
            self.output.append(json.dumps(self.structured(json.loads(data)),ensure_ascii=False,indent=1))
        elif self.skip: self.output.append(data)
        else: self.output.append(escape(self.translate(data),quote=False))

    def handle_entityref(self,name): self.output.append('&'+name+';')
    def handle_charref(self,name): self.output.append('&#'+name+';')
    def handle_decl(self,decl): self.output.append('<!'+decl+'>')
    def handle_comment(self,data): self.output.append('<!--'+data+'-->')


def transform(html, translate, lang='en', blog_paths=()):
    parser=LocaliseHTML(translate,lang,blog_paths)
    parser.feed(html)
    return ''.join(parser.output)


def translator(lang):
    catalog=json.loads((CATALOGS/(lang+'.json')).read_text(encoding='utf-8'))['strings']
    def translate(value):
        key=normalise(value)
        if not translatable(key): return value
        if key not in catalog: raise ValueError(f'Missing {lang} translation: {key[:160]}')
        return value[:len(value)-len(value.lstrip())]+catalog[key]+value[len(value.rstrip()):]
    return translate


def variants(pages):
    blogs=[p for p in pages if p.path.startswith('blog/')]
    extra=[]
    for page in blogs:
        page.alternates={lang:('blog/'+lang+'/'+page.path[5:] if lang!='en' else page.path) for lang in LANGUAGES}
        for lang in LANGUAGES:
            if lang=='en': continue
            clone=deepcopy(page)
            clone.path=page.alternates[lang]
            clone.language=lang
            clone.llms=False
            clone.llms_title=(page.llms_title or page.title)+' — '+LANGUAGES[lang]
            clone.llms_note=''
            extra.append(clone)
    return pages+extra


def finish_html(html,page):
    from sitelib import BASE, esc
    if not page.alternates: return html
    original_paths=[p for p in page.blog_paths]
    if page.language != 'en': html=transform(html,translator(page.language),page.language,original_paths)
    alts=[]; buttons=[]
    for lang,path in page.alternates.items():
        canonical=BASE+(path[:-10] if path.endswith('index.html') else path)
        alts.append(f'<link rel="alternate" hreflang="{lang}" href="{canonical}">')
        current=' aria-current="page"' if lang==page.language else ''
        buttons.append(f'<a href="@/{path}" lang="{lang}" hreflang="{lang}" dir="auto"{current}>{LANGUAGES[lang]}</a>')
    english=BASE+page.alternates['en'].replace('index.html','')
    alts.append(f'<link rel="alternate" hreflang="x-default" href="{english}">')
    html=html.replace('</head>','\n'.join(alts)+'\n</head>')
    bar=f'<div class="container language-tools"><nav class="language-switch" aria-label="{LABELS[page.language]}"><span>{LABELS[page.language]}</span>'+''.join(buttons)+'</nav>'
    if page.language!='en': bar+=f'<p class="translation-note">{esc(NOTICES[page.language])}</p>'
    bar+='</div>'
    return html.replace('<main id="main" tabindex="-1">','<main id="main" tabindex="-1">'+bar)
