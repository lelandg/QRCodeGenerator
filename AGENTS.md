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
