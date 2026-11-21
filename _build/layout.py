"""Shared page shell for dataclinic.com."""
import html, json
from config import *

E = html.escape


def pay_link(kind, src):
    return f"{PAY[kind]}?client_reference_id={PAY_REF}{src}"


def jsonld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False) + "</script>"


ORG = {"@context": "https://schema.org", "@type": "Organization", "name": "Data Clinic Ltd",
       "url": SITE + "/", "logo": SITE + "/img/logo.png",
       "sameAs": [CO_UK + "/"],
       "address": {"@type": "PostalAddress", "streetAddress": "The Pavilions, Bridge Hall Lane",
                   "addressLocality": "Bury", "postalCode": "BL9 7NX", "addressCountry": "GB"},
       "email": SUPPORT_EMAIL, "foundingDate": "2002"}

NAV = [("/", "Home"), ("/hard-drive-recovery-software/", "Hard drive software"),
       ("/memory-card-recovery-software/", "Memory card software"), ("/pricing/", "Pricing"),
       ("/guides/", "Guides"), ("/support/", "Support")]


def page(path, title, desc, body, *, uk_twin=None, schema=(), crumbs=None, noindex=False, active=None):
    """path like '/pricing/'. uk_twin: matching dataclinic.co.uk URL for hreflang en-GB."""
    url = SITE + path
    robots = "noindex,follow" if (noindex or not LAUNCHED) else "index,follow"
    alts = ""
    if uk_twin:
        alts = (f'<link rel="alternate" hreflang="en" href="{url}">\n'
                f'<link rel="alternate" hreflang="en-GB" href="{uk_twin}">\n'
                f'<link rel="alternate" hreflang="x-default" href="{url}">\n')
    blocks = [jsonld(s) for s in schema]
    if crumbs:
        items = [{"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + p}
                 for i, (p, n) in enumerate(crumbs)]
        blocks.append(jsonld({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items}))
    nav = "".join(f'<a href="{h}"{" class=on" if (active or path) == h else ""}>{t}</a>' for h, t in NAV)
    langs = "".join(
        f'<li><a href="/"{" class=cur" if c == "en" else ""}>{n}{"" if c == "en" else " <small>coming soon</small>"}</a></li>'
        for c, n in LANGS)
    uk = (f'<div class="ukbar" id="ukbar" hidden><div class="wrap">In the UK? Our UK site and data recovery lab are at '
          f'<a href="{uk_twin or CO_UK + "/"}">dataclinic.co.uk&nbsp;→</a>'
          f'<button aria-label="Close" onclick="dcCloseUk()">×</button></div></div>')
    bc = ""
    if crumbs and len(crumbs) > 1:
        bc = ('<nav class="crumbs wrap" aria-label="Breadcrumb">' +
              " › ".join(f'<a href="{p}">{E(n)}</a>' for p, n in crumbs[:-1]) +
              f' › <span>{E(crumbs[-1][1])}</span></nav>')
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{url}">
{alts}<meta property="og:type" content="website">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/img/hdd-02-results-screen.jpg">
<link rel="icon" type="image/png" href="/img/favicon-icon.png">
<link rel="stylesheet" href="/site.css">
{chr(10).join(blocks)}
</head>
<body>
{uk}
<header class="hdr"><div class="wrap">
<a class="logo" href="/"><img src="/img/logo.png" alt="Data Clinic" width="163" height="28"><span>Recovery Software</span></a>
<button class="menu-t" aria-label="Menu" onclick="document.querySelector('.nav').classList.toggle('open')">☰</button>
<nav class="nav">{nav}
<div class="lang" id="lang"><button onclick="document.getElementById('lang').classList.toggle('open')" aria-haspopup="true">🌐 English ▾</button><ul>{langs}</ul></div>
<a class="btn sm" href="/download/">Download</a>
</nav></div></header>
{bc}
<main>
{body}
</main>
{FOOTER}
</body></html>
"""


FOOTER = f"""<footer class="ftr"><div class="wrap">
<div class="cols">
<div><img src="/img/logo.png" alt="Data Clinic" width="140" height="24" style="margin-bottom:12px">
<p>Data recovery software from Data Clinic Ltd, a data recovery company working since 2002.</p></div>
<div><h4>Software</h4><a href="/hard-drive-recovery-software/">Recovery for Hard Drives</a><a href="/memory-card-recovery-software/">Recovery for Memory Cards (free)</a><a href="/which-software/">Which one do I need?</a><a href="/pricing/">Pricing</a><a href="/download/">Downloads</a></div>
<div><h4>Help</h4><a href="/guides/">Guides</a><a href="/support/">Support</a><a href="/about/">About Data Clinic</a><a href="{CO_UK}/">UK data recovery lab</a></div>
<div><h4>Legal</h4><a href="/legal/refund-policy/">Refund policy</a><a href="/legal/licence-agreement/">Licence agreement</a><a href="/legal/privacy/">Privacy</a><a href="#" onclick="return dcCookieSettings()">Cookie settings</a></div>
</div>
<div class="legal">© 2026 {COMPANY}. Windows is a trademark of Microsoft Corporation; Mac, APFS and FileVault are trademarks of Apple Inc. Other names are the property of their owners.</div>
</div></footer>
<script>
document.addEventListener('click',e=>{{const l=document.getElementById('lang');if(l&&!l.contains(e.target))l.classList.remove('open')}});
function dcCloseUk(){{try{{localStorage.setItem('dcUkBar','x')}}catch(e){{}}document.getElementById('ukbar').hidden=true}}
(function(){{try{{if(localStorage.getItem('dcUkBar'))return}}catch(e){{}}
var l=(navigator.languages||[navigator.language||'']).join(',');var tz='';try{{tz=Intl.DateTimeFormat().resolvedOptions().timeZone||''}}catch(e){{}}
if(/en-GB/i.test(l)||tz==='Europe/London'){{document.getElementById('ukbar').hidden=false}}}})();
</script>
<div class="ckbar" id="ckbar" hidden role="dialog" aria-label="Cookie choice"><div class="wrap"><p>May we use Google Analytics cookies to see which pages help people? Nothing is set unless you say yes. <a href="/legal/privacy/">Privacy</a></p>
<div class="ckbtns"><button class="btn sm ghost" onclick="dcConsent('n')">No, thanks</button><button class="btn sm" onclick="dcConsent('y')">Yes, that's fine</button></div></div></div>
<script>
window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}
function dcGa(){{if(window.dcGaOn)return;window.dcGaOn=1;var s=document.createElement('script');s.async=1;s.src='https://www.googletagmanager.com/gtag/js?id={GA4_ID}';document.head.appendChild(s);gtag('js',new Date());gtag('config','{GA4_ID}',{{anonymize_ip:true}})}}
function dcConsent(v){{try{{localStorage.setItem('dcCk',v)}}catch(e){{}}document.getElementById('ckbar').hidden=true;if(v==='y')dcGa()}}
function dcCookieSettings(){{document.getElementById('ckbar').hidden=false;return false}}
function dcEv(n,p){{if(window.dcGaOn)gtag('event',n,p||{{}})}}
(function(){{var v=null;try{{v=localStorage.getItem('dcCk')}}catch(e){{}}if(v==='y')dcGa();else if(v!=='n')document.getElementById('ckbar').hidden=false}})();
document.addEventListener('click',function(e){{var a=e.target.closest&&e.target.closest('a');if(!a)return;var h=a.href||'';
if(/\\.exe($|\\?)/i.test(h))dcEv('dc_com_download_click',{{product:/HardDrive/i.test(h)?'hdd':'card',page:location.pathname}});
else if(/buy\\.stripe\\.com/.test(h))dcEv('dc_com_buy_click',{{plan:(/bJe5k/.test(h)?'personal_28d':/dRm6o/.test(h)?'personal_1y':'business_1y'),page:location.pathname}})}});
</script>"""

CUR_NOTE = ('<div class="curnote"><span aria-hidden="true">💱</span><div>Prices are set in pounds sterling (GBP). '
            '<b>At checkout you see the price in your own currency</b>, with any sales tax for your country worked out '
            'automatically. Payment is handled by Stripe.</div></div>')


def dl_hdd(label="Download free for Windows", cls="btn"):
    return f'<a class="{cls}" href="{HDD["installer"]}">{label}</a>'


def dl_card(label="Download free for Windows", cls="btn"):
    return f'<a class="{cls}" href="{CARD["installer"]}">{label}</a>'


NOT_WINDOWS = ('<p class="notwin" hidden>This software runs on a Windows 10 or 11 PC — not on phones, tablets or Macs. '
               'Open this page on your Windows PC to download it, or <button class="linkbtn" onclick="dcCopy(this)">copy the link</button>.</p>'
               '<script>(function(){var u=navigator.userAgent;if(!/Windows/i.test(u)){document.querySelectorAll(".notwin").forEach(e=>e.hidden=false)}})();'
               'function dcCopy(b){try{navigator.clipboard.writeText(location.href);b.textContent="link copied"}catch(e){}}</script>')


def faq_block(qas, heading="Questions"):
    items = "".join(f"<details><summary>{E(q)}</summary><p>{a}</p></details>" for q, a in qas)
    return (f'<section id="faq" class="faq"><div class="wrap narrow"><h2>{heading}</h2>{items}</div></section>')


def faq_schema(qas):
    import re
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q,
         "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", a)}} for q, a in qas]}


def band(title, text, button):
    return f'<section class="band"><div class="wrap"><h2>{title}</h2><p>{text}</p>{button}</div></section>'
