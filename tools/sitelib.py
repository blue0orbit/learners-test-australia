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
BASE = "https://learnertest.com/"
BASE_PATH = "/"
# AdMob publisher id, published in app-ads.txt (it is public by design)
ADMOB_PUBLISHER = "pub-1798960414758701"
# IndexNow key (public by design): the key file at the site root proves we own the URLs we submit
INDEXNOW_KEY = "02adf338491ab11d8179dbdec8da3278"
# Google Play listing. None until the app is public: then store buttons show "Coming soon" with no link.
PLAY_URL: str | None = None
# Our other app (same developer), linked from the footer, about and download pages
DTT_URL = "https://dttireland.com/"
DTT_PLAY = "https://play.google.com/store/apps/details?id=com.app.dttireland"
DATE = "2026-09-30"
DATE_H = "30 September 2026"
PRICE = "A$5.99"
DISCLAIMER = (
    "Learners Test Australia is an independent study app. It is not affiliated with, endorsed by or connected to "
    "any Australian state or territory government, licensing authority or other government agency."
)
# The eight states and territories, in the order the site lists them: (code, name, page).
STATES = [
    ("NSW", "New South Wales", "nsw-dkt-practice-test.html"),
    ("VIC", "Victoria", "vic-learner-permit-test-practice.html"),
    ("QLD", "Queensland", "qld-learner-test-practice.html"),
    ("SA", "South Australia", "sa-learners-test-practice.html"),
    ("WA", "Western Australia", "wa-learners-test-practice.html"),
    ("TAS", "Tasmania", "tas-learners-test-practice.html"),
    ("ACT", "Australian Capital Territory", "act-learners-test-practice.html"),
    ("NT", "Northern Territory", "nt-learners-test-practice.html"),
]

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
    # SA, WA, TAS, ACT and NT: URLs as recorded in the app's coverage maps and packs (content-src/coverage/*.md).
    "sa_myls": "https://www.sa.gov.au/topics/driving-and-transport/licences/learners-permit/apply/myls-course-and-theory-test",
    "sa_theory_test": "https://www.sa.gov.au/topics/driving-and-transport/licences/learners-permit/apply/study-and-theory-test-offline",
    "sa_conditions": "https://www.sa.gov.au/topics/driving-and-transport/licences/licence-details/licence-conditions",
    "sa_handbook": "https://www.mylicence.sa.gov.au/road-rules/the-drivers-handbook",
    "sa_learners_stage": "https://www.mylicence.sa.gov.au/my-car-licence/learners-stage",
    "wa_rtc": "https://www.legislation.wa.gov.au/legislation/statutes.nsf/law_s257.html",
    "wa_atdr": "https://www.legislation.wa.gov.au/legislation/statutes.nsf/law_s45436.html",
    "wa_atda": "https://www.legislation.wa.gov.au/legislation/statutes.nsf/law_a146691.html",
    "wa_dtmi": "https://www.transport.wa.gov.au/",
    "tas_pp_learner": "https://www.platesplus.tas.gov.au/getting_your_learner_licence",
    "tas_pp_faq": "https://www.platesplus.tas.gov.au/frequently_asked_questions/course_frequently_asked_questions",
    "tas_pp_hpt": "https://www.platesplus.tas.gov.au/frequently_asked_questions/hpt_frequently_asked_questions",
    "tas_st_test": "https://www.service.tas.gov.au/services/transport/driver-and-rider-licences/complete-a-learner-driver-licence-knowledge-test/",
    "tas_dlvr": "https://www.legislation.tas.gov.au/view/html/inforce/current/sr-2021-026",
    "act_learner": "https://www.accesscanberra.act.gov.au/driving-transport-and-parking/licences/get-your-learner-driver-licence",
    "act_prov": "https://www.accesscanberra.act.gov.au/driving-transport-and-parking/licences/get-your-provisional-driver-licence",
    "act_dlr": "https://www.legislation.act.gov.au/sl/2000-14/",
    "act_rrr": "https://www.legislation.act.gov.au/sl/2017-43/",
    "nt_licence": "https://nt.gov.au/driving/licence/getting-an-nt-licence/get-your-driver-licence",
    "nt_practical": "https://nt.gov.au/driving/licence/getting-an-nt-licence/get-your-driver-licence/take-a-practical-driving-test-with-an-authorised-driving-examiner",
    "nt_mva": "https://legislation.nt.gov.au/Legislation/MOTOR-VEHICLES-ACT-1949",
    "nt_tr": "https://legislation.nt.gov.au/Legislation/TRAFFIC-REGULATIONS-1999",
    "gh_pages_data": "https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages",
}

# Website languages: the app's five. The key is the URL folder (English lives at the root). Every translated page is
# marked for readers in Australia (hreflang language-AU), and English is the x-default.
LOCALES = {
    "en": {"hreflang": "en-AU", "dir": "ltr", "og": "en_AU", "name": "English", "label": "Language"},
    "zh": {"hreflang": "zh-Hans-AU", "dir": "ltr", "og": "zh_CN", "name": "中文", "label": "语言"},
    "ar": {"hreflang": "ar-AU", "dir": "rtl", "og": "ar_AR", "name": "العربية", "label": "اللغة"},
    "vi": {"hreflang": "vi-AU", "dir": "ltr", "og": "vi_VN", "name": "Tiếng Việt", "label": "Ngôn ngữ"},
    "es": {"hreflang": "es-AU", "dir": "ltr", "og": "es_LA", "name": "Español", "label": "Idioma"},
}

NAV = [
    ("features", "Features", "features.html"),
    ("states", "States", "states.html"),
    ("blog", "Guides", "blog/"),
    ("faq", "FAQ", "faq.html"),
    ("about", "About", "about.html"),
    ("contact", "Contact", "contact.html"),
    ("download", "Download", "download.html"),
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
            "Learners Test Australia is an Android study app by BlueOrbit for learner drivers in all eight Australian "
            "states and territories. It has practice questions and mock tests in each state's knowledge test format, "
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
            "South Australian learner's theory test (8 give-way questions, then 42) and myLs test (30 questions) practice",
            "Western Australian learner's permit practice test (30 questions)",
            "Tasmanian driver knowledge test practice (30 questions, some with more than one correct answer)",
            "ACT learner licence knowledge test practice (35 questions)",
            "Northern Territory driver knowledge test practice (30 questions)",
            "Explained answers with handbook page or road rule references",
            "Daily study plan with spaced reviews",
            "Progress tracking and an estimated pass chance",
            "Hazard perception practice: 72 real-time 3D driving clips and still traffic scenes",
            "English, Simplified Chinese, Arabic, Vietnamese and Spanish",
            "Dark mode",
        ],
        **({"downloadUrl": PLAY_URL, "installUrl": PLAY_URL} if PLAY_URL else {}),
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


def dtt_application() -> dict:
    """Our other app, by the same developer (see the about page)."""
    return {
        "@type": "MobileApplication",
        "@id": DTT_URL + "#app",
        "name": "DTT Ireland",
        "description": "Practice app for the Irish driver theory test, for car and motorcycle learners, by BlueOrbit.",
        "operatingSystem": "Android",
        "applicationCategory": "EducationalApplication",
        "url": DTT_URL,
        "installUrl": DTT_PLAY,
        "author": {"@id": ORG_ID},
        "publisher": {"@id": ORG_ID},
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
    '<path d="M6.4 18.6 6.3 17.5 6.4 16.5 6.7 15.5 7.1 14.5 7.7 13.6 8.3 12.9 9.2 12.2 10.1 11.7 11.0 11.3 12.1 11.1 40.3 7.1 41.4 7.0 42.4 7.1 43.4 7.4 44.4 7.8 45.3 8.4 46.1 9.1 46.7 9.9 47.3 10.8 47.6 11.7 47.9 12.8 51.9 41.0 51.9 42.1 51.8 43.1 51.6 44.1 51.1 45.1 50.6 46.0 49.9 46.8 49.1 47.4 48.2 48.0 47.2 48.4 46.2 48.6 17.9 52.6 16.8 52.6 15.8 52.5 14.8 52.3 13.8 51.8 12.9 51.3 12.2 50.6 11.5 49.8 11.0 48.9 10.6 47.9 10.4 46.9Z" fill="#FFB52B"/>'
    '<path d="M9.6 19.1 9.6 18.4 9.6 17.7 9.8 17.0 10.1 16.4 10.5 15.8 10.9 15.2 11.5 14.8 12.1 14.4 12.7 14.2 13.4 14.0 39.8 10.3 40.5 10.3 41.2 10.4 41.9 10.5 42.6 10.8 43.2 11.2 43.7 11.6 44.1 12.2 44.5 12.8 44.7 13.4 44.9 14.1 48.6 40.6 48.7 41.3 48.6 42.0 48.4 42.6 48.1 43.3 47.8 43.9 47.3 44.4 46.7 44.8 46.1 45.2 45.5 45.4 44.8 45.6 18.4 49.3 17.7 49.4 17.0 49.3 16.3 49.1 15.7 48.8 15.1 48.5 14.5 48.0 14.1 47.5 13.7 46.8 13.5 46.2 13.3 45.5Z" fill="none" stroke="#12161D" stroke-width="2.1" stroke-linejoin="round"/>'
    '<path d="M15.9 18.2 23.9 17.1 26.4 34.8 38.4 33.1 39.5 40.5 19.5 43.3Z" fill="#12161D"/>'
    '<circle cx="50.1" cy="45.6" r="10.4" fill="#12161D"/>'
    '<circle cx="50.1" cy="45.6" r="8.3" fill="#1FA45A"/>'
    '<path d="M45.0 46.9 48.9 51.0 55.5 43.3 53.4 41.5 48.8 46.9 47.0 45.0Z" fill="#FFFFFF"/></svg>'
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
    if PLAY_URL:
        return (
            f'<div class="store-soon {extra_cls}"><div class="btn-row">'
            f'<a class="btn btn-primary" href="{esc(PLAY_URL)}" rel="noopener" aria-describedby="{nid}">'
            f'{icon("phone")}<span>Get it on Google Play</span></a>{beside}</div>'
            f'<p id="{nid}" class="store-soon-note">Free Android app, for Android 8.0 or later.</p>'
            f"</div>"
        )
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
    image_path: str = "assets/img/og-image.png"
    image_alt: str = "Learners Test Australia logo and tagline"
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
        f'<a class="brand" href="@/" translate="no">{plate_svg(34)}<span class="brand-text">Learners Test '
        '<span class="brand-accent">Australia</span></span></a>'
        "<!--LANG-SWITCH-->"
        '<button type="button" class="nav-toggle" aria-expanded="false" aria-controls="site-nav">'
        '<span class="nav-toggle-bars" aria-hidden="true"></span><span class="nav-toggle-label">Menu</span></button>'
        f'<nav id="site-nav" class="site-nav" aria-label="Main"><ul>{"".join(items)}</ul></nav>'
        "</div></header>"
    )


FOOTER_STATE_LINKS = [
    ("NSW DKT practice", "nsw-dkt-practice-test.html"),
    ("VIC learner permit test", "vic-learner-permit-test-practice.html"),
    ("QLD learner test", "qld-learner-test-practice.html"),
    ("SA learners test", "sa-learners-test-practice.html"),
    ("WA learners test", "wa-learners-test-practice.html"),
    ("TAS learners test", "tas-learners-test-practice.html"),
    ("ACT learners test", "act-learners-test-practice.html"),
    ("NT learners test", "nt-learners-test-practice.html"),
]


def footer_html() -> str:
    state_lis = "\n".join(f'      <li><a href="@/{p}">{t}</a></li>' for t, p in FOOTER_STATE_LINKS)
    return f"""<footer class="site-footer on-dark">
<div class="container footer-grid">
  <div class="footer-brand">
    <a class="brand" href="@/" translate="no">{plate_svg(34)}<span class="brand-text">Learners Test <span class="brand-accent">Australia</span></span></a>
    <p>Learner test practice for every Australian state and territory. An Android app by {DEVELOPER}.</p>
    <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
    <p class="footer-sister">Also by {DEVELOPER}: <a href="{DTT_URL}">DTT Ireland</a>, driver theory test practice for Ireland.</p>
  </div>
  <nav class="footer-col" aria-label="States and territories">
    <h2 class="footer-h">States and territories</h2>
    <ul>
{state_lis}
    </ul>
  </nav>
  <nav class="footer-col" aria-label="The app and guides">
    <h2 class="footer-h">The app and guides</h2>
    <ul>
      <li><a href="@/features.html">Features</a></li>
      <li><a href="@/states.html">Learner tests by state</a></li>
      <li><a href="@/blog/">Guides</a></li>
      <li><a href="@/blog/give-way-rules-for-learner-drivers.html">Give way rules</a></li>
      <li><a href="@/blog/hazard-perception-test-nsw-vic-qld.html">Hazard perception</a></li>
      <li><a href="@/about.html">About</a></li>
      <li><a href="@/download.html">Download the app</a></li>
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
  <!--LANG-LIST-->
  <p class="disclaimer">{DISCLAIMER}</p>
  <p>&copy; 2026 {DEVELOPER}. Fonts: <a href="@/assets/fonts/OFL-Overpass.txt">Overpass</a> and
  <a href="@/assets/fonts/OFL-AtkinsonHyperlegibleNext.txt">Atkinson Hyperlegible Next</a>, used under the SIL Open Font License 1.1.</p>
</div></div>
</footer>"""


def page_html(page: Page) -> str:
    """Everything inside <body>: skip link, header, main and footer (with the language menu slots still empty)."""
    return ('<a class="skip-link" href="#main">Skip to main content</a>\n' + header_html(page)
            + '\n<main id="main" tabindex="-1">\n' + page.body + "\n</main>\n" + footer_html())


def lang_menus(lang: str, links: dict[str, str]) -> tuple[str, str]:
    """The header language menu and the footer language list. `links` maps each language to the site-relative path
    of this page in that language, or of that language's home page when the page isn't translated."""
    if len(links) < 2:
        return "", ""
    cur = LOCALES[lang]
    items = []
    for code, loc in LOCALES.items():
        if code not in links:
            continue
        mark = ' aria-current="true"' if code == lang else ""
        items.append(f'<li><a href="@/{links[code]}" hreflang="{loc["hreflang"]}" lang="{loc["hreflang"]}"{mark}>'
                     f'{loc["name"]}</a></li>')
    lis = "".join(items)
    switch = (f'<details class="lang-switch"><summary><span class="visually-hidden">{cur["label"]}: </span>'
              f'{icon("globe")}<span>{cur["name"]}</span></summary><ul>{lis}</ul></details>')
    footer = f'<nav class="footer-langs" aria-label="{cur["label"]}"><ul>{lis}</ul></nav>'
    return switch, footer


def render(page: Page, *, lang: str = "en", body_html: str | None = None, title: str | None = None,
           description: str | None = None, image_alt: str | None = None, ld_nodes: list[dict] | None = None,
           alternates: dict[str, str] | None = None, menu_links: dict[str, str] | None = None) -> str:
    """Render a page. English by default; tools/i18n.py passes the translated body and head texts for other languages.
    `alternates` maps language -> site-relative path of the same page in that language (hreflang); `menu_links` feeds
    the language menu (see lang_menus)."""
    p = page
    loc = LOCALES[lang]
    title = p.title if title is None else title
    description = p.description if description is None else description
    image_alt = p.image_alt if image_alt is None else image_alt
    robots = "noindex,follow" if p.noindex else "index,follow,max-image-preview:large"
    og_img = BASE + p.image_path
    if ld_nodes is None:
        ld_nodes = list(p.jsonld)
        if p.crumbs and len(p.crumbs) > 1:
            ld_nodes.append(breadcrumb_ld(p.crumbs))
    ld_html = ""
    if ld_nodes:
        graph = {"@context": "https://schema.org", "@graph": ld_nodes}
        ld_html = '<script type="application/ld+json">' + json.dumps(graph, ensure_ascii=False, indent=1) + "</script>\n"
    canonical = "" if p.noindex else f'<link rel="canonical" href="{esc(p.canonical)}">\n'
    hreflang = ""
    og_alt = ""
    if alternates and len(alternates) > 1 and not p.noindex:
        for code, path in alternates.items():
            hreflang += f'<link rel="alternate" hreflang="{LOCALES[code]["hreflang"]}" href="{esc(BASE + path)}">\n'
            if code != lang:
                og_alt += f'<meta property="og:locale:alternate" content="{LOCALES[code]["og"]}">\n'
        hreflang += f'<link rel="alternate" hreflang="x-default" href="{esc(BASE + alternates["en"])}">\n'
    article_meta = ""
    if p.article:
        article_meta = (
            f'<meta property="article:published_time" content="{p.article["published"]}">\n'
            f'<meta property="article:modified_time" content="{p.article["modified"]}">\n'
            f'<meta property="article:author" content="{DEVELOPER}">\n'
        )
    dir_attr = ' dir="rtl"' if loc["dir"] == "rtl" else ""
    head = f"""<!doctype html>
<html lang="{loc['hreflang']}"{dir_attr}>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<meta name="robots" content="{robots}">
{canonical}{hreflang}<meta name="theme-color" content="#12161D">
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
<meta property="og:locale" content="{loc['og']}">
{og_alt}<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:url" content="{esc(p.canonical)}">
<meta property="og:image" content="{og_img}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{esc(image_alt)}">
{article_meta}<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(description)}">
<meta name="twitter:image" content="{og_img}">
<meta name="twitter:image:alt" content="{esc(image_alt)}">
<script>document.documentElement.classList.add('js')</script>
<script src="@/assets/js/site.js" defer></script>
{ld_html}</head>
<body>
"""
    body = page_html(p) if body_html is None else body_html
    switch, footer_langs = lang_menus(lang, menu_links or {})
    body = body.replace("<!--LANG-SWITCH-->", switch).replace("<!--LANG-LIST-->", footer_langs)
    out = head + body + "\n</body>\n</html>\n"
    return relink(out, p)


def words(s: str) -> int:
    return len(strip_tags(s).split())
