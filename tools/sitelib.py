"""Shared layout, components and structured data for the Learners Test Australia website.

Pages are plain Python objects rendered to static HTML by tools/build.py. Inside page bodies,
links to other pages are written as "@/path" (site-root relative); render() rewrites them to
relative URLs for the page's depth, so the site works under the GitHub Pages sub-path and from
a local folder alike.
"""
from __future__ import annotations

import html
import json
import re
from dataclasses import dataclass, field

SITE_NAME = "Learners Test Australia"
APP_NAME = "Learners Test Australia: DKT"
PACKAGE = "com.blueorbit.learnerstestau"
DEVELOPER = "BlueOrbit"
EMAIL = "blue0orbit@gmail.com"
BASE = "https://blue0orbit.github.io/learners-test-australia/"
BASE_PATH = "/learners-test-australia/"
DATE = "2026-09-30"
DATE_H = "30 September 2026"
PRICE = "A$5.99"
DISCLAIMER = (
    "Learners Test Australia is an independent study app. It is not affiliated with, or endorsed by, "
    "Transport for NSW, Service NSW, VicRoads, Transport Victoria, Queensland TMR or any government agency."
)

# Official sources (all verbatim from the app's packs, the Play listing or the coverage maps).
SRC = {
    "nsw_dkt": "https://www.nsw.gov.au/driving-boating-and-transport/driving-nsw/driver-and-rider-licences/driver-licences/driver-licence-tests/driver-knowledge-test",
    "nsw_learner": "https://www.nsw.gov.au/driving-boating-and-transport/driving-nsw/driver-and-rider-licences/driver-licences/learner-driver-licence",
    "nsw_ruh": "https://www.nsw.gov.au/driving-boating-and-transport/roads-safety-and-rules/safety-updates-for-nsw-road-users/road-user-handbook",
    "nsw_hpt": "https://www.nsw.gov.au/driving-boating-and-transport/driving-nsw/driver-and-rider-licences/driver-licences/driver-licence-tests/hazard-perception-test",
    "nsw_driving_test": "https://www.nsw.gov.au/driving-boating-and-transport/driving-nsw/driver-and-rider-licences/driver-licences/driver-licence-tests/driving-test",
    "vic_lpt": "https://www.vicroads.vic.gov.au/ls-and-ps/getting-your-ls/learner-permit-test",
    "vic_hpt": "https://www.vicroads.vic.gov.au/ls-and-ps/getting-your-ps/hazard-perception-test",
    "vic_prepare_l": "https://transport.vic.gov.au/road-and-active-transport/registration-and-licensing/licences/learner-permit/prepare-for-your-learner-permit",
    "vic_prepare_p": "https://transport.vic.gov.au/road-and-active-transport/registration-and-licensing/licences/probationary-licence/prepare-for-your-probationary-licence",
    "vic_handbooks": "https://transport.vic.gov.au/road-and-active-transport/registration-and-licensing/licences/driver-history-handbooks-and-logbooks/driver-handbooks-and-logbooks",
    "vic_lp_rules": "https://transport.vic.gov.au/road-and-active-transport/road-rules-and-safety/learner-and-probationary-driver-road-rules",
    "vic_gls": "https://transport.vic.gov.au/road-and-active-transport/road-rules-and-safety/victorias-graduated-licensing-system",
    "qld_tests": "https://www.qld.gov.au/transport/licensing/getting/tests",
    "qld_prepl": "https://www.qld.gov.au/transport/licensing/getting/learner/prepl/prepl/prepl-online-learning-and-assessment",
    "qld_getting_learner": "https://www.qld.gov.au/transport/licensing/getting/learner/getting-a-learner-licence",
    "qld_learner_rules": "https://www.qld.gov.au/transport/licensing/getting/rules",
    "qld_logbook": "https://www.qld.gov.au/transport/licensing/getting/learner-logbook",
    "qld_progression": "https://www.qld.gov.au/transport/licensing/driver-licensing/applying/driver-licence-progression",
    "qld_handbook": "https://www.publications.qld.gov.au/dataset/your-keys-to-driving-in-queensland",
    "qld_give_way": "https://www.qld.gov.au/transport/safety/rules/road/give-way",
    "qld_roundabouts": "https://www.qld.gov.au/transport/safety/rules/road/roundabouts",
    "gh_pages_data": "https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages",
}

NAV = [
    ("features", "Features", "features.html"),
    ("states", "States", "states.html"),
    ("blog", "Guides", "blog/"),
    ("faq", "FAQ", "faq.html"),
    ("about", "About", "about.html"),
    ("contact", "Contact", "contact.html"),
]

ORG_ID = BASE + "#organization"
SITE_ID = BASE + "#website"
APP_ID = BASE + "#app"


def esc(s: str) -> str:
    return html.escape(s, quote=True)


def strip_tags(s: str) -> str:
    s = re.sub(r"<br\s*/?>", " ", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = html.unescape(s)
    return re.sub(r"\s+", " ", s).strip()


def organization(full: bool = True) -> dict:
    org = {
        "@type": "Organization",
        "@id": ORG_ID,
        "name": DEVELOPER,
        "url": BASE,
        "logo": {"@type": "ImageObject", "url": BASE + "assets/img/logo-plate.png", "width": 512, "height": 512},
    }
    if full:
        org["email"] = EMAIL
        org["contactPoint"] = {
            "@type": "ContactPoint",
            "contactType": "customer support",
            "email": EMAIL,
            "availableLanguage": ["English"],
        }
    return org


def mobile_application() -> dict:
    return {
        "@type": "MobileApplication",
        "@id": APP_ID,
        "name": APP_NAME,
        "alternateName": SITE_NAME,
        "description": (
            "Learners Test Australia is an Android study app by BlueOrbit for learner drivers in New South Wales, "
            "Victoria and Queensland. It has practice questions and mock tests in each state's knowledge test format, "
            "with every answer explained and linked to the handbook page or road rule it comes from."
        ),
        "operatingSystem": "Android",
        "applicationCategory": "EducationalApplication",
        "inLanguage": ["en", "zh-Hans", "ar", "vi", "es"],
        "url": BASE,
        "image": BASE + "assets/img/icon-512.png",
        "author": {"@id": ORG_ID},
        "publisher": {"@id": ORG_ID},
        "featureList": [
            "NSW Driver Knowledge Test practice (45 questions in two sections)",
            "Victorian learner permit test practice (32 questions)",
            "Queensland written road rules test (30 questions in two sections) and PrepL final test (30 questions) practice",
            "Explained answers with handbook page or road rule references",
            "Daily study plan with spaced reviews",
            "Progress tracking and an estimated pass chance",
            "Hazard perception practice with still traffic scenes",
            "English, Simplified Chinese, Arabic, Vietnamese and Spanish",
            "Dark mode",
        ],
        "offers": [
            {
                "@type": "Offer",
                "name": "Free download",
                "price": "0",
                "priceCurrency": "AUD",
                "description": "Free to download. Every practice question is free. One free mock test a day, and another by watching a short ad. Contains ads and an optional in-app purchase.",
            },
            {
                "@type": "Offer",
                "name": "Premium (one-time in-app purchase)",
                "price": "5.99",
                "priceCurrency": "AUD",
                "description": "One-time purchase, no subscription: no ads, unlimited mock tests, section forecasts and weak spots, and hazard perception practice, for every state.",
            },
        ],
    }


def breadcrumb_ld(crumbs: list[tuple[str, str]]) -> dict:
    items = []
    for i, (name, path) in enumerate(crumbs, start=1):
        items.append({"@type": "ListItem", "position": i, "name": name, "item": BASE + path})
    return {"@type": "BreadcrumbList", "itemListElement": items}


def faq_ld(items: list[tuple[str, str]]) -> dict:
    return {
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": strip_tags(q), "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}}
            for q, a in items
        ],
    }


# ── Icons (24 x 24, stroke = currentColor) ───────────────────────────────────────────────────
_ICONS = {
    "map": '<path d="M9 4 3 6.5v13L9 17l6 2.5 6-2.5v-13L15 6.5 9 4Z"/><path d="M9 4v13M15 6.5v13"/>',
    "list": '<rect x="4" y="3.5" width="16" height="17" rx="2.5"/><path d="M8 8.5h8M8 12h8M8 15.5h5"/>',
    "book": '<path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H20v15H6.5A2.5 2.5 0 0 0 4 20.5v-15Z"/><path d="M4 20.5A2.5 2.5 0 0 1 6.5 18H20v3H6.5"/><path d="M9 7.5h7"/>',
    "calendar": '<rect x="3.5" y="5" width="17" height="15.5" rx="2.5"/><path d="M3.5 10h17M8 3v4M16 3v4"/><path d="m9 15 2 2 4-4"/>',
    "chart": '<path d="M4 20V4M4 20h16"/><path d="M8 16v-4M12 16V8M16 16v-6"/>',
    "eye": '<path d="M2.5 12S6 5.5 12 5.5 21.5 12 21.5 12 18 18.5 12 18.5 2.5 12 2.5 12Z"/><circle cx="12" cy="12" r="3"/>',
    "globe": '<circle cx="12" cy="12" r="8.5"/><path d="M3.5 12h17M12 3.5c2.5 2.6 3.5 5.4 3.5 8.5s-1 5.9-3.5 8.5c-2.5-2.6-3.5-5.4-3.5-8.5s1-5.9 3.5-8.5Z"/>',
    "moon": '<path d="M20 14.5A8 8 0 0 1 9.5 4a8 8 0 1 0 10.5 10.5Z"/>',
    "offline": '<path d="M3 3l18 18"/><path d="M8.5 16.5a5 5 0 0 1 7 0M5 12.5a10 10 0 0 1 4-2.3M19 12.5a10 10 0 0 0-3.2-2M1.5 8.5a15 15 0 0 1 4.3-2.8M22.5 8.5A15 15 0 0 0 11 5"/><circle cx="12" cy="19.5" r=".8"/>',
    "check": '<path d="m5 12.5 4.5 4.5L19 7.5"/>',
    "shield": '<path d="M12 3 4.5 6v5.5c0 4.5 3.2 8.2 7.5 9.5 4.3-1.3 7.5-5 7.5-9.5V6L12 3Z"/><path d="m9 12 2 2 4-4"/>',
    "mail": '<rect x="3" y="5" width="18" height="14" rx="2.5"/><path d="m4 7 8 6 8-6"/>',
    "flag": '<path d="M5 21V4M5 4h11l-2 4 2 4H5"/>',
    "bell": '<path d="M6 16V11a6 6 0 1 1 12 0v5l1.5 2h-15L6 16Z"/><path d="M10 20.5a2 2 0 0 0 4 0"/>',
    "phone": '<rect x="7" y="2.5" width="10" height="19" rx="2.5"/><path d="M11 18.5h2"/>',
    "star": '<path d="m12 3.5 2.6 5.3 5.9.9-4.3 4.1 1 5.8L12 16.9l-5.2 2.7 1-5.8-4.3-4.1 5.9-.9L12 3.5Z"/>',
    "route": '<circle cx="6" cy="18" r="2.5"/><circle cx="18" cy="6" r="2.5"/><path d="M8.5 18H15a3 3 0 0 0 0-6H9a3 3 0 0 1 0-6h6.5"/>',
    "text": '<path d="M4 6V4.5h11V6M9.5 4.5v15M7.5 19.5h4"/><path d="M14 12v-1h6v1M17 11v8.5M16 19.5h2"/>',
    "clock": '<circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 2"/>',
    "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "external": '<path d="M14 4h6v6M20 4l-9 9"/><path d="M18 14v4.5a1.5 1.5 0 0 1-1.5 1.5h-11A1.5 1.5 0 0 1 4 18.5v-11A1.5 1.5 0 0 1 5.5 6H10"/>',
}


def icon(name: str, cls: str = "icon") -> str:
    return (
        f'<svg class="{cls}" viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" '
        f'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">'
        f"{_ICONS[name]}</svg>"
    )


PLATE_SVG = (
    '<svg class="plate-mark" viewBox="0 0 64 64" width="{s}" height="{s}" aria-hidden="true" focusable="false">'
    '<rect x="2" y="2" width="60" height="60" rx="12" fill="#FFC72C"/>'
    '<rect x="7.5" y="7.5" width="49" height="49" rx="8.5" fill="none" stroke="#12161D" stroke-width="3"/>'
    '<path d="M20 15h9v25.5h15V49H20z" fill="#12161D"/></svg>'
)


def plate_svg(size: int = 36) -> str:
    return PLATE_SVG.format(s=size)


# ── Components ───────────────────────────────────────────────────────────────────────────────
def chip(code: str) -> str:
    return f'<span class="plate-chip">{esc(code)}</span>'


def ext(url: str, text: str) -> str:
    """External link to an official source; opens in the same tab (no target) to keep things simple."""
    return f'<a href="{esc(url)}" rel="noopener">{text}<span class="visually-hidden"> (official website)</span></a>'


_soon_count = [0]


def coming_soon(extra_cls: str = "", beside: str = "") -> str:
    """A disabled, non-link 'Coming soon' control. There is deliberately no store link or Play badge.
    `beside` is optional HTML (e.g. a secondary button) shown next to it."""
    _soon_count[0] += 1
    nid = f"soon-note-{_soon_count[0]}"
    return (
        f'<div class="store-soon {extra_cls}"><div class="btn-row">'
        f'<button type="button" class="btn btn-soon" disabled aria-describedby="{nid}">'
        f'{icon("phone")}<span>Coming soon to Google Play</span></button>{beside}</div>'
        f'<p id="{nid}" class="store-soon-note">Android app. Not on Google Play yet: we will add the link here when it is.</p>'
        f"</div>"
    )


def source_box(links: list[tuple[str, str]], note: str | None = None, title: str = "Check the official source") -> str:
    items = "".join(f"<li>{ext(u, t)}</li>" for t, u in links)
    note_html = f"<p>{note}</p>" if note else ""
    return (
        f'<aside class="source-box" aria-labelledby="src-title">'
        f'<h2 id="src-title" class="source-title">{icon("flag")}{esc(title)}</h2>'
        f"{note_html}<ul>{items}</ul>"
        f'<p class="source-small">Rules and test formats change. We checked these pages on {DATE_H}; '
        f"the official website is always the final word.</p></aside>"
    )


def faq_block(items: list[tuple[str, str]], heading: str = "Frequently asked questions", hid: str = "faq") -> str:
    parts = [f'<section class="faq" aria-labelledby="{hid}"><h2 id="{hid}">{esc(heading)}</h2>']
    for q, a in items:
        parts.append(f'<details><summary><h3 class="faq-q">{q}</h3></summary><div class="faq-a">{a}</div></details>')
    parts.append("</section>")
    return "".join(parts)


def updated_line() -> str:
    return f'<p class="meta">Last updated: <time datetime="{DATE}">{DATE_H}</time></p>'


def breadcrumbs_html(crumbs: list[tuple[str, str]]) -> str:
    lis = []
    for i, (name, path) in enumerate(crumbs):
        if i == len(crumbs) - 1:
            lis.append(f'<li><span aria-current="page">{esc(name)}</span></li>')
        else:
            href = "@/" + path
            lis.append(f'<li><a href="{href}">{esc(name)}</a></li>')
    return f'<nav class="breadcrumbs" aria-label="Breadcrumb"><ol>{"".join(lis)}</ol></nav>'


def page_head(h1: str, lead: str | None, crumbs: list[tuple[str, str]], meta_html: str | None = None,
              eyebrow: str | None = None) -> str:
    eb = f'<p class="eyebrow">{eyebrow}</p>' if eyebrow else ""
    ld = f'<p class="lead">{lead}</p>' if lead else ""
    mh = meta_html if meta_html is not None else updated_line()
    return (
        f'<div class="page-head"><div class="container">{breadcrumbs_html(crumbs)}{eb}'
        f"<h1>{h1}</h1>{ld}{mh}</div></div>"
    )


# ── Page model and rendering ─────────────────────────────────────────────────────────────────
@dataclass
class Page:
    path: str  # e.g. "index.html", "blog/index.html"
    title: str
    description: str
    body: str
    nav: str | None = None
    crumbs: list[tuple[str, str]] = field(default_factory=list)  # [(name, path)], path "" = home
    jsonld: list[dict] = field(default_factory=list)
    og_type: str = "website"
    noindex: bool = False
    priority: str = "0.6"
    changefreq: str = "monthly"
    llms: bool = False  # include in llms-full.txt
    llms_title: str | None = None
    llms_note: str | None = None  # one-line description for llms.txt
    article: dict | None = None  # published/modified times for og:article

    @property
    def depth(self) -> int:
        return self.path.count("/")

    @property
    def url_path(self) -> str:
        if self.path == "index.html":
            return ""
        if self.path.endswith("/index.html"):
            return self.path[: -len("index.html")]
        return self.path

    @property
    def canonical(self) -> str:
        return BASE + self.url_path


def _prefix(page: Page) -> str:
    if page.path == "404.html":
        return BASE_PATH
    return "../" * page.depth


def relink(s: str, page: Page) -> str:
    p = _prefix(page)
    home = p if p else "./"
    s = s.replace('="@/"', f'="{home}"')
    return s.replace('="@/', f'="{p}')


def header_html(page: Page) -> str:
    items = []
    for key, label, path in NAV:
        cur = ' aria-current="page"' if page.nav == key else ""
        items.append(f'<li><a href="@/{path}"{cur}>{label}</a></li>')
    return (
        '<header class="site-header on-dark"><div class="container header-inner">'
        f'<a class="brand" href="@/">{plate_svg(34)}<span class="brand-text">Learners Test '
        '<span class="brand-accent">Australia</span></span></a>'
        '<button type="button" class="nav-toggle" aria-expanded="false" aria-controls="site-nav">'
        '<span class="nav-toggle-bars" aria-hidden="true"></span><span class="nav-toggle-label">Menu</span></button>'
        f'<nav id="site-nav" class="site-nav" aria-label="Main"><ul>{"".join(items)}</ul></nav>'
        "</div></header>"
    )


def footer_html() -> str:
    return f"""<footer class="site-footer on-dark">
<div class="container footer-grid">
  <div class="footer-brand">
    <a class="brand" href="@/">{plate_svg(34)}<span class="brand-text">Learners Test <span class="brand-accent">Australia</span></span></a>
    <p>Learner test practice for NSW, VIC and QLD. An Android app by {DEVELOPER}.</p>
    <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
  </div>
  <nav class="footer-col" aria-label="The app">
    <h2 class="footer-h">The app</h2>
    <ul>
      <li><a href="@/features.html">Features</a></li>
      <li><a href="@/states.html">States</a></li>
      <li><a href="@/nsw-dkt-practice-test.html">NSW DKT practice</a></li>
      <li><a href="@/vic-learner-permit-test-practice.html">VIC learner permit test</a></li>
      <li><a href="@/qld-learner-test-practice.html">QLD learner test</a></li>
    </ul>
  </nav>
  <nav class="footer-col" aria-label="Learn">
    <h2 class="footer-h">Learn</h2>
    <ul>
      <li><a href="@/blog/">Guides</a></li>
      <li><a href="@/blog/give-way-rules-for-learner-drivers.html">Give way rules</a></li>
      <li><a href="@/blog/hazard-perception-test-nsw-vic-qld.html">Hazard perception</a></li>
      <li><a href="@/about.html">About</a></li>
    </ul>
  </nav>
  <nav class="footer-col" aria-label="Legal and support">
    <h2 class="footer-h">Legal and support</h2>
    <ul>
      <li><a href="@/privacy-policy.html">Privacy</a></li>
      <li><a href="@/cookies.html">Cookies</a></li>
      <li><a href="@/terms.html">Terms</a></li>
      <li><a href="@/account-deletion.html">Delete account</a></li>
      <li><a href="@/faq.html">FAQ</a></li>
      <li><a href="@/contact.html">Contact</a></li>
    </ul>
  </nav>
</div>
<div class="container"><div class="footer-legal">
  <p class="disclaimer">{DISCLAIMER}</p>
  <p>&copy; 2026 {DEVELOPER}. Fonts: <a href="@/assets/fonts/OFL-Overpass.txt">Overpass</a> and
  <a href="@/assets/fonts/OFL-AtkinsonHyperlegibleNext.txt">Atkinson Hyperlegible Next</a>, used under the SIL Open Font License 1.1.</p>
</div></div>
</footer>"""


def render(page: Page) -> str:
    p = page
    robots = "noindex,follow" if p.noindex else "index,follow"
    og_img = BASE + "assets/img/og-image.png"
    ld_nodes = list(p.jsonld)
    if p.crumbs and len(p.crumbs) > 1:
        ld_nodes.append(breadcrumb_ld(p.crumbs))
    ld_html = ""
    if ld_nodes:
        graph = {"@context": "https://schema.org", "@graph": ld_nodes}
        ld_html = '<script type="application/ld+json">' + json.dumps(graph, ensure_ascii=False, indent=1) + "</script>\n"
    canonical = "" if p.noindex else f'<link rel="canonical" href="{esc(p.canonical)}">\n'
    article_meta = ""
    if p.article:
        article_meta = (
            f'<meta property="article:published_time" content="{p.article["published"]}">\n'
            f'<meta property="article:modified_time" content="{p.article["modified"]}">\n'
            f'<meta property="article:author" content="{DEVELOPER}">\n'
        )
    head = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(p.title)}</title>
<meta name="description" content="{esc(p.description)}">
<meta name="robots" content="{robots}">
{canonical}<meta name="theme-color" content="#12161D">
<meta name="color-scheme" content="light dark">
<meta name="author" content="{DEVELOPER}">
<link rel="preload" href="@/assets/fonts/overpass.ttf" as="font" type="font/ttf" crossorigin>
<link rel="stylesheet" href="@/assets/css/site.css">
<link rel="icon" href="@/favicon.ico" sizes="any">
<link rel="icon" href="@/assets/img/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="@/assets/img/apple-touch-icon.png">
<link rel="manifest" href="@/site.webmanifest">
<meta property="og:type" content="{p.og_type}">
<meta property="og:site_name" content="{SITE_NAME}">
<meta property="og:locale" content="en_AU">
<meta property="og:title" content="{esc(p.title)}">
<meta property="og:description" content="{esc(p.description)}">
<meta property="og:url" content="{esc(p.canonical)}">
<meta property="og:image" content="{og_img}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Learners Test Australia logo, a yellow learner plate with a black L, and the words: learner test practice for NSW, VIC and QLD">
{article_meta}<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(p.title)}">
<meta name="twitter:description" content="{esc(p.description)}">
<meta name="twitter:image" content="{og_img}">
<meta name="twitter:image:alt" content="Learners Test Australia logo and tagline">
<script>document.documentElement.classList.add('js')</script>
<script src="@/assets/js/site.js" defer></script>
{ld_html}</head>
<body>
<a class="skip-link" href="#main">Skip to main content</a>
"""
    out = head + header_html(p) + '\n<main id="main" tabindex="-1">\n' + p.body + "\n</main>\n" + footer_html() + "\n</body>\n</html>\n"
    return relink(out, p)


def words(s: str) -> int:
    return len(strip_tags(s).split())
