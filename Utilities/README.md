# Utilities

Practical command-line tools for productivity, networking, security, and automation.

## Prerequisites

```bash
pip install -e ".[gui,automation]"
```

> **Platform note:** `network.py` (Wi-Fi password retriever) only works on **Windows**.
> `desktop_automation.py` requires a visible, focusable window to receive keystrokes.

## Scripts

| Script | Description | Run |
|--------|-------------|-----|
| `desktop_automation.py` | Keyboard automation typer (with FAILSAFE + countdown) | `python desktop_automation.py` |
| `browser.py` | Minimal PyQt5 web browser | `python browser.py` |
| `password_manager.py` | Encrypted local password manager | `python password_manager.py` |
| `passwrd_generator.py` | Cryptographically secure password generator | `python passwrd_generator.py` |
| `password.py` | Hash password cracker (bcrypt / MD5, educational) | `python password.py` |
| `password_hash.py` | Hash a password string | `python password_hash.py` |
| `network.py` | Retrieve saved Wi-Fi passwords (Windows only) | `python network.py` |
| `connectivity.py` | Check internet / site connectivity | `python connectivity.py` |
| `transfer.py` | File transfer via QR code | `python transfer.py` |
| `google.py` | Google search from the terminal | `python google.py` |
| `github.py` | GitHub repository details finder | `python github.py` |
| `url.py` | QR code generator for URLs | `python url.py` |
| `btc.py` | Bitcoin mining simulator | `python btc.py` |
| `secret_code.py` | Caesar cipher encoder/decoder | `python secret_code.py` |
| `short_form.py` | Abbreviation / short-form generator | `python short_form.py` |
| `word_count.py` | Word and letter counter | `python word_count.py` |
| `count_down.py` | Countdown timer with audio | `python count_down.py` |
| `birthday.py` | Birthday reminder finder | `python birthday.py` |

## Security Notes

- `desktop_automation.py`: Move the mouse to **any screen corner** to abort immediately (pyautogui FAILSAFE).
- `network.py`: Uses `shell=False` with tokenised argument lists — no shell injection risk.
- `passwrd_generator.py`: Uses `secrets.choice()` (CSPRNG) — safe for generating real passwords.
