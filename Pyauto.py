import pyautogui
import time

pyautogui.FAILSAFE = False

time.sleep(3)
for i in range(50):
    print(i)
    pyautogui.keyDown("ctrl")
    pyautogui.press("t")
    pyautogui.keyUp("ctrl")

print("Program Ended..........")
