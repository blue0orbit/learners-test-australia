"""Translated versions of the website: Simplified Chinese, Arabic, Vietnamese and Spanish (the app's languages).

How it works
  The English pages are the source. Each page in PAGES is split into segments: runs of text with their inline markup
  (a paragraph, a list item, a heading, a table cell...), a few attribute values (alt, aria-label, title) and the
  page's title, description, image alt and breadcrumb names. Inside a run, inline tags become numbered placeholders,
  <t1>...</t1> for elements and <x2/> for things that stay exactly as they are (icons, images, line breaks, names
  marked translate="no"), so translators only see text. Translations live in tools/i18n/LANG.json, keyed by a hash of
  the English segment. When the English changes, its translation goes missing again, and a page is built in a language
  only when every one of its segments is translated: pages are never half translated.

  Translated pages live in /zh/, /ar/, /vi/ and /es/ with the English file names. Each one is marked for readers in
  Australia (hreflang zh-Hans-AU, ar-AU, vi-AU, es-AU), English is the x-default, every version lists all the others,
  links between translated pages stay in the same language, and guides and legal pages stay in English.

Commands (from the repo root)
  python tools/i18n.py extract                          write tools/i18n/_source.json (every segment, in page order)
  python tools/i18n.py todo LANG OUT.json [core|states] the segments LANG still needs, as a file to translate
  python tools/i18n.py validate LANG PART.json          check a translated file (the "t" fields) without saving it
  python tools/i18n.py merge LANG PART.json [...]       check translated files and add them to tools/i18n/LANG.json
  python tools/i18n.py check [LANG]                     coverage per page, and errors in saved translations
  Translator guide: tools/i18n/TRANSLATING.md
"""
from __future__ import annotations

import hashlib
import html
import json
import re
import sys
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from sitelib import (  # noqa: E402
    APP_NAME, BASE, DEVELOPER, EMAIL, LOCALES, SITE_ID, SITE_NAME, STATES, Page, breadcrumb_ld, mobile_application,
    organization, page_html, render, strip_tags,
)

HERE = Path(__file__).resolve().parent
I18N = HERE / "i18n"
LANGS = [c for c in LOCALES if c != "en"]
CORE_PAGES = ["index.html", "features.html", "states.html", "faq.html", "about.html", "contact.html", "download.html"]
STATE_PAGES = [p for _, _, p in STATES]
PAGES = CORE_PAGES + STATE_PAGES

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}
INLINE = {"a", "abbr", "b", "bdi", "bdo", "br", "button", "cite", "code", "em", "i", "img", "kbd", "mark", "q", "s",
          "small", "span", "strong", "sub", "sup", "svg", "time", "u", "var", "wbr"}
OPAQUE = {"svg", "img", "br", "wbr", "input"}
SKIP = {"script", "style", "svg", "template"}
ATTR_RE = re.compile(r'(\s(?:alt|aria-label|title|placeholder)=")([^"]*)(")')
PH_RE = re.compile(r"</?t\d+>|<x\d+/>")
FAQ_RE = re.compile(r'<h3 class="faq-q">(.*?)</h3></summary><div class="faq-a">(.*?)</div></details>', re.S)
CODES = re.compile(r"\b(NSW|VIC|QLD|SA|WA|TAS|ACT|NT|DKT|HPT|PrepL|myLs)\b")
NO_TRANSLATE = {SITE_NAME, APP_NAME, DEVELOPER, EMAIL}


# ── HTML tree with source offsets ─────────────────────────────────────────────────────────────
class Node:
    __slots__ = ("tag", "attrs", "start", "open_end", "close_start", "end", "children")

    def __init__(self, tag: str, attrs: dict, start: int, open_end: int):
        self.tag, self.attrs, self.start, self.open_end = tag, attrs, start, open_end
        self.close_start = self.end = open_end
        self.children: list = []


class Text:
    __slots__ = ("start", "end", "comment")

    def __init__(self, start: int, end: int, comment: bool = False):
        self.start, self.end, self.comment = start, end, comment


class _Builder(HTMLParser):
    def __init__(self, src: str):
        super().__init__(convert_charrefs=False)
        self.src = src
        self.lines = [0] + [m.end() for m in re.finditer("\n", src)]
        self.root = Node("#root", {}, 0, 0)
        self.root.close_start = self.root.end = len(src)
        self.stack = [self.root]

    def _off(self) -> int:
        line, col = self.getpos()
        return self.lines[line - 1] + col

    def _add(self, n) -> None:
        self.stack[-1].children.append(n)

    def handle_starttag(self, tag, attrs):
        start = self._off()
        n = Node(tag, {k: (v or "") for k, v in attrs}, start, start + len(self.get_starttag_text()))
        self._add(n)
        if tag not in VOID:
            self.stack.append(n)

    def handle_startendtag(self, tag, attrs):
        start = self._off()
        self._add(Node(tag, {k: (v or "") for k, v in attrs}, start, start + len(self.get_starttag_text())))

    def handle_endtag(self, tag):
        start = self._off()
        end = self.src.index(">", start) + 1
        for i in range(len(self.stack) - 1, 0, -1):
            if self.stack[i].tag == tag:
                n = self.stack[i]
                n.close_start, n.end = start, end
                del self.stack[i:]
                return

    def handle_data(self, data):
        start = self._off()
        self._add(Text(start, start + len(data)))

    def handle_entityref(self, name):
        start = self._off()
        self._add(Text(start, self.src.index(";", start) + 1))

    handle_charref = handle_entityref

    def handle_comment(self, data):
        start = self._off()
        self._add(Text(start, self.src.index("-->", start) + 3, comment=True))


def parse(src: str) -> Node:
    b = _Builder(src)
    b.feed(src)
    b.close()
    return b.root


def _frozen(n: Node) -> bool:
    """Elements kept exactly as they are: translate="no", or text in another language (a lang attribute)."""
    return n.attrs.get("translate") == "no" or "lang" in n.attrs


def _opaque(n: Node) -> bool:
    return n.tag in OPAQUE or _frozen(n)


def _inline(n) -> bool:
    if isinstance(n, Text):
        return True
    if n.tag in OPAQUE or (n.tag in INLINE and _frozen(n)):
        return True
    return n.tag in INLINE and all(_inline(c) for c in n.children)


def _runs(node: Node):
    """Yield the translatable runs under node as lists of sibling nodes."""
    if node.tag in SKIP or (node.tag != "#root" and _frozen(node)):
        return
    cur: list = []
    for ch in node.children:
        if _inline(ch):
            cur.append(ch)
        else:
            yield cur
            cur = []
            yield from _runs(ch)
    yield cur


def _encode(nodes: list, src: str) -> tuple[str, list]:
    parts: list[str] = []
    tags: list[tuple[str, str | None]] = []

    def enc(n) -> None:
        if isinstance(n, Text):
            if n.comment:
                parts.append(f"<x{len(tags)}/>")
                tags.append((src[n.start:n.end], None))
            else:
                parts.append(src[n.start:n.end])
        elif _opaque(n) or n.tag in VOID:
            parts.append(f"<x{len(tags)}/>")
            tags.append((src[n.start:n.end], None))
        else:
            k = len(tags)
            tags.append((src[n.start:n.open_end], src[n.close_start:n.end]))
            parts.append(f"<t{k}>")
            for c in n.children:
                enc(c)
            parts.append(f"</t{k}>")

    for n in nodes:
        enc(n)
    return re.sub(r"\s+", " ", "".join(parts)).strip(), tags


def _decode(t: str, tags: list) -> str:
    t = re.sub(r"<x(\d+)/>", lambda m: tags[int(m.group(1))][0], t)
    t = re.sub(r"<t(\d+)>", lambda m: tags[int(m.group(1))][0], t)
    return re.sub(r"</t(\d+)>", lambda m: tags[int(m.group(1))][1], t)


def plain(text: str) -> str:
    """Text without placeholders or tags, entities decoded."""
    return html.unescape(re.sub(r"<[^>]+>", "", PH_RE.sub("", text))).strip()


def _skip(text: str) -> bool:
    p = re.sub(r"\s+", " ", plain(text))
    return (not re.search(r"[A-Za-z]", p) or p in NO_TRANSLATE or bool(re.fullmatch(r"[A-Z]{2,4}", p))
            or bool(re.fullmatch(r"\S+@\S+\.\S+", p)) or bool(re.fullmatch(r"https?://\S+", p)))


def key(kind: str, text: str) -> str:
    return hashlib.sha1(f"{kind}\0{text}".encode("utf-8")).hexdigest()[:16]


# ── Segments of a page ───────────────────────────────────────────────────────────────────────
def segments(page: Page) -> list[dict]:
    """Every translatable segment of an English page, in page order: {key, kind, src, note}."""
    out: list[dict] = []
    seen: set[str] = set()

    def add(kind: str, text: str, note: str = "") -> None:
        k = key("run" if kind == "run" else "txt", text)
        if k not in seen:
            seen.add(k)
            out.append({"key": k, "kind": kind, "src": text, "note": note})

    add("title", page.title, "page title: in search results and the browser tab")
    add("description", page.description, "meta description: the snippet under the title in search results")
    add("image_alt", page.image_alt, "alt text of the share image")
    for name, _ in page.crumbs:
        add("crumb", name, "breadcrumb name")
    if page.path in ("index.html", "download.html"):
        add("ld", mobile_application()["description"], "app description for search engines (structured data)")
    src = page_html(page)
    for nodes in _runs(parse(src)):
        nodes = _trim(nodes, src)
        if not nodes:
            continue
        text, _ = _encode(nodes, src)
        if not _skip(text):
            add("run", text)
    for m in ATTR_RE.finditer(src):
        v = html.unescape(m.group(2))
        if not _skip(v):
            add("attr", v, "attribute (alt text or label for screen readers)")
    return out


def _trim(nodes: list, src: str) -> list:
    def blank(n) -> bool:
        return isinstance(n, Text) and (n.comment or not src[n.start:n.end].strip())
    while nodes and blank(nodes[0]):
        nodes = nodes[1:]
    while nodes and blank(nodes[-1]):
        nodes = nodes[:-1]
    return nodes


def translate_html(src: str, tm: dict, missing: set) -> str:
    """Replace every run and attribute value in src with its translation from tm (key -> text)."""
    edits = []
    for nodes in _runs(parse(src)):
        nodes = _trim(nodes, src)
        if not nodes:
            continue
        text, tags = _encode(nodes, src)
        if _skip(text):
            continue
        k = key("run", text)
        if k not in tm:
            missing.add(k)
            continue
        start, end = nodes[0].start, nodes[-1].end
        edits.append((start, end, _decode(tm[k], tags)))
    out = src
    for start, end, rep in sorted(edits, reverse=True):
        out = out[:start] + rep + out[end:]

    def attr(m: re.Match) -> str:
        v = html.unescape(m.group(2))
        if _skip(v):
            return m.group(0)
        k = key("txt", v)
        if k not in tm:
            missing.add(k)
            return m.group(0)
        return m.group(1) + html.escape(tm[k], quote=True) + m.group(3)

    return ATTR_RE.sub(attr, out)


# ── Translation memory ───────────────────────────────────────────────────────────────────────
def load_tm(lang: str) -> dict:
    """key -> translation"""
    p = I18N / f"{lang}.json"
    if not p.exists():
        return {}
    return {k: v["t"] for k, v in json.loads(p.read_text(encoding="utf-8")).items()}


def _t(tm: dict, kind: str, text: str, missing: set) -> str:
    k = key("txt", text)
    if k not in tm:
        missing.add(k)
        return text
    return tm[k]


# ── Building the translated site ──────────────────────────────────────────────────────────────
class Plan:
    """Which pages exist in which language, and their translated content. Built before writing any page, because
    every English page links to its translations (hreflang and the language menu)."""

    def __init__(self, pages: list[Page]):
        self.pages = {p.path: p for p in pages}
        self.tms = {lang: load_tm(lang) for lang in LANGS}
        self.built: dict[str, set[str]] = {lang: set() for lang in LANGS}
        self.missing: dict[str, dict[str, int]] = {lang: {} for lang in LANGS}
        for path in PAGES:
            page = self.pages.get(path)
            if page is None:
                continue
            src = page_html(page)
            for lang in LANGS:
                miss: set[str] = set()
                translate_html(src, self.tms[lang], miss)
                for s in segments(page):
                    if s["kind"] != "run" and s["kind"] != "attr" and s["key"] not in self.tms[lang]:
                        miss.add(s["key"])
                if miss:
                    self.missing[lang][path] = len(miss)
                else:
                    self.built[lang].add(path)

    def alternates(self, path: str) -> dict[str, str]:
        page = self.pages[path]
        alt = {"en": page.url_path}
        for lang in LANGS:
            if path in self.built[lang]:
                alt[lang] = f"{lang}/{page.url_path}"
        return alt

    def menu_links(self, path: str) -> dict[str, str]:
        links = {"en": "", **{lang: f"{lang}/" for lang in LANGS if "index.html" in self.built[lang]}}
        if path in self.pages:
            links.update(self.alternates(path))
        return links

    def localized(self) -> list[tuple[Page, str]]:
        """(page, html) for every translated page."""
        out = []
        for lang in LANGS:
            tm = self.tms[lang]
            for path in PAGES:
                if path not in self.built[lang]:
                    continue
                out.append(self._page(self.pages[path], lang, tm))
        return out

    def _page(self, page: Page, lang: str, tm: dict) -> tuple[Page, str]:
        miss: set[str] = set()
        built = self.built[lang]
        body = translate_html(page_html(page), tm, miss)
        body = _localize_links(body, lang, built)
        title = _t(tm, "title", page.title, miss)
        desc = _t(tm, "description", page.description, miss)
        alt = _t(tm, "image_alt", page.image_alt, miss)
        crumbs = [(_t(tm, "crumb", n, miss), _local_path(p, lang, built)) for n, p in page.crumbs]
        loc_page = Page(path=f"{lang}/{page.path}", title=title, description=desc, body="", crumbs=crumbs,
                        og_type=page.og_type, image_path=page.image_path, image_alt=alt, priority=page.priority,
                        changefreq=page.changefreq)
        hreflang = LOCALES[lang]["hreflang"]
        canon = loc_page.canonical
        nodes: list[dict] = [{
            "@type": "WebPage", "@id": canon + "#webpage", "url": canon, "name": title, "description": desc,
            "inLanguage": hreflang, "isPartOf": {"@id": SITE_ID}, "publisher": organization(full=False),
        }]
        if len(crumbs) > 1:
            nodes.append(breadcrumb_ld(crumbs))
        faqs = FAQ_RE.findall(body)
        if faqs:
            nodes.append({"@type": "FAQPage", "inLanguage": hreflang, "mainEntity": [
                {"@type": "Question", "name": strip_tags(q), "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}}
                for q, a in faqs]})
        if page.path in ("index.html", "download.html"):
            app = mobile_application()
            app = {k: v for k, v in app.items() if k not in ("featureList", "offers", "alternateName")}
            app["description"] = _t(tm, "ld", app["description"], miss)
            app["url"] = BASE + f"{lang}/"
            app["offers"] = {"@type": "Offer", "price": "0", "priceCurrency": "AUD"}
            nodes.append(app)
        assert not miss, (lang, page.path, len(miss))
        doc = render(loc_page, lang=lang, body_html=body, title=title, description=desc, image_alt=alt, ld_nodes=nodes,
                     alternates=self.alternates(page.path), menu_links=self.menu_links(page.path))
        return loc_page, doc


def _local_path(path: str, lang: str, built: set[str]) -> str:
    target = (path or "index.html")
    if target.endswith("/"):
        target += "index.html"
    return f"{lang}/{path}" if target in built else path


def _localize_links(s: str, lang: str, built: set[str]) -> str:
    """Links to pages that exist in this language stay in it; the rest (guides, legal pages) go to English."""
    def repl(m: re.Match) -> str:
        path, rest = m.group(1), m.group(2) or ""
        return f'href="@/{_local_path(path, lang, built)}{rest}"'
    return re.sub(r'href="@/([^"#?]*)([#?][^"]*)?"', repl, s)


# ── Checking translations ────────────────────────────────────────────────────────────────────
TITLE_MAX = {"zh": 40, "ar": 70, "vi": 70, "es": 70}
DESC_RANGE = {"zh": (45, 100), "ar": (100, 175), "vi": (110, 190), "es": (120, 190)}


def validate(src: str, t: str, kind: str, lang: str) -> list[str]:
    errs = []
    if not t or not t.strip():
        return ["empty translation"]
    if Counter(PH_RE.findall(src)) != Counter(PH_RE.findall(t)):
        errs.append(f"placeholders differ: {sorted(PH_RE.findall(src))} vs {sorted(PH_RE.findall(t))}")
    for n in re.findall(r"<t(\d+)>", t):
        if f"</t{n}>" in t and t.index(f"<t{n}>") > t.index(f"</t{n}>"):
            errs.append(f"</t{n}> comes before <t{n}>")
    if re.search(r"<(?!/?t\d+>|x\d+/>)/?[A-Za-z]", t):
        errs.append("raw HTML tag in the translation (only <tN>, </tN> and <xN/> placeholders are allowed)")
    ps, pt = plain(src), plain(t)
    lost = Counter(re.findall(r"\d+", ps)) - Counter(re.findall(r"\d+", pt))
    if lost:
        errs.append(f"numbers missing: {sorted(lost.elements())}")
    if re.search("[٠-٩۰-۹]", t):
        errs.append("Arabic-Indic digits (keep 0-9)")
    for tok in ("A$", EMAIL, "Google Play", "BlueOrbit"):
        if tok in ps and tok not in pt:
            errs.append(f"'{tok}' must stay as it is")
    for code in set(CODES.findall(ps)):
        if code not in pt:
            errs.append(f"code '{code}' must stay in Latin letters")
    if SITE_NAME in ps and SITE_NAME not in pt:
        errs.append(f"the name '{SITE_NAME}' must stay in English")
    if kind == "title" and len(pt) > TITLE_MAX[lang]:
        errs.append(f"title is {len(pt)} characters (max {TITLE_MAX[lang]})")
    if kind == "description":
        lo, hi = DESC_RANGE[lang]
        if not lo <= len(pt) <= hi:
            errs.append(f"description is {len(pt)} characters (want {lo}-{hi})")
    for script, owner in ((r"[؀-ۿ]", "ar"), (r"[一-鿿]", "zh")):
        if lang != owner and re.search(script, pt) and not re.search(script, ps):
            errs.append("text in the wrong script")
    return errs


def source() -> list[dict]:
    """Every segment of every translated page, in page order, with the pages it appears on."""
    sys.path.insert(0, str(HERE))
    import build  # noqa: E402  (tools/build.py; imported here to avoid a cycle)
    by_path = {p.path: p for p in build.all_pages()}
    order: dict[str, dict] = {}
    for path in PAGES:
        for s in segments(by_path[path]):
            if s["key"] in order:
                order[s["key"]]["pages"].append(path)
            else:
                order[s["key"]] = {**s, "pages": [path], "group": "core" if path in CORE_PAGES else "states"}
    return list(order.values())


def _read_part(p: Path) -> dict:
    data = json.loads(p.read_text(encoding="utf-8"))
    if isinstance(data, dict):
        return {k: v if isinstance(v, str) else v.get("t", "") for k, v in data.items()}
    return {d["key"]: d.get("t", "") for d in data}


def _check_part(lang: str, part: dict, src_by_key: dict) -> tuple[dict, list[str]]:
    ok, problems = {}, []
    for k, t in part.items():
        s = src_by_key.get(k)
        if s is None:
            problems.append(f"{k}: not a current segment (English changed?)")
            continue
        e = validate(s["src"], t, s["kind"], lang)
        if e:
            problems.append(f"{k} [{s['kind']}] {s['src'][:70]!r}: " + "; ".join(e))
        else:
            ok[k] = t
    return ok, problems


def main(argv: list[str]) -> int:
    if not argv:
        print(__doc__)
        return 2
    cmd, args = argv[0], argv[1:]
    src = source()
    by_key = {s["key"]: s for s in src}
    if cmd == "extract":
        I18N.mkdir(exist_ok=True)
        (I18N / "_source.json").write_text(json.dumps(src, ensure_ascii=False, indent=1), encoding="utf-8")
        words = sum(len(plain(s["src"]).split()) for s in src)
        print(f"{len(src)} segments, {words} English words -> tools/i18n/_source.json")
        for g in ("core", "states"):
            gs = [s for s in src if s["group"] == g]
            print(f"  {g}: {len(gs)} segments, {sum(len(plain(s['src']).split()) for s in gs)} words")
        return 0
    if cmd == "todo":
        lang, out = args[0], Path(args[1])
        group = args[2] if len(args) > 2 else None
        tm = load_tm(lang)
        todo = [{"key": s["key"], "kind": s["kind"], "note": s["note"], "pages": s["pages"], "src": s["src"], "t": ""}
                for s in src if s["key"] not in tm and (group is None or s["group"] == group)]
        out.write_text(json.dumps(todo, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"{lang}: {len(todo)} segments to translate -> {out}")
        return 0
    if cmd in ("validate", "merge"):
        lang = args[0]
        merged = 0
        bad = 0
        tm_path = I18N / f"{lang}.json"
        store = json.loads(tm_path.read_text(encoding="utf-8")) if tm_path.exists() else {}
        for part_file in args[1:]:
            ok, problems = _check_part(lang, _read_part(Path(part_file)), by_key)
            for pr in problems:
                print("ERROR", pr)
            bad += len(problems)
            if cmd == "merge":
                for k, t in ok.items():
                    store[k] = {"src": by_key[k]["src"], "t": t}
                merged += len(ok)
        if cmd == "merge":
            order = {s["key"]: i for i, s in enumerate(src)}
            store = dict(sorted(store.items(), key=lambda kv: order.get(kv[0], 10 ** 9)))
            tm_path.write_text(json.dumps(store, ensure_ascii=False, indent=1), encoding="utf-8")
            print(f"{lang}: merged {merged} translations; {bad} rejected")
        else:
            print(f"{lang}: {bad} problem(s)")
        return 1 if bad else 0
    if cmd == "check":
        langs = args or LANGS
        status = 0
        for lang in langs:
            tm_path = I18N / f"{lang}.json"
            store = json.loads(tm_path.read_text(encoding="utf-8")) if tm_path.exists() else {}
            errs = []
            for k, v in store.items():
                if k in by_key:
                    e = validate(by_key[k]["src"], v["t"], by_key[k]["kind"], lang)
                    if e:
                        errs.append(f"{k} {by_key[k]['src'][:60]!r}: " + "; ".join(e))
            stale = [k for k in store if k not in by_key]
            print(f"{lang}: {sum(1 for k in by_key if k in store)}/{len(by_key)} segments, {len(errs)} error(s), "
                  f"{len(stale)} unused")
            for path in PAGES:
                need = [s for s in src if path in s["pages"]]
                have = sum(1 for s in need if s["key"] in store)
                print(f"  {'OK ' if have == len(need) else '   '}{path}: {have}/{len(need)}")
            for e in errs:
                print("  ERROR", e)
            status |= 1 if errs else 0
        return status
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
