"""Build the dataclinic.com software-site preview (English). Run: python3 build.py"""
import html

DL = "https://www.dataclinic.co.uk/drive-rescue/DataClinic-HardDriveRecovery-Setup-1.1.1.exe"
MCDL = "https://www.dataclinic.co.uk/drive-rescue/DataClinic-MemoryCardRecovery-Setup-1.1.0.exe"
PAY = {"28d": "https://buy.stripe.com/bJe5kCboi4ebdoObaEao800",
       "1y": "https://buy.stripe.com/dRm6oG4ZU9yvgB0fqUao801",
       "biz": "https://buy.stripe.com/14AdR83VQ9yv84u0w0ao802"}
CO_UK = "https://www.dataclinic.co.uk/"
LANGS = [("en", "English"), ("es", "Español"), ("de", "Deutsch"), ("fr", "Français"), ("it", "Italiano"),
         ("pt-br", "Português (Brasil)"), ("nl", "Nederlands"), ("pl", "Polski"), ("tr", "Türkçe"),
         ("ru", "Русский"), ("hi", "हिन्दी"), ("ja", "日本語"), ("zh-cn", "简体中文")]

def head(title, desc, path):
    alts = "\n".join(
        f'<link rel="alternate" hreflang="{c}" href="https://www.dataclinic.com/{"" if c=="en" else c+"/"}{path}">'
        for c, _ in LANGS[:1])
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<!-- Live site: canonical + hreflang. en-GB points UK searchers to the .co.uk twin; x-default = .com -->
<link rel="canonical" href="https://www.dataclinic.com/{path}">
{alts}
<link rel="alternate" hreflang="en-GB" href="https://www.dataclinic.co.uk/data-recovery-software-for-hard-drives/">
<link rel="alternate" hreflang="x-default" href="https://www.dataclinic.com/{path}">
<link rel="icon" href="img/favicon-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&family=Roboto+Condensed:wght@700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="site.css">
</head>
<body>
<div class="pv">Preview — dataclinic.com software site (English). Not live yet. Other languages follow once the English site is approved.</div>
<div class="ukbar" id="ukbar"><div class="wrap">In the UK? Our UK site and data recovery lab are at <a href="{CO_UK}">dataclinic.co.uk&nbsp;→</a><button aria-label="Close" onclick="document.getElementById('ukbar').remove()">×</button></div></div>
"""

def header(active):
    items = [("index.html", "Home"), ("products.html", "Products"),
             ("hard-drive-recovery-software.html#pricing", "Pricing"), ("#", "Guides"), ("#", "Support")]
    nav = "".join(f'<a href="{h}"{" class=on" if t==active else ""}>{t}</a>' for h, t in items)
    langs = "".join(
        f'<li><a href="#"{" class=cur" if c=="en" else ""}>{n}{"" if c=="en" else " <small>coming soon</small>"}</a></li>'
        for c, n in LANGS)
    return f"""<header class="hdr"><div class="wrap">
<a class="logo" href="index.html"><img src="img/logo.png" alt="Data Clinic" width="163" height="28"><span>Recovery Software</span></a>
<button class="menu-t" aria-label="Menu" onclick="document.querySelector('.nav').classList.toggle('open')">☰</button>
<nav class="nav">{nav}
<div class="lang" id="lang"><button onclick="document.getElementById('lang').classList.toggle('open')" aria-haspopup="true">🌐 English ▾</button><ul>{langs}</ul></div>
<a class="btn sm" href="{DL}">Download free</a>
</nav></div></header>
"""

FOOTER = f"""<footer class="ftr"><div class="wrap">
<div class="cols">
<div><img src="img/logo.png" alt="Data Clinic" width="140" height="24" style="margin-bottom:12px">
<p>Professional data recovery software from Data Clinic Ltd — built by a data recovery lab working since 2002.</p></div>
<div><h4>Products</h4><a href="hard-drive-recovery-software.html">Recovery for Hard Drives</a><a href="memory-card-recovery.html">Memory Card Recovery (free)</a><a href="hard-drive-recovery-software.html#pricing">Pricing</a><a href="hard-drive-recovery-software.html#faq">FAQ</a><a href="{DL}">Download</a></div>
<div><h4>Help</h4><a href="#">Guides</a><a href="#">Contact support</a><a href="{CO_UK}">UK data recovery lab</a></div>
<div><h4>Legal</h4><a href="#">Refund policy</a><a href="#">Licence agreement</a><a href="#">Privacy</a></div>
</div>
<div class="legal">© 2026 Data Clinic Ltd · Company no. 04417174 · VAT GB 793061422 · The Pavilions, Bridge Hall Lane, Bury BL9 7NX, United Kingdom · Windows is a trademark of Microsoft Corporation.</div>
</div></footer>
<script>document.addEventListener('click',e=>{{const l=document.getElementById('lang');if(l&&!l.contains(e.target))l.classList.remove('open')}});</script>
</body></html>"""

CUR_NOTE = ('<div class="curnote"><span>💱</span><div>Prices are set in pounds sterling (GBP). <b>At checkout you see the price in '
            'your own currency</b>, with any sales tax for your country worked out automatically. Payment is handled by Stripe.</div></div>')


PRODGRID = f"""<div class="prods">
<a class="prod" href="hard-drive-recovery-software.html"><img src="img/hdd-02-results-screen.jpg" alt="" width="1400" height="724"><div class="pb"><span class="badge">Flagship · from £39.99</span><h3>Recovery for Hard Drives</h3><p>Deleted, formatted and lost files from hard drives, SSDs and USB sticks — with Ask Rex AI, health checks and drive imaging.</p><span class="more">Explore →</span></div></a>
<a class="prod" href="memory-card-recovery.html"><img src="img/mc-device-picker.jpg" alt="" width="1200" height="384"><div class="pb"><span class="badge free">Free</span><h3>Memory Card Recovery</h3><p>Deleted photos and videos from SD and microSD cards — free, no registration, with previews before you save.</p><span class="more">Explore →</span></div></a>
</div>"""

# ---------------- HOME ----------------
home = head("Data Clinic Recovery for Hard Drives — see your lost files before you pay",
            "Recover deleted and lost files from hard drives, SSDs and USB sticks on Windows. Free scan and preview, Ask Rex AI, strictly read-only. From a data recovery lab working since 2002.",
            "") + header("Home") + f"""
<main>
<section class="hero"><div class="wrap grid">
<div>
<div class="rexpill"><b>NEW</b> Ask Rex AI — describe what you've lost in your own words</div>
<p class="eyebrow">Windows data recovery software</p>
<h1>Get your lost files back. <em>See them before you pay.</em></h1>
<p class="lead">Data Clinic Recovery for Hard Drives finds deleted and lost files on hard drives, SSDs and USB sticks. It was written by a data recovery lab, so it knows when to stop — and the scan and preview are free.</p>
<div class="ctas"><a class="btn" href="{DL}">Download free for Windows</a><a class="btn ghost" href="hard-drive-recovery-software.html">How it works</a></div>
<p class="fine">Windows 10/11 (64-bit) · version 1.1.1 · licences from £39.99 — shown in your currency at checkout</p>
</div>
<div class="shot"><img src="img/hdd-02-results-screen.jpg" alt="Scan results with previews, folders and a verdict for every file" width="1400" height="724"></div>
</div></section>
<div class="trust"><div class="wrap"><span>Free scan and preview</span><span>Strictly read-only</span><span>Checks drive health first</span><span>13 languages</span><span>From a lab working since 2002</span></div></div>

<section class="alt"><div class="wrap">
<div class="center"><p class="eyebrow" style="color:var(--blue)">Our software</p><h2>Recovery tools built by a recovery lab</h2>
<p class="intro">Every Data Clinic program is written by engineers who recover data professionally — read-only, honest about the limits, and free to try.</p></div>
{PRODGRID}
</div></section>

<section><div class="wrap">
<div class="center"><p class="eyebrow" style="color:var(--blue)">What it recovers</p><h2>When the drive works but the files are gone</h2>
<p class="intro">Deleted by mistake, formatted, or a drive Windows suddenly can't read — if the drive itself still works, this is where to start.</p></div>
<div class="cards">
<div class="card"><div class="ico">🗑️</div><h3>Deleted files</h3><p>Shift+Delete, an emptied Recycle Bin, a folder gone missing — found with their original names and folders wherever the drive's file tables still list them.</p></div>
<div class="card"><div class="ico">💽</div><h3>Formatted drives</h3><p>A deep scan reads the whole drive and recognises dozens of file types by their content — photos, video, music, documents, email and archives.</p></div>
<div class="card"><div class="ico">⚠️</div><h3>"You need to format the disk"</h3><p>Drives showing as RAW, or with a damaged file system, can usually be read without formatting — and the files copied off safely.</p></div>
<div class="card"><div class="ico">🍎</div><h3>Mac drives on a Windows PC</h3><p>Reads Mac APFS, HFS+ and HFS drives that Windows can't open, and copies the files off — no Mac needed.</p></div>
<div class="card"><div class="ico">🔌</div><h3>External drives and USB sticks</h3><p>External hard drives, SSDs and USB memory sticks, plus internal drives other than the one Windows runs from.</p></div>
<div class="card"><div class="ico">🩺</div><h3>Drives showing early trouble</h3><p>Copy a struggling drive to an image file once, then recover from the copy — so a weak drive isn't read again and again.</p></div>
</div></div></section>

<section class="rex"><div class="wrap split">
<div>
<p class="eyebrow">Ask Rex AI · new in version 1.1</p>
<h2>Just say what you've lost</h2>
<p>Press <b>Ask Rex AI</b> and describe it the way you'd tell a person — <i>"my deleted folder called Dave"</i>, <i>"all my photos from last summer"</i>, <i>"Windows says my drive needs formatting and I'm scared"</i>.</p>
<ul class="ticks">
<li>Rex explains what's probably wrong and proposes a plan — which scan to run and which files to pick.</li>
<li>Nothing starts until you press <b>Yes</b>. Rex never presses anything himself.</li>
<li>The software checks every plan against its own safety rules — a failing drive gets no plan at all.</li>
<li>Off until you turn it on. Your files, their contents and the list of file names are never sent.</li>
</ul>
<p class="note">Free for planning and scanning within a daily limit. Powered by Claude, Anthropic's AI model; not offered where Anthropic's service isn't available.</p>
</div>
<div class="phone"><img src="img/hdd-05-ask-rex-plan.jpg" alt="Ask Rex proposing a plan to recover a deleted folder" width="488" height="882"></div>
</div></section>

<section class="alt"><div class="wrap split rev">
<div class="shot"><img src="img/hdd-03-drive-health-smart.jpg" alt="Drive health check shown before any scan" width="1120" height="430"></div>
<div>
<p class="eyebrow" style="color:var(--blue)">Built by a recovery lab</p>
<h2>Software that knows when to stop</h2>
<p>Most recovery software will happily scan a dying drive until it's beyond saving. Ours was written by the engineers at Data Clinic, a data recovery lab working since 2002 — so it behaves the way they would.</p>
<ul class="ticks">
<li><b>Health check first.</b> It reads the drive's own health report before anything is scanned, and refuses to scan a drive that reports failure.</li>
<li><b>Strictly read-only.</b> It never writes to, repairs or formats the drive it scans, and won't let you save files back onto it.</li>
<li><b>Honest verdicts.</b> Every file shows whether it can really be recovered before you pay — files that are gone are marked as gone.</li>
</ul>
</div>
</div></section>

<section><div class="wrap">
<div class="center"><p class="eyebrow" style="color:var(--blue)">Pricing</p><h2>Scan and preview free. Pay only to recover.</h2>
<p class="intro">Every licence includes everything the software does.</p></div>
<div class="prices">
<div class="price"><h3>Personal — 28 days</h3><div class="amt">£39.99</div><div class="per">One-off. Never renews.</div><a class="btn line" href="hard-drive-recovery-software.html#pricing">See details</a></div>
<div class="price best"><h3>Personal — 1 year</h3><div class="amt">£69.99</div><div class="per">Per year · cancel any time</div><a class="btn" href="hard-drive-recovery-software.html#pricing">See details</a></div>
<div class="price"><h3>Business — 1 year</h3><div class="amt">£149</div><div class="per">Per year · up to 3 PCs · commercial use</div><a class="btn line" href="hard-drive-recovery-software.html#pricing">See details</a></div>
</div>
{CUR_NOTE}
</div></section>

<section class="band"><div class="wrap">
<h2>Find out what's recoverable — free</h2>
<p>Download, scan and preview without paying anything. Windows 10 or 11, 64-bit.</p>
<a class="btn" href="{DL}">Download free</a>
</div></section>
</main>
""" + FOOTER

# ---------------- PRODUCT ----------------
prod = head("Hard Drive & SSD Recovery Software for Windows — Data Clinic",
            "Recover deleted, formatted and lost files from hard drives, SSDs and USB sticks. Free scan and preview, Ask Rex AI, health check, strictly read-only. Licences from £39.99.",
            "hard-drive-recovery-software/") + header("Products") + f"""
<main>
<section class="hero"><div class="wrap grid">
<div>
<p class="eyebrow">Windows software · hard drives, SSDs and USB sticks</p>
<h1>Data Clinic Recovery for Hard Drives</h1>
<p class="lead">Data recovery software, written by data recovery experts. Recover deleted and lost files from hard drives, SSDs and USB memory sticks — with a free scan and preview, so you never pay to find out whether your files are there.</p>
<div class="ctas"><a class="btn" href="{DL}">Download free</a><a class="btn ghost" href="#pricing">See prices</a></div>
<p class="fine">Windows 10/11, 64-bit · needs administrator rights · version 1.1.1 · 13 languages</p>
</div>
<div class="shot"><img src="img/hdd-02-results-screen.jpg" alt="Scan results with previews, filters and folders" width="1400" height="724"></div>
</div></section>
<div class="trust"><div class="wrap"><span>Free scan and preview</span><span>Strictly read-only</span><span>Health check before every scan</span><span>Ask Rex AI</span></div></div>

<section><div class="wrap">
<div class="center"><p class="eyebrow" style="color:var(--blue)">What it does</p><h2>Three ways to get files back</h2></div>
<div class="cards">
<div class="card"><div class="ico">⚡</div><h3>Quick scan</h3><p>Reads the drive's file tables (NTFS, exFAT, FAT32 and Mac APFS, HFS+ and HFS) and brings back any kind of file they still list — with original names and folders, including files emptied from the Recycle Bin.</p></div>
<div class="card"><div class="ico">🔍</div><h3>Deep scan</h3><p>Reads the file tables first, then the whole drive, recognising files by their content — for formatted drives and damaged file tables. It always finds at least what a quick scan finds.</p></div>
<div class="card"><div class="ico">🧬</div><h3>Image a struggling drive</h3><p>Copies a drive showing early trouble to an image file once, so every scan works from the copy. Unreadable sectors are mapped; interrupted images resume. Imaging is free.</p></div>
</div>
<p class="center muted" style="margin-top:26px;font-size:15px">Deep scan finds JPEG, PNG, HEIC, Canon/Nikon/Sony raw, MP4, MOV, MKV, MP3, WAV, PDF, Word, Excel, PowerPoint, Outlook PST/OST, ZIP, RAR and more — and you can add your own file signatures.</p>
</div></section>

<section class="rex"><div class="wrap split">
<div>
<p class="eyebrow">Ask Rex AI</p>
<h2>Tell it what you've lost, in your own words</h2>
<p>A chat panel opens beside the normal screens. Describe what you want back and Rex proposes a plan: which scan to run and which files to pick. Part of a name is enough — <i>"Laurie project"</i> finds <i>"Laurie's Project File.txt"</i>.</p>
<ul class="ticks">
<li><b>Nothing starts until you press Yes</b> — and before you agree, the file list shows exactly which files Rex would tick.</li>
<li><b>Guided to your saved files.</b> Rex names the button to press on each screen and rings it in green. He never presses anything himself.</li>
<li><b>Safety stays in the software.</b> A failing drive gets no plan; a drive with warning signs is imaged first; the drive is never written to.</li>
<li><b>Private by design.</b> Off until you turn it on. Files, file contents and the list of file names are never sent.</li>
</ul>
<p class="note">Free for planning and scanning within a daily limit — recovering files needs a licence. Available in all 13 languages; powered by Claude, Anthropic's AI model, and not offered where Anthropic's service isn't available. AI suggestions can be wrong — which is why the software checks every plan and waits for your Yes.</p>
</div>
<div class="phone"><img src="img/hdd-05-ask-rex-plan.jpg" alt="Rex proposes a plan for a deleted folder" width="488" height="882"></div>
</div></section>

<section class="alt"><div class="wrap">
<div class="center"><p class="eyebrow" style="color:var(--blue)">How it works</p><h2>Four steps. Only the last one costs anything.</h2></div>
<div class="steps">
<div class="step"><h3>Choose drive</h3><p>Install, plug in the drive and choose it. Its health report is checked straight away; a failing drive stops here.</p><span class="tag">Free</span></div>
<div class="step"><h3>Look for files</h3><p>The tool recommends one way to look — usually a quick scan, or imaging first if the drive shows warning signs.</p><span class="tag">Free</span></div>
<div class="step"><h3>Pick files</h3><p>Browse with thumbnail previews, folders and filters. Files that can't be recovered are hidden by default.</p><span class="tag">Free</span></div>
<div class="step"><h3>Save files</h3><p>Choose another drive to save to. Enter your licence key here — and only here.</p><span class="tag pay">Licence needed</span></div>
</div>
<div class="split" style="margin-top:56px">
<div class="shot"><img src="img/hdd-01-drive-picker.jpg" alt="The drive picker only lists drives that can safely be read" width="925" height="511"></div>
<div><h3>It can't touch the wrong drive</h3><p class="muted">The picker only lists drives that can safely be read. The drive Windows runs from never appears, so it can never be scanned or changed — and recovered files can only be saved to a different drive. Enforced, not just advised.</p></div>
</div>
</div></section>

<section id="pricing"><div class="wrap">
<div class="center"><p class="eyebrow" style="color:var(--blue)">Pricing</p><h2>One feature set. Choose how long you need it.</h2>
<p class="intro">Every licence includes everything above. Scan and preview are free — you only pay to recover. Your licence key arrives by email straight after payment.</p></div>
<div class="prices">
<div class="price"><h3>Personal — 28 days</h3><div class="amt">£39.99</div><div class="per">One-off. Never renews.</div>
<ul><li>A single recovery job on your own drives</li><li>Everything the tool does</li><li>14-day refund window</li></ul>
<a class="btn line" href="{PAY['28d']}">Buy — £39.99</a></div>
<div class="price best"><h3>Personal — 1 year</h3><div class="amt">£69.99</div><div class="per">Renews yearly · we email before it does · cancel any time</div>
<ul><li>Your own drives, all year</li><li>Everything the tool does</li><li>30-day refund window</li><li>A year costs less than two 28-day licences</li></ul>
<a class="btn" href="{PAY['1y']}">Buy — £69.99</a></div>
<div class="price"><h3>Business — 1 year</h3><div class="amt">£149</div><div class="per">Renews yearly · cancel any time</div>
<ul><li>PC repair shops and IT support</li><li>Commercial use, up to 3 PCs at one business</li><li>Your business name on the job report</li><li>30-day refund window</li></ul>
<a class="btn line" href="{PAY['biz']}">Buy — £149</a></div>
</div>
{CUR_NOTE}
<p class="center muted" style="font-size:14px;margin-top:14px">Secure checkout by Stripe. Licences are sold through Onelink ("Link"), Stripe's merchant-of-record service, which handles payment, tax and receipts.</p>
</div></section>

<section class="alt"><div class="wrap">
<div class="center"><p class="eyebrow" style="color:var(--blue)">Honest about the limits</p><h2>What no software can do</h2></div>
<div class="limits">
<div class="limit"><h3>Overwritten data is gone</h3><p>When a drive has re-used the space a deleted file occupied, no software can bring it back. This tool tells you, file by file, rather than selling false hope.</p></div>
<div class="limit"><h3>SSDs erase deleted files</h3><p>On an SSD, deleted files are usually erased by the drive itself within minutes (TRIM), and a quick format erases the whole drive. The tool marks such files "erased by the drive".</p></div>
<div class="limit"><h3>Encryption needs its keys</h3><p>Windows EFS files come back unreadable without the original account's key. FileVault-encrypted Mac volumes are named but cannot be read.</p></div>
<div class="limit"><h3>A failing drive needs a lab</h3><p>Clicking, not detected, or a health report that says failing — that's a job for a professional lab, not software. The tool says so and stops. <a href="{CO_UK}">Our lab is in the UK →</a></p></div>
</div>
</div></section>

<section id="faq" class="faq"><div class="wrap" style="max-width:860px">
<div class="center"><p class="eyebrow" style="color:var(--blue)">FAQ</p><h2>Questions</h2></div>
<details><summary>Is the scan really free?</summary><p>Yes. Choosing the drive, scanning, imaging, previewing files, the job report and CSV export are all free. You only need a licence at the final step, to save recovered files.</p></details>
<details><summary>What currency will I pay in?</summary><p>Prices are set in pounds sterling, but checkout shows the price in your own currency, with any sales tax for your country worked out automatically.</p></details>
<details><summary>Does it work on a Mac?</summary><p>The software runs on Windows 10 and 11 (64-bit). It can read drives formatted on a Mac (APFS, HFS+ and HFS) once they're plugged into a Windows PC.</p></details>
<details><summary>Can it recover files from the drive Windows runs from?</summary><p>No. To keep that drive safe, it never appears in the drive list. To recover from it, take the drive out and connect it to another Windows PC.</p></details>
<details><summary>Which languages?</summary><p>13: English, Spanish, German, French, Italian, Portuguese (Brazil), Dutch, Polish, Turkish, Russian, Hindi, Japanese and Chinese (Simplified). Job reports are in English.</p></details>
<details><summary>What does Ask Rex send over the internet?</summary><p>Only what you type to Rex and what Rex needs to plan — never your files, their contents or the list of file names. Ask Rex is off until you turn it on.</p></details>
<details><summary>My drive is clicking or isn't detected. Will this help?</summary><p>No — those are physical faults, and running any software on the drive can make things worse. Stop using it and take it to a professional data recovery lab.</p></details>
</div></section>

<section class="band"><div class="wrap">
<h2>See what's recoverable — before you pay</h2>
<p>Free download for Windows 10 and 11. Version 1.1.1.</p>
<a class="btn" href="{DL}">Download free</a>
</div></section>
</main>
""" + FOOTER


# ---------------- PRODUCTS HUB ----------------
hub = head("Data recovery software for Windows — Data Clinic",
           "Data recovery software built by a data recovery lab: Recovery for Hard Drives and free Memory Card Recovery. Read-only, honest previews, free to try.",
           "software/") + header("Products") + f"""
<main>
<section class="hero" style="padding:56px 0 48px"><div class="wrap">
<p class="eyebrow">Products</p><h1>Data recovery software, from a data recovery lab</h1>
<p class="lead">Choose by what you've lost it from. Every program scans and previews for free, never writes to the drive it's recovering, and tells you honestly when a job needs a lab instead.</p>
</div></section>
<section><div class="wrap">{PRODGRID}
<div class="curnote" style="max-width:none;margin-top:30px"><span>🧭</span><div><b>Not sure which?</b> Memory cards from cameras and phones → Memory Card Recovery (free). Hard drives, SSDs, USB sticks and Mac drives → Recovery for Hard Drives. A drive that clicks, isn't detected or shows 0&nbsp;MB is a physical fault — no software can fix it.</div></div>
</div></section>
</main>
""" + FOOTER

# ---------------- MEMORY CARD ----------------
mc = head("Free Memory Card Recovery Software for SD & microSD — Data Clinic",
          "Recover deleted photos and videos from SD and microSD cards, free. Quick and deep scan, previews before you save, strictly read-only. Windows 10/11.",
          "memory-card-recovery/") + header("Products") + f"""
<main>
<section class="hero"><div class="wrap grid">
<div>
<p class="eyebrow">Free · Windows 10/11 · SD and microSD cards</p>
<h1>Lost photos or videos from a memory card? <em>Get them back — free.</em></h1>
<p class="lead">Data Clinic Memory Card Recovery finds deleted photos, videos and other camera files on SD and microSD cards. No registration, no catches — see exactly what's recoverable before you save anything.</p>
<div class="ctas"><a class="btn" href="{MCDL}">Free download — 59 MB</a><a class="btn ghost" href="#how">How it works</a></div>
<p class="fine">Windows 10/11 (64-bit) · version 1.1.0 · digitally signed by Data Clinic Ltd</p>
</div>
<div class="shot"><img src="img/mc-device-picker.jpg" alt="Only removable memory cards are listed" width="1200" height="384"></div>
</div></section>
<div class="trust"><div class="wrap"><span>100% free</span><span>No registration</span><span>Strictly read-only</span><span>Honest previews</span></div></div>

<section id="how"><div class="wrap">
<div class="center"><p class="eyebrow" style="color:var(--blue)">How it works</p><h2>Plug in. Scan. Preview and recover.</h2></div>
<div class="cards">
<div class="card"><div class="ico">🔌</div><h3>Plug in</h3><p>Connect the card to your Windows PC. Only removable media shows up — your PC's own drives are never touched.</p></div>
<div class="card"><div class="ico">🔍</div><h3>Scan</h3><p>A quick scan for recently deleted files, or a deep scan for a formatted card or a damaged file table. Always read-only.</p></div>
<div class="card"><div class="ico">🖼️</div><h3>Preview and recover</h3><p>See thumbnails of your photos and videos first, then save the ones you want to a different drive.</p></div>
</div></div></section>

<section class="alt"><div class="wrap split">
<div>
<p class="eyebrow" style="color:var(--blue)">What it recovers</p>
<h2>Built for camera memory cards</h2>
<p><b>Quick scan</b> reads the card's file table and brings back deleted files of any type, with their original names and folders.</p>
<p><b>Deep scan</b> searches the whole card for 17 formats: JPEG, PNG, GIF, TIFF, HEIC · Canon CR2/CR3, Nikon NEF, Sony ARW, Adobe DNG · MP4, MOV, AVI · MP3, WAV · PDF and Word. Files found this way come back without their original names.</p>
<p class="muted">Every deep-scanned photo is checked all the way through: damaged photos are marked as damaged and shown as they'll actually be saved — never as a clean thumbnail.</p>
</div>
<div class="limits" style="grid-template-columns:1fr">
<div class="limit"><h3>Overwritten files are gone</h3><p>Stop using the card straight away — every new photo can overwrite one you want back.</p></div>
<div class="limit"><h3>Memory cards only</h3><p>For USB sticks, hard drives and SSDs, use <a href="hard-drive-recovery-software.html">Recovery for Hard Drives</a>.</p></div>
<div class="limit"><h3>0 MB or not detected?</h3><p>That's a physical fault — no software can repair it. Stop trying more tools and take it to a recovery lab.</p></div>
</div>
</div></section>

<section class="band"><div class="wrap">
<h2>Get your photos back — free</h2><p>Windows 10 or 11, 64-bit. No registration.</p>
<a class="btn" href="{MCDL}">Free download</a>
</div></section>
</main>
""" + FOOTER
open("products.html","w").write(hub)
open("memory-card-recovery.html","w").write(mc)

open("index.html", "w").write(home)
open("hard-drive-recovery-software.html", "w").write(prod)
print("built", len(home), len(prod))
