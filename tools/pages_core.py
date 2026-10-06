"""Home, features, states hub, FAQ, about, contact and 404 pages."""
from sitelib import (
    APP_NAME, CHECKED_H, DEVELOPER, DISCLAIMER, DTT_PLAY, DTT_URL, EMAIL, PLAY_URL, PRICE, SITE_ID, SITE_NAME, SRC,
    BASE, ORG_ID, Page, chip, coming_soon, dtt_application, ext, faq_block, faq_ld, icon, mobile_application,
    organization, page_head, plate_svg, updated_line,
)

LANGS = ('English, <span class="nw" lang="zh-Hans">中文</span>, <span class="nw" lang="ar" dir="rtl">العربية</span>, '
         '<span class="nw" lang="vi">Tiếng Việt</span> and <span class="nw" lang="es">Español</span>')


# ── Decorative app mockups (always paired with a text caption) ────────────────────────────────
ROUNDABOUT_SIGN = (
    '<svg viewBox="0 0 100 88" width="84" height="74" aria-hidden="true" focusable="false">'
    '<path d="M6 6h88L50 82Z" fill="#FFFFFF" stroke="#CC3B42" stroke-width="9" stroke-linejoin="round"/>'
    '<g fill="none" stroke="#12161D" stroke-width="5" stroke-linecap="round">'
    '<path d="M38 26a14 14 0 0 1 20-2"/><path d="M63 31a14 14 0 0 1-6 18"/><path d="M47 52a14 14 0 0 1-12-15"/></g>'
    '<g fill="#12161D"><path d="m57 19 6 6-8 2z"/><path d="m61 49-8 2 2-8z"/><path d="m31 38 4-8 5 7z"/></g></svg>'
)


def mock_question() -> str:
    return f"""<figure class="mock-figure">
<div class="phone" aria-hidden="true"><div class="screen">
  <div class="scr-top"><span>{chip('NSW')} Practice</span><span class="scr-muted">3 of 20</span></div>
  <div class="scr-card"><div class="scr-sign">{ROUNDABOUT_SIGN}</div>
  <div class="scr-q">You approach a roundabout with this sign. Who must you give way to?</div></div>
  <div class="scr-opt"><span class="k">A</span><span>Only vehicles coming from your right</span></div>
  <div class="scr-opt ok"><span class="k">B</span><span>All vehicles already in the roundabout</span></div>
  <div class="scr-card scr-feedback"><div class="t">Correct</div>
  <div>Slow down or stop and give way to every vehicle already in the roundabout, whichever direction it came from.</div>
  <div class="scr-src">Source: Road User Handbook p.91–92 · NSW Road Rules 2014 r.114</div></div>
  <div class="scr-btn">Next</div>
</div></div>
<figcaption>Illustration of a practice question from the NSW pack: the answer is explained, with the handbook page and road rule it comes from.</figcaption>
</figure>"""


def mock_today() -> str:
    return f"""<figure class="mock-figure">
<div class="phone" aria-hidden="true"><div class="screen">
  <div class="scr-top"><span>Today</span>{chip('VIC')}</div>
  <div class="scr-card scr-row"><div><div class="scr-big">24</div><div class="scr-muted">days until your test</div></div>
  <div style="text-align:right"><div class="scr-big">72%</div><div class="scr-muted">pass chance</div></div></div>
  <div class="scr-card"><div class="scr-label">TODAY'S PLAN</div>
  <ul class="scr-plan">
    <li><span class="scr-dot done"></span><span><b>Quick check</b><br><span class="scr-muted">12 questions to find your starting point</span></span></li>
    <li><span class="scr-dot"></span><span><b>Reviews due</b><br><span class="scr-muted">8 questions to revisit before you forget them</span></span></li>
    <li><span class="scr-dot"></span><span><b>Fix your mistakes</b><br><span class="scr-muted">5 questions you got wrong</span></span></li>
    <li><span class="scr-dot"></span><span><b>Mock test</b><br><span class="scr-muted">32 questions, same format as the real test</span></span></li>
  </ul></div>
  <div class="scr-card scr-row"><span><b>4-day streak</b></span><span class="scr-muted">Keep it going</span></div>
</div></div>
<figcaption>Illustration of the Today screen with sample data: a countdown, an estimated pass chance and a short daily plan.</figcaption>
</figure>"""


def mock_results() -> str:
    return f"""<figure class="mock-figure">
<div class="phone" aria-hidden="true"><div class="screen">
  <div class="scr-top"><span>{chip('QLD')} Mock test</span><span class="scr-muted">Results</span></div>
  <div class="scr-card"><div class="scr-big" style="color:var(--good-text)">Passed</div>
  <div class="scr-muted">You reached the pass mark in every section.</div></div>
  <div class="scr-card"><div class="scr-label">BY SECTION</div>
    <div class="scr-row" style="margin-top:.5rem"><b>Giving way</b><span>9 of 10</span></div>
    <div class="passbar"><span class="fill" style="--v:90%"></span><span class="line" style="--p:90%"></span></div>
    <div class="scr-muted scr-src">Pass 9</div>
    <div class="scr-row" style="margin-top:.6rem"><b>Road rules</b><span>19 of 20</span></div>
    <div class="passbar"><span class="fill" style="--v:95%"></span><span class="line" style="--p:90%"></span></div>
    <div class="scr-muted scr-src">Pass 18</div>
  </div>
  <div class="scr-card scr-row"><span>1 to review</span><span class="scr-muted">12 minutes</span></div>
  <div class="scr-btn">Practise these mistakes</div>
</div></div>
<figcaption>Illustration of mock test results with sample data: each section shows your score against its pass line.</figcaption>
</figure>"""


def mock_fingerprint() -> str:
    return f"""<figure class="mock-figure">
<div class="phone" aria-hidden="true"><div class="screen">
  <div class="scr-q">Where will you take your test?</div>
  <div class="scr-row" style="flex-wrap:wrap;justify-content:flex-start">{chip('NSW')} <span class="scr-muted">VIC</span> <span class="scr-muted">QLD</span> <span class="scr-muted">SA</span> <span class="scr-muted">WA</span> <span class="scr-muted">TAS</span> <span class="scr-muted">ACT</span> <span class="scr-muted">NT</span></div>
  <div class="scr-card"><div class="scr-label">DRIVER KNOWLEDGE TEST (IN PERSON)</div>
  <ul class="scr-plan">
    <li><span class="scr-dot"></span>45 questions</li>
    <li><span class="scr-dot"></span>General knowledge: at least 12 of 15 correct</li>
    <li><span class="scr-dot"></span>Road safety: at least 29 of 30 correct</li>
    <li><span class="scr-dot"></span>No time limit</li>
    <li><span class="scr-dot"></span>The test ends early once you can no longer pass</li>
  </ul>
  <div class="scr-src">Source: nsw.gov.au · checked 5 Oct 2026</div></div>
  <div class="scr-muted scr-src">Confirm the format with your state's transport authority before your test.</div>
  <div class="scr-btn">Continue</div>
</div></div>
<figcaption>Illustration of the state picker: each state shows its test format, the source and the date it was checked.</figcaption>
</figure>"""


def mock_hazard() -> str:
    """A 3D hazard clip as it looks before you answer: only the task, never the hazard or the answer."""
    return f"""<figure class="mock-figure">
<div class="phone" aria-hidden="true"><div class="screen">
  <div class="scr-top"><span>Hazard perception</span><span class="scr-muted">3D clip</span></div>
  <div class="clip"><span class="xroad"></span><span class="road"></span><span class="ind"></span><span class="bonnet"></span></div>
  <div class="scr-card"><div class="scr-label">YOUR TASK</div>
  <div class="scr-q">Turn right</div>
  <div>Tap when it is safe to start your turn.</div></div>
  <div class="scr-muted scr-src">Tap anywhere on the clip at the moment it becomes safe.</div>
  <div class="scr-btn">Start clip</div>
</div></div>
<figcaption>Illustration of a 3D hazard perception clip: you are told what you want to do, then tap when it becomes safe.</figcaption>
</figure>"""


# ── Shared blocks ─────────────────────────────────────────────────────────────────────────────
def state_cards(heading_level: str = "h3") -> str:
    h = heading_level
    return f"""<div class="grid grid-4">
<article class="card state-card">
  <div class="state-top">{chip('NSW')}<{h}>NSW Driver Knowledge Test (DKT)</{h}></div>
  <dl>
    <dt>Questions</dt><dd>45, in two sections</dd>
    <dt>Pass marks</dt><dd>General knowledge: 12 of 15. Road safety: 29 of 30.</dd>
    <dt>In the app</dt><dd>The mock test ends where the real test would, once passing is no longer possible.</dd>
  </dl>
  <a class="card-link" href="@/nsw-dkt-practice-test.html">NSW DKT practice test {icon('arrow')}</a>
</article>
<article class="card state-card">
  <div class="state-top">{chip('VIC')}<{h}>Victorian learner permit test</{h}></div>
  <dl>
    <dt>Questions</dt><dd>32 multiple choice</dd>
    <dt>Pass mark</dt><dd>25 of 32 (78%)</dd>
    <dt>In the app</dt><dd>Victoria-only topics such as hook turns and trams are included.</dd>
  </dl>
  <a class="card-link" href="@/vic-learner-permit-test-practice.html">VIC learner permit test practice {icon('arrow')}</a>
</article>
<article class="card state-card">
  <div class="state-top">{chip('QLD')}<{h}>Queensland written test and PrepL</{h}></div>
  <dl>
    <dt>Written road rules test</dt><dd>30 questions in two sections. Giving way: 9 of 10. Road rules: 18 of 20.</dd>
    <dt>PrepL final test</dt><dd>30 questions. Pass mark: 27 of 30.</dd>
    <dt>In the app</dt><dd>Mock tests for both routes.</dd>
  </dl>
  <a class="card-link" href="@/qld-learner-test-practice.html">QLD learner test practice {icon('arrow')}</a>
</article>
<article class="card state-card">
  <div class="state-top">{chip('SA')}<{h}>SA learner's theory test and myLs</{h}></div>
  <dl>
    <dt>In person</dt><dd>8 give-way questions, all must be right, then 42. Pass mark: 32 of 42.</dd>
    <dt>myLs test</dt><dd>30 questions. Pass mark: 27 of 30.</dd>
    <dt>In the app</dt><dd>Mock tests for both routes, with select-all-that-apply questions.</dd>
  </dl>
  <a class="card-link" href="@/sa-learners-test-practice.html">SA learners test practice {icon('arrow')}</a>
</article>
<article class="card state-card">
  <div class="state-top">{chip('WA')}<{h}>WA learner's permit theory test</{h}></div>
  <dl>
    <dt>Before your permit</dt><dd>Show you know WA's traffic laws and safe driving, normally by a theory test.</dd>
    <dt>Test format</dt><dd>30 questions, 24 to pass.</dd>
    <dt>In the app</dt><dd>A 30-question practice test written from WA legislation.</dd>
  </dl>
  <a class="card-link" href="@/wa-learners-test-practice.html">WA learners test practice {icon('arrow')}</a>
</article>
<article class="card state-card">
  <div class="state-top">{chip('TAS')}<{h}>Tasmanian driver knowledge test</{h}></div>
  <dl>
    <dt>Online test</dt><dd>30 questions, after the free Plates Plus course.</dd>
    <dt>Pass mark</dt><dd>27 of 30. Some questions have more than one correct answer.</dd>
    <dt>In the app</dt><dd>30-question mocks with select-all-that-apply questions.</dd>
  </dl>
  <a class="card-link" href="@/tas-learners-test-practice.html">Tasmania learners test practice {icon('arrow')}</a>
</article>
<article class="card state-card">
  <div class="state-top">{chip('ACT')}<{h}>ACT learner licence knowledge test</{h}></div>
  <dl>
    <dt>Questions</dt><dd>35, from a bank of more than 300</dd>
    <dt>Pass mark</dt><dd>At least 31 of 35</dd>
    <dt>In the app</dt><dd>35-question practice tests. The real test is taken only through an approved course.</dd>
  </dl>
  <a class="card-link" href="@/act-learners-test-practice.html">ACT learners test practice {icon('arrow')}</a>
</article>
<article class="card state-card">
  <div class="state-top">{chip('NT')}<{h}>NT driver knowledge test</{h}></div>
  <dl>
    <dt>Questions</dt><dd>30, from a pool of more than 300</dd>
    <dt>Pass mark</dt><dd>26 of 30</dd>
    <dt>In the app</dt><dd>30-question mocks scored against the 26-question pass line.</dd>
  </dl>
  <a class="card-link" href="@/nt-learners-test-practice.html">NT learners test practice {icon('arrow')}</a>
</article>
</div>"""


ALL_STATES_TEXT = ("New South Wales, Victoria, Queensland, South Australia, Western Australia, Tasmania, the Australian "
                   "Capital Territory and the Northern Territory")


def price_table() -> str:
    return f"""<div class="table-wrap"><table class="price-table">
<caption>What is free and what Premium adds</caption>
<thead><tr><th scope="col">Feature</th><th scope="col">Free</th><th scope="col">Premium</th></tr></thead>
<tbody>
<tr><th scope="row">Every practice question, with explanations</th><td class="yes">Yes</td><td class="yes">Yes</td></tr>
<tr><th scope="row">Daily plan, reviews and progress</th><td class="yes">Yes</td><td class="yes">Yes</td></tr>
<tr><th scope="row">Estimated pass chance</th><td class="yes">Yes</td><td class="yes">Yes</td></tr>
<tr><th scope="row">Mock tests</th><td>1 a day, plus another for each short ad you choose to watch</td><td class="yes">Unlimited</td></tr>
<tr><th scope="row">Ads</th><td>Banner ads on results and guide pages</td><td class="yes">No ads</td></tr>
<tr><th scope="row">Section forecasts, weak spots and review planner</th><td class="no">No</td><td class="yes">Yes</td></tr>
<tr><th scope="row">Hazard perception practice</th><td>Sample 3D clips and scenes</td><td class="yes">All 72 clips and every scene</td></tr>
<tr><th scope="row">Price</th><td>Free</td><td>{PRICE} once. No subscription.</td></tr>
</tbody></table></div>"""


FEATURES_GRID = [
    ("map", "Your state's test, in its real format",
     "Mock tests use the same number of questions, sections and pass marks as your state's knowledge test, as published on its official website."),
    ("book", "Every answer explained",
     "Each question tells you why the answer is right and shows the handbook page or road rule it comes from."),
    ("calendar", "A plan for every day",
     "A quick check, reviews due, mistakes to fix and new questions, paced to your test date. Spaced repetition brings questions back just before you'd forget them."),
    ("chart", "Progress and pass chance",
     "See how much you've covered, your weakest topic and an estimated pass chance based on your recent answers. It is an estimate, not a guarantee."),
    ("eye", "Hazard perception clips",
     "Real-time 3D driving clips from the driver's seat: tap when it is safe to turn, move off, overtake or change lanes. Plus still scenes and a guide to your state's test."),
    ("globe", "Five languages",
     f"Menus, questions and explanations in {LANGS}, for every state and territory. Arabic reads right to left."),
    ("moon", "Dark mode and large text",
     "Follows your phone's theme, with a switch in Settings. Screens have TalkBack labels and support large font sizes."),
    ("offline", "Practise offline",
     "Questions are built into the app, so you can practise without a connection once you've signed in. Progress syncs when you're back online."),
]


def features_grid() -> str:
    cards = "".join(
        f'<div class="card"><span class="icon-tile">{icon(i)}</span><h3>{t}</h3><p>{d}</p></div>'
        for i, t, d in FEATURES_GRID
    )
    return f'<div class="grid grid-4">{cards}</div>'


INDEPENDENCE = f"""<div class="callout"><h3>Independent, and upfront about it</h3>
<p>{DISCLAIMER} Always check your state's official handbook and website before your test.</p></div>"""


# ── Home ──────────────────────────────────────────────────────────────────────────────────────
def home() -> Page:
    body = f"""<section class="hero on-dark" aria-labelledby="hero-title">
<div class="container hero-grid">
  <div>
    <p class="eyebrow">Learner driver app for every state and territory</p>
    <h1 id="hero-title">Practise for your <span class="hl">learners test</span> in your state's real format</h1>
    <p class="lead">{SITE_NAME} is an Android app by {DEVELOPER} for learner drivers in all eight Australian states and
    territories. Choose your state and practise its knowledge test the way it is really set: original questions checked
    against official sources, every answer explained, and mock tests that show exactly where the pass line is.</p>
    {coming_soon(beside='<a class="btn btn-ghost" href="@/features.html">See the features</a>')}
    <p class="fine">Free to practise. One free mock test a day. Optional one-time Premium for {PRICE}.</p>
  </div>
  {mock_question()}
</div>
</section>

<section class="section" aria-labelledby="states-title">
<div class="container">
  <div class="section-head">
    <p class="eyebrow">Pick your state</p>
    <h2 id="states-title">Your state's learner test, in its real format</h2>
    <p>Road rules and knowledge tests differ between states. The app covers all eight states and territories: it sets
    up practice and mock tests for the one where you'll sit your test, and you can add or switch states later.</p>
  </div>
  {state_cards()}
  <p style="margin-top:1.5rem"><a class="card-link" href="@/states.html">Compare the learner tests by state {icon('arrow')}</a></p>
</div>
</section>

<section class="section section-alt" aria-labelledby="what-title">
<div class="container">
  <div class="section-head">
    <p class="eyebrow">What the app does</p>
    <h2 id="what-title">Everything you need to prepare, in one learner driver app</h2>
    <p>Practice questions for every state's learner test, from the NSW DKT to the NT driver knowledge test, built around
    how people actually learn: little and often, with every mistake turned into a review.</p>
  </div>
  {features_grid()}
  <p style="margin-top:1.5rem"><a class="card-link" href="@/features.html">Take the full feature tour {icon('arrow')}</a></p>
</div>
</section>

<section class="section" aria-labelledby="how-title">
<div class="container two-col" style="align-items:center">
  <div>
    <p class="eyebrow">How it works</p>
    <h2 id="how-title">From your first question to test day</h2>
    <ol class="steps">
      <li><h3>Choose your state and test date</h3><p>The app shows your test's format and paces a daily plan to your date. No date yet? That's fine too.</p></li>
      <li><h3>Practise a little every day</h3><p>Start with a 12-question quick check, then work through reviews, mistakes and new questions.</p></li>
      <li><h3>Sit mock tests</h3><p>Same number of questions and pass marks as the real test, with results shown section by section.</p></li>
      <li><h3>Watch your pass chance</h3><p>An estimate from your recent answers shows when you're getting close. Then check the official website and book.</p></li>
    </ol>
  </div>
  {mock_today()}
</div>
</section>

<section class="section section-alt" aria-labelledby="price-title">
<div class="container">
  <div class="section-head">
    <p class="eyebrow">Pricing, plainly</p>
    <h2 id="price-title">Free to practise. Premium is optional and paid once.</h2>
    <p>Every practice question is free for everyone. Free learners get one mock test a day, and another each time
    they choose to watch a short ad. Premium is a one-time purchase of {PRICE} through Google Play: no subscription,
    and it covers every state.</p>
  </div>
  {price_table()}
  <p class="meta">Refunds follow Google Play's refund policy and your rights under the Australian Consumer Law.
  See the <a href="@/faq.html">FAQ</a> for more.</p>
</div>
</section>

<section class="section" aria-labelledby="content-title">
<div class="container two-col">
  <div class="prose">
    <p class="eyebrow">How the questions are made</p>
    <h2 id="content-title">Original questions, checked against official sources</h2>
    <p>For each state we first map every fact the official material tests, using the current handbook where we may,
    the official test pages and the road rules legislation. Then every question is written in our own words to test one
    of those facts, with the handbook page or road rule it comes from and the date it was last checked.</p>
    <ul class="check-list">
      <li>No official questions, answer options, handbook text or images are reproduced.</li>
      <li>Road signs and diagrams are redrawn as original illustrations.</li>
      <li>Where an older official source differs from the current rule, the question follows the current rule.</li>
    </ul>
    <p><a href="@/about.html">Read how we make and check the content</a>.</p>
  </div>
  <aside>{INDEPENDENCE}</aside>
</div>
</section>

<section class="section section-alt" aria-labelledby="guides-title">
<div class="container">
  <div class="section-head">
    <p class="eyebrow">Guides</p>
    <h2 id="guides-title">Learner test guides</h2>
    <p>Plain-English guides to learner tests and road rules, written from official sources as checked on {CHECKED_H}.
    Every state and territory also has its own page: <a href="@/states.html">learner tests by state</a>.</p>
  </div>
  <div class="grid grid-3">
    <article class="card post-card"><h3><a href="@/blog/nsw-driver-knowledge-test-explained.html">How the NSW Driver Knowledge Test works</a></h3><p>Sections, pass marks, the online option and what comes after your Ls.</p></article>
    <article class="card post-card"><h3><a href="@/blog/victorian-learner-permit-test-explained.html">The Victorian learner permit test explained</a></h3><p>Online course or in person, the 32-question format and Victoria-only rules.</p></article>
    <article class="card post-card"><h3><a href="@/blog/qld-written-road-rules-test-vs-prepl.html">QLD written road rules test vs PrepL</a></h3><p>Two ways to your Queensland learner licence, compared side by side.</p></article>
    <article class="card post-card"><h3><a href="@/blog/give-way-rules-for-learner-drivers.html">Give way rules every learner must know</a></h3><p>The national rules, and where NSW, VIC and QLD differ.</p></article>
    <article class="card post-card"><h3><a href="@/blog/how-to-use-mock-tests-and-mistakes.html">How to use mock tests and mistakes</a></h3><p>Know your mistake budget and turn every wrong answer into a review.</p></article>
    <article class="card post-card"><h3><a href="@/blog/hazard-perception-test-nsw-vic-qld.html">Hazard perception test in NSW, VIC and QLD</a></h3><p>What it is, when you sit it and how to build the skill.</p></article>
  </div>
</div>
</section>

<section class="section light-cta" aria-labelledby="get-title">
<div class="container"><div class="prose">
  <h2 id="get-title">Get the app</h2>
  <p>{APP_NAME} is an Android app. It isn't on Google Play yet. When it is, this button will link straight to the
  listing. The <a href="@/download.html">download page</a> has the details, and how to try the app early.</p>
  {coming_soon('light')}
</div></div>
</section>"""
    return Page(
        path="index.html",
        title="Learners Test Australia: DKT & Learner Permit Practice",
        description=("Learners test practice app for every Australian state and territory: original questions in each "
                     "state's real test format, explained answers and mock tests."),
        body=body,
        nav=None,
        crumbs=[],
        jsonld=[
            organization(),
            {"@type": "WebSite", "@id": SITE_ID, "name": SITE_NAME, "url": BASE, "inLanguage": "en-AU",
             "publisher": {"@id": ORG_ID},
             "description": "Website of Learners Test Australia, an independent learner driver study app for all eight Australian states and territories."},
            mobile_application(),
        ],
        priority="1.0",
        changefreq="weekly",
        llms=True,
        llms_title="Home",
        llms_note="What the app is, the tests it covers in all eight states and territories, pricing (free practice, one-time A$5.99 Premium) and how questions are written.",
    )


# ── Features ──────────────────────────────────────────────────────────────────────────────────
def features() -> Page:
    crumbs = [("Home", ""), ("Features", "features.html")]
    body = page_head(
        "Learner driver app features",
        f"A closer look at {SITE_NAME}: state-specific mock tests, explained answers, a daily plan, progress tracking, "
        "hazard perception practice and more.",
        crumbs,
        eyebrow="Feature tour",
    ) + f"""
<div class="content"><div class="container">

<section class="feature-row" aria-labelledby="f1">
<div class="two-col" style="align-items:center">
  <div class="prose">
    <h2 id="f1">Pick your state, practise its test</h2>
    <p>When you first open the app you choose where you'll take your test. The app then shows that test's
    "fingerprint": how many questions it has, the pass mark for each section, whether there is a time limit and
    whether it ends early. Every summary shows its official source and the date we checked it.</p>
    <ul>
      <li><strong>NSW:</strong> Driver Knowledge Test, 45 questions in two sections (general knowledge and road safety).</li>
      <li><strong>VIC:</strong> learner permit test, 32 questions.</li>
      <li><strong>QLD:</strong> written road rules test, 30 questions in two sections (giving way and road rules), and the PrepL final test, 30 questions.</li>
      <li><strong>SA:</strong> learner's theory test in person, 8 give-way questions and then 42, and the myLs test, 30 questions.</li>
      <li><strong>WA:</strong> a 30-question learner's permit practice test.</li>
      <li><strong>TAS:</strong> the online driver knowledge test, 30 questions, some with more than one correct answer.</li>
      <li><strong>ACT:</strong> a 35-question learner licence knowledge test.</li>
      <li><strong>NT:</strong> driver knowledge test, 30 questions.</li>
    </ul>
    <p>Progress is saved separately for each state, so switching states never mixes up your results.
    <a href="@/states.html">Compare the tests by state</a>.</p>
  </div>
  {mock_fingerprint()}
</div>
</section>

<section class="feature-row flip" aria-labelledby="f2">
<div class="two-col" style="align-items:center">
  <div class="prose">
    <h2 id="f2">Every answer explained, with its source</h2>
    <p>After each answer you see whether you were right, a short explanation, why the rule matters, and the source:
    the handbook page or road rule number. If you want to read more, you know exactly where to look.</p>
    <p>Questions come in the forms real tests use: single answers, road signs and diagrams, plus
    select-all-that-apply questions for the South Australian myLs and Tasmanian online tests. A quick
    "How sure were you?" tap (knew it, unsure or guessed) helps the app decide when to show a question again, and you
    can save or flag any question to come back to.</p>
    <p>Each state's question pack has from 386 (NT) to 555 (SA) original questions, about 3,770 in all, and hundreds
    of original sign and diagram illustrations are shared across states.</p>
  </div>
  {mock_question()}
</div>
</section>

<section class="feature-row" aria-labelledby="f3">
<div class="two-col" style="align-items:center">
  <div class="prose">
    <h2 id="f3">A daily plan paced to your test date</h2>
    <p>Today's plan puts the right things in front of you:</p>
    <ul>
      <li><strong>Quick check:</strong> 12 questions to find your starting point.</li>
      <li><strong>Reviews due:</strong> questions to revisit just before you'd forget them (spaced repetition).</li>
      <li><strong>Fix your mistakes:</strong> the questions you got wrong.</li>
      <li><strong>Learn new questions:</strong> ones you haven't seen yet.</li>
      <li><strong>Mock test:</strong> the full test, same format as the real one.</li>
    </ul>
    <p>Other ways to practise: mixed practice (20 questions, new ones first), mistakes, saved questions, weak spots
    and practice by topic, with a mastery ring for each topic. Optional study reminders and a countdown help you keep going, and a study streak counts
    real study only.</p>
  </div>
  {mock_today()}
</div>
</section>

<section class="feature-row flip" aria-labelledby="f4">
<div class="two-col" style="align-items:center">
  <div class="prose">
    <h2 id="f4">Mock tests that show the pass line</h2>
    <p>Mock tests have the same sections and number of questions as the real test, and each section is scored
    against its own pass mark.
    In the NSW mock, the test ends where the real DKT would, once passing is no longer possible, and you can choose
    to keep practising the rest. In the South Australian in-person theory test mock, a mistake in Part A (giving way)
    ends the test after Part A, as it does at Service SA. The other mock tests run to the last question.</p>
    <p>Results show your score in each section against its pass line, how long you took and which questions to
    review, with one tap to practise your mistakes. <a href="@/blog/how-to-use-mock-tests-and-mistakes.html">How to get
    the most out of mock tests</a>.</p>
    <p>Free learners get one mock test a day, plus another each time they choose to watch a short ad. Premium makes
    mock tests unlimited.</p>
  </div>
  {mock_results()}
</div>
</section>

<section class="feature-row" aria-labelledby="f5">
<div class="two-col" style="align-items:center">
  <div class="prose">
    <h2 id="f5">Progress and an honest pass-chance estimate</h2>
    <p>The Progress tab shows how many questions you've answered and seen, your study streak, minutes studied this
    week and your recent accuracy. After your first 12 answers (the quick check), the Today screen shows an estimated
    pass chance.</p>
    <p>With Premium you also get a forecast for each section (your expected score and the chance of passing that
    section), your weak spots and a planner for upcoming reviews.</p>
    <p class="note">The pass chance is an estimate from your recent answers, not a guarantee. The official test is set
    by your state's licensing authority.</p>
  </div>
  <div class="card">
    <h3>Section forecast (Premium)</h3>
    <p class="meta">Illustration with sample data</p>
    <p style="margin:.8rem 0 .2rem"><strong>General knowledge</strong>: expected 13 of 15</p>
    <div class="passbar"><span class="fill" style="--v:86%"></span><span class="line" style="--p:80%"></span></div>
    <p style="margin:.8rem 0 .2rem"><strong>Road safety</strong>: expected 28 of 30</p>
    <div class="passbar"><span class="fill under" style="--v:93%"></span><span class="line" style="--p:96.7%"></span></div>
    <p class="meta" style="margin-top:.8rem">Here the road safety forecast sits just under its pass line, so that's where to focus.</p>
  </div>
</div>
</section>

<section class="feature-row flip" aria-labelledby="f6">
<div class="two-col" style="align-items:center">
  <div class="prose">
    <h2 id="f6">Hazard perception practice</h2>
    <p>Hazard perception is about spotting risks early. The app plays 72 short driving clips in real-time 3D, seen
    from the driver's seat: you are told what you want to do (turn right, move off, overtake, change lanes or slow
    down) and tap when it becomes safe, in the same style as the hazard perception tests. Clips cover suburban
    streets, traffic lights, roundabouts, school zones, country roads with kangaroos and road trains, freeways,
    level crossings and Melbourne trams, by day, at dusk, at night and in the rain. Afterwards a timeline shows when
    it was safe and when you tapped, with the road rule explained, and you can watch the clip again.</p>
    <p>There are also 40 illustrated still scenes where you tap the hazard. 11 clips and 6 scenes are free, and
    Premium unlocks them all. Every clip and scene can be browsed in picture libraries, and any clip can be replayed.
    Each state's licence guide explains where its hazard perception test fits on the way to your
    P plates (the Northern Territory has no separate test: hazards are assessed in the practical driving test).
    The clips and scenes are original practice material, not a copy of any official test.
    <a href="@/blog/hazard-perception-test-nsw-vic-qld.html">Read our hazard perception guide</a>.</p>
  </div>
  {mock_hazard()}
</div>
</section>

<section class="feature-row" aria-labelledby="f7">
  <h2 id="f7">Also included</h2>
  <div class="grid grid-3">
    <div class="card"><span class="icon-tile">{icon('route')}</span><h3>Licence guide</h3><p>Each step from learner to full licence in your state, with links to the official pages.</p></div>
    <div class="card"><span class="icon-tile">{icon('bell')}</span><h3>Reminders and countdown</h3><p>A daily nudge and a countdown to your test, if you turn them on.</p></div>
    <div class="card"><span class="icon-tile">{icon('star')}</span><h3>Streak and badges</h3><p>A study streak and six badges for real study (your first session, a 7-day streak, 100 answers, every topic tried, a mock test passed, 8 hazard clips passed). No points to grind.</p></div>
    <div class="card"><span class="icon-tile">{icon('globe')}</span><h3>Five languages</h3><p>{LANGS}, including the questions and explanations for every state and territory. Arabic reads right to left.</p></div>
    <div class="card"><span class="icon-tile">{icon('text')}</span><h3>Accessible by design</h3><p>Readable fonts, large-text support, dark mode, TalkBack labels and a spoken timer.</p></div>
    <div class="card"><span class="icon-tile">{icon('offline')}</span><h3>Offline practice, synced progress</h3><p>Practise without a connection after signing in. Your progress is saved to your account and follows you to a new phone.</p></div>
    <div class="card"><span class="icon-tile">{icon('shield')}</span><h3>Your privacy choices</h3><p>A short privacy card at the start and switches in Settings. <a href="@/privacy-policy.html">Privacy policy</a>.</p></div>
    <div class="card"><span class="icon-tile">{icon('check')}</span><h3>Sources you can see</h3><p>Settings lists the question pack version, the handbook edition it was checked against, and every source.</p></div>
    <div class="card"><span class="icon-tile">{icon('phone')}</span><h3>Phones and tablets</h3><p>Runs on Android 8.0 or later, with a layout that adapts to larger screens.</p></div>
  </div>
</section>

<section class="feature-row" aria-labelledby="f8">
  <h2 id="f8">Free and Premium</h2>
  {price_table()}
  <p>Questions about paying, restoring a purchase or refunds? See the <a href="@/faq.html">FAQ</a>.</p>
</section>

<section class="feature-row light-cta" aria-labelledby="f9">
  <h2 id="f9">Coming soon to Android</h2>
  <p>The app isn't on Google Play yet. This page will link to it when it is.</p>
  {coming_soon('light')}
</section>

</div></div>"""
    return Page(
        path="features.html",
        title="Learner Driver App Features | Learners Test Australia",
        description=("Tour the Learners Test Australia app: mock tests for all 8 states, explained answers with sources, a "
                     "daily plan, pass-chance estimate and 3D hazard clips."),
        body=body,
        nav="features",
        crumbs=crumbs,
        priority="0.9",
        llms=True,
        llms_title="Features",
        llms_note="Feature tour: test formats for all eight states and territories, explained answers with sources, daily plan, mock tests, progress, 72 real-time 3D hazard perception clips, languages, offline.",
    )


# ── States hub ────────────────────────────────────────────────────────────────────────────────
def states() -> Page:
    crumbs = [("Home", ""), ("States", "states.html")]
    body = page_head(
        "Learner driver knowledge tests by state",
        "Each Australian state and territory runs its own learner knowledge test. Here is how all eight compare, and "
        "where to find the details for yours.",
        crumbs,
        eyebrow="States and territories",
    ) + f"""
<div class="content"><div class="container">
<div class="answer-box"><p class="answer-label">In short</p>
<p>Every state and territory sets its own learner knowledge test. Formats range from 30 questions (Queensland, the
Tasmanian online test, the Northern Territory and South Australia's myLs) through 32 in Victoria's in-person test and
35 in the ACT to 45 in the NSW DKT and 50 in South Australia's in-person test, and several states also offer an online
course route. {SITE_NAME} has practice for
all eight: {ALL_STATES_TEXT}.</p></div>

<h2>How do the learner tests compare across Australia?</h2>
<div class="table-wrap"><table>
<caption>Knowledge test formats, as checked on {CHECKED_H}</caption>
<thead><tr><th scope="col">State</th><th scope="col">Test</th><th scope="col">Questions</th><th scope="col">Pass mark</th><th scope="col">How you take it</th></tr></thead>
<tbody>
<tr><th scope="row"><a href="@/nsw-dkt-practice-test.html">NSW</a></th><td>Driver Knowledge Test (DKT)</td><td>45: 15 general knowledge, 30 road safety</td><td>12 of 15 and 29 of 30</td><td>In person, or the DKT online course and final test from 15 years 11 months</td></tr>
<tr><th scope="row"><a href="@/vic-learner-permit-test-practice.html">VIC</a></th><td>Learner permit test</td><td>32 (in-person test)</td><td>25 of 32 (78%)</td><td>Online learner permit course with a final test (the default route), or in person</td></tr>
<tr><th scope="row"><a href="@/qld-learner-test-practice.html">QLD</a></th><td>Written road rules test</td><td>30: 10 giving way, 20 road rules and licence requirements</td><td>9 of 10 and 18 of 20</td><td>On paper at a licence-issuing centre, or PrepL online (final test of 30 questions, pass 27)</td></tr>
<tr><th scope="row"><a href="@/sa-learners-test-practice.html">SA</a></th><td>Learner's theory test</td><td>In person: 8 give-way, then 42 road rules and safety</td><td>All 8, and 32 of 42</td><td>In person at Service SA, or myLs online (30-question test, pass 27)</td></tr>
<tr><th scope="row"><a href="@/wa-learners-test-practice.html">WA</a></th><td>Learner's permit theory test</td><td>30</td><td>24 of 30</td><td>In person at a department centre or regional agent (online test announced, no start date yet)</td></tr>
<tr><th scope="row"><a href="@/tas-learners-test-practice.html">TAS</a></th><td>Driver knowledge test</td><td>30 (online test)</td><td>27 of 30</td><td>Free Plates Plus course and online test (recommended), or a standalone test at a Service Tasmania shop</td></tr>
<tr><th scope="row"><a href="@/act-learners-test-practice.html">ACT</a></th><td>Learner licence knowledge test</td><td>35, from a bank of more than 300</td><td>At least 31 of 35</td><td>Only at the end of an approved course, with an approved provider or participating school</td></tr>
<tr><th scope="row"><a href="@/nt-learners-test-practice.html">NT</a></th><td>Driver knowledge test</td><td>30, from a pool of more than 300</td><td>26 of 30</td><td>At an MVR office (in remote areas, a police station or DriveSafe NT)</td></tr>
</tbody></table></div>
<p class="meta">Sources: the official test pages and legislation linked on each state's page. Some details are not
published, such as the size of the NSW and Victorian online final tests, the Tasmanian standalone test format and every
detail of the ACT pass rule. For Western Australia we state only what we could confirm from WA legislation.</p>

<h2>Choose your state</h2>
{state_cards('h3')}

<h2 style="margin-top:2.5rem">Which states have an online route?</h2>
<p>New South Wales, Victoria, Queensland, South Australia and Tasmania all offer an online course that ends with a
test: the DKT online in NSW, the learner permit course in Victoria, PrepL in Queensland, myLs in South Australia and
Plates Plus in Tasmania. In the ACT the test comes at the end of an approved course run by a provider or school. In the
Northern Territory you sit the test at an MVR office. Each state page explains the options and ages.</p>

<h2>What is the same in every state?</h2>
<p>Much of what the tests check comes from the national Australian Road Rules, which most states and territories adopt
in their own law (Western Australia has its own Road Traffic Code, which follows them closely): giving way at
intersections and roundabouts, traffic lights, speed limit signs and most road markings. The details that differ are
usually licensing rules (supervised hours, plate rules, passenger limits, alcohol and phone rules for new drivers) and
a few local road rules, such as Victoria's hook turns or the Northern Territory's 130 km/h roads. Our guide to
<a href="@/blog/give-way-rules-for-learner-drivers.html">give way rules</a> covers the shared rules.</p>
</div></div>"""
    return Page(
        path="states.html",
        title="Learner Tests by State | Learners Test Australia",
        description=("Compare learner knowledge tests in all 8 states and territories: NSW DKT, VIC permit test, QLD, SA, "
                     "WA, TAS, ACT and NT formats, pass marks and routes."),
        body=body,
        nav="states",
        crumbs=crumbs,
        priority="0.9",
        llms=True,
        llms_title="States",
        llms_note="Side-by-side comparison of the learner knowledge tests in all eight states and territories, with links to each state's page.",
    )


# ── FAQ ───────────────────────────────────────────────────────────────────────────────────────
FAQ_GROUPS = [
    ("About the app", [
        ("What is Learners Test Australia?",
         f"<p>{SITE_NAME} (on Google Play as “{APP_NAME}”) is an Android study app by {DEVELOPER} for people preparing "
         "for an Australian learner driver knowledge test. You choose your state, then practise with original questions, "
         "explained answers and mock tests in that state's test format.</p>"),
        ("Is Learners Test Australia an official government app?",
         f"<p>No. {DISCLAIMER} The official test is run by your state or territory's licensing authority, so always check "
         "its current handbook and website.</p>"),
        ("Are these the real test questions?",
         "<p>No. Every question is written for the app in our own words. The questions test the same facts the official "
         "material covers, but no official questions, answer options, handbook text or images are reproduced.</p>"),
        ("Which states and territories does the app cover?",
         f"<p>All eight: {ALL_STATES_TEXT}. Each has its own question pack, mock tests and licence guide, and you can "
         'switch states at any time. <a href="@/states.html">Compare the tests by state</a>.</p>'),
        ("Which tests can I practise?",
         "<p>The NSW Driver Knowledge Test (45 questions: 15 general knowledge, pass 12, and 30 road safety, pass 29), the "
         "Victorian learner permit test (32 questions, pass 25), the Queensland written road rules test (10 giving way, "
         "pass 9, and 20 road rules, pass 18) and PrepL final test (30 questions, pass 27), the South Australian "
         "learner's theory test (8 give-way questions, all must be right, then 42, pass 32) and myLs test (30 questions, "
         "pass 27), a 30-question Western Australian practice test, the Tasmanian online driver knowledge test (30 "
         "questions, pass 27), a 35-question ACT practice test (pass line 31) and the Northern Territory driver knowledge "
         "test (30 questions, pass 26). There is also hazard perception practice with real-time 3D driving clips and still scenes.</p>"),
    ]),
    ("Price and Premium", [
        ("Is the app free?",
         "<p>Yes. It is free to download and every practice question is free. Free learners get one mock test a day, plus "
         "another each time they choose to watch a short ad. The free version shows banner ads on results and guide pages.</p>"),
        ("What does Premium include, and how much is it?",
         f"<p>Premium is a one-time purchase of {PRICE}. It removes ads and adds unlimited mock tests, section forecasts, "
         "weak spots and a review planner, and all the hazard perception clips and scenes. It covers every state. Every practice "
         "question stays free for everyone.</p>"),
        ("Is Premium a subscription?",
         "<p>No. Premium is a lifetime purchase: there are no subscriptions or renewals. It belongs to the Google account "
         "that bought it, so it stays available if you sign in again on the same Google account.</p>"),
        ("I bought Premium but it isn't showing. What should I do?",
         f'<p>Open Settings → Premium → Restore purchase. If that doesn\'t fix it, email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>'),
        ("Can I get a refund?",
         "<p>Purchases are processed by Google Play, so refunds follow Google Play's refund policy and your rights under the "
         "Australian Consumer Law. Deleting your account does not refund a purchase, except where the law requires it.</p>"),
    ]),
    ("Account and privacy", [
        ("Do I need an account, and why?",
         "<p>Yes. You sign in when you start, with Google, Facebook or an email address. Your answers and progress for each "
         "state are saved to your account, so they follow you to a new phone. Tips and offers by email are optional, and "
         "you can unsubscribe any time.</p>"),
        ("How do I delete my account and data?",
         f'<p>In the app, open Settings → Delete account. This removes your account and saved progress. You can also email '
         f'<a href="mailto:{EMAIL}">{EMAIL}</a> from your account\'s email address with the subject “Delete my account”. '
         'Full steps are on the <a href="@/account-deletion.html">account deletion page</a>.</p>'),
        ("What data does the app collect?",
         "<p>Your name and email address when you sign in, your study data (answers, sessions, saved questions and chosen "
         "state), anonymous usage statistics and crash reports only if you allow them, and, in the free version, your "
         "device's advertising ID for ads. We never sell your personal information. Details are in the "
         '<a href="@/privacy-policy.html">privacy policy</a>.</p>'),
        ("Why are there ads, and can I control ad personalisation?",
         "<p>Ads keep practice free. Where the law requires it (for example in the EEA and UK), Google asks for your consent "
         "first, and you can change it in Settings → Ad privacy choices. You can also reset or delete your advertising ID "
         'in your phone\'s settings. Premium removes ads. See the <a href="@/cookies.html">cookie policy</a>.</p>'),
    ]),
    ("Using the app", [
        ("Which languages does the app support?",
         f"<p>{LANGS}. Menus, questions and explanations are translated for every state and territory, and Arabic reads "
         "right to left. You can change the language in Settings. "
         "Language options for the official tests themselves differ by state, so check your state's website.</p>"),
        ("Does the app work offline?",
         "<p>Mostly. Questions are built into the app, so after you've signed in you can practise without a connection, and "
         "your progress syncs when you're back online. You need a connection to sign in, to watch an ad for an extra mock "
         "test and to buy or restore Premium.</p>"),
        ("Which phones does it run on? Is there an iPhone version?",
         "<p>The app runs on Android phones and tablets with Android 8.0 or later. It is Android only for now.</p>"),
        ("When will the app be on Google Play?",
         "<p>Soon. It isn't listed yet, so there is no store link on this site. When it goes live, the “Coming soon to Google "
         "Play” button will become a link to the listing.</p>"),
        ("How does the pass-chance estimate work?",
         "<p>After your first 12 answers (the quick check), the app estimates your chance of passing from your recent "
         "answers. It "
         "is an estimate, not a guarantee. Premium adds a forecast for each section of the test.</p>"),
        ("Does the app include hazard perception practice?",
         "<p>Yes. There are 72 real-time 3D driving clips where you tap when it is safe to act, in the same style as the "
         "hazard perception tests, plus 40 illustrated still scenes and a guide to your state's hazard perception test "
         "(the Northern Territory has none; hazards are assessed in its practical driving test). 11 clips and 6 scenes "
         "are free, and Premium unlocks them all. Every clip and scene can be browsed in picture libraries, and any clip "
         "can be replayed. They are original practice material and "
         'are not a copy of any official test. See our <a href="@/blog/hazard-perception-test-nsw-vic-qld.html">hazard '
         "perception guide</a>.</p>"),
    ]),
    ("Questions and accuracy", [
        ("How are the questions written?",
         "<p>For each state we build a coverage map of every fact the official material tests, from the current handbook, "
         "the official test pages, the official practice tests (used only to see which facts are tested) and the road rules "
         "legislation; for Western Australia, Tasmania, the ACT and the Northern Territory, from legislation instead of a "
         "handbook. Each question is then written in original wording to test one of those facts, with a rule reference "
         "(handbook page or road rule) and a review date. Questions are never copied or paraphrased from official question "
         'banks. <a href="@/about.html">More about our content</a>.</p>'),
        ("How accurate are the questions?",
         f"<p>The questions were checked against the official sources current on {CHECKED_H}: the NSW Road User "
         "Handbook (edition 02/2026), Victoria's Road to Solo Driving handbook (checked against current Transport Victoria "
         "and VicRoads pages), Your keys to driving in Queensland (checked against current Queensland Government pages "
         "and legislation) and South Australia's Driver's Handbook (February 2026). Western Australian, Tasmanian, ACT "
         "and Northern Territory questions are written from each one's road rules and licensing legislation. Rules change, "
         'so always check your state\'s official website before your test. <a href="@/about.html">Our sources, state by '
         "state</a>.</p>"),
        ("I think a question is wrong. How do I report it?",
         f'<p>Email <a href="mailto:{EMAIL}">{EMAIL}</a> with your state, the question (or its first few words), what you '
         'think is wrong and, if you can, a link to the official source. The <a href="@/contact.html">contact page</a> lists '
         "what helps us fix it fastest. We aim to reply within 5 business days.</p>"),
        ("How old do I need to be to use the app?",
         "<p>Under our Terms of Service you must be at least 15 to use the app and create an account, and if you are under "
         "18 a parent or legal guardian must consent to your use of the app.</p>"),
    ]),
]


def faq() -> Page:
    crumbs = [("Home", ""), ("FAQ", "faq.html")]
    all_items = [qa for _, items in FAQ_GROUPS for qa in items]
    groups = "".join(
        f'<div class="faq-group">{faq_block(items, heading=title, hid=f"faq-{i}")}</div>'
        for i, (title, items) in enumerate(FAQ_GROUPS, start=1)
    )
    body = page_head(
        "Learner test app FAQ",
        f"Straight answers about {SITE_NAME}: what it is and isn't, states, price, accounts, languages, offline use and "
        "how the questions are written.",
        crumbs,
        eyebrow="Frequently asked questions",
    ) + f"""
<div class="content"><div class="container prose">
<p>Can't find your answer? Email <a href="mailto:{EMAIL}">{EMAIL}</a> or see the <a href="@/contact.html">contact page</a>.</p>
{groups}
</div></div>"""
    return Page(
        path="faq.html",
        title="Learner Test App FAQ | Learners Test Australia",
        description=("Answers about Learners Test Australia: is it official, which states, what's free, Premium A$5.99, "
                     "accounts, deleting data, languages and offline use."),
        body=body,
        nav="faq",
        crumbs=crumbs,
        jsonld=[faq_ld(all_items)],
        priority="0.8",
        llms=True,
        llms_title="FAQ",
        llms_note=f"{len(all_items)} questions and answers: independence, states, price and Premium, account and deletion, languages, offline, accuracy.",
    )


# ── About ─────────────────────────────────────────────────────────────────────────────────────
def about() -> Page:
    crumbs = [("Home", ""), ("About", "about.html")]
    body = page_head(
        "About Learners Test Australia and how we make our questions",
        f"Who makes the app, why it exists, and the process behind every question.",
        crumbs,
        eyebrow="About",
    ) + f"""
<div class="content"><div class="container two-col">
<div class="prose">
<h2>Who makes Learners Test Australia?</h2>
<p>{SITE_NAME} is made by {DEVELOPER}, an independent app developer. {DEVELOPER} is not a driving school or a
government agency, and the app has no connection with any licensing authority. You can reach us at
<a href="mailto:{EMAIL}">{EMAIL}</a>.</p>

<h2>Why a state-by-state learner test app?</h2>
<p>Each state runs its own knowledge test with its own format, pass marks and licensing rules. A question bank that
mixes them up teaches the wrong numbers: the supervised hours, plate rules and alcohol limits for new drivers are not
the same everywhere. So the app has one profile per state, and each profile follows that state's handbook, test format
and rules.</p>

<h2>How are the questions made and checked?</h2>
<ol class="steps">
  <li><h3>A coverage map for each state</h3><p>We list every fact the official material tests, using the current
  handbook, the official test pages, the official practice tests (only to see which facts get tested) and the road
  rules legislation. For Western Australia, Tasmania, the ACT and the Northern Territory we work from legislation
  instead of a handbook. Each fact records its source and the date it was checked.</p></li>
  <li><h3>Original questions</h3><p>Every question is written in our own words to test one fact from the map, with
  wrong options based on common misunderstandings. No official question, answer option, handbook sentence or image is
  reproduced, and we don't paraphrase official question banks.</p></li>
  <li><h3>A source and a review date on every question</h3><p>Each question carries the handbook page or road rule it
  comes from and the date it was last verified. The launch packs were checked on {CHECKED_H}.</p></li>
  <li><h3>The current rule wins</h3><p>Where an older official source differs from the current rule, the question
  follows the current rule. Facts we couldn't confirm from a current official source are flagged for manual checking
  rather than turned into questions.</p></li>
  <li><h3>Original artwork</h3><p>Road signs, markings and diagrams are redrawn from written descriptions, not traced
  from official artwork.</p></li>
</ol>

<h2>Which official sources are the questions checked against?</h2>
<div class="table-wrap"><table>
<thead><tr><th scope="col">State</th><th scope="col">Main source</th><th scope="col">Also checked against</th></tr></thead>
<tbody>
<tr><th scope="row">NSW</th><td>Road User Handbook, edition 02/2026</td><td>NSW Road Rules 2014 and NSW Government licence and test pages</td></tr>
<tr><th scope="row">VIC</th><td>Road to Solo Driving, April 2023 edition</td><td>Road Safety Road Rules 2017 and current Transport Victoria and VicRoads pages</td></tr>
<tr><th scope="row">QLD</th><td>Your keys to driving in Queensland, No. 19 (November 2022)</td><td>The Queensland Road Rules Regulation in force from 31 August 2026 and current Queensland Government pages</td></tr>
<tr><th scope="row">SA</th><td>The Driver's Handbook (MR200), February 2026 edition</td><td>South Australian road traffic and motor vehicle legislation, and sa.gov.au and mylicence pages</td></tr>
<tr><th scope="row">WA</th><td>WA legislation: Road Traffic Code 2000 (in force from 14 May 2026) and the licensing regulations</td><td>Nothing else: every WA fact comes from legislation</td></tr>
<tr><th scope="row">TAS</th><td>Tasmanian legislation: Road Rules 2019 (in force from 11 December 2025) and the licensing regulations</td><td>Plates Plus and Service Tasmania pages, for the test format, ages and fees only</td></tr>
<tr><th scope="row">ACT</th><td>ACT legislation: Road Transport (Road Rules) Regulation 2017 (republication 17) and the licensing laws</td><td>Access Canberra pages, for the test format, ages and fees only</td></tr>
<tr><th scope="row">NT</th><td>NT legislation: Traffic Regulations 1999 (in force at 28 May 2026) and the Motor Vehicles Act 1949</td><td>nt.gov.au pages, for the test format, ages and fees only</td></tr>
</tbody></table></div>
<p>Where a handbook is older than the current rules (for example, Queensland's 2022 handbook predates the 2026 e-scooter
and e-bike changes), the current official pages and legislation decide the answer. For Western Australia, Tasmania, the
ACT and the Northern Territory we use no handbook at all: the questions are written from legislation.</p>

<h2>Attribution</h2>
<p>Queensland road rules content is based on content from the Queensland Legislation website at {CHECKED_H}
(CC BY 4.0). Queensland Government web pages are © The State of Queensland (Department of Transport and Main Roads),
CC BY 4.0. Transport Victoria web pages are licensed under CC BY 4.0, except images and branding.</p>
<p>South Australian content draws on The Driver's Handbook (MR200, February 2026), Department of Infrastructure and
Transport, Government of South Australia, sourced on {CHECKED_H} from mylicence.sa.gov.au, © Government of South
Australia, CC BY 3.0 AU, and on South Australian legislation, based on content from the South Australian Legislation
website at {CHECKED_H} (CC BY 4.0). Western Australian content is based on content from the Western Australian Legislation
website at {CHECKED_H}, © State of Western Australia, CC BY 4.0. Tasmanian content is based on material from the Tasmanian
Legislation website at {CHECKED_H}, © State of Tasmania, CC BY 4.0. ACT facts are restated from ACT legislation on the ACT
Legislation Register, sourced on {CHECKED_H}, © Australian Capital Territory. Northern Territory facts are restated from
Northern Territory legislation published at legislation.nt.gov.au, sourced on {CHECKED_H}; this is not an official version
of that legislation.</p>
<p>We restate facts in our own words, reproduce no text, logos or images, and none of these sources endorses the app or
this website. For the law in force, always go to the official legislation website for your state or territory.</p>

<h2>Our other app: DTT Ireland</h2>
<p>{DEVELOPER} also makes <a href="{DTT_URL}">DTT Ireland</a>, a practice app for the Irish driver theory test, for car
and motorcycle learners, in nine languages. It is on <a href="{DTT_PLAY}" rel="noopener">Google Play</a>. It follows
the same approach: practice in the real test's format, with every answer explained.</p>

<h2>Independence</h2>
<p>{DISCLAIMER}</p>

<h2>About this website</h2>
<p>This site uses no cookies, analytics or trackers and loads nothing from third parties. See the
<a href="@/privacy-policy.html#website">privacy policy</a>.</p>
</div>
<aside><div class="card aside-card">
  <img src="@/assets/img/icon-512.png" width="96" height="96" loading="lazy" decoding="async"
    alt="Learners Test Australia app icon: a yellow learner plate with a black L on a dark background">
  <h2>At a glance</h2>
  <ul>
    <li><strong>App:</strong> {APP_NAME}</li>
    <li><strong>Developer:</strong> {DEVELOPER}</li>
    <li><strong>Platform:</strong> Android 8.0 or later</li>
    <li><strong>States:</strong> all 8 states and territories</li>
    <li><strong>Languages:</strong> 5</li>
    <li><strong>Price:</strong> free, optional {PRICE} Premium</li>
    <li><strong>Contact:</strong> <a href="mailto:{EMAIL}">{EMAIL}</a></li>
  </ul>
</div></aside>
</div></div>"""
    return Page(
        path="about.html",
        title="About Us and Our Content | Learners Test Australia",
        description=("Who makes Learners Test Australia, why it's built state by state, and how every original question is "
                     "checked against official handbooks and legislation."),
        body=body,
        nav="about",
        crumbs=crumbs,
        jsonld=[{"@type": "AboutPage", "name": "About Learners Test Australia", "url": BASE + "about.html",
                 "about": {"@id": ORG_ID}, "publisher": organization(full=False)},
                dtt_application()],
        priority="0.6",
        llms=True,
        llms_title="About and content process",
        llms_note="Who makes the app (BlueOrbit), how questions are written and checked, handbook editions used, attribution.",
    )


# ── Contact ───────────────────────────────────────────────────────────────────────────────────
def contact() -> Page:
    crumbs = [("Home", ""), ("Contact", "contact.html")]
    body = page_head(
        "Contact and support",
        "Questions, a question you think is wrong, Premium help or a privacy request: email us and we'll get back to you.",
        crumbs,
        eyebrow="Support",
    ) + f"""
<div class="content"><div class="container two-col">
<div class="prose">
<div class="callout">
  <h2 style="margin-top:0">Email support</h2>
  <p style="font-size:1.25rem"><a href="mailto:{EMAIL}">{EMAIL}</a></p>
  <p>We aim to reply within 5 business days.</p>
</div>

<h2>How do I report a question error?</h2>
<p>We check every question against official sources, but rules change and mistakes happen. If something looks wrong,
please tell us. These details help us find and fix it quickly:</p>
<ul>
  <li><strong>Your state and test</strong>, for example “NSW DKT” or “QLD PrepL”.</li>
  <li><strong>The question</strong>: its text or first few words, or a screenshot.</li>
  <li><strong>What you think is wrong</strong>: the answer the app marked correct, and the answer you think is right.</li>
  <li><strong>The official source</strong>, if you have it: a handbook page or a link to the official web page.</li>
  <li><strong>The language</strong> you use the app in.</li>
  <li><strong>The question pack version</strong>, shown in Settings under Content.</li>
</ul>
<p>A subject line like “Question error: VIC” helps us sort your email.</p>

<h2>Premium help</h2>
<p>If Premium isn't showing after you bought it, open Settings → Premium → Restore purchase first. If it still isn't
there, email us. Refunds follow Google Play's refund policy and your rights under the Australian Consumer Law.</p>

<h2>Account and privacy requests</h2>
<p>To delete your account, use Settings → Delete account in the app, or follow the steps on the
<a href="@/account-deletion.html">account deletion page</a>. To access or correct your information, or to make a
privacy complaint, email us; the <a href="@/privacy-policy.html">privacy policy</a> explains your rights.</p>

<h2>What we can't help with</h2>
<p>We can't book tests, issue licences or see your test results. For those, contact your state's licensing authority:</p>
<ul>
  <li>NSW: {ext(SRC['nsw_dkt'], 'Driver Knowledge Test on nsw.gov.au')}</li>
  <li>Victoria: {ext(SRC['vic_lpt'], 'Learner permit test on VicRoads')}</li>
  <li>Queensland: {ext(SRC['qld_tests'], 'Driver tests on qld.gov.au')}</li>
  <li>South Australia: {ext(SRC['sa_theory_test'], "Learner's test at Service SA on sa.gov.au")}</li>
  <li>Western Australia: {ext(SRC['wa_dtmi'], 'Department of Transport and Major Infrastructure')}</li>
  <li>Tasmania: {ext(SRC['tas_st_test'], 'Learner knowledge test on Service Tasmania')}</li>
  <li>ACT: {ext(SRC['act_learner'], 'Learner driver licence on Access Canberra')}</li>
  <li>Northern Territory: {ext(SRC['nt_licence'], 'Driver licence on nt.gov.au')}</li>
</ul>
</div>
<aside><div class="card aside-card">
  <h2>Quick links</h2>
  <ul>
    <li><a href="@/faq.html">FAQ</a></li>
    <li><a href="@/account-deletion.html">Delete your account</a></li>
    <li><a href="@/privacy-policy.html">Privacy policy</a></li>
    <li><a href="@/terms.html">Terms of service</a></li>
    <li><a href="@/about.html">How we make the questions</a></li>
  </ul>
</div></aside>
</div></div>"""
    return Page(
        path="contact.html",
        title="Contact and Support | Learners Test Australia",
        description=("Contact Learners Test Australia support by email: report a question error, get help with Premium, or "
                     "make an account or privacy request. We aim to reply fast."),
        body=body,
        nav="contact",
        crumbs=crumbs,
        jsonld=[{"@type": "ContactPage", "name": "Contact Learners Test Australia", "url": BASE + "contact.html",
                 "about": organization()}],
        priority="0.5",
        llms_note="Support email, what to include when reporting a question error, Premium and privacy help.",
    )


# ── Download ──────────────────────────────────────────────────────────────────────────────────
def download() -> Page:
    crumbs = [("Home", ""), ("Download", "download.html")]
    if PLAY_URL:
        status = ("<p>Learners Test Australia is free on Google Play. Tap the button to open the listing, then tap "
                  "Install.</p>")
    else:
        status = ("<p>The app isn't on Google Play yet. When it is, the button below will open the listing, and this page "
                  "will say so. You can try it before then: see <a href=\"#early\">try the app early</a>.</p>")
    body = page_head(
        "Download the Learners Test Australia app",
        "The learner test practice app for all eight Australian states and territories, for Android phones and tablets.",
        crumbs,
        eyebrow="Download",
    ) + f"""
<div class="content"><div class="container two-col">
<div class="prose">
<h2>Get it on Android</h2>
{status}
{coming_soon('light')}

<h2>What you need</h2>
<ul>
  <li><strong>An Android phone or tablet</strong> with Android 8.0 or later. There is no iPhone version yet.</li>
  <li><strong>An account</strong>: sign in with Google, Facebook, or an email address and password. Your progress is
  saved to it, so it follows you to a new phone.</li>
  <li><strong>A connection to sign in</strong>. After that, the questions are built into the app and you can practise
  offline.</li>
</ul>

<h2>What you get for free</h2>
<ul class="check-list">
  <li>Every practice question for your state, with every answer explained.</li>
  <li>Your state's test format: the same number of questions, sections and pass marks.</li>
  <li>One free mock test a day, and another for each short ad you choose to watch.</li>
  <li>A daily study plan, progress tracking and an estimated pass chance.</li>
  <li>Sample hazard perception practice: 11 of the 72 3D clips and 6 of the 40 still scenes.</li>
  <li>All eight states and territories, in English, Chinese, Arabic, Vietnamese and Spanish.</li>
</ul>
<p>Premium is optional: a one-time {PRICE} purchase through Google Play, with no subscription. It removes ads and adds
unlimited mock tests, forecasts for each section of the test, your weak spots, a review planner, and all 72 hazard
perception clips and 40 still scenes. See the <a href="@/features.html">features</a>.</p>

<h2 id="early">Try the app early</h2>
<p>Before the app goes public on Google Play, we are inviting a small group of learners and parents to test it. If you
have an Android phone and would like to help, email us at <a href="mailto:{EMAIL}?subject=Early%20tester">{EMAIL}</a>
with the subject “Early tester”. Send it from, or include, the Google account email you use on Google Play: Google Play
only lets you install a test app on an account we have invited. We use your email address only to invite you to the
test and to reply to you.</p>

<h2>More apps from {DEVELOPER}</h2>
<div class="card">
  <h3><a href="{DTT_URL}">DTT Ireland: driver theory test practice</a></h3>
  <p>Our app for learner drivers in Ireland: practice for the Irish driver theory test, for car and motorcycle, in nine
  languages. Free on <a href="{DTT_PLAY}" rel="noopener">Google Play</a>.</p>
</div>
</div>
<aside><div class="card aside-card">
  <img src="@/assets/img/icon-512.png" width="96" height="96" loading="lazy" decoding="async"
    alt="Learners Test Australia app icon: a yellow learner plate with a black L and a green tick">
  <h2>At a glance</h2>
  <ul>
    <li><strong>App:</strong> {APP_NAME}</li>
    <li><strong>Developer:</strong> {DEVELOPER}</li>
    <li><strong>Platform:</strong> Android 8.0 or later</li>
    <li><strong>States:</strong> all 8 states and territories</li>
    <li><strong>Languages:</strong> English, 中文, العربية, Tiếng Việt, Español</li>
    <li><strong>Price:</strong> free, optional {PRICE} Premium</li>
  </ul>
</div></aside>
</div></div>"""
    return Page(
        path="download.html",
        title="Download the App | Learners Test Australia",
        description=("Download Learners Test Australia for Android: free learner test practice for every state and "
                     "territory, what you need to install it, and how to try it early."),
        body=body,
        nav="download",
        crumbs=crumbs,
        jsonld=[{"@type": "WebPage", "name": "Download Learners Test Australia", "url": BASE + "download.html",
                 "about": {"@id": BASE + "#app"}, "publisher": organization(full=False)},
                mobile_application()],
        priority="0.8",
        llms_note="Download page: Android 8.0 or later, account needed, what is free, Premium, how to join the early test.",
    )


# ── 404 ───────────────────────────────────────────────────────────────────────────────────────
def not_found() -> Page:
    body = f"""<div class="content"><div class="container notfound prose">
<p class="big" aria-hidden="true">404</p>
<h1>Page not found</h1>
<p>Sorry, we couldn't find that page. It may have moved, or the address may have a typo.</p>
<h2>Try one of these</h2>
<ul>
  <li><a href="@/">Home</a></li>
  <li><a href="@/features.html">Features</a></li>
  <li><a href="@/states.html">Learner tests by state</a>: <a href="@/nsw-dkt-practice-test.html">NSW</a>,
  <a href="@/vic-learner-permit-test-practice.html">VIC</a>, <a href="@/qld-learner-test-practice.html">QLD</a>,
  <a href="@/sa-learners-test-practice.html">SA</a>, <a href="@/wa-learners-test-practice.html">WA</a>,
  <a href="@/tas-learners-test-practice.html">TAS</a>, <a href="@/act-learners-test-practice.html">ACT</a>,
  <a href="@/nt-learners-test-practice.html">NT</a></li>
  <li><a href="@/blog/">Guides</a></li>
  <li><a href="@/faq.html">FAQ</a></li>
  <li><a href="@/contact.html">Contact</a></li>
</ul>
</div></div>"""
    return Page(
        path="404.html",
        title="Page Not Found | Learners Test Australia",
        description=("The page you were looking for isn't here. Find learner test practice for every state and territory, "
                     "our guides, the FAQ and contact details from the links here."),
        body=body,
        noindex=True,
    )
