import pyautogui
from time import sleep


def auto():
    pyautogui.PAUSE = 0.5

    print(pyautogui.position())
    print(pyautogui.size())

    sleep(10)
    pyautogui.moveTo(x=333, y=173, duration=1)

    sleep(1)
    pyautogui.moveTo(x=273, y=339, duration=1)

    sleep(1)
    pyautogui.moveTo(x=645, y=280, duration=1)

    sleep(1)
    pyautogui.click(x=645, y=280)


auto()
