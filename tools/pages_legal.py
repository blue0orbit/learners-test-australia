"""Privacy policy, cookie policy, terms of service and account deletion pages.

The privacy policy and terms mirror the in-app text in app/src/main/res/values/strings.xml
(privacy_* and tos_* strings, both last updated 9 October 2026, app build 16, 0.16.0). Keep them
word-for-word in sync with the app: only headings and HTML structure are added here, plus website-only sections at
the end (privacy: "This website" and "The web app"; terms: "Web study app"), which the callout above each page
mentions. The web app sections describe the web study app at au.learnertest.com/app/, which is not part of this repo.
Premium bought on the website (Paddle, merchant of record) is described only in those website-only sections (privacy
"Buying Premium on the website", terms "Buying Premium on the website") and on the cookie and deletion pages: the
in-app text is about Google Play and must stay word-for-word the app's.
"""
from sitelib import (
    APP_NAME, BASE, COOKIES_DATE, COOKIES_DATE_H, DELETION_DATE, DELETION_DATE_H, DEVELOPER, EMAIL, LEGAL_DATE, LEGAL_DATE_H, PACKAGE, PRICE, SITE_NAME, SRC,
    TERMS_DATE, TERMS_DATE_H, Page, page_head, updated_line,
)

MAIL = f'<a href="mailto:{EMAIL}">{EMAIL}</a>'
# The web study app (served by Cloudflare, not built from this repo)
WEB_APP = f"{BASE}app/"
WEB_APP_LINK = f'<a href="{WEB_APP}">au.learnertest.com/app/</a>'
# Paddle, the merchant of record for Premium bought on the website (Paddle Buyer Terms, last updated 31 March 2026)
PADDLE_BUYER_TERMS = "https://www.paddle.com/legal/checkout-buyer-terms"
PADDLE_REFUNDS = "https://www.paddle.com/legal/refund-policy"
PADDLE_PRIVACY = "https://www.paddle.com/legal/privacy"
PADDLE_NET = "https://paddle.net"


def legal_intro(kind: str, in_app_path: str, extra: str) -> str:
    return (
        f'<div class="callout"><p><strong>App:</strong> {APP_NAME} (Android) · <strong>Developer:</strong> {DEVELOPER} · '
        f"<strong>Contact:</strong> {MAIL}</p>"
        f"<p>This is the same {kind} shown in the app ({in_app_path}), plus {extra} at the end.</p></div>"
    )


# ── Privacy policy ────────────────────────────────────────────────────────────────────────────
def privacy() -> Page:
    crumbs = [("Home", ""), ("Privacy policy", "privacy-policy.html")]
    body = page_head(
        "Privacy Policy",
        f"How the {SITE_NAME} app and web app handle your information, and a note on this website.",
        crumbs,
        meta_html=updated_line(LEGAL_DATE, LEGAL_DATE_H),
    ) + f"""
<div class="content"><div class="container prose">
{legal_intro("privacy policy", "Settings → Privacy policy", "sections on this website and the web app")}

<h2 id="overview">Overview</h2>
<p>Learners Test Australia is an independent study app by blue0orbit, a sole trader (“we”, “us”), that helps you prepare for an Australian learner driver knowledge test. It is not affiliated with any government, transport or licensing agency.</p>
<p>This policy explains what the app collects, why, and the choices you have. Questions: {MAIL}.</p>

<h2 id="information-we-collect">Information we collect</h2>
<p><strong>Account:</strong> when you sign in, we receive your name, your email address and a user ID from Google Firebase Authentication. You can sign in with Google, or with an email address and password (Firebase handles your password; we never see it). Where the app offers it, you can also sign in with Facebook. If you agree to tips and offers by email, we store that choice and when you made it.</p>
<p><strong>Study data:</strong> your answers, completed practice sessions and mock tests, saved questions and the state you study for. This is stored on your device and in your account so it follows you to a new phone. Your test date and reminder settings stay on your device.</p>
<p id="premium-purchases"><strong>Premium purchases:</strong> Google Play handles the payment, and we never see your card or payment details. When you buy Premium, the app adds a one-way hash of your account’s user ID to the purchase, and Google Play keeps it with its record of the purchase. This ties the purchase to your learner account. The app checks your purchases with Google Play on your phone.</p>
<p id="purchase-checks"><strong>Purchase checks on our server (being switched on in stages):</strong> blue0orbit runs a purchase-checking service on Google Cloud in Belgium (europe-west1). We are switching it on in stages. In the first stage, the app sends your purchases to the service, which checks and records them, but Premium is still decided on your phone. In the next stage, the service’s record decides Premium. Until the service is switched on for your app, the app sends nothing to it. While it is on and you are signed in, each time Google Play tells the app which purchases you have (when the app starts, and after a purchase, a restore or a sign-in), the app sends the service the Google Play purchase token and product of each Premium purchase on your phone that was made with your learner account or with no account attached, together with a Firebase ID token, which identifies your account, and an App Check token. Purchases tied to another learner account are not sent, and nothing is sent while you are signed out. Extra mock tests earned by watching an ad always stay on your phone and are never sent to this service.</p>
<p>The service checks each purchase with Google Play, links it to the first account that verified it (another account can’t then use it) and receives refund notices from Google Play. It keeps its purchase records (your account’s user ID, each purchase token, the product, the purchase’s status and when it was checked) in Belgium for up to 6 years, so a purchase can be restored and can’t be claimed twice, and to meet our legal and accounting obligations. It writes your Premium record in your account in our Firebase project, stored in Sydney (australia-southeast1): the features unlocked, a revision number, an end time for any time-limited pass, and when the record was worked out. The app reads this record, and only the service can change it. The app also keeps the service’s latest answer for your account on your phone. Once the record decides Premium, Premium bought with the same account on another of our services is honoured in the app too. About a day after you delete your account, the service deletes your Premium record. Google Cloud logs technical details of each request to the service, such as your IP address, and keeps these logs for a limited time.</p>
<p><strong>App protection:</strong> to keep our cloud database for the genuine app, the app uses Firebase App Check with Google Play Integrity. Google checks that the app and your device are genuine, and the app sends the resulting token with its requests to Firebase.</p>
<p><strong>Push messages:</strong> Firebase Cloud Messaging gives the app a push token, so we can send announcements to all learners or to learners in one state. You receive them only if notifications are on.</p>
<p><strong>If you allow “Help improve the app”:</strong> usage statistics (screens viewed, features used, the state you study for, test results and the app language) with an app instance ID, your device model, Android version, app version and approximate location (country, region or city), plus crash reports and performance data (such as app start time and how long network requests take). They are not linked to your name, email address or user ID, and analytics never collects your advertising ID.</p>
<p id="ads"><strong>Ads:</strong> the free version shows banner ads from Google AdMob on results and guide pages, and you can choose to watch a rewarded video from Unity Ads to get an extra mock test. Ad providers receive your device’s advertising ID, IP address (from which they estimate your general location), device information and how you interact with ads. Ads are requested only after Google’s consent tool has checked whether consent is needed where you are. Where the law requires it (for example in the EEA, the UK and Switzerland), Google asks you first: ads are personalised only if you agree. You can change your choice in Settings → Ad privacy choices, which appears where it applies to you. Elsewhere, ads may be personalised. You can reset or delete your advertising ID in your phone’s settings at any time.</p>

<h2 id="how-we-use-your-data">How we use your data</h2>
<p>We use your data to:</p>
<ul>
  <li>Create your account and keep your progress in sync</li>
  <li>Build your daily plan, reviews and pass-chance estimate</li>
  <li>Check and restore your Premium purchase, and stop one purchase being used by several accounts</li>
  <li>Protect the app and our cloud database from abuse</li>
  <li>Send study reminders and announcements, if you turn them on</li>
  <li>Send tips and offers by email, only if you opt in (unsubscribe any time)</li>
  <li>Show ads in the free version</li>
  <li>Fix crashes and improve the app, if you allow it</li>
</ul>
<p>We don’t sell your name, email address or study data. Ad providers may use your advertising ID as described above.</p>

<h2 id="third-party-services">Third-party services</h2>
<p>The app uses these services, each with its own privacy policy:</p>
<ul>
  <li>Google Firebase — sign-in, cloud storage of progress, analytics, crash and performance reports, push messages, remote settings and app protection (App Check)</li>
  <li>Google Play — Premium purchases and purchase checks, Play Integrity checks and in-app ratings (we never see your payment details)</li>
  <li>Google Cloud — runs our purchase-checking service, in Belgium</li>
  <li>Google AdMob — banner ads (free version)</li>
  <li>Unity Ads — optional rewarded video ads (free version)</li>
  <li>Google User Messaging Platform — ad consent where required</li>
  <li>Facebook Login — optional sign-in, where the app offers it</li>
</ul>
<p>Some of these providers store or process data outside Australia, for example in the United States. Our purchase-checking service runs on Google Cloud in Belgium and keeps its purchase records there, outside Australia.</p>

<h2 id="data-protection-and-retention">Data protection &amp; retention</h2>
<p>We share your data only with the providers above, for the purposes in this policy. Data is sent over encrypted connections, and your cloud progress and profile can only be read by your own account. Your Premium record can be read only by your account and changed only by our purchase-checking service.</p>
<p>We keep your data while your account exists. Delete your account in Settings and your cloud progress, profile and sign-in are deleted straight away; Google then removes them from its backup systems, which Google says can take up to 180 days. About a day after you delete your account, our purchase-checking service deletes your Premium record, if you have one. The service keeps its purchase records for up to 6 years, and Google Cloud keeps its request logs for a limited time (see <a href="#purchase-checks">“Purchase checks on our server”</a>). Firebase keeps crash reports for 90 days. Google Play keeps its own record of your purchases under its own policies. You can also email us to ask for deletion.</p>

<h2 id="your-rights">Your rights</h2>
<p><strong>Australia:</strong> we handle personal information under the Australian Privacy Principles (Privacy Act 1988). You can ask to access or correct your information, or complain, by emailing us. If you are not satisfied with our response you can contact the Office of the Australian Information Commissioner (<a href="https://www.oaic.gov.au/" rel="noopener">oaic.gov.au</a>).</p>
<p><strong>EEA and UK:</strong> you have rights to access, correct, delete, restrict and port your data, to object to processing, and to withdraw your consent at any time (in Settings or by emailing us). We rely on your consent for analytics, marketing email and personalised ads, and on our contract with you to run your account and check your purchases.</p>
<p><strong>Children:</strong> the app is for people preparing for a learner licence, usually 15 and over. It is not directed at children under 13, and we do not knowingly collect their data.</p>
<p><strong>Changes:</strong> if we change this policy in an important way, we will tell you in the app first.</p>

<h2 id="contact">Contact</h2>
<p>Privacy questions, data requests or complaints:</p>
<p>Email: {MAIL}</p>
<p>We aim to reply within 5 business days.</p>

<h2 id="website">This website</h2>
<p>This section is about the website you are reading now (au.learnertest.com), not the Android app. The points below
cover its information pages; the web study app at au.learnertest.com/app/ works differently and is covered in
<a href="#web-app">The web app</a> below.</p>
<ul>
  <li><strong>No cookies.</strong> These pages set no cookies and store nothing in your browser (no local storage or similar).</li>
  <li><strong>No analytics or trackers.</strong> There are no analytics, advertising, tracking pixels or social media widgets.</li>
  <li><strong>Nothing loaded from third parties.</strong> Fonts, images, styles and the one small script (it opens and closes the menu on small screens) are all served from this website itself.</li>
  <li><strong>Hosting.</strong> The site is delivered by Cloudflare, Inc. (domain name service, content delivery and hosting) and GitHub, Inc. (GitHub Pages). They process technical data such as your IP address and browser details to deliver the pages securely (see <a href="{SRC['cloudflare_privacy']}" rel="noopener">Cloudflare's privacy policy</a>). GitHub says it logs the IP address of visitors to GitHub Pages sites for security purposes (see <a href="{SRC['gh_pages_data']}" rel="noopener">About GitHub Pages</a>). Both are US companies, so this may happen outside Australia. We don't use those logs, and the site has no analytics of its own.</li>
  <li><strong>Email.</strong> If you email us, we use your message and email address to reply to you. If you ask to try the app early, we also use your email address to invite you to the test on Google Play, and remove it from the test list when you ask or when testing ends.</li>
</ul>

<h2 id="web-app">The web app</h2>
<p>This section is about the web study app at {WEB_APP_LINK}. It started as an invite-only beta and is now open to
everyone: anyone with an account can sign in and study there. The web app shows no ads and uses no analytics.</p>

<h3 id="web-app-sign-in">Signing in</h3>
<p>You sign in with the same account as the Android app, with Google or with an email address and password, or you can create an account there. Sign-in uses Google Firebase Authentication, in the same Firebase project as the app. If you use an email address and password, you must confirm your email address with the link Firebase sends you. Firebase keeps you signed in with a token stored in your browser. Facebook sign-in, which the app offers, is not available in the web app.</p>

<h3 id="web-app-recaptcha">Protection against abuse</h3>
<p>Inside the web app only, we use Firebase App Check with Google reCAPTCHA Enterprise to stop automated copying of our questions and other abuse. While you use the web app, reCAPTCHA assesses your browser to tell genuine use from automated scripts. To do this, Google may set cookies and collect information about your device and browser and how you interact with the page, under Google’s <a href="https://policies.google.com/privacy" rel="noopener">Privacy Policy</a> and <a href="https://policies.google.com/terms" rel="noopener">Terms of Service</a>. The web app shows the notice “This site uses reCAPTCHA to stop automated abuse.” reCAPTCHA does not run on the rest of this website.</p>

<h3 id="web-app-question-service">What the question service keeps</h3>
<p>The web app’s pages and its question service are hosted by Cloudflare (Cloudflare Workers and a Cloudflare D1 database), which processes your IP address and technical details of each request to deliver them and to protect them from attacks. The question service gives the web app its questions, puts together mock exams and marks them. It keeps the following, linked only to your account’s user ID (not your name or email address):</p>
<ul>
  <li>Which questions it has given your account, and the day each one was first given, to limit copying of the question bank. These are deleted once your account has gone a year without new questions and 35 days without getting any questions or mock exams.</li>
  <li>Daily counts of the questions, new questions and mock exams it has given your account, for the daily fair-use limits. These are deleted after about 35 days.</li>
  <li>The mock exams it put together for you: the questions, their order, the language, the start time, the time limit and the time you handed the exam in. These are deleted after about 90 days.</li>
  <li>While the web app is invite-only: the list of invited accounts (the user ID, the date it was added and a short note), so that only those accounts can study there. The web app is open to everyone now and does not use the list, but the list from the beta is kept: an entry is not deleted automatically; we remove it when you ask.</li>
</ul>
<p>To apply the right limits, the question service checks, using your own sign-in, whether our Firebase project holds a Premium record for your account. It keeps the answer in memory for up to five minutes and does not store it.</p>
<p>Your practice answers are checked in your browser and never sent to us. When you hand in a mock exam, your answers are sent only so it can be marked: the question service sends back your result and does not keep your answers. Your IP address is used to limit the number of requests from each address; it is not stored in the question service’s database.</p>

<h3 id="web-app-purchases">Buying Premium on the website</h3>
<p>If you buy Premium in the web app, it is sold through Paddle, our reseller and the merchant of record for these purchases: Paddle.com Market Limited, or the Paddle company named in <a href="{PADDLE_BUYER_TERMS}" rel="noopener">Paddle’s buyer terms</a> for where you buy. Paddle runs the checkout, takes the payment, handles sales tax, sends your receipt and handles refunds and chargebacks. Premium bought in the Android app through Google Play is covered under <a href="#premium-purchases">Premium purchases</a> above.</p>
<ul>
  <li><strong>What you give Paddle.</strong> Only when you choose to buy, the web app loads Paddle’s checkout from Paddle and opens it over the page. In the checkout you give Paddle your email address, your country (and postcode where tax needs it), your payment details and anything else the checkout asks for. Paddle is responsible for this information itself and handles it under its own <a href="{PADDLE_PRIVACY}" rel="noopener">privacy notice</a>, which also covers anything Paddle’s checkout collects about your device or browser. We never receive your full card number, and we don’t keep any payment details: Paddle’s payment notices to our service can include the card type, its last four digits, its expiry date and the cardholder’s name (or, for PayPal, the PayPal email address), which our service does not store.</li>
  <li><strong>What the web app and our server send.</strong> When you choose to buy, the web app sends our purchase-checking service (see <a href="#purchase-checks">Purchase checks on our server</a>) the product, a Firebase ID token, which identifies your account, and an App Check token. The service then asks Paddle for a checkout with Premium’s price and a random reference that lets us match the payment to your account. We don’t send Paddle your name, email address or user ID. As with the app’s requests, Google Cloud logs technical details of each request to the service, such as your IP address, and keeps these logs for a limited time.</li>
  <li><strong>What we keep.</strong> Our service checks each payment with Paddle and keeps a purchase record: your account’s user ID, the product, the price and currency, Paddle’s transaction ID, our checkout reference, the payment’s status (completed, refunded, charged back or reversed) and the IDs of any refunds, with the times. We don’t keep your name, email address, postal address, billing country or payment details. Paddle’s notifications to our service are checked to make sure they come from Paddle, and the service keeps only the details listed here, never the notification itself.</li>
  <li><strong>Your Premium.</strong> You must be signed in to buy, and Premium belongs to the account you were signed in to when you bought it. Once Paddle confirms the payment and our service has checked it with Paddle, usually within about 10 minutes, the service adds Premium to your Premium record in our Firebase project in Sydney, which the web app uses. The Android app does not use Premium bought on the website yet. If Paddle makes a full refund, or the payment is charged back, the service removes Premium from your Premium record.</li>
  <li><strong>Why we use it.</strong> To give you the Premium you paid for and keep it on your account, to deal with refunds and chargebacks, to stop one payment being used twice or by another account, to prevent fraud and handle disputes, and to keep the records the law requires for tax and accounting. If you are in the EEA or the UK, we rely on our contract with you (giving you what you paid for, and refunds), our legal obligations (tax and accounting) and our legitimate interests (preventing fraud and handling disputes and chargebacks).</li>
  <li><strong>Who else sees what.</strong> Paddle sees what you give it at checkout, plus the product and price. Paddle’s payment processors and banks handle your payment details. Google hosts our purchase records and your Premium record for us. We don’t sell this information.</li>
  <li><strong>How long we keep it.</strong> We keep purchase records for up to 6 years, also after you delete your account, to meet our legal and accounting obligations. About a day after you delete your account, the service deletes your Premium record. Paddle keeps its own records of your purchase under its own privacy notice.</li>
</ul>
<p>For receipts, refunds and help with a payment, go to <a href="{PADDLE_NET}" rel="noopener">paddle.net</a> or use the link in Paddle’s receipt email.</p>

<h3 id="web-app-overseas">Where web app data is stored</h3>
<p>The question service’s database is stored by Cloudflare in data centres in Western Europe, so the records listed above are held outside Australia. Cloudflare, which delivers the web app, and Google, which provides Firebase Authentication and reCAPTCHA, are US companies and may also process data from the web app in the United States and other countries where they operate. We use them only to run the web app.</p>
<p>If you buy Premium on the website, Paddle handles the purchase: Paddle.com Market Limited is in the United Kingdom, and Paddle and its payment processors may also handle your information in other countries. Our purchase records are stored on Google Cloud in Belgium (europe-west1), outside Australia, and your Premium record in our Firebase project in Sydney.</p>

<h3 id="web-app-progress">Progress stored in your browser</h3>
<p>The progress the web app shows (your answers and mock exam results), your saved questions and your settings in it (state, test date, daily goal and question language) are stored only in your browser’s local storage on that device, separately for each account. They are not synced with the Android app yet. To delete your answers and mock exam results for the test you are studying, open Progress → Delete progress on this device in the web app; to delete everything, clear this site’s data in your browser.</p>

<h3 id="web-app-deletion">Deleting what the question service keeps</h3>
<p>You can delete the question service’s record of which questions it gave your account, and your mock exams, at any time: in the web app, open Account → Delete what our server keeps, or email {MAIL}. Daily counts stay until they expire after about 35 days, because deleting them early would reset the daily limits. To be removed from the beta invite list, email us.</p>
<p>The web app has no Delete account option of its own yet: delete your account in the Android app or by email (see <a href="@/account-deletion.html">delete your account</a>). The question service is not told when your account is deleted, so delete its records first in the web app, or email us. Otherwise they are deleted only as described above: the record of which questions it gave you once your account has gone a year without new questions and 35 days without getting any questions or mock exams, daily counts after about 35 days and mock exams after about 90 days.</p>
<p>If you bought Premium on the website, our purchase-checking service deletes your Premium record about a day after your account is deleted, and keeps its purchase records for up to 6 years (see <a href="#web-app-purchases">Buying Premium on the website</a>).</p>

<p>See also the <a href="@/cookies.html">cookie policy</a> and how to <a href="@/account-deletion.html">delete your account</a>.</p>
</div></div>"""
    return Page(
        path="privacy-policy.html",
        lastmod=LEGAL_DATE,
        title="Privacy Policy | Learners Test Australia",
        description=("Privacy policy for the Learners Test Australia app and web app: what we collect, why, third-party "
                     "services, retention, your rights, and this website."),
        body=body,
        crumbs=crumbs,
        priority="0.4",
        changefreq="yearly",
        llms=True,
        llms_title="Privacy policy",
        llms_note=("The app's privacy policy (same text as in the app) plus sections on this website (no cookies, analytics "
                   "or third-party requests outside the web app) and on the web study app (sign-in, reCAPTCHA, what the "
                   "question service keeps, Premium bought on the website through Paddle as merchant of record and the "
                   "purchase records we keep, storage outside Australia, progress stored in the browser, deletion)."),
    )


# ── Cookie policy ─────────────────────────────────────────────────────────────────────────────
def cookies() -> Page:
    crumbs = [("Home", ""), ("Cookie policy", "cookies.html")]
    body = page_head(
        "Cookie policy",
        "Our information pages set no cookies. Here is what the web app and the Android app use, and how to control it.",
        crumbs,
        meta_html=updated_line(COOKIES_DATE, COOKIES_DATE_H),
    ) + f"""
<div class="content"><div class="container prose">
<div class="answer-box"><p class="answer-label">In short</p>
<p>Apart from the web study app at au.learnertest.com/app/, the {SITE_NAME} website sets no cookies, stores nothing
in your browser and loads nothing from third parties, so there is no cookie banner to accept. The web app keeps your
progress in your browser's local storage, keeps you signed in with a Firebase token in your browser, and uses Google
reCAPTCHA, which may set cookies, to stop automated abuse. Only if you choose to buy Premium there does it load
Paddle's checkout. The Android app works differently from a website: it keeps
data on your phone, uses Google Firebase for your account and progress, and in the free version lets ad providers use
your advertising ID, subject to consent where the law requires it.</p></div>

<h2>Does this website use cookies?</h2>
<p>Not outside the web app. The information pages set no cookies and use no local storage, analytics, advertising or
tracking of any kind. Every file they use (pages, fonts, images, styles and the small menu script) comes from this
site. The site is delivered by Cloudflare and GitHub Pages; see the <a href="@/privacy-policy.html#website">privacy
policy</a> for what they process. The web app is covered in the next section.</p>

<h2 id="web-app">What does the web app use?</h2>
<p>The web study app at {WEB_APP_LINK} uses the following, as described in the
<a href="@/privacy-policy.html#web-app">privacy policy</a>.</p>

<h3>Local storage in your browser</h3>
<p>The progress the web app shows (answers and mock exam results), your saved questions and your settings in it
(state, test date, daily goal and question language) are stored only in your browser's local storage on that device,
separately for each account. They are not synced with the Android app yet. To delete your answers and mock exam
results for the test you are studying, open Progress → Delete progress on this device in the web app; to delete
everything, clear this site's data in your browser.</p>

<h3>Firebase sign-in</h3>
<p>Firebase Authentication keeps you signed in to the web app with a token stored in your browser.</p>

<h3>Google reCAPTCHA</h3>
<p>Inside the web app only, Firebase App Check uses Google reCAPTCHA Enterprise to stop automated abuse. Google may set
cookies and collect information about your device and browser and how you interact with the page, under Google's
<a href="https://policies.google.com/privacy" rel="noopener">Privacy Policy</a> and
<a href="https://policies.google.com/terms" rel="noopener">Terms of Service</a>. The web app shows the notice “This site
uses reCAPTCHA to stop automated abuse.”</p>

<h3>Paddle checkout (only if you buy Premium)</h3>
<p>Premium bought on the website is sold through Paddle. Only when you choose to buy, the web app loads Paddle's checkout
script from Paddle and opens Paddle's checkout over the page, in Paddle's own frame. What Paddle's checkout collects,
including any cookies it uses, is covered by <a href="{PADDLE_PRIVACY}" rel="noopener">Paddle's privacy notice</a>.
See <a href="@/privacy-policy.html#web-app-purchases">Buying Premium on the website</a> in the privacy policy.</p>

<h2>What does the Android app use instead of cookies?</h2>
<p>Apps don't rely on browser cookies the way websites do. The {SITE_NAME} app uses the following, as described in
its <a href="@/privacy-policy.html">privacy policy</a>.</p>

<h3>Storage on your phone</h3>
<p>The app keeps your study data (answers, sessions, saved questions and your chosen state) on your phone so it works
without a connection, and syncs it to your account. Your test date, reminder settings and display preferences stay
on your phone. To remove them, uninstall the app or clear its storage in Android's app settings. Clearing storage
signs you out but doesn't delete the progress saved to your account; to delete that, see
<a href="@/account-deletion.html">delete your account</a>.</p>

<h3>Google Firebase</h3>
<ul>
  <li><strong>Sign-in and cloud storage of progress:</strong> needed for your account and to keep your progress in sync.</li>
  <li><strong>Analytics and crash reports:</strong> usage statistics and crash reports with an app instance ID, not linked to your name, email address or user ID, only if you allow “Help improve the app”. You can switch this on or off in the app's Settings, under Privacy.</li>
  <li><strong>Push messages:</strong> Firebase Cloud Messaging gives your phone a push token so the app can receive announcements. You can turn notifications off in Android settings at any time.</li>
  <li><strong>Remote settings:</strong> lets us adjust some app settings without an update.</li>
  <li><strong>App protection:</strong> Firebase App Check with Google Play Integrity checks that requests to our cloud database come from the genuine app on a genuine device.</li>
</ul>

<h3>Advertising identifiers (free version)</h3>
<p>The free version shows banner ads from Google AdMob and optional rewarded video ads from Unity Ads. These ad
providers may use your device's advertising ID. Ads are requested only after Google's User Messaging Platform has
checked whether consent is needed where you are. Where the law requires it (for example in the EEA, the UK and
Switzerland), it asks for your consent first: ads are personalised only if you agree. Premium removes ads.</p>
<p><strong>To change your ad choices in the app:</strong> open Settings → Ad privacy choices. This option appears
where a consent choice applies to you.</p>

<h3>Facebook Login</h3>
<p>Facebook is used only as an optional way to sign in. The app switches off Facebook's automatic app events and
advertising ID collection, so nothing is sent to Meta unless you choose “Continue with Facebook”, and then only what
sign-in needs.</p>

<h2>How do I reset or delete my advertising ID on Android?</h2>
<ol>
  <li>Open your phone's <strong>Settings</strong>.</li>
  <li>Find the <strong>Ads</strong> page. Depending on your phone it is under <strong>Google → Ads</strong>, or
  <strong>Security &amp; privacy → More privacy settings → Ads</strong>.</li>
  <li>Choose <strong>Reset advertising ID</strong> to get a new one, or <strong>Delete advertising ID</strong>
  (Android 12 and later) so apps can no longer use it for ads.</li>
</ol>

<h2>Summary</h2>
<div class="table-wrap"><table>
<thead><tr><th scope="col">What</th><th scope="col">Where</th><th scope="col">Why</th><th scope="col">Your choice</th></tr></thead>
<tbody>
<tr><th scope="row">Cookies</th><td>This website, outside the web app</td><td>None used</td><td>Nothing to set</td></tr>
<tr><th scope="row">Browser local storage</th><td>Web app</td><td>Progress, saved questions and settings in the web app</td><td>Progress → Delete progress on this device, or clear this site's data</td></tr>
<tr><th scope="row">Firebase sign-in token</th><td>Web app</td><td>Keeps you signed in</td><td>Clear this site's data</td></tr>
<tr><th scope="row">reCAPTCHA cookies (Google)</th><td>Web app</td><td>Stop automated abuse</td><td>Used only inside the web app</td></tr>
<tr><th scope="row">Paddle checkout</th><td>Web app, when you buy Premium</td><td>Payment, tax and receipt, by Paddle</td><td>Loaded only if you choose to buy</td></tr>
<tr><th scope="row">Phone storage</th><td>App</td><td>Progress, settings, offline practice</td><td>Uninstall or clear storage</td></tr>
<tr><th scope="row">Firebase sign-in and sync</th><td>App</td><td>Your account and progress</td><td>Delete your account</td></tr>
<tr><th scope="row">Analytics and crash reports</th><td>App</td><td>Fix crashes, improve the app</td><td>Settings → Help improve the app</td></tr>
<tr><th scope="row">Push token</th><td>App</td><td>Announcements</td><td>Android notification settings</td></tr>
<tr><th scope="row">Advertising ID</th><td>App (free version)</td><td>Ads from AdMob and Unity Ads</td><td>Settings → Ad privacy choices (where shown); reset or delete the ID in Android settings; Premium removes ads</td></tr>
</tbody></table></div>

<p>Questions? Email {MAIL}.</p>
</div></div>"""
    return Page(
        path="cookies.html",
        lastmod=COOKIES_DATE,
        title="Cookie Policy | Learners Test Australia",
        description=("Our info pages set no cookies. See what the Learners Test Australia web app and Android app use "
                     "(browser storage, reCAPTCHA, ad ID) and how to control it."),
        body=body,
        crumbs=crumbs,
        priority="0.3",
        changefreq="yearly",
        llms_note=("The website sets no cookies outside the web study app; what the web app (browser storage, Firebase "
                   "sign-in, reCAPTCHA, Paddle's checkout if you buy Premium) and the Android app use, and how to change ad "
                   "choices or reset the advertising ID."),
    )


# ── Terms of service ──────────────────────────────────────────────────────────────────────────
def terms() -> Page:
    crumbs = [("Home", ""), ("Terms of service", "terms.html")]
    body = page_head(
        "Terms of Service",
        f"The terms for using the {SITE_NAME} app and web app.",
        crumbs,
        meta_html=updated_line(TERMS_DATE, TERMS_DATE_H),
    ) + f"""
<div class="content"><div class="container prose">
{legal_intro("terms of service", "Settings → Terms", "a section on the web app")}

<h2 id="acceptance">1. Acceptance of Terms</h2>
<p>By downloading, installing, or using Learners Test Australia ("the App"), you agree to be bound by these Terms of Service ("Terms"). If you do not agree to these Terms, please do not use the App. These Terms form a legally binding agreement between you and the developer of Learners Test Australia. Your continued use of the App after any changes to these Terms constitutes acceptance of the updated Terms.</p>

<h2 id="disclaimer">2. App Disclaimer</h2>
<p>Learners Test Australia is an independent study aid designed to help users prepare for an Australian learner driver knowledge test. It is NOT affiliated with, endorsed by, sponsored by, or connected in any way to any Australian state or territory government, transport department or licensing agency.</p>
<p>All practice questions and educational content within the App are for study and preparation purposes only. Completing this App, achieving high scores, or unlocking any in-app achievement does NOT guarantee passing your official learner test. The official test is run by your state or territory's licensing authority. Always refer to its current official handbook and website for authoritative information.</p>

<h2 id="eligibility">3. Eligibility</h2>
<p>The App is intended for users who are preparing for an Australian learner driver knowledge test. You must be at least 15 years of age to use the App and create an account. If you are under 18, you confirm that a parent or legal guardian has consented to your use of the App. By using the App, you represent and warrant that you meet these eligibility requirements.</p>

<h2 id="accounts">4. User Accounts &amp; Responsibilities</h2>
<p>You are responsible for maintaining the confidentiality of your account credentials and for all activity that occurs under your account. You agree to provide accurate and complete information when registering and to keep this information up to date. You may not share your account with others, create multiple accounts for abusive purposes, or use another person's account without permission.</p>
<p>You are responsible for safeguarding your password and agree to notify us immediately at {MAIL} if you suspect any unauthorised access to your account. We are not liable for any loss resulting from unauthorised use of your account.</p>

<h2 id="billing">5. Premium &amp; Billing</h2>
<p>Some features are available through a one-time purchase (“Premium”). Premium is a lifetime purchase: there are no subscriptions or renewals.</p>
<p>Purchases are processed by Google Play under its terms of sale. We never see or store your payment details.</p>
<p>Premium belongs to the learner account you were signed in with when you bought it, so other accounts on the same phone don’t get it. We are switching on our purchase-checking service in stages (see the Privacy Policy). Until its record decides Premium, the app checks Premium with Google Play on your phone, so the Google Play account that paid must be on that phone too. Once the record decides, Premium follows your learner account: sign in with it to use Premium on another phone.</p>
<p>Refunds follow Google Play’s refund policy and your rights under the Australian Consumer Law. A refunded purchase no longer unlocks Premium.</p>
<p>If Premium is not showing after you bought it, open Settings → Premium → Restore purchase, or email {MAIL}.</p>

<h2 id="acceptable-use">6. Acceptable Use</h2>
<p>You agree to use the App only for lawful purposes and in accordance with these Terms. You must not:</p>
<ul>
  <li>Attempt to gain unauthorised access to any part of the App, its servers, or any connected systems.</li>
  <li>Reverse engineer, decompile, disassemble, or attempt to extract the source code of the App.</li>
  <li>Copy, reproduce, or distribute any App content without our express written permission.</li>
  <li>Use automated tools, bots, or scrapers to access or collect data from the App.</li>
  <li>Impersonate any person or entity, or misrepresent your affiliation with any person or entity.</li>
  <li>Attempt to circumvent any content protection, subscription verification, or security measure within the App.</li>
</ul>
<p>We reserve the right to suspend or terminate your account if we determine, in our sole discretion, that you have violated these Terms.</p>

<h2 id="intellectual-property">7. Intellectual Property</h2>
<p>All content in the App — including practice questions, explanations, illustrations, icons, text and software — is owned by or licensed to the developer and protected by intellectual property laws. Questions are written for the App and checked against official sources (handbooks, legislation and government pages, listed under Settings, Official sources and licences); official material is referenced, not reproduced.</p>
<p>You may use the App for your own personal, non-commercial study. You may not copy, sell or distribute its content.</p>
<p>The Learners Test Australia name and logo belong to the developer.</p>

<h2 id="warranties">8. Disclaimer of Warranties</h2>
<p>The App is provided on an "as is" and "as available" basis without warranties of any kind, either express or implied. To the fullest extent permitted by applicable law, we disclaim all warranties, including but not limited to implied warranties of merchantability, fitness for a particular purpose, and non-infringement.</p>
<p>We do not warrant that the App will be uninterrupted or error-free. We do not warrant the accuracy, completeness, or currency of any question or content within the App. Question content is for educational preparation only and may not reflect the exact content of your state or territory's current official learner test.</p>
<p>We make no guarantee that use of the App will result in passing an official learner test.</p>

<h2 id="liability">9. Limitation of Liability</h2>
<p>To the maximum extent permitted by applicable law, the developer of Learners Test Australia shall not be liable for any indirect, incidental, special, consequential, or punitive damages arising from your use of — or inability to use — the App, including but not limited to failure to pass an official learner test, loss of data, or loss of revenue, even if advised of the possibility of such damages.</p>
<p>Our total aggregate liability to you for any claim arising from these Terms or your use of the App shall not exceed the amount you paid for Premium in the 12 months preceding the claim, or A$10, whichever is greater. Nothing in these Terms limits liability that cannot be excluded under applicable consumer protection law, including the Australian Consumer Law.</p>

<h2 id="termination">10. Termination</h2>
<p>We may suspend or end access to the App if you seriously breach these Terms.</p>
<p>You can delete your account at any time in Settings. Deleting it erases your progress in every state and your profile, as described in our <a href="@/privacy-policy.html">Privacy Policy</a>. Deleting your account does not refund a purchase, except where required by law.</p>
<p>Premium belongs to the learner account that bought it, so if you delete that account, Premium can't be moved to a new account automatically. Email us if you need help.</p>

<h2 id="changes">11. Changes to These Terms</h2>
<p>We may update these Terms from time to time to reflect changes to the App, our practices, or applicable law. When we make material changes, we will update the "Last updated" date shown on this page and may notify you within the App.</p>
<p>Your continued use of the App after any changes constitutes acceptance of the updated Terms. If you do not agree to the updated Terms, you should stop using the App before the changes take effect.</p>

<h2 id="governing-law">12. Governing Law &amp; Contact</h2>
<p>These Terms are governed by and construed in accordance with the laws of New South Wales, Australia. Any disputes arising under these Terms shall be subject to the non-exclusive jurisdiction of the courts of New South Wales and the federal courts of Australia, without prejudice to any mandatory consumer protection rights you may have under the law of your country, including the Australian Consumer Law.</p>
<p>If you have any questions about these Terms, please contact us at:</p>
<p>Email: {MAIL}</p>
<p>We aim to respond to all enquiries within 5 business days.</p>

<h2 id="web-app">Web study app</h2>
<p>The web study app at {WEB_APP_LINK} uses the same account as the Android app, and these Terms apply to it. Anyone
with an account can use it. In addition:</p>
<ul>
  <li><strong>Fair use.</strong> To keep the service fair and protect the question bank, each account has daily limits on the number of questions, new questions and mock exams it can get in the web app. Our server applies these limits, and we may adjust them.</li>
  <li><strong>Practice only.</strong> Mock exam results in the web app are for practice only. They are not an official test result and do not count towards any official test.</li>
  <li><strong>No scraping or automated access.</strong> You must not scrape or copy the questions from the web app, access it with bots, scripts or other automated tools, or use several accounts to get around the daily limits.</li>
  <li><strong>Limits and suspension.</strong> We may limit or suspend an account that breaks these rules.</li>
</ul>

<h3 id="web-purchase">Buying Premium on the website</h3>
<p>Section 5 is about Premium bought in the Android app through Google Play. The points below apply if you buy Premium on the website, in the web app.</p>
<ul>
  <li><strong>Who sells it.</strong> Premium bought on the website is sold through Paddle, our reseller and the merchant of record for these purchases: Paddle.com Market Limited, or the Paddle company named in Paddle’s buyer terms for where you buy. Paddle runs the checkout, takes the payment, handles sales tax and sends your receipt. <a href="{PADDLE_BUYER_TERMS}" rel="noopener">Paddle’s Buyer Terms</a> apply to the purchase; these Terms cover the Premium access we provide. We never receive your full card number, and we don’t store your payment details.</li>
  <li><strong>Price.</strong> Premium costs {PRICE}, tax included, charged in Australian dollars (your bank may convert it). It is a one-time payment: there are no subscriptions or renewals.</li>
  <li><strong>Your account.</strong> You must be signed in to buy. Premium belongs to the account you were signed in to when you bought it and can’t be moved to another account. An account that already has Premium can’t buy it again.</li>
  <li><strong>What it unlocks.</strong> Premium is a lifetime purchase: it unlocks the web app’s Premium features on that account for as long as we provide the web app. These are higher daily limits, including more than one mock test a day (the fair-use limits above still apply), and the accuracy trend and weak areas. Premium bought on the website does not unlock Premium in the Android app yet.</li>
  <li><strong>When it arrives.</strong> Premium is added to your account after Paddle confirms the payment and our server has checked it with Paddle, usually within about 10 minutes. If it doesn’t appear, email {MAIL}.</li>
  <li><strong>Refunds.</strong> Refunds for purchases on the website follow <a href="{PADDLE_REFUNDS}" rel="noopener">Paddle’s Refund Policy</a> and your rights under the Australian Consumer Law. Ask Paddle for a refund at <a href="{PADDLE_NET}" rel="noopener">paddle.net</a> or through the link in Paddle’s receipt email; we can’t refund a website purchase ourselves. A full refund or a chargeback removes Premium from your account.</li>
  <li><strong>EU, EEA and UK consumers.</strong> If you are a consumer in the European Union, the wider EEA or the UK, Paddle’s Buyer Terms and Refund Policy let you withdraw from the purchase within 14 days for a full refund, unless you started using Premium within those 14 days after agreeing, during the purchase, that it could be made available straight away.</li>
  <li><strong>Your rights.</strong> Nothing in these Terms excludes, restricts or modifies the consumer guarantees you have under the Australian Consumer Law. Nothing in these Terms affects your statutory rights.</li>
</ul>
</div></div>"""
    return Page(
        path="terms.html",
        lastmod=TERMS_DATE,
        title="Terms of Service | Learners Test Australia",
        description=("Terms of service for the Learners Test Australia app: independence disclaimer, eligibility, Premium "
                     "billing, acceptable use, liability and NSW governing law."),
        body=body,
        crumbs=crumbs,
        priority="0.3",
        changefreq="yearly",
        llms_note=("The app's terms of service (same text as in the app, plus a section on the web study app, including "
                   "Premium bought on the website through Paddle: A$5.99 once, refunds through Paddle), governed by New "
                   "South Wales law."),
    )


# ── Account deletion (Google Play requirement) ────────────────────────────────────────────────
def account_deletion() -> Page:
    crumbs = [("Home", ""), ("Delete your account", "account-deletion.html")]
    body = page_head(
        "Delete your Learners Test Australia account and data",
        None,
        crumbs,
        meta_html=updated_line(DELETION_DATE, DELETION_DATE_H),
    ) + f"""
<div class="content"><div class="container prose">
<div class="callout">
  <p><strong>App:</strong> {APP_NAME} (Android, package {PACKAGE})<br>
  <strong>Developer:</strong> {DEVELOPER}<br>
  <strong>Contact:</strong> {MAIL}</p>
</div>

<p>You can delete your {SITE_NAME} account and the data linked to it at any time, either in the app or by email.
Uninstalling the app does not delete your account.</p>

<h2 id="in-the-app">Option 1: delete your account in the app</h2>
<ol>
  <li>Open {SITE_NAME} and sign in to the account you want to delete.</li>
  <li>Tap the <strong>Settings</strong> (gear) icon at the top of the Today, Practice, Tests or Progress tab.</li>
  <li>Scroll to <strong>Account</strong> and tap <strong>Delete account</strong> (“Removes your account and all saved progress”).</li>
  <li>Read the message and tap <strong>Delete</strong> to confirm. This can't be undone.</li>
  <li>If you haven't signed in recently, the app deletes your progress first and then asks you to sign in again.
  Sign in and repeat this step to finish deleting the account itself.</li>
</ol>
<p>When it's done, the app shows “Your account has been deleted.”</p>

<h2 id="by-email">Option 2: ask us by email</h2>
<p>If you can't use the app (for example, you no longer have the phone), email {MAIL} from the email address of your
account, with the subject <strong>“Delete my account”</strong>. We may reply to that address to confirm the request
before deleting. We aim to reply within 5 business days.</p>
<p>You can also email us if you want particular data deleted without deleting your whole account.</p>

<h2 id="what-is-deleted">What is deleted</h2>
<ul>
  <li>Your account (your sign-in).</li>
  <li>Your profile: your name and email address.</li>
  <li>Your progress in every state: answers, completed practice sessions and mock tests, and saved questions.</li>
  <li>Your email preferences.</li>
  <li>Your Premium record, if you have one: our purchase-checking service deletes it about a day after your
  account is deleted (see the <a href="@/privacy-policy.html#purchase-checks">privacy policy</a>).</li>
</ul>
<p>Your cloud progress, profile and sign-in are deleted straight away. Google then removes them from its backup
systems, which Google says can take up to 180 days.</p>

<h2 id="what-is-kept">What is kept</h2>
<ul>
  <li><strong>Premium purchases.</strong> Premium belongs to the learner account that bought it, so after you delete
  that account it can't be moved to a new account automatically; email us if you need help. Google Play keeps its own
  record of the purchase under its own policies, including the one-way hash of your user ID that the app added to it.
  Our purchase-checking service keeps its purchase records (your user ID, each purchase token, the product, the
  purchase’s status and when it was checked) for up to 6 years, to meet our legal and accounting obligations, and
  Google Cloud keeps its request logs for a limited time.
  If you bought Premium on the website, Paddle keeps its own record of the purchase under its own privacy notice, and
  our purchase-checking service keeps its purchase record (your user ID, the product, the price, Paddle’s transaction
  ID and the payment’s status, including any refund) for up to 6 years, also after your account is deleted; your
  Premium record is deleted as described above (see <a href="@/privacy-policy.html#web-app-purchases">Buying Premium
  on the website</a>).
  We never receive your full card number, and we don’t store your payment details. Deleting your account does not
  refund a purchase, except where required by law.</li>
  <li><strong>Usage statistics and crash reports.</strong> If you allowed “Help improve the app”, these are not
  linked to your account, so deleting it does not remove them. Firebase deletes crash reports after 90 days.</li>
  <li><strong>Settings stored only on your phone.</strong> Your test date and reminder settings stay on your device.
  They are removed when you uninstall the app or clear its storage in Android settings.</li>
  <li><strong>Web app records.</strong> If you used the web study app, its question service is not told when your
  account is deleted. You can delete its record of which questions it gave you, and your mock exams, at any time in
  the web app (Account → Delete what our server keeps) or by email; daily counts stay until they expire, and a beta
  invite-list entry is removed when you email us. Otherwise its record of which questions it gave you is deleted once
  your account has gone a year without new questions and 35 days without getting any questions or mock exams; daily
  counts are deleted after about 35 days and mock exams after about 90 days. Progress, saved questions and settings
  the web app stores in your browser stay on that device until you delete them in the web app (Progress → Delete
  progress on this device) or clear this site’s data. See the <a href="@/privacy-policy.html#web-app">privacy
  policy</a>.</li>
</ul>
<p>More detail is in the <a href="@/privacy-policy.html#data-protection-and-retention">privacy policy</a>.</p>
</div></div>"""
    return Page(
        path="account-deletion.html",
        lastmod=DELETION_DATE,
        title="Delete Your Account and Data | Learners Test Australia",
        description=("How to delete your Learners Test Australia account and data: in the app via Settings, Delete account, "
                     "or by email. What is deleted and what is kept."),
        body=body,
        crumbs=crumbs,
        priority="0.5",
        changefreq="yearly",
        llms=True,
        llms_title="Delete your account",
        llms_note="Steps to delete the account in the app or by email, what is deleted and what is kept.",
    )
