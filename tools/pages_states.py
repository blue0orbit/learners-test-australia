"""State landing pages: NSW DKT, VIC learner permit test, QLD written test and PrepL.

Every fact comes from content-src/coverage/{nsw,vic,qld}.md in the app repository (checked 30 September 2026).
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


def app_cta(state: str) -> str:
    return (f'<section class="callout light-cta" aria-labelledby="cta-{state}"><h2 id="cta-{state}" style="margin-top:0">'
            f"Practise with {SITE_NAME}</h2>"
            f"<p>{DISCLAIMER}</p>{coming_soon('light')}</section>")


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
