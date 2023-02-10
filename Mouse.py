from time import sleep
from Constants import CPS
import pyautogui

def click() -> None:
    pyautogui.click()

def tripleClick() -> None:
    for i in range(3):
        pyautogui.click()
        sleep(1.0/CPS)

def setCursor(x : int, y : float) -> None:
    pyautogui.moveTo(x, y)
