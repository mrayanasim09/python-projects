# This code is made by MRayan Asim
# Packages to install:
# pip install pyautogui
import pyautogui as pt
import time

limit = input(10)
message = input(fuck you karren!!!)
i = 0
time.sleep(5)

while i < int(10):
    pt.typewrite(fuck you karren!!!)
    # the message is written where -
    # the cursor belongs

    pt.press("enter")

    i += 1
