"""Build dataclinic.com into ../dist. Run from src/: python3 build.py"""
import os, shutil, datetime
from config import *
from layout import page, faq_block, faq_schema, band, dl_hdd, dl_card, jsonld, E
import pages
from guides import GUIDES

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "dist")
TODAY = datetime.date.today().isoformat()
shutil.rmtree(OUT, ignore_errors=True)
os.makedirs(OUT)
written = []


def w(path, content, index=True):
    rel = path.strip("/")
    fn = os.path.join(OUT, rel, "index.html") if (path.endswith("/") or path == "") else os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(fn), exist_ok=True)
    open(fn, "w", encoding="utf-8").write(content)
    if index:
        written.append(path)


w("/", pages.HOME)
w("/hard-drive-recovery-software/", pages.HDD_PAGE)
w("/memory-card-recovery-software/", pages.CARD_PAGE)
w("/drive-health-check/", pages.HEALTH_PAGE)
w("/pricing/", pages.PRICING)
w("/which-software/", pages.CHOOSER)
w("/download/", pages.DOWNLOAD)
w("/support/", pages.SUPPORT)
w("/about/", pages.ABOUT)
w("/legal/refund-policy/", pages.REFUND)
w("/legal/licence-agreement/", pages.EULA)
w("/legal/privacy/", pages.PRIVACY)
w("/licence/", pages.LICENCE, index=False)
w("/404.html", pages.NOTFOUND, index=False)

# ---------------- guides
cards = []
for g in GUIDES:
    path = f"/guides/{g['slug']}/"
    prod = g["product"]
    cta = (band("See what's recoverable — free", "Scan and preview for free on Windows 10 or 11. Pay only to save files.", dl_hdd("Download Recovery for Hard Drives"))
           if prod == "hdd" else
           band("Recover your photos — free", "Data Clinic Recovery for Memory Cards. Windows 10 or 11.", dl_card("Download free")))
    side = ('<aside class="side"><div class="sidebox"><h3>Recovery for Hard Drives</h3><p>Free scan and preview. Strictly read-only. Checks drive health first.</p>'
            f'{dl_hdd("Download free", "btn sm")}<p class="small"><a href="/hard-drive-recovery-software/">How it works →</a></p></div></aside>'
            if prod == "hdd" else
            '<aside class="side"><div class="sidebox"><h3>Recovery for Memory Cards</h3><p>Free for SD and microSD cards. No registration.</p>'
            f'{dl_card("Download free", "btn sm")}<p class="small"><a href="/memory-card-recovery-software/">How it works →</a></p></div></aside>')
    article = {"@context": "https://schema.org", "@type": "Article", "headline": g["title"], "description": g["desc"],
               "author": {"@type": "Organization", "name": "Data Clinic Ltd"},
               "publisher": {"@type": "Organization", "name": "Data Clinic Ltd", "logo": {"@type": "ImageObject", "url": SITE + "/img/logo.png"}},
               # Fixed dates per guide (set "published"/"modified" in guides.py); never the build date.
               "datePublished": g.get("published", "2026-11-21"),
               "dateModified": g.get("modified", g.get("published", "2026-11-21")), "mainEntityOfPage": SITE + path}
    body = f"""<article>
<section class="pagehead guidehead"><div class="wrap"><p class="eyebrow blue">Guide</p><h1>{g['h1']}</h1></div></section>
<section class="tight"><div class="wrap guidegrid">
<div class="prose">
<div class="answer-box"><b>Short answer:</b> {g['answer']}</div>
{g['body']}
</div>
{side}
</div></section>
</article>
{faq_block(g['faq'], "Questions")}
{cta}"""
    w(path, page(path, g["title"] + " | Data Clinic", g["desc"], body, uk_twin=g.get("twin"),
                 schema=[article, faq_schema(g["faq"])],
                 crumbs=[("/", "Home"), ("/guides/", "Guides"), (path, g["h1"])], active="/guides/"))
    cards.append(f'<a class="gcard" href="{path}"><h3>{E(g["h1"])}</h3><p>{E(g["desc"])}</p></a>')

w("/guides/", page("/guides/", "Data Recovery Guides — Deleted, Formatted and RAW Drives | Data Clinic",
                   "Step-by-step data recovery guides from a data recovery company: deleted files, formatted and RAW drives, Mac drives on Windows, SSDs, memory cards and failing drives.",
                   f"""<section class="pagehead"><div class="wrap center"><h1>Data recovery guides</h1>
<p class="intro">Written by people who recover data for a living — including when software isn't the answer.</p></div></section>
<section class="tight"><div class="wrap"><div class="ggrid">{''.join(cards)}</div></div></section>""",
                   crumbs=[("/", "Home"), ("/guides/", "Guides")]))

# ---------------- static files
shutil.copytree(os.path.join(os.path.dirname(__file__), "img"), os.path.join(OUT, "img"))
shutil.copy(os.path.join(os.path.dirname(__file__), "site.css"), OUT)
open(os.path.join(OUT, "CNAME"), "w").write("www.dataclinic.com\n")
open(os.path.join(OUT, ".nojekyll"), "w").write("")
open(os.path.join(OUT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nDisallow: /licence/\n\nSitemap: {SITE}/sitemap.xml\n")
urls = "".join(f"<url><loc>{SITE}{p}</loc><lastmod>{TODAY}</lastmod></url>\n" for p in written)
open(os.path.join(OUT, "sitemap.xml"), "w").write(
    f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
llms = f"""# Data Clinic Recovery Software

> Data recovery software for Windows from Data Clinic Ltd, a UK data recovery company working since 2002. Software only on this site; the UK lab is at {CO_UK}/.

## Products
- [{HDD['name']}]({SITE}/hard-drive-recovery-software/): Windows 10/11 (64-bit). Hard drives, SSDs and USB sticks; reads NTFS, exFAT, FAT32 and Mac APFS, HFS+, HFS. Quick scan, deep scan, imaging, SMART health check before scanning, strictly read-only, Ask Rex AI assistant (optional, off by default). Free scan and preview; licences £39.99 (28 days), £69.99 (1 year), £149 (Business, 1 year). Current version {HDD['version']}.
- [{CARD['name']}]({SITE}/memory-card-recovery-software/): free; SD and microSD cards (FAT32/exFAT); deep scan recognises 17 formats. Version {CARD['version']}.

## Honest limits
- Overwritten data cannot be recovered by any software.
- SSDs usually erase deleted files within minutes (TRIM); a quick format on an SSD erases the whole drive.
- Cannot read BitLocker, ReFS, Linux or FAT16 file systems, dynamic disks or RAID needing rebuild; never scans the drive Windows runs from.
- Physically failing drives (clicking, not detected, 0 MB) need a data recovery lab, not software.

## Guides
""" + "".join(f"- [{g['h1']}]({SITE}/guides/{g['slug']}/)\n" for g in GUIDES)
open(os.path.join(OUT, "llms.txt"), "w").write(llms)
print("built", len(written), "indexable pages + licence + 404 →", os.path.abspath(OUT))
