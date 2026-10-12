/* The Dental House — main.js (vanilla, no dependencies) */
(function () {
  'use strict';

  var doc = document.documentElement;
  var body = document.body;

  /* ---- Header: solid + blurred once the page scrolls ---- */
  var header = document.querySelector('.site-header');
  if (header) {
    var onScroll = function () {
      header.classList.toggle('is-scrolled', window.scrollY > 24);
    };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  /* ---- Mobile menu overlay ---- */
  var menu = document.getElementById('mobile-menu');
  var openBtn = document.querySelector('[data-menu-open]');
  var closeBtn = document.querySelector('[data-menu-close]');
  var lastFocus = null;

  function focusables() {
    return menu.querySelectorAll('a[href], button:not([disabled])');
  }
  function openMenu() {
    lastFocus = document.activeElement;
    menu.hidden = false;
    // next frame so the fade transition runs
    requestAnimationFrame(function () {
      menu.classList.add('is-open');
      closeBtn.focus(); // only focusable once the overlay is visible
    });
    menu.setAttribute('aria-hidden', 'false');
    openBtn.setAttribute('aria-expanded', 'true');
    body.classList.add('menu-open');
  }
  function closeMenu() {
    menu.classList.remove('is-open');
    menu.setAttribute('aria-hidden', 'true');
    openBtn.setAttribute('aria-expanded', 'false');
    body.classList.remove('menu-open');
    setTimeout(function () { if (!menu.classList.contains('is-open')) menu.hidden = true; }, 400);
    if (lastFocus) lastFocus.focus();
  }
  if (menu && openBtn && closeBtn) {
    openBtn.addEventListener('click', openMenu);
    closeBtn.addEventListener('click', closeMenu);
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && menu.classList.contains('is-open')) closeMenu();
    });
    menu.addEventListener('keydown', function (e) {
      if (e.key !== 'Tab') return;
      var items = focusables();
      var first = items[0], last = items[items.length - 1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    });
    menu.addEventListener('click', function (e) {
      if (e.target.closest('a[href]')) closeMenu();
    });
    window.addEventListener('resize', function () {
      if (window.innerWidth >= 1240 && menu.classList.contains('is-open')) closeMenu();
    });
  }

  /* ---- Scroll reveal ---- */
  var reveals = document.querySelectorAll('.reveal');
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (!('IntersectionObserver' in window) || reduce) {
    reveals.forEach(function (el) { el.classList.add('is-visible'); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          io.unobserve(entry.target);
        }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    reveals.forEach(function (el) { io.observe(el); });
  }

  /* ---- Highlight today's opening hours ---- */
  var today = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat'][new Date().getDay()];
  document.querySelectorAll('.hours tr[data-day="' + today + '"]').forEach(function (row) {
    row.classList.add('is-today');
  });

  /* ---- Current year ---- */
  document.querySelectorAll('[data-year]').forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });

  /* ---- Booking enquiry form: opens the visitor's email app with the details filled in ----
     If you switch to Formspree, change the form's action/method in contact.html and
     delete this block (see the comment above the form). */
  var form = document.getElementById('booking-form');
  if (form && form.getAttribute('action').indexOf('mailto:') === 0) {
    form.addEventListener('submit', function (e) {
      if (!form.checkValidity()) return; // let the browser show its messages
      e.preventDefault();
      var data = new FormData(form);
      var lines = [
        'Name: ' + (data.get('name') || ''),
        'Phone: ' + (data.get('phone') || ''),
        'Email: ' + (data.get('email') || ''),
        'New or existing patient: ' + (data.get('patient') || ''),
        'Reason: ' + (data.get('reason') || ''),
        'Preferred days / times: ' + (data.get('preferred') || ''),
        '',
        (data.get('message') || '')
      ];
      var subject = 'Appointment enquiry from ' + (data.get('name') || 'the website');
      var href = form.getAttribute('action').split('?')[0] +
        '?subject=' + encodeURIComponent(subject) +
        '&body=' + encodeURIComponent(lines.join('\n'));
      window.location.href = href;
      var status = document.getElementById('form-status');
      if (status) {
        status.textContent = 'Your email app should now open with your message ready to send. If nothing happens, please call us on 01909 472477 or email enquiries@thedentalhouse.co.uk.';
      }
    });
  }
})();
