"""State landing pages: NSW DKT, VIC learner permit test, QLD written test and PrepL, SA theory test and myLs,
WA learner's permit, TAS driver knowledge test, ACT learner licence knowledge test and NT driver knowledge test.

Every fact comes from content-src/coverage/{nsw,vic,qld,sa,wa,tas,act,nt}.md in the app repository (checked
30 September 2026), including the section 7 corrections. Facts those maps mark "verify" are not stated as facts.
Rules followed for the newer pages:
  WA   the official question count and pass mark come only from DTMI pages (map V-01), so they are not stated;
       every WA fact below comes from WA legislation. The WA transport site is linked, never quoted.
  ACT  the restricted course and test names in act.md 1.3 are never used, and no question is called mandatory.
  NT   nt.gov.au is all rights reserved: facts only, in our own words.
"""
from sitelib import (
    DATE_H, DISCLAIMER, SITE_NAME, SRC, Page, chip, ext, faq_block, faq_ld, icon, page_head, source_box,
)
from pages_core import coming_soon


def facts_table(caption: str, rows: list[tuple[str, str]]) -> str:
    trs = "".join(f'<tr><th scope="row">{k}</th><td>{v}</td></tr>' for k, v in rows)
    return f'<div class="table-wrap"><table><caption>{caption}</caption><tbody>{trs}</tbody></table></div>'


def related(links: list[tuple[str, str]]) -> str:
    lis = "".join(f'<li><a href="@/{p}">{t}</a></li>' for t, p in links)
    return f'<div class="card aside-card"><h2>Related guides</h2><ul>{lis}</ul></div>'


def app_cta(state: str, extra: str = "") -> str:
    """App call to action with the shared DISCLAIMER; `extra` names the state bodies the app is not connected to."""
    note = f" {extra}" if extra else ""
    return (f'<section class="callout light-cta" aria-labelledby="cta-{state}"><h2 id="cta-{state}" style="margin-top:0">'
            f"Practise with {SITE_NAME}</h2>"
            f"<p>{DISCLAIMER}{note}</p>{coming_soon('light')}</section>")


RELATED_NEW = [
    ("Learner tests by state", "states.html"),
    ("Give way rules every learner must know", "blog/give-way-rules-for-learner-drivers.html"),
    ("How to use mock tests and mistakes", "blog/how-to-use-mock-tests-and-mistakes.html"),
    ("App features", "features.html"),
    ("FAQ", "faq.html"),
]


# ── NSW ───────────────────────────────────────────────────────────────────────────────────────
NSW_FAQ = [
    ("How many questions are in the NSW DKT?",
     "<p>The format published by the NSW Government is 45 multiple-choice questions: 15 general knowledge questions, "
     "where you need 12 correct, and 30 road safety questions, where you need 29 correct.</p>"),
    ("How many questions can you get wrong in the DKT?",
     "<p>Up to 3 in the general knowledge section and 1 in the road safety section. A 4th wrong answer in general "
     "knowledge, or a 2nd in road safety, ends the test.</p>"),
    ("Is there a time limit for the DKT?",
     "<p>No time limit is published for the in-person DKT.</p>"),
    ("Can I do the DKT online in NSW?",
     "<p>Yes. The DKT online is a course of about 4 to 6 hours with a final test, and you can start it from 15 years and "
     "11 months. The number of questions and pass mark of its final test are not published.</p>"),
    ("Are the questions in Learners Test Australia the real DKT questions?",
     "<p>No. They are original practice questions written for the app and checked against the Road User Handbook "
     "(edition 02/2026). The app is independent and not connected to the NSW Government.</p>"),
]


def nsw() -> Page:
    crumbs = [("Home", ""), ("States", "states.html"), ("NSW DKT practice test", "nsw-dkt-practice-test.html")]
    body = page_head(
        "NSW DKT practice test: the Driver Knowledge Test explained",
        "What's in the NSW Driver Knowledge Test, the pass marks for each section, the online option, and how to practise for it.",
        crumbs,
        eyebrow=f"{chip('NSW')} New South Wales",
    ) + f"""
<div class="content"><div class="container two-col">
<article class="prose">
<div class="answer-box"><p class="answer-label">Quick answer</p>
<p>The NSW Driver Knowledge Test (DKT) is the multiple-choice test you pass to get a learner licence in New South Wales.
The format published by the NSW Government is 45 questions in two sections: 15 general knowledge questions, where you
need 12 correct, and 30 road safety questions, where you need 29 correct. There is no time limit, and the test ends as
soon as passing is no longer possible.</p></div>

{facts_table("NSW DKT at a glance (checked " + DATE_H + ")", [
    ("Test", "Driver Knowledge Test (DKT), car (class C)"),
    ("Questions", "45 multiple choice"),
    ("Sections and pass marks", "General knowledge: 12 of 15. Road safety: 29 of 30."),
    ("Ends early", "After a 4th wrong answer in general knowledge or a 2nd in road safety"),
    ("Time limit", "None published"),
    ("Ways to sit it", "In person from 16, or the DKT online course and final test from 15 years 11 months"),
    ("Based on", "Road User Handbook, edition 02/2026"),
])}

<h2>How many questions are in the NSW DKT, and what is the pass mark?</h2>
<p>The in-person DKT is a computer test with questions drawn at random from a question bank. It has two parts, and you
must pass both. In the 15-question general knowledge part you can afford 3 mistakes. In the 30-question road safety
part you can afford only 1. That makes road safety the part to take most seriously: two slips and the test is over,
however well the rest went.</p>
<p class="note">The NSW Government sets out this 45-question structure on its knowledge test pages (it is spelled out on
the rider knowledge test page), and the car DKT is reported to use the same structure. Check the official DKT page
when you book.</p>

<h2>Can you do the DKT online?</h2>
<p>Yes. Since 2024 NSW has offered the DKT online: a course of about 4 to 6 hours with a final test at the end, open
from 15 years and 11 months. The NSW Government does not publish the number of questions or the pass mark for the
online final test. Both versions are built on the Road User Handbook, so the same study covers either route.</p>

<h2>How old do you need to be?</h2>
<ul>
  <li><strong>DKT online:</strong> from 15 years and 11 months.</li>
  <li><strong>DKT in person, and the learner licence itself:</strong> from 16.</li>
  <li><strong>Driving test for your P1 licence:</strong> from 17.</li>
</ul>

<h2>What topics are in the NSW DKT?</h2>
<p>The DKT covers the Road User Handbook: licences, safe driving (speed, alcohol, drugs, seatbelts, phones and fatigue),
sharing the road with pedestrians, cyclists and heavy vehicles, stopping, giving way and turning, overtaking and
merging, lanes and markings, parking, hazards, vehicle safety and penalties. In the NSW Government's published 2018
question list, the topics with the most questions were pedestrians, intersections and giving way, traffic signs, safe
following and stopping distances, and traffic lights.</p>
<p>A few NSW rules that learners often get wrong:</p>
<ul>
  <li>Learner, P1 and P2 drivers must have a zero blood alcohol concentration.</li>
  <li>Learner, P1 and P2 drivers may not use a phone at all while driving, not even hands-free or when stopped at lights.</li>
  <li>Learner and P1 drivers may not go faster than 90 km/h, and P2 drivers 100 km/h, even where signs allow more.</li>
  <li>L plates go on the outside of the car, front and back (or on a roof sign), with the whole letter visible.</li>
  <li>Learners may not drive in Sydney's Moore Park, Centennial Park or Parramatta Park.</li>
  <li>In good conditions, keep at least a 3-second gap to the vehicle ahead.</li>
</ul>

<h2>What happens after you pass the DKT?</h2>
<p>You get a learner licence, valid for 5 years (if it expires, you must pass the DKT again). If you are under 25, you
need to hold it for at least 12 months and log at least 120 hours of supervised driving, 20 of them at night, before
the driving test. The Safer Drivers Course earns 20 bonus hours, and each hour-long lesson with a licensed instructor
can be logged as 3 hours. Your supervisor must hold a full Australian licence and sit beside you.</p>
<p>Next comes the Hazard Perception Test: if you are under 25, you can sit it only after at least 10 months on your
Ls, and a pass stays valid for 15 months for the driving test. Our <a href="@/blog/hazard-perception-test-nsw-vic-qld.html">hazard
perception guide</a> explains what it tests.</p>

<h2>How to practise for the NSW DKT with Learners Test Australia</h2>
<ul class="check-list">
  <li>Mock DKTs in the 15 + 30 format, ending where the real test would once passing is no longer possible.</li>
  <li>More than 400 original NSW questions, checked against the Road User Handbook (edition 02/2026).</li>
  <li>Every answer explained, with the handbook page and road rule it comes from.</li>
  <li>A daily plan of reviews and mistakes, so road safety questions become second nature before test day.</li>
</ul>
<p>For a deeper walk-through, read <a href="@/blog/nsw-driver-knowledge-test-explained.html">how the NSW Driver
Knowledge Test works</a> and <a href="@/blog/give-way-rules-for-learner-drivers.html">the give way rules every
learner must know</a>.</p>

{faq_block(NSW_FAQ, heading="NSW DKT questions people ask", hid="nsw-faq")}

{source_box([
    ("Driver Knowledge Test (nsw.gov.au)", SRC["nsw_dkt"]),
    ("Road User Handbook (nsw.gov.au)", SRC["nsw_ruh"]),
    ("Learner driver licence (nsw.gov.au)", SRC["nsw_learner"]),
    ("Hazard Perception Test (nsw.gov.au)", SRC["nsw_hpt"]),
])}
{app_cta('nsw')}
</article>
<aside>{related([
    ("How the NSW Driver Knowledge Test works", "blog/nsw-driver-knowledge-test-explained.html"),
    ("Give way rules every learner must know", "blog/give-way-rules-for-learner-drivers.html"),
    ("How to use mock tests and mistakes", "blog/how-to-use-mock-tests-and-mistakes.html"),
    ("Hazard perception test in NSW, VIC and QLD", "blog/hazard-perception-test-nsw-vic-qld.html"),
    ("Learner tests by state", "states.html"),
    ("FAQ", "faq.html"),
])}</aside>
</div></div>"""
    return Page(
        path="nsw-dkt-practice-test.html",
        title="NSW DKT Practice Test 2026 | Learners Test Australia",
        description=("NSW DKT practice: the Driver Knowledge Test has 45 questions in two sections (pass 12 of 15 and "
                     "29 of 30). Format, online DKT, topics and how to prepare."),
        body=body,
        nav="states",
        crumbs=crumbs,
        jsonld=[faq_ld(NSW_FAQ)],
        priority="0.9",
        llms=True,
        llms_title="NSW DKT practice test",
        llms_note="NSW Driver Knowledge Test: 45 questions (15 general knowledge, pass 12; 30 road safety, pass 29), online DKT, ages, topics, next steps.",
    )


# ── VIC ───────────────────────────────────────────────────────────────────────────────────────
VIC_FAQ = [
    ("How many questions are in the VIC learner permit test?",
     "<p>The in-person learner permit test has 32 multiple-choice questions with three options each, and you need 25 "
     "correct (78%), according to VicRoads' practice test page. The size and pass mark of the online final test are "
     "not published.</p>"),
    ("Can I do the Victorian learner permit test online?",
     "<p>Yes, and it is now the default. The online learner permit course takes about 4 to 6 hours and ends with a final "
     "test. It is in English only, the first attempt is free, and you have 12 months to finish.</p>"),
    ("Which languages is the in-person test offered in?",
     "<p>VicRoads lists 13: Arabic, Chinese (Mandarin), Vietnamese, Turkish, Persian, Cambodian, Sinhalese, Somali, "
     "Albanian, Macedonian, Russian, Serbian and Spanish. If your language isn't offered, you can book a free "
     "interpreter, including Auslan.</p>"),
    ("How old do you need to be for a learner permit in Victoria?",
     "<p>16. You can start the online course at 15 years and 11 months, but the permit is only issued from 16.</p>"),
    ("Is the VicRoads practice test the same as the real test?",
     "<p>It has the same size and pass mark as the in-person test, but it is a revision aid. The Road to Solo Driving "
     "handbook says the practice test doesn't cover everything, so study the whole handbook.</p>"),
]


def vic() -> Page:
    crumbs = [("Home", ""), ("States", "states.html"),
              ("VIC learner permit test practice", "vic-learner-permit-test-practice.html")]
    body = page_head(
        "VIC learner permit test practice: how the LPT works",
        "The Victorian learner permit test explained: the online course, the 32-question in-person test, what it covers and how to prepare.",
        crumbs,
        eyebrow=f"{chip('VIC')} Victoria",
    ) + f"""
<div class="content"><div class="container two-col">
<article class="prose">
<div class="answer-box"><p class="answer-label">Quick answer</p>
<p>To get a learner permit in Victoria you pass the learner permit test (LPT), which checks your knowledge of road law
and road safety from the Road to Solo Driving handbook, plus an eyesight check. Most people now take it online as part
of the learner permit course. The in-person test, for people who need another language or an interpreter or who have no
internet, has 32 multiple-choice questions and you need 25 correct (78%).</p></div>

{facts_table("Victorian learner permit test at a glance (checked " + DATE_H + ")", [
    ("Test", "Learner permit test (LPT), car"),
    ("Default route", "Online learner permit course with a final test: about 4–6 hours, English only, first attempt free, 12 months to finish"),
    ("In person", "32 multiple-choice questions, three options each; pass mark 25 of 32 (78%); allow about 45 minutes; appointment fee"),
    ("Who sits it in person", "People who need another language or an interpreter, or who have no computer or internet"),
    ("Minimum age", "16 for the permit; the online course can start at 15 years 11 months"),
    ("Based on", "Road to Solo Driving handbook (April 2023 edition)"),
    ("Permit lasts", "10 years (ends earlier when you move to a probationary licence)"),
])}

<h2>How many questions are in the Victorian learner permit test?</h2>
<p>The in-person test has 32 multiple-choice questions, each with three options, and you need at least 25 right. That
figure comes from VicRoads' practice test page, which says its practice test has the same size and pass mark as the real
one. VicRoads doesn't publish the size or pass mark of the online course's final test, so the app's mock follows the
in-person format.</p>

<h2>Online course or in person: which applies to you?</h2>
<p>The online learner permit course is now the standard route. It takes about 4 to 6 hours, is in English only, and
you have 12 months to finish it; the first attempt at the final test is free.</p>
<p>Sitting the test in person at a VicRoads Customer Service Centre is for people who need another language or an
interpreter, or who have no computer or internet access, and an appointment fee applies. VicRoads offers the in-person
test in 13 languages: Arabic, Chinese (Mandarin), Vietnamese, Turkish, Persian, Cambodian, Sinhalese, Somali, Albanian,
Macedonian, Russian, Serbian and Spanish. If yours isn't listed, a free interpreter can be booked, including Auslan.
Allow about 45 minutes: the eyesight test and permit application happen at the same visit.</p>

<h2>What does the learner permit test cover?</h2>
<p>The test draws on the whole Road to Solo Driving handbook: the licensing section and its four chapters on the
challenges of driving, learning to drive, managing risk, and rules and responsibilities. In the VicRoads practice test,
the topics that come up most are giving way, learning to drive and hazard perception, parking, speed limits and
pedestrians (from our review of the practice test on {DATE_H}). The handbook itself warns that the practice test
doesn't cover everything.</p>
<p>Victoria has some rules you won't find in other states' tests:</p>
<ul>
  <li><strong>Hook turns:</strong> at intersections with a hook turn sign, mainly in central Melbourne, you turn right
  from the far-left lane and wait near the far side until the lights for the road you're entering turn green.</li>
  <li><strong>Trams:</strong> when a tram stops at a stop with no safety zone, stop at the back of the tram without going
  past it, and don't pass while the doors are open. Once the doors close and nobody is on the road, you may pass at no more than 10 km/h.</li>
  <li><strong>Phones for L and P drivers:</strong> a phone may only be used in a commercially made mounting for
  navigation or audio set up before the trip, without touching it. No calls at all, not even hands-free.</li>
</ul>
<p>Other learner rules to know: you must have a zero blood alcohol concentration; L plates go on the front and rear,
visible from 20 metres; learners must not tow; and your supervisor sits in the front passenger seat, holds a full
licence, must be under 0.05 and must not drink at all while supervising.</p>

<h2>What happens after you get your learner permit?</h2>
<p>Your permit lasts 10 years. If you'll be under 21 at your licence test, you need at least 120 hours of supervised
driving, 20 or more after dark, recorded in the myLearners app or the Learner Log Book. From 21 no log book is
required. You must hold the permit for at least 12 months if under 21, 6 months if 21 to under 25, and 3 months if 25
or older. The Hazard Perception Test comes before the drive test and can be taken from 17 years 11 months, and the
probationary licence is available from 18.</p>

<h2>How to practise for the VIC learner permit test with Learners Test Australia</h2>
<ul class="check-list">
  <li>32-question mock tests scored against the 25-question pass line.</li>
  <li>More than 400 original Victorian questions, checked against Road to Solo Driving and current Transport Victoria and VicRoads pages.</li>
  <li>Victoria-only topics such as hook turns, trams and L and P device rules.</li>
  <li>Every answer explained, with the handbook page or road rule it comes from.</li>
</ul>
<p>Read our deeper guide, <a href="@/blog/victorian-learner-permit-test-explained.html">the Victorian learner permit
test explained</a>, and brush up on <a href="@/blog/give-way-rules-for-learner-drivers.html">give way rules</a>, the
biggest topic in the practice test.</p>

{faq_block(VIC_FAQ, heading="VIC learner permit test questions people ask", hid="vic-faq")}

{source_box([
    ("Learner permit test (VicRoads)", SRC["vic_lpt"]),
    ("Prepare for your learner permit (Transport Victoria)", SRC["vic_prepare_l"]),
    ("Driver handbooks and logbooks, including Road to Solo Driving (Transport Victoria)", SRC["vic_handbooks"]),
    ("Learner and probationary driver road rules (Transport Victoria)", SRC["vic_lp_rules"]),
])}
{app_cta('vic')}
</article>
<aside>{related([
    ("The Victorian learner permit test explained", "blog/victorian-learner-permit-test-explained.html"),
    ("Give way rules every learner must know", "blog/give-way-rules-for-learner-drivers.html"),
    ("Hazard perception test in NSW, VIC and QLD", "blog/hazard-perception-test-nsw-vic-qld.html"),
    ("How to use mock tests and mistakes", "blog/how-to-use-mock-tests-and-mistakes.html"),
    ("Learner tests by state", "states.html"),
    ("FAQ", "faq.html"),
])}</aside>
</div></div>"""
    return Page(
        path="vic-learner-permit-test-practice.html",
        title="VIC Learner Permit Test Practice | Learners Test Australia",
        description=("Victorian learner permit test (LPT) practice: 32 questions, pass mark 25 (78%) in person, or the online "
                     "course. What it covers, VIC-only rules and tips."),
        body=body,
        nav="states",
        crumbs=crumbs,
        jsonld=[faq_ld(VIC_FAQ)],
        priority="0.9",
        llms=True,
        llms_title="VIC learner permit test practice",
        llms_note="Victorian learner permit test: online course (default) or 32-question in-person test (pass 25), languages, topics, VIC-only rules.",
    )


# ── QLD ───────────────────────────────────────────────────────────────────────────────────────
QLD_FAQ = [
    ("How many questions are in the Queensland learner test?",
     "<p>Both routes have 30 questions. The written road rules test has 10 giving-way questions (you need 9) and 20 road "
     "rules and licence requirement questions (you need 18). The PrepL final test has 30 questions and you need 27.</p>"),
    ("How many questions can you get wrong?",
     "<p>In the written test, 1 in the giving-way section and 2 in the road rules section; failing either section fails "
     "the test. In the PrepL final test, 3 in total.</p>"),
    ("Is PrepL compulsory in Queensland?",
     "<p>Not yet. The Queensland Government says PrepL will replace the written test, but until it is made mandatory you "
     "can choose either route.</p>"),
    ("How much does PrepL cost?",
     "<p>One fee, the same as the written test fee ($29.70 as at 1 July 2026), gives 12 months' access. If you fail the "
     "final test you can try again after 24 hours at no extra cost.</p>"),
    ("Can I do the written road rules test online?",
     "<p>No. The written test is sat on paper at a licence-issuing centre. The online route is PrepL.</p>"),
]


def qld() -> Page:
    crumbs = [("Home", ""), ("States", "states.html"), ("QLD learner test practice", "qld-learner-test-practice.html")]
    body = page_head(
        "QLD learner test practice: written road rules test and PrepL",
        "Queensland's two routes to a learner licence, the questions and pass marks for each, what they cover and how to prepare.",
        crumbs,
        eyebrow=f"{chip('QLD')} Queensland",
    ) + f"""
<div class="content"><div class="container two-col">
<article class="prose">
<div class="answer-box"><p class="answer-label">Quick answer</p>
<p>In Queensland you can qualify for a car learner licence in one of two ways: the written road rules test, sat on paper
at a licence-issuing centre, or PrepL, an online course with a final test. The written test has 30 multiple-choice
questions in two separately scored sections: giving way (10 questions, need 9) and road rules and licence requirements
(20 questions, need 18). The PrepL final test has 30 questions and you need 27 (90%).</p></div>

{facts_table("Queensland learner tests at a glance (checked " + DATE_H + ")", [
    ("Written road rules test", "30 multiple-choice questions on paper. Giving way: 9 of 10. Road rules and licence requirements: 18 of 20. Failing either section fails the test."),
    ("Where", "TMR customer service centre, participating QGAP office, or licence-issuing police station in rural and remote areas"),
    ("Written test age and attempts", "From 16. A fee for every attempt, one attempt a day; after a fail, wait until the next working day"),
    ("PrepL", "Online course of about 4–6 hours, then a final test of 30 questions; pass 27 of 30 (90%)"),
    ("PrepL age and fee", "Enrol from 15 years 11 months. One fee ($29.70 as at 1 July 2026) for 12 months' access; retry after 24 hours at no extra cost"),
    ("A pass lasts", "5 years (either route)"),
    ("Based on", "Your keys to driving in Queensland (No. 19, November 2022), plus current rules"),
])}

<h2>How many questions are in the QLD written road rules test?</h2>
<p>Thirty, in two sections that are scored separately. The giving-way section has 10 questions and you can afford only
one mistake. The road rules and licence requirements section has 20 questions and you can afford two. A strong score in
one section can't make up for a weak one in the other. No formal time limit is published; the handbook suggests
allowing at least 30 minutes.</p>

<h2>What is PrepL, and how is it different?</h2>
<p>PrepL is Queensland's online learning and assessment course. It takes about 4 to 6 hours on a phone, tablet or
computer and has three sections: Your driving attitude, Signs and rules, and Sharing the road. Assessment pieces are
built in, and the final test has 30 questions with a pass mark of 27. You can enrol from 15 years and 11 months, so your
learner licence can be issued on your 16th birthday. PrepL isn't compulsory yet: until it is, you can choose either
route. Letting someone else do your PrepL can see your enrolment cancelled, a penalty of more than $6,900 for them, and
a 6-month wait before you can enrol again. Our guide compares
<a href="@/blog/qld-written-road-rules-test-vs-prepl.html">the written test and PrepL side by side</a>.</p>

<h2>What does the Queensland learner test cover?</h2>
<p>The written test's second section is officially about road rules and driver licence requirements, so licensing
rules (learner conditions, the logbook, P1 and P2 rules, demerit points and alcohol limits) are core content, not
background. The rest covers signs, speed limits, traffic lights and road markings, alcohol and drugs, phones,
seatbelts and child restraints, parking, and sharing the road. The handbook says learners are tested in detail on giving
way: unsigned crossroads and T-intersections, STOP and GIVE WAY signs, turning, roundabouts, merging, U-turns,
driveways, buses and emergency vehicles.</p>
<p>The current handbook dates from 2022, so it doesn't include Queensland's 2026 e-scooter and e-bike law changes. The
app follows the current rules.</p>
<p>A few Queensland rules to know as a learner:</p>
<ul>
  <li>Your blood alcohol limit is zero, whatever your age.</li>
  <li>Your supervisor must hold an open licence for that class, have held one for at least a year, and sit beside you.</li>
  <li>L plates go on the front and rear of the car, readable from 20 metres.</li>
  <li>No driver may hold a phone or rest it on their body while driving, even when stopped in traffic or when the phone is switched off.</li>
  <li>Four or more demerit points within 12 months suspends a learner licence for 3 months. Driving without a proper supervisor alone carries 4 points.</li>
</ul>

<h2>What happens after you pass?</h2>
<p>Your learner licence lasts 3 years. If you are under 25, you need 100 hours of supervised driving, including at least
10 at night, recorded in a logbook; each hour with an accredited driver trainer counts as 3 logbook hours, for up to 10
hours of lessons. Every car learner, whatever their age, must pass the hazard perception test before the practical test,
and can sit it after holding the learner licence for 6 months. The practical test comes after at least a year on your
learner licence. Under 25s then move to a P1 licence (from 17); if you are 25 or older, you go straight to P2.</p>

<h2>How to practise for the QLD learner test with Learners Test Australia</h2>
<ul class="check-list">
  <li>Mock tests for both routes: the written test with its separate giving-way and road rules pass lines, and the PrepL final test.</li>
  <li>More than 500 original Queensland questions, with giving-way scenarios drawn as diagrams.</li>
  <li>Checked against the Queensland handbook, the Road Rules Regulation in force from 31 August 2026 and current Queensland Government pages.</li>
  <li>Every answer explained, with the handbook page or rule it comes from.</li>
</ul>
<p>Giving way is worth a whole section, so read <a href="@/blog/give-way-rules-for-learner-drivers.html">the give way
rules every learner must know</a> and learn to <a href="@/blog/how-to-use-mock-tests-and-mistakes.html">use your
mistake budget</a>.</p>

{faq_block(QLD_FAQ, heading="QLD learner test questions people ask", hid="qld-faq")}

{source_box([
    ("Driver tests, written and online (qld.gov.au)", SRC["qld_tests"]),
    ("PrepL online learning and assessment (qld.gov.au)", SRC["qld_prepl"]),
    ("Getting a learner licence (qld.gov.au)", SRC["qld_getting_learner"]),
    ("Rules for learner driving (qld.gov.au)", SRC["qld_learner_rules"]),
    ("Learner logbook (qld.gov.au)", SRC["qld_logbook"]),
    ("Your keys to driving in Queensland (Queensland Government publications)", SRC["qld_handbook"]),
])}
{app_cta('qld')}
</article>
<aside>{related([
    ("QLD written road rules test vs PrepL", "blog/qld-written-road-rules-test-vs-prepl.html"),
    ("Give way rules every learner must know", "blog/give-way-rules-for-learner-drivers.html"),
    ("How to use mock tests and mistakes", "blog/how-to-use-mock-tests-and-mistakes.html"),
    ("Hazard perception test in NSW, VIC and QLD", "blog/hazard-perception-test-nsw-vic-qld.html"),
    ("Learner tests by state", "states.html"),
    ("FAQ", "faq.html"),
])}</aside>
</div></div>"""
    return Page(
        path="qld-learner-test-practice.html",
        title="QLD Learner Test & PrepL Practice | Learners Test Australia",
        description=("QLD learner test practice: the written road rules test (30 questions, two sections) and the PrepL final "
                     "test (30, pass 27). Formats, topics and tips."),
        body=body,
        nav="states",
        crumbs=crumbs,
        jsonld=[faq_ld(QLD_FAQ)],
        priority="0.9",
        llms=True,
        llms_title="QLD learner test practice",
        llms_note="Queensland written road rules test (10 giving way, pass 9; 20 road rules, pass 18) and PrepL final test (30, pass 27), fees, topics, next steps.",
    )


# ── SA (content-src/coverage/sa.md) ───────────────────────────────────────────────────────────
SA_FAQ = [
    ("How many questions are in the SA learners test?",
     "<p>It depends on the route. The in-person learner's theory test at Service SA has 50: 8 give-way diagram questions "
     "in Part A, which must all be right, and 42 road rules and safety questions in Part B, where you need 32. The myLs "
     "test has 30 questions and you need 27.</p>"),
    ("How many questions can you get wrong?",
     "<p>In the in-person test, none in Part A and up to 10 in Part B. In the myLs test, up to 3.</p>"),
    ("Is myLs compulsory in South Australia?",
     "<p>No. myLs is the recommended route, but the in-person test is still available, and failing the in-person test "
     "doesn't stop you enrolling in myLs.</p>"),
    ("Are the questions in Learners Test Australia the real SA test questions?",
     "<p>No. They are original practice questions written for the app and checked against The Driver's Handbook "
     "(February 2026) and South Australian legislation. The app is independent and not connected to the Government of "
     "South Australia.</p>"),
]


def sa() -> Page:
    crumbs = [("Home", ""), ("States", "states.html"), ("SA learners test practice", "sa-learners-test-practice.html")]
    body = page_head(
        "SA learners test practice: the learner's theory test and myLs",
        "South Australia's two routes to a learner's permit, the questions and pass marks for each, the rules you are "
        "tested on and how to prepare.",
        crumbs,
        eyebrow=f"{chip('SA')} South Australia",
    ) + f"""
<div class="content"><div class="container two-col">
<article class="prose">
<div class="answer-box"><p class="answer-label">Quick answer</p>
<p>To get a learner's permit in South Australia you pass the learner's theory test, in one of two ways. myLs is an
online course that finishes with a 30-question test where you need 27 correct, and some questions have more than one
right answer. The in-person test at a Service SA centre has two parts: 8 give-way diagram questions that must all be
answered correctly, then 42 multiple-choice questions on road rules and safety, where you need 32.</p></div>

{facts_table("SA learner's theory test at a glance (checked " + DATE_H + ")", [
    ("Test", "Learner's theory test, car: online through myLs, or in person at Service SA"),
    ("In person", "Part A: 8 give-way diagram questions, all must be correct. Part B: 42 multiple-choice questions, pass 32 of 42. On paper or a computer."),
    ("myLs", "Online course of about 4 hours, then a 30-question test in one sitting; pass 27 of 30. Some questions have more than one correct answer."),
    ("Minimum age", "myLs from 15 years 9 months; the in-person test and the permit from 16"),
    ("Based on", "The Driver's Handbook (MR200), February 2026 edition"),
    ("Permit lasts", "2 years"),
])}

<h2>How many questions are in the SA learner's theory test, and what is the pass mark?</h2>
<p>The in-person test has two parts, taken in order. Part A shows 8 diagrams and asks who must give way in each. One
give-way mistake means you can't go on to Part B, so the attempt is a fail. Part B has 42 multiple-choice questions on
road rules and road safety, and you need 32, so you can afford up to 10 mistakes there.</p>
<p>The myLs test is a single block of 30 questions with a pass mark of 27, done in one sitting without help. Some
questions have more than one correct answer: a hint tells you when, and you only score if you select every correct
option.</p>

<h2>myLs or the in-person test: which route suits you?</h2>
<p>myLs is the route South Australia recommends, but it isn't compulsory. You first set up your identity, photo and a
mySAGOV account at a Service SA centre. The course starts with Your driving attitude, then Signs and rules and Sharing
the road in either order, and finishing all three unlocks the test. One fee covers 12 months' access with unlimited test
attempts.</p>
<p>The in-person test is for people aged 16 or older. You book it, pay the fee each time you sit, and take it at one of
the Service SA centres that run theory tests, so check which ones before you book. No list of test languages is
published, so ask Service SA if you need help with English. Failing in person doesn't stop you switching to myLs.</p>

<h2>How old do you need to be?</h2>
<ul>
  <li><strong>myLs:</strong> enrol from 15 years and 9 months.</li>
  <li><strong>In-person test, and the learner's permit itself:</strong> from 16.</li>
  <li><strong>P1 provisional licence:</strong> from 17.</li>
</ul>

<h2>What does the SA learner's theory test cover?</h2>
<p>The Driver's Handbook says the test is based directly on its road rules and road safety sections, including the
licensing chapters: learner and P conditions, supervising drivers, the log book and demerit points are core material.
Giving way matters most, since it has a whole part of the in-person test. South Australian rules that catch learners
out:</p>
<ul>
  <li><strong>25 km/h school zones:</strong> the limit applies whenever a child is in the zone. Near selected schools
  there are also 40 km/h limits on school days, from 8 to 9:30 am and 2 to 4 pm.</li>
  <li><strong>More 25 km/h rules:</strong> pass a stopped school bus, a stopped emergency vehicle with flashing red or
  blue lights (unless it is across a median strip) or a stopped breakdown vehicle with flashing amber lights on your
  side of the road at no more than 25 km/h.</li>
  <li><strong>100 km/h cap:</strong> learners and P drivers must not exceed 100 km/h, even on roads signed 110.</li>
  <li><strong>Phones:</strong> learners and P1 drivers may not use a phone at all while driving, not even hands-free,
  except to pay or show a code while stationary in a place such as a drive-through.</li>
</ul>

<h2>What happens after you pass?</h2>
<p>Your permit lasts 2 years. A qualified supervising driver must sit next to you: someone who has held a full licence
for that class of vehicle for the past 2 years, hasn't been disqualified in that time, isn't on a good behaviour
condition and is under 0.05. Your own limit is zero, L plates go on the front and rear, and 4 demerit points, speeding
by 10 km/h or more, or any other permit breach brings a 6-month disqualification.</p>
<p>Before P1 you need 75 hours of supervised driving, 15 of them at night, whatever your age, and at least 12 months on
your permit (6 months if you are 25 or older). You also pass the Hazard Perception Test and either a Vehicle On Road
Test or competency-based training and assessment. P1 drivers show red P plates; P2 drivers show none. Under 25, P1
also brings a midnight-to-5 am ban and a limit of one passenger aged 16 to 20 (family excluded), unless a qualified
supervising driver sits beside you or an exemption applies.</p>

<h2>How to practise for the SA learners test with Learners Test Australia</h2>
<ul class="check-list">
  <li>Mock tests for both routes: the in-person format, where Part B only starts once all 8 give-way answers are right,
  and the 30-question myLs test.</li>
  <li>More than 550 original South Australian questions, checked against The Driver's Handbook and SA legislation.</li>
  <li>Dozens of select-all-that-apply questions in the myLs style.</li>
  <li>Every answer explained, with its handbook page or rule, in English and four other languages.</li>
</ul>
<p>Giving way decides Part A, so read <a href="@/blog/give-way-rules-for-learner-drivers.html">the give way rules every
learner must know</a> and learn how to <a href="@/blog/how-to-use-mock-tests-and-mistakes.html">use mock tests and your
mistakes</a>.</p>

{faq_block(SA_FAQ, heading="SA learners test questions people ask", hid="sa-faq")}

{source_box([
    ("Complete the myLs course online (sa.gov.au)", SRC["sa_myls"]),
    ("Complete your learner's test at Service SA (sa.gov.au)", SRC["sa_theory_test"]),
    ("Licence conditions (sa.gov.au)", SRC["sa_conditions"]),
    ("The Driver's Handbook (mylicence.sa.gov.au)", SRC["sa_handbook"]),
    ("Learner's stage (mylicence.sa.gov.au)", SRC["sa_learners_stage"]),
])}
{app_cta('sa', "It is not connected to the Government of South Australia, the Department for Infrastructure and Transport or Service SA.")}
</article>
<aside>{related(RELATED_NEW)}</aside>
</div></div>"""
    return Page(
        path="sa-learners-test-practice.html",
        title="SA Learners Test & myLs Practice | Learners Test Australia",
        description=("SA learners test practice: the in-person theory test (8 give-way questions, then 42, pass 32) or "
                     "the myLs online test (30, pass 27). Rules, ages and tips."),
        body=body,
        nav="states",
        crumbs=crumbs,
        jsonld=[faq_ld(SA_FAQ)],
        priority="0.9",
        llms=True,
        llms_title="SA learners test practice",
        llms_note="South Australian learner's theory test: in person (8 give-way questions, all correct, then 42, pass 32) or myLs online (30, pass 27), ages, SA rules, next steps.",
    )


# ── WA (content-src/coverage/wa.md; legislation only, see the module docstring) ───────────────
WA_FAQ = [
    ("How many questions are in the WA learners test?",
     "<p>We don't state the official question count or pass mark here: check the WA Department of Transport and Major "
     "Infrastructure's website. The app's WA practice test uses a 30-question format.</p>"),
    ("Who can supervise a learner driver in WA?",
     "<p>A licensed driving instructor, or someone who has held a licence for that kind of vehicle for at least 4 years. "
     "Your supervisor must be under 0.05 (zero in a few special cases).</p>"),
    ("How many supervised hours do WA learners need?",
     "<p>If you are under 25, at least 50 hours, including at least 5 at night, recorded in an approved log book before "
     "the practical driving assessment. Learners aged 25 or older have no minimum hours, but still need the hazard "
     "perception test.</p>"),
    ("Are the questions in Learners Test Australia the official WA test questions?",
     "<p>No. They are original practice questions written for the app from Western Australian legislation. The app is "
     "independent and not connected to the Government of Western Australia.</p>"),
]


def wa() -> Page:
    crumbs = [("Home", ""), ("States", "states.html"), ("WA learners test practice", "wa-learners-test-practice.html")]
    dtmi = ext(SRC["wa_dtmi"], "Department of Transport and Major Infrastructure website")
    body = page_head(
        "WA learners test practice: your learner's permit theory test",
        "What Western Australian law says you need for a learner's permit, the rules the test checks, what comes next "
        "and how to practise.",
        crumbs,
        eyebrow=f"{chip('WA')} Western Australia",
    ) + f"""
<div class="content"><div class="container two-col">
<article class="prose">
<div class="answer-box"><p class="answer-label">Quick answer</p>
<p>In Western Australia you must show you know the state's traffic laws and safe driving techniques before a learner's
permit is issued, normally by passing a theory test. You can hold a car learner's permit from 16, and it lasts 3 years.
We don't state the test's official question count or pass mark, because we couldn't confirm them from a source we're
able to use: check with the WA Department of Transport and Major Infrastructure. The app's WA practice test uses a
30-question format.</p></div>

{facts_table("WA learner's permit at a glance (checked " + DATE_H + ")", [
    ("Before the permit", "Show reasonable knowledge of WA traffic laws and safe driving techniques, normally by passing a theory test"),
    ("Test format", "Not stated here: check the Department of Transport and Major Infrastructure's website"),
    ("Minimum age", "16 for a car learner's permit (15 years 6 months for a moped-only permit)"),
    ("Permit lasts", "3 years"),
    ("Supervisor", "A licensed driving instructor, or someone who has held a licence for that kind of vehicle for at least 4 years"),
    ("On your permit", "No faster than 100 km/h, L plates front and rear, zero alcohol"),
    ("Based on", "WA legislation, including the Road Traffic Code 2000"),
])}

<h2>How many questions are in the WA learners test, and what is the pass mark?</h2>
<p>This page doesn't give the official number of questions or pass mark: for WA's test format, check the department's
own website before you book.</p>
<p>The law sets out what the test is for: before a permit is issued, you must show reasonable knowledge of WA's traffic
laws and of safe driving techniques, so expect questions on both. The app's WA practice test uses a 30-question format
drawn from every topic; treat it as practice for the rules, not a copy of the official test.</p>

<h2>WA has its own road rules: what is different?</h2>
<p>Western Australia doesn't adopt the national Australian Road Rules word for word. Its road rules are the Road Traffic
Code 2000, which follows the national rules closely but has its own numbering and some local differences:</p>
<ul>
  <li><strong>110 km/h default:</strong> outside built-up areas, the limit where no sign applies is 110 km/h (50 km/h in
  built-up areas).</li>
  <li><strong>Keep left at 90 km/h:</strong> on multi-lane roads with a limit of 90 km/h or more, stay out of the right
  lane except to overtake, turn right or U-turn, or for a few other set reasons.</li>
  <li><strong>40 km/h past incidents:</strong> pass a stationary emergency, breakdown, tow or Main Roads incident
  response vehicle with flashing lights at no more than 40 km/h.</li>
  <li><strong>No hook turns for cars:</strong> only bicycle and e-rideable riders may hook turn.</li>
</ul>

<h2>Who can supervise a WA learner, and what are the learner rules?</h2>
<p>A learner's permit only lets you drive to learn, with a licensed driving instructor or someone who has held a licence
for that kind of vehicle for at least 4 years. The law treats the person beside you as your supervisor. They must be
under 0.05 (zero in a few special cases) and free of illicit drugs, and police can test them.</p>
<ul>
  <li>Never drive faster than 100 km/h, even where the limit is 110 km/h.</li>
  <li>Show L plates at the front and rear: a black L on yellow, at least 150 mm square. You and your supervisor are both
  responsible for them.</li>
  <li>Your alcohol limit is zero until you have held a licence for 2 years.</li>
  <li>On 30 September 2026, WA had no learner-only rules on passengers, night driving or phones.</li>
</ul>

<h2>What happens after you get your learner's permit?</h2>
<p>Under 25, log at least 50 hours of supervised driving, including 5 at night (sunset to sunrise), in an approved log
book signed by your supervisor; from 25 there is no minimum. The hazard perception test comes next: under 25, once you
are 16 years and 6 months old and have held your permit for 6 months; from 25, after 6 months on your permit. Under-25s
can take the practical driving assessment from 17, after the hours and the hazard test; from 25, 6 months after the
permit was granted.</p>
<p>Red P plates (a white P on red) come first, for 6 months: no driving between midnight and 5 am except in limited
cases such as work or study travel, and only one passenger unless one of them has held a full licence for at least 4
years, the others are immediate family, or you carry them for work. Green P plates (a white P on green) follow until you
have held a licence for 2 years and are at least 19. Novice drivers are disqualified for 3 months at 4 demerit points in
their first year, or 8 in their second.</p>
<p class="note">These are the rules in force on 30 September 2026, so check for changes before you book.</p>

<h2>How to practise for the WA learners test with Learners Test Australia</h2>
<ul class="check-list">
  <li>A 30-question practice test that mixes every topic and is scored at the end.</li>
  <li>More than 500 original WA questions, written from the Road Traffic Code 2000 and WA's licensing laws.</li>
  <li>WA-only rules such as red and green P plates, the 4-year supervisor rule and the 90 km/h keep-left rule.</li>
  <li>Every answer explained, with the regulation it comes from, in English and four other languages.</li>
</ul>
<p>Brush up on <a href="@/blog/give-way-rules-for-learner-drivers.html">give way rules</a>, which WA's code mostly shares
with the national rules, and read <a href="@/blog/how-to-use-mock-tests-and-mistakes.html">how to use mock tests and
mistakes</a>.</p>

{faq_block(WA_FAQ, heading="WA learners test questions people ask", hid="wa-faq")}

{source_box([
    ("Road Traffic Code 2000 (legislation.wa.gov.au)", SRC["wa_rtc"]),
    ("Road Traffic (Authorisation to Drive) Regulations 2014 (legislation.wa.gov.au)", SRC["wa_atdr"]),
    ("Road Traffic (Authorisation to Drive) Act 2008 (legislation.wa.gov.au)", SRC["wa_atda"]),
], note=f"Facts on this page come from Western Australian legislation. For bookings, fees and the current test format, use the {dtmi}.")}
{app_cta('wa', "It is not connected to the Government of Western Australia or the Department of Transport and Major Infrastructure.")}
</article>
<aside>{related(RELATED_NEW)}</aside>
</div></div>"""
    return Page(
        path="wa-learners-test-practice.html",
        title="WA Learners Test Practice | Learners Test Australia",
        description=("WA learners test practice: what you need for a learner's permit, supervisor and log book rules, red "
                     "and green P plates, WA-only road rules and how to prepare."),
        body=body,
        nav="states",
        crumbs=crumbs,
        jsonld=[faq_ld(WA_FAQ)],
        priority="0.9",
        llms=True,
        llms_title="WA learners test practice",
        llms_note="Western Australian learner's permit: the knowledge requirement (official test format not stated here; the app's practice test uses 30 questions), age 16, supervisor, hours, HPT, red and green P plates, WA road rules.",
    )


# ── TAS (content-src/coverage/tas.md) ─────────────────────────────────────────────────────────
TAS_FAQ = [
    ("How many questions are in the Tasmanian learners test?",
     "<p>The online driver knowledge test, taken after the Plates Plus course, has 30 questions and you need 27 correct. "
     "The format of the standalone test at Service Tasmania shops is not published.</p>"),
    ("Are there compulsory questions in the Tasmanian online test?",
     "<p>No. No single question has to be answered correctly to pass. Some questions do have more than one correct "
     "answer, and you only score if you choose every correct option.</p>"),
    ("Does the Plates Plus course cost anything?",
     "<p>No. The course and the driver knowledge test are free, online or at a Service Tasmania shop. You pay the "
     "learner licence fee after you pass.</p>"),
    ("Is Learners Test Australia the official Plates Plus app?",
     "<p>No. It is an independent practice app with original questions written from Tasmanian legislation. It is not "
     "connected to the Tasmanian Government, Plates Plus or Service Tasmania.</p>"),
]


def tas() -> Page:
    crumbs = [("Home", ""), ("States", "states.html"), ("Tasmania learners test practice", "tas-learners-test-practice.html")]
    body = page_head(
        "Tasmania learners test practice: Plates Plus and the driver knowledge test",
        "Tasmania's two ways to a learner licence, the online test's questions and pass mark, what it covers and how to "
        "prepare.",
        crumbs,
        eyebrow=f"{chip('TAS')} Tasmania",
    ) + f"""
<div class="content"><div class="container two-col">
<article class="prose">
<div class="answer-box"><p class="answer-label">Quick answer</p>
<p>In Tasmania you get a car learner licence by passing the driver knowledge test (DKT). Most learners take the free
Plates Plus online course first and then a 30-question online test, where you need 27 correct. Some questions have more
than one correct answer, and there are no compulsory questions. You can also sit a standalone test at a Service
Tasmania shop without doing the course, but its format isn't published.</p></div>

{facts_table("Tasmanian driver knowledge test at a glance (checked " + DATE_H + ")", [
    ("Test", "Driver knowledge test (DKT), car"),
    ("Online route", "Free Plates Plus course of about 4 to 6 hours, then a 30-question online test; pass 27 of 30"),
    ("Question style", "Multiple choice; some questions have more than one correct answer, and each question says whether it does. No compulsory questions."),
    ("Time", "About 30 to 40 minutes, in one sitting"),
    ("Retries online", "One attempt every 12 hours, within 12 months of first enrolling"),
    ("Standalone test", "At any Service Tasmania shop, no course needed, free; format not published"),
    ("Minimum age", "15 years 11 months for the course and test; 16 for the learner licence"),
    ("After passing", "Apply at a Service Tasmania shop within 12 months: identity documents, eyesight test, medical declaration and the licence fee"),
])}

<h2>How many questions are in the Tasmanian driver knowledge test?</h2>
<p>The online test has 30 multiple-choice questions and the pass mark is 27, so you can get no more than 3 wrong. There
are no compulsory questions, but some questions have more than one correct answer. Each question tells you whether it
does, and you must select every correct option to get the mark. The test takes about 30 to 40 minutes in one sitting,
and leaving part-way through loses your progress.</p>
<p>The standalone test at a Service Tasmania shop is a separate version of the test, but its number of questions and
pass mark are not published. Tasmania's official information says people who skip the course are much less likely to
pass. After a fail at a shop you can resit the next business day, or switch to the online course.</p>

<h2>What is Plates Plus, and how does it work?</h2>
<p>Plates Plus is Tasmania's official online course for new drivers and the recommended way to your learner licence.
You enrol from 15 years and 11 months with a client ID, set up online through myServiceTas or at a Service Tasmania
shop. The course takes about 4 to 6 hours in three sections; you can't skip content, and finishing all three unlocks the
test. The course and test are free, you have 12 months from first enrolling to pass, and after a failed attempt you
wait 12 hours. Once you pass, apply for your learner licence at a Service Tasmania shop within 12 months.</p>

<h2>How old do you need to be?</h2>
<ul>
  <li><strong>Plates Plus course and driver knowledge test:</strong> from 15 years and 11 months.</li>
  <li><strong>Learner licence:</strong> from 16.</li>
  <li><strong>P1 provisional licence:</strong> from 17.</li>
</ul>

<h2>What does the Tasmanian DKT cover?</h2>
<p>The course and test cover the road rules and the reasons for them, safe driving attitudes and behaviour (with a focus
on speeding, seatbelts, fatigue, distraction, and drink and drug driving) and licensing rules. Tasmanian rules that
often catch learners out:</p>
<ul>
  <li><strong>Speed caps:</strong> learners must not exceed 90 km/h and P1 drivers 100 km/h, whatever the sign says.</li>
  <li><strong>Gravel roads:</strong> outside built-up areas, the default limit on unsealed roads is 80 km/h.</li>
  <li><strong>40 km/h zones:</strong> no faster than 40 km/h past a stopped or slow police, emergency or roadside
  assistance vehicle with flashing lights (unless it is across a median strip), or within 50 m of a school bus showing
  its warning sign and light.</li>
  <li><strong>Turning at traffic lights:</strong> no faster than 20 km/h.</li>
  <li><strong>Double broken centre lines:</strong> in Tasmania you must not cross them to overtake.</li>
  <li><strong>Phones:</strong> learners and P1 drivers may not use a phone at all while driving, not even hands-free.</li>
</ul>

<h2>What happens after you get your learner licence?</h2>
<p>Your learner licence lasts 5 years. You may drive only with a supervising driver next to you: someone who has held a
full licence for the past 12 months without a break. Show L plates at the front and rear, keep your alcohol at zero and
don't tow anything. Four or more demerit points within 12 months brings a 3-month suspension.</p>
<p>You must hold your learner licence for at least 12 months in a row before P1, whatever your age, and log at least 80
hours of driving, 15 of them at night. The Hazard Perception Test can be sat from 3 months before the earliest test date
printed on your licence: it has 25 video clips, you need 13 right, it's free and you can retry straight away. Pass it
before you book the P1 driving assessment.</p>
<p>On P1 you show red P plates for at least 12 months and may carry no more than one passenger aged 16 to 21, unless an
exemption applies (for example for family). Some P1 offences, such as speeding by 10 km/h or more, restart your P1
year. P2 brings green P plates, for 2 years if you are under 23, so the earliest age for a full licence is 20.</p>

<h2>How to practise for the Tasmanian learners test with Learners Test Australia</h2>
<ul class="check-list">
  <li>30-question mock tests scored against the 27-question pass line.</li>
  <li>Select-all-that-apply questions, like the ones in the online test.</li>
  <li>More than 450 original Tasmanian questions, written from the Road Rules 2019 and Tasmania's licensing laws.</li>
  <li>Every answer explained, with the rule or regulation it comes from.</li>
</ul>
<p>For the shared national rules, read <a href="@/blog/give-way-rules-for-learner-drivers.html">the give way rules every
learner must know</a>, and plan your practice with <a href="@/blog/how-to-use-mock-tests-and-mistakes.html">our mock
test guide</a>.</p>

{faq_block(TAS_FAQ, heading="Tasmania learners test questions people ask", hid="tas-faq")}

{source_box([
    ("Getting your learner licence (Plates Plus)", SRC["tas_pp_learner"]),
    ("Course frequently asked questions (Plates Plus)", SRC["tas_pp_faq"]),
    ("Complete a learner driver licence knowledge test (Service Tasmania)", SRC["tas_st_test"]),
    ("Hazard perception test questions (Plates Plus)", SRC["tas_pp_hpt"]),
    ("Driver Licensing and Vehicle Registration Regulations 2021 (legislation.tas.gov.au)", SRC["tas_dlvr"]),
])}
{app_cta('tas', "It is not connected to the Tasmanian Government, Plates Plus, Service Tasmania or Transport Tasmania.")}
</article>
<aside>{related(RELATED_NEW)}</aside>
</div></div>"""
    return Page(
        path="tas-learners-test-practice.html",
        title="Tasmania Learners Test Practice | Learners Test Australia",
        description=("Tasmania learners test practice: the free Plates Plus course and 30-question online driver knowledge "
                     "test (pass 27), the standalone test, ages and TAS rules."),
        body=body,
        nav="states",
        crumbs=crumbs,
        jsonld=[faq_ld(TAS_FAQ)],
        priority="0.9",
        llms=True,
        llms_title="Tasmania learners test practice",
        llms_note="Tasmanian driver knowledge test: free Plates Plus course and 30-question online test (pass 27, some multi-answer, no compulsory questions), standalone test, ages, TAS rules.",
    )


# ── ACT (content-src/coverage/act.md; naming rules in the module docstring) ───────────────────
ACT_FAQ = [
    ("How many questions are in the ACT learners test?",
     "<p>The ACT learner licence knowledge test has 35 multiple-choice questions, drawn at random from a bank of more "
     "than 300. You need at least 31 correct. Not every detail of the pass rule is published, so aim to get every "
     "question right.</p>"),
    ("Where do you sit the ACT learners test?",
     "<p>At the end of an approved course, run by an approved provider or, for its own students, a participating "
     "school. Access Canberra doesn't run the test.</p>"),
    ("How many supervised hours do ACT learners need?",
     "<p>If you were under 25 when your learner licence was issued or last renewed, 100 hours including 10 at night. "
     "From 25, it is 50 hours including 5 at night. After 3 months on your licence, some approved courses count for part "
     "of the hours.</p>"),
    ("Is Learners Test Australia an approved ACT course?",
     "<p>No. It is an independent practice app with original questions written from ACT legislation. It is not the ACT "
     "course, doesn't replace it and is not connected to the ACT Government, Access Canberra or any approved course "
     "provider.</p>"),
]


def act() -> Page:
    crumbs = [("Home", ""), ("States", "states.html"), ("ACT learners test practice", "act-learners-test-practice.html")]
    body = page_head(
        "ACT learners test practice: the ACT learner licence knowledge test",
        "How the ACT's learner licence knowledge test works, who runs it, what it covers and how to prepare for it.",
        crumbs,
        eyebrow=f"{chip('ACT')} Australian Capital Territory",
    ) + f"""
<div class="content"><div class="container two-col">
<article class="prose">
<div class="answer-box"><p class="answer-label">Quick answer</p>
<p>In the ACT there is one way to a car learner licence: an approved course, run by an approved provider or, for its own
students, a participating school, which ends with a supervised knowledge test. The test has 35 multiple-choice
questions drawn at random from a bank of more than 300, and you need at least 31 correct. You can apply for your learner
licence from 15 years and 9 months, and a pass can be used for 2 years.</p></div>

{facts_table("ACT learner licence knowledge test at a glance (checked " + DATE_H + ")", [
    ("Test", "ACT learner licence knowledge test, car"),
    ("How you take it", "Only at the end of an approved course with an approved provider or participating school, supervised by the provider"),
    ("Before the test", "Finish the course modules and pass a course quiz with at least 50%"),
    ("Questions", "35 multiple choice, drawn at random from a bank of more than 300"),
    ("Pass mark", "At least 31 of 35 (not every detail of the pass rule is published)"),
    ("Cost", "Set by the provider, and must cover two attempts at each test; some providers and schools charge nothing"),
    ("Minimum age", "15 years 9 months for the learner licence"),
    ("A pass lasts", "2 years, for applying for your learner licence"),
])}

<h2>How many questions are in the ACT learners test, and what is the pass mark?</h2>
<p>The test is computerised: 35 multiple-choice questions drawn at random from a bank of more than 300. You need at
least 31 correct, so you can't pass with more than 4 wrong. That is the minimum rather than the whole rule: the ACT
doesn't publish every detail of how the test is marked, so treat every topic as one you need to know. The course fee
covers two attempts at each test, and the provider can charge for more.</p>

<h2>How does the ACT course work?</h2>
<p>There is no test at Access Canberra offices. You enrol in an approved course with an approved provider, or with
your school if it runs the course for its students (some offer it free in Year 10). You finish the course modules and a
course quiz, where you need at least 50%, then sit the knowledge test, supervised by the provider. An accredited
interpreter can interpret but can't help you answer. No list of test languages is published.</p>
<p>When you pass, you get a completion certificate. Within 2 years, take it with your identity and residency documents
to an Access Canberra Service Centre, pass an eye test and pay the fee. You'll receive a logbook and L plates.</p>

<h2>How old do you need to be?</h2>
<ul>
  <li><strong>Car learner licence:</strong> from 15 years and 9 months. Ask your provider or school when you can start
  the course.</li>
  <li><strong>Driving assessment and provisional licence:</strong> from 17.</li>
</ul>

<h2>What does the ACT knowledge test cover?</h2>
<p>The knowledge test is about road rules, including the ACT's licensing rules. Rules that set the ACT apart:</p>
<ul>
  <li><strong>No learner speed or passenger limits:</strong> ACT learners follow the normal speed limits, may carry
  passengers and have no high-powered car ban, as long as the supervisor sits next to them.</li>
  <li><strong>L plates:</strong> at the front and rear, or on the roof.</li>
  <li><strong>Supervisors at zero:</strong> your supervisor needs a full Australian car licence (no minimum number of
  years), must have no alcohol at all and must not drink while supervising.</li>
  <li><strong>Phones:</strong> learners and all P drivers, P2 included, may not make calls at all, not even hands-free or
  by voice command.</li>
  <li><strong>40 km/h past emergency vehicles:</strong> pass a stopped or slow police or emergency vehicle with flashing
  red or blue lights at no more than 40 km/h, unless it is across a median strip.</li>
  <li><strong>Light rail:</strong> Canberra's light rail vehicles count as trams under the road rules.</li>
</ul>

<h2>What happens after you get your learner licence?</h2>
<p>Your learner licence lasts 5 years. Hold it for at least 12 months, or 6 months if you were 25 or older when it was
issued or last renewed. Under-25s need 100 hours of driving, including 10 at night, in the logbook; from 25 it is 50,
including 5 at night. After 3 months, approved courses count towards the total: the Safer Driver Course for 20 hours
(under-25s), the Vulnerable Road User Program for 10 and Learner Driver First Aid for 5.</p>
<p>After more than 3 months on your learner licence you can sit the online Hazard Perception Test. Then, from 17, you
take a one-off driving assessment or competency-based training and assessment with an accredited instructor.</p>
<p>The provisional licence lasts 3 years: under 25 at issue, 12 months on P1 (red P plates), then P2 (green P plates);
from 25, P2 throughout. Between 11 pm and 5 am a P1 driver may carry no more than one passenger aged 16 to 22 who isn't
family, unless travelling for work or study. Four demerit points within 3 years, on L or P plates, brings a 3-month
suspension.</p>

<h2>How to practise for the ACT learners test with Learners Test Australia</h2>
<ul class="check-list">
  <li>35-question practice tests scored against a 31-question pass line.</li>
  <li>More than 440 original ACT questions, written from ACT legislation.</li>
  <li>ACT-only rules such as roof-mounted plates, zero alcohol for supervisors and the late-night P1 passenger rule.</li>
  <li>Every answer explained, with the section it comes from.</li>
</ul>
<p>The app is for practice only: the real test can only be taken through an approved course provider or a participating
school. For the shared national rules, read <a href="@/blog/give-way-rules-for-learner-drivers.html">the give way rules
every learner must know</a>.</p>

{faq_block(ACT_FAQ, heading="ACT learners test questions people ask", hid="act-faq")}

{source_box([
    ("Get your learner driver licence (Access Canberra)", SRC["act_learner"]),
    ("Get your provisional driver licence (Access Canberra)", SRC["act_prov"]),
    ("Road Transport (Driver Licensing) Regulation 2000 (ACT Legislation Register)", SRC["act_dlr"]),
    ("Road Transport (Road Rules) Regulation 2017 (ACT Legislation Register)", SRC["act_rrr"]),
])}
{app_cta('act', "It is not connected to the ACT Government, Access Canberra, the Road Transport Authority or any approved course provider, and it is not the ACT course or a replacement for it.")}
</article>
<aside>{related(RELATED_NEW)}</aside>
</div></div>"""
    return Page(
        path="act-learners-test-practice.html",
        title="ACT Learners Test Practice | Learners Test Australia",
        description=("ACT learners test practice: the 35-question learner licence knowledge test (at least 31 correct), how "
                     "the approved course works, ages, hours and ACT rules."),
        body=body,
        nav="states",
        crumbs=crumbs,
        jsonld=[faq_ld(ACT_FAQ)],
        priority="0.9",
        llms=True,
        llms_title="ACT learners test practice",
        llms_note="ACT learner licence knowledge test: taken only at the end of an approved course (provider or school), 35 questions from a bank of 300+, at least 31 correct, age 15 years 9 months, ACT rules.",
    )


# ── NT (content-src/coverage/nt.md; facts only from nt.gov.au) ────────────────────────────────
NT_FAQ = [
    ("How many questions are in the NT learners test?",
     "<p>The NT driver knowledge test has 30 multiple-choice questions, drawn at random from a pool of more than 300. "
     "You need at least 26 correct, so you can get up to 4 wrong.</p>"),
    ("Is there a hazard perception test in the NT?",
     "<p>No. The NT has no separate hazard perception test. How you respond to hazards is assessed during the practical "
     "driving test instead.</p>"),
    ("How long do you need to hold an NT learner licence?",
     "<p>At least 6 months in a row before you can be granted a provisional licence. If your learner licence lapses or "
     "is suspended, the 6 months start again.</p>"),
    ("What is the speed limit for learner and P drivers in the NT?",
     "<p>80 km/h for learners and 100 km/h for provisional drivers, even on roads signed 110 or 130 km/h.</p>"),
    ("Are the questions in Learners Test Australia the real NT test questions?",
     "<p>No. They are original practice questions written for the app from Northern Territory legislation. The app is "
     "independent and not connected to the Northern Territory Government or the Motor Vehicle Registry.</p>"),
]


def nt() -> Page:
    crumbs = [("Home", ""), ("States", "states.html"), ("NT learners test practice", "nt-learners-test-practice.html")]
    body = page_head(
        "NT learners test practice: the driver knowledge test",
        "The Northern Territory's driver knowledge test for a learner licence: questions, pass mark, where to sit it, "
        "the rules it checks and how to prepare.",
        crumbs,
        eyebrow=f"{chip('NT')} Northern Territory",
    ) + f"""
<div class="content"><div class="container two-col">
<article class="prose">
<div class="answer-box"><p class="answer-label">Quick answer</p>
<p>To get a car learner licence in the Northern Territory you pass the driver knowledge test, often called the theory
test, at a Motor Vehicle Registry (MVR) office. It has 30 multiple-choice questions on NT road rules, drawn at random
from a pool of more than 300, and you need at least 26 correct. You must be at least 16, and a pass stays valid for 12
months.</p></div>

{facts_table("NT driver knowledge test at a glance (checked " + DATE_H + ")", [
    ("Test", "Driver knowledge test (theory test) for a car (class C) learner licence"),
    ("Questions", "30 multiple choice, drawn at random from a pool of more than 300"),
    ("Pass mark", "At least 26 of 30"),
    ("Where", "An MVR office during its theory test hours; in remote areas, a local police station or the DriveSafe NT remote program"),
    ("Minimum age", "16"),
    ("A pass lasts", "12 months"),
    ("Not published", "Sections, time limit, paper or computer, and retry rules"),
    ("Learner licence lasts", "2 years"),
    ("Hazard perception test", "None in the NT: your response to hazards is assessed in the practical test"),
])}

<h2>How many questions are in the NT driver knowledge test?</h2>
<p>Thirty, all multiple choice and all about NT road rules, picked at random from a pool of more than 300. You need 26
correct, so 4 wrong answers is the most you can afford. There is one overall pass mark: the NT doesn't mention separate
sections, and it doesn't publish whether any question must be answered correctly, whether there is a time limit, or
whether the test is on paper or a computer. Retry rules aren't published either, so ask MVR if you need to resit.</p>

<h2>Where do you sit the NT learners test?</h2>
<p>At an MVR office, during its theory test hours, which end before the office closes. Bring evidence of your identity
and NT residency, plus a completed learner licence application. In remote areas you can sit the test at your local
police station or through the DriveSafe NT remote program. No list of test languages is published, so contact MVR if
you need help with English.</p>

<h2>How old do you need to be?</h2>
<ul>
  <li><strong>Driver knowledge test and learner licence:</strong> from 16.</li>
  <li><strong>Provisional licence:</strong> you must hold your learner licence for 6 months in a row first, so the
  earliest is 16 years and 6 months.</li>
</ul>

<h2>What does the NT test cover?</h2>
<p>By law you must understand the road traffic laws before you get a learner licence, so the test is about NT road law:
the national road rules as the Territory applies them, plus its own licensing, speed, alcohol and phone rules. NT rules
that often surprise learners from other states:</p>
<ul>
  <li><strong>Higher default limits:</strong> 60 km/h in built-up areas unless a sign says otherwise, 110 km/h outside
  them, and 130 km/h on roads signed for it. Every NT road has a speed limit.</li>
  <li><strong>Learner and P caps:</strong> learners must not exceed 80 km/h and P drivers 100 km/h, whatever the sign
  says.</li>
  <li><strong>Front seats:</strong> when a learner drives, only the supervisor may sit in the front.</li>
  <li><strong>Supervisors:</strong> a supervisor must be over 18 and hold a full licence for that type of vehicle. They
  count as the driver for alcohol and drug laws and can be held responsible for the learner's offences.</li>
  <li><strong>Phones:</strong> learners and P drivers may not use a phone at all while driving, not even hands-free,
  unless the car is stopped out of the line of traffic.</li>
  <li><strong>Road trains:</strong> road trains up to 53.5 m long use NT roads, so leave plenty of room when following
  or overtaking one.</li>
</ul>

<h2>What happens after you pass?</h2>
<p>After the test you pass an eye test at an MVR office (or bring a recent eye report from a doctor or optometrist) and
pay the learner licence fee. The licence lasts 2 years. Show L plates at the front and rear, keep your alcohol at zero
and stay at or under 80 km/h. Five or more demerit points within 12 months brings a suspension.</p>
<p>After at least 6 months in a row on your learner licence you can take the practical driving test, an on-road drive of
about 40 minutes with an authorised driving examiner. There is no separate hazard perception test in the NT: the
examiner assesses how you respond to hazards, along with observation, speed, road position, decisions and control of
the car. If you pass in an automatic, your licence can be limited to automatics.</p>
<p>The NT has one provisional stage, with red P plates for the whole period: 2 years if you are under 25 when it starts,
or 12 months if you are 25 or older. P drivers keep to 100 km/h, zero alcohol and no phone use at all. If you are under
25, zero alcohol continues for a while after your P plates come off. Keep a clean record on your P plates for at least
12 months and you may qualify for a free 10-year licence.</p>

<h2>How to practise for the NT learners test with Learners Test Australia</h2>
<ul class="check-list">
  <li>30-question mock tests scored against the 26-question pass line.</li>
  <li>More than 380 original NT questions, written from NT legislation, including the Traffic Regulations 1999 and the
  Motor Vehicles Act 1949.</li>
  <li>NT-only rules such as the 80 km/h learner cap, the front-seat rule, 130 km/h roads and the single red P stage.</li>
  <li>Every answer explained, with the rule it comes from.</li>
</ul>
<p>Read <a href="@/blog/give-way-rules-for-learner-drivers.html">the give way rules every learner must know</a> for the
national rules the NT shares, and <a href="@/blog/how-to-use-mock-tests-and-mistakes.html">how to use mock tests and
mistakes</a> to plan your practice.</p>

{faq_block(NT_FAQ, heading="NT learners test questions people ask", hid="nt-faq")}

{source_box([
    ("Get your driver licence (nt.gov.au)", SRC["nt_licence"]),
    ("Practical driving test with an authorised driving examiner (nt.gov.au)", SRC["nt_practical"]),
    ("Motor Vehicles Act 1949 (legislation.nt.gov.au)", SRC["nt_mva"]),
    ("Traffic Regulations 1999 (legislation.nt.gov.au)", SRC["nt_tr"]),
], note="This page restates Northern Territory legislation in plain English. It is not an official version of that legislation.")}
{app_cta('nt', "It is not connected to the Northern Territory Government, the Motor Vehicle Registry (MVR) or the Registrar of Motor Vehicles.")}
</article>
<aside>{related(RELATED_NEW)}</aside>
</div></div>"""
    return Page(
        path="nt-learners-test-practice.html",
        title="NT Learners Test Practice | Learners Test Australia",
        description=("NT learners test practice: the driver knowledge test has 30 questions from a pool of 300+ (pass 26). "
                     "Where to sit it, ages, NT road rules and next steps."),
        body=body,
        nav="states",
        crumbs=crumbs,
        jsonld=[faq_ld(NT_FAQ)],
        priority="0.9",
        llms=True,
        llms_title="NT learners test practice",
        llms_note="Northern Territory driver knowledge test: 30 questions from a pool of 300+, pass 26, at an MVR office, from 16, no hazard perception test, NT rules and next steps.",
    )
