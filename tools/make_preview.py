"""Bundle the built site into ONE self-contained HTML file for offline previewing.

Usage:  python3 tools/build.py && python3 tools/make_preview.py
Output: thedentalhouse-preview.html (double-click to open; no server needed).

This file is for previewing only. Upload the thedentalhouse-site/ folder, not this file.
"""
import base64
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "thedentalhouse-site"
OUT = ROOT / "thedentalhouse-preview.html"

PAGES = ["index", "about", "treatments", "careplans", "theteam", "new-patients", "nervous-patients",
         "emergency", "fees", "contact", "patient-info", "privacy-policy", "cookie-policy"]


def body_of(html):
    cls = re.search(r'<body class="([^"]*)"', html).group(1)
    inner = re.search(r"<body[^>]*>(.*)</body>", html, re.S).group(1)
    inner = re.sub(r"<script\b[^>]*>.*?</script>", "", inner, flags=re.S)  # e.g. Cookiebot declaration
    return cls, inner


def main():
    css = (SITE / "assets/css/styles.css").read_text()
    js = (SITE / "assets/js/main.js").read_text().strip()
    assert js.splitlines()[1].startswith("(function ()") and js.endswith("})();")
    js = js.replace("(function () {", "window.__initSite = function () {", 1)[:-len("})();")] + "};"
    favicon = base64.b64encode((SITE / "assets/img/favicon.svg").read_bytes()).decode()

    # embed the real photos once, as data URIs; pages reference them by name
    imgs = {}
    for f in sorted((SITE / "assets/img").glob("*.jpg")):
        imgs[f.name] = "data:image/jpeg;base64," + base64.b64encode(f.read_bytes()).decode()
    css = css.replace('url("../img/texture-linen.jpg")',
                      f'url("{imgs["texture-linen.jpg"]}")' if "texture-linen.jpg" in imgs else "none")

    pages = {}
    for p in PAGES:
        cls, inner = body_of((SITE / f"{p}.html").read_text())
        title = re.search(r"<title>(.*?)</title>", (SITE / f"{p}.html").read_text()).group(1)
        inner = re.sub(r'src="assets/img/([^"]+)"', r'data-img="\1"', inner)
        inner = inner.replace(' loading="lazy"', '')  # images are embedded, so load them all at once
        pages[p] = {"cls": cls, "title": title, "html": inner}

    templates = "\n".join(
        f'<template id="tpl-{p}" data-cls="{d["cls"]}" data-title="{d["title"]}">{d["html"]}</template>'
        for p, d in pages.items())

    router = """
var IMGS = %s;
window.Cookiebot = { renew: function () { alert('On the live site this opens the Cookiebot cookie settings.'); } };
(function () {
  var pages = %s;
  function render(page, anchor) {
    if (pages.indexOf(page) < 0) page = 'index';
    var tpl = document.getElementById('tpl-' + page);
    document.body.className = tpl.dataset.cls;
    document.title = tpl.dataset.title + ' (preview)';
    document.body.innerHTML = tpl.innerHTML + document.getElementById('preview-chip-tpl').innerHTML;
    document.querySelectorAll('img[data-img]').forEach(function (img) {
      var src = IMGS[img.dataset.img];
      if (src) img.src = src; else img.hidden = true;
    });
    window.__initSite();
    var target = anchor && document.getElementById(anchor);
    if (target) { setTimeout(function () { target.scrollIntoView(); }, 30); } else { window.scrollTo(0, 0); }
  }
  function fromHash() {
    var h = location.hash.replace(/^#\\/?/, '').split('/');
    render(h[0] || 'index', h[1]);
  }
  document.addEventListener('click', function (e) {
    var a = e.target.closest('a[href]');
    if (!a) return;
    var href = a.getAttribute('href');
    if (/^\\/GDPR\\//.test(href)) {
      e.preventDefault();
      alert('This links to an existing PDF on your server:\\n\\n' + decodeURIComponent(href) + '\\n\\nIt will open once the site is uploaded.');
      return;
    }
    var m = href.match(/^\\/?([a-z0-9-]+)\\.html(?:#(.+))?$/);
    if (m) {
      e.preventDefault();
      var next = '#/' + m[1] + (m[2] ? '/' + m[2] : '');
      if (location.hash === next) fromHash(); else location.hash = next;
      return;
    }
    if (href.charAt(0) === '#' && href.length > 1) {
      var el = document.getElementById(href.slice(1));
      if (el) { e.preventDefault(); el.scrollIntoView({ behavior: 'smooth' }); if (el.tabIndex >= 0 || el.id === 'main') el.focus({ preventScroll: true }); }
    }
  });
  document.addEventListener('submit', function (e) {
    // the real form opens the visitor's email app; in the preview just explain that
    if (e.target.id === 'booking-form' && e.target.checkValidity()) {
      e.preventDefault(); e.stopImmediatePropagation();
      var s = document.getElementById('form-status');
      if (s) s.textContent = 'Preview: on the live site this opens your email app with the enquiry filled in, ready to send to enquiries@thedentalhouse.co.uk.';
    }
  }, true);
  window.addEventListener('hashchange', fromHash);
  fromHash();
})();
""" % (json.dumps(imgs), json.dumps(PAGES))

    chip = """<template id="preview-chip-tpl"><div class="preview-chip" role="note">Preview: the map and reviews tab appear once the site is live</div></template>"""
    chip_css = """
.preview-chip { position: fixed; z-index: 95; left: 50%; transform: translateX(-50%); bottom: calc(84px + env(safe-area-inset-bottom));
  background: rgba(31,42,46,.86); color: #fff; font: 600 12px/1.3 var(--font-body); padding: .45rem .9rem; border-radius: 999px;
  pointer-events: none; white-space: nowrap; box-shadow: 0 6px 20px -8px rgba(0,0,0,.5); }
@media (min-width: 768px) { .preview-chip { bottom: 18px; } }
"""

    html = f"""<!doctype html>
<html lang="en-GB" class="js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<title>The Dental House (preview)</title>
<!-- OFFLINE PREVIEW of the new website. Do not upload this file; upload the thedentalhouse-site/ folder. -->
<link rel="icon" href="data:image/svg+xml;base64,{favicon}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300..600;1,9..144,300..500&amp;family=Manrope:wght@400..700&amp;display=swap">
<style>
{css}
{chip_css}
</style>
<!-- each page's content; the router copies one into <body> (kept in <head> so it survives the swap) -->
{templates}
{chip}
</head>
<body>
<script>
{js}
</script>
<script>
{router}
</script>
</body>
</html>
"""
    OUT.write_text(html)
    print(f"Wrote {OUT} ({OUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
