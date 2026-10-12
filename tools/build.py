"""Build The Dental House static site into ../thedentalhouse-site/.

Usage:  python3 tools/build.py
The output is plain HTML/CSS/JS. Upload the contents of thedentalhouse-site/ to public_html.
"""
import os
import re
from pathlib import Path

from parts import (PHONE, PHONE_TEL, EMAIL, FACEBOOK, SITE_URL, icon, icon_filled_star, media, verify, pdf, page,
                   page_hero, cta_buttons, final_cta, hours_table, LOGO_MARK)
from data import TREATMENTS, HOME_TREATMENTS, TEAM_GROUPS, PLAN_BENEFITS, IMAGES

OUT = Path(__file__).resolve().parent.parent / "thedentalhouse-site"
B = ""  # relative base for normal pages
TX = {t["id"]: t for t in TREATMENTS}
PAGES = {}


def add(path, html):
    PAGES[path] = html


def initials(p):
    return (p["first"][0] + p["last"][0]).upper()


def slug(p):
    return re.sub(r"[^a-z0-9]+", "-", f'{p["first"]} {p["last"]}'.lower()).strip("-")


def avatar(p, base=B):
    name = f'{p.get("title", "") + " " if p.get("title") else ""}{p["first"]} {p["last"]}'
    return (f'<div class="avatar" aria-hidden="true">{initials(p)}'
            f'<img src="{base}assets/img/team-{slug(p)}.jpg" alt="" width="152" height="152" loading="lazy" '
            f'decoding="async" onerror="this.hidden=true"></div>'), name


# ============================================================ HOME
def build_home():
    tx_cards = ""
    for i, tid in enumerate(HOME_TREATMENTS):
        t = TX[tid]
        tx_cards += f'''<article class="card card--link reveal" data-delay="{i % 3}">
  {media(B, t["img"], t["alt"], 1600, 1200, variant=["", "warm", "deep"][i % 3])}
  <div class="card__body">
    <h3><a class="card__link" href="treatments.html#{t["id"]}">{t["title"]}</a></h3>
    <p>{t["card"]}</p>
    <span class="link-arrow" aria-hidden="true">Find out more {icon("arrow")}</span>
  </div>
</article>'''

    team_avatars = ""
    for grp, people in TEAM_GROUPS[:2]:
        for p in people:
            av, _ = avatar(p)
            team_avatars += av

    body = f'''
<section class="hero" aria-labelledby="hero-title">
  {media(B, "hero-home.jpg", "The bright, welcoming reception at The Dental House", 2400, 1350, eager=True, variant="deep")}
  <div class="container">
    <div class="hero__inner">
      <p class="eyebrow reveal-load">Private family dentistry in Worksop</p>
      <h1 id="hero-title" class="reveal-load">Looking after <em>you</em> &amp; your&nbsp;smile</h1>
      <p class="lede reveal-load">A friendly, personal family practice on Carlton Road, where you'll see familiar faces, have time to ask questions, and go at a pace that feels right for you.</p>
      <div class="reveal-load">{cta_buttons(B, light=True)}</div>
      <div class="hero__meta reveal-load">
        <span>{icon("pin")}37 Carlton Road, Worksop</span>
        <span>{icon("clock")}Open Monday to Friday</span>
      </div>
    </div>
  </div>
</section>

<section class="trust" aria-label="Why patients choose us">
  <div class="container">
    <ul>
      <li>{icon("shield")}GDC-registered team</li>
      <li>{icon("heart")}Family &amp; nervous-patient friendly</li>
      <li>{icon("plan")}Dental care plans</li>
      <li>{icon("star")}5/5 verified reviews</li>
    </ul>
  </div>
</section>

<section class="section textured">
  <div class="container">
    <div class="split split--wide-media">
      <div class="feature__media reveal">
        {media(B, "reception.jpg", "A calm waiting area with a sage armchair and soft natural light", 1600, 1200, cls="media--shadow", variant="warm")}
        <div class="feature__note"><strong>Time to talk</strong>Every appointment includes time for your questions.</div>
      </div>
      <div class="reveal" data-delay="1">
        <p class="eyebrow">Welcome to The Dental House</p>
        <h2>Calm, personal care in the heart of <em>Worksop</em></h2>
        <p class="lede">We're an independent practice, so we can take the time to get to know you. Every decision about your care is made with you, explained in plain English and never rushed.</p>
        <ul class="checklist">
          <li>{icon("check")}<span>Time to talk at every appointment</span></li>
          <li>{icon("check")}<span>A written estimate before any treatment begins</span></li>
          <li>{icon("check")}<span>Care for the whole family, from first teeth onwards</span></li>
        </ul>
        <a class="link-arrow" href="about.html">About our practice {icon("arrow")}</a>
      </div>
    </div>
  </div>
</section>

<section class="section section--linen">
  <div class="container">
    <div class="section-head section-head--split">
      <div>
        <p class="eyebrow">Treatments</p>
        <h2>Everything your smile needs, under <em>one</em> roof</h2>
      </div>
      <p class="lede">From routine check-ups and hygiene visits to crowns, whitening and clear aligners, every treatment starts with a conversation about what matters to you.</p>
    </div>
    <div class="tx-grid">
      {tx_cards}
    </div>
    <div class="text-center mt-3"><a class="btn btn--outline" href="treatments.html">See all treatments {icon("arrow")}</a></div>
  </div>
</section>

<section class="section textured">
  <div class="container">
    <div class="split split--reverse">
      <div class="feature__media reveal">
        {media(B, "nervous-patients.jpg", "A dental nurse offering a reassuring hand to a patient in the chair", 1800, 1200, cls="media--shadow")}
      </div>
      <div class="reveal" data-delay="1">
        <p class="eyebrow">Nervous patients</p>
        <h2>Nervous about the <em>dentist?</em></h2>
        <p class="lede">You're not alone, and you won't be judged. Many of our patients felt the same before their first visit.</p>
        <ul class="checklist">
          <li>{icon("chat")}<span>We'll talk first, with no examination until you're ready</span></li>
          <li>{icon("hand")}<span>Agree a stop signal and take breaks whenever you need them</span></li>
          <li>{icon("compass")}<span>We explain each step before we do it, at your pace</span></li>
        </ul>
        <a class="btn" href="nervous-patients.html">How we can help {icon("arrow")}</a>
      </div>
    </div>
  </div>
</section>

<section class="section section--tight">
  <div class="container">
    <div class="band on-dark">
      <div class="split">
        <div class="reveal">
          <p class="eyebrow">Dental care plans</p>
          <h2>Spread the cost, and put <em>prevention</em> first</h2>
          <p class="lede">A simple monthly plan that helps you keep up with routine care, with 20% off many treatments, plus emergency cover at home and away.</p>
          <ul class="checklist">
            <li>{icon("check")}<span>20% off fillings, crowns, bridges, dentures and more</span></li>
            <li>{icon("check")}<span>Out-of-hours emergency care and worldwide trauma cover</span></li>
            <li>{icon("check")}<span>Fixed monthly payments by Direct Debit</span></li>
          </ul>
          <div class="btn-row"><a class="btn btn--brass" href="careplans.html">Compare care plans {icon("arrow")}</a></div>
        </div>
        <div class="reveal" data-delay="2">
          {media(B, "family-smile.jpg", "Three generations of a family laughing together on a sofa", 1800, 1200, variant="warm")}
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section textured">
  <div class="container">
    <div class="split split--wide-text">
      <div class="reveal">
        <p class="eyebrow">Meet the team</p>
        <h2>Experienced, friendly and <em>local</em></h2>
        <p class="lede">Our dentists, hygienists, therapists, dental nurses and receptionists work closely together to make every visit feel friendly and personal.</p>
        <div class="team-teaser">{team_avatars}</div>
        <a class="btn btn--outline" href="theteam.html">Meet the whole team {icon("arrow")}</a>
      </div>
      <div class="reveal" data-delay="2">
        {media(B, "surgery-room.jpg", "A modern treatment room with a teal dental chair and oak cabinetry", 1600, 1200, cls="media--shadow", variant="deep")}
      </div>
    </div>
  </div>
</section>

<section class="section section--white" aria-labelledby="reviews-title">
  <div class="container">
    <div class="section-head section-head--center reveal">
      <p class="eyebrow">Patient reviews</p>
      <h2 id="reviews-title">In our patients' <em>words</em></h2>
      <p class="lede">Our reviews are independently collected and verified by Working Feedback. Look for the reviews tab at the side of the page.</p>
    </div>
    <!-- REAL REVIEWS ONLY: paste verified reviews from Working Feedback into these cards (name/initials with permission). Do not invent testimonials. -->
    <div class="reviews-slot">
      <figure class="review-placeholder reveal" data-delay="0">
        <span class="quote-mark" aria-hidden="true">&ldquo;</span>
        <p>{verify("ADD REAL REVIEW")} Verified review from Working Feedback.</p>
        <div class="stars" aria-hidden="true">{icon_filled_star() * 5}</div>
      </figure>
      <figure class="review-placeholder reveal" data-delay="1">
        <span class="quote-mark" aria-hidden="true">&ldquo;</span>
        <p>{verify("ADD REAL REVIEW")} Verified review from Working Feedback.</p>
        <div class="stars" aria-hidden="true">{icon_filled_star() * 5}</div>
      </figure>
      <figure class="review-placeholder reveal" data-delay="2">
        <span class="quote-mark" aria-hidden="true">&ldquo;</span>
        <p>{verify("ADD REAL REVIEW")} Verified review from Working Feedback.</p>
        <div class="stars" aria-hidden="true">{icon_filled_star() * 5}</div>
      </figure>
    </div>
  </div>
</section>

<section class="section section--linen" aria-labelledby="visit-title">
  <div class="container">
    <div class="split">
      <div class="reveal">
        <p class="eyebrow">Visit us</p>
        <h2 id="visit-title">Opening hours &amp; <em>finding us</em></h2>
        {hours_table()}
        <ul class="info-list mt-2">
          <li>{icon("pin")}<div><strong>Address</strong>37 Carlton Road, Worksop, Nottinghamshire S80 1PD</div></li>
          <li>{icon("car")}<div><strong>Parking</strong>Pay-and-display at Worksop Train Station or Matalan (Eastgate), or the Halfords/Screwfix car park.</div></li>
          <li>{icon("access")}<div><strong>Access</strong>Disabled access is at the rear of the practice.</div></li>
        </ul>
        <div class="mt-2"><a class="link-arrow" href="contact.html">Contact &amp; directions {icon("arrow")}</a></div>
      </div>
      <div class="reveal" data-delay="2">
        <div class="map">
          <iframe title="Map showing The Dental House, 37 Carlton Road, Worksop" src="https://www.google.com/maps?q=The+Dental+House,+37+Carlton+Road,+Worksop+S80+1PD&amp;output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
        </div>
      </div>
    </div>
  </div>
</section>

{final_cta(B)}
'''
    add("index.html", page(B, "index.html",
                           "The Dental House | Friendly Family Dentist in Worksop",
                           "The Dental House is a friendly, independent family dental practice on Carlton Road, Worksop. Check-ups, hygiene, cosmetic dentistry, Invisalign and dental care plans.",
                           body, body_class="has-dark-hero"))


# ============================================================ ABOUT
def build_about():
    values = [
        ("users", "Personal care", "You'll see familiar faces who know you and your history, and who remember what matters to you."),
        ("chat", "Decisions made together", "We explain what we see and set out your options, costs and alternatives. You decide what happens next."),
        ("compass", "At your pace", "Nothing is rushed. If you'd like time to think, or would rather take treatment in smaller steps, that's fine with us."),
        ("leaf", "A calm atmosphere", "A friendly welcome, a quiet waiting room and a team who take time to put you at ease."),
    ]
    vcards = "".join(f'''<div class="card card--plain reveal" data-delay="{i}">
  <span class="icon-badge">{icon(ic)}</span>
  <h3>{t}</h3>
  <p>{d}</p>
</div>''' for i, (ic, t, d) in enumerate(values))
    body = f'''
{page_hero(B, "Our practice", "A family practice that takes <em>time</em> for you",
               "The Dental House is an independent, private dental practice in Worksop. We look after individuals and families of all ages, and we believe good dentistry starts with listening.",
               "About", media(B, "reception.jpg", "A calm waiting area with a sage armchair and soft natural light", 1600, 1200, cls="media--shadow", variant="warm"),
               cta_buttons(B))}

<section class="section section--white">
  <div class="container">
    <div class="split split--wide-text">
      <div class="reveal">
        <p class="eyebrow">Our philosophy</p>
        <h2>Good dentistry is <em>personal</em></h2>
      </div>
      <div class="prose reveal" data-delay="1">
        <p>We know that a visit to the dentist isn't everyone's idea of a good morning. That's why we work hard to make The Dental House feel calm, friendly and unhurried, from the moment you walk in.</p>
        <p>Every patient is different, so your care is planned around you. We'll talk you through what we find, explain your options in plain English and give you a written estimate before any treatment begins. You're involved in every decision, and you're always welcome to ask questions.</p>
        <p>Our focus is on keeping your mouth healthy for life. That means prevention first, careful and conservative treatment when it's needed, and regular care that fits around you and your family.</p>
      </div>
    </div>
  </div>
</section>

<section class="section textured">
  <div class="container">
    <div class="section-head section-head--center reveal">
      <p class="eyebrow">What you can expect</p>
      <h2>The way we <em>work</em></h2>
    </div>
    <div class="grid grid--4">{vcards}</div>
  </div>
</section>

<section class="section section--linen">
  <div class="container">
    <div class="split">
      <div class="feature__media reveal">
        {media(B, "surgery-room.jpg", "A modern treatment room with a teal dental chair and oak cabinetry", 1600, 1200, cls="media--shadow", variant="deep")}
      </div>
      <div class="reveal" data-delay="1">
        <p class="eyebrow">The team</p>
        <h2>Experienced people you'll <em>get to know</em></h2>
        <p class="lede">Our dentists, hygienists and therapists are supported by an experienced team of dental nurses and receptionists. Every clinician is registered with the General Dental Council.</p>
        <div class="btn-row"><a class="btn" href="theteam.html">Meet the team {icon("arrow")}</a><a class="btn btn--outline" href="new-patients.html">Becoming a patient</a></div>
      </div>
    </div>
  </div>
</section>

<section class="section section--white">
  <div class="container">
    <div class="grid grid--3">
      <a class="card card--plain card--cream card--link reveal" href="{pdf("brochure")}" style="text-decoration:none;color:inherit">
        <span class="icon-badge">{icon("file")}</span>
        <h3>Practice brochure</h3>
        <p>Everything about the practice in one place. PDF.</p>
      </a>
      <a class="card card--plain card--cream card--link reveal" data-delay="1" href="patient-info.html" style="text-decoration:none;color:inherit">
        <span class="icon-badge">{icon("info")}</span>
        <h3>Patient information</h3>
        <p>Privacy notices, complaints procedure and practice policies.</p>
      </a>
      <a class="card card--plain card--cream card--link reveal" data-delay="2" href="contact.html" style="text-decoration:none;color:inherit">
        <span class="icon-badge">{icon("pin")}</span>
        <h3>Finding us</h3>
        <p>37 Carlton Road, with parking nearby and disabled access at the rear.</p>
      </a>
    </div>
  </div>
</section>

{final_cta(B)}
'''
    add("about.html", page(B, "about.html", "About Our Practice | The Dental House, Worksop",
                           "An independent family dental practice in Worksop offering personal, unhurried care. We involve you in every decision and work at a pace that suits you.",
                           body))


# ============================================================ TREATMENTS
def build_treatments():
    index = "".join(
        f'<li><a href="#{t["id"]}">{icon(t["icon"])}<span>{t["title"]}</span>{icon("arrow", "arrow")}</a></li>'
        for t in TREATMENTS)
    sections = ""
    for i, t in enumerate(TREATMENTS):
        if t["img"]:
            visual = media(B, t["img"], t["alt"], 1600, 1200, cls="media--shadow", variant=["", "warm", "deep"][i % 3])
        else:
            visual = f'<div class="tx-icon-panel" aria-hidden="true">{icon(t["icon"])}</div>'
        rev = " split--reverse" if i % 2 else ""
        sections += f'''<section class="tx-section" id="{t["id"]}" aria-labelledby="{t["id"]}-title">
  <div class="container">
    <div class="split{rev}">
      <div class="reveal">{visual}</div>
      <div class="reveal" data-delay="1">
        <p class="eyebrow">Treatment</p>
        <h2 id="{t["id"]}-title">{t["title"]}</h2>
        <div class="lede">{t["intro"]}</div>
        <div class="tx-facts">
          <div><h3>Who it's for</h3>{t["who"]}</div>
          <div><h3>What to expect</h3>{t["expect"]}</div>
        </div>
        <div class="btn-row"><a class="btn" href="contact.html#book">Ask about {t["short"].lower() if t["id"] != "invisalign" else "Invisalign"}</a><a class="btn btn--outline" href="fees.html">Fees</a></div>
      </div>
    </div>
  </div>
</section>'''
    body = f'''
{page_hero(B, "Treatments", "Care for every <em>stage</em> of life",
               "From routine check-ups to restoring and improving your smile, every treatment begins with a conversation. We'll explain your options, the costs and the alternatives, so you can decide what's right for you.",
               "Treatments")}
<section class="section--tight" style="padding-top:0" aria-label="Treatment list">
  <div class="container">
    <ul class="tx-index" role="list" style="list-style:none;padding:0;margin:0">{index}</ul>
  </div>
</section>
<div class="mt-3"></div>
{sections}
<section class="section section--tight">
  <div class="container container--narrow">
    <div class="notice reveal">
      {icon("info")}
      <div>
        <h3>Your treatment, your choice</h3>
        <p>Every mouth is different, so results vary from person to person. Your dentist will discuss the benefits, risks, alternatives and costs of any treatment with you, and give you a written estimate before you go ahead.</p>
      </div>
    </div>
  </div>
</section>
{final_cta(B)}
'''
    add("treatments.html", page(B, "treatments.html", "Dental Treatments in Worksop | The Dental House",
                                "Check-ups, hygiene, tooth-coloured fillings, whitening, veneers, crowns and bridges, dentures, Invisalign, mouthguards and extractions at The Dental House, Worksop.",
                                body))


# ============================================================ CARE PLANS
def build_careplans():
    rows = "".join(
        f'<tr><th scope="row">{b}</th><td>{icon("check", label="Included")}</td><td>{icon("check", label="Included")}</td></tr>'
        for b in PLAN_BENEFITS)
    v = verify()
    body = f'''
{page_hero(B, "Dental care plans", "Routine care, spread <em>monthly</em>",
               "Our care plans make it easy to keep up with regular check-ups and hygiene visits, with savings on treatment and emergency cover included. One simple monthly payment, and no surprises.",
               "Care plans", media(B, "family-smile.jpg", "Three generations of a family laughing together on a sofa", 1800, 1200, cls="media--shadow", variant="warm"),
               f'<div class="btn-row"><a class="btn" href="#join">How to join</a><a class="btn btn--outline" href="tel:{PHONE_TEL}">{icon("phone")}Call {PHONE}</a></div>')}

<section class="section section--white" aria-labelledby="compare-title">
  <div class="container">
    <div class="section-head section-head--center reveal">
      <p class="eyebrow">Compare plans</p>
      <h2 id="compare-title">Plan A &amp; Plan <em>B</em></h2>
      <p class="lede">Both plans include the benefits below. Ask us which plan suits your needs.</p>
    </div>
    <!-- [VERIFY] Monthly prices and the difference between Plan A and Plan B (e.g. number of examinations / hygiene visits per year) are not on the current site. Fill in before going live. -->
    <div class="compare-wrap reveal">
      <table class="compare">
        <caption>Prices are per month, collected by Direct Debit. {v}</caption>
        <thead>
          <tr>
            <th scope="col"><span class="visually-hidden">Benefit</span></th>
            <th scope="col"><span class="plan-name">Plan A</span><span class="plan-price">£[VERIFY]/month</span></th>
            <th scope="col"><span class="plan-name">Plan B</span><span class="plan-price">£[VERIFY]/month</span></th>
          </tr>
        </thead>
        <tbody>
          <tr class="group"><th scope="rowgroup" colspan="3">Routine care</th></tr>
          <tr><th scope="row">Dental examinations per year</th><td>{v}</td><td>{v}</td></tr>
          <tr><th scope="row">Hygiene appointments per year</th><td>{v}</td><td>{v}</td></tr>
          <tr class="group"><th scope="rowgroup" colspan="3">Included with both plans</th></tr>
          {rows}
        </tbody>
      </table>
    </div>
  </div>
</section>

<section class="section textured" id="join" aria-labelledby="join-title">
  <div class="container">
    <div class="section-head reveal">
      <p class="eyebrow">How to join</p>
      <h2 id="join-title">Joining takes a few <em>minutes</em></h2>
    </div>
    <ol class="stepper">
      <li class="reveal" data-delay="0"><h3>Get in touch</h3><p>Call us on {PHONE} or pop in to the practice to talk through which plan suits you.</p></li>
      <li class="reveal" data-delay="1"><h3>Complete your agreement</h3><p>Call in to fill in a short care plan agreement and a Direct Debit mandate.</p></li>
      <li class="reveal" data-delay="2"><h3>Monthly payments</h3><p>Payments are collected monthly by Direct Debit.</p></li>
      <li class="reveal" data-delay="3"><h3>You're covered</h3><p>Your cover starts on the 1st of the month.</p></li>
    </ol>
  </div>
</section>

<section class="section section--linen">
  <div class="container">
    <div class="grid grid--2">
      <div class="note-box note-box--white reveal">
        <p class="eyebrow">Prefer to pay as you go?</p>
        <h3>Registration &amp; Insurance Scheme</h3>
        <p class="price-tag">£45.68 <small>per year</small></p>
        <p>If you'd rather not join a care plan, you can pay for treatment as you need it under our fee-per-item arrangement. You'll be given a written estimate before any treatment.</p>
        <a class="link-arrow" href="{pdf("fees")}">Private fee scale (PDF) {icon("download")}</a>
      </div>
      <div class="note-box reveal" data-delay="1">
        <p class="eyebrow">Good to know</p>
        <h3>Questions about care plans?</h3>
        <ul class="checklist">
                    <li>{icon("check")}<span>Payments are taken monthly by Direct Debit, and cover begins on the 1st of the month.</span></li>
          <li>{icon("check")}<span>Our team will happily talk you through the options, with no obligation.</span></li>
        </ul>
        <a class="btn" href="contact.html#book">Ask about a care plan</a>
      </div>
    </div>
  </div>
</section>
{final_cta(B, "Keep your smile <em>healthy</em> for life", "Talk to us about which care plan suits you and your family.")}
'''
    add("careplans.html", page(B, "careplans.html", "Dental Care Plans | The Dental House, Worksop",
                               "Spread the cost of routine dental care with a monthly plan from The Dental House in Worksop. 20% off many treatments, emergency cover and worldwide trauma insurance.",
                               body))


# ============================================================ TEAM
def build_team():
    groups = ""
    for gname, people in TEAM_GROUPS:
        cards = ""
        for i, p in enumerate(people):
            av, name = avatar(p)
            rows = ""
            if p.get("gdc"):
                gdc = p["gdc"]
                if p.get("gdc_verify"):
                    gdc += " " + verify()
                    gdc = ("<!-- [VERIFY] Tina Welsh and Dr Robert Hardy were both listed as GDC No. 80637 on the old site. "
                           "One is wrong. Check both on the GDC register (olr.gdc-uk.org) and correct. -->") + gdc
                rows += f'<div><dt>GDC No.</dt><dd>{gdc}</dd></div>'
            if p.get("reg"):
                rows += f'<div><dt>Registered</dt><dd>{p["reg"]}</dd></div>'
            if p.get("quals"):
                rows += f'<div><dt>Qualifications</dt><dd>{p["quals"]}</dd></div>'
            post = f' <span class="post">{p["post"]}</span>' if p.get("post") else ""
            cards += f'''<article class="team-card reveal" data-delay="{i % 3}">
  {av}
  <div class="team-card__name">
    <h3>{name}{post}</h3>
    <p class="role">{p["role"]}</p>
  </div>
  {f"<dl>{rows}</dl>" if rows else ""}
</article>'''
        groups += f'''<section class="team-group" aria-label="{gname}">
  <div class="team-group__title"><h2>{gname}</h2><hr class="hairline"></div>
  <div class="team-grid">{cards}</div>
</section>'''
    body = f'''
{page_hero(B, "Our team", "The people behind your <em>smile</em>",
               "A close, experienced team of dentists, hygienists, therapists, nurses and receptionists. All our clinicians are registered with the General Dental Council.",
               "Our team")}
<section class="section section--linen" style="padding-top:clamp(3rem,6vw,4.5rem)">
  <div class="container">
    {groups}
    <p class="small muted mt-3">You can check any clinician's registration on the <a href="https://olr.gdc-uk.org/SearchRegister" rel="noopener" target="_blank">GDC online register</a>.</p>
  </div>
</section>
{final_cta(B, "Come and <em>meet</em> us", "We'd be glad to welcome you to the practice.")}
'''
    add("theteam.html", page(B, "theteam.html", "Meet Our Team | The Dental House, Worksop",
                             "Meet the dentists, hygienists, therapists, dental nurses and reception team at The Dental House, Worksop. All clinicians are GDC registered.",
                             body))


# ============================================================ NEW PATIENTS
def faq(items):
    return '<div class="accordion">' + "".join(
        f'<details><summary>{q}{icon("plus")}</summary><div class="answer">{a}</div></details>' for q, a in items) + "</div>"


def build_new_patients():
    faqs = faq([
        ("Are you taking on new patients?", f"<p>Yes, we welcome new patients of all ages. Call us on {PHONE} or send an enquiry and we'll arrange your first visit. {verify()}</p>"),
        ("Do you offer NHS treatment?", f"<p>The Dental House is a private practice. You can join one of our dental care plans or pay for treatment as you go. {verify('VERIFY: confirm no NHS contract')}</p>"),
        ("Do you see children?", f"<p>Yes. We're a family practice, and we love seeing children from an early age so that visiting the dentist feels normal and relaxed. Please ask about care plan options for children. {verify()}</p>"),
        ("How much will my first visit cost?", f'<p>Please see our <a href="fees.html">fees page</a> and the <a href="{pdf("fees")}">private fee scale (PDF)</a>, or call us and we\'ll be happy to explain. You\'ll always get a written estimate before any treatment.</p>'),
        ("How do I pay?", f"<p>Payment is due on completion of treatment, by cash or card {verify()}. Care plan fees are paid monthly by Direct Debit.</p>"),
        ("What if I need to cancel?", "<p>Please give us at least 24 hours' notice so we can offer the appointment to someone else.</p>"),
        ("I'm nervous. Can you help?", '<p>Absolutely. Let us know when you book and we\'ll make sure there\'s time to talk first. Read more on our <a href="nervous-patients.html">nervous patients page</a>.</p>'),
        ("Is there parking and step-free access?", "<p>Pay-and-display parking is available at Worksop Train Station or Matalan (Eastgate), and in the Halfords/Screwfix car park. Disabled access is at the rear of the practice.</p>"),
    ])
    body = f'''
{page_hero(B, "New patients", "A warm <em>welcome</em> to The Dental House",
               "Joining a new practice should feel easy. Here's what to expect at your first visit, what to bring, and how to register.",
               "New patients", media(B, "new-patients.jpg", "A receptionist welcoming a new patient at the front desk", 1800, 1200, cls="media--shadow", variant="warm"),
               cta_buttons(B))}

<section class="section section--white">
  <div class="container">
    <div class="section-head reveal">
      <p class="eyebrow">How to register</p>
      <h2>Three simple <em>steps</em></h2>
    </div>
    <ol class="stepper" style="grid-template-columns:repeat(auto-fit,minmax(240px,1fr))">
      <li class="reveal"><h3>Get in touch</h3><p>Call {PHONE} or send us an enquiry. We'll find an appointment that suits you.</p></li>
      <li class="reveal" data-delay="1"><h3>Tell us about you</h3><p>We'll ask you to complete a medical history form when you arrive, or before your visit.</p></li>
      <li class="reveal" data-delay="2"><h3>Your first visit</h3><p>A relaxed, thorough consultation with your dentist, and time for any questions.</p></li>
    </ol>
  </div>
</section>

<section class="section textured">
  <div class="container">
    <div class="grid grid--2">
      <div class="reveal">
        <p class="eyebrow">Your first visit</p>
        <h2>What to <em>expect</em></h2>
        <ul class="checklist">
          <li>{icon("check")}<span>A friendly welcome and a chance to tell us about any worries or goals</span></li>
          <li>{icon("check")}<span>A thorough examination of your teeth, gums and mouth, including a mouth cancer check</span></li>
          <li>{icon("check")}<span>X-rays if they're needed</span></li>
          <li>{icon("check")}<span>A clear explanation of what we find, and your options</span></li>
          <li>{icon("check")}<span>A written treatment plan and estimate before any treatment begins</span></li>
        </ul>
      </div>
      <div class="reveal" data-delay="1">
        <p class="eyebrow">What to bring</p>
        <h2>Bring <em>along</em></h2>
        <ul class="checklist">
          <li>{icon("file")}<span>A list of any medicines you take, including inhalers and creams</span></li>
          <li>{icon("file")}<span>Details of any medical conditions or allergies</span></li>
          <li>{icon("file")}<span>Your previous dentist's details, if you have them</span></li>
          <li>{icon("card")}<span>A payment card, as payment is due on completion of treatment</span></li>
          <li>{icon("clock")}<span>Please arrive a few minutes early to settle in</span></li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section section--linen" aria-labelledby="pay-title">
  <div class="container">
    <div class="section-head reveal">
      <p class="eyebrow">Paying for your care</p>
      <h2 id="pay-title">Care plan or <em>pay as you go</em></h2>
    </div>
    <div class="grid grid--2">
      <div class="note-box note-box--white reveal">
        <span class="icon-badge">{icon("plan")}</span>
        <h3 class="mt-2">Dental care plan</h3>
        <p>A fixed monthly payment for your routine care, with 20% off many treatments and emergency cover at home and abroad.</p>
        <a class="link-arrow" href="careplans.html">Compare care plans {icon("arrow")}</a>
      </div>
      <div class="note-box note-box--white reveal" data-delay="1">
        <span class="icon-badge">{icon("card")}</span>
        <h3 class="mt-2">Pay as you go</h3>
        <p>Join our Registration &amp; Insurance Scheme for £45.68 a year, and pay for treatment as you need it, with a written estimate first.</p>
        <a class="link-arrow" href="fees.html">See our fees {icon("arrow")}</a>
      </div>
    </div>
  </div>
</section>

<section class="section section--white" aria-labelledby="faq-title">
  <div class="container container--narrow">
    <div class="section-head reveal">
      <p class="eyebrow">FAQs</p>
      <h2 id="faq-title">Questions new patients <em>ask</em></h2>
    </div>
    <div class="reveal">{faqs}</div>
  </div>
</section>
{final_cta(B, "We'd love to <em>meet</em> you")}
'''
    add("new-patients.html", page(B, "new-patients.html", "New Patients | The Dental House, Worksop",
                                  "Registering as a new patient at The Dental House, Worksop: what to expect at your first visit, what to bring, care plans and pay-as-you-go options, and FAQs.",
                                  body))


# ============================================================ NERVOUS
def build_nervous():
    steps = [
        ("chat", "Talk first", "Your first visit can simply be a chat. Tell us what worries you, what's happened before and what helps. Nothing happens until you're ready."),
        ("hand", "A stop signal", "Before we start, we'll agree a simple signal, such as raising your hand. When you use it, we stop. You're in control throughout."),
        ("compass", "Step by step", "We'll explain what we're about to do before we do it, and check in with you as we go. No surprises."),
        ("pause", "Breaks whenever you need", "Need a moment to rest your jaw or catch your breath? Just say. We can also split treatment into shorter visits."),
        ("clock", "Time to settle", "Let us know you're nervous when you book, and we'll allow extra time so nothing feels rushed. Quieter times of day may suit you too."),
        ("users", "Bring someone along", "You're welcome to bring a friend or family member for support."),
    ]
    cards = "".join(f'''<div class="card card--plain reveal" data-delay="{i % 3}">
  <span class="icon-badge">{icon(ic)}</span><h3>{t}</h3><p>{d}</p></div>''' for i, (ic, t, d) in enumerate(steps))
    body = f'''
{page_hero(B, "Nervous patients", "It's okay to feel <em>nervous</em>",
               "Lots of people feel anxious about visiting the dentist, often because of a bad experience in the past. We won't judge you, and we'll never rush you. Together we'll find a way that feels manageable.",
               "Nervous patients", media(B, "nervous-patients.jpg", "A dental nurse offering a reassuring hand to a patient in the chair", 1800, 1200, cls="media--shadow"),
               cta_buttons(B))}
<section class="section section--white">
  <div class="container">
    <div class="section-head section-head--center reveal">
      <p class="eyebrow">How we help</p>
      <h2>You set the <em>pace</em></h2>
      <p class="lede" style="margin-inline:auto">Small things make a big difference. Here are some of the ways we help nervous patients feel more comfortable.</p>
    </div>
    <div class="grid grid--3">{cards}</div>
  </div>
</section>
<section class="section textured">
  <div class="container">
    <div class="split">
      <div class="reveal">
        <p class="eyebrow">Getting started</p>
        <h2>The hardest part is <em>picking up the phone</em></h2>
        <p class="lede">If calling feels like too much, send us an enquiry instead and let us know you're nervous. We'll take it from there, gently.</p>
        {cta_buttons(B)}
      </div>
      <div class="reveal" data-delay="1">
        <div class="note-box note-box--white">
          <h3>Been a while since your last visit?</h3>
          <p>That's completely fine, and more common than you might think. There's no telling-off here. We'll simply start from where you are now and focus on what you'd like to achieve.</p>
          <p class="mb-0">If you feel you need more support than we can offer at the practice, we'll talk through the other options with you.</p>
        </div>
      </div>
    </div>
  </div>
</section>
{final_cta(B, "Take the <em>first</em> step", "Call, email or send an enquiry. Just let us know you're nervous, and we'll look after the rest.")}
'''
    add("nervous-patients.html", page(B, "nervous-patients.html", "Nervous Patients | The Dental House, Worksop",
                                      "Nervous about the dentist? At The Dental House in Worksop we go at your pace, agree a stop signal and explain every step. Talk to us with no pressure.",
                                      body))


# ============================================================ EMERGENCY
def build_emergency():
    body = f'''
{page_hero(B, "Emergencies", "Dental pain or an <em>accident?</em>",
               "If you're in pain, have broken a tooth or had an accident, call us as early in the day as you can and we'll do our best to help.",
               "Emergencies", media(B, "emergency.jpg", "A phone resting on a table beside a cup of tea in evening lamplight", 1800, 1200, cls="media--shadow", variant="deep"),
               f'<a class="phone-hero" href="tel:{PHONE_TEL}">{icon("phone")}{PHONE}</a>')}
<section class="section section--white">
  <div class="container">
    <div class="grid grid--3">
      <div class="card card--plain card--cream reveal">
        <span class="icon-badge">{icon("clock")}</span>
        <h3>During opening hours</h3>
        <p>For a same-day emergency appointment, call {PHONE} as early in the day as possible. We'll assess your pain and provide temporary treatment at the practice where needed.</p>
        <p><a class="link-arrow" href="tel:{PHONE_TEL}">Call {PHONE} {icon("arrow")}</a></p>
      </div>
      <div class="card card--plain card--cream reveal" data-delay="1">
        <span class="icon-badge">{icon("phone")}</span>
        <h3>Out of hours: existing patients</h3>
        <p>If you're an existing patient, call {PHONE} and follow the instructions on the answerphone. Care plan members are covered for out-of-hours emergency care.</p>
      </div>
      <div class="card card--plain card--cream reveal" data-delay="2">
        <span class="icon-badge">{icon("info")}</span>
        <h3>Not a patient, or we're closed</h3>
        <p>If you're not registered with us and need help when we're closed, call <strong>NHS 111</strong> or visit <a href="https://111.nhs.uk" rel="noopener" target="_blank">111.nhs.uk</a> for advice on urgent dental care.</p>
      </div>
    </div>
  </div>
</section>
<section class="section section--tight textured">
  <div class="container container--narrow">
    <div class="notice notice--urgent reveal">
      {icon("alert")}
      <div>
        <h3>When to go to A&amp;E or call 999</h3>
        <p>Go to A&amp;E or call 999 if you have swelling of the face, mouth or neck that is affecting your breathing, swallowing or vision. Do the same for bleeding from the mouth that won't stop, or a serious injury to your face, mouth or teeth.</p>
      </div>
    </div>
    <div class="notice reveal mt-2">
      {icon("info")}
      <div>
        <h3>If a tooth is knocked out</h3>
        <p>Hold it by the crown (the white part), not the root. If it's an adult tooth and it's clean, try to put it back in its socket. If you can't, keep it in milk. Then call us straight away, as time matters. Don't try to put a baby tooth back in.</p>
      </div>
    </div>
  </div>
</section>
{final_cta(B, "We're here to <em>help</em>", "Call us as early in the day as possible for a same-day emergency appointment.")}
'''
    add("emergency.html", page(B, "emergency.html", "Dental Emergencies | The Dental House, Worksop",
                               "Dental emergency in Worksop? Call The Dental House on 01909 472477 as early as possible for a same-day appointment. Out-of-hours advice for patients and non-patients.",
                               body))


# ============================================================ FEES
def build_fees():
    body = f'''
{page_hero(B, "Fees", "Clear, honest <em>pricing</em>",
               "We believe you should always know what your treatment will cost before it begins. You'll receive a written estimate for any treatment, and we're always happy to talk through the options.",
               "Fees")}
<section class="section section--white" style="padding-top:clamp(3rem,6vw,4.5rem)">
  <div class="container">
    <div class="grid grid--3">
      <a class="card card--plain card--cream card--link reveal" href="{pdf("fees")}" style="text-decoration:none;color:inherit">
        <span class="icon-badge">{icon("download")}</span>
        <p class="doc-meta">PDF · March 2026</p>
        <h3>Private fee scale</h3>
        <p>Our full list of private fees, updated March 2026.</p>
        <span class="link-arrow">Download {icon("arrow")}</span>
      </a>
      <div class="card card--plain card--cream reveal" data-delay="1">
        <span class="icon-badge">{icon("card")}</span>
        <h3>Paying for treatment</h3>
        <p>Payment is due on completion of treatment, by cash or card {verify()}. A written estimate is always given before treatment begins.</p>
        <p class="small muted">Please give at least 24 hours' notice if you need to cancel an appointment.</p>
      </div>
      <a class="card card--plain card--cream card--link reveal" data-delay="2" href="careplans.html" style="text-decoration:none;color:inherit">
        <span class="icon-badge">{icon("plan")}</span>
        <h3>Dental care plans</h3>
        <p>Spread the cost of routine care with a monthly plan and save 20% on many treatments.</p>
        <span class="link-arrow">Compare plans {icon("arrow")}</span>
      </a>
    </div>
  </div>
</section>
<section class="section section--linen">
  <div class="container container--narrow">
    <div class="note-box note-box--white reveal">
      <p class="eyebrow">Pay as you go</p>
      <h2 class="h3">Registration &amp; Insurance Scheme</h2>
      <p class="price-tag">£45.68 <small>per year</small></p>
      <p class="mb-0">Patients who prefer not to join a care plan can register with us under our Registration &amp; Insurance Scheme and pay for treatment item by item, at the prices in our private fee scale.</p>
    </div>
  </div>
</section>
{final_cta(B)}
'''
    add("fees.html", page(B, "fees.html", "Fees & Payment | The Dental House, Worksop",
                          "Private dental fees at The Dental House, Worksop. Download our fee scale, learn how payment works, and compare monthly dental care plans.",
                          body))


# ============================================================ CONTACT
def build_contact():
    body = f'''
{page_hero(B, "Contact &amp; find us", "We'd love to <em>hear</em> from you",
               "Call us, email or send an appointment enquiry below. Our reception team will get back to you as soon as they can during opening hours.",
               "Contact", media(B, "contact-exterior.jpg", "The front of The Dental House at 37 Carlton Road, Worksop", 1800, 1200, cls="media--shadow", variant="warm"),
               cta_buttons(B))}
<section class="section section--white">
  <div class="container">
    <div class="split split--wide-media" style="align-items:start">
      <div class="reveal" id="book">
        <p class="eyebrow">Book an appointment</p>
        <h2>Appointment <em>enquiry</em></h2>
        <p class="muted">Send us a few details and we'll call or email to arrange a time. For anything urgent, please call {PHONE}.</p>
        <!--
          FORM HANDLING
          Default: the "mailto:" action opens the visitor's email app with their details filled in (main.js builds it).
          Better (recommended): use Formspree so messages arrive without needing an email app.
            1. Create a free form at https://formspree.io and copy your form ID.
            2. Change the form tag below to:
               <form class="form-card" id="booking-form" action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
            3. Optionally add: <input type="hidden" name="_subject" value="New appointment enquiry">
        -->
        <form class="form-card" id="booking-form" action="mailto:{EMAIL}" method="post" enctype="text/plain">
          <div class="form-grid">
            <div class="field"><label for="f-name">Your name</label><input id="f-name" name="name" type="text" autocomplete="name" required></div>
            <div class="field"><label for="f-phone">Phone</label><input id="f-phone" name="phone" type="tel" autocomplete="tel" required></div>
            <div class="field full"><label for="f-email">Email</label><input id="f-email" name="email" type="email" autocomplete="email"></div>
            <div class="field full">
              <fieldset>
                <legend>Are you a new or existing patient?</legend>
                <div class="radio-row">
                  <label><input type="radio" name="patient" value="New patient" required> New patient</label>
                  <label><input type="radio" name="patient" value="Existing patient"> Existing patient</label>
                </div>
              </fieldset>
            </div>
            <div class="field">
              <label for="f-reason">What's it about?</label>
              <select id="f-reason" name="reason">
                <option>Check-up</option>
                <option>Hygienist appointment</option>
                <option>Dental care plan</option>
                <option>Cosmetic treatment / whitening</option>
                <option>Invisalign consultation</option>
                <option>Something else</option>
              </select>
            </div>
            <div class="field"><label for="f-pref">Preferred days or times</label><input id="f-pref" name="preferred" type="text" placeholder="e.g. Tuesday mornings"></div>
            <div class="field full"><label for="f-msg">Anything else we should know?</label><span class="hint" id="f-msg-hint">Please don't include detailed medical information here. We'll ask for that securely.</span><textarea id="f-msg" name="message" aria-describedby="f-msg-hint"></textarea></div>
            <div class="field full"><label class="check"><input type="checkbox" name="consent" value="yes" required><span>I'm happy for The Dental House to contact me about this enquiry. See our <a href="privacy-policy.html">privacy policy</a>.</span></label></div>
            <div class="field full"><button class="btn" type="submit">{icon("mail")}Send enquiry</button></div>
          </div>
          <p class="form-status" id="form-status" role="status" aria-live="polite"></p>
        </form>
      </div>
      <div class="reveal" data-delay="1">
        <p class="eyebrow">Get in touch</p>
        <ul class="info-list">
          <li>{icon("phone")}<div><strong>Phone</strong><a href="tel:{PHONE_TEL}">{PHONE}</a></div></li>
          <li>{icon("mail")}<div><strong>Email</strong><a href="mailto:{EMAIL}">{EMAIL}</a></div></li>
          <li>{icon("pin")}<div><strong>Address</strong>37 Carlton Road<br>Worksop<br>Nottinghamshire<br>S80 1PD</div></li>
          <li>{icon("facebook")}<div><strong>Facebook</strong><a href="{FACEBOOK}" rel="noopener" target="_blank">Follow us on Facebook</a></div></li>
        </ul>
        <hr class="hairline--short hairline">
        <h3>Opening hours</h3>
        {hours_table()}
      </div>
    </div>
  </div>
</section>
<section class="section section--linen" aria-labelledby="find-title">
  <div class="container">
    <div class="split">
      <div class="reveal">
        <div class="map">
          <iframe title="Map showing The Dental House, 37 Carlton Road, Worksop" src="https://www.google.com/maps?q=The+Dental+House,+37+Carlton+Road,+Worksop+S80+1PD&amp;output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
        </div>
      </div>
      <div class="reveal" data-delay="1">
        <p class="eyebrow">Finding us</p>
        <h2 id="find-title">Getting <em>here</em></h2>
        <ul class="info-list">
          <li>{icon("car")}<div><strong>Parking</strong>Pay-and-display parking is available at Worksop Train Station or Matalan (Eastgate). Parking is also available in the Halfords/Screwfix car park.</div></li>
          <li>{icon("access")}<div><strong>Accessibility</strong>Disabled access is at the rear of the practice. Let us know when you book if there's anything we can do to help.</div></li>
          <li>{icon("calendar")}<div><strong>Cancellations</strong>Please give at least 24 hours' notice if you need to cancel or rearrange.</div></li>
          <li>{icon("alert")}<div><strong>Emergencies</strong>In pain? Call as early in the day as possible. <a href="emergency.html">Emergency advice</a>.</div></li>
        </ul>
      </div>
    </div>
  </div>
</section>
'''
    add("contact.html", page(B, "contact.html", "Contact & Find Us | The Dental House, Worksop",
                             "Contact The Dental House, 37 Carlton Road, Worksop S80 1PD. Call 01909 472477, email or send an appointment enquiry. Opening hours, parking and access.",
                             body))


# ============================================================ PATIENT INFO
def build_patient_info():
    docs = [
        ("privacy", "Privacy notice for patients", "How we collect, use and protect your personal information."),
        ("privacy_children", "Privacy notice for children", "A child-friendly explanation of how we look after personal information."),
        ("leaflet", "Your personal information", "Patient leaflet on personal information (April 2025)."),
        ("complaints", "Complaints procedure", "How to raise a concern, and how we'll respond."),
        ("brochure", "Practice brochure", "An overview of the practice, team and services (February 2026)."),
        ("fees", "Private fee scale", "Our current private fees (March 2026)."),
    ]
    cards = "".join(f'''<a class="card card--plain card--link reveal" data-delay="{i % 3}" href="{pdf(k)}" style="text-decoration:none;color:inherit">
  <div class="doc-card"><span class="icon-badge">{icon("file")}</span><div>
    <p class="doc-meta">PDF</p><h3>{t}</h3><p>{d}</p><span class="link-arrow">Open {icon("arrow")}</span></div></div>
</a>''' for i, (k, t, d) in enumerate(docs))
    body = f'''
{page_hero(B, "Patient information", "Policies &amp; <em>practice</em> information",
               "Useful documents about how we run the practice and look after your information. All documents open as PDFs.",
               "Patient information")}
<section class="section section--tight textured" style="padding-top:0">
  <div class="container container--narrow">
    <div class="notice reveal">
      {icon("leaf")}
      <div>
        <h3>Coughs, colds and respiratory illness</h3>
        <p>If you're feeling unwell with a cough, cold, flu-like symptoms or a high temperature, please don't come to the practice. Call us on <a href="tel:{PHONE_TEL}">{PHONE}</a> and we'll happily rearrange your appointment.</p>
        <p>Face coverings are optional. You're welcome to wear one if you'd prefer.</p>
      </div>
    </div>
  </div>
</section>
<section class="section section--linen">
  <div class="container">
    <div class="section-head reveal"><p class="eyebrow">Documents</p><h2>Downloads</h2></div>
    <div class="grid grid--3">{cards}</div>
  </div>
</section>
'''
    add("patient-info.html", page(B, "patient-info.html", "Patient Information | The Dental House, Worksop",
                                  "Privacy notices, complaints procedure, practice brochure and fee scale for patients of The Dental House, Worksop.",
                                  body))


# ============================================================ LEGAL
def build_legal():
    privacy = f'''
{page_hero(B, "Legal", "Privacy <em>policy</em>", "How The Dental House collects, uses and protects your personal information.", "Privacy policy")}
<section class="section section--white" style="padding-top:clamp(3rem,6vw,4.5rem)">
  <div class="container">
    <div class="prose">
      <!-- [VERIFY] Paste the full privacy policy wording from the current live site here (the new site could not reach the old one). -->
      <div class="notice">{icon("info")}<div><h3>Policy wording to be added {verify()}</h3><p>The full privacy policy text from the previous website will be added here.</p></div></div>
      <h2>Patient privacy notices</h2>
      <p>Our detailed privacy notices explain how we use and protect the information we hold about you as a patient:</p>
      <ul>
        <li><a href="{pdf("privacy")}">Privacy notice for patients (PDF)</a></li>
        <li><a href="{pdf("privacy_children")}">Privacy notice for children (PDF)</a></li>
        <li><a href="{pdf("leaflet")}">Patient leaflet on personal information (PDF)</a></li>
      </ul>
      <h2>Website enquiries</h2>
      <p>If you contact us through this website, we use the details you give us only to respond to your enquiry and arrange your care. Please don't send detailed medical information by email.</p>
      <h2>Contact</h2>
      <p>If you have a question about your personal information, please contact our Practice Manager on <a href="tel:{PHONE_TEL}">{PHONE}</a> or <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
    </div>
  </div>
</section>'''
    add("privacy-policy.html", page(B, "privacy-policy.html", "Privacy Policy | The Dental House, Worksop",
                                    "Privacy policy for The Dental House, Worksop, including our patient privacy notices.", privacy))

    cookie = f'''
{page_hero(B, "Legal", "Cookie <em>policy</em>", "How this website uses cookies, and how to change your preferences.", "Cookie policy")}
<section class="section section--white" style="padding-top:clamp(3rem,6vw,4.5rem)">
  <div class="container">
    <div class="prose">
      <!-- [VERIFY] Paste any additional cookie policy wording from the current live site here. -->
      <p>We use cookies to make this website work and, with your consent, to understand how it is used. You can change or withdraw your consent at any time.</p>
      <p><a class="btn btn--outline" href="javascript:Cookiebot.renew()">Change cookie settings</a></p>
      <h2>Cookies used on this site</h2>
      <!-- Cookiebot automatically lists the cookies in use here. [VERIFY] the declaration script is enabled in your Cookiebot account. -->
      <script id="CookieDeclaration" src="https://consent.cookiebot.com/a1c3f3a2-a95b-4b3c-bea5-ab9f977018f7/cd.js" type="text/javascript" async></script>
    </div>
  </div>
</section>'''
    add("cookie-policy.html", page(B, "cookie-policy.html", "Cookie Policy | The Dental House, Worksop",
                                   "Cookie policy for The Dental House website, and how to change your cookie settings.", cookie))


def build_404():
    base = "/"  # served from any path, so absolute
    body = f'''
<section class="section error-page textured">
  <div class="container container--narrow">
    <p class="big" aria-hidden="true">404</p>
    <h1 class="h2">Sorry, we can't find <em>that page</em></h1>
    <p class="lede" style="margin-inline:auto">It may have moved when we updated our website. Try one of these instead, or give us a call on {PHONE}.</p>
    <div class="btn-row" style="justify-content:center">
      <a class="btn" href="/index.html">{icon("home")}Home page</a>
      <a class="btn btn--outline" href="/treatments.html">Treatments</a>
      <a class="btn btn--outline" href="/contact.html">Contact us</a>
    </div>
  </div>
</section>'''
    add("404.html", page(base, "404.html", "Page Not Found | The Dental House, Worksop",
                         "Sorry, that page could not be found.", body).replace(
        '<meta name="viewport"', '<meta name="robots" content="noindex">\n<meta name="viewport"'))


# ============================================================ EXTRAS
def build_extras():
    pages = ["index.html", "about.html", "treatments.html", "careplans.html", "theteam.html", "new-patients.html",
             "nervous-patients.html", "emergency.html", "fees.html", "contact.html", "patient-info.html",
             "privacy-policy.html", "cookie-policy.html"]
    urls = "\n".join(
        f"  <url><loc>{SITE_URL}/{'' if p == 'index.html' else p}</loc>"
        f"<priority>{'1.0' if p == 'index.html' else '0.5' if 'policy' in p else '0.8'}</priority></url>"
        for p in pages)
    (OUT / "sitemap.xml").write_text(
        f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n')
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n")

    # Logo + favicon
    (OUT / "assets/img/favicon.svg").write_text(
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">'
        '<rect width="32" height="32" rx="8" fill="#1E4D4F"/>'
        '<path d="M7 25.5V14.8L16 7.5l4.6 3.8V8.3h2.8v5.3L25 14.8v10.7" fill="none" stroke="#F7F2EA" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>'
        '<path d="M13.2 25.5v-3.7a2.8 2.8 0 0 1 5.6 0v3.7" fill="none" stroke="#C49A5A" stroke-width="1.8" stroke-linecap="round"/>'
        '</svg>\n')
    (OUT / "assets/img/logo.svg").write_text(
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 330 48" role="img" aria-label="The Dental House">'
        '<path d="M6 42V22.5L22 9.5l8 6.5V10h5v10l3 2.5V42" fill="none" stroke="#1E4D4F" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>'
        '<path d="M17 42v-6.5a5 5 0 0 1 10 0V42" fill="none" stroke="#C49A5A" stroke-width="2" stroke-linecap="round"/>'
        '<text x="54" y="36" font-family="Fraunces, Georgia, \'Times New Roman\', serif" font-size="30" fill="#1F2A2E" letter-spacing="-0.3">the dental <tspan font-style="italic" font-weight="300">house</tspan></text>'
        '</svg>\n')

    # Image README
    rows = "\n".join(f"| `{f}` | {d} | {u} | {a} |" for f, d, u, a in IMAGES)
    team_rows = "\n".join(
        f"| `team-{slug(p)}.jpg` | {p.get('title', '') + ' ' if p.get('title') else ''}{p['first']} {p['last']} |"
        for _, people in TEAM_GROUPS for p in people)
    (OUT / "assets/img/README.md").write_text(f"""# Images for The Dental House website

Drop images into this folder (`assets/img/`) using **exactly** these filenames. Until a file
exists, the site shows a soft gradient placeholder labelled with the expected filename. Once
you add the file, it appears automatically. No code changes are needed.

Tips:
- Save photos as JPG, around 75–80% quality. Aim for under 300 KB each (hero under 450 KB).
- Keep to the ratios below. Images are cropped to fill their frames (`object-fit: cover`).
- Alt text is already in the HTML. If you change what a photo shows, update its `alt` text in the pages too.

## Site images

| File | Size (ratio) | Used on | Alt text in the HTML |
|---|---|---|---|
{rows}

## Team photos (optional)

Square photos, at least **400 × 400**, face centred. They replace the initials monogram automatically.

| File | Person |
|---|---|
{team_rows}

## Already included
- `favicon.svg`: browser tab icon
- `logo.svg`: standalone wordmark for emails, print and documents (uses Georgia if Fraunces isn't installed)
""")


def build_verify_md():
    (OUT / "VERIFY.md").write_text(f"""# To verify before going live

Everything marked **VERIFY** on the site (shown as a dashed yellow tag, `<mark class="verify">`)
or as `[VERIFY]` in an HTML comment is listed here. Search the HTML files for `verify` to find each one.

## Practice details
- [ ] **Phone number.** The site uses **{PHONE}** (from the brief). Stephanie's email signature shows **01909 470597**. Confirm which is the main patient line.
- [ ] **Payment methods.** The site says "cash or card", changed from cheque. Confirm. (fees.html, new-patients.html)
- [ ] **Website address.** The site assumes `{SITE_URL}` (canonical links, sitemap, social tags). Confirm www vs non-www, and that HTTPS is set up on the hosting.
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
""")


def main():
    build_home(); build_about(); build_treatments(); build_careplans(); build_team()
    build_new_patients(); build_nervous(); build_emergency(); build_fees(); build_contact()
    build_patient_info(); build_legal(); build_404()
    OUT.mkdir(exist_ok=True)
    for path, html in PAGES.items():
        (OUT / path).write_text(html)
    build_extras(); build_verify_md()
    print(f"Built {len(PAGES)} pages into {OUT}")


if __name__ == "__main__":
    main()
