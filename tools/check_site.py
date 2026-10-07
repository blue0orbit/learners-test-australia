"""Validate the built site. Run from anywhere:  python tools/check_site.py

Checks
  links      every relative href/src resolves to a file (and #fragments to an id); no third-party resources
  pages      one <title>, meta description, lang="en-AU", exactly one <h1>, canonical, OG + Twitter tags, robots,
             viewport, theme-color; unique titles (<= 60 chars) and descriptions (140-160 chars)
  structure  well-formed tags, unique ids, heading levels never skip downwards, <img> alt/width/height
  json-ld    every block parses; expected types per page; no ratings or reviews
  files      sitemap lists every indexable page (with lastmod); robots.txt, llms.txt, llms-full.txt, .nojekyll,
             site.webmanifest exist and are sensible
  content    word counts for posts (800-1500) and state pages (700-1200); honesty and placeholder scans; ACT naming
             and WA format rules
  contrast   WCAG AA contrast for the colour pairs used in the stylesheet
Exit code 1 if any error is found.
"""
from __future__ import annotations

import json
import re
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse

sys.path.insert(0, str(Path(__file__).resolve().parent))
from sitelib import LOCALES, PLAY_URL  # noqa: E402

LANG_DIRS = {c for c in LOCALES if c != "en"}
# Title and description lengths (characters) for translated pages; English uses 60 and 140-160.
TITLE_MAX = {"zh": 40, "ar": 70, "vi": 70, "es": 70}
DESC_RANGE = {"zh": (45, 100), "ar": (100, 175), "vi": (110, 190), "es": (120, 190)}


def lang_of(rel: str) -> str:
    first = rel.split("/", 1)[0]
    return first if first in LANG_DIRS and "/" in rel else "en"

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://au.learnertest.com/"
BASE_PATH = "/"
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}
STATE_PAGES = (
    "nsw-dkt-practice-test.html", "vic-learner-permit-test-practice.html", "qld-learner-test-practice.html",
    "sa-learners-test-practice.html", "wa-learners-test-practice.html", "tas-learners-test-practice.html",
    "act-learners-test-practice.html", "nt-learners-test-practice.html",
)
DISCLAIMER_TEXT = ("It is not affiliated with, endorsed by or connected to any Australian state or territory government, "
                   "licensing authority or other government agency.")

errors: list[str] = []
warnings: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.links: list[tuple[str, str, str]] = []  # (tag, attr, value)
        self.ids: list[str] = []
        self.titles: list[str] = []
        self.meta: dict[str, list[str]] = {}
        self.link_rel: dict[str, list[str]] = {}
        self.html_lang: str | None = None
        self.html_dir: str | None = None
        self.alternates: dict[str, str] = {}
        self.headings: list[tuple[int, str]] = []
        self.jsonld: list[str] = []
        self.imgs: list[dict] = []
        self.stack: list[str] = []
        self.structure_errors: list[str] = []
        self._in: str | None = None
        self._buf: list[str] = []
        self._in_main = False
        self.main_text: list[str] = []
        self._skip_main = 0

    def handle_starttag(self, tag, attrs):
        a = {k: (v or "") for k, v in attrs}
        if tag not in VOID:
            self.stack.append(tag)
        if tag == "html":
            self.html_lang = a.get("lang")
            self.html_dir = a.get("dir")
        if "id" in a:
            self.ids.append(a["id"])
        for attr in ("href", "src"):
            if attr in a:
                self.links.append((tag, attr, a[attr]))
        if tag == "meta":
            key = a.get("name") or a.get("property")
            if key:
                self.meta.setdefault(key, []).append(a.get("content", ""))
        if tag == "link" and "rel" in a:
            self.link_rel.setdefault(a["rel"], []).append(a.get("href", ""))
            if a["rel"] == "alternate" and "hreflang" in a:
                self.alternates[a["hreflang"]] = a.get("href", "")
        if tag == "img":
            self.imgs.append(a)
        if tag == "title" or tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            self._in = tag
            self._buf = []
        if tag == "script" and a.get("type") == "application/ld+json":
            self._in = "ld"
            self._buf = []
        if tag == "main":
            self._in_main = True
        if self._in_main and (a.get("aria-hidden") == "true" or tag in {"script", "style", "svg"}):
            self._skip_main += 1 if tag not in VOID else 0

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if not self.stack:
            self.structure_errors.append(f"stray </{tag}>")
        elif self.stack[-1] != tag:
            self.structure_errors.append(f"</{tag}> closes <{self.stack[-1]}>")
            if tag in self.stack:
                while self.stack and self.stack.pop() != tag:
                    pass
        else:
            self.stack.pop()
        if self._in and tag == self._in:
            text = re.sub(r"\s+", " ", "".join(self._buf)).strip()
            if tag == "title":
                self.titles.append(text)
            else:
                self.headings.append((int(tag[1]), text))
            self._in = None
        elif self._in == "ld" and tag == "script":
            self.jsonld.append("".join(self._buf))
            self._in = None
        if tag == "main":
            self._in_main = False

    def handle_data(self, data):
        if self._in:
            self._buf.append(data)
        if self._in_main and self._in != "ld":
            self.main_text.append(data)


def html_files() -> list[Path]:
    return sorted(p for p in ROOT.rglob("*.html") if "tools" not in p.relative_to(ROOT).parts)


def resolve(page: Path, url: str) -> Path | None:
    path = unquote(urlparse(url).path)
    if path.startswith(BASE_PATH):
        target = ROOT / path[len(BASE_PATH):]
    elif path.startswith("/"):
        return None
    else:
        target = (page.parent / path).resolve() if path else page
    if url.split("#")[0].split("?")[0].endswith("/") or (target.exists() and target.is_dir()):
        target = target / "index.html"
    return target


def url_to_file(url: str) -> Path:
    rel = url[len(BASE):]
    if rel == "" or rel.endswith("/"):
        rel += "index.html"
    return ROOT / rel


def contrast(c1: str, c2: str) -> float:
    def lum(h: str) -> float:
        h = h.lstrip("#")
        rgb = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
        lin = [c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4 for c in rgb]
        return 0.2126 * lin[0] + 0.7152 * lin[1] + 0.0722 * lin[2]
    a, b = sorted((lum(c1), lum(c2)), reverse=True)
    return (a + 0.05) / (b + 0.05)


def main() -> int:
    files = html_files()
    parsed: dict[Path, PageParser] = {}
    for f in files:
        p = PageParser()
        p.feed(f.read_text(encoding="utf-8"))
        parsed[f] = p

    # ── links ──
    n_rel = n_ext = 0
    ext_urls: set[str] = set()
    for f, p in parsed.items():
        rel = f.relative_to(ROOT).as_posix()
        for tag, attr, url in p.links:
            if url.startswith(("mailto:", "tel:", "data:")):
                continue
            if url.startswith(("http://", "https://")):
                if tag == "a":
                    n_ext += 1
                    ext_urls.add(url)
                    if url.startswith("http://"):
                        err(f"{rel}: insecure link {url}")
                elif not (tag == "link" and url.startswith(BASE)):
                    err(f"{rel}: third-party resource <{tag} {attr}={url}>")
                continue
            if url.startswith("#"):
                if url[1:] and url[1:] not in p.ids:
                    err(f"{rel}: missing anchor {url}")
                continue
            if url.startswith("/") and not (rel == "404.html" and url.startswith(BASE_PATH)):
                err(f"{rel}: root-relative link {url} (use relative links)")
                continue
            target = resolve(f, url)
            n_rel += 1
            if target is None or not target.exists():
                err(f"{rel}: broken link {url}")
                continue
            frag = urlparse(url).fragment
            if frag and target.suffix == ".html" and target in parsed and frag not in parsed[target].ids:
                err(f"{rel}: missing anchor {url}")
        # Our app is not listed yet, so no link to its listing (sitelib.PLAY_URL turns the buttons into links later).
        # Links to the developer's other app (DTT Ireland) are fine.
        play_ids = set(re.findall(r"play\.google\.com/store/apps/details\?id=([\w.]+)", f.read_text(encoding="utf-8")))
        if "com.blueorbit.learnerstestau" in play_ids and not PLAY_URL:
            err(f"{rel}: links to the app's Google Play listing, but the app is not listed yet")
        if play_ids - {"com.app.dttireland", "com.blueorbit.learnerstestau"}:
            err(f"{rel}: links to an unexpected Google Play listing {sorted(play_ids)}")

    # ── per-page meta ──
    titles: dict[str, str] = {}
    descs: dict[str, str] = {}
    for f, p in parsed.items():
        rel = f.relative_to(ROOT).as_posix()
        is404 = rel == "404.html"
        if len(p.titles) != 1:
            err(f"{rel}: expected one <title>, found {len(p.titles)}")
        t = p.titles[0] if p.titles else ""
        lang = lang_of(rel)
        tmax = 60 if lang == "en" else TITLE_MAX[lang]
        if len(t) > tmax:
            err(f"{rel}: title is {len(t)} chars (> {tmax}): {t}")
        if t in titles:
            err(f"{rel}: duplicate title with {titles[t]}")
        titles[t] = rel
        d = (p.meta.get("description") or [""])[0]
        if not d:
            err(f"{rel}: missing meta description")
        else:
            lo, hi = (140, 160) if lang == "en" else DESC_RANGE[lang]
            if not lo <= len(d) <= hi:
                err(f"{rel}: description is {len(d)} chars (want {lo}-{hi})")
        if d in descs:
            err(f"{rel}: duplicate description with {descs[d]}")
        descs[d] = rel
        want_lang = LOCALES[lang]["hreflang"]
        if p.html_lang != want_lang:
            err(f"{rel}: html lang is {p.html_lang!r}, expected {want_lang!r}")
        if (p.html_dir == "rtl") != (LOCALES[lang]["dir"] == "rtl"):
            err(f"{rel}: html dir is {p.html_dir!r}")
        # hreflang: every version lists itself and all the others, plus x-default (the English page)
        if p.alternates:
            canon_here = (p.link_rel.get("canonical") or [""])[0]
            if p.alternates.get(want_lang) != canon_here:
                err(f"{rel}: hreflang {want_lang} does not point at this page's canonical")
            if p.alternates.get("x-default") != p.alternates.get("en-AU"):
                err(f"{rel}: x-default should be the English page")
            for hl, href in p.alternates.items():
                target = url_to_file(href) if href.startswith(BASE) else None
                if target is None or not target.exists():
                    err(f"{rel}: hreflang {hl} points at a missing page {href}")
                elif target.resolve() in parsed and parsed[target.resolve()].alternates != p.alternates:
                    err(f"{rel}: hreflang set differs from the one on {target.relative_to(ROOT).as_posix()}")
        elif lang != "en":
            err(f"{rel}: translated page without hreflang alternates")
        h1s = [h for h in p.headings if h[0] == 1]
        if len(h1s) != 1:
            err(f"{rel}: expected exactly one <h1>, found {len(h1s)}")
        for key in ("viewport", "robots", "theme-color", "og:title", "og:description", "og:url", "og:image", "og:type",
                    "twitter:card", "twitter:title", "twitter:description", "twitter:image"):
            if key not in p.meta:
                err(f"{rel}: missing meta {key}")
        canon = p.link_rel.get("canonical", [])
        if is404:
            if "noindex" not in (p.meta.get("robots") or [""])[0]:
                err("404.html should be noindex")
        else:
            if len(canon) != 1 or not canon[0].startswith(BASE):
                err(f"{rel}: missing or non-absolute canonical")
            else:
                if url_to_file(canon[0]).resolve() != f.resolve():
                    err(f"{rel}: canonical {canon[0]} does not point at this file")
                if (p.meta.get("og:url") or [""])[0] != canon[0]:
                    err(f"{rel}: og:url differs from canonical")
            is_home = rel == "index.html" or (lang != "en" and rel == f"{lang}/index.html")
            if not is_home and 'class="breadcrumbs"' not in f.read_text(encoding="utf-8"):
                err(f"{rel}: missing visible breadcrumbs")
        # structure
        for s in p.structure_errors[:5]:
            err(f"{rel}: markup: {s}")
        if p.stack:
            err(f"{rel}: unclosed tags {p.stack[-5:]}")
        dup = {i for i in p.ids if p.ids.count(i) > 1}
        if dup:
            err(f"{rel}: duplicate ids {sorted(dup)}")
        prev = 0
        for lvl, text in p.headings:
            if prev and lvl > prev + 1:
                err(f"{rel}: heading jumps from h{prev} to h{lvl} ({text[:40]})")
            prev = lvl
        for img in p.imgs:
            if not img.get("alt"):
                err(f"{rel}: <img src={img.get('src')}> has no alt text")
            if not (img.get("width") and img.get("height")):
                err(f"{rel}: <img src={img.get('src')}> has no width/height")

    # ── JSON-LD ──
    type_count: dict[str, int] = {}
    for f, p in parsed.items():
        rel = f.relative_to(ROOT).as_posix()
        types: set[str] = set()
        for block in p.jsonld:
            try:
                data = json.loads(block)
            except json.JSONDecodeError as e:
                err(f"{rel}: JSON-LD does not parse: {e}")
                continue
            if data.get("@context") != "https://schema.org":
                err(f"{rel}: JSON-LD missing @context")
            nodes = data.get("@graph", [data])
            for n in nodes:
                types.add(n.get("@type", "?"))
            if re.search(r'"(aggregateRating|review|ratingValue)"', block):
                err(f"{rel}: JSON-LD contains ratings or reviews")
        for t in types:
            type_count[t] = type_count.get(t, 0) + 1
        expect: set[str] = set()
        if lang_of(rel) != "en":
            base_rel = rel.split("/", 1)[1]
            if base_rel == "index.html":
                expect = {"WebPage", "MobileApplication"}
            elif base_rel == "faq.html" or base_rel.endswith(("-practice-test.html", "-test-practice.html")):
                expect = {"WebPage", "FAQPage", "BreadcrumbList"}
            else:
                expect = {"WebPage", "BreadcrumbList"}
        elif rel == "index.html":
            expect = {"Organization", "WebSite", "MobileApplication"}
        elif rel == "faq.html" or rel.endswith("-practice-test.html") or rel.endswith("-test-practice.html"):
            expect = {"FAQPage", "BreadcrumbList"}
        elif rel.startswith("blog/") and rel != "blog/index.html":
            expect = {"BlogPosting", "BreadcrumbList"}
        elif rel == "blog/index.html":
            expect = {"Blog", "BreadcrumbList"}
        elif rel != "404.html":
            expect = {"BreadcrumbList"}
        missing = expect - types
        if missing:
            err(f"{rel}: JSON-LD missing {sorted(missing)}")

    # ── sitemap / robots / llms / misc files ──
    sm = ROOT / "sitemap.xml"
    sitemap_urls: list[str] = []
    if not sm.exists():
        err("sitemap.xml missing")
    else:
        ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        tree = ET.parse(sm)
        for u in tree.getroot().findall("s:url", ns):
            loc = u.findtext("s:loc", namespaces=ns)
            sitemap_urls.append(loc)
            if not u.findtext("s:lastmod", namespaces=ns):
                err(f"sitemap: {loc} has no lastmod")
            if not url_to_file(loc).exists():
                err(f"sitemap: {loc} has no matching file")
        listed = {url_to_file(u).resolve() for u in sitemap_urls}
        for f in files:
            rel = f.relative_to(ROOT).as_posix()
            if rel == "404.html":
                if f.resolve() in listed:
                    err("sitemap lists 404.html")
                continue
            if f.resolve() not in listed:
                err(f"sitemap does not list {rel}")
    robots = ROOT / "robots.txt"
    if not robots.exists():
        err("robots.txt missing")
    else:
        rt = robots.read_text(encoding="utf-8")
        if f"Sitemap: {BASE}sitemap.xml" not in rt:
            err("robots.txt does not point to the sitemap")
        for bot in ["GPTBot", "ChatGPT-User", "OAI-SearchBot", "ClaudeBot", "Claude-User", "Claude-SearchBot",
                    "anthropic-ai", "PerplexityBot", "Google-Extended", "Applebot-Extended", "CCBot", "Bingbot", "Googlebot"]:
            if f"User-agent: {bot}\nAllow: /" not in rt:
                err(f"robots.txt does not allow {bot}")
        if re.search(r"^Disallow:\s*/\s*$", rt, re.M):
            err("robots.txt disallows everything")
    llms = ROOT / "llms.txt"
    if not llms.exists():
        err("llms.txt missing")
    else:
        lt = llms.read_text(encoding="utf-8")
        if not lt.startswith("# ") or "\n> " not in lt or "\n## " not in lt:
            err("llms.txt does not follow the llms.txt layout (H1, blockquote, H2 sections)")
        for m in re.finditer(r"\]\((https://[^)]+)\)", lt):
            if m.group(1).startswith(BASE) and not url_to_file(m.group(1)).exists():
                err(f"llms.txt links to missing {m.group(1)}")
    full = ROOT / "llms-full.txt"
    if not full.exists() or full.stat().st_size < 20000:
        err("llms-full.txt missing or too small")
    for name in (".nojekyll", "site.webmanifest", "favicon.ico", "404.html", "assets/img/og-image.png",
                 "assets/fonts/OFL-Overpass.txt", "assets/fonts/OFL-AtkinsonHyperlegibleNext.txt"):
        if not (ROOT / name).exists():
            err(f"{name} missing")
    try:
        man = json.loads((ROOT / "site.webmanifest").read_text(encoding="utf-8"))
        for icon in man.get("icons", []):
            if not (ROOT / icon["src"]).exists():
                err(f"manifest icon missing: {icon['src']}")
    except Exception as e:  # noqa: BLE001
        err(f"site.webmanifest invalid: {e}")

    # ── content ──
    counts: dict[str, int] = {}
    for f, p in parsed.items():
        rel = f.relative_to(ROOT).as_posix()
        text = " ".join(p.main_text)
        wc = len(text.split())
        counts[rel] = wc
        raw = f.read_text(encoding="utf-8")
        low = text.lower()
        translated = lang_of(rel) != "en"
        if translated:
            counts[rel] = len(text)  # characters: words don't split the same way in every language
        if rel.startswith("blog/") and rel != "blog/index.html":
            # article body only: between the answer box and the source box
            m = re.search(r'<article class="prose">(.*?)<aside class="source-box"', raw, re.S)
            body_wc = len(re.sub(r"<[^>]+>", " ", m.group(1)).split()) if m else 0
            counts[rel] = body_wc
            if not 800 <= body_wc <= 1500:
                err(f"{rel}: post body has {body_wc} words (want 800-1500)")
            product_guide = rel == "blog/why-choose-learners-test-australia.html"
            source_heading = "About this product guide" if product_guide else "Check the official source"
            for needle in (source_heading, "BlueOrbit"):
                if needle not in raw:
                    err(f"{rel}: missing '{needle}'")
            if not re.search(r'Published <time datetime="\d{4}-\d{2}-\d{2}">', raw):
                err(f"{rel}: missing dated publication byline")
            if product_guide and "first-party product guide" not in raw:
                err(f"{rel}: product guide must disclose first-party authorship")
        if rel in STATE_PAGES and not translated:
            m = re.search(r'<article class="prose">(.*?)<section class="callout light-cta"', raw, re.S)
            body_wc = len(re.sub(r"<[^>]+>", " ", m.group(1)).split()) if m else 0
            counts[rel] = body_wc
            if not 700 <= body_wc <= 1200:
                err(f"{rel}: state page body has {body_wc} words (want 700-1200)")
        # State content rules (see tools/pages_states.py): ACT restricted names never appear anywhere, no ACT question
        # is called mandatory.
        raw_low = raw.lower()
        for name in ("pre-learner", "prelearner", "road rules knowledge test", "safe plates"):
            if name in raw_low:
                err(f"{rel}: contains the restricted ACT name '{name}'")
        if rel == "act-learners-test-practice.html" and "mandatory" in raw_low:
            err(f"{rel}: describes a question as mandatory")
        # ("todo" is an ordinary word in Spanish, so it is only a placeholder on English pages)
        for bad in ("lorem", "ipsum", "tbd", "placeholder") + (() if translated else ("todo",)):
            if re.search(rf"\b{bad}\b", low):
                err(f"{rel}: contains '{bad}'")
        if 'href="#"' in raw:
            err(f"{rel}: placeholder link href=\"#\"")
        for claim in (r"\bpass rate", r"\btestimonial", r"\b\d[\d,]* (downloads|users|learners have)\b", r"\b\d(\.\d)? stars?\b",
                      r"\brated\b"):
            if re.search(claim, low):
                err(f"{rel}: possible invented claim matching {claim}")
        if not translated and rel != "404.html" and "Last updated" not in raw and rel not in ("index.html",):
            warn(f"{rel}: no 'Last updated' line")
        if translated:
            if not re.search(r'<p class="disclaimer">[^<]{40,}</p>', raw):
                err(f"{rel}: footer disclaimer missing")
            # English sentence starts left in a translated page (official titles, kept in English on purpose, aside)
            main_html = raw.split("<main", 1)[-1].split("</main>")[0].replace("Your keys to driving in Queensland", "")
            if re.search(r"<(p|li|h[1-6]|td|th)[^>]*>\s*(?:<[^>]+>\s*)*(?:The|This|Your|You|Every|Our) [a-z]+ [a-z]+", main_html):
                warn(f"{rel}: some text in <main> looks untranslated")
        elif DISCLAIMER_TEXT not in raw:
            err(f"{rel}: footer disclaimer missing")
        for need in ("privacy-policy.html", "cookies.html", "terms.html", "account-deletion.html", "faq.html", "contact.html"):
            if need not in raw.split('<footer', 1)[-1]:
                err(f"{rel}: footer lacks link to {need}")
        if "2026 BlueOrbit" not in raw:
            err(f"{rel}: footer copyright missing")

    # ── contrast (pairs used in site.css) ──
    pairs = [
        ("light body text", "#12161D", "#F3F4F6"), ("light muted on bg", "#4A5261", "#F3F4F6"),
        ("light muted on surface", "#4A5261", "#FFFFFF"), ("light muted on surface-2", "#4A5261", "#E8EAEE"),
        ("light link on bg", "#7A4A00", "#F3F4F6"), ("light link on surface", "#7A4A00", "#FFFFFF"),
        ("light link on accent", "#7A4A00", "#FFF3DA"), ("light good text", "#12703E", "#FFFFFF"),
        ("dark body text", "#F3F4F6", "#0C0F14"), ("dark muted on bg", "#A9B1BD", "#0C0F14"),
        ("dark muted on surface", "#A9B1BD", "#151A22"), ("dark muted on surface-2", "#A9B1BD", "#1B212B"),
        ("dark link on bg", "#FFA41B", "#0C0F14"), ("dark link on surface", "#FFA41B", "#151A22"),
        ("dark link on accent", "#FFA41B", "#231C10"), ("dark good text", "#4CC98A", "#151A22"),
        ("header text on ink", "#F3F4F6", "#12161D"), ("nav current (amber on ink)", "#FFA41B", "#12161D"),
        ("hero lead on ink", "#D2D7DF", "#12161D"), ("hero fine print on ink", "#B9C0CB", "#12161D"),
        ("soon note on ink", "#C3CAD4", "#12161D"), ("footer text", "#C9CFD8", "#0C0F14"),
        ("footer text (dark)", "#C9CFD8", "#07090C"), ("footer heading (plate)", "#FFC72C", "#0C0F14"),
        ("primary button text", "#12161D", "#FFA41B"), ("plate chip", "#12161D", "#FFC72C"),
        ("step number", "#12161D", "#FFA41B"), ("skip link", "#12161D", "#FFA41B"),
        ("correct option key", "#FFFFFF", "#16874B"), ("wrong option key", "#FFFFFF", "#CC3B42"),
    ]
    for name, fg, bg in pairs:
        r = contrast(fg, bg)
        if r < 4.5:
            err(f"contrast {name}: {fg} on {bg} = {r:.2f} (< 4.5)")

    # ── report ──
    print(f"Pages checked: {len(files)}")
    print(f"Relative links/resources resolved: {n_rel}; external links (not fetched): {n_ext} ({len(ext_urls)} unique)")
    print(f"Sitemap URLs: {len(sitemap_urls)}")
    print("JSON-LD types: " + ", ".join(f"{k}×{v}" for k, v in sorted(type_count.items())))
    print("Word counts (posts/state pages: article body; others: main text; translated pages: characters):")
    for rel, wc in sorted(counts.items()):
        print(f"  {wc:5d}  {rel}")
    print("Contrast: min ratio {:.2f} across {} pairs".format(min(contrast(fg, bg) for _, fg, bg in pairs), len(pairs)))
    for w in warnings:
        print("WARN  " + w)
    for e in errors:
        print("ERROR " + e)
    print(f"\n{len(errors)} error(s), {len(warnings)} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
