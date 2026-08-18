# This code is made by MRayan Asim
# Gesture-Controlled Brightness — hand distance maps to screen brightness.
#
# Packages needed:
#   pip install opencv-python mediapipe screen-brightness-control numpy
from __future__ import annotations

import platform
import sys
from math import hypot

import cv2
import mediapipe as mp
import numpy as np

# ---------------------------------------------------------------------------
# OS guard — screen-brightness-control only works on Windows/Linux
# ---------------------------------------------------------------------------
_BRIGHTNESS_SUPPORTED = platform.system() in ("Windows", "Linux")

if _BRIGHTNESS_SUPPORTED:
    import screen_brightness_control as sbc
else:
    print(
        f"[WARNING] screen-brightness-control is not supported on {platform.system()}. "
        "Brightness values will be printed to stdout instead."
    )


def _set_brightness(level: int) -> None:
    """Set screen brightness or fall back to printing the value."""
    if _BRIGHTNESS_SUPPORTED:
        sbc.set_brightness(int(level))
    else:
        print(f"[Brightness] {int(level)}%", end="\r")


# ---------------------------------------------------------------------------
# EMA smoother — prevents flicker from hand tremor
# ---------------------------------------------------------------------------


class _EMA:
    """Exponential Moving Average filter for a scalar signal."""

    def __init__(self, alpha: float = 0.15) -> None:
        """
        Args:
            alpha: Smoothing factor in (0, 1]. Lower = smoother but slower to react.
        """
        if not (0 < alpha <= 1):
            raise ValueError(f"alpha must be in (0, 1], got {alpha!r}")
        self._alpha = alpha
        self._value: float | None = None

    def update(self, measurement: float) -> float:
        if self._value is None:
            self._value = measurement
        else:
            self._value = self._alpha * measurement + (1 - self._alpha) * self._value
        return self._value


# ---------------------------------------------------------------------------
# MediaPipe setup
# ---------------------------------------------------------------------------

_mp_hands = mp.solutions.hands
_hands = _mp_hands.Hands(
    static_image_mode=False,
    model_complexity=1,
    min_detection_confidence=0.75,
    min_tracking_confidence=0.75,
    max_num_hands=2,
)
_draw = mp.solutions.drawing_utils

# ---------------------------------------------------------------------------
# Main capture loop
# ---------------------------------------------------------------------------


def run() -> None:
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("[ERROR] Cannot open camera. Check that a webcam is connected.")
        sys.exit(1)

    ema = _EMA(alpha=0.15)

    try:
        while True:
            try:
                ret, frame = cap.read()
            except Exception as exc:  # noqa: BLE001
                print(f"[ERROR] Camera read failed: {exc}")
                break

            if not ret or frame is None:
                print("[WARNING] Empty frame received — camera may have disconnected.")
                break

            frame = cv2.flip(frame, 1)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            try:
                result = _hands.process(frame_rgb)
            except Exception as exc:  # noqa: BLE001
                print(f"[WARNING] MediaPipe processing error: {exc}")
                cv2.imshow("Brightness Controller", frame)
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
                continue

            landmark_list: list[tuple[int, int, int]] = []

            if result.multi_hand_landmarks:
                for hand_lm in result.multi_hand_landmarks:
                    h, w, _ = frame.shape
                    for _id, lm in enumerate(hand_lm.landmark):
                        landmark_list.append((_id, int(lm.x * w), int(lm.y * h)))
                    _draw.draw_landmarks(frame, hand_lm, _mp_hands.HAND_CONNECTIONS)

            if landmark_list:
                # Thumb tip (id=4) and index finger tip (id=8)
                _, x1, y1 = landmark_list[4]
                _, x2, y2 = landmark_list[8]

                cv2.circle(frame, (x1, y1), 7, (0, 255, 0), cv2.FILLED)
                cv2.circle(frame, (x2, y2), 7, (0, 255, 0), cv2.FILLED)
                cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)

                distance = hypot(x2 - x1, y2 - y1)
                raw_brightness = float(np.interp(distance, [15, 220], [0, 100]))
                smooth_brightness = ema.update(raw_brightness)
                _set_brightness(round(smooth_brightness))

            cv2.imshow("Brightness Controller", frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    finally:
        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    run()
