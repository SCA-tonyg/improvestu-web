# improvestu.com

Static landing site for Improvestu — **FARU** product marketing (FABU marketing is hidden until launch).

## Temporary home setup (2026-09)

- `/` — redirects to `/faru/` (company home archived)
- Archived company home: `_archive/home-2026-09/` (restore instructions in that folder’s README)

## Routes

- `/faru/` — FARU product page (how it works, Free vs FARU+, safety FAQ, store links)
- `/sitemap.xml`, `/llms.txt` — discovery helpers for search and AI assistants
- `/faru/admin-panel/` — FARU campus admin console (admin accounts only)
- `/fabu/` — redirects toward FARU until FABU launch (product page withheld)
- `/fabu/admin-panel/` — FABU staff admin console (admin accounts only; not linked publicly)
- `/fabu/privacy/`, `/fabu/terms/` — legal pages kept for store review; not linked from home

Keep a root `.nojekyll` so GitHub Pages serves `/fabu/admin-panel/_next/` assets.

Store links live in `faru/index.html`. Update `href`s there when listing URLs change.

## Restore company home later

```powershell
Copy-Item -Force _archive\home-2026-09\index.html index.html
```

Commit and push. See `_archive/home-2026-09/README.md`.

## Local preview

```powershell
python -m http.server 8080
```

Then visit http://localhost:8080 (you should land on `/faru/`).

## Deploy (GitHub Pages)

1. Push to `main`.
2. **Settings → Pages →** Deploy from branch `main` / root.
3. This repo includes a `CNAME` file for `improvestu.com`.

### DNS at your registrar

| Type  | Name | Value                          |
|-------|------|--------------------------------|
| A     | `@`  | `185.199.108.153`              |
| A     | `@`  | `185.199.109.153`              |
| A     | `@`  | `185.199.110.153`              |
| A     | `@`  | `185.199.111.153`              |
| CNAME | `www`| `<your-user>.github.io`        |

## Contact

improvestu@gmail.com
