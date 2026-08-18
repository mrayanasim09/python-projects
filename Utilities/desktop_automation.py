# This code is made by MRayan Asim
# Desktop Automation — Keyboard Typer
#
# SAFETY NOTICE:
#   - pyautogui.FAILSAFE is enabled: move your mouse to any screen corner to abort immediately.
#   - A 5-second countdown is shown before any keystrokes are sent.
#   - Press Ctrl+C during the countdown to cancel safely.
#
# Packages to install:
#   pip install pyautogui

import time

import pyautogui

# --- Safety: enable fail-safe (move mouse to corner to abort) ---
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.05  # minimum inter-action delay enforced by pyautogui


def countdown(seconds: int = 5) -> None:
    """Display a visible countdown before automation begins."""
    print("\n⚠  Desktop automation will start in:")
    print("   Move your mouse to any screen CORNER at any time to abort.\n")
    for remaining in range(seconds, 0, -1):
        print(f"   {remaining}...", flush=True)
        time.sleep(1)
    print("   Starting now!\n")


def type_message(message: str, repeat: int, delay: float = 0.1) -> None:
    """
    Type *message* the given number of times, pressing Enter after each.

    Args:
        message: The text to type.
        repeat:  Number of times to send the message (must be > 0).
        delay:   Seconds to wait between successive messages.
    """
    if repeat <= 0:
        raise ValueError(f"repeat must be a positive integer, got {repeat!r}")
    if not message:
        raise ValueError("message must not be empty")

    for i in range(repeat):
        pyautogui.typewrite(message, interval=0.02)
        pyautogui.press("enter")
        if i < repeat - 1:
            time.sleep(delay)


def main() -> None:
    try:
        repeat = int(input("How many times should the message be sent? "))
        if repeat <= 0:
            print("Error: count must be a positive integer.")
            return
    except ValueError:
        print("Error: please enter a valid integer.")
        return

    message = input("Enter the message to type: ")
    if not message.strip():
        print("Error: message cannot be blank.")
        return

    print(f"\nWill type {repeat!r} message(s) into the currently focused window.")
    countdown(seconds=5)

    try:
        type_message(message, repeat, delay=0.1)
    except pyautogui.FailSafeException:
        print("\n✋  Fail-safe triggered — automation aborted.")
    else:
        print("\n✅  Done.")


if __name__ == "__main__":
    main()
