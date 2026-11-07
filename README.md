# improvestu.com

Static landing site for Improvestu — **FARU** (campus carpool) and **FASU** (study buddy).

## Routes

- `/` — company home (FARU + FASU)
- `/faru/` — FARU product marketing
- `/fasu/` — FASU Study Buddy product marketing
- `/fasu/privacy/`, `/fasu/terms/` — FASU legal
- `/sitemap.xml`, `/llms.txt` — discovery helpers
- `/faru/admin-panel/` — FARU campus admin console
- `/fabu/` — redirects toward FARU until FABU launch (product page withheld)

Keep a root `.nojekyll` so GitHub Pages serves `/fabu/admin-panel/_next/` assets.

## Local preview

```powershell
python -m http.server 8080
```

Then visit http://localhost:8080.

## Deploy (GitHub Pages)

1. Push to `main`.
2. **Settings → Pages →** Deploy from branch `main` / root.
3. This repo includes a `CNAME` file for `improvestu.com`.

## Contact

improvestu@gmail.com
