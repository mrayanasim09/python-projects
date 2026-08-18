# This code is made by MRayan Asim
from __future__ import annotations

import datetime
import math
import os

try:
    import tkinter as Tkinter
except ImportError:
    import Tkinter  # type: ignore[no-redef]


def hand_coords(
    value: int,
    max_value: int,
    cx: float,
    cy: float,
    length: float,
) -> tuple[float, float]:
    """
    Compute the tip (x, y) of a clock hand as polar coordinates.

    Args:
        value:      Current time unit (e.g. seconds 0–59, or scaled minutes/hours).
        max_value:  Full-scale value that maps to 360°  (e.g. 60 for seconds).
        cx, cy:     Centre of the clock face.
        length:     Length of the hand in pixels.

    Returns:
        (x, y) coordinates of the hand tip.
    """
    angle_deg = value * (360 / max_value) - 90  # 0 at top, clockwise
    angle_rad = math.radians(angle_deg)
    x = cx + length * math.cos(angle_rad)
    y = cy + length * math.sin(angle_rad)
    return x, y


class Main(Tkinter.Tk):
    def __init__(self) -> None:
        Tkinter.Tk.__init__(self)
        self.cx = 150
        self.cy = 150
        self.length = 50
        self._create_all_widgets()

    def _create_all_widgets(self) -> None:
        self._create_canvas()
        self._create_background()
        self._create_hands()

    def _create_canvas(self) -> None:
        self.canvas = Tkinter.Canvas(self, bg="black")
        self.canvas.pack(expand="yes", fill="both")

    def _create_background(self) -> None:
        # Image file lives alongside this script
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "download.png")
        self.image = Tkinter.PhotoImage(file=file_path)
        self.canvas.create_image(self.cx, self.cy, image=self.image)

    def _create_hands(self) -> None:
        self.hands = []
        for _ in range(3):
            line = self.canvas.create_line(
                self.cx,
                self.cy,
                self.cx + self.length,
                self.cy + self.length,
                width=2,
                fill="red",
            )
            self.hands.append(line)

    def update_hands(self) -> None:
        """Reposition all three clock hands based on the current time."""
        now = datetime.datetime.now()

        # Convert 24-hour to 12-hour scale mapped to 60 units (like minutes)
        hour_value = (now.hour % 12) * 5 + now.minute // 12
        time_values = (hour_value, now.minute, now.second)

        for hand_line, value in zip(self.hands, time_values, strict=False):
            x0, y0 = self.canvas.coords(hand_line)[0:2]
            tip_x, tip_y = hand_coords(value, 60, self.cx, self.cy, self.length)
            self.canvas.coords(hand_line, x0, y0, tip_x, tip_y)


if __name__ == "__main__":
    root = Main()

    def main_loop() -> None:
        root.update()
        root.update_idletasks()
        root.update_hands()
        root.after(1000, main_loop)

    main_loop()
    root.mainloop()
