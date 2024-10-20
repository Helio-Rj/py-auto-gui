import pyautogui
import time

print(pyautogui.position())
print(pyautogui.size())

time.sleep(10)
pyautogui.click(x=343, y=193)
