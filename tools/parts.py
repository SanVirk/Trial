"""Shared pieces for The Dental House static site: icons, head, header, footer, helpers."""
from urllib.parse import quote
import json

SITE_URL = "https://www.thedentalhouse.co.uk"  # [VERIFY] www vs non-www, and that HTTPS is live
PHONE = "01909 472477"
PHONE_TEL = "+441909472477"
EMAIL = "enquiries@thedentalhouse.co.uk"
FACEBOOK = "https://www.facebook.com/profile.php?id=61586200125006"
ADDRESS_LINES = ["37 Carlton Road", "Worksop", "Nottinghamshire", "S80 1PD"]

HOURS = [
    ("mon", "Monday", "9.00am – 6.00pm", ("09:00", "18:00")),
    ("tue", "Tuesday", "8.30am – 5.00pm", ("08:30", "17:00")),
    ("wed", "Wednesday", "8.30am – 5.00pm", ("08:30", "17:00")),
    ("thu", "Thursday", "8.30am – 6.00pm", ("08:30", "18:00")),
    ("fri", "Friday", "8.30am – 1.00pm", ("08:30", "13:00")),
    ("sat", "Saturday", "Closed", None),
    ("sun", "Sunday", "Closed", None),
]

PDFS = {
    "privacy": "/GDPR/M 217T(E) Privacy Notice for Patients Ver 1 (3) (1).pdf",
    "privacy_children": "/GDPR/M 217TC(E) Privacy Notice for Children Ver 1 (2) (1).pdf",
    "complaints": "/GDPR/G 110C Patient Complaints Procedure Ver 6 (12) (1).pdf",
    "leaflet": "/GDPR/April 2025 M_217P_-_Patient_Leaflet_on_Personal_Information_Ver_6_0.pdf",
    "brochure": "/GDPR/The Dental House Practice Brochure [Feb 26].pdf",
    "fees": "/GDPR/Patients Private Fee Scale [March 2026].pdf",
}


def pdf(key):
    """Root-relative, URL-encoded href for an existing PDF (spaces, brackets and parentheses encoded)."""
    return quote(PDFS[key], safe="/")


def verify(text="VERIFY"):
    return f'<mark class="verify" title="To be confirmed before going live">{text}</mark>'


# ---------------------------------------------------------------- icons
# 24×24, 1.5 stroke, round caps — one consistent line family.
_ICON_PATHS = {
    "phone": '<path d="M5.5 3.5h3l1.5 4-2 1.5a11 11 0 0 0 7 7l1.5-2 4 1.5v3a2 2 0 0 1-2 2A16.5 16.5 0 0 1 3.5 5.5a2 2 0 0 1 2-2z"/>',
    "calendar": '<rect x="3.5" y="5" width="17" height="15.5" rx="2.5"/><path d="M3.5 10h17M8 3v4M16 3v4M8 14h2M14 14h2M8 17h2"/>',
    "tooth": '<path d="M7.2 3.5C5 3.5 3.7 5.3 3.7 7.7c0 2.2.8 3.6 1.4 5.3.6 1.7.8 3.4 1.2 5.2.3 1.6.8 2.8 1.9 2.8s1.4-1.3 1.7-2.8c.3-1.5.7-3.2 2.1-3.2s1.8 1.7 2.1 3.2c.3 1.5.6 2.8 1.7 2.8s1.6-1.2 1.9-2.8c.4-1.8.6-3.5 1.2-5.2.6-1.7 1.4-3.1 1.4-5.3 0-2.4-1.3-4.2-3.5-4.2-1.9 0-2.9 1-4.8 1s-2.9-1-4.8-1z"/>',
    "shield": '<path d="M12 3 4.5 6v5.5c0 4.6 3.2 8.2 7.5 9.5 4.3-1.3 7.5-4.9 7.5-9.5V6L12 3z"/><path d="m8.8 12 2.2 2.2 4.3-4.4"/>',
    "heart": '<path d="M12 20s-7.5-4.4-7.5-10A4.3 4.3 0 0 1 12 7.4 4.3 4.3 0 0 1 19.5 10c0 5.6-7.5 10-7.5 10z"/>',
    "family": '<circle cx="8" cy="7" r="2.5"/><circle cx="16.5" cy="8" r="2"/><path d="M3.5 20v-3.5A4.5 4.5 0 0 1 8 12a4.5 4.5 0 0 1 4.5 4.5V20M13 20v-3a3.5 3.5 0 0 1 7 0v3"/>',
    "plan": '<rect x="4.5" y="3.5" width="15" height="17" rx="2.5"/><path d="M8.5 8.5h7M8.5 12h7M8.5 15.5h4"/>',
    "star": '<path d="m12 3.5 2.6 5.3 5.9.9-4.3 4.1 1 5.8L12 16.9l-5.2 2.7 1-5.8-4.3-4.1 5.9-.9L12 3.5z"/>',
    "sparkle": '<path d="M12 3.5c.6 4 2.5 6 6.5 6.5-4 .6-5.9 2.5-6.5 6.5-.6-4-2.5-5.9-6.5-6.5 4-.5 5.9-2.5 6.5-6.5zM18.5 15.5c.3 1.6 1 2.3 2.5 2.5-1.5.3-2.2 1-2.5 2.5-.3-1.5-1-2.2-2.5-2.5 1.5-.2 2.2-.9 2.5-2.5z"/>',
    "clock": '<circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 2"/>',
    "pin": '<path d="M12 21s-6.5-6-6.5-11a6.5 6.5 0 0 1 13 0c0 5-6.5 11-6.5 11z"/><circle cx="12" cy="10" r="2.3"/>',
    "mail": '<rect x="3.5" y="5.5" width="17" height="13" rx="2.5"/><path d="m4 7 8 6 8-6"/>',
    "facebook": '<path d="M14.5 8.5h2.5V5h-2.5A3.5 3.5 0 0 0 11 8.5V11H8.5v3.5H11V21h3.5v-6.5H17l.5-3.5h-3V9a.5.5 0 0 1 .5-.5z"/>',
    "arrow": '<path d="M4.5 12h15M14 6.5l5.5 5.5-5.5 5.5"/>',
    "check": '<path d="m5 12.5 4.5 4.5L19 7.5"/>',
    "check-circle": '<circle cx="12" cy="12" r="8.5"/><path d="m8.3 12.3 2.6 2.6 4.8-5"/>',
    "plus": '<path d="M12 5v14M5 12h14"/>',
    "menu": '<path d="M4 8h16M4 16h16"/>',
    "close": '<path d="M6 6l12 12M18 6 6 18"/>',
    "alert": '<path d="M12 4 3 19.5h18L12 4z"/><path d="M12 10v4.5M12 17.3v.2"/>',
    "leaf": '<path d="M19.5 4.5C10 4.5 4.5 9 4.5 15.5c0 2 .9 3.5 2.4 4 5.6-1 10.6-6 12.6-15z"/><path d="M4.5 19.5c3-4 6.5-7 10-9"/>',
    "file": '<path d="M7 3.5h7l4.5 4.5v12.5H7a1.5 1.5 0 0 1-1.5-1.5V5A1.5 1.5 0 0 1 7 3.5z"/><path d="M13.5 3.5V8h5M9 12.5h6M9 16h4"/>',
    "card": '<rect x="3" y="6" width="18" height="12.5" rx="2.5"/><path d="M3 10h18M6.5 15h3.5"/>',
    "users": '<circle cx="9" cy="8" r="3"/><path d="M3.5 19.5v-1A4.5 4.5 0 0 1 8 14h2a4.5 4.5 0 0 1 4.5 4.5v1"/><path d="M15 5.3a3 3 0 0 1 0 5.4M17 14a4.5 4.5 0 0 1 3.5 4.4v1.1"/>',
    "hand": '<path d="M8 12.5V6a1.5 1.5 0 0 1 3 0v5M11 11V4.5a1.5 1.5 0 0 1 3 0V11M14 11V6a1.5 1.5 0 0 1 3 0v7.5a7 7 0 0 1-7 7h-.5a6 6 0 0 1-4.8-2.4L3.4 15a1.5 1.5 0 0 1 2.3-1.9L8 15.5"/>',
    "chat": '<path d="M20 12a7.5 7.5 0 0 1-11 6.6L4 20l1.4-4.4A7.5 7.5 0 1 1 20 12z"/><path d="M9 11h6M9 14h3.5"/>',
    "car": '<path d="M5 16.5V12l1.8-4.5A2 2 0 0 1 8.7 6h6.6a2 2 0 0 1 1.9 1.5L19 12v4.5"/><path d="M3.5 16.5h17v2H3.5zM5 12h14"/><circle cx="7.5" cy="14.3" r=".6"/><circle cx="16.5" cy="14.3" r=".6"/>',
    "access": '<circle cx="12" cy="4.8" r="1.8"/><path d="M5 9l7 1.5L19 9M12 10.5V15l-3 5.5M12 15l3 5.5"/>',
    "smile": '<circle cx="12" cy="12" r="8.5"/><path d="M8.5 14a4.5 4.5 0 0 0 7 0M9 9.5v.5M15 9.5v.5"/>',
    "crown": '<path d="M7 9.5c0-3 2-5 5-5s5 2 5 5v3H7v-3z"/><path d="M7 12.5h10l-1 3.5c-.4 1.7-1 4.5-2 4.5s-1.2-2.5-2-2.5-1 2.5-2 2.5-1.6-2.8-2-4.5l-1-3.5z"/>',
    "aligner": '<path d="M3.5 9.5c2-3 5-4.5 8.5-4.5s6.5 1.5 8.5 4.5c-1 2.5-2.5 4.5-4 5.5-1.2.8-2.5.4-3-.8-.4-.9-.8-1.2-1.5-1.2s-1.1.3-1.5 1.2c-.5 1.2-1.8 1.6-3 .8-1.5-1-3-3-4-5.5z"/><path d="M7 9.5h10"/>',
    "drop": '<path d="M12 3.5s-6 6.5-6 11a6 6 0 0 0 12 0c0-4.5-6-11-6-11z"/><path d="M9.5 15a2.5 2.5 0 0 0 2.5 2.5"/>',
    "brush": '<path d="M4 20l9-9M13 11l2.5-2.5 3 3L16 14l-3-3zM15.5 8.5l2-2a1.4 1.4 0 0 1 2 2l-2 2"/><path d="M5 17l2 2"/>',
    "mouthguard": '<path d="M4 10c0-3 3.6-5 8-5s8 2 8 5c0 3.5-2 7-4.5 7-1.3 0-2.2-1-3.5-1s-2.2 1-3.5 1C6 17 4 13.5 4 10z"/><path d="M7.5 10.5c1.4.7 2.9 1 4.5 1s3.1-.3 4.5-1"/>',
    "extract": '<path d="M8.2 9.5c-1.6 0-2.7 1.3-2.7 3.1 0 1.6.6 2.6 1 3.9.5 1.3.6 2.5.9 3.8.2 1.2.6 1.7 1.3 1.7s1-.9 1.2-2c.2-1.1.5-2.3 1.6-2.3s1.4 1.2 1.6 2.3c.2 1.1.5 2 1.2 2s1.1-.5 1.3-1.7c.3-1.3.4-2.5.9-3.8.4-1.3 1-2.3 1-3.9 0-1.8-1.1-3.1-2.7-3.1-1.4 0-2.1.7-3.5.7s-2.1-.7-3.5-.7z"/><path d="M12 6.5V2.5M9.5 4.5 12 2l2.5 2.5"/>',
    "denture": '<path d="M3.5 8.5c1.5-2.5 4.8-4 8.5-4s7 1.5 8.5 4"/><path d="M5 8.2v3.3a2 2 0 0 0 4 0V7.2M9 7.2v4.3a2 2 0 0 0 3 0 2 2 0 0 0 3 0V7.2M15 7.2v4.3a2 2 0 0 0 4 0V8.2"/><path d="M4.5 19.5c1.5 0 2.5-1 7.5-1s6 1 7.5 1"/>',
    "home": '<path d="M4 20.5V10l8-6 8 6v10.5"/><path d="M9.5 20.5v-5a2.5 2.5 0 0 1 5 0v5"/>',
    "external": '<path d="M13.5 4.5h6v6M19.5 4.5 11 13M17 13.5v5a1.5 1.5 0 0 1-1.5 1.5h-10A1.5 1.5 0 0 1 4 18.5v-10A1.5 1.5 0 0 1 5.5 7h5"/>',
    "download": '<path d="M12 4v11M7.5 10.5 12 15l4.5-4.5M5 19.5h14"/>',
    "info": '<circle cx="12" cy="12" r="8.5"/><path d="M12 11v5.5M12 7.8v.2"/>',
    "pause": '<circle cx="12" cy="12" r="8.5"/><path d="M10 9v6M14 9v6"/>',
    "compass": '<circle cx="12" cy="12" r="8.5"/><path d="m15.5 8.5-2 5-5 2 2-5 5-2z"/>',
}


def icon(name, cls="", label=None):
    aria = f'role="img" aria-label="{label}"' if label else 'aria-hidden="true" focusable="false"'
    classes = ("icon " + cls).strip()
    return f'<svg class="{classes}" viewBox="0 0 24 24" {aria}>{_ICON_PATHS[name]}</svg>'


def icon_filled_star():
    return f'<svg class="icon" viewBox="0 0 24 24" aria-hidden="true" focusable="false">{_ICON_PATHS["star"]}</svg>'


LOGO_MARK = (
    '<svg class="logo-mark" viewBox="0 0 32 32" aria-hidden="true" focusable="false">'
    '<path d="M5 28V14.5L16 5.5l5.6 4.6V6.2h3.4v6.7L27 14.5V28" fill="none" stroke="currentColor" '
    'stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>'
    '<path class="roof" d="M12.6 28v-4.6a3.4 3.4 0 0 1 6.8 0V28" fill="none" stroke-width="1.5" stroke-linecap="round"/>'
    '</svg>'
)


def logo(base):
    return (f'<a class="logo" href="{base}index.html" aria-label="The Dental House, home">{LOGO_MARK}'
            '<span class="logo-word">the dental <em>house</em></span></a>')


def media(base, name, alt, w, h, cls="", eager=False, variant=""):
    """Image with a CSS gradient placeholder behind it. If the file is missing the <img> hides itself
    and the gradient (labelled with the expected filename) shows instead."""
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    v = f" media--{variant}" if variant else ""
    return (f'<figure class="media{v} {cls}" style="--ar:{w}/{h}" data-ph="{name}">'
            f'<img src="{base}assets/img/{name}" alt="{alt}" width="{w}" height="{h}" {load} decoding="async" '
            f'onerror="this.hidden=true"></figure>')


# ---------------------------------------------------------------- nav
NAV_MAIN = [
    ("about.html", "About"),
    ("treatments.html", "Treatments"),
    ("careplans.html", "Care plans"),
    ("theteam.html", "Our team"),
    ("new-patients.html", "New patients"),
    ("contact.html", "Contact"),
]
NAV_ALL = [
    ("index.html", "Home"),
    ("about.html", "About the practice"),
    ("treatments.html", "Treatments"),
    ("careplans.html", "Dental care plans"),
    ("theteam.html", "Our team"),
    ("new-patients.html", "New patients"),
    ("nervous-patients.html", "Nervous patients"),
    ("fees.html", "Fees"),
    ("emergency.html", "Emergencies"),
    ("patient-info.html", "Patient information"),
    ("contact.html", "Contact &amp; find us"),
]


def _cur(page, href):
    return ' aria-current="page"' if page == href else ""


def header(base, page):
    links = "".join(
        f'<li><a class="nav-link" href="{base}{h}"{_cur(page, h)}>{t}</a></li>' for h, t in NAV_MAIN)
    menu_links = "".join(
        f'<li><a href="{base}{h}"{_cur(page, h)}>{t}{icon("arrow")}</a></li>' for h, t in NAV_ALL)
    return f'''<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header">
  <div class="container">
    {logo(base)}
    <nav class="primary-nav" aria-label="Main">
      <ul>{links}</ul>
    </nav>
    <div class="header-cta">
      <a class="btn btn--outline btn--sm" href="tel:{PHONE_TEL}">{icon("phone")}<span>Call {PHONE}</span></a>
      <a class="btn btn--sm" href="{base}contact.html#book">Book an appointment</a>
    </div>
    <button class="menu-toggle" type="button" data-menu-open aria-expanded="false" aria-controls="mobile-menu">
      {icon("menu")}<span>Menu</span>
    </button>
  </div>
</header>
<div class="mobile-menu" id="mobile-menu" role="dialog" aria-modal="true" aria-label="Site menu" aria-hidden="true" hidden>
  <div class="mobile-menu__top">
    {logo(base).replace('class="logo"', 'class="logo" tabindex="-1"')}
    <button class="menu-toggle" type="button" data-menu-close>{icon("close")}<span>Close</span></button>
  </div>
  <nav aria-label="Mobile">
    <ul>{menu_links}</ul>
  </nav>
  <div class="mobile-menu__foot">
    <a class="btn btn--brass" href="{base}contact.html#book">{icon("calendar")}Book an appointment</a>
    <a class="btn btn--light" href="tel:{PHONE_TEL}">{icon("phone")}Call {PHONE}</a>
    <p>37 Carlton Road, Worksop S80 1PD</p>
  </div>
</div>'''


def hours_table(cls="hours"):
    rows = "".join(
        f'<tr data-day="{d}"><th scope="row">{name}</th><td{" class=\"closed\"" if not t else ""}>{label}</td></tr>'
        for d, name, label, t in HOURS)
    return f'<table class="{cls}"><caption class="visually-hidden">Opening hours</caption><tbody>{rows}</tbody></table>'


def footer(base):
    return f'''<footer class="site-footer on-dark">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        {logo(base)}
        <p>A friendly, independent family dental practice in the heart of Worksop.</p>
        <div class="btn-row">
          <a class="btn btn--brass btn--sm" href="{base}contact.html#book">Book an appointment</a>
        </div>
      </div>
      <div>
        <h2>Visit &amp; contact</h2>
        <ul class="footer-contact">
          <li>{icon("pin")}<address>{"<br>".join(ADDRESS_LINES)}</address></li>
          <li>{icon("phone")}<a href="tel:{PHONE_TEL}">{PHONE}</a></li>
          <li>{icon("mail")}<a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li>{icon("facebook")}<a href="{FACEBOOK}" rel="noopener" target="_blank">Facebook<span class="visually-hidden"> (opens in a new tab)</span></a></li>
        </ul>
      </div>
      <div>
        <h2>Opening hours</h2>
        {hours_table()}
      </div>
      <div>
        <h2>Quick links</h2>
        <ul>
          <li><a href="{base}treatments.html">Treatments</a></li>
          <li><a href="{base}careplans.html">Dental care plans</a></li>
          <li><a href="{base}new-patients.html">New patients</a></li>
          <li><a href="{base}nervous-patients.html">Nervous patients</a></li>
          <li><a href="{base}emergency.html">Emergencies</a></li>
          <li><a href="{base}fees.html">Fees</a></li>
          <li><a href="{base}patient-info.html">Patient information</a></li>
          <li><a href="{base}theteam.html">Our team</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-reg">
      <div class="stack">
        <p>All our clinicians are registered with the General Dental Council (<a href="https://www.gdc-uk.org" rel="noopener" target="_blank">gdc-uk.org</a>).</p>
        <p class="cqc-slot">{icon("shield")}<span>Care Quality Commission rating — official CQC widget goes here {verify()}</span></p>
        <p>&copy; The Dental House <span data-year>2026</span></p>
      </div>
      <nav class="footer-legal" aria-label="Legal">
        <a href="{base}privacy-policy.html">Privacy policy</a>
        <a href="{base}cookie-policy.html">Cookie policy</a>
        <a href="javascript:Cookiebot.renew()">Cookie settings</a>
        <a href="{pdf("complaints")}">Complaints procedure</a>
      </nav>
    </div>
  </div>
</footer>
<div class="action-bar" aria-label="Quick actions">
  <a class="btn btn--outline" href="tel:{PHONE_TEL}">{icon("phone")}Call</a>
  <a class="btn" href="{base}contact.html#book">{icon("calendar")}Book</a>
</div>'''


def jsonld():
    data = {
        "@context": "https://schema.org",
        "@type": "Dentist",
        "@id": SITE_URL + "/#practice",
        "name": "The Dental House",
        "url": SITE_URL + "/",
        "image": SITE_URL + "/assets/img/og-image.jpg",
        "logo": SITE_URL + "/assets/img/logo.svg",
        "telephone": "+44 1909 472477",
        "email": EMAIL,
        "priceRange": "££",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "37 Carlton Road",
            "addressLocality": "Worksop",
            "addressRegion": "Nottinghamshire",
            "postalCode": "S80 1PD",
            "addressCountry": "GB",
        },
        # [VERIFY] approximate — confirm by dropping a pin on Google Maps
        "geo": {"@type": "GeoCoordinates", "latitude": 53.3088, "longitude": -1.1222},
        "openingHoursSpecification": [
            {"@type": "OpeningHoursSpecification", "dayOfWeek": name, "opens": t[0], "closes": t[1]}
            for d, name, label, t in HOURS if t
        ],
        "sameAs": [FACEBOOK],
        "isAcceptingNewPatients": True,
    }
    return json.dumps(data, indent=2, ensure_ascii=False)


def head(base, title, description, path, extra=""):
    canonical = SITE_URL + "/" + ("" if path == "index.html" else path)
    return f'''<!doctype html>
<html lang="en-GB" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<!-- Cookiebot consent banner. [VERIFY] compare with the tag on the old site and keep any extra attributes it had. -->
<script id="Cookiebot" src="https://consent.cookiebot.com/uc.js" data-cbid="a1c3f3a2-a95b-4b3c-bea5-ab9f977018f7" data-blockingmode="auto" type="text/javascript"></script>
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
<meta name="theme-color" content="#1E4D4F">
<meta property="og:type" content="website">
<meta property="og:site_name" content="The Dental House">
<meta property="og:locale" content="en_GB">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE_URL}/assets/img/og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{base}assets/img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300..600;1,9..144,300..500&amp;family=Manrope:wght@400..700&amp;display=swap">
<link rel="stylesheet" href="{base}assets/css/styles.css">
<script>document.documentElement.className=document.documentElement.className.replace('no-js','js');</script>
<script type="application/ld+json">
{jsonld()}
</script>
<!-- Working Feedback reviews tab. [VERIFY] compare with the tag on the old site. -->
<script type="text/javascript" src="https://features.myworkingfeedback.com/review-tab/8927166" async></script>
<script src="{base}assets/js/main.js" defer></script>
{extra}</head>'''


def page(base, path, title, description, body, body_class="", extra_head=""):
    return f'''{head(base, title, description, path, extra_head)}
<body class="{body_class}">
{header(base, path)}
<main id="main" tabindex="-1">
{body}
</main>
{footer(base)}
</body>
</html>
'''


def breadcrumb(base, label):
    return (f'<nav class="breadcrumb" aria-label="Breadcrumb"><ol><li><a href="{base}index.html">Home</a></li>'
            f'<li aria-current="page">{label}</li></ol></nav>')


def page_hero(base, eyebrow, title, lede, label, media_html="", buttons=""):
    grid = "page-hero__grid page-hero__grid--media" if media_html else "page-hero__grid"
    right = f'<div class="reveal" data-delay="2">{media_html}</div>' if media_html else ""
    return f'''<section class="page-hero textured">
  <div class="container">
    <div class="{grid}">
      <div>
        {breadcrumb(base, label)}
        <p class="eyebrow">{eyebrow}</p>
        <h1>{title}</h1>
        <p class="lede">{lede}</p>
        {buttons}
      </div>
      {right}
    </div>
  </div>
</section>'''


def cta_buttons(base, light=False):
    call_cls = "btn--light" if light else "btn--outline"
    book_cls = "btn--brass" if light else ""
    return (f'<div class="btn-row"><a class="btn {book_cls}" href="{base}contact.html#book">{icon("calendar")}Book an appointment</a>'
            f'<a class="btn {call_cls}" href="tel:{PHONE_TEL}">{icon("phone")}Call {PHONE}</a></div>')


def final_cta(base, title="Ready when <em>you</em> are", lede="Whether it's a routine check-up or something that's been on your mind for a while, we'd be glad to help. Call us or send an enquiry and we'll find a time that suits you."):
    return f'''<section class="section cta-final">
  <div class="container">
    <div class="band on-dark reveal">
      <p class="eyebrow">Book an appointment</p>
      <h2>{title}</h2>
      <p class="lede">{lede}</p>
      {cta_buttons(base, light=True)}
    </div>
  </div>
</section>'''
