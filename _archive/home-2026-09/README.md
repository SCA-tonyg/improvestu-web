# Archived company home (2026-09)

Snapshot of the Improvestu root homepage before `/` temporarily became a redirect to `/faru/`.

## Restore later

From the repo root:

```powershell
Copy-Item -Force _archive\home-2026-09\index.html index.html
# Optional if root styles diverged:
# Copy-Item -Force _archive\home-2026-09\styles.css styles.css
```

Then commit and push to GitHub Pages.

Also update `README.md` if it still says the root redirects to FARU.
