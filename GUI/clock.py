# This code is made by MRayan Asim
try:
    import tkinter as Tkinter
except ImportError:
    import Tkinter

import math
import time
import os


class Main(Tkinter.Tk):
    def __init__(self):
        Tkinter.Tk.__init__(self)
        self.x = 150
        self.y = 150
        self.length = 50
        self.create_all_functions()

    def create_all_functions(self):
        self.create_canvas_for_shapes()
        self.create_background()
        self.create_sticks()

    def create_background(self):
        file_name = "download.png"  # you can replace it with your image name or you can download the image you can check out it at https://github.com/mrayanasim09/python-projects/blob/main/GUI/download.png
        script_directory = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_directory, file_name)
        self.image = Tkinter.PhotoImage(file=file_path)
        self.canvas.create_image(150, 150, image=self.image)

    def create_canvas_for_shapes(self):
        self.canvas = Tkinter.Canvas(self, bg="black")
        self.canvas.pack(expand="yes", fill="both")

    def create_sticks(self):
        self.sticks = []
        for _ in range(3):
            store = self.canvas.create_line(
                self.x,
                self.y,
                self.x + self.length,
                self.y + self.length,
                width=2,
                fill="red",
            )
            self.sticks.append(store)

    def update_class(self):
        now = time.localtime()
        t = time.strptime(str(now.tm_hour), "%H")
        hour = int(time.strftime("%I", t)) * 5
        now = (hour, now.tm_min, now.tm_sec)

        for n, i in enumerate(now):
            x, y = self.canvas.coords(self.sticks[n])[0:2]
            cr = [x, y]
            cr.append(
                self.length * math.cos(math.radians(i * 6) - math.radians(90)) + self.x
            )
            cr.append(
                self.length * math.sin(math.radians(i * 6) - math.radians(90)) + self.y
            )
            self.canvas.coords(self.sticks[n], tuple(cr))


if __name__ == "__main__":
    root = Main()

    def main_loop():
        root.update()
        root.update_idletasks()
        root.update_class()
        root.after(1000, main_loop)  # Call the main loop function after 1 second

    main_loop()
    root.mainloop()
