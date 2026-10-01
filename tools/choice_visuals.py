"""Accessible, server-rendered product visuals; no competitor claims or fake screenshots."""
from sitelib import PRICE, STATES, esc


def decorate_sections(sections):
    overview = '''<div class="choice-facts" aria-label="App at a glance">
<div><strong>8</strong><span>states &amp; territories</span></div>
<div><strong>Free</strong><span>every practice question</span></div>
<div><strong>One-time</strong><span>optional Premium</span></div></div>'''
    states = '<div class="choice-states" aria-label="Explore your state">' + ''.join(
        f'<a href="@/{path}"><strong>{code}</strong><span>{esc(name)}</span><span aria-hidden="true">↗</span></a>'
        for code, name, path in STATES) + '</div>'
    explanation = '''<figure class="choice-demo">
<div class="choice-demo-top"><span>THE LEARNING EXPERIENCE</span><span>Illustrative study flow</span></div>
<div class="choice-demo-grid"><div class="choice-answer"><span class="choice-step">01 / ANSWER</span>
<h3>You missed a question.<br>Now what?</h3><p>A result starts the review.</p>
<div class="choice-result"><span aria-hidden="true">↻</span> Review this answer</div></div>
<div class="choice-explain"><span class="choice-step">02 / UNDERSTAND</span>
<h3>Turn the mistake into a lesson.</h3><ol><li><strong>Read the explanation</strong><span>Understand the reason behind the answer.</span></li>
<li><strong>Check the source</strong><span>Find the handbook page or road rule.</span></li>
<li><strong>Practise it again</strong><span>Revisit the topic in your review.</span></li></ol></div></div>
<figcaption>Conceptual explanation of the study flow, not a screenshot or a measured learning outcome.</figcaption></figure>'''
    routine = '''<ol class="choice-flow" aria-label="Daily study routine">
<li><span>01</span><strong>Quick check</strong><small>Find your starting point</small></li>
<li><span>02</span><strong>Review</strong><small>Revisit questions due</small></li>
<li><span>03</span><strong>Fix mistakes</strong><small>Work through explanations</small></li>
<li><span>04</span><strong>Practise</strong><small>Try new questions</small></li></ol>'''
    plans = f'''<div class="choice-plans">
<section class="choice-plan"><p class="choice-kicker">BUILD YOUR ROUTINE</p><h3>Free practice</h3>
<p class="choice-price">A$0</p><p>Core learning, included.</p><ul><li>Every question + explanation</li>
<li>Daily plan, reviews and progress</li><li>1 mock test a day</li><li>Extra mocks through optional ads</li>
<li>Sample hazard practice</li></ul><p class="choice-plan-note">Includes ads.</p></section>
<section class="choice-plan choice-plan-premium"><p class="choice-kicker">MORE ROOM TO PRACTISE</p><h3>Premium</h3>
<p class="choice-price">{PRICE}<span> once</span></p><p>Everything in Free, plus:</p><ul><li>Unlimited mock tests</li>
<li>No ads</li><li>Section forecasts + weak spots</li><li>Review planner</li><li>Full hazard-practice collection</li></ul>
<p class="choice-plan-note">No subscription.</p></section></div>'''
    comparison = '''<p>Compare the two plans feature by feature. Both keep explained question practice at the centre of your preparation.</p>
<div class="table-wrap choice-comparison"><table><caption>Learners Test Australia: Free versus Premium</caption>
<thead><tr><th scope="col">What you get</th><th scope="col">Free</th><th scope="col">Premium</th></tr></thead>
<tbody><tr><th scope="row">Every question + explanation</th><td>Included</td><td>Included</td></tr>
<tr><th scope="row">Daily plan + reviews</th><td>Included</td><td>Included</td></tr>
<tr><th scope="row">Mock tests</th><td>1/day + optional ad extras</td><td>Unlimited</td></tr>
<tr><th scope="row">Ads</th><td>Included</td><td>None</td></tr>
<tr><th scope="row">Section forecasts + review planner</th><td>Not included</td><td>Included</td></tr>
<tr><th scope="row">Hazard practice</th><td>Samples</td><td>Full collection</td></tr></tbody></table></div>
<details class="choice-detail"><summary>Comparing us with another app? Use this checklist.</summary>
<p>Check its state coverage, answer explanations, source references, offline limits and total cost. Check what is free before paying.
We have not tested every store alternative; this comparison describes our own plans.</p></details>'''
    output=[]
    for sid,title,body in sections:
        if sid == 'fit': body=overview+body
        elif sid == 'state': body=states+body
        elif sid == 'explanations': body=explanation+body
        elif sid == 'routine': body=routine+body
        elif sid == 'value': body=plans+body
        elif sid == 'compare': title='Free or Premium? See the difference'; body=comparison
        elif sid == 'next':
            body += '<div class="choice-actions"><a class="btn btn-primary" href="@/features.html">Explore every feature ↗</a><a class="btn" href="@/states.html">Find your state</a></div>'
        output.append((sid,title,body))
    return output
