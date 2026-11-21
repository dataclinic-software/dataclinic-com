"""Guides for dataclinic.com. Each: direct answer first, safe steps, what not to do, software steps, honest limits, FAQ."""
from config import *

HDD_DL = HDD["installer"]
LAB = (f'Data Clinic\'s own lab is in the UK (<a href="{CO_UK}/">dataclinic.co.uk</a>); elsewhere, '
       'choose a professional data recovery lab near you.')

STOP = ('<div class="callout warn"><b>Stop if the drive is physically failing.</b> Clicking, grinding or beeping, '
        'a drive Windows doesn\'t detect or shows as 0 MB, or one that keeps disconnecting has a hardware fault. '
        'Running any software on it can make things worse — <a href="/guides/is-my-hard-drive-failing/">read this first</a>.</div>')

SW_STEPS = """<ol class="numbered">
<li><b>Download and install</b> <a href="/hard-drive-recovery-software/">Data Clinic Recovery for Hard Drives</a> on a <i>different</i> drive from the one you're recovering.</li>
<li><b>Choose drive.</b> Connect the drive and choose it in the list. The software reads the drive's health report straight away; if the drive reports failure, it stops there.</li>
<li><b>Look for files.</b> {scan}</li>
<li><b>Pick files.</b> Browse the results with previews, folders and filters, and tick what you want. Every file shows whether it can really be recovered. Scanning and previewing are free.</li>
<li><b>Save files</b> to a different drive. This is the only step that needs a licence.</li>
</ol>"""

GUIDES = [
# ------------------------------------------------------------------ 1
dict(slug="recover-deleted-files-recycle-bin", product="hdd",
 title="How to Recover Files Deleted from the Recycle Bin (or with Shift+Delete)",
 h1="Recover files deleted from the Recycle Bin or with Shift+Delete",
 desc="Emptied the Recycle Bin or used Shift+Delete? What to check first, why to stop using the drive, and how to recover deleted files on Windows — including the honest limits.",
 answer="Emptying the Recycle Bin or pressing Shift+Delete doesn't wipe a file straight away on a hard drive: Windows marks the space as free, and the file stays there until something new is written over it. Stop using the drive, check the backups below, then scan the drive with recovery software from a different computer or drive. On an SSD, the honest answer is different — see the limits.",
 body=f"""
<h2>First: check the places Windows keeps copies</h2>
<ul>
<li><b>The Recycle Bin itself</b>, if you haven't emptied it: right-click the file and choose Restore.</li>
<li><b>OneDrive, Google Drive or Dropbox</b>: each has its own recycle bin or deleted-files view on the website, usually keeping files for 30 days or more.</li>
<li><b>File History or a backup drive</b>: right-click the folder the file was in and choose <i>Properties → Previous Versions</i>.</li>
</ul>

<h2>Then stop writing to the drive</h2>
<p>Every file you save, download or install could land on the space your deleted file still occupies. Don't install recovery software on that drive, and don't save recovered files back onto it.</p>
<div class="callout"><b>Was the file on your C: drive?</b> Recovery for Hard Drives never scans the drive Windows is running from — reading and writing to it all the time would put your files at risk. Shut the computer down, take the drive out and connect it to another Windows PC with a USB adapter, where it can be scanned safely. If that isn't practical, ask someone who can, or a professional.</div>

<h2>Recover the files with Recovery for Hard Drives</h2>
{SW_STEPS.format(scan="Run a <b>quick scan</b>. It reads the drive's file tables and lists deleted files with their original names and folders — including files emptied from the Recycle Bin on NTFS, exFAT and FAT32 drives. If what you need isn't there, try a <b>deep scan</b> (under “Other ways”), which also finds files by their content.")}
<p>Not sure where to look? Turn on <b>Ask Rex AI</b> and type what you lost — <i>"the folder called Accounts 2025 I deleted yesterday"</i>. Rex proposes a plan, and nothing starts until you press Yes.</p>

<h2>Honest limits</h2>
<ul>
<li><b>Overwritten files are gone.</b> If new data has been written over a deleted file, no software can bring it back. The software marks such files rather than pretending.</li>
<li><b>SSDs usually erase deleted files within minutes.</b> Most laptops now use SSDs, which clear deleted data themselves (TRIM). The software checks and marks those files “erased by the drive”. <a href="/guides/ssd-deleted-files-trim/">Why SSDs are different →</a></li>
<li><b>Recovered files carry today's date</b>, not their original date.</li>
</ul>
""",
 faq=[("Does Shift+Delete delete a file permanently?", "It skips the Recycle Bin, but on a hard drive the data stays where it was until it's overwritten, so it can often be recovered. On an SSD it's usually erased by the drive within minutes."),
      ("How long do I have to recover a deleted file?", "On a hard drive, until something overwrites it — which could be minutes on a busy system drive, or months on an external drive you don't use. Stop using the drive as soon as you notice."),
      ("Can I recover deleted files without software?", "Only from a copy: the Recycle Bin, a cloud service's deleted-files folder, File History or another backup. Once those are empty, you need recovery software."),
      ("Is the scan free?", "Yes. Scanning and previewing are free; a licence is needed only to save the recovered files.")]),
# ------------------------------------------------------------------ 2
dict(slug="recover-formatted-hard-drive", product="hdd", twin=CO_UK + "/recover-files-from-formatted-hard-drive/",
 title="How to Recover Files From a Formatted Hard Drive (and What Not to Do)",
 h1="Recover files from a formatted hard drive",
 desc="Formatted the wrong drive? A quick format leaves most data in place. What not to do, how quick and full formats differ, and how to get files back on Windows.",
 answer="A quick format only rebuilds the drive's file table; the files themselves usually stay on the drive until they're overwritten. Stop using the drive, don't copy anything onto it, and run a deep scan. A full format in Windows 10 or 11 writes zeros over the whole drive — after that, nothing is recoverable.",
 body=f"""
<h2>What not to do</h2>
<ul>
<li><b>Don't copy files back onto the drive</b> or start using it again — that overwrites the old data.</li>
<li><b>Don't format it again</b>, “just to be sure”, and don't run a full format.</li>
<li><b>Don't run disk repair tools</b> such as CHKDSK. They write to the drive.</li>
</ul>
{STOP}

<h2>Quick format or full format?</h2>
<p>Windows' <i>Quick Format</i> box is ticked by default. A quick format writes a new, empty file table and leaves the rest of the drive alone — which is why recovery usually works. A full format (unticking Quick Format) also writes zeros to every sector on Windows Vista and later; that data is gone for good.</p>
<p>The file system matters too:</p>
<ul>
<li><b>NTFS</b> (most Windows drives): a format clears the file table, so file names and folders can't come back. A deep scan finds files by their content and gives them numbered names such as <code>Rescued_0001.jpg</code>, in a folder called <code>[Found by content]</code>.</li>
<li><b>exFAT and FAT32</b> (many external drives and USB sticks): after a quick format, the old folder listings often survive. The deep scan finds them and brings many files back with their names, under <code>[Old folder listings]</code> — except files that sat in the drive's top folder.</li>
<li><b>SSDs</b>: a quick format erases the whole drive (TRIM). Formatted SSDs are usually not recoverable.</li>
</ul>

<h2>Recover the files</h2>
{SW_STEPS.format(scan="Choose <b>deep scan</b> (under “Other ways”). It reads the drive's file tables first — so anything they still list keeps its name — then reads the whole drive and recognises files by their content. On a large drive this takes hours; you can stop at any time and keep what's been found.")}
<p>Deep scan recognises dozens of formats — photos and camera raw, video, music, PDF and Office documents, Outlook PST, archives — and you can add signatures for your own file types.</p>

<h2>Honest limits</h2>
<ul>
<li>Anything copied onto the drive since the format has overwritten something.</li>
<li>Large videos are often stored in fragments; a deep scan may recover them incomplete.</li>
<li>Files found only by content have no original names or folders.</li>
</ul>
""",
 faq=[("Can a formatted hard drive be recovered?", "Usually, after a quick format, if nothing much has been written to it since. After a full format in Windows Vista or later, no — the data has been overwritten with zeros."),
      ("Why are my recovered files called Rescued_0001?", "On an NTFS drive, formatting clears the file table where names are kept. Files found by their content alone come back with numbered names."),
      ("I reinstalled Windows on the drive. Can I still recover files?", "Some, sometimes — but installing Windows writes many gigabytes, so a lot will have been overwritten. Take the drive out and scan it from another PC."),
      ("Does it work on a formatted SSD?", "Usually not. A quick format on an SSD tells the drive to erase everything, and it does.")]),
# ------------------------------------------------------------------ 3
dict(slug="drive-shows-raw", product="hdd", twin=CO_UK + "/raw-drive-recovery/",
 title="Drive Showing as RAW? How to Recover Your Files Without Formatting",
 h1="Drive showing as RAW? Get your files back without formatting",
 desc="Disk Management says your drive is RAW and Windows wants to format it. Why it happens, what not to do, and how to copy your files off safely.",
 answer="A drive shows as RAW when Windows can't recognise its file system — usually because the file system is damaged, the drive was unplugged mid-write, or it's formatted in a way Windows doesn't read (such as a Mac drive). The files are normally still there. Don't format it and don't run CHKDSK; scan it with recovery software and copy the files to another drive.",
 body=f"""
<h2>Why drives go RAW</h2>
<ul>
<li><b>Damaged file system</b> — often after the drive was unplugged without “Safely remove”, or a power cut.</li>
<li><b>A Mac-formatted drive</b> (APFS or HFS+) plugged into Windows. Windows shows it as RAW or unreadable — the drive is fine. <a href="/guides/read-mac-drive-on-windows/">Read a Mac drive on Windows →</a></li>
<li><b>A failing drive</b> that can't read its own file table. If it's slow, clicking, or disconnecting, that's the cause.</li>
</ul>
{STOP}

<h2>What not to do</h2>
<ul>
<li><b>Don't click “Format disk”</b> when Windows offers.</li>
<li><b>Don't run CHKDSK.</b> Windows may suggest it, and it sometimes “fixes” a damaged file system by discarding the parts it doesn't understand — including your files.</li>
<li><b>Don't initialise or repartition</b> the drive in Disk Management.</li>
</ul>

<h2>Recover the files</h2>
{SW_STEPS.format(scan="Start with the recommended scan. A <b>quick scan</b> can read file tables Windows has given up on — including Mac APFS, HFS+ and HFS — and lists files with their names and folders. If the file table is too damaged, a <b>deep scan</b> reads the whole drive and finds files by their content.")}
<p>Once your files are safely copied off, you can format the drive and use it again — if its health report is good.</p>

<h2>Honest limits</h2>
<ul><li>If the drive is RAW because it's failing, software is the wrong tool — the drive needs a lab. {LAB}</li>
<li>BitLocker-encrypted drives can look RAW too; Recovery for Hard Drives can't read BitLocker.</li></ul>
""",
 faq=[("Can I fix a RAW drive without losing data?", "Copy the files off first, with recovery software, then format the drive. Trying to “fix” it in place risks the files."),
      ("Will CHKDSK fix a RAW drive?", "Usually it reports that it can't run on RAW drives. When it does run on a damaged drive, it can delete what it can't make sense of — so don't use it before your files are safe."),
      ("My external drive shows RAW on Windows but works on a Mac.", "Then it's Mac-formatted. Windows can't read APFS or HFS+, but Recovery for Hard Drives can, and can copy the files onto a Windows drive.")]),
# ------------------------------------------------------------------ 4
dict(slug="you-need-to-format-the-disk", product="hdd",
 title="“You Need to Format the Disk Before You Can Use It” — Don't Click Format",
 h1="“You need to format the disk in drive E: before you can use it”",
 desc="Windows says you need to format the disk before you can use it. Click Cancel. Why it appears, and how to get your files off safely first.",
 answer="Click <b>Cancel</b>. This message means Windows can't read the drive's file system — not that the files are gone. Formatting would make recovery much harder. Work out which of the causes below applies, then copy the files off with recovery software before you format anything.",
 body=f"""
<h2>The usual causes</h2>
<ol>
<li><b>The drive was formatted on a Mac</b> (APFS or HFS+). Windows can't read it, so it offers to format it. Nothing is wrong with the drive. <a href="/guides/read-mac-drive-on-windows/">Read it on Windows →</a></li>
<li><b>The file system is damaged</b> — often after unplugging the drive while it was busy, or a power cut. The files are usually intact. <a href="/guides/drive-shows-raw/">RAW drive guide →</a></li>
<li><b>The drive is failing</b> and can't read its own file table. Look for the warning signs below.</li>
<li><b>It's encrypted</b> with BitLocker or another tool and hasn't been unlocked.</li>
</ol>
{STOP}

<h2>Get the files off safely</h2>
{SW_STEPS.format(scan="Run the recommended scan. The software reads file systems Windows can't — damaged NTFS, exFAT and FAT32, and Mac APFS, HFS+ and HFS — and shows files with their names. If the file table is badly damaged, use a <b>deep scan</b>.")}
<p>A USB stick that shows this message is usually a damaged file system too — that's exactly what the deep scan is for. But a stick that shows <b>0 MB</b> or keeps disconnecting has failed physically; software can't fix that.</p>

<h2>After your files are safe</h2>
<p>Once everything you need is copied to another drive, formatting the drive will make it usable again — if its health report is good. If the software reported warning signs, replace the drive instead.</p>
""",
 faq=[("If I click Format, are my files gone?", "A quick format makes recovery harder but often still possible — stop using the drive and run a deep scan. A full format overwrites everything."),
      ("Why does this happen to a drive that worked yesterday?", "Most often it was unplugged while Windows was writing to it, or it was used on a Mac. Sometimes it's the first sign of a failing drive."),
      ("Can CHKDSK fix it?", "It can make it worse. Get the files off first.")]),
# ------------------------------------------------------------------ 5
dict(slug="recover-deleted-files-external-hard-drive", product="hdd", twin=CO_UK + "/recover-deleted-files-from-external-hard-drive/",
 title="Deleted Files from an External Hard Drive? How to Get Them Back",
 h1="Recover deleted files from an external hard drive",
 desc="Deleted files from an external hard drive or USB drive? Where they might still be, why you should stop using the drive, and how to recover them on Windows.",
 answer="Files deleted from an external hard drive are usually still on it until they're overwritten — and external drives are often recoverable because they're used less than the main drive. Stop copying anything onto it, check its Recycle Bin, then scan it with recovery software.",
 body=f"""
<h2>Check the Recycle Bin first — it depends on the drive</h2>
<p>Windows treats external <b>hard drives</b> like internal ones: files deleted normally go to the Recycle Bin, so check there first. Files deleted from <b>USB memory sticks</b> skip the Recycle Bin and are deleted straight away. Either way, Shift+Delete skips it.</p>

<h2>Stop using the drive</h2>
<p>Don't save, copy or download anything onto it. Leave it unplugged until you're ready to scan, and save recovered files to a different drive.</p>
{STOP}

<h2>Recover the files</h2>
{SW_STEPS.format(scan="Run a <b>quick scan</b>: it lists deleted files the drive's file table still knows about, with their names and folders. If something's missing, a <b>deep scan</b> also searches the whole drive by file content. If the drive shows any warning signs, the software suggests <b>imaging it first</b> — copying it once to a file — so a weak drive isn't read over and over.")}

<h2>External SSDs are different</h2>
<p>Portable SSDs often erase deleted files themselves within minutes (TRIM). The software checks every deleted file and marks those the drive has erased. <a href="/guides/ssd-deleted-files-trim/">More on SSDs →</a></p>

<h2>Honest limits</h2>
<ul><li>Overwritten files can't be recovered by anyone.</li>
<li>A drive that clicks, isn't detected or disconnects needs a lab. {LAB}</li></ul>
""",
 faq=[("Do files deleted from an external drive go to the Recycle Bin?", "From an external hard drive, usually yes. From a USB memory stick, no — they're deleted immediately."),
      ("Can I recover files from an external drive that was dropped?", "If it now clicks, isn't detected or makes unusual noises, don't use software — a dropped drive often has damaged heads. That's a lab job."),
      ("Does it work with Seagate, WD, Toshiba and other brands?", "Yes — the brand doesn't matter for deleted files. What matters is that the drive still works.")]),
# ------------------------------------------------------------------ 6
dict(slug="read-mac-drive-on-windows", product="hdd", twin=CO_UK + "/read-mac-drive-on-windows/",
 title="Mac Drive on a Windows PC? How to Read It and Get Your Files Off",
 h1="Read a Mac drive on Windows and copy your files off",
 desc="Windows can't open Mac APFS or HFS+ drives and offers to format them. How to read a Mac-formatted drive on Windows and copy your files to a Windows drive — no Mac needed.",
 answer="Windows can't read drives formatted on a Mac (APFS, HFS+ or HFS), so it shows them as unreadable or asks you to format them — don't. The drive is fine. Recovery for Hard Drives reads Mac drives on Windows and copies the files onto a Windows drive, including files the Mac had deleted where an old copy of the file table survives.",
 body=f"""
<h2>Why Windows can't open it</h2>
<p>Macs use their own file systems: <b>APFS</b> on recent Macs and <b>HFS+</b> (“Mac OS Extended”) on older ones and many Time Machine drives. Windows has no built-in support for either, so it reports the drive as RAW or says you need to format it. <b>Click Cancel.</b></p>

<h2>Copy the files off on Windows</h2>
{SW_STEPS.format(scan="Run a <b>quick scan</b>. It reads APFS, HFS+ and HFS directly and lists every file still on the drive, with names and folders. Deleted Mac files come back with their names where an old copy of the file table survives (APFS and HFS+).")}
<p>Recovered files are saved to a Windows drive (NTFS or exFAT), ready to use straight away.</p>

<h2>Limits</h2>
<ul>
<li><b>FileVault-encrypted</b> volumes are identified but can't be read.</li>
<li>A few files Apple stores compressed may not come back; APFS <b>Fusion Drives</b> need a lab.</li>
<li>The software runs on Windows only — a Mac edition isn't available yet.</li>
</ul>
<p>If you only need to move files between a Mac and a PC in future, format a drive as <b>exFAT</b> — both systems read and write it.</p>
""",
 faq=[("Can Windows read a Mac hard drive?", "Not without extra software. Windows doesn't support APFS or HFS+."),
      ("Can I recover deleted files from a Mac drive on Windows?", "Often, yes: deleted Mac files come back with their names where an old copy of the file table survives (APFS and HFS+). If the Mac drive is an internal SSD, deleted files are usually erased by the drive itself."),
      ("Will it change anything on the Mac drive?", "No. It reads the drive strictly read-only and saves files to a different drive.")]),
# ------------------------------------------------------------------ 7
dict(slug="recover-formatted-usb-stick", product="hdd", twin=CO_UK + "/recover-formatted-usb-stick/",
 title="Formatted a USB Stick by Mistake? How to Recover Your Files",
 h1="Formatted a USB stick by mistake? How to get the files back",
 desc="Formatted the wrong USB flash drive? After a quick format most files are still there. How to recover them on Windows, and when a stick has failed for good.",
 answer="If you quick-formatted a USB stick, your files are usually still on it — and because most sticks use exFAT or FAT32, many can come back with their original names. Stop using the stick, don't copy anything onto it, and run a deep scan.",
 body=f"""
<h2>Why sticks are often recoverable</h2>
<p>A quick format writes a fresh, empty file table. On exFAT and FAT32 — how most USB sticks come — the old folder listings often survive, so the deep scan can bring many files back with their names, under <code>[Old folder listings]</code>. Files that sat in the stick's top folder come back without names.</p>

<h2>Recover the files</h2>
{SW_STEPS.format(scan="Choose <b>deep scan</b> (under “Other ways”). It reads the file table first, then the whole stick, finding old folder listings and recognising files by their content. Sticks have no health report, so the health check will say it's not available — that's normal.")}

<h2>When a stick has failed</h2>
<p>A stick that shows <b>0 MB</b>, isn't recognised, or keeps disconnecting has a hardware fault. Software can't fix that. A stick that Windows <i>asks to format</i> is different — that's usually a damaged file system, and exactly what the deep scan is for. <a href="/guides/you-need-to-format-the-disk/">Don't format it →</a></p>

<h2>Memory cards</h2>
<p>For SD and microSD cards from cameras and phones, use our free <a href="/memory-card-recovery-software/">memory card tool</a>.</p>
""",
 faq=[("Can you unformat a USB stick?", "Not in place — but you can recover the files from it onto another drive, which gets you the same result safely."),
      ("I formatted the stick and copied new files onto it.", "Some old files will be overwritten. Stop now and scan; what's left may still be recoverable."),
      ("Why does the health check say “not available”?", "USB sticks don't have a health report (SMART) the way hard drives do.")]),
# ------------------------------------------------------------------ 8
dict(slug="ssd-deleted-files-trim", product="hdd",
 title="Can Deleted Files Be Recovered From an SSD? The Honest Answer",
 h1="Can deleted files be recovered from an SSD?",
 desc="Why most SSDs erase deleted files within minutes (TRIM), when recovery is still possible, and how to check — the honest answer from a data recovery company.",
 answer="Usually not. Most SSDs use TRIM: when you delete a file, Windows tells the drive the space is free and the drive erases it, typically within minutes. A quick format on an SSD erases the whole drive the same way. What <i>can</i> often be recovered from an SSD is data lost another way — a damaged file system, a drive showing as RAW, or a partition that's gone missing.",
 body=f"""
<h2>What TRIM does</h2>
<p>An SSD can't simply overwrite old data; it has to erase blocks before reusing them. To keep the drive fast, Windows sends a <b>TRIM</b> command for deleted space, and the SSD clears it in the background. Once that happens, the deleted file is gone — for any software and any lab.</p>

<h2>When SSD recovery is possible</h2>
<ul>
<li><b>Damaged or RAW file systems</b> — the files weren't deleted, just made unreadable. <a href="/guides/drive-shows-raw/">RAW drive guide →</a></li>
<li><b>A lost or deleted partition</b> where the data area hasn't been trimmed.</li>
<li><b>Some external SSDs and older systems</b> where TRIM wasn't passed through. Many modern USB enclosures do pass it, so don't count on this.</li>
</ul>

<h2>Check, rather than guess</h2>
<p>Recovery for Hard Drives scans SSDs and checks each deleted file it finds. Files the drive has already erased are marked <b>“erased by the drive”</b>, so you can see what's genuinely recoverable before you pay — the scan and preview are free.</p>
<p>If the SSD is the one Windows runs from, take it out and connect it to another PC — the software never scans the running system drive.</p>

<h2>Protect yourself next time</h2>
<p>Because SSD deletions are so final, a backup is the only reliable protection: File History or another backup tool, plus a cloud service with a deleted-files folder.</p>
""",
 faq=[("Does a lab have special tools to undo TRIM?", "No. Once an SSD has erased the blocks, the data no longer exists on the chips."),
      ("Is TRIM always on?", "On Windows 10 and 11 with an internal SSD, almost always. Some external enclosures and older systems don't pass it through."),
      ("Can I recover files from a formatted SSD?", "Usually not — a quick format on an SSD trims the whole drive.")]),
# ------------------------------------------------------------------ 9
dict(slug="recover-deleted-photos-sd-card", product="card",
 title="How to Recover Deleted Photos from an SD Card (Free Tool)",
 h1="Recover deleted or formatted photos from an SD card",
 desc="Deleted photos or formatted an SD or microSD card? Stop using the card, then recover photos and videos for free on Windows. What works, and what doesn't.",
 answer="Take the card out of the camera or phone straight away — every new photo can overwrite one you're trying to recover. Then connect it to a Windows PC with a card reader and scan it with the free Data Clinic Recovery for Memory Cards: a quick scan for deleted photos, a deep scan for a formatted card.",
 body=f"""
<h2>Do this first</h2>
<ul>
<li><b>Stop using the card.</b> Don't take more photos, and don't format it in the camera.</li>
<li><b>Use a card reader</b> on a Windows 10 or 11 PC. A phone or camera connected by cable often can't be scanned directly.</li>
</ul>

<h2>Recover the photos — free</h2>
<ol class="numbered">
<li><b>Download</b> the free <a href="/memory-card-recovery-software/">Data Clinic Recovery for Memory Cards</a> and install it on your PC (not on the card).</li>
<li><b>Connect the card.</b> Only removable cards appear — your PC's own drives are never touched.</li>
<li><b>Quick scan</b> for recently deleted files. It finds any type of file the card's file table still lists, with original names and folders.</li>
<li><b>Deep scan</b> if the card was formatted or the quick scan comes up short. It recognises 17 formats: JPEG, PNG, GIF, TIFF, HEIC, Canon CR2/CR3, Nikon NEF, Sony ARW, DNG, MP4, MOV, AVI, MP3, WAV, PDF and Word.</li>
<li><b>Save</b> the photos to your PC — never back onto the card.</li>
</ol>
<p>Every photo the deep scan finds is checked all the way through. Damaged photos are marked as damaged and shown as they'll actually be saved, so you know what you're getting.</p>

<h2>Honest limits</h2>
<ul>
<li>Photos that have been overwritten can't be recovered.</li>
<li>Deep-scan results come back without their original file names.</li>
<li>Videos stored in fragments can come back incomplete.</li>
<li>A card that shows <b>0 MB</b>, isn't recognised or gives constant errors has failed physically — no software can fix that. If many recovered photos are damaged, the card itself may be failing; stop using it.</li>
</ul>
<p>Camera raw formats not in the list above, or a card in a USB card reader with other file types? <a href="/hard-drive-recovery-software/">Recovery for Hard Drives</a> can also scan a card in a reader and recognises many more formats.</p>
""",
 faq=[("Can I recover photos after formatting an SD card?", "Often, yes, if you haven't taken new photos since. Run a deep scan."),
      ("Is the memory card software really free?", "Yes — no trial, no registration and no upsell inside the app."),
      ("Can I recover photos from my phone's internal storage?", "Not with this software — it works on removable SD and microSD cards. Phone internal storage is encrypted and needs different methods."),
      ("Does it work on a Mac?", "Not yet — it runs on Windows 10 and 11.")]),
# ------------------------------------------------------------------ 10
dict(slug="is-my-hard-drive-failing", product="hdd",
 title="Is My Hard Drive Failing? The Signs, and When to Stop",
 h1="Is my hard drive failing? The signs, and when to stop",
 desc="Clicking, slow, freezing or not detected? The signs of a failing hard drive, what SMART warnings mean, and why you should stop before running recovery software.",
 answer="Clicking, grinding or beeping noises, a drive that isn't detected or shows 0 MB, one that keeps disconnecting, or a health (SMART) report that says failing are signs of a physical fault. Stop using the drive: every hour it runs can make recovery harder, and no software can repair hardware. Slowness and occasional read errors are early warnings — copy your data off once, carefully, and replace the drive.",
 body=f"""
<h2>Signs of a physical fault — stop now</h2>
<ul>
<li><b>Clicking, grinding, scraping or beeping.</b> Often failing heads or a seized motor. Repeated power-ons can scratch the platters.</li>
<li><b>Not detected</b> by the computer, or detected with the wrong size or <b>0 MB</b>.</li>
<li><b>Keeps disconnecting</b> or makes Windows freeze when plugged in.</li>
<li><b>A SMART report that says failing.</b></li>
</ul>
<p>These need a professional data recovery lab, which can image the drive with hardware built for failing drives. {LAB}</p>

<h2>Early warnings — act carefully</h2>
<ul>
<li>The drive has become very slow, or copying stalls on some files.</li>
<li>Occasional read errors, or files that won't open.</li>
<li>SMART shows a caution, such as reallocated or pending sectors.</li>
</ul>
<p>Back up anything important <b>once</b>, then replace the drive. If the data isn't backed up anywhere else, read the drive as few times as possible.</p>

<h2>How Recovery for Hard Drives handles this</h2>
<ul>
<li>It reads the drive's own health report when you choose it, before anything is scanned, and <b>refuses to scan a drive that reports failure</b>.</li>
<li>If a drive shows warning signs, it recommends <b>imaging it first</b>: one careful read into an image file on another drive, so every scan works from the copy. Unreadable areas are mapped, interrupted images resume, and imaging is free.</li>
<li>If the drive reports 0 MB, returns read errors or disconnects on its own, the software says so and tells you to stop using the drive.</li>
</ul>

<h2>What not to do</h2>
<ul>
<li>Don't put the drive in the freezer, tap it, or open it — opening a drive outside a clean room ruins it.</li>
<li>Don't run CHKDSK or “repair” tools on a failing drive.</li>
<li>Don't keep trying different recovery programs; each scan works the failing hardware.</li>
</ul>
""",
 faq=[("Can software fix a clicking hard drive?", "No. Clicking is almost always a mechanical fault. Software makes the drive work harder; a lab replaces or works around the failed parts."),
      ("What is SMART?", "Self-Monitoring, Analysis and Reporting Technology — a health report most hard drives and SSDs keep about themselves. Recovery for Hard Drives reads it before scanning. Some USB cases don't pass it through, and USB sticks don't have one."),
      ("My drive is just slow. Is it failing?", "Possibly. Check its SMART report; if it shows reallocated or pending sectors, copy your data off once and replace the drive."),
      ("Should I try recovery software on a failing drive?", "Not if it reports failure, clicks, or isn't detected. If it only shows early warnings, image it once and recover from the image.")]),
]
