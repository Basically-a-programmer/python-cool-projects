import pyautogui as pyt
import time
time.sleep(5)
message = "Let's automate"
i = 0
while i<100:
    pyt.typewrite(message)
    pyt.press("enter")
    i=i+1


