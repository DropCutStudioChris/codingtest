# Project Context

Pomodoro timer — a minimal static webpage (HTML/CSS/JS) served locally, used
as a learning vehicle for Anvil Plan Spec (APS) planning and authorisation.

- **Runtime:** Python 3 (for serving and validation); no Node on this machine.
- **Serving:** `python3 -m http.server 8000` from the project root.
- **App files:** `index.html`, `style.css`, `app.js`.
- **Tests:** `tests/` — Python `unittest` contract checks plus a serve check.
- **Planning:** APS under `plans/` (see `aps-rules.md`); drive with the `aps` CLI.
