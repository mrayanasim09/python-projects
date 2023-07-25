import pyautogui as pt
import time

limit = input("Enter limit:")
message = input("Enter message:")
i = 0
time.sleep(5)

while i < int(limit):
    pt.typewrite(message)
    # the message is written where -
    # the cursor belongs      

    pt.press("enter")

    i+=1