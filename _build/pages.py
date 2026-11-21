"""Core pages for dataclinic.com (English)."""
from layout import *

H = HDD
LAB_NOTE = (f'Data Clinic\'s own lab is in the UK (<a href="{CO_UK}/">dataclinic.co.uk</a>). '
            'Elsewhere, take the drive to a professional data recovery lab near you — and stop using it until then.')

HDD_APP = {"@context": "https://schema.org", "@type": "SoftwareApplication", "name": H["name"],
           "operatingSystem": "Windows 10, Windows 11 (64-bit)", "applicationCategory": "UtilitiesApplication",
           "softwareVersion": H["version"], "downloadUrl": H["installer"], "fileSize": H["size"],
           "url": SITE + "/hard-drive-recovery-software/", "image": SITE + "/img/hdd-02-results-screen.jpg",
           "publisher": {"@type": "Organization", "name": "Data Clinic Ltd"},
           "offers": [{"@type": "Offer", "name": n, "price": p, "priceCurrency": "GBP", "url": SITE + "/pricing/"}
                      for n, p in [("Free scan and preview", "0"), ("Personal licence, 28 days", "39.99"),
                                   ("Personal licence, 1 year", "69.99"), ("Business licence, 1 year", "149")]],
           "featureList": ["Quick scan with original names and folders", "Deep scan by file content",
                           "Imaging of struggling drives", "Drive health (SMART) check before scanning",
                           "Reads Mac APFS, HFS+ and HFS drives on Windows", "Ask Rex AI assistant",
                           "Strictly read-only"]}
CARD_APP = {"@context": "https://schema.org", "@type": "SoftwareApplication", "name": CARD["name"],
            "operatingSystem": "Windows 10, Windows 11 (64-bit)", "applicationCategory": "UtilitiesApplication",
            "softwareVersion": CARD["version"], "downloadUrl": CARD["installer"], "fileSize": CARD["size"],
            "url": SITE + "/memory-card-recovery-software/", "isAccessibleForFree": True,
            "publisher": {"@type": "Organization", "name": "Data Clinic Ltd"},
            "offers": {"@type": "Offer", "price": "0", "priceCurrency": "GBP"}}

PRICE_CARDS = lambda src: f"""<div class="prices">
<div class="price"><h3>Personal — 28 days</h3><div class="amt">£39.99</div><div class="per">One-off. Never renews.</div>
<ul><li>A single recovery job on your own drives</li><li>Everything the software does</li><li>Changed your mind? Refund within 14 days</li></ul>
<a class="btn line" href="{pay_link('personal_28d', src)}">Buy — £39.99</a></div>
<div class="price best"><h3>Personal — 1 year</h3><div class="amt">£69.99</div><div class="per">Renews yearly · we email you before it does · cancel any time</div>
<ul><li>Your own drives, all year</li><li>Everything the software does</li><li>Recovery promise: 30 days</li><li>Costs less than two 28-day licences</li></ul>
<a class="btn" href="{pay_link('personal_1y', src)}">Buy — £69.99</a></div>
<div class="price"><h3>Business — 1 year</h3><div class="amt">£149</div><div class="per">Renews yearly · we email you before it does · cancel any time</div>
<ul><li>PC repair shops, IT support and other businesses</li><li>Commercial use on customers' drives</li><li>Up to 3 PCs at one business</li><li>Your business name on the job report</li></ul>
<a class="btn line" href="{pay_link('business_1y', src)}">Buy — £149</a></div>
</div>"""

# ---------------------------------------------------------------- HOME
HOME = page("/", "Data Recovery Software for Windows — See Your Files Before You Pay | Data Clinic",
            "Recover deleted, formatted and lost files from hard drives, SSDs, USB sticks and memory cards. Free scan and preview, Ask Rex AI, strictly read-only. From a data recovery company working since 2002.",
            f"""
<section class="hero"><div class="wrap grid">
<div>
<div class="rexpill"><b>NEW</b> Ask Rex AI — describe what you've lost in your own words</div>
<p class="eyebrow">Data recovery software for Windows</p>
<h1>Get your lost files back. <em>See them before you pay.</em></h1>
<p class="lead">Data recovery software written by a data recovery company. It finds deleted and lost files on hard drives, SSDs, USB sticks and memory cards — and it knows when a drive needs more than software.</p>
<div class="ctas">{dl_hdd()}<a class="btn ghost" href="/which-software/">Which software do I need?</a></div>
<p class="fine">Windows 10/11 (64-bit) · free scan and preview · licences from £39.99, shown in your currency at checkout</p>
{NOT_WINDOWS}
</div>
<div class="shot"><img src="/img/hdd-02-results-screen.jpg" alt="Scan results with previews, folders and an honest verdict for every file" width="1400" height="724" fetchpriority="high"></div>
</div></section>
<div class="trust"><div class="wrap"><span>Free scan and preview</span><span>Strictly read-only</span><span>Checks drive health first</span><span>13 languages</span><span>Since 2002</span></div></div>

<section><div class="wrap">
<div class="center"><p class="eyebrow blue">Our software</p><h2>Two tools, each built for its job</h2></div>
<div class="prods">
<a class="prod" href="/hard-drive-recovery-software/"><img src="/img/hdd-01-drive-picker.jpg" alt="" width="925" height="511" loading="lazy">
<div><h3>Recovery for Hard Drives</h3><p>Hard drives, SSDs and USB memory sticks — deleted files, formatted drives, RAW drives and Mac drives on Windows. Ask Rex AI built in.</p>
<span class="pill">Free scan · licences from £39.99</span></div></a>
<a class="prod" href="/memory-card-recovery-software/"><img src="/img/mc-device-picker.jpg" alt="" width="980" height="380" loading="lazy" style="object-fit:contain;background:#f5f7fa">
<div><h3>Recovery for Memory Cards</h3><p>SD and microSD cards from cameras, drones and phones — deleted and formatted photos and videos.</p>
<span class="pill free">Completely free</span></div></a>
</div>
<p class="center muted small">Not sure? <a href="/which-software/">Answer two questions</a> and we'll point you to the right one.</p>
</div></section>

<section class="alt"><div class="wrap">
<div class="center"><p class="eyebrow blue">What it recovers</p><h2>When the drive works but the files are gone</h2>
<p class="intro">Deleted by mistake, formatted, or a drive Windows suddenly can't read — if the drive itself still works, this is where to start.</p></div>
<div class="cards">
<div class="card"><div class="ico">🗑️</div><h3>Deleted files</h3><p>Shift+Delete, an emptied Recycle Bin, a folder gone missing — found with original names and folders wherever the drive's file tables still list them.</p><a href="/guides/recover-deleted-files-recycle-bin/">Guide →</a></div>
<div class="card"><div class="ico">💽</div><h3>Formatted drives</h3><p>A deep scan reads the whole drive and recognises dozens of file types by their content — photos, video, music, documents, email and archives.</p><a href="/guides/recover-formatted-hard-drive/">Guide →</a></div>
<div class="card"><div class="ico">⚠️</div><h3>"You need to format the disk"</h3><p>Drives showing as RAW, or with a damaged file system, can usually be read without formatting — and the files copied off safely.</p><a href="/guides/you-need-to-format-the-disk/">Guide →</a></div>
<div class="card"><div class="ico">🍎</div><h3>Mac drives on Windows</h3><p>Reads Mac APFS, HFS+ and HFS drives that Windows can't open, and copies the files off — no Mac needed.</p><a href="/guides/read-mac-drive-on-windows/">Guide →</a></div>
<div class="card"><div class="ico">🔌</div><h3>External drives and USB sticks</h3><p>External hard drives, SSDs and USB memory sticks, plus internal drives other than the one Windows runs from.</p><a href="/guides/recover-deleted-files-external-hard-drive/">Guide →</a></div>
<div class="card"><div class="ico">📷</div><h3>Memory cards</h3><p>Deleted or formatted photos and videos on SD and microSD cards — with our free memory card tool.</p><a href="/guides/recover-deleted-photos-sd-card/">Guide →</a></div>
</div></div></section>

<section class="rex"><div class="wrap split">
<div>
<p class="eyebrow">Ask Rex AI · in Recovery for Hard Drives</p>
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
<div class="phone"><img src="/img/hdd-05-ask-rex-plan.jpg" alt="Ask Rex proposing a plan to recover a deleted folder" width="488" height="882" loading="lazy"></div>
</div></section>

<section><div class="wrap split rev">
<div class="shot"><img src="/img/hdd-03-drive-health-smart.jpg" alt="Drive health check shown before any scan" width="1120" height="430" loading="lazy"></div>
<div>
<p class="eyebrow blue">Written by a data recovery company</p>
<h2>Software that knows when to stop</h2>
<p>Most recovery software will happily scan a dying drive until it's beyond saving. Ours was written by the engineers at Data Clinic, who have recovered data from failed drives since 2002 — so it behaves the way they would.</p>
<ul class="ticks">
<li><b>Health check first.</b> It reads the drive's own health report before anything is scanned, and refuses to scan a drive that reports failure.</li>
<li><b>Strictly read-only.</b> It never writes to, repairs or formats the drive it scans, and won't let you save files back onto it.</li>
<li><b>Honest verdicts.</b> Every file shows whether it can really be recovered before you pay — files that are gone are marked as gone.</li>
</ul>
</div>
</div></section>

<section class="alt"><div class="wrap">
<div class="center"><p class="eyebrow blue">Pricing</p><h2>Scan and preview free. Pay only to recover.</h2>
<p class="intro">Every Recovery for Hard Drives licence includes everything the software does. The memory card tool is free.</p></div>
{PRICE_CARDS('home')}
{CUR_NOTE}
</div></section>

<section><div class="wrap">
<div class="center"><p class="eyebrow blue">Guides</p><h2>Start with the right guide</h2></div>
<ul class="glist">
<li><a href="/guides/recover-deleted-files-recycle-bin/">Recover files deleted from the Recycle Bin or with Shift+Delete</a></li>
<li><a href="/guides/recover-formatted-hard-drive/">Recover files from a formatted hard drive</a></li>
<li><a href="/guides/drive-shows-raw/">Drive showing as RAW? Get your files back without formatting</a></li>
<li><a href="/guides/is-my-hard-drive-failing/">Is my hard drive failing? The signs, and when to stop</a></li>
<li><a href="/guides/ssd-deleted-files-trim/">Can deleted files be recovered from an SSD?</a></li>
<li><a href="/guides/">All guides →</a></li>
</ul>
</div></section>
{band("Find out what's recoverable — free", "Download, scan and preview without paying anything. Windows 10 or 11, 64-bit.", dl_hdd("Download free"))}
""", schema=[ORG, {"@context": "https://schema.org", "@type": "WebSite", "name": "Data Clinic Recovery Software", "url": SITE + "/"}])

# ---------------------------------------------------------------- HDD PRODUCT
HDD_FAQ = [
    ("Is the scan really free?", "Yes. Choosing the drive, scanning, imaging, previewing files, the job report and CSV export are all free. You only need a licence at the final step, to save recovered files."),
    ("Can this software damage my drive or make things worse?", "No. It opens the drive strictly read-only and never writes to, repairs or formats it. The one caution: if a drive is physically failing, any reading — by any software — makes the failing hardware work. That's why it checks the drive's own health report before every scan, and stops and tells you when it sees failure symptoms."),
    ("What's the difference between a quick scan and a deep scan?", "A quick scan reads the drive's file tables — fast, with names and folders. A deep scan does the same first, then reads every sector and finds files by their content, even after a format, so it always finds at least what a quick scan finds. Files found only by content come back with numbered names like Rescued_0001.jpg in a [Found by content] folder. On a large drive a deep scan takes hours; you can stop at any time and keep what has been found."),
    ("When should I use “Image the drive first”?", "Whenever a drive shows any sign of trouble — read errors, slow patches, a caution on its health report. The software reads every sector once and saves an exact copy to a file on another drive; scans then work from the copy, so the drive isn't read again and again. Imaging is free. A drive whose health report says it is failing is not imaged — that's a job for a lab."),
    ("Does it work on SSDs?", "It scans them, with one honest limit: most SSDs erase deleted data themselves within minutes (TRIM), and a quick format on an SSD erases the whole drive, so deleted and formatted files are usually gone for good. The software checks each deleted file and marks any the drive has erased. Files lost to a damaged file table can still be found."),
    ("Does it read Mac drives?", "Yes — APFS, HFS+ and HFS, on Windows, including files the Mac had deleted where an old copy of the file table survives (APFS and HFS+). FileVault-encrypted volumes are identified but cannot be read; APFS Fusion Drives need a lab. The software itself runs on Windows only."),
    ("Can it recover files from the drive Windows runs from?", "No. To keep that drive safe, it never appears in the drive list. To recover from it, take the drive out and connect it to another Windows PC, where it shows up like any other drive."),
    (f"What won't version {H['version']} do?", "It can't read BitLocker-encrypted drives, Windows dynamic disks (spanned or striped volumes), RAID arrays that need rebuilding from their member disks, or ReFS, Linux and FAT16 file systems. Recovered files are dated the day you recover them, not their original date. The deep scan doesn't find Fujifilm, Olympus or Panasonic raw files. The program needs administrator rights each time it starts, and the licence key is saved per Windows user."),
    ("Why might a recovered video not play?", "Videos are big, so drives often store them in fragments. A deep scan finds a video's start but can't always reassemble scattered pieces, so a recovered video may be incomplete. That's a limit of how drives store data, not something more scanning can fix."),
    ("What does Ask Rex send over the internet?", "Ask Rex is off until you turn it on. When you use it, what you type and basic job details (such as the drive's size and health and how many files were found) go through Data Clinic's server to Anthropic, the provider of the Claude AI model behind Rex. Your files, their contents and the list of file names are never sent; a file or folder name is sent only if you type it. Please don't type passwords or personal details into it."),
    ("What does the software send over the internet?", "Only what you choose to send — a problem report from the Help menu, or a contact request from the failure screen — plus two small automatic checks when it starts online: whether a newer version is available (nothing about you or your drives), and, if a licence key is entered, the key and version to check whether it has been renewed or refunded. And, if you turn it on, Ask Rex as described above. It never sends the contents of your files. See the <a href=\"/legal/privacy/\">privacy policy</a>."),
    ("Do I need to be online?", "No. The licence key is verified on your PC. You need to be online only to buy — and, for a yearly licence, the program picks up your renewed key by itself the next time it starts online."),
    ("Which languages?", "13: English, Spanish, German, French, Italian, Portuguese (Brazil), Dutch, Polish, Turkish, Russian, Hindi, Japanese and Chinese (Simplified). The software follows your Windows display language; change it in Help → Language. Job reports are in English."),
    ("My drive is clicking or isn't detected. Will this help?", "No — those are physical faults, and running any software on the drive can make things worse. Stop using it and take it to a professional data recovery lab. " + LAB_NOTE),
]

HDD_PAGE = page("/hard-drive-recovery-software/", "Hard Drive & SSD Recovery Software for Windows | Data Clinic",
                "Recover deleted, formatted and lost files from hard drives, SSDs and USB sticks on Windows. Free scan and preview, Ask Rex AI, drive health check, strictly read-only. Licences from £39.99.",
                f"""
<section class="hero"><div class="wrap grid">
<div>
<p class="eyebrow">Windows software · hard drives, SSDs and USB sticks</p>
<h1>Data Clinic Recovery for Hard Drives</h1>
<p class="lead">Recover deleted and lost files from hard drives, SSDs and USB memory sticks — with a free scan and preview, so you never pay to find out whether your files are there.</p>
<div class="ctas">{dl_hdd("Download free")}<a class="btn ghost" href="/pricing/">See prices</a></div>
<p class="fine">Windows 10/11, 64-bit · needs administrator rights · version {H['version']} · 13 languages</p>
{NOT_WINDOWS}
</div>
<div class="shot"><img src="/img/hdd-02-results-screen.jpg" alt="Scan results with previews, filters and folders" width="1400" height="724" fetchpriority="high"></div>
</div></section>
<div class="trust"><div class="wrap"><span>Free scan and preview</span><span>Strictly read-only</span><span>Health check before every scan</span><span>Ask Rex AI</span></div></div>

<section><div class="wrap">
<div class="center"><p class="eyebrow blue">What it does</p><h2>Three ways to get files back</h2>
<p class="intro">It recovers from external USB drives and sticks, and from internal drives other than the one Windows runs from.</p></div>
<div class="cards">
<div class="card"><div class="ico">⚡</div><h3>Quick scan</h3><p>Reads the drive's file tables (NTFS, exFAT, FAT32 and Mac APFS, HFS+ and HFS) and brings back any kind of file they still list — documents, email, photos, video, project files — with original names and folders, including files emptied from the Recycle Bin.</p></div>
<div class="card"><div class="ico">🔍</div><h3>Deep scan</h3><p>Reads the file tables first, then the whole drive, recognising files by their content — for formatted drives and damaged file tables. It always finds at least what a quick scan finds.</p></div>
<div class="card"><div class="ico">🧬</div><h3>Image a struggling drive</h3><p>Copies a drive showing early trouble to an image file once, so every scan works from the copy. Unreadable sectors are mapped; interrupted images resume. Imaging is free.</p></div>
</div>
<p class="center muted small" style="margin-top:26px">Deep scan recognises JPEG, PNG, GIF, TIFF, BMP, WebP, Photoshop, HEIC, Canon, Nikon, Sony and Adobe DNG raw, MP4, MOV, AVI, MKV/WebM, WMV, MP3, WAV, FLAC, M4A, WMA, Ogg/Opus, PDF, Word, Excel, PowerPoint, OpenDocument, Outlook PST/OST and MSG, ZIP, RAR, 7-Zip and ISO — and you can add signatures for your own file types.</p>
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
<p class="note">Free for planning and scanning within a daily limit — recovering files needs a licence. Powered by Claude, Anthropic's AI model, and not offered where Anthropic's service isn't available. AI suggestions can be wrong — which is why the software checks every plan and waits for your Yes.</p>
</div>
<div class="phone"><img src="/img/hdd-05-ask-rex-plan.jpg" alt="Rex proposes a plan for a deleted folder" width="488" height="882" loading="lazy"></div>
</div></section>

<section class="alt"><div class="wrap">
<div class="center"><p class="eyebrow blue">How it works</p><h2>Four steps. Only the last one costs anything.</h2></div>
<div class="steps">
<div class="step"><h3>Choose drive</h3><p>Install, plug in the drive and choose it. Its health report is checked straight away; a drive that reports failure stops here.</p><span class="tag">Free</span></div>
<div class="step"><h3>Look for files</h3><p>The software recommends one way to look — usually a quick scan, or imaging first if the drive shows warning signs. Deep scan and imaging are under "Other ways".</p><span class="tag">Free</span></div>
<div class="step"><h3>Pick files</h3><p>Browse with thumbnail previews, folders and filters. Files that can't be recovered are hidden by default.</p><span class="tag">Free</span></div>
<div class="step"><h3>Save files</h3><p>Choose another drive to save to. Enter your licence key here — and only here.</p><span class="tag pay">Licence needed</span></div>
</div>
<div class="split" style="margin-top:56px">
<div class="shot"><img src="/img/hdd-01-drive-picker.jpg" alt="The drive picker only lists drives that can safely be read" width="925" height="511" loading="lazy"></div>
<div><h3>It can't touch the wrong drive</h3><p class="muted">The picker only lists drives that can safely be read. The drive Windows runs from never appears, so it can never be scanned or changed — and recovered files can only be saved to a different drive. Enforced, not just advised.</p>
<h3>Free extras</h3><p class="muted">File details and a read-only hex view, a printable job report (PDF) with the drive's health data and the file list, CSV export, the full SMART table, and saved scan results you can reopen later without rescanning.</p></div>
</div>
</div></section>

<section><div class="wrap">
<div class="center"><p class="eyebrow blue">Pricing</p><h2>One feature set. Choose how long you need it.</h2>
<p class="intro">Every licence includes everything above. Your licence key arrives by email straight after payment.</p></div>
{PRICE_CARDS('hdd_page')}
{CUR_NOTE}
<p class="center muted small" style="margin-top:14px">Secure checkout by Stripe. Licences are sold through Onelink (or "Link"), Stripe's merchant-of-record service, which handles payment, tax and receipts. <a href="/pricing/">Pricing details and refunds →</a></p>
</div></section>

<section class="alt"><div class="wrap">
<div class="center"><p class="eyebrow blue">Honest about the limits</p><h2>What no software can do</h2></div>
<div class="limits">
<div class="limit"><h3>Overwritten data is gone</h3><p>When a drive has re-used the space a deleted file occupied, no software can bring it back. This software tells you, file by file, rather than selling false hope.</p></div>
<div class="limit"><h3>SSDs erase deleted files</h3><p>On an SSD, deleted files are usually erased by the drive itself within minutes (TRIM), and a quick format erases the whole drive. The software marks such files "erased by the drive".</p></div>
<div class="limit"><h3>Encryption needs its keys</h3><p>Windows EFS files come back unreadable without the original account's key. BitLocker drives can't be read. FileVault-encrypted Mac volumes are named but cannot be read.</p></div>
<div class="limit"><h3>A failing drive needs a lab</h3><p>Clicking, not detected, or a health report that says failing — that's a job for a professional lab, not software. The software says so and stops. <a href="/guides/is-my-hard-drive-failing/">Signs of a failing drive →</a></p></div>
</div>
</div></section>

<section><div class="wrap center">
<p class="eyebrow blue">What's new</p><h2>Version {H['version']} · {H['released']}</h2>
<p class="intro">{H['whatsnew']}</p>
<p><a href="/download/">Download page, checksums and installation help →</a></p>
</div></section>
{faq_block(HDD_FAQ)}
{band("See what's recoverable — before you pay", f"Free download for Windows 10 and 11. Version {H['version']}.", dl_hdd("Download free"))}
""", uk_twin=H["cot_uk"], schema=[HDD_APP, faq_schema(HDD_FAQ)],
                crumbs=[("/", "Home"), ("/hard-drive-recovery-software/", "Recovery for Hard Drives")])

# ---------------------------------------------------------------- CARD PRODUCT
CARD_FAQ = [
    ("Is it really free?", "Yes — no trial, no upsell inside the app, no registration."),
    ("Which cards does it work on?", "SD and microSD memory cards formatted FAT32 or exFAT, which is how virtually all camera, drone and phone cards are formatted. Connect the card with a card reader."),
    ("Will it work on a USB stick, hard drive or SSD?", "No — it's built for memory cards only and won't even show your PC's own drives. For USB sticks, hard drives and SSDs, use <a href=\"/hard-drive-recovery-software/\">Recovery for Hard Drives</a> (a card in a USB card reader can also be scanned there)."),
    ("Which file types can it recover?", "A quick scan recovers any type of deleted file the card's file table still lists, with its original name and folder. A deep scan — for formatted cards and damaged file tables — recognises 17 formats: JPEG, PNG, GIF, TIFF, HEIC, CR2, CR3, NEF, ARW, DNG, MP4, MOV, AVI, MP3, WAV, PDF and Word (.docx). Deep-scan results come back without their original names."),
    ("Some of my photos are marked as damaged. Why?", "Every photo found by a deep scan is checked all the way through. Damaged photos are marked as damaged and shown as they'll actually be saved, never as a clean thumbnail. If many photos on a card are damaged, the card itself may be failing — the app tells you to stop using it."),
    ("Is there a Mac version?", "Not yet — it runs on Windows 10 and 11 (64-bit)."),
    ("Why does Windows show a warning when I run it?", "That's Microsoft SmartScreen, which is cautious about newly released software whoever published it. The installer is digitally signed by Data Clinic Ltd — click “More info”, check the publisher says Data Clinic Ltd, then “Run anyway”."),
    ("My card shows 0 MB or isn't recognised.", "That's usually physical failure, which no software can fix — and trying more tools can make things worse. Stop using the card. " + LAB_NOTE),
]
CARD_PAGE = page("/memory-card-recovery-software/", "Free Memory Card & SD Card Recovery Software for Windows | Data Clinic",
                 "Free software to recover deleted and formatted photos and videos from SD and microSD cards. Read-only, no registration, checks every photo for damage. Windows 10/11.",
                 f"""
<section class="hero"><div class="wrap grid">
<div>
<p class="eyebrow">Free Windows software · SD and microSD cards</p>
<h1>Data Clinic Recovery for Memory Cards</h1>
<p class="lead">Lost photos or videos from a memory card? A free tool from the engineers at Data Clinic for SD and microSD cards from cameras, drones and phones. No registration, no catches.</p>
<div class="ctas">{dl_card(f"Free download — {CARD['size']}")}<a class="btn ghost" href="/guides/recover-deleted-photos-sd-card/">How to use it</a></div>
<p class="fine">Windows 10/11, 64-bit · version {CARD['version']} · signed by Data Clinic Ltd</p>
{NOT_WINDOWS}
</div>
<div class="shot"><img src="/img/mc-device-picker.jpg" alt="Choose the memory card to scan: the tool lists only removable cards and never changes them" width="980" height="380" fetchpriority="high"></div>
</div></section>
<div class="trust"><div class="wrap"><span>100% free</span><span>No registration</span><span>Strictly read-only</span><span>Every photo checked for damage</span></div></div>

<section><div class="wrap">
<div class="center"><h2>Three simple steps</h2></div>
<div class="steps three">
<div class="step"><h3>Connect the card</h3><p>Use a card reader on your Windows PC. Only removable cards show up — your PC's own drives are never touched.</p></div>
<div class="step"><h3>Scan</h3><p>A <b>quick scan</b> finds recently deleted files with their names; a <b>deep scan</b> finds photos and videos on a formatted card or one with a damaged file table.</p></div>
<div class="step"><h3>Save</h3><p>Preview what was found and save it to a different drive — never back onto the card.</p></div>
</div>
</div></section>

<section class="alt"><div class="wrap split">
<div>
<h2>Honest about what it finds</h2>
<ul class="ticks">
<li><b>Every photo checked all the way through.</b> Damaged photos are marked as damaged and shown as they'll actually be saved — never as a clean thumbnail.</li>
<li><b>Warns you about a failing card.</b> If many photos on a card are damaged, the app tells you the card itself may be failing and to stop using it.</li>
<li><b>Read-only.</b> It never writes to, repairs or formats the card being scanned.</li>
</ul>
<h3>Deep scan recognises 17 formats</h3>
<p class="muted">Photos: JPEG, PNG, GIF, TIFF, HEIC · Raw: Canon CR2 and CR3, Nikon NEF, Sony ARW, Adobe DNG · Video: MP4, MOV, AVI · Audio: MP3, WAV · Documents: PDF, Word (.docx).</p>
</div>
<div>
<div class="limits one">
<div class="limit"><h3>Overwritten photos are gone</h3><p>Stop using the card straight away — every new photo can overwrite one you're trying to recover.</p></div>
<div class="limit"><h3>Deep scan finds no names</h3><p>Files found by a deep scan come back without their original names or folders, and fragmented videos can come back incomplete.</p></div>
<div class="limit"><h3>Physical failure needs a lab</h3><p>A card that shows 0 MB, isn't recognised or gives constant errors has failed in hardware — no software can fix that.</p></div>
</div>
</div>
</div></section>

<section><div class="wrap center">
<h2>Files on a hard drive, SSD or USB stick?</h2>
<p class="intro">USB sticks hold many file types the card tool doesn't look for — spreadsheets, presentations, archives. Use <a href="/hard-drive-recovery-software/">Recovery for Hard Drives</a> instead: free to scan and preview.</p>
<p class="muted small">What's new in {CARD['version']} ({CARD['released']}): memory cards only (USB sticks are covered by Recovery for Hard Drives); deep scan checks every photo all the way through and marks damaged ones honestly; new results screen with filters and helper tips.</p>
</div></section>
{faq_block(CARD_FAQ)}
{band("Get your photos back — free", "Windows 10 and 11, 64-bit. No registration.", dl_card("Free download"))}
""", uk_twin=CARD["cot_uk"], schema=[CARD_APP, faq_schema(CARD_FAQ)],
                 crumbs=[("/", "Home"), ("/memory-card-recovery-software/", "Recovery for Memory Cards")])

# ---------------------------------------------------------------- PRICING
PRICING_FAQ = [
    ("What currency will I pay in?", "Prices are set in pounds sterling. Checkout shows the price in your own currency, with any sales tax for your country worked out automatically."),
    ("How do I get my licence key?", "By email, straight after payment. Open the software, go to Help → Licence… (or the Save files step), paste the key and press Apply key."),
    ("Which licence do I need?", "For your own drives, a Personal licence: 28 days for a single recovery job, or a year if you'd like it on hand. If you recover data for customers — a PC repair shop or IT support — you need the Business licence, which allows commercial use on up to three PCs at one business."),
    ("Can I get a refund?", "Yes. A licence can be refunded within 14 days of purchase, no questions asked. If files the software showed as recoverable come back unusable and support can't put it right, you get a full refund — within 14 days for a 28-day licence, or 30 days for a yearly one. See the <a href=\"/legal/refund-policy/\">refund policy</a>."),
    ("Do yearly licences renew automatically?", "Yes. We email you before a renewal, and you can cancel at any time. An unwanted renewal is refunded in full if you ask within 14 days. A 28-day licence never renews."),
    ("Who sells the licence?", "Licences are sold through Onelink (or “Link”), Stripe's merchant-of-record service, which handles payment, tax, receipts and refunds — your receipt will say “Sold through Onelink”. The licence itself is granted by Data Clinic Ltd."),
]
PRICING = page("/pricing/", "Pricing — Data Clinic Recovery Software",
               "Recovery for Hard Drives: free scan and preview; licences from £39.99, shown in your currency at checkout. Recovery for Memory Cards is free.",
               f"""
<section class="pagehead"><div class="wrap center"><h1>Pricing</h1>
<p class="intro">Scan and preview are always free. You only pay to save recovered files with Recovery for Hard Drives — and the memory card tool is free.</p></div></section>
<section class="tight"><div class="wrap">
<h2 class="center">Recovery for Hard Drives</h2>
{PRICE_CARDS('pricing')}
{CUR_NOTE}
<p class="center muted small" style="margin-top:14px">Every licence includes everything the software does — quick scan, deep scan, imaging, Ask Rex and the job report. What differs is who may use it, for how long, and the business extras.</p>
</div></section>
<section class="alt tight"><div class="wrap split">
<div><h2>Recovery for Memory Cards</h2><p>SD and microSD cards. <b>Free</b> — no trial, no registration, no upsell inside the app.</p>{dl_card("Free download", "btn line")}</div>
<div><h3>If the drive turns out to need a lab</h3><p class="muted">Some drives are beyond any software. If yours turns out to be physically failing, you can have a full refund. Licence holders who send the drive to Data Clinic's lab in the UK also get a lab benefit: a Personal licence fee comes off the lab's price (within 90 days of buying), and Business licences get 10% off lab jobs. Details in the <a href="/legal/refund-policy/">refund policy</a>.</p></div>
</div></section>
{faq_block(PRICING_FAQ)}
""", schema=[faq_schema(PRICING_FAQ)], crumbs=[("/", "Home"), ("/pricing/", "Pricing")])

# ---------------------------------------------------------------- CHOOSER
CHOOSER = page("/which-software/", "Which Data Recovery Software Do I Need? | Data Clinic",
               "Two questions to find the right Data Clinic recovery tool for your drive, card or USB stick — and when software isn't the answer.",
               f"""
<section class="pagehead"><div class="wrap center"><h1>Which software do I need?</h1>
<p class="intro">Two quick questions, so you download the right tool — or know when software isn't the answer.</p></div></section>
<section class="tight"><div class="wrap narrow">
<div class="chooser" id="ch">
<fieldset><legend>1. What were the files on?</legend>
<label><input type="radio" name="dev" value="card"> An SD or microSD memory card (camera, drone, phone)</label>
<label><input type="radio" name="dev" value="usb"> A USB memory stick</label>
<label><input type="radio" name="dev" value="hdd"> An external hard drive or SSD</label>
<label><input type="radio" name="dev" value="int"> A drive inside my computer</label>
<label><input type="radio" name="dev" value="mac"> A Mac or a Mac-formatted drive</label>
</fieldset>
<fieldset><legend>2. What is the drive doing?</legend>
<label><input type="radio" name="sym" value="ok"> It works — the files were deleted or the drive was formatted</label>
<label><input type="radio" name="sym" value="raw"> Windows asks me to format it, or it shows as RAW</label>
<label><input type="radio" name="sym" value="phys"> It clicks, isn't detected, shows 0 MB or keeps disconnecting</label>
</fieldset>
<div class="answer" id="ans" aria-live="polite"><p class="muted">Choose an answer to each question.</p></div>
</div>
</div></section>
<section class="alt tight"><div class="wrap narrow">
<h2>At a glance</h2>
<table class="tbl"><thead><tr><th></th><th>Recovery for Hard Drives</th><th>Recovery for Memory Cards</th></tr></thead><tbody>
<tr><td>Hard drives and SSDs</td><td>✓</td><td>—</td></tr>
<tr><td>USB memory sticks</td><td>✓</td><td>—</td></tr>
<tr><td>SD and microSD cards</td><td>✓ (in a USB card reader)</td><td>✓</td></tr>
<tr><td>Mac drives (APFS, HFS+) on Windows</td><td>✓</td><td>—</td></tr>
<tr><td>File types by content (deep scan)</td><td>Dozens, plus your own</td><td>17 photo, video, audio and document formats</td></tr>
<tr><td>Drive health check, imaging, Ask Rex AI</td><td>✓</td><td>—</td></tr>
<tr><td>Price</td><td>Free scan; licence to recover</td><td>Free</td></tr>
</tbody></table>
</div></section>
<script>
(function(){{
var A={{
 card:'<h3>Recovery for Memory Cards — free</h3><p>Built for SD and microSD cards. Connect the card with a card reader.</p><a class="btn" href="/memory-card-recovery-software/">Get the memory card tool</a>',
 hdd:'<h3>Recovery for Hard Drives</h3><p>Free to scan and preview; a licence only to save the files.</p><a class="btn" href="/hard-drive-recovery-software/">Get Recovery for Hard Drives</a>',
 int:'<h3>Recovery for Hard Drives — on another PC</h3><p>The software never scans the drive Windows runs from, to keep it safe. Stop using the computer, take the drive out and connect it to another Windows PC with a USB adapter. Other internal drives can be scanned directly. If the drive is an SSD, read <a href="/guides/ssd-deleted-files-trim/">this first</a>.</p><a class="btn" href="/hard-drive-recovery-software/">Get Recovery for Hard Drives</a>',
 mac:'<h3>Recovery for Hard Drives — on a Windows PC</h3><p>The software runs on Windows and reads Mac APFS, HFS+ and HFS drives. Connect the Mac drive to a Windows PC. A Mac edition isn\\'t available yet.</p><a class="btn" href="/guides/read-mac-drive-on-windows/">Read the Mac drive guide</a>',
 raw:'<p><b>Don\\'t format it.</b> Click Cancel on the format message — formatting makes recovery harder. See <a href="/guides/you-need-to-format-the-disk/">what to do instead</a>.</p>',
 phys:'<h3>This needs a lab, not software</h3><p>Clicking, not detected, 0 MB or constant disconnects are physical faults. Running any recovery software can make them worse. Stop using the drive and take it to a professional data recovery lab. {LAB_NOTE.replace("'", "&#39;")}</p><p><a href="/guides/is-my-hard-drive-failing/">Signs of a failing drive →</a></p>'
}};
function upd(){{var d=(document.querySelector('[name=dev]:checked')||{{}}).value,s=(document.querySelector('[name=sym]:checked')||{{}}).value,o=document.getElementById('ans');
 if(!d||!s){{return}}
 if(s==='phys'){{o.innerHTML=A.phys;return}}
 var k=d==='card'?'card':(d==='usb'||d==='hdd')?'hdd':d;
 o.innerHTML=(s==='raw'?A.raw:'')+A[k];}}
document.querySelectorAll('#ch input').forEach(function(i){{i.addEventListener('change',upd)}});
}})();
</script>
""", crumbs=[("/", "Home"), ("/which-software/", "Which software do I need?")])

# ---------------------------------------------------------------- DOWNLOAD
DOWNLOAD = page("/download/", "Download Data Clinic Recovery Software for Windows",
                "Download Data Clinic Recovery for Hard Drives and the free Recovery for Memory Cards. Signed installers for Windows 10 and 11, checksums and installation help.",
                f"""
<section class="pagehead"><div class="wrap center"><h1>Downloads</h1>
<p class="intro">Both installers are digitally signed by Data Clinic Ltd. Windows 10 or 11, 64-bit.</p>{NOT_WINDOWS}</div></section>
<section class="tight"><div class="wrap">
<div class="dlrow">
<div class="dlbox"><h2>Recovery for Hard Drives</h2>
<p>Hard drives, SSDs and USB sticks. Free scan and preview; a licence to save recovered files.</p>
<p class="meta">Version {H['version']} · {H['released']} · {H['size']} · needs administrator rights</p>
{dl_hdd("Download " + H['version'])}
<p class="meta">SHA-256: <code>{H['sha256']}</code></p>
<p class="small"><a href="/hard-drive-recovery-software/">Product details</a> · What's new: {H['whatsnew']}</p></div>
<div class="dlbox"><h2>Recovery for Memory Cards</h2>
<p>SD and microSD cards. Completely free.</p>
<p class="meta">Version {CARD['version']} · {CARD['released']} · {CARD['size']}</p>
{dl_card("Download " + CARD['version'])}
<p class="meta">SHA-256: <code>{CARD['sha256']}</code></p>
<p class="small"><a href="/memory-card-recovery-software/">Product details</a></p></div>
</div>
</div></section>
<section class="alt tight"><div class="wrap narrow">
<h2>Installing</h2>
<ol class="numbered">
<li><b>Install on a different drive from the one you're recovering.</b> Never download or install recovery software onto the drive with the lost files — the installer could overwrite them.</li>
<li><b>Run the installer.</b> Windows asks for permission because the software reads drives directly. Check that the verified publisher shows <b>Data Clinic Ltd</b>.</li>
<li><b>If Microsoft SmartScreen appears</b> ("Windows protected your PC"), click <b>More info</b>, check the publisher says Data Clinic Ltd, then <b>Run anyway</b>. SmartScreen is cautious about newly released software whoever published it; every new version is submitted to Microsoft.</li>
<li><b>Updating.</b> When Recovery for Hard Drives starts online, it tells you if a newer version is available. Install the new version over the old one; your licence key carries over.</li>
</ol>
<p class="small muted">To check a download, run <code>certutil -hashfile &lt;file&gt; SHA256</code> in Command Prompt and compare the result with the checksums above.</p>
</div></section>
""", crumbs=[("/", "Home"), ("/download/", "Downloads")])

# ---------------------------------------------------------------- SUPPORT
SUPPORT_FAQ = [
    ("I bought a licence. Where's my key?", f"It's emailed straight after payment, usually within a few minutes. Check your spam folder. If it hasn't arrived within 30 minutes, email <a href=\"mailto:{SUPPORT_EMAIL}\">{SUPPORT_EMAIL}</a> with your order number."),
    ("How do I enter my licence key?", "Open Recovery for Hard Drives, choose Help → Licence… (or enter it on the Save files step), paste the key and press Apply key. The key is saved per Windows user, so another account on the same PC needs it entered again."),
    ("My yearly licence renewed. Do I need a new key?", "No. The program picks up the renewed key by itself the next time it starts online."),
    ("How do I cancel a yearly licence?", f"Use the link in the email we send before each renewal, or email {SUPPORT_EMAIL}. An unwanted renewal is refunded in full if you ask within 14 days."),
    ("How do I get a refund?", "Email <a href=\"mailto:customerservices@dataclinic.co.uk\">customerservices@dataclinic.co.uk</a> with your order number. Onelink/Stripe refunds your original payment method and the key is deactivated. See the <a href=\"/legal/refund-policy/\">refund policy</a>."),
    ("Windows says “Windows protected your PC”.", "That's Microsoft SmartScreen, which is cautious about new software. Click More info, check the publisher is Data Clinic Ltd, then Run anyway."),
    ("My drive doesn't appear in the list.", "The drive Windows runs from never appears, by design. Other drives may be missing if Windows can't see them at all — check Disk Management. A drive Windows doesn't detect, or that shows 0 MB, is usually physically failing: stop using it. See <a href=\"/guides/is-my-hard-drive-failing/\">signs of a failing drive</a>."),
    ("The software says my drive is failing.", "Stop using the drive — every further read can make things worse, and software can't fix physical failure. You can claim a full refund. " + LAB_NOTE),
    ("How do I send a problem report?", "In Recovery for Hard Drives, use the Help menu. The report includes your description and the program's technical log; you can save it to a file and read it before sending."),
]
SUPPORT = page("/support/", "Support — Data Clinic Recovery Software",
               "Help with licence keys, installation, SmartScreen, refunds and renewals for Data Clinic recovery software, and how to contact support.",
               f"""
<section class="pagehead"><div class="wrap center"><h1>Support</h1>
<p class="intro">Answers to common questions — and a real team behind them.</p></div></section>
<section class="tight"><div class="wrap">
<div class="cards">
<div class="card"><div class="ico">✉️</div><h3>Email support</h3><p>Write to <a href="mailto:{SUPPORT_EMAIL}">{SUPPORT_EMAIL}</a>. Include your order number if you've bought a licence. Office hours Monday–Friday, 8am–4pm UK time (GMT/BST).</p></div>
<div class="card"><div class="ico">📥</div><h3>Downloads</h3><p>Latest versions, checksums and installation help.</p><a href="/download/">Downloads →</a></div>
<div class="card"><div class="ico">📚</div><h3>Guides</h3><p>Step-by-step help for deleted files, formatted and RAW drives, Mac drives and memory cards.</p><a href="/guides/">Guides →</a></div>
</div>
</div></section>
{faq_block(SUPPORT_FAQ, "Common questions")}
""", schema=[faq_schema(SUPPORT_FAQ)], crumbs=[("/", "Home"), ("/support/", "Support")])

# ---------------------------------------------------------------- ABOUT
ABOUT = page("/about/", "About Data Clinic — Data Recovery Software from a Data Recovery Company",
             "Data Clinic Ltd has recovered data since 2002. Our software is built from what that work has taught us: check the drive first, never write to it, and be honest about what's recoverable.",
             f"""
<section class="pagehead"><div class="wrap center"><h1>About Data Clinic</h1></div></section>
<section class="tight"><div class="wrap narrow prose">
<p>Data Clinic is a data recovery company, not a software company. Data Clinic Ltd has been recovering data in the United Kingdom since 2002: our engineers work on failed hard drives, SSDs, RAID systems, phones and memory cards every day, in our own lab.</p>
<p>Our software is built from what that work has taught us. That's why it checks a drive's health before it scans, never writes to the drive it's reading, and tells you plainly when a file is gone or a drive needs more than software. We'd rather you knew the truth before you paid than after.</p>
<h2>What we make</h2>
<ul><li><a href="/hard-drive-recovery-software/">Data Clinic Recovery for Hard Drives</a> — hard drives, SSDs and USB sticks, with Ask Rex AI.</li>
<li><a href="/memory-card-recovery-software/">Data Clinic Recovery for Memory Cards</a> — free, for SD and microSD cards.</li></ul>
<h2>Company details</h2>
<p>{COMPANY}.<br>Email: <a href="mailto:{SUPPORT_EMAIL}">{SUPPORT_EMAIL}</a>.<br>Our UK website and data recovery lab: <a href="{CO_UK}/">dataclinic.co.uk</a>.</p>
</div></section>
""", schema=[ORG], crumbs=[("/", "Home"), ("/about/", "About")])

# ---------------------------------------------------------------- LICENCE (after payment)
LICENCE = page("/licence/", "Thank you for your order — Data Clinic Recovery for Hard Drives",
               "Your licence key for Data Clinic Recovery for Hard Drives.",
               f"""
<section class="pagehead"><div class="wrap center narrow">
<h1>Thank you for your order</h1>
<div id="ty-pending"><p class="intro">Your key is on its way…</p></div>
<div id="ty-ready" hidden>
<p class="intro">Your licence key:</p>
<div class="keybox"><code id="ty-key"></code><button class="btn sm" id="ty-copy">Copy</button></div>
<p id="ty-type" class="muted"></p><p id="ty-valid" class="muted"></p>
<p>Open Data Clinic Recovery for Hard Drives, choose <b>Help → Licence…</b> (or enter it on the <b>Save files</b> step), paste the key and press <b>Apply key</b>. We've also emailed it to you.</p>
</div>
<div id="ty-mail" hidden><p class="intro">Your key is in your email.</p></div>
<div id="ty-late" hidden><p class="intro">Your key will arrive by email within a few minutes. If it hasn't come in 30 minutes, contact <a href="mailto:{SUPPORT_EMAIL}">{SUPPORT_EMAIL}</a>.</p></div>
<p style="margin-top:26px">{dl_hdd("Download Data Clinic Recovery for Hard Drives")}</p>
</div></section>
<script>
(function(){{
var API="{LICENCE_KEY_API}",TYPES={{personal_28d:'Personal licence (28 days)',personal_1y:'Personal licence (1 year)',business_1y:'Business licence (1 year)'}};
function $(i){{return document.getElementById(i)}}
function fmt(s){{var m=/^(\\d{{4}})-(\\d{{2}})-(\\d{{2}})/.exec(s||'');if(!m)return s||'';var mo=['January','February','March','April','May','June','July','August','September','October','November','December'];return (+m[3])+' '+mo[+m[2]-1]+' '+m[1]}}
var sid=null;try{{sid=new URLSearchParams(location.search).get('session')}}catch(e){{}}
var done=false;function show(id){{if(done)return;done=true;$('ty-pending').hidden=true;$(id).hidden=false}}
if(!sid){{show('ty-mail');return}}
var t0=Date.now(),fails=0;
function ready(j){{show('ty-ready');$('ty-key').textContent=j.key;var t=j.type||'',y=!!j.renews||/1y|year/i.test(t);$('ty-type').textContent=TYPES[t]||'';
 if(y){{$('ty-valid').textContent=j.renews?('Renews automatically on '+fmt(j.renews)):'Renews automatically each year.'}}else if(j.expires){{$('ty-valid').textContent='Valid until '+fmt(j.expires)+' (does not renew)'}}}}
function tick(){{if(done)return;if(Date.now()-t0>120000){{show('ty-late');return}}
 fetch(API+'?session='+encodeURIComponent(sid),{{cache:'no-store',credentials:'omit'}}).then(function(r){{if(r.status===429||r.status===400){{show('ty-late');return null}}return r.json()}}).then(function(j){{
  if(done)return;if(j&&j.status==='ready'&&j.key){{ready(j);return}}if(j&&j.status==='expired'){{show('ty-mail');return}}setTimeout(tick,3500)}})
 ['catch'](function(){{if(++fails>=3){{show('ty-late');return}}setTimeout(tick,3500)}})}}
tick();
$('ty-copy').addEventListener('click',function(){{var b=this;try{{navigator.clipboard.writeText($('ty-key').textContent).then(function(){{b.textContent='Copied'}})}}catch(e){{}}}});
}})();
</script>
""", noindex=True)

# ---------------------------------------------------------------- LEGAL
def legal(src, path, title, desc):
    import re
    frag = open(f"legal/{src}").read()
    frag = (frag.replace('href="hard-drive-recovery-software.html"', 'href="/hard-drive-recovery-software/"')
            .replace('href="refund-policy.html"', 'href="/legal/refund-policy/"')
            .replace('href="licence-agreement.html"', 'href="/legal/licence-agreement/"')
            .replace('href="privacy.html"', 'href="/legal/privacy/"'))
    frag = re.sub(r"\s*·\s*0800 151 2207", "", frag)
    return page(path, title, desc, f'<section class="tight"><div class="wrap narrow prose legaldoc">{frag}</div></section>',
                crumbs=[("/", "Home"), (path, title.split(" — ")[0])])


REFUND = legal("refund.frag.html", "/legal/refund-policy/", "Refund policy — Data Clinic Recovery for Hard Drives",
               "Refunds for Data Clinic Recovery for Hard Drives licences: 14 days no questions asked, plus our recovery promise.")
EULA = legal("licence.frag.html", "/legal/licence-agreement/", "Licence agreement — Data Clinic Recovery for Hard Drives",
             "End-user licence agreement for Data Clinic Recovery for Hard Drives.")
PRIVACY = legal("privacy.frag.html", "/legal/privacy/", "Privacy policy — Data Clinic",
                "How Data Clinic Ltd handles personal information, including what its recovery software sends.")
PRIVACY = PRIVACY.replace('<section class="tight"><div class="wrap narrow prose legaldoc">',
                          '<section class="tight"><div class="wrap narrow prose legaldoc"><div class="note-box">'
                          '<b>This website (dataclinic.com)</b> does not set cookies, use analytics or collect '
                          'personal information. It loads only its own files; downloads and some links go to our UK '
                          f'website, <a href="{CO_UK}/">dataclinic.co.uk</a>. The policy below is Data Clinic Ltd\'s '
                          'privacy policy and covers our software.</div>', 1)

NOTFOUND = page("/404.html", "Page not found — Data Clinic Recovery Software", "Page not found.",
                f"""<section class="pagehead"><div class="wrap center"><h1>Page not found</h1>
<p class="intro">That page doesn't exist — but your files might still. Try one of these:</p>
<p><a class="btn" href="/">Home</a> <a class="btn line" href="/guides/">Guides</a> <a class="btn line" href="/download/">Downloads</a></p></div></section>""",
                noindex=True)
