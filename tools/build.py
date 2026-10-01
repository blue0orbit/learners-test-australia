"""Build the static site: HTML pages, sitemap.xml, robots.txt, llms.txt, llms-full.txt, site.webmanifest,
.nojekyll, favicon.svg and SEO.md.

Run from anywhere:  python tools/build.py
Then validate:      python tools/check_site.py
"""
from __future__ import annotations

import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import i18n  # noqa: E402
import pages_blog  # noqa: E402
import pages_core  # noqa: E402
import pages_legal  # noqa: E402
import pages_states  # noqa: E402
from sitelib import (  # noqa: E402
    ADMOB_PUBLISHER, APP_NAME, BASE, DATE, INDEXNOW_KEY, LOCALES, DATE_H, DEVELOPER, DISCLAIMER, EMAIL, PLATE_SVG, PRICE, SITE_NAME, Page, render,
)

ROOT = Path(__file__).resolve().parent.parent


def all_pages() -> list[Page]:
    posts = [f() for f in pages_blog.POSTS]
    return [
        pages_core.home(),
        pages_core.features(),
        pages_core.states(),
        pages_states.nsw(),
        pages_states.vic(),
        pages_states.qld(),
        pages_states.sa(),
        pages_states.wa(),
        pages_states.tas(),
        pages_states.act(),
        pages_states.nt(),
        pages_core.faq(),
        pages_blog.blog_index(posts),
        *posts,
        pages_core.about(),
        pages_core.contact(),
        pages_core.download(),
        pages_legal.privacy(),
        pages_legal.cookies(),
        pages_legal.terms(),
        pages_legal.account_deletion(),
        pages_core.not_found(),
    ]


# ── HTML → plain text for llms-full.txt ──────────────────────────────────────────────────────
class TextExtractor(HTMLParser):
    BLOCK = {"p", "div", "section", "article", "aside", "figure", "figcaption", "details", "summary", "dl", "ul", "ol",
             "table", "caption", "blockquote", "main", "header", "footer"}
    SKIP_CLASSES = ("phone", "breadcrumbs", "toc", "store-soon", "light-cta", "nav-toggle")

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.out: list[str] = []
        self.skip_depth = 0
        self.stack: list[tuple[str, bool]] = []
        self.href: str | None = None

    def _skipping(self) -> bool:
        return self.skip_depth > 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        void = tag in {"br", "img", "hr", "meta", "link", "input", "source"}
        skip = (a.get("aria-hidden") == "true" or tag in {"svg", "button", "script", "style"}
                or any(c in (a.get("class") or "").split() for c in self.SKIP_CLASSES))
        if not void:
            self.stack.append((tag, skip))
            if skip:
                self.skip_depth += 1
        if self._skipping():
            return
        if tag in {"h1", "h2", "h3", "h4"}:
            self.out.append("\n\n" + "#" * int(tag[1]) + " ")
        elif tag in self.BLOCK:
            self.out.append("\n\n")
        elif tag == "li":
            self.out.append("\n- ")
        elif tag == "tr":
            self.out.append("\n| ")
        elif tag == "dt":
            self.out.append("\n- ")
        elif tag == "dd":
            self.out.append(": ")
        elif tag == "br":
            self.out.append("\n")
        elif tag == "a":
            self.href = a.get("href")

    def handle_endtag(self, tag):
        if not self.stack:
            return
        # pop to the matching tag
        while self.stack:
            t, skip = self.stack.pop()
            if skip:
                self.skip_depth -= 1
            if t == tag:
                break
        if self._skipping():
            return
        if tag in {"h1", "h2", "h3", "h4"} or tag in self.BLOCK:
            self.out.append("\n\n")
        elif tag in {"td", "th"}:
            self.out.append(" | ")
        elif tag == "a" and self.href:
            h = self.href
            if h.startswith("@/"):
                self.out.append(f" ({BASE}{h[2:]})")
            elif h.startswith("http"):
                self.out.append(f" ({h})")
            self.href = None

    def handle_data(self, data):
        if self._skipping():
            return
        self.out.append(re.sub(r"\s+", " ", data))

    def text(self) -> str:
        s = "".join(self.out)
        s = re.sub(r"[ \t]+\n", "\n", s)
        s = re.sub(r"\n[ \t]+", "\n", s)
        s = re.sub(r"\n{3,}", "\n\n", s)
        s = re.sub(r" {2,}", " ", s)
        return s.strip()


def page_text(p: Page) -> str:
    t = TextExtractor()
    t.feed(p.body)
    return t.text()


# ── Other generated files ─────────────────────────────────────────────────────────────────────
AI_AND_SEARCH_BOTS = [
    "Googlebot", "Bingbot", "GPTBot", "ChatGPT-User", "OAI-SearchBot", "ClaudeBot", "Claude-User",
    "Claude-SearchBot", "anthropic-ai", "PerplexityBot", "Google-Extended", "Applebot-Extended", "CCBot",
]


def robots_txt() -> str:
    lines = [
        f"# robots.txt for the {SITE_NAME} website ({BASE})",
        "# All crawlers, including search engines and AI assistants, are welcome to read and cite this site.",
        "",
        "User-agent: *",
        "Allow: /",
        "",
    ]
    for bot in AI_AND_SEARCH_BOTS:
        lines += [f"User-agent: {bot}", "Allow: /", ""]
    lines.append(f"Sitemap: {BASE}sitemap.xml")
    return "\n".join(lines) + "\n"


def sitemap_xml(pages: list[Page]) -> str:
    rows = []
    for p in pages:
        if p.noindex:
            continue
        rows.append(
            f"  <url>\n    <loc>{p.canonical}</loc>\n    <lastmod>{p.article['modified'][:10] if p.article else ('2026-10-01' if p.path == 'blog/index.html' else DATE)}</lastmod>\n"
            f"    <changefreq>{p.changefreq}</changefreq>\n    <priority>{p.priority}</priority>\n  </url>"
        )
    return ('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            + "\n".join(rows) + "\n</urlset>\n")


SUMMARY = (
    f"{SITE_NAME} (Google Play title “{APP_NAME}”) is an independent Android study app by {DEVELOPER} for learner "
    "drivers in all eight Australian states and territories. It has original practice questions and mock tests "
    "in each state's learner knowledge test format, with every answer explained and linked to the handbook page or road "
    f"rule it comes from. Free to practise, with an optional one-time {PRICE} Premium purchase. Not affiliated with any "
    "government agency. The app is not on Google Play yet (coming soon)."
)

KEY_FACTS = [
    f"Developer: {DEVELOPER}. Support email: {EMAIL}. Package: com.blueorbit.learnerstestau. Platform: Android 8.0 or later.",
    "States and territories covered: all eight (NSW, VIC, QLD, SA, WA, TAS, ACT, NT).",
    "NSW Driver Knowledge Test (DKT): 45 questions; general knowledge 15 (pass 12) and road safety 30 (pass 29); ends early once passing is impossible; no time limit published (structure as published by the NSW Government on its knowledge test pages; the car DKT is reported to follow it). DKT online course from 15 years 11 months.",
    "Victorian learner permit test: online learner permit course with final test is the default; in-person test is 32 multiple-choice questions, pass 25 (78%).",
    "Queensland written road rules test: 30 questions; giving way 10 (pass 9) and road rules and licence requirements 20 (pass 18). PrepL final test: 30 questions, pass 27 (90%).",
    "South Australian learner's theory test: in person, Part A 8 give-way diagram questions (all must be correct) then Part B 42 questions (pass 32); or myLs online course and 30-question test (pass 27, some questions with more than one correct answer). myLs from 15 years 9 months; permit and in-person test from 16.",
    "Western Australia: before a learner's permit (from 16) you must show knowledge of WA traffic laws and safe driving techniques, normally by a theory test. This site does not state the official question count or pass mark (check the WA Department of Transport and Major Infrastructure); the app's WA practice test uses a 30-question format.",
    "Tasmanian driver knowledge test: free Plates Plus online course, then a 30-question online test (pass 27; some questions with more than one correct answer; no compulsory questions), from 15 years 11 months. The standalone Service Tasmania test format is not published.",
    "ACT learner licence knowledge test: taken only at the end of an approved course (approved provider or participating school); 35 questions from a bank of more than 300; at least 31 correct needed (not every detail of the pass rule is published). Learner licence from 15 years 9 months.",
    "Northern Territory driver knowledge test: 30 questions from a pool of more than 300, pass 26, at an MVR office, from 16. No hazard perception test in the NT.",
    "Free version: every practice question free; one free mock test per day plus another per rewarded ad; banner ads on results and guide pages.",
    f"Premium: one-time {PRICE}, no subscription, all states: no ads, unlimited mock tests, section forecasts, weak spots and review planner, all 72 hazard perception clips and every scene.",
    "Languages: English, Simplified Chinese, Arabic, Vietnamese, Spanish, for the questions and explanations of all eight states and territories. Dark mode. Offline practice after sign-in.",
    "Account required (Google, Facebook or email). Delete in the app via Settings → Delete account, or email with subject “Delete my account”.",
    "Content: original questions checked against official handbooks and legislation as at 30 September 2026; no official questions, text or images reproduced.",
    f"Disclaimer: {DISCLAIMER}",
]


def llms_txt(pages: list[Page], localized: list[Page] | None = None) -> str:
    by_path = {p.path: p for p in pages}

    def item(path: str) -> str:
        p = by_path[path]
        name = p.llms_title or p.title.split(" | ")[0]
        return f"- [{name}]({p.canonical}): {p.llms_note or p.description}"

    groups = [
        ("The app", ["index.html", "features.html", "faq.html", "about.html", "download.html"]),
        ("Learner tests by state", ["states.html", "nsw-dkt-practice-test.html", "vic-learner-permit-test-practice.html",
                                    "qld-learner-test-practice.html", "sa-learners-test-practice.html",
                                    "wa-learners-test-practice.html", "tas-learners-test-practice.html",
                                    "act-learners-test-practice.html", "nt-learners-test-practice.html"]),
        ("Guides", ["blog/index.html"] + [p.path for p in pages if p.path.startswith("blog/") and p.path != "blog/index.html"]),
        ("Policies and support", ["privacy-policy.html", "cookies.html", "terms.html", "account-deletion.html", "contact.html"]),
    ]
    out = [f"# {SITE_NAME}", "", f"> {SUMMARY}", "", "Key facts (checked " + DATE_H + "):", ""]
    out += [f"- {f}" for f in KEY_FACTS]
    for title, paths in groups:
        out += ["", f"## {title}", ""]
        out += [item(pth) for pth in paths]
    by_lang: dict[str, list[Page]] = {}
    for lp in localized or []:
        by_lang.setdefault(lp.path.split("/", 1)[0], []).append(lp)
    if by_lang:
        out += ["", "## Other languages", "",
                "The home, features, states, state, FAQ, about, contact and download pages are also available in these "
                "languages, for readers in Australia (guides and policies are in English):", ""]
        for code, lps in by_lang.items():
            loc = LOCALES[code]
            out.append(f"- {loc['name']} ({loc['hreflang']}): " + ", ".join(
                f"[{lp.title.split('｜')[0].split(' | ')[0]}]({lp.canonical})" for lp in lps))
    out += ["", "## Optional", "",
            f"- [Full text of the main pages]({BASE}llms-full.txt): plain-text copy of the home, features, states, state, "
            "FAQ, guide, privacy and account deletion pages, for quoting accurate facts.",
            f"- [Sitemap]({BASE}sitemap.xml): every page on the site."]
    return "\n".join(out) + "\n"


def llms_full_txt(pages: list[Page]) -> str:
    out = [f"# {SITE_NAME}: full text", "", f"> {SUMMARY}", "",
           f"Source: {BASE} · Content current as of {DATE_H}. Each section below is one page of the website.", ""]
    for p in pages:
        if not p.llms:
            continue
        out += ["", "---", "", f"URL: {p.canonical}", "", page_text(p)]
    return "\n".join(out).strip() + "\n"


def manifest() -> str:
    return json.dumps({
        "name": SITE_NAME,
        "short_name": "Learners Test",
        "description": "Learner test practice for every Australian state and territory.",
        "start_url": "./",
        "scope": "./",
        "display": "browser",
        "background_color": "#12161D",
        "theme_color": "#12161D",
        "icons": [
            {"src": "assets/img/icon-192.png", "sizes": "192x192", "type": "image/png"},
            {"src": "assets/img/icon-512.png", "sizes": "512x512", "type": "image/png"},
        ],
    }, indent=2) + "\n"


def favicon_svg() -> str:
    svg = PLATE_SVG.format(s=64).replace('class="plate-mark" ', 'xmlns="http://www.w3.org/2000/svg" ')
    svg = svg.replace(' aria-hidden="true" focusable="false"', "")
    return svg + "\n"


# ── SEO keyword map (written to SEO.md) ───────────────────────────────────────────────────────
KEYWORDS = {
    "blog/why-choose-learners-test-australia.html": ("learner test app", ["compare learner test apps", "Learners Test Australia", "Android learner test practice"]),
    "index.html": ("learners test", ["learner test practice", "learner driver app Australia", "DKT practice test", "learners permit test", "road rules test Australia", "L plates"]),
    "features.html": ("learner driver app features", ["mock test", "explained answers", "road signs quiz", "hazard perception practice", "learner test app in Chinese, Arabic, Vietnamese, Spanish"]),
    "states.html": ("learner test by state", ["road rules test Australia", "NSW DKT", "VIC learner permit test", "QLD written road rules test", "SA learners test", "WA learners test", "TAS learners test", "ACT learners test", "NT learners test", "learners permit test"]),
    "nsw-dkt-practice-test.html": ("NSW DKT practice test", ["driver knowledge test NSW", "DKT online", "NSW learner licence", "DKT pass mark", "how many questions DKT"]),
    "vic-learner-permit-test-practice.html": ("VIC learner permit test practice", ["Victorian learner test practice", "learner permit test (LPT)", "Road to Solo Driving", "VicRoads learner permit test languages"]),
    "qld-learner-test-practice.html": ("QLD learner test practice", ["QLD written road rules test", "PrepL practice test", "PrepL final test", "Queensland learner licence"]),
    "sa-learners-test-practice.html": ("SA learners test practice", ["SA learner's theory test", "myLs practice test", "myLs test pass mark", "Service SA theory test", "SA learner's permit"]),
    "wa-learners-test-practice.html": ("WA learners test practice", ["WA learner's permit", "WA theory test", "WA supervised driving hours", "red and green P plates WA"]),
    "tas-learners-test-practice.html": ("Tasmania learners test practice", ["Plates Plus test", "Tasmanian driver knowledge test", "DKT Tasmania", "TAS learner licence"]),
    "act-learners-test-practice.html": ("ACT learners test practice", ["ACT learner licence knowledge test", "ACT knowledge test practice", "Canberra learners test", "ACT learner licence"]),
    "nt-learners-test-practice.html": ("NT learners test practice", ["NT driver knowledge test", "NT theory test", "NT learner licence", "MVR knowledge test"]),
    "faq.html": ("learner test app FAQ", ["is the learner test app official", "delete learner app account", "learner test app offline", "learner test app languages"]),
    "blog/index.html": ("learner driver guides", ["learner test tips", "road rules guides", "L plates guide"]),
    "blog/nsw-driver-knowledge-test-explained.html": ("NSW Driver Knowledge Test", ["DKT format", "DKT online", "Road User Handbook", "NSW learner licence rules"]),
    "blog/victorian-learner-permit-test-explained.html": ("Victorian learner permit test", ["VIC LPT", "learner permit course online", "hook turns", "VicRoads test languages"]),
    "blog/qld-written-road-rules-test-vs-prepl.html": ("QLD written road rules test vs PrepL", ["PrepL cost", "PrepL final test pass mark", "Queensland learner licence"]),
    "blog/give-way-rules-for-learner-drivers.html": ("give way rules", ["give way to the right", "T-intersection rules", "roundabout rules", "hook turn"]),
    "blog/how-to-use-mock-tests-and-mistakes.html": ("mock test", ["learner test practice", "DKT practice test", "learners permit test tips", "study plan"]),
    "blog/hazard-perception-test-nsw-vic-qld.html": ("hazard perception test", ["HPT NSW", "HPT VIC", "HPT QLD", "hazard perception practice"]),
    "about.html": ("about Learners Test Australia", ["original learner test questions", "how questions are checked", "BlueOrbit"]),
    "contact.html": ("learner test app support", ["report a question error", "Premium restore purchase"]),
    "privacy-policy.html": ("privacy policy", ["learner app data", "no cookies website"]),
    "cookies.html": ("cookie policy", ["advertising ID", "ad privacy choices"]),
    "terms.html": ("terms of service", ["Premium refund", "NSW governing law"]),
    "account-deletion.html": ("delete account", ["delete learner app data", "account deletion"]),
}


def seo_md(pages: list[Page]) -> str:
    out = [
        f"# SEO keyword map: {SITE_NAME} website",
        "",
        f"Base URL: {BASE} · Updated {DATE_H}. Generated by `tools/build.py` (edit `KEYWORDS` there).",
        "",
        "Rules we follow: keywords used naturally in the title (primary keyword first, then the brand), H1, intro, "
        "H2s, alt text and anchor text; no keyword stuffing; no invented statistics, ratings, reviews, user counts or "
        "pass rates; every road-rule fact traceable to the coverage maps and official sources.",
        "",
        "Language keywords (the app supports them; the site is English): learner test app in Chinese (中文), Arabic "
        "(العربية), Vietnamese (Tiếng Việt), Spanish (Español).",
        "",
        "| Page | Primary keyword | Secondary keywords | Title |",
        "|---|---|---|---|",
    ]
    for p in pages:
        if p.path not in KEYWORDS:
            continue
        prim, sec = KEYWORDS[p.path]
        out.append(f"| `{p.path}` | {prim} | {', '.join(sec)} | {p.title.replace('|', chr(92) + '|')} |")
    out += [
        "",
        "## Technical SEO checklist (verified by `tools/check_site.py`)",
        "",
        "- Unique `<title>` (≤ 60 characters) and meta description (140–160 characters) on every page.",
        "- Canonical URL (absolute), Open Graph and Twitter card tags, `robots` meta, `lang=\"en-AU\"`, viewport, theme colour.",
        "- Exactly one H1 per page; breadcrumbs (visible and BreadcrumbList JSON-LD) on inner pages.",
        "- JSON-LD: Organization, WebSite and MobileApplication (home; no ratings or reviews), FAQPage (FAQ and state "
        "pages), BlogPosting (guides), Blog (guide index), BreadcrumbList (inner pages).",
        "- sitemap.xml lists every indexable page with lastmod; robots.txt allows all crawlers (including AI crawlers) "
        "and points to the sitemap; llms.txt and llms-full.txt for AI assistants.",
        "- No third-party requests; self-hosted fonts with the heading font preloaded; one stylesheet; one tiny script.",
        "",
        "## Hosting notes",
        "",
        "- GitHub Pages serves this site at the custom domain learnertest.com (the `CNAME` file); the old address "
        "blue0orbit.github.io/learners-test-australia/ redirects here. The domain is registered at internet.bs and its DNS runs on Cloudflare (free plan, records set to DNS only).",
        "- `robots.txt`, `sitemap.xml` and `app-ads.txt` (AdMob) sit at the domain root, where crawlers look for them.",
        "- After publishing changes, run `python tools/indexnow.py` to tell Bing, Yandex, Seznam, Naver and Yep "
        "(IndexNow) which pages changed; the key file is at the site root.",
        "- `404.html` uses root-relative links because GitHub Pages serves it at any missing path.",
    ]
    return "\n".join(out) + "\n"


def main() -> None:
    pages = all_pages()
    plan = i18n.Plan(pages)  # which pages exist in which language (tools/i18n.py)
    from blog_i18n import register_blogs, localized_blogs
    blogs = register_blogs(pages, plan)
    for p in pages:
        dest = ROOT / p.path
        dest.parent.mkdir(parents=True, exist_ok=True)
        alternates = plan.alternates(p.path) if p.path in i18n.PAGES or p.path.startswith('blog/') else None
        dest.write_text(render(p, alternates=alternates, menu_links=plan.menu_links(p.path)), encoding="utf-8",
                        newline="\n")
    # Translated pages: the language folders are rewritten from scratch, so a page whose translation fell behind the
    # English disappears instead of going stale.
    for lang in i18n.LANGS:
        folder = ROOT / lang
        if folder.exists():
            for old in folder.glob("*.html"):
                old.unlink()
    localized = plan.localized() + localized_blogs(blogs, plan)
    for lp, doc in localized:
        dest = ROOT / lp.path
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(doc, encoding="utf-8", newline="\n")
    for lang in i18n.LANGS:
        todo = plan.missing[lang]
        print(f"  {lang}: {len(plan.built[lang])}/{len(i18n.PAGES)+len(blogs)} pages translated"
              + (f" ({sum(todo.values())} segments missing)" if todo else ""))
    (ROOT / "sitemap.xml").write_text(sitemap_xml(pages + [lp for lp, _ in localized]), encoding="utf-8", newline="\n")
    (ROOT / "robots.txt").write_text(robots_txt(), encoding="utf-8", newline="\n")
    (ROOT / "llms.txt").write_text(llms_txt(pages, [lp for lp, _ in localized]), encoding="utf-8", newline="\n")
    (ROOT / "llms-full.txt").write_text(llms_full_txt(pages), encoding="utf-8", newline="\n")
    (ROOT / "site.webmanifest").write_text(manifest(), encoding="utf-8", newline="\n")
    (ROOT / ".nojekyll").write_text("", encoding="utf-8")
    (ROOT / "CNAME").write_text(BASE.split("//")[1].rstrip("/") + "\n", encoding="utf-8", newline="\n")
    (ROOT / f"{INDEXNOW_KEY}.txt").write_text(INDEXNOW_KEY + "\n", encoding="utf-8", newline="\n")
    (ROOT / "app-ads.txt").write_text(f"google.com, {ADMOB_PUBLISHER}, DIRECT, f08c47fec0942fa0\n", encoding="utf-8", newline="\n")
    (ROOT / "assets" / "img" / "favicon.svg").write_text(favicon_svg(), encoding="utf-8", newline="\n")
    (ROOT / "SEO.md").write_text(seo_md(pages), encoding="utf-8", newline="\n")
    print(f"Built {len(pages)} English and {len(localized)} translated pages into {ROOT}")


if __name__ == "__main__":
    main()
