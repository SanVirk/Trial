/* =====================================================================
   West Heath Dental Practice — shared shell + interactions
   Injects topbar, header nav and footer so every page stays consistent.
   ===================================================================== */
(function () {
  "use strict";

  var PHONE_DISPLAY = "0121 475 3545";
  var PHONE_HREF = "tel:01214753545";
  var EMAIL = "info@westheathdental.co.uk";
  var ADDRESS = "181 West Heath Road, Birmingham, B31 3HD";
  var BOOK_HREF = "contact.html#book";

  /* ---- Icon set (inline SVG, stroke style) ---- */
  var I = {
    phone:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/></svg>',
    clock:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
    pin:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/></svg>',
    mail:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg>',
    arrow:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
    chevDown:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="m6 9 6 6 6-6"/></svg>',
    chevL:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="m15 18-6-6 6-6"/></svg>',
    chevR:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="m9 18 6-6-6-6"/></svg>',
    check:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg>',
    plus:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14M5 12h14"/></svg>',
    shield:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/></svg>',
    heart:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.6l-1-1a5.5 5.5 0 0 0-7.8 7.8l1 1L12 21l7.8-7.6 1-1a5.5 5.5 0 0 0 0-7.8z"/></svg>',
    smile:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M8 14s1.5 2 4 2 4-2 4-2"/><path d="M9 9h.01M15 9h.01"/></svg>',
    sparkle:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l1.9 5.1L19 10l-5.1 1.9L12 17l-1.9-5.1L5 10l5.1-1.9L12 3z"/><path d="M19 15l.8 2.2L22 18l-2.2.8L19 21l-.8-2.2L16 18l2.2-.8L19 15z"/></svg>',
    user:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/></svg>',
    users:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="8" r="3.5"/><path d="M2.5 21a6.5 6.5 0 0 1 13 0"/><path d="M16 5.5a3.5 3.5 0 0 1 0 7M22 21a6.5 6.5 0 0 0-4-6"/></svg>',
    tooth:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5.5C10.5 4 8.5 3.2 6.8 4 4.6 5 4 7.6 4 10c0 3 .8 5 1.6 7.6.4 1.3.7 2.9 1.7 2.9 1.2 0 1.2-2 1.6-3.4.3-1.1.6-2.1 1.6-2.1h.99c1 0 1.3 1 1.6 2.1.4 1.4.4 3.4 1.6 3.4 1 0 1.3-1.6 1.7-2.9C18.2 15 19 13 19 10c0-2.4-.6-5-2.8-6-1.7-.8-3.7 0-5.2 1.5"/></svg>',
    crown:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 18h18M3 18 4 7l5 5 3-7 3 7 5-5 1 11"/></svg>',
    align:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="9" width="18" height="6" rx="2"/><path d="M7 9v6M11 9v6M15 9v6"/></svg>',
    implant:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 3h6l-1 4h-4z"/><path d="M10 7c0 2 .5 3 .7 4.5M14 7c0 2-.5 3-.7 4.5"/><path d="M12 11v4M10.5 15h3M11 18h2M11.5 21h1"/></svg>',
    star:'<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l2.95 6.6 7.05.6-5.3 4.7 1.6 7L12 17.8 5.7 21.5l1.6-7L2 9.8l7.05-.6z"/></svg>',
    fb:'<svg viewBox="0 0 24 24" fill="currentColor"><path d="M22 12a10 10 0 1 0-11.56 9.88v-6.99H7.9V12h2.54V9.8c0-2.5 1.49-3.89 3.78-3.89 1.09 0 2.24.2 2.24.2v2.46h-1.26c-1.24 0-1.63.77-1.63 1.56V12h2.78l-.44 2.89h-2.34v6.99A10 10 0 0 0 22 12z"/></svg>',
    ig:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1.2" fill="currentColor" stroke="none"/></svg>',
    google:'<svg viewBox="0 0 24 24" fill="currentColor"><path d="M21.35 11.1H12v3.2h5.35c-.25 1.5-1.7 4.4-5.35 4.4a5.7 5.7 0 0 1 0-11.4c1.62 0 2.72.69 3.35 1.28l2.28-2.2C16.18 4.1 14.32 3.3 12 3.3a8.7 8.7 0 1 0 0 17.4c5.02 0 8.34-3.53 8.34-8.5 0-.57-.06-1-.13-1.4z"/></svg>',
    award:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="5"/><path d="M8.2 12.5 7 22l5-3 5 3-1.2-9.5"/></svg>',
    calendar:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4.5" width="18" height="17" rx="2"/><path d="M3 9h18M8 2.5v4M16 2.5v4"/></svg>',
    leaf:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M11 20A7 7 0 0 1 4 13c0-6 7-9 16-9 0 9-3 16-9 16z"/><path d="M11 20c0-5 2-9 6-12"/></svg>',
    car:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 13l1.5-4.5A2 2 0 0 1 8.4 7h7.2a2 2 0 0 1 1.9 1.5L19 13"/><path d="M4 13h16v4H4z"/><circle cx="7.5" cy="17.5" r="1.5"/><circle cx="16.5" cy="17.5" r="1.5"/></svg>',
    train:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="5" y="3" width="14" height="13" rx="3"/><path d="M5 10h14M9 16l-2 4M15 16l2 4"/><circle cx="9" cy="13" r="0.6" fill="currentColor"/><circle cx="15" cy="13" r="0.6" fill="currentColor"/></svg>'
  };

  /* ---- Nav model ---- */
  var NAV = [
    { label: "Home", href: "index.html", key: "home" },
    { label: "About", key: "about", children: [
      { label: "About the Practice", sub: "Our story & values", href: "about.html" },
      { label: "Meet the Team", sub: "Your dental professionals", href: "team.html" },
      { label: "New Patients", sub: "What to expect on your visit", href: "new-patients.html" }
    ]},
    { label: "Treatments", href: "treatments.html", key: "treatments" },
    { label: "Fees & Finance", href: "fees.html", key: "fees" },
    { label: "Reviews", href: "testimonials.html", key: "testimonials" },
    { label: "Contact", href: "contact.html", key: "contact" }
  ];

  function buildHeader(active) {
    var topbar =
      '<div class="topbar"><div class="container">' +
        '<div class="tb-left">' +
          '<span class="tb-item"><a href="' + PHONE_HREF + '">' + I.phone + ' ' + PHONE_DISPLAY + '</a></span>' +
          '<span class="tb-item hours tb-hide">' + I.clock + ' Mon–Fri · Sat by arrangement</span>' +
          '<span class="tb-item tb-hide">' + I.pin + ' ' + ADDRESS + '</span>' +
        '</div>' +
        '<div class="tb-right">' +
          '<span class="tb-item tb-hide">' + I.mail + ' <a href="mailto:' + EMAIL + '">' + EMAIL + '</a></span>' +
          '<span class="tb-social">' +
            '<a href="https://www.google.com/maps/search/?api=1&query=West+Heath+Dental+Practice+B31+3HD" target="_blank" rel="noopener" aria-label="Find us on Google">' + I.google + '</a>' +
            '<a href="https://www.facebook.com/" target="_blank" rel="noopener" aria-label="Facebook">' + I.fb + '</a>' +
          '</span>' +
        '</div>' +
      '</div></div>';

    var menu = NAV.map(function (item) {
      var isActive = item.key === active ? " active" : "";
      if (item.children) {
        var subActive = item.children.some(function(c){ return c.href === pageFile(); });
        var dd = item.children.map(function (c) {
          return '<a href="' + c.href + '">' + c.label + '<small>' + c.sub + '</small></a>';
        }).join("");
        return '<li class="has-dd' + (isActive || subActive ? " active" : "") + '">' +
          '<a href="' + item.children[0].href + '" aria-haspopup="true">' + item.label + '<span class="caret">' + I.chevDown + '</span></a>' +
          '<div class="dd">' + dd + '</div></li>';
      }
      return '<li class="' + (isActive ? "active" : "") + '"><a href="' + item.href + '">' + item.label + '</a></li>';
    }).join("");

    var header =
      '<header class="site-header"><div class="container"><nav class="nav" aria-label="Primary">' +
        '<a class="brand" href="index.html" aria-label="West Heath Dental Practice — home">' +
          '<img src="assets/img/logo.png" alt="West Heath Dental Practice">' +
        '</a>' +
        '<ul class="nav-menu">' + menu +
          '<li class="menu-cta"><a class="btn btn-primary btn-block" href="' + BOOK_HREF + '">' + I.calendar + ' Book an appointment</a></li>' +
        '</ul>' +
        '<div class="nav-cta">' +
          '<a class="nav-phone" href="' + PHONE_HREF + '">' + I.phone + '<span>' + PHONE_DISPLAY + '</span></a>' +
          '<a class="btn btn-primary" href="' + BOOK_HREF + '">' + I.calendar + ' Book online</a>' +
          '<button class="nav-toggle" aria-label="Open menu" aria-expanded="false"><span></span></button>' +
        '</div>' +
      '</nav></div></header><div class="menu-backdrop"></div>';

    return topbar + header;
  }

  function buildFooter() {
    var quick = [
      ["About the practice", "about.html"], ["Meet the team", "team.html"],
      ["New patients", "new-patients.html"], ["Fees & finance", "fees.html"], ["Patient reviews", "testimonials.html"]
    ];
    var treatments = [
      ["Dental implants", "treatments.html#implants"], ["Invisalign & braces", "treatments.html#orthodontics"],
      ["Teeth whitening", "treatments.html#whitening"], ["Veneers", "treatments.html#veneers"],
      ["Crowns & bridges", "treatments.html#restorative"], ["Hygiene & health", "treatments.html#hygiene"]
    ];
    function links(arr){ return arr.map(function(l){ return '<li><a href="' + l[1] + '">' + l[0] + '</a></li>'; }).join(""); }

    var yr = "©";
    return '<footer class="site-footer"><div class="container">' +
      '<div class="footer-grid">' +
        '<div class="footer-brand">' +
          '<img src="assets/img/logo.png" alt="West Heath Dental Practice">' +
          '<p>An established, family-centred private dental practice in West Heath, Birmingham — inspiring confident, healthy smiles for over four decades.</p>' +
          '<div class="footer-social">' +
            '<a href="https://www.google.com/maps/search/?api=1&query=West+Heath+Dental+Practice+B31+3HD" target="_blank" rel="noopener" aria-label="Google">' + I.google + '</a>' +
            '<a href="https://www.facebook.com/" target="_blank" rel="noopener" aria-label="Facebook">' + I.fb + '</a>' +
            '<a href="https://www.instagram.com/" target="_blank" rel="noopener" aria-label="Instagram">' + I.ig + '</a>' +
          '</div>' +
        '</div>' +
        '<div><h4>Explore</h4><ul class="footer-links">' + links(quick) + '</ul></div>' +
        '<div><h4>Treatments</h4><ul class="footer-links">' + links(treatments) + '</ul></div>' +
        '<div><h4>Get in touch</h4><ul class="footer-contact">' +
          '<li>' + I.pin + '<span>181 West Heath Road,<br>West Heath, Birmingham, B31 3HD</span></li>' +
          '<li>' + I.phone + '<a href="' + PHONE_HREF + '">' + PHONE_DISPLAY + '</a></li>' +
          '<li>' + I.mail + '<a href="mailto:' + EMAIL + '">' + EMAIL + '</a></li>' +
          '<li>' + I.clock + '<span>Mon, Fri 9–5:30 · Tue, Wed 9–6<br>Thu 10–7 · Sat by arrangement</span></li>' +
        '</ul></div>' +
      '</div>' +
      '<div class="footer-bottom">' +
        '<span>' + yr + ' <span id="yr"></span> West Heath Dental Practice. All rights reserved.</span>' +
        '<span class="legal"><a href="#">Privacy Policy</a><a href="#">Complaints</a><a href="#">Regulated by the GDC &amp; CQC</a></span>' +
      '</div>' +
    '</div></footer>';
  }

  function pageFile() {
    var p = location.pathname.split("/").pop();
    return p === "" ? "index.html" : p;
  }

  /* ---- Interactions ---- */
  function wireNav() {
    var header = document.querySelector(".site-header");
    var toggle = document.querySelector(".nav-toggle");
    var backdrop = document.querySelector(".menu-backdrop");

    function closeMenu(){ document.body.classList.remove("menu-open"); if(toggle) toggle.setAttribute("aria-expanded","false"); }
    if (toggle) {
      toggle.addEventListener("click", function () {
        var open = document.body.classList.toggle("menu-open");
        toggle.setAttribute("aria-expanded", open ? "true" : "false");
      });
    }
    if (backdrop) backdrop.addEventListener("click", closeMenu);
    document.querySelectorAll(".nav-menu a").forEach(function (a) {
      a.addEventListener("click", function(){ if (window.innerWidth <= 980) closeMenu(); });
    });
    window.addEventListener("keydown", function(e){ if (e.key === "Escape") closeMenu(); });

    var onScroll = function () {
      if (header) header.classList.toggle("scrolled", window.scrollY > 12);
    };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  function wireReveal() {
    var els = document.querySelectorAll(".reveal");
    if (!els.length) return;
    function revealAll() { els.forEach(function (el) { el.classList.add("in"); }); }
    function inView(el) {
      var r = el.getBoundingClientRect();
      var vh = window.innerHeight || document.documentElement.clientHeight;
      return r.top < vh * 0.96 && r.bottom > 0;
    }
    // Anything already on screen appears straight away (no waiting on the observer).
    els.forEach(function (el) { if (inView(el)) el.classList.add("in"); });

    if (!("IntersectionObserver" in window)) { revealAll(); return; }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); }
      });
    }, { threshold: 0.1, rootMargin: "0px 0px -6% 0px" });
    els.forEach(function (el) { if (!el.classList.contains("in")) io.observe(el); });

    // Failsafe: never leave content hidden if the observer doesn't fire.
    window.addEventListener("load", function () { setTimeout(revealAll, 1400); });
  }

  function wireSlider() {
    document.querySelectorAll("[data-slider]").forEach(function (root) {
      var track = root.querySelector(".ttrack");
      var slides = root.querySelectorAll(".tslide");
      var dotsWrap = root.querySelector(".tdots");
      var prev = root.querySelector("[data-prev]");
      var next = root.querySelector("[data-next]");
      if (!track || !slides.length) return;
      var i = 0, n = slides.length, timer;

      if (dotsWrap) {
        for (var d = 0; d < n; d++) {
          var b = document.createElement("button");
          b.setAttribute("aria-label", "Go to review " + (d + 1));
          b.addEventListener("click", (function (idx) { return function () { go(idx); reset(); }; })(d));
          dotsWrap.appendChild(b);
        }
      }
      function go(idx) {
        i = (idx + n) % n;
        track.style.transform = "translateX(" + (-i * 100) + "%)";
        if (dotsWrap) dotsWrap.querySelectorAll("button").forEach(function (dot, k) { dot.classList.toggle("on", k === i); });
      }
      function reset(){ clearInterval(timer); timer = setInterval(function(){ go(i + 1); }, 6500); }
      if (prev) prev.addEventListener("click", function () { go(i - 1); reset(); });
      if (next) next.addEventListener("click", function () { go(i + 1); reset(); });
      go(0); reset();
      root.addEventListener("mouseenter", function(){ clearInterval(timer); });
      root.addEventListener("mouseleave", reset);
    });
  }

  function wireAccordions() {
    document.querySelectorAll(".accordion").forEach(function (acc) {
      acc.querySelectorAll(".acc-q").forEach(function (q) {
        q.addEventListener("click", function () {
          var item = q.closest(".acc-item");
          var a = item.querySelector(".acc-a");
          var open = item.classList.toggle("open");
          a.style.maxHeight = open ? a.scrollHeight + "px" : 0;
        });
      });
    });
  }

  function wireContactForm() {
    var form = document.getElementById("contact-form");
    if (!form) return;
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var f = form.elements;
      var name = (f.name && f.name.value || "").trim();
      var subject = "Website enquiry" + (name ? " from " + name : "");
      var body =
        "Name: " + (f.name ? f.name.value : "") + "\n" +
        "Phone: " + (f.phone ? f.phone.value : "") + "\n" +
        "Email: " + (f.email ? f.email.value : "") + "\n" +
        "Interested in: " + (f.treatment ? f.treatment.value : "") + "\n\n" +
        "Message:\n" + (f.message ? f.message.value : "");
      var status = document.getElementById("form-status");
      window.location.href = "mailto:" + EMAIL + "?subject=" + encodeURIComponent(subject) + "&body=" + encodeURIComponent(body);
      if (status) {
        status.hidden = false;
        status.textContent = "Opening your email app to send this securely to our reception team. Prefer to talk? Call " + PHONE_DISPLAY + ".";
      }
    });
  }

  function setYear() {
    var y = document.getElementById("yr");
    if (y) y.textContent = String(new Date().getFullYear());
  }

  function wireHours() {
    var today = new Date().getDay();
    document.querySelectorAll(".hours-row[data-day]").forEach(function (row) {
      if (parseInt(row.getAttribute("data-day"), 10) === today) row.classList.add("today");
    });
  }

  /* ---- Boot ---- */
  function init() {
    document.documentElement.classList.add("js");
    var active = document.body.getAttribute("data-page") || pageFile().replace(".html", "") || "home";
    var slot = document.getElementById("site-header-slot");
    if (slot) slot.innerHTML = buildHeader(active);
    var fslot = document.getElementById("site-footer-slot");
    if (fslot) fslot.innerHTML = buildFooter();

    // expose icons for inline use on pages (data-icon="name")
    document.querySelectorAll("[data-icon]").forEach(function (el) {
      var name = el.getAttribute("data-icon");
      if (I[name]) el.innerHTML = I[name];
    });

    wireNav();
    wireReveal();
    wireSlider();
    wireAccordions();
    wireContactForm();
    wireHours();
    setYear();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else { init(); }
})();
