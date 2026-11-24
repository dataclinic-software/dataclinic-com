"""Single source of truth for dataclinic.com. Update here on every software release, then run build.py."""

SITE = "https://www.dataclinic.com"
CO_UK = "https://www.dataclinic.co.uk"

# Pre-launch: every page carries noindex until Chris approves launch. Flip to True at launch.
LAUNCHED = True

HDD = {
    "name": "Data Clinic Recovery for Hard Drives",
    "version": "1.1.2",
    "released": "November 2026",
    "installer": CO_UK + "/drive-rescue/DataClinic-HardDriveRecovery-Setup-1.1.2.exe",
    "sha256": "b3e83a2691797e29deb8083429875543e5e0eb0378df692c63b698d6e1d32a04",
    "size": "59.7 MB",
    "whatsnew": "Fixes a false “signs of physical failure” warning that some healthy drives in USB cases could get "
                "after a quick scan. The scan screen now shows steady progress from start to finish, and the program can "
                "send anonymous usage counts, which you can turn off in Settings. Install it over 1.1.1; your licence key "
                "carries over.",
    "cot_uk": CO_UK + "/data-recovery-software-for-hard-drives/",
}

CARD = {
    "name": "Data Clinic Recovery for Memory Cards",
    "version": "1.1.0",
    "released": "28-10-2026",
    "installer": CO_UK + "/drive-rescue/DataClinic-MemoryCardRecovery-Setup-1.1.0.exe",
    "sha256": "60216bacd1d1fb396fe56de66a5ce56e760a32f223a3c23ff35142fc694a48f3",
    "size": "59 MB",
    "cot_uk": CO_UK + "/data-recovery-software-free-download-from-data-clinic-ltd/",
}

PAY = {
    "personal_28d": "https://buy.stripe.com/bJe5kCboi4ebdoObaEao800",
    "personal_1y": "https://buy.stripe.com/dRm6oG4ZU9yvgB0fqUao801",
    "business_1y": "https://buy.stripe.com/14AdR83VQ9yv84u0w0ao802",
}
# client_reference_id labels the Stripe checkout session by origin (agreed with the Software project 21-11-2026)
PAY_REF = "web_com_"

SUPPORT_EMAIL = "support@dataclinic.com"
GA4_ID = "G-6QEBHWDTVL"  # GA4 property 565403697 "dataclinic.com (software site)", account DC (April 2022)
LICENCE_KEY_API = CO_UK + "/software-licence/key/"

COMPANY = ("Data Clinic Ltd · Company no. 04417174 · VAT GB 793061422 · "
           "Registered office: The Pavilions, Bridge Hall Lane, Bury BL9 7NX, United Kingdom")

LANGS = [("en", "English"), ("es", "Español"), ("de", "Deutsch"), ("fr", "Français"), ("it", "Italiano"),
         ("pt-br", "Português (Brasil)"), ("nl", "Nederlands"), ("pl", "Polski"), ("tr", "Türkçe"),
         ("ru", "Русский"), ("hi", "हिन्दी"), ("ja", "日本語"), ("zh-cn", "简体中文")]
