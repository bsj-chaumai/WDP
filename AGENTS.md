# WDP

## Cursor Cloud specific instructions

### What this repo is
This repository is a **single-file, client-side front-end mockup** — `operation-setup-wizard-mockup (3).html` — of the "WDP Operation Setup Wizard" (稼働分析セットアップ), a Japanese-language wizard for configuring workplace-occupancy/attendance analytics. There is **no backend, package manager, build step, or test suite** in this repo. It is a design proposal (README: `提案`).

### Dependencies
- No install step is required. The only runtime dependency is **SheetJS `xlsx@0.18.5`**, loaded at runtime from `cdn.jsdelivr.net` (needs outbound internet). Excel (`.xlsx`) parsing will fail without CDN access; CSV parsing is pure in-page JS and works offline.

### Running it (dev)
- Serve the file over HTTP (preferred over `file://` so relative fetches behave):
  - `python3 -m http.server 8000` from the repo root, then open `http://localhost:8000/operation-setup-wizard-mockup%20(3).html` (note the URL-encoded space `%20` and the `(3)` in the filename).

### Lint / test / build
- None exist. There is no linter, test runner, or build tooling configured.

### Non-obvious gotchas
- The wizard references sample data files under `operation-samples/…` (the "📥 サンプル" download links) and a backend `POST /operation-analysis/setup` (S3 → AWS Glue) plus a Cisco Meraki webhook. **None of these exist in the repo** — the sample-download links 404 and the final "保存して分析開始" step only fires a mock `alert()`. To exercise the CSV upload + auto column-mapping flow, upload your own CSV (e.g. columns `clientMac,Timestamp` with Unix-second timestamps for the "① Wifi CSV" method).
