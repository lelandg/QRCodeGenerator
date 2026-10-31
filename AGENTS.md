# QRCodeGenerator — agent guide

Small Python CLI (`main.py`, `qr_code_utils.py`) that generates QR codes from text, embeds an optional center image, reads QR codes back from images, and builds Wi-Fi QR codes. Global house rules apply; this file adds only repo-specific items.

## Hard rules

- The `--wifi` path extracts the current Wi-Fi password with `netsh ... key=clear`. Never print, log, or commit that password or the generated `wifi_qrcode.png`.

## Gotchas

- `--wifi` works only on native Windows (`netsh wlan`). It fails in WSL and on Linux/macOS.
- `--filter` / `-f` DISABLES image filtering (argparse `store_false`). Pass `-f` for B&W logos with a white background.
- Embedding relies on `ERROR_CORRECT_H`. Do not lower the error-correction level or the center image breaks decoding.
- `pyzbar` needs the system `zbar` library. `pip install` alone does not make `-r` work.

## Conventions

- No test suite. Verify a change by generating a code and reading it back with `-r`.
- Run from Windows with `python`; from WSL with `python3`.

## Pointers

- CLI reference and examples: `ReadMe.md`, `usage.txt`.

## Scanning & review

Policy lives in `~/.config/agents/AGENTS.md` -> "Dependency, code, and secret
scanning" and "Model delegation & cross-provider review". It is not restated
here; read it there. What is specific to this repo:

- CI runs `gitleaks` and `osv-scanner` on every PR, every push to `main`, and
  weekly (`.github/workflows/security.yml`). There is no `npm audit` job: this
  repo is pip-only, with no `package-lock.json`.
- `requirements.txt` pins nothing, so `osv-scanner` filters all three packages
  as unscannable and reports clean. Dependabot alerts are the real dependency
  signal here until the requirements carry versions.
- Dependabot config is committed, with grouped security PRs (`.github/dependabot.yml`).
- Dependabot **alerts** are a per-repo GitHub setting; a config file does not
  turn them on. Without them the config above governs version updates only.
  Check: `gh api -X GET repos/lelandg/QRCodeGenerator/vulnerability-alerts` (exit 0 = on,
  404 = off). Enable: same path with `-X PUT`.
- PR reviewers configured for this repo: **Codex** (run locally against the
  committed branch before opening the PR) and **CodeRabbit**
  (`coderabbitai[bot]`). How to read their checks -- which one re-reviews a
  push, why a green check does not mean "no findings", and which label skips
  which bot -- is in the global policy cited above and is deliberately not
  repeated here.
