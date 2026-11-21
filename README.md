# dataclinic.com

Data Clinic's international site for its data recovery **software** (no lab service pages — UK lab work stays on dataclinic.co.uk).

- The site root is the built output, served by GitHub Pages (custom domain in `CNAME`).
- Source lives in `_build/`: `config.py` (versions, download links, payment links, launch flag), `layout.py`, `pages.py`, `guides.py`, `build.py`, legal fragments in `_build/legal/`. Images are in `/img`.
- To rebuild: copy `/img` next to `_build/`, run `python3 build.py` in `_build/`, and copy `../dist/` to the repo root.
- Pre-launch: `LAUNCHED = False` in `config.py` puts `noindex` on every page. Flip it only when Chris approves launch.
