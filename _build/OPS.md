# dataclinic.com — operations runbook

For Claude sessions and scheduled tasks. Read before changing the site. Owner: Chris Seeley (Data Clinic Ltd).

## Mandate (Chris, 21-11-2026)
- Sell Data Clinic's recovery software worldwide; become and stay the market leader.
- Claude has **standing permission to publish to dataclinic.com** (push to `main`) without asking each time, within the rules below.
- **Ask Chris first** for: prices, legal terms (licence, refund, privacy terms), anything mentioning the UK lab, anything that costs money (ads, paid listings, tools), new products or claims about unreleased features.

## Rules the site always follows
1. Software only. No lab service pages or lab sales copy. Never compete with dataclinic.co.uk for UK lab work.
2. UK searchers go to the .co.uk: every .com page with a .co.uk twin has hreflang (en, en-GB → .co.uk, x-default → .com), and the .co.uk side must match (see "UK twins").
3. Honest claims only: capabilities from the Software project's spec and release notes. No recovery percentages, no planned features, honest limits on every product page.
4. UK spelling, written for a worldwide reader.
5. Physical faults always route to "stop and use a lab" (link to the .co.uk), with no hard sell.
6. Refunds/legal contact stays customerservices@dataclinic.co.uk; general contact is support@dataclinic.com.

## Build and publish
- Repo `dataclinic-software/dataclinic-com`, branch `main`. Root = built site served by GitHub Pages (CNAME www.dataclinic.com). Source in `_build/`.
- Build: copy `/img` to `_build/img`, run `python3 build.py` in `_build/`, copy `../dist/.` to the repo root, delete `_build/img` and `dist`. Restore `_build/__pycache__` if git shows it deleted (it is tracked).
- `config.py`: versions, installers, SHA-256s, payment links, `LAUNCHED` (True since 21-11-2026), `GA4_ID`, `SUPPORT_EMAIL`.
- `site.css` lives in `_build/` (the build copies it); the CSS link is cache-busted by content hash.
- GitHub Pages caches ~10 min; verify with `?v=<random>`.

## Analytics and search
- GA4 property **565403697** "dataclinic.com (software site)", measurement ID **G-6QEBHWDTVL**, in GA account 227257045 "DC (April 2022)" (Data Clinic owned; users: chris.seeley@, analytics@, reporting service account as Viewer).
- GA4 loads **only after the visitor clicks "Yes"** on the cookie bar (choice in localStorage `dcCk`). "Cookie settings" link in the footer reopens it.
- Events: `dc_com_download_click` (product, page), `dc_com_buy_click` (plan, page), `dc_com_licence_key_shown` (type), `dc_com_key_copied`. Consent-only, so counts are a lower bound; Stripe is the source of truth for sales.
- Search Console: Domain property **sc-domain:dataclinic.com** (owner chris.seeley@dataclinic.co.uk; reporting service account = Full). Sitemap https://www.dataclinic.com/sitemap.xml submitted 21-11-2026.
- API access: service account `dataclinic-reporter@api-project-1006475031190.iam.gserviceaccount.com`. Helper on the Mac: `Data Clinic - Online Diagnosis Tool/dataclinic-com/ops/gapi.py` (`gsc(path)`, `ga4(endpoint, body)`).
- Stripe: account "Data Clinic Software"; payment links carry `client_reference_id=web_com_<page>`. After-payment redirect → https://www.dataclinic.com/licence/?session={CHECKOUT_SESSION_ID} (rollback: the .co.uk product page with the same query).

## UK twins (hreflang on both sites)
- .com side: `uk_twin=` argument on `page()` in `pages.py`/`guides.py`.
- .co.uk side: WPCode PHP snippet **18648** "dc-hreflang-com-twins" (frontend only) holds the path → .com URL map. **Add a line there whenever a new .com page gets a .co.uk twin**, then check both pages show matching hreflang.

## Licence key endpoint
- https://www.dataclinic.co.uk/software-licence/key/?session=… (owned by the Software project). Sends `Access-Control-Allow-Origin: https://www.dataclinic.com` on all replies. Rate limit 60/IP/hour. Yearly licences: show `renews`, never `expires`.

## Release sync (each software release note)
Update `config.py` (version, installer URL, size, SHA-256, what's new) and screenshots, on the same day as the .co.uk.
