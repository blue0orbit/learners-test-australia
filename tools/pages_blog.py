"""Blog index and posts.

Every road-rule or test fact in these posts comes from content-src/coverage/{nsw,vic,qld}.md in the app
repository, checked on 30 September 2026. Posts are written in our own words; no official wording is copied.
"""
from sitelib import (
    BASE, DATE, DATE_H, DEVELOPER, SITE_NAME, SRC, Page, chip, esc, organization, page_head, source_box,
    strip_tags, words,
)

BLOG_CRUMB = ("Guides", "blog/")


def byline(body_html: str) -> str:
    mins = max(1, round(words(body_html) / 220))
    return (
        f'<p class="meta">By <a href="@/about.html">{DEVELOPER}</a> · Published <time datetime="{DATE}">{DATE_H}</time> · '
        f"Last updated: <time datetime=\"{DATE}\">{DATE_H}</time> · {mins} min read</p>"
    )


def toc(items: list[tuple[str, str]]) -> str:
    lis = "".join(f'<li><a href="#{i}">{esc(t)}</a></li>' for i, t in items)
    return f'<nav class="toc" aria-labelledby="toc-h"><h2 id="toc-h">In this guide</h2><ol>{lis}</ol></nav>'


def post(slug: str, title: str, h1: str, description: str, summary: str, sections: list[tuple[str, str, str]],
         sources: list[tuple[str, str]], section_name: str, keywords: list[str], llms_note: str,
         related: list[tuple[str, str]]) -> Page:
    path = f"blog/{slug}.html"
    crumbs = [("Home", ""), BLOG_CRUMB, (h1, path)]
    content = "".join(f'<h2 id="{sid}">{esc(t)}</h2>{html}' for sid, t, html in sections)
    rel = "".join(f'<li><a href="@/{p}">{esc(t)}</a></li>' for t, p in related)
    article_html = (
        f'<div class="answer-box"><p class="answer-label">Summary</p><p>{summary}</p></div>'
        + toc([(sid, t) for sid, t, _ in sections])
        + content
    )
    body = page_head(h1, None, crumbs, meta_html=byline(article_html), eyebrow=f'<span class="tag">{esc(section_name)}</span>') + f"""
<div class="content"><div class="container two-col">
<article class="prose">
{article_html}
{source_box(sources)}
</article>
<aside><div class="card aside-card"><h2>Related</h2><ul>{rel}</ul></div></aside>
</div></div>"""
    wc = words(article_html)
    ld = {
        "@type": "BlogPosting",
        "headline": h1,
        "description": description,
        "datePublished": DATE,
        "dateModified": DATE,
        "author": {"@type": "Organization", "name": DEVELOPER, "url": BASE + "about.html"},
        "publisher": organization(full=False),
        "image": {"@type": "ImageObject", "url": BASE + "assets/img/og-image.png", "width": 1200, "height": 630},
        "mainEntityOfPage": {"@type": "WebPage", "@id": BASE + path},
        "url": BASE + path,
        "inLanguage": "en-AU",
        "wordCount": wc,
        "articleSection": section_name,
        "keywords": keywords,
        "isPartOf": {"@type": "Blog", "@id": BASE + "blog/#blog", "name": f"{SITE_NAME} guides"},
    }
    return Page(
        path=path, title=title, description=description, body=body, nav="blog", crumbs=crumbs, jsonld=[ld],
        og_type="article", priority="0.7", llms=True, llms_title=h1, llms_note=llms_note,
        article={"published": DATE + "T09:00:00+10:00", "modified": DATE + "T09:00:00+10:00"},
    )


# ── Post 1: NSW DKT ───────────────────────────────────────────────────────────────────────────
def post_nsw() -> Page:
    sections = [
        ("journey", "Where does the DKT fit in the NSW licence journey?", """
<p>New South Wales uses a graduated licensing scheme. You start on a learner licence, move to a P1 licence (red P
plates), then a P2 licence (green P plates), and finally a full licence. The whole journey takes at least four years if
you are under 25, or three years if you are 25 or older.</p>
<p>Three tests mark the way. The Driver Knowledge Test gets you your Ls. The Hazard Perception Test comes during your
learner period. The practical driving test gets you your P1 licence. The DKT is the only one you can do before you have
driven at all, which is why it is all about knowing the rules rather than handling the car.</p>"""),
        ("format", "What is the format of the DKT?", """
<p>The format the NSW Government publishes for its knowledge tests is 45 multiple-choice questions split into two
parts, each with its own pass mark:</p>
<ul>
  <li><strong>General knowledge:</strong> 15 questions, and you need at least 12 right.</li>
  <li><strong>Road safety:</strong> 30 questions, and you need at least 29 right.</li>
</ul>
<p>The in-person test runs on a computer, with questions drawn at random from a question bank, and no time limit is
published. It also stops early: a 4th wrong answer in general knowledge, or a 2nd wrong answer in road safety, ends
the test, because at that point you can no longer pass.</p>
<p>It helps to think of this as a mistake budget. You can drop 3 questions in general knowledge, but only 1 in road
safety. Road safety is twice as long and almost unforgiving, so it deserves most of your revision time.</p>
<p class="note">This 45-question structure is spelled out on the NSW Government's rider knowledge test page, and the
car DKT is reported to follow it. Confirm the details on the official DKT page when you book.</p>"""),
        ("online", "In person or online: which DKT should you choose?", """
<p>You have two routes. The in-person DKT is open from age 16. The DKT online, introduced in 2024, is a course of about
4 to 6 hours with a final test at the end, and you can start it from 15 years and 11 months. The NSW Government doesn't
publish how many questions the online final test has or what its pass mark is.</p>
<p>Both routes are built on the same book, the Road User Handbook, so your preparation is the same either way. The
online course suits people who like to learn in stages; the in-person test suits people who are ready now and want the
familiar 45-question format.</p>"""),
        ("study", "What should you study for the DKT?", """
<p>Everything comes back to the Road User Handbook. The edition current on 30 September 2026 is 02/2026, published in
February 2026, with 208 printed pages. It runs from licences, through safe driving behaviour (speed, alcohol, drugs,
seatbelts, phones and fatigue) and sharing the road, to stopping, giving way and turning, overtaking and merging,
lanes and markings, parking, hazards, vehicle safety and penalties.</p>
<p>The NSW Government has also published an official DKT question list, dated 2018. It holds 358 questions: 79 general
knowledge, 225 road safety, 51 traffic signs and 3 about test integrity. The busiest topics in it are pedestrians,
intersections and giving way, traffic signs, safe following and stopping distances, and traffic lights, which is a
useful guide to where the marks are.</p>
<p>Be careful with anything older than the current handbook, though. A few items in the 2018 list no longer match
today's rules. For example, red-light cameras in NSW now also detect speeding at any light colour, and the agency you
deal with is Transport for NSW rather than the old RTA. When sources disagree, learn the current handbook's version.</p>"""),
        ("traps", "Which NSW rules do learners most often get wrong?", """
<p>These rules come up again and again, and each has a common wrong belief attached:</p>
<ul>
  <li><strong>STOP signs mean a full stop, every time.</strong> Stop behind the line, as close to it as you can, even
  when no one is coming. A rolling stop is not a stop.</li>
  <li><strong>Yellow means stop if you safely can.</strong> Only keep going if you are so close that braking suddenly
  could cause a crash. Never speed up to beat the red.</li>
  <li><strong>T-intersections:</strong> if you are on the road that ends, you give way to every vehicle on the road that
  continues, whether it is turning or not.</li>
  <li><strong>U-turns at traffic lights</strong> are not allowed in NSW unless a “U-turn permitted” sign is shown.</li>
  <li><strong>“Left turn on red permitted after stopping”</strong> means exactly that: stop at the red first, then turn
  when it is safe, giving way to traffic from the right and pedestrians.</li>
  <li><strong>Following distance:</strong> keep at least 3 seconds behind the vehicle ahead in good conditions, and 4 or
  more in the wet, on gravel or at night.</li>
  <li><strong>Only time lowers your blood alcohol.</strong> Coffee, water, food, a shower or exercise don't. For
  learner, P1 and P2 drivers the limit is zero anyway.</li>
  <li><strong>No phones for L and P drivers.</strong> Not for calls (even hands-free), music, maps or texts, and not
  while stopped at lights or in a queue.</li>
  <li><strong>Speed:</strong> the default limit is 50 km/h in a built-up area and 100 km/h elsewhere. Learner and P1
  drivers may not exceed 90 km/h, and P2 drivers 100 km/h, whatever the signs say. In a shared zone the limit is
  10 km/h and you give way to any pedestrian.</li>
</ul>"""),
        ("after", "What happens after you pass the DKT?", """
<p>Passing gets you a learner licence, which lasts 5 years. If it runs out, you have to pass the DKT again.</p>
<p>If you are under 25, you must hold your Ls for at least 12 months and log at least 120 hours of supervised driving,
including 20 hours at night, before the driving test. The Safer Drivers Course adds 20 bonus hours, and each one-hour
lesson with a licensed instructor can be logged as 3 hours.</p>
<p>Your supervisor must hold a full Australian licence and sit beside you, and their blood alcohol must be under 0.05
with no drugs present. Your L plates go on the outside of the car, front and back (or on a roof sign), with the whole
letter showing. Learners are not allowed to drive in Moore Park, Centennial Park or Parramatta Park in Sydney, and may
not tow at all.</p>
<p>If you are under 25, you can sit the Hazard Perception Test after at least 10 months on your Ls, and a pass stays
valid for 15 months for the driving test, which you can take from 17. If you don't pass the driving test, you can
re-book and try again after 7 days.</p>"""),
        ("prepare", "How should you prepare for the DKT?", """
<p>A simple plan works well. Read the handbook one chapter at a time, and after each chapter answer practice questions
on it. Once you have covered everything, start sitting full mock tests in the 15 + 30 format and keep a close eye on
the road safety part, where one mistake is all you can afford. Every wrong answer is a signal: read the explanation,
look up the handbook page and come back to the question a few days later.</p>
<p>In {SITE_NAME}, NSW mock tests follow this format and end where the real test would. Our guide to
<a href="@/blog/how-to-use-mock-tests-and-mistakes.html">using mock tests and mistakes</a> explains the method, and the
<a href="@/nsw-dkt-practice-test.html">NSW DKT practice test page</a> has the key facts at a glance.</p>""".replace("{SITE_NAME}", SITE_NAME)),
    ]
    return post(
        slug="nsw-driver-knowledge-test-explained",
        title="NSW Driver Knowledge Test Guide | Learners Test Australia",
        h1="How the NSW Driver Knowledge Test works",
        description=("How the NSW Driver Knowledge Test (DKT) works in 2026: 45 questions, pass marks for each section, the "
                     "DKT online, what to study and what comes after your Ls."),
        summary=("The NSW Driver Knowledge Test (DKT) is the multiple-choice test you pass to get a learner licence in New "
                 "South Wales. It is built on the Road User Handbook, and the format the NSW Government publishes is 45 "
                 "questions in two parts: general knowledge (15 questions, 12 to pass) and road safety (30 questions, 29 to "
                 "pass). This guide covers the format, the online option, what to study and what comes next, as checked on "
                 f"{DATE_H}."),
        sections=sections,
        sources=[
            ("Driver Knowledge Test (nsw.gov.au)", SRC["nsw_dkt"]),
            ("Road User Handbook (nsw.gov.au)", SRC["nsw_ruh"]),
            ("Learner driver licence (nsw.gov.au)", SRC["nsw_learner"]),
            ("Driving test (nsw.gov.au)", SRC["nsw_driving_test"]),
        ],
        section_name="NSW",
        keywords=["NSW DKT", "Driver Knowledge Test", "NSW learner licence", "DKT online", "DKT practice test"],
        llms_note="Deep guide to the NSW DKT: format and mistake budget, DKT online, the Road User Handbook, common traps, learner licence rules.",
        related=[
            ("NSW DKT practice test", "nsw-dkt-practice-test.html"),
            ("Give way rules every learner must know", "blog/give-way-rules-for-learner-drivers.html"),
            ("How to use mock tests and mistakes", "blog/how-to-use-mock-tests-and-mistakes.html"),
            ("Hazard perception test in NSW, VIC and QLD", "blog/hazard-perception-test-nsw-vic-qld.html"),
            ("FAQ", "faq.html"),
        ],
    )


# ── Post 2: VIC LPT ───────────────────────────────────────────────────────────────────────────
def post_vic() -> Page:
    sections = [
        ("who", "Who needs to sit the learner permit test?", """
<p>Anyone getting their first car learner permit in Victoria. The permit is issued from age 16, and you can start the
online course at 15 years and 11 months. You also need a Victorian home address, evidence of identity, to be medically
fit to drive, not be disqualified or under a Fines Victoria licence suspension, and to pay the fee.</p>
<p>The learner permit test has two parts: an eyesight check, and a multiple-choice test of road law and road safety
drawn from the Road to Solo Driving handbook.</p>"""),
        ("online", "What is the online learner permit course like?", """
<p>For most people the test now happens online. The learner permit course takes about 4 to 6 hours and finishes with a
final test. It is in English only, the first attempt is free, and you have 12 months to complete it. VicRoads doesn't
publish how many questions the online final test has or what its pass mark is.</p>"""),
        ("in-person", "What happens at an in-person test?", """
<p>You sit the test at a VicRoads Customer Service Centre only if you need another language or an interpreter, or if you
have no computer or internet access. An appointment fee applies, and you should allow about 45 minutes, because the
eyesight test and your permit application happen at the same visit.</p>
<p>The in-person test has 32 multiple-choice questions with three options each, and you need 25 correct, which is 78%.
That comes from the VicRoads practice test page, which says its practice test matches the real one in size and pass
mark. It is offered in 13 languages: Arabic, Chinese (Mandarin), Vietnamese, Turkish, Persian, Cambodian, Sinhalese,
Somali, Albanian, Macedonian, Russian, Serbian and Spanish. If your language isn't offered, you can book a free
interpreter, including Auslan.</p>
<p>Bring original identity documents: photocopies are refused, even certified ones. You need one Category A document
(such as a passport or an Australian birth certificate), one Category B document (such as a Medicare card, a bank card
or a utility bill less than a year old) and proof of your Victorian address. If your eyesight is poor, bring an
eyesight certificate from an optometrist or ophthalmologist; if you have a condition that may affect your driving,
bring a doctor's report.</p>
<p>Once you pass, you pay, have your photo taken and get a paper receipt that lets you start driving straight away. The
card arrives by post in about a week, and a digital permit is accepted too.</p>"""),
        ("covers", "What does the learner permit test cover?", """
<p>The whole Road to Solo Driving handbook (April 2023 edition): the licensing section and all four chapters, on the
challenges of driving, learning to drive, managing risk, and rules and responsibilities. The VicRoads practice test is
a revision aid, and the handbook points out that it doesn't cover everything.</p>
<p>That said, the practice test does show where the emphasis is. When we reviewed it on {DATE_H}, the biggest groups of
questions were giving way, learning to drive (including hazard perception), parking, speed limits and pedestrians.</p>
<p>Don't skip the chapters that sound like background. The handbook's early chapters explain why the rules exist, and
they are testable. For example, the handbook says new drivers are about three times as likely as experienced drivers to
be in a casualty crash, that crash risk jumps to its highest point when you first drive solo on P1, and that new solo
drivers with about 120 hours of supervised practice have roughly 30% lower crash risk than those with about 50 hours.
It also explains hazard perception: spotting and predicting risks and responding in time, which is different from fast
reflexes.</p>""".replace("{DATE_H}", DATE_H)),
        ("unique", "Which Victorian rules are different from other states?", """
<ul>
  <li><strong>Hook turns.</strong> At traffic-light intersections with a hook turn sign, found mainly in central
  Melbourne and inner suburbs, you turn right from the far-left lane. Signal right, move forward keeping as far left as
  you can until you are close to the far side of the road you're turning into, wait there until the lights for that road
  turn green, check nothing is moving in the lane to your right, then turn.</li>
  <li><strong>Trams.</strong> When a tram stops at a stop without a safety zone, stop at the back of the tram without
  going past it, and don't pass while the doors are open. When the doors close and nobody is on the road, you may pass at no more than 10 km/h.</li>
  <li><strong>Phones for L and P drivers.</strong> A phone in a commercially made mounting may only be used for
  navigation or audio set up before you start, and you mustn't touch it, even at red lights. No calls at all, not even
  hands-free, and no voice commands. An unmounted phone mustn't be touched or have anything running on it, and it can't
  sit on your lap (a pocket or pouch is fine).</li>
</ul>"""),
        ("conditions", "What are the learner permit conditions?", """
<ul>
  <li>Carry your permit (card, paper receipt or official digital permit) every time you drive.</li>
  <li>Show L plates on the front and rear of the car, clearly visible from 20 metres.</li>
  <li>Always have a supervisor beside you in the front passenger seat, holding a current full licence (not a
  probationary one) for that type of vehicle.</li>
  <li>Your blood alcohol must be zero. Your supervisor must be under 0.05 and must not drink at all while supervising.</li>
  <li>Don't tow a trailer, caravan or any other vehicle, and remember a car permit covers cars only.</li>
</ul>
<p>Driving without a supervisor is an impoundment offence in Victoria: the car can be impounded, whoever owns it.</p>"""),
        ("next", "How do you get from L plates to P plates?", """
<p>Your permit lasts 10 years. If you'll be under 21 at your licence test, you need at least 120 hours of supervised
driving, 20 or more of them after dark, logged in the myLearners app or the Learner Log Book. From 21 a log book isn't
required. You must hold your permit continuously for at least 12 months if you are under 21, 6 months if you are 21 to
under 25, or 3 months if you are 25 or older.</p>
<p>Before the drive test you pass the Hazard Perception Test, which you can sit from 17 years 11 months. The
probationary licence is available from 18. If you're under 21 when licensed, you spend at least a year on P1 and then at
least three years on P2; if you're 21 or older, you go straight to P2 for at least three years.</p>
<p>Ready to practise? The <a href="@/vic-learner-permit-test-practice.html">VIC learner permit test practice page</a>
sums up the format, and our <a href="@/blog/give-way-rules-for-learner-drivers.html">give way guide</a> covers the
biggest topic in the practice test.</p>"""),
    ]
    return post(
        slug="victorian-learner-permit-test-explained",
        title="VIC Learner Permit Test Explained | Learners Test Australia",
        h1="The Victorian learner permit test explained",
        description=("The Victorian learner permit test explained: the online course, the 32-question in-person test (pass "
                     "25), documents, what it covers and Victoria-only rules."),
        summary=("Victoria's learner permit test (LPT) is how you qualify for a car learner permit. Most people now take it "
                 "online as part of the learner permit course. The in-person test at VicRoads, for people who need another "
                 "language or an interpreter or have no internet, has 32 multiple-choice questions and a pass mark of 25 "
                 "(78%). Both cover the whole Road to Solo Driving handbook. Facts as checked on "
                 f"{DATE_H}."),
        sections=sections,
        sources=[
            ("Learner permit test (VicRoads)", SRC["vic_lpt"]),
            ("Prepare for your learner permit (Transport Victoria)", SRC["vic_prepare_l"]),
            ("Driver handbooks and logbooks (Transport Victoria)", SRC["vic_handbooks"]),
            ("Learner and probationary driver road rules (Transport Victoria)", SRC["vic_lp_rules"]),
            ("Victoria's graduated licensing system (Transport Victoria)", SRC["vic_gls"]),
        ],
        section_name="Victoria",
        keywords=["VIC learner permit test", "Victorian learner test", "LPT", "Road to Solo Driving", "learner permit course"],
        llms_note="Deep guide to the Victorian learner permit test: online course, in-person 32-question test, documents, handbook, VIC-only rules, permit conditions.",
        related=[
            ("VIC learner permit test practice", "vic-learner-permit-test-practice.html"),
            ("Give way rules every learner must know", "blog/give-way-rules-for-learner-drivers.html"),
            ("Hazard perception test in NSW, VIC and QLD", "blog/hazard-perception-test-nsw-vic-qld.html"),
            ("How to use mock tests and mistakes", "blog/how-to-use-mock-tests-and-mistakes.html"),
            ("FAQ", "faq.html"),
        ],
    )


# ── Post 3: QLD written vs PrepL ──────────────────────────────────────────────────────────────
def post_qld() -> Page:
    sections = [
        ("routes", "What are the two routes to a Queensland learner licence?", f"""
<p>Before a car learner licence can be issued in Queensland you must pass one of two knowledge assessments (and be
medically fit to drive). They cover the same rules but work very differently.</p>
<div class="table-wrap"><table>
<caption>Written road rules test and PrepL compared (checked {DATE_H})</caption>
<thead><tr><th scope="col"></th><th scope="col">Written road rules test</th><th scope="col">PrepL</th></tr></thead>
<tbody>
<tr><th scope="row">Format</th><td>30 multiple-choice questions on paper</td><td>Online course of about 4–6 hours, then a 30-question final test</td></tr>
<tr><th scope="row">Pass mark</th><td>Giving way 9 of 10 and road rules 18 of 20, scored separately</td><td>27 of 30 (90%)</td></tr>
<tr><th scope="row">Where</th><td>A licence-issuing centre</td><td>Phone, tablet or computer</td></tr>
<tr><th scope="row">Earliest age</th><td>16</td><td>Enrol from 15 years 11 months</td></tr>
<tr><th scope="row">Cost and retries</th><td>A fee for every attempt; one attempt a day; after a fail, wait until the next working day</td><td>One fee ($29.70 as at 1 July 2026) for 12 months' access; retry after 24 hours at no extra cost</td></tr>
<tr><th scope="row">A pass lasts</th><td>5 years</td><td>5 years</td></tr>
</tbody></table></div>"""),
        ("written", "How does the written road rules test work?", """
<p>You sit the written test on paper at a TMR customer service centre, a participating QGAP office or, in rural and
remote areas, a licence-issuing police station. You must be at least 16.</p>
<p>It has 30 multiple-choice questions in two sections, scored separately. Section one is giving way: 10 questions, and
you need 9. Section two is road rules and driver licence requirements: 20 questions, and you need 18. Fail either section
and you fail the test, however well you did in the other.</p>
<p>No formal time limit is published, but the handbook suggests allowing at least 30 minutes. You pay a fee for every
attempt and can sit only once a day; after a fail you wait until the next working day. The questions are based on the
handbook <em>Your keys to driving in Queensland</em>. When you pass, you receive a driver licence receipt that lets you
start supervised driving until your card arrives in the mail.</p>"""),
        ("prepl", "How does PrepL work?", """
<p>PrepL is Queensland's online learning and assessment course. It takes about 4 to 6 hours and has three sections:
Your driving attitude, Signs and rules, and Sharing the road with others. Assessment pieces are built into the course
and unlock as you progress, and at the end there is a final test of 30 multiple-choice questions. You need 27 correct.</p>
<p>You can enrol from 15 years and 11 months, so your learner licence can be issued on your 16th birthday. One fee, the
same as the written test fee ($29.70 as at 1 July 2026), gives you 12 months' access, and if you fail the final test you
can try again after 24 hours at no extra cost. You still need to show evidence of identity, which you can do at any time
during your enrolment.</p>
<p>PrepL must be your own work. If someone else does it for you, your enrolment can be cancelled, they risk a penalty of
more than $6,900, and you can't enrol again for 6 months.</p>"""),
        ("replace", "Is PrepL replacing the written test?", """
<p>Eventually. The Queensland Government says PrepL will replace the written test, but it isn't compulsory yet. Until it
is, you can choose either route. Once it becomes mandatory, people without internet access may be exempt and sit the
written test instead.</p>"""),
        ("choose", "Which route should you choose?", """
<p>Both lead to the same learner licence and both passes last 5 years, so it comes down to what suits you:</p>
<ul>
  <li><strong>Timing:</strong> PrepL lets you enrol before you turn 16 and have everything ready for your birthday. The
  written test can't be sat until you are 16.</li>
  <li><strong>Retries:</strong> a failed PrepL final test can be retried after 24 hours at no extra cost within your 12
  months. Each written test attempt costs a fee, and you can only sit once a day.</li>
  <li><strong>How you learn:</strong> PrepL is interactive and self-paced. The written test suits people who have
  already studied the handbook and want a single sitting.</li>
  <li><strong>Pass marks:</strong> the written test lets you drop 1 giving-way question and 2 road rules questions;
  PrepL lets you drop 3 questions in total.</li>
  <li><strong>Access:</strong> PrepL needs a phone, tablet or computer and an internet connection.</li>
</ul>"""),
        ("content", "What do both routes test?", """
<p>Giving way matters on both routes. It is a whole section of the written test, and the handbook says learners are
tested on it in detail: unsigned crossroads and T-intersections, STOP and GIVE WAY signs, turning across traffic,
roundabouts, merging, U-turns, driveways, buses and emergency vehicles.</p>
<p>Licence requirements are core content too, not background. Know these learner rules:</p>
<ul>
  <li>Your learner licence lasts 3 years, and you must carry it (card, Digital Licence app or receipt) whenever you drive.</li>
  <li>Your alcohol limit is zero, and your supervisor must not drink alcohol while you are driving under their supervision.</li>
  <li>Your supervisor must hold an open licence for that class, have held one for at least a year, and sit beside you.</li>
  <li>L plates go on the front and rear, readable from 20 metres.</li>
  <li>If you are under 25, you need 100 hours of supervised driving, including 10 at night, in a logbook. Each hour with
  an accredited driver trainer counts as 3 hours, for up to 10 hours of lessons.</li>
  <li>Four or more demerit points in 12 months means a 3-month suspension for a learner.</li>
  <li>You can sit the hazard perception test after 6 months on your learner licence, and the practical test after a year.</li>
</ul>
<p>The current handbook is edition No. 19 from November 2022, so it predates some recent changes, including Queensland's
2026 e-scooter and e-bike rules and fines that are indexed each July. The official pages and the current Road Rules
Regulation have the latest versions.</p>"""),
        ("practise", "How can you practise for either route?", f"""
<p>{SITE_NAME} has mock tests for both: the written test, with separate pass lines for giving way and road rules, and
the PrepL final test. Giving-way questions are drawn as diagrams, and every answer shows the handbook page or rule it
comes from. See the <a href="@/qld-learner-test-practice.html">QLD learner test practice page</a> for the key facts, and
our <a href="@/blog/give-way-rules-for-learner-drivers.html">give way guide</a> for the section that trips most people up.</p>"""),
    ]
    return post(
        slug="qld-written-road-rules-test-vs-prepl",
        title="QLD Road Rules Test vs PrepL | Learners Test Australia",
        h1="QLD written road rules test vs PrepL: which should you do?",
        description=("Queensland's written road rules test vs PrepL compared: questions, pass marks, age, cost, retries and "
                     "what both test, so you can choose your route to your Ls."),
        summary=("Queensland offers two routes to a car learner licence. The written road rules test is 30 questions on "
                 "paper in two separately scored sections: giving way (need 9 of 10) and road rules and licence requirements "
                 "(need 18 of 20). PrepL is an online course of about 4 to 6 hours with a 30-question final test (need 27). "
                 f"PrepL isn't compulsory yet, so you can choose. Facts as checked on {DATE_H}."),
        sections=sections,
        sources=[
            ("Driver tests, written and online (qld.gov.au)", SRC["qld_tests"]),
            ("PrepL online learning and assessment (qld.gov.au)", SRC["qld_prepl"]),
            ("Getting a learner licence (qld.gov.au)", SRC["qld_getting_learner"]),
            ("Rules for learner driving (qld.gov.au)", SRC["qld_learner_rules"]),
            ("Your keys to driving in Queensland (Queensland Government publications)", SRC["qld_handbook"]),
        ],
        section_name="Queensland",
        keywords=["QLD written road rules test", "PrepL", "PrepL final test", "Queensland learner licence", "QLD learner test"],
        llms_note="Comparison of the Queensland written road rules test and PrepL: format, pass marks, age, cost, retries, what both test.",
        related=[
            ("QLD learner test practice", "qld-learner-test-practice.html"),
            ("Give way rules every learner must know", "blog/give-way-rules-for-learner-drivers.html"),
            ("How to use mock tests and mistakes", "blog/how-to-use-mock-tests-and-mistakes.html"),
            ("Hazard perception test in NSW, VIC and QLD", "blog/hazard-perception-test-nsw-vic-qld.html"),
            ("FAQ", "faq.html"),
        ],
    )


# ── Post 4: Give way rules ────────────────────────────────────────────────────────────────────
def post_give_way() -> Page:
    sections = [
        ("meaning", "What does “give way” actually mean?", """
<p>To give way is to slow down and, if needed, stop so that you don't collide with another road user. If you have
already stopped, you stay stopped until it is safe to go. Giving way doesn't always mean stopping, but it always means
being ready to.</p>
<p>Give-way rules apply to bicycles, e-scooter riders and horse riders just as they do to cars and trucks.</p>"""),
        ("signs", "What do STOP and GIVE WAY signs require?", """
<p>At a <strong>STOP</strong> sign or stop line, come to a complete stop behind the line, every time, even when nothing
is coming. Then give way as you would at a give way sign. At a <strong>GIVE WAY</strong> sign or line, slow down and be
ready to stop; if the way is clear you don't have to stop.</p>
<p>At either sign, give way to every vehicle already in, entering or approaching the intersection, and to pedestrians.
There are three exceptions: a vehicle doing a U-turn, a vehicle turning left from a slip lane, and an oncoming vehicle
that is turning right and also faces a stop or give way sign or line.</p>
<p>The painted lines carry the same meaning as the signs, so if a sign has been knocked down, a continuous line still
means stop and a broken line still means give way.</p>
<p>A STOP sign isn't “stronger” than a GIVE WAY sign. When two drivers face each other at signs, both give way to other
traffic first, and then the normal rules decide between them: the driver turning right gives way to the one going
straight or turning left.</p>"""),
        ("uncontrolled", "Who goes first where there are no signs or lights?", """
<p>At a crossroads with no signs, lines or lights, give way to vehicles coming from your right. This “give way to the
right” rule only applies at these unsigned intersections; T-intersections, roundabouts and signed intersections have
their own rules.</p>
<ul>
  <li><strong>Turning right:</strong> you also give way to oncoming vehicles going straight or turning left, and to
  pedestrians crossing the road you're entering.</li>
  <li><strong>Turning left:</strong> give way to vehicles approaching from your right, and to pedestrians crossing the
  road you turn into.</li>
  <li><strong>Two drivers turning right from opposite directions</strong> can turn at the same time, passing in front of
  each other.</li>
  <li><strong>A vehicle doing a U-turn</strong> gives way to everyone else, including you.</li>
</ul>"""),
        ("t-intersections", "How do T-intersections work?", """
<p>A T-intersection is where one road ends at another. If you are on the road that ends, you give way to all vehicles on
the road that continues, from both directions, whether they are turning or not. If you are on the continuing road and
turning right into the road that ends, you give way to oncoming vehicles going straight or turning left.</p>
<p>Watch for continuing roads that bend around a corner, often shown by a continuity line. Traffic following the bend
has priority, so drivers leaving the bend to go into the other road, or coming out of it, give way.</p>"""),
        ("lights", "What about traffic lights?", """
<ul>
  <li><strong>Turning right on a plain green:</strong> give way to oncoming traffic and wait for a safe gap. If the
  lights change while you are in the intersection, finish your turn when it is safe.</li>
  <li><strong>Green arrow:</strong> oncoming traffic faces red, but still watch for pedestrians.</li>
  <li><strong>Flashing yellow:</strong> you may go, applying the normal give-way rules.</li>
  <li><strong>Lights off:</strong> if a stop sign is fitted to the signal post (NSW's version has three black dots),
  treat the intersection as a stop sign. Otherwise use the normal rules for intersections without signs.</li>
  <li><strong>Blocked road ahead:</strong> don't enter the intersection, even on green, unless there is room for your
  car on the other side.</li>
</ul>"""),
        ("roundabouts", "Who do you give way to at a roundabout?", """
<p>Every vehicle already in the roundabout, whether it is on your right, straight ahead or on your left. A common wrong
belief is that you only give way to the right. Keep watching riders already in the roundabout, who are harder to see,
and remember a vehicle beside or ahead of you may be about to exit across your path.</p>"""),
        ("pedestrians", "When must you give way to pedestrians, and when merging?", """
<p>When you turn at an intersection, give way to pedestrians crossing the road you are turning into, even when you have
a green light and they are crossing on the walk signal. When entering or leaving a driveway or car park, give way to
pedestrians and riders on the footpath and to vehicles on the road.</p>
<p>When your marked lane ends, or you change lanes, give way to vehicles already in the lane you're moving into. Where
two lines of traffic merge with no lane lines at all, the vehicle in front goes first (the “zip” merge).</p>"""),
        ("emergency", "What about emergency vehicles and police?", """
<p>If an emergency vehicle is approaching with its siren or flashing red or blue lights, get out of its way as soon as
it is safe, usually by slowing and moving left, even if you have a green light. Police or authorised people directing
traffic override lights and signs, so always follow their directions.</p>"""),
        ("differences", "Where do NSW, VIC and QLD differ?", """
<p>The rules above come from the national Australian Road Rules, so they apply in all three states. A few local details
differ:</p>
<ul>
  <li><strong>Hook turns (VIC):</strong> at intersections with a hook turn sign, mainly in central Melbourne, you turn
  right from the far-left lane.</li>
  <li><strong>Trams:</strong> in Victoria you give way to trams entering or approaching a roundabout, and Queensland has
  the same rule for the Gold Coast light rail. In NSW, when light rail is at an intersection, wait until the intersection is
  clear and never move into its path.</li>
  <li><strong>Giving way to buses:</strong> all three have “give way to buses” rules for buses pulling out from a stop
  and signalling. Victoria applies it in built-up areas; Queensland on roads with a limit of 70 km/h or less, for drivers
  in the left lane.</li>
  <li><strong>U-turns at traffic lights:</strong> in NSW you may only U-turn at lights where a “U-turn permitted” sign is
  shown. Transport Victoria's guidance says Victoria allows U-turns unless a sign or line prohibits them. Check your own
  state's rule before relying on it.</li>
</ul>"""),
        ("weight", "How much do give-way questions count in the test?", """
<p>A lot. In Queensland's written test, giving way is a whole 10-question section and you need 9 right. In Victoria it
was the biggest single group in the VicRoads practice test when we reviewed it on {DATE_H}. In NSW, intersections and
giving way is one of the largest topics in the published question list. Practise with diagrams until each situation
feels obvious; our <a href="@/blog/how-to-use-mock-tests-and-mistakes.html">mock test guide</a> explains how to turn
mistakes into reviews.</p>""".replace("{DATE_H}", DATE_H)),
    ]
    return post(
        slug="give-way-rules-for-learner-drivers",
        title="Give Way Rules for Learner Drivers | Learners Test Australia",
        h1="Give way rules every learner driver must know",
        description=("Give way rules for learner drivers in NSW, VIC and QLD: STOP and GIVE WAY signs, give way to the right, "
                     "T-intersections, roundabouts and state differences."),
        summary=("Giving way means slowing down and, if needed, stopping to avoid a collision, then staying stopped until it "
                 "is safe. The core rules are national, so they are the same in NSW, VIC and QLD: stop fully at STOP signs, "
                 "give way to the right at intersections with no signs or lights, the road that ends gives way at a "
                 "T-intersection, right-turners give way to oncoming traffic, and you give way to every vehicle already in a "
                 f"roundabout. A few details differ by state. As checked on {DATE_H}."),
        sections=sections,
        sources=[
            ("Road User Handbook (nsw.gov.au)", SRC["nsw_ruh"]),
            ("Driver handbooks, including Road to Solo Driving (Transport Victoria)", SRC["vic_handbooks"]),
            ("Giving way (qld.gov.au)", SRC["qld_give_way"]),
            ("Roundabouts (qld.gov.au)", SRC["qld_roundabouts"]),
        ],
        section_name="Road rules",
        keywords=["give way rules", "give way to the right", "T-intersection rules", "roundabout rules", "learner driver"],
        llms_note="Give way rules for NSW, VIC and QLD learners: signs, unsigned intersections, T-intersections, lights, roundabouts, pedestrians, state differences.",
        related=[
            ("QLD learner test practice", "qld-learner-test-practice.html"),
            ("VIC learner permit test practice", "vic-learner-permit-test-practice.html"),
            ("NSW DKT practice test", "nsw-dkt-practice-test.html"),
            ("How to use mock tests and mistakes", "blog/how-to-use-mock-tests-and-mistakes.html"),
        ],
    )


# ── Post 5: Mock tests and mistakes ───────────────────────────────────────────────────────────
def post_mocks() -> Page:
    sections = [
        ("budget", "What is a mistake budget?", f"""
<p>Every learner knowledge test has a pass mark, and the gap between the number of questions and the pass mark is your
mistake budget: how many you can get wrong and still pass. Where a test has sections, each section has its own budget,
and you can't borrow from one to cover another.</p>
<div class="table-wrap"><table>
<caption>Mistake budgets by test (formats as published, checked {DATE_H})</caption>
<thead><tr><th scope="col">Test</th><th scope="col">Section</th><th scope="col">Questions</th><th scope="col">Pass mark</th><th scope="col">Mistakes allowed</th></tr></thead>
<tbody>
<tr><th scope="row" rowspan="2">{chip('NSW')} DKT</th><td>General knowledge</td><td>15</td><td>12</td><td>3</td></tr>
<tr><td>Road safety</td><td>30</td><td>29</td><td>1</td></tr>
<tr><th scope="row">{chip('VIC')} Learner permit test (in person)</th><td>All questions</td><td>32</td><td>25</td><td>7</td></tr>
<tr><th scope="row" rowspan="2">{chip('QLD')} Written road rules test</th><td>Giving way</td><td>10</td><td>9</td><td>1</td></tr>
<tr><td>Road rules and licence requirements</td><td>20</td><td>18</td><td>2</td></tr>
<tr><th scope="row">{chip('QLD')} PrepL final test</th><td>All questions</td><td>30</td><td>27</td><td>3</td></tr>
</tbody></table></div>
<p>Look at where the budget is tight. One mistake in NSW road safety or Queensland giving way is all you get. That is
where a mock test tells you the most.</p>"""),
        ("when", "When should you start doing mock tests?", """
<p>Not on day one. A mock test measures what you know; it isn't the best way to learn it. Start by reading your state's
handbook a chapter at a time and answering practice questions on each topic. In the app, a 12-question quick check
finds your starting point, and the daily plan mixes reviews, mistakes and new questions.</p>
<p>Once you've worked through every topic at least once, start sitting full mock tests. From then on, alternate: mock
test, fix the mistakes, practise, and mock test again.</p>"""),
        ("sit", "How do you sit a mock test like the real thing?", """
<ul>
  <li>Find a quiet spot and set aside enough time to finish in one go.</li>
  <li>No notes, no handbook and no looking things up. The point is to find the gaps.</li>
  <li>Answer every question, and flag the ones you're unsure of to review afterwards.</li>
  <li>Read the whole question and every option before choosing. Many wrong options are tempting because they are
  almost right.</li>
</ul>
<p>In the NSW mock, the test ends where the real DKT would, as soon as passing is no longer possible, and you can choose
to keep practising the remaining questions. That early stop is a useful jolt: it shows exactly how little room there is
in the road safety section.</p>"""),
        ("mistakes", "What should you do with your mistakes?", """
<p>Your mistakes are the most valuable part of a mock test. For each one:</p>
<ol>
  <li><strong>Read the explanation</strong> and the rule it comes from. In the app every answer shows the handbook page
  or road rule.</li>
  <li><strong>Work out why you got it wrong.</strong> Did you not know the rule, misread the question, or mix it up with
  a similar rule?</li>
  <li><strong>Look it up.</strong> Reading the handbook page puts the rule in context and often clears up neighbouring
  rules too.</li>
  <li><strong>Come back to it later.</strong> Answering it again a few days later, rather than straight away, is what
  makes it stick.</li>
</ol>
<p>Don't ignore your lucky guesses either. A correct answer you guessed is a mistake waiting to happen. The app asks
“How sure were you?” after each answer (knew it, unsure or guessed) and uses your reply to decide when to show the
question again.</p>"""),
        ("results", "How should you read your results?", """
<p>Look at each section against its own pass line, not just your total. A score of 40 out of 45 in the NSW DKT sounds
comfortable, but if 2 of those 5 mistakes were in road safety, it is a fail. In the app, results show every section
against its pass line, and the Today screen shows your weakest topic.</p>
<p>Over time, the pass-chance estimate combines your recent answers into a single number. Treat it as a guide, not a
guarantee: it is based on practice questions, and the official test is set by your state. Premium adds a forecast for
each section, which helps when one section is holding you back.</p>"""),
        ("how-many", "How many mock tests should you do?", """
<p>There is no magic number. A better target is consistency: pass several mock tests in a row with a little room to
spare in every section, especially the tight ones. If you pass one and fail the next, keep going.</p>
<p>Aim to understand the rules rather than memorise answers. Our questions are original, not the official ones, so
recognising a question won't help you in the real test; knowing the rule will. In the free version you get one mock test
a day, plus another each time you choose to watch a short ad. Premium makes them unlimited.</p>"""),
        ("traps", "Which traps catch people out?", """
<ul>
  <li><strong>Other states' numbers.</strong> Learning from a mix of sources can teach you the wrong figures. Supervised
  hours are a classic: NSW asks under-25s for 120 hours including 20 at night; Victoria asks for 120 hours, 20 or more
  after dark, if you'll be under 21 at your licence test; Queensland asks under-25s for 100 hours including 10 at night.</li>
  <li><strong>Old rules.</strong> Rules change. Check that what you're learning matches the current handbook and your
  state's website.</li>
  <li><strong>Rushing the easy ones.</strong> Most mistakes on questions you know come from reading too fast.</li>
</ul>
<p>Ready to start? See the practice pages for <a href="@/nsw-dkt-practice-test.html">NSW</a>,
<a href="@/vic-learner-permit-test-practice.html">VIC</a> and <a href="@/qld-learner-test-practice.html">QLD</a>.</p>"""),
    ]
    return post(
        slug="how-to-use-mock-tests-and-mistakes",
        title="Mock Test Tips for Learners | Learners Test Australia",
        h1="How to use mock tests and mistakes to prepare for your learner test",
        description=("How to use mock tests for your learner test: know your mistake budget in each section, sit mocks like "
                     "the real test and turn every mistake into a review."),
        summary=("Mock tests work best when you sit them like the real test and then study your mistakes. Know your mistake "
                 "budget: 1 in the NSW DKT road safety section, 3 in NSW general knowledge, 7 in the Victorian in-person test, "
                 "1 in Queensland's giving-way section, 2 in its road rules section and 3 in the PrepL final test. Then read "
                 "each explanation, look up the rule and come back to the question a few days later."),
        sections=sections,
        sources=[
            ("NSW Driver Knowledge Test (nsw.gov.au)", SRC["nsw_dkt"]),
            ("Victorian learner permit test (VicRoads)", SRC["vic_lpt"]),
            ("Queensland driver tests (qld.gov.au)", SRC["qld_tests"]),
            ("Queensland PrepL (qld.gov.au)", SRC["qld_prepl"]),
        ],
        section_name="Study tips",
        keywords=["mock test", "learner test practice", "DKT practice test", "study tips", "learners permit test"],
        llms_note="Study method: mistake budgets per test and section, when and how to sit mock tests, reviewing mistakes, reading results.",
        related=[
            ("NSW DKT practice test", "nsw-dkt-practice-test.html"),
            ("VIC learner permit test practice", "vic-learner-permit-test-practice.html"),
            ("QLD learner test practice", "qld-learner-test-practice.html"),
            ("App features", "features.html"),
        ],
    )


# ── Post 6: Hazard perception ─────────────────────────────────────────────────────────────────
def post_hpt() -> Page:
    sections = [
        ("what", "What is hazard perception?", """
<p>Hazard perception is the skill of spotting possible dangers on the road, judging how risky they are, predicting what
might happen, and responding in time. Victoria's Road to Solo Driving handbook stresses that it is not the same as quick
reactions: young drivers often react fast but are slower to anticipate. It grows only with plenty of varied driving
experience, and the aim is that most situations on the road don't take you by surprise.</p>
<p>Hazards are anything that could lead to a crash: vehicles ahead, behind, beside you or in side streets, a truck
double-parked, trains, pedestrians, bicycle riders, weather, potholes, heavy traffic, tight curves and crests you can't
see over.</p>"""),
        ("where", "Where does the hazard perception test fit in each state?", f"""
<p>In all three states the hazard perception test (HPT) comes during your learner period, after the knowledge test
and before the practical driving test.</p>
<div class="table-wrap"><table>
<caption>Hazard perception test by state (checked {DATE_H})</caption>
<thead><tr><th scope="col">State</th><th scope="col">When you can sit it</th><th scope="col">How long a pass lasts</th></tr></thead>
<tbody>
<tr><th scope="row">{chip('NSW')}</th><td>If you are under 25, after at least 10 months on your Ls</td><td>15 months, for the driving test</td></tr>
<tr><th scope="row">{chip('VIC')}</th><td>From 17 years 11 months, with a current Victorian learner permit</td><td>Pass the drive test within 12 months, or sit the HPT again</td></tr>
<tr><th scope="row">{chip('QLD')}</th><td>After holding your learner licence for at least 6 months; required for every car learner, whatever their age</td><td>You pass it once</td></tr>
</tbody></table></div>"""),
        ("nsw", "What should you know about the HPT in NSW?", """
<p>In NSW the Hazard Perception Test is the second of three tests: the DKT gets you your Ls, the HPT comes during your
learner period, and the driving test gets you your P1 licence. If you are under 25, you can only sit it after at least 10
months on your learner licence, and your pass stays valid for 15 months for the driving test. The NSW Government's HPT
page explains the current format and how to book.</p>"""),
        ("vic", "What should you know about the HPT in Victoria?", """
<p>In Victoria you must pass the Hazard Perception Test before the drive test. You can sit it from 17 years 11 months if
you hold a current Victorian learner permit. VicRoads describes it as 25 short video clips, taking up to 45 minutes, in
which you choose whether to slow down, stop or keep going. After you pass, you have 12 months to pass the drive test;
otherwise you sit the HPT again.</p>"""),
        ("qld", "What should you know about the HPT in Queensland?", """
<p>Since 1 July 2021 every car learner in Queensland, of any age, must pass the hazard perception test before the
practical test. You can sit it after holding your learner licence for at least 6 months, and your logbook doesn't need
to be finished first. It is done online only, not at service centres, using computer-generated 3D video clips of
situations that crash data shows are hard for new drivers, and you only need to pass it once. The fee was $42.70 as at
1 July 2026. If you turn up to the practical test without an HPT pass, the test is cancelled and the fee isn't
refunded.</p>"""),
        ("build", "How do you build hazard perception skill?", """
<p>Mostly by driving, with a supervisor, in as many different conditions as you can. The Victorian handbook's advice
applies everywhere:</p>
<ul>
  <li><strong>Scan the whole scene.</strong> Keep looking far ahead, to both sides and in your mirrors, rather than
  staring at the car in front.</li>
  <li><strong>Know your blind spots.</strong> Every car has areas no mirror shows, however well the mirrors are set.
  Head-check with a quick glance over your shoulder before changing lanes, merging, pulling out, reversing or
  overtaking.</li>
  <li><strong>Practise in variety:</strong> at night, in the wet, in busy and quiet traffic, on roads with different speed
  limits, and on sealed and gravel surfaces.</li>
  <li><strong>Drive little and often.</strong> Frequent short drives of 10 minutes to an hour are worth more than a few
  long ones, especially early on.</li>
</ul>
<p>The supervised hours each state asks for exist partly for this reason: NSW asks under-25s for 120 hours, Victoria
asks for 120 hours if you'll be under 21 at your licence test, and Queensland asks under-25s for 100 hours.</p>"""),
        ("app", "Can an app help with hazard perception?", f"""
<p>An app can't replace time behind the wheel, but it can help you practise the thinking. {SITE_NAME} has illustrated
traffic scenes, drawn from above, where you tap the hazard you should be ready for and then read why it matters: a
person waiting between parked cars, a ball on the road with a child nearby, a parked car signalling to pull out, or
a kangaroo beside a country road at dusk. A few sample scenes are free,
and Premium unlocks the full set. Each state also has a guide to its HPT.</p>
<p>The scenes are still images for practice. They are not a copy of any official test, which uses video clips. For the
knowledge test side, see our <a href="@/blog/how-to-use-mock-tests-and-mistakes.html">mock test guide</a> and the
<a href="@/features.html">feature tour</a>.</p>"""),
    ]
    return post(
        slug="hazard-perception-test-nsw-vic-qld",
        title="Hazard Perception Test Explained | Learners Test Australia",
        h1="Hazard perception test: what it is in NSW, VIC and QLD",
        description=("The hazard perception test (HPT) in NSW, VIC and QLD: what hazard perception is, when you can sit the "
                     "test, how long a pass lasts and how to build the skill."),
        summary=("Hazard perception is the skill of spotting possible dangers early, judging how risky they are and "
                 "responding in time. In NSW, Victoria and Queensland you sit a hazard perception test (HPT) during your "
                 "learner period, after the knowledge test and before the practical driving test. When you can sit it and "
                 f"how long a pass lasts differ by state. Facts as checked on {DATE_H}."),
        sections=sections,
        sources=[
            ("Hazard Perception Test (nsw.gov.au)", SRC["nsw_hpt"]),
            ("Hazard perception test (VicRoads)", SRC["vic_hpt"]),
            ("Driver tests, written and online (qld.gov.au)", SRC["qld_tests"]),
            ("Driver licence progression (qld.gov.au)", SRC["qld_progression"]),
        ],
        section_name="Hazard perception",
        keywords=["hazard perception test", "HPT NSW", "HPT VIC", "HPT QLD", "hazard perception practice"],
        llms_note="Hazard perception explained, and the HPT in NSW (after 10 months, valid 15 months), VIC (from 17y11m, 25 clips) and QLD (after 6 months, online).",
        related=[
            ("App features", "features.html"),
            ("NSW DKT practice test", "nsw-dkt-practice-test.html"),
            ("VIC learner permit test practice", "vic-learner-permit-test-practice.html"),
            ("QLD learner test practice", "qld-learner-test-practice.html"),
        ],
    )


POSTS = [post_nsw, post_vic, post_qld, post_give_way, post_mocks, post_hpt]


def blog_index(posts: list[Page]) -> Page:
    crumbs = [("Home", ""), BLOG_CRUMB]
    cards = []
    for p in posts:
        h1 = p.llms_title
        cards.append(
            f'<article class="card post-card"><span class="tag">{esc(p.jsonld[0]["articleSection"])}</span>'
            f'<h2><a href="@/{p.path}">{esc(h1)}</a></h2>'
            f'<p class="post-meta">By {DEVELOPER} · <time datetime="{DATE}">{DATE_H}</time></p>'
            f"<p>{esc(p.description)}</p></article>"
        )
    body = page_head(
        "Learner driver guides",
        "Plain-English guides to the learner knowledge tests in NSW, Victoria and Queensland, written from official sources.",
        crumbs,
        eyebrow="Guides",
    ) + f"""
<div class="content"><div class="container">
<p class="note">Every fact in these guides was checked against official sources on {DATE_H}, and each guide links to
them. Rules change, so the official website is always the final word.</p>
<div class="post-list">{''.join(cards)}</div>
</div></div>"""
    ld = {
        "@type": "Blog",
        "@id": BASE + "blog/#blog",
        "name": f"{SITE_NAME} guides",
        "url": BASE + "blog/",
        "inLanguage": "en-AU",
        "publisher": organization(full=False),
        "blogPost": [{"@type": "BlogPosting", "headline": p.llms_title, "url": BASE + p.path, "datePublished": DATE} for p in posts],
    }
    return Page(
        path="blog/index.html",
        title="Learner Driver Guides | Learners Test Australia",
        description=("Guides for learner drivers: how the NSW DKT, VIC learner permit test and QLD road rules test work, give "
                     "way rules, mock test tips and hazard perception."),
        body=body,
        nav="blog",
        crumbs=crumbs,
        jsonld=[ld],
        priority="0.8",
        changefreq="weekly",
        llms_note="Index of the learner driver guides.",
    )
