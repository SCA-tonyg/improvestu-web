# improvestu.com

Static landing site for Improvestu — download hub for **FARU** (FABU marketing is hidden until launch).

- `/` — home (FARU)
- `/faru/` — FARU product page (features, safety, store placeholders)
- `/faru/admin-panel/` — FARU campus admin console (admin accounts only)
- `/fabu/` — redirects home until FABU launch (product page withheld)
- `/fabu/admin-panel/` — FABU staff admin console (admin accounts only; not linked publicly)
- `/fabu/privacy/`, `/fabu/terms/` — legal pages kept for store review; not linked from home

Keep a root `.nojekyll` so GitHub Pages serves `/fabu/admin-panel/_next/` assets.

Store buttons are placeholders until the apps are listed. Update the `href`s in
`index.html` and `faru/index.html` (and remove `is-placeholder`) when links are live.
Restore FABU on the home page from git history (or re-add the product card) when ready to launch.

## Local preview

Open `index.html` in a browser, or from this folder:

```powershell
python -m http.server 8080
```

Then visit http://localhost:8080

## Deploy (GitHub Pages)

1. Create a GitHub repo (e.g. `improvestu-web` or `improvestu.github.io`).
2. Push this folder to `main`.
3. **Settings → Pages →** Deploy from branch `main` / root (or `/docs` if you prefer).
4. This repo includes a `CNAME` file for `improvestu.com`.

### DNS at your registrar

Point the domain at GitHub Pages (typical):

| Type  | Name | Value                          |
|-------|------|--------------------------------|
| A     | `@`  | `185.199.108.153`              |
| A     | `@`  | `185.199.109.153`              |
| A     | `@`  | `185.199.110.153`              |
| A     | `@`  | `185.199.111.153`              |
| CNAME | `www`| `<your-user>.github.io`        |

Or use Cloudflare Pages / Netlify: connect the repo and set the custom domain `improvestu.com` — they will show the exact DNS records.

## Contact

improvestu@gmail.com
