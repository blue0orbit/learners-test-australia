"""Privacy policy, cookie policy, terms of service and account deletion pages.

The privacy policy and terms mirror the in-app text in app/src/main/res/values/strings.xml
(privacy_* and tos_* strings, last updated 30 September 2026). Keep them word-for-word in sync
with the app: only headings and HTML structure are added here.
"""
from sitelib import (
    APP_NAME, BASE, DATE, DATE_H, DEVELOPER, EMAIL, PACKAGE, SITE_NAME, SRC, Page, page_head, updated_line,
)

MAIL = f'<a href="mailto:{EMAIL}">{EMAIL}</a>'


def legal_intro(kind: str, in_app_path: str) -> str:
    return (
        f'<div class="callout"><p><strong>App:</strong> {APP_NAME} (Android) · <strong>Developer:</strong> {DEVELOPER} · '
        f"<strong>Contact:</strong> {MAIL}</p>"
        f"<p>This is the same {kind} shown in the app ({in_app_path}).</p></div>"
    )


# ── Privacy policy ────────────────────────────────────────────────────────────────────────────
def privacy() -> Page:
    crumbs = [("Home", ""), ("Privacy policy", "privacy-policy.html")]
    body = page_head(
        "Privacy Policy",
        f"How the {SITE_NAME} app handles your information, and a note on this website.",
        crumbs,
        meta_html=f'<p class="meta">Last updated: <time datetime="{DATE}">{DATE_H}</time></p>',
    ) + f"""
<div class="content"><div class="container prose">
{legal_intro("privacy policy", "Settings → Privacy policy")}

<h2 id="overview">Overview</h2>
<p>Learners Test Australia is an independent study app that helps you prepare for an Australian learner driver knowledge test. It is not affiliated with any government, transport or licensing agency.</p>
<p>This policy explains what the app collects, why, and the choices you have. Questions: {MAIL}.</p>

<h2 id="information-we-collect">Information we collect</h2>
<p><strong>Account:</strong> when you sign in with Google, Facebook or email, we receive your name and email address.</p>
<p><strong>Study data:</strong> your answers, completed practice sessions and mock tests, saved questions and the state you study for. This is stored on your device and in your account so it follows you to a new phone. Your test date and reminder settings stay on your device.</p>
<p><strong>If you allow “Help improve the app”:</strong> anonymous usage statistics and crash reports (device model, Android version, app version, screens used).</p>
<p><strong>Ads:</strong> the free version shows ads. Ad providers may use your device’s advertising ID. Where the law requires it (for example in the EEA and UK), Google asks for your consent first, and you can change it in Settings.</p>

<h2 id="how-we-use-your-data">How we use your data</h2>
<p>We use your data to:</p>
<ul>
  <li>Create your account and keep your progress in sync</li>
  <li>Build your daily plan, reviews and pass-chance estimate</li>
  <li>Send study reminders and announcements, if you turn them on</li>
  <li>Send tips and offers by email, only if you opt in (unsubscribe any time)</li>
  <li>Show ads in the free version</li>
  <li>Fix crashes and improve the app, if you allow it</li>
</ul>
<p>We never sell your personal information.</p>

<h2 id="third-party-services">Third-party services</h2>
<p>The app uses these services, each with its own privacy policy:</p>
<ul>
  <li>Google Firebase — sign-in, cloud storage of progress, analytics, crash reports, push messages and remote settings</li>
  <li>Google AdMob — banner ads (free version)</li>
  <li>Unity Ads — optional rewarded video ads (free version)</li>
  <li>Google User Messaging Platform — ad consent where required</li>
  <li>Google Play Billing — the Premium purchase (we never see your payment details)</li>
  <li>Facebook Login — optional sign-in</li>
</ul>

<h2 id="data-protection-and-retention">Data protection &amp; retention</h2>
<p>Your data is shared only with the providers above, and only as needed to run the app. Data is sent over encrypted connections, and your cloud data can only be read by your own account.</p>
<p>We keep your data while your account exists. Delete your account in Settings and your cloud progress and profile are deleted straight away; copies in the providers’ backups are removed within 30 days. You can also email us to ask for deletion.</p>

<h2 id="your-rights">Your rights</h2>
<p><strong>Australia:</strong> we handle personal information under the Australian Privacy Principles (Privacy Act 1988). You can ask to access or correct your information, or complain, by emailing us. If you are not satisfied with our response you can contact the Office of the Australian Information Commissioner (<a href="https://www.oaic.gov.au/" rel="noopener">oaic.gov.au</a>).</p>
<p><strong>EEA and UK:</strong> you have rights to access, correct, delete, restrict and port your data and to object to processing. We rely on your consent for analytics, marketing email and personalised ads, and on our contract with you to run your account.</p>
<p><strong>Children:</strong> the app is for people preparing for a learner licence, usually 15 and over. It is not directed at children under 13, and we do not knowingly collect their data.</p>
<p><strong>Changes:</strong> if we change this policy in an important way, we will tell you in the app first.</p>

<h2 id="contact">Contact</h2>
<p>Privacy questions, data requests or complaints:</p>
<p>Email: {MAIL}</p>
<p>We aim to reply within 5 business days.</p>

<h2 id="website">This website</h2>
<p>This section is about the website you are reading now (learnertest.com), not the app.</p>
<ul>
  <li><strong>No cookies.</strong> The website sets no cookies and stores nothing in your browser (no local storage or similar).</li>
  <li><strong>No analytics or trackers.</strong> There are no analytics, advertising, tracking pixels or social media widgets.</li>
  <li><strong>Nothing loaded from third parties.</strong> Fonts, images, styles and the one small script (it opens and closes the menu on small screens) are all served from this website itself.</li>
  <li><strong>Hosting.</strong> The site is hosted on GitHub Pages. GitHub says it logs the IP address of visitors to GitHub Pages sites for security purposes (see <a href="{SRC['gh_pages_data']}" rel="noopener">About GitHub Pages</a>). We don't use those logs, and the site has no analytics of its own.</li>
  <li><strong>Email.</strong> If you email us, we use your message and email address to reply to you.</li>
</ul>
<p>See also the <a href="@/cookies.html">cookie policy</a> and how to <a href="@/account-deletion.html">delete your account</a>.</p>
</div></div>"""
    return Page(
        path="privacy-policy.html",
        title="Privacy Policy | Learners Test Australia",
        description=("Privacy policy for the Learners Test Australia app: what we collect, why, third-party services, "
                     "retention, your rights, and why this website uses no cookies."),
        body=body,
        crumbs=crumbs,
        priority="0.4",
        changefreq="yearly",
        llms=True,
        llms_title="Privacy policy",
        llms_note="The app's privacy policy (same text as in the app) plus a section on this website: no cookies, analytics or third-party requests.",
    )


# ── Cookie policy ─────────────────────────────────────────────────────────────────────────────
def cookies() -> Page:
    crumbs = [("Home", ""), ("Cookie policy", "cookies.html")]
    body = page_head(
        "Cookie policy",
        "This website sets no cookies. Here is what the app uses instead, and how to control it.",
        crumbs,
    ) + f"""
<div class="content"><div class="container prose">
<div class="answer-box"><p class="answer-label">In short</p>
<p>The {SITE_NAME} website sets no cookies, stores nothing in your browser and loads nothing from third parties, so
there is no cookie banner to accept. The app works differently from a website: it keeps data on your phone, uses
Google Firebase for your account and progress, and in the free version lets ad providers use your advertising ID,
subject to consent where the law requires it.</p></div>

<h2>Does this website use cookies?</h2>
<p>No. This website sets no cookies and uses no local storage, analytics, advertising or tracking of any kind. Every
file (pages, fonts, images, styles and the small menu script) comes from this site. The site is hosted on GitHub Pages;
see the <a href="@/privacy-policy.html#website">privacy policy</a> for what GitHub logs.</p>

<h2>What does the app use instead of cookies?</h2>
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
  <li><strong>Analytics and crash reports:</strong> anonymous usage statistics and crash reports, only if you allow “Help improve the app”. You can switch this on or off in the app's Settings, under Privacy.</li>
  <li><strong>Push messages:</strong> Firebase Cloud Messaging gives your phone a push token so the app can receive announcements. You can turn notifications off in Android settings at any time.</li>
  <li><strong>Remote settings:</strong> lets us adjust some app settings without an update.</li>
</ul>

<h3>Advertising identifiers (free version)</h3>
<p>The free version shows banner ads from Google AdMob and optional rewarded video ads from Unity Ads. These ad
providers may use your device's advertising ID. Where the law requires it (for example in the EEA and UK), Google's
User Messaging Platform asks for your consent first. Premium removes ads.</p>
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
<tr><th scope="row">Cookies</th><td>This website</td><td>None used</td><td>Nothing to set</td></tr>
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
        title="Cookie Policy | Learners Test Australia",
        description=("This website sets no cookies. Learn what the Learners Test Australia app uses instead (device storage, "
                     "Firebase, advertising ID) and how to control it."),
        body=body,
        crumbs=crumbs,
        priority="0.3",
        changefreq="yearly",
        llms_note="The website sets no cookies; what the app uses instead and how to change ad choices or reset the advertising ID.",
    )


# ── Terms of service ──────────────────────────────────────────────────────────────────────────
def terms() -> Page:
    crumbs = [("Home", ""), ("Terms of service", "terms.html")]
    body = page_head(
        "Terms of Service",
        f"The terms for using the {SITE_NAME} app.",
        crumbs,
    ) + f"""
<div class="content"><div class="container prose">
{legal_intro("terms of service", "Settings → Terms")}

<h2 id="acceptance">1. Acceptance of Terms</h2>
<p>By downloading, installing, or using Learners Test Australia ("the App"), you agree to be bound by these Terms of Service ("Terms"). If you do not agree to these Terms, please do not use the App. These Terms form a legally binding agreement between you and the developer of Learners Test Australia. Your continued use of the App after any changes to these Terms constitutes acceptance of the updated Terms.</p>

<h2 id="disclaimer">2. App Disclaimer</h2>
<p>Learners Test Australia is an independent study aid designed to help users prepare for an Australian learner driver knowledge test. It is NOT affiliated with, endorsed by, sponsored by, or connected in any way to any Australian state or territory government, transport department or licensing agency.</p>
<p>All practice questions and educational content within the App are for study and preparation purposes only. Completing this App, achieving high scores, or unlocking any in-app achievement does NOT guarantee passing your official learner test. The official test is run by your state or territory's licensing authority. Always refer to its current official handbook and website for authoritative information.</p>

<h2 id="eligibility">3. Eligibility</h2>
<p>The App is intended for users who are preparing for an Australian learner driver knowledge test. You must be at least 16 years of age to use the App and create an account. If you are under 18, you confirm that a parent or legal guardian has consented to your use of the App. By using the App, you represent and warrant that you meet these eligibility requirements.</p>

<h2 id="accounts">4. User Accounts &amp; Responsibilities</h2>
<p>You are responsible for maintaining the confidentiality of your account credentials and for all activity that occurs under your account. You agree to provide accurate and complete information when registering and to keep this information up to date. You may not share your account with others, create multiple accounts for abusive purposes, or use another person's account without permission.</p>
<p>You are responsible for safeguarding your password and agree to notify us immediately at {MAIL} if you suspect any unauthorised access to your account. We are not liable for any loss resulting from unauthorised use of your account.</p>

<h2 id="billing">5. Premium &amp; Billing</h2>
<p>Some features are available through a one-time purchase (“Premium”). Premium is a lifetime purchase: there are no subscriptions or renewals.</p>
<p>Purchases are processed by Google Play under its terms of sale. We never see or store your payment details.</p>
<p>Refunds follow Google Play’s refund policy and your rights under the Australian Consumer Law.</p>
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
<p>All content in the App — including practice questions, explanations, illustrations, icons, text and software — is owned by or licensed to the developer and protected by intellectual property laws. Questions are written for the App and checked against official handbooks; official material is referenced, not reproduced.</p>
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
<p>A Premium purchase belongs to the Google account that bought it, not to your Learners Test Australia account, so it stays available if you sign in again on the same Google account.</p>

<h2 id="changes">11. Changes to These Terms</h2>
<p>We may update these Terms from time to time to reflect changes to the App, our practices, or applicable law. When we make material changes, we will update the "Last updated" date shown on this page and may notify you within the App.</p>
<p>Your continued use of the App after any changes constitutes acceptance of the updated Terms. If you do not agree to the updated Terms, you should stop using the App before the changes take effect.</p>

<h2 id="governing-law">12. Governing Law &amp; Contact</h2>
<p>These Terms are governed by and construed in accordance with the laws of New South Wales, Australia. Any disputes arising under these Terms shall be subject to the non-exclusive jurisdiction of the courts of New South Wales and the federal courts of Australia, without prejudice to any mandatory consumer protection rights you may have under the law of your country, including the Australian Consumer Law.</p>
<p>If you have any questions about these Terms, please contact us at:</p>
<p>Email: {MAIL}</p>
<p>We aim to respond to all enquiries within 5 business days.</p>
</div></div>"""
    return Page(
        path="terms.html",
        title="Terms of Service | Learners Test Australia",
        description=("Terms of service for the Learners Test Australia app: independence disclaimer, eligibility, Premium "
                     "billing, acceptable use, liability and NSW governing law."),
        body=body,
        crumbs=crumbs,
        priority="0.3",
        changefreq="yearly",
        llms_note="The app's terms of service (same text as in the app), governed by New South Wales law.",
    )


# ── Account deletion (Google Play requirement) ────────────────────────────────────────────────
def account_deletion() -> Page:
    crumbs = [("Home", ""), ("Delete your account", "account-deletion.html")]
    body = page_head(
        "Delete your Learners Test Australia account and data",
        None,
        crumbs,
        meta_html=updated_line(),
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
</ul>
<p>Your cloud progress and profile are deleted straight away. Copies in our service providers’ backups are removed
within 30 days.</p>

<h2 id="what-is-kept">What is kept</h2>
<ul>
  <li><strong>Premium purchases.</strong> A Premium purchase belongs to the Google account that bought it, and
  purchase records are kept by Google Play under its own policies, not by us. We never see or store your payment
  details. If you later sign in again with the same Google account, Premium is still available. Deleting your
  account does not refund a purchase, except where required by law.</li>
  <li><strong>Settings stored only on your phone.</strong> Your test date and reminder settings stay on your device.
  They are removed when you uninstall the app or clear its storage in Android settings.</li>
</ul>
<p>More detail is in the <a href="@/privacy-policy.html#data-protection-and-retention">privacy policy</a>.</p>
</div></div>"""
    return Page(
        path="account-deletion.html",
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
