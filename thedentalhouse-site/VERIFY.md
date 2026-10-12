# To verify before going live

Everything marked **VERIFY** on the site (shown as a dashed yellow tag, `<mark class="verify">`)
or as `[VERIFY]` in an HTML comment is listed here. Search the HTML files for `verify` to find each one.

## Practice details
- [ ] **Phone number.** The site uses **01909 472477** (from the brief). Stephanie's email signature shows **01909 470597**. Confirm which is the main patient line.
- [ ] **Payment methods.** The site says "cash or card", changed from cheque. Confirm. (fees.html, new-patients.html)
- [ ] **Website address.** The site assumes `https://www.thedentalhouse.co.uk` (canonical links, sitemap, social tags). Confirm www vs non-www, and that HTTPS is set up on the hosting.
- [ ] **Map position.** The latitude/longitude in the structured data (every page's `<head>`) are approximate. Drop a pin in Google Maps and update them.
- [ ] **CQC rating.** Add the official CQC rating widget in the footer (placeholder in `tools/parts.py` / every page footer). Registered providers with a rating must display it on their website.
- [ ] **NHS.** new-patients.html FAQ says the practice is private only. Confirm there's no NHS contract.
- [ ] **New patients.** The FAQ says you're taking new patients. Confirm.
- [ ] **Children's plans.** The FAQ mentions care plan options for children. Confirm.

## Team (theteam.html)
- [ ] **GDC No. 80637** is listed for both **Tina Welsh** and **Dr Robert Hardy**. One is wrong. Check both on https://olr.gdc-uk.org/SearchRegister. (Dentists registered around 2002 had numbers in the 80,000s, so Dr Hardy's is more likely correct.)
- [ ] **Elizabeth Every.** Registered 09/01/1986, but her listed qualifications are dated 1995 and 2002. Confirm the registration date.
- [ ] **Dr Gregory Jones.** "Invisalign Orthodontics 2000". Invisalign arrived in the UK around 2001. Confirm the year.
- [ ] Make sure the wording for Dr Jones says "special interest", not "specialist", unless he is on the GDC specialist list.

## Care plans (careplans.html)
- [ ] **Monthly prices** for Plan A and Plan B (`£[VERIFY]/month`).
- [ ] **What differs between Plan A and Plan B** (examinations and hygiene visits per year).
- [ ] **"Free antibiotics dispensed at the practice".** Consider removing it.

## Treatments (treatments.html)
- [ ] **Whitening.** Confirm the system used (home trays are assumed).
- [ ] Have a clinician read through all treatment copy before launch.

## Reviews (index.html)
- [ ] Paste **real, verified** reviews from Working Feedback into the three review cards (with permission). Delete any card you don't fill.
- [ ] Confirm the "5/5 verified reviews" claim in the trust strip matches the current Working Feedback score.

## Third-party scripts (every page's `<head>`)
- [ ] **Cookiebot.** Compare the tag with the old site and keep any extra attributes it had. `data-blockingmode="auto"` is set. It may hold back the Google Map until visitors accept cookies.
- [ ] **Working Feedback.** Compare the script tag with the old site.
- [ ] **Cookie declaration** on cookie-policy.html uses Cookiebot's `cd.js`. Check it shows your cookie list.

## Policies
- [ ] **privacy-policy.html.** Paste the full wording from the old site. (This build environment couldn't reach the live site.)
- [ ] **cookie-policy.html.** Add any extra wording from the old site.

## Deployment
- [ ] Upload the **contents** of `thedentalhouse-site/` into `public_html` (or your web root).
- [ ] The old `/GDPR/` folder is **not** in this package. Leave it on the server, because the site links to it.
- [ ] To make the custom 404 page work on Apache hosting, add this line to your existing `.htaccess` (don't replace the file):
      `ErrorDocument 404 /404.html`
- [ ] Old pages that no longer exist (if any) can be redirected in `.htaccess`, e.g. `Redirect 301 /oldpage.html /treatments.html`.
- [ ] Submit `sitemap.xml` in Google Search Console.
- [ ] Contact form: the default opens the visitor's email app. For a better experience set up Formspree (instructions in a comment in contact.html).
