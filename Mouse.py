from time import sleep
from Constants import CPS
import pyautogui

"""
Simulates a mouse click
"""
def click():
    pyautogui.click()

"""
Simulates three mouse clicks in a row using the specified speed in Constants.py
"""
def tripleClick():
    for i in range(3):
        pyautogui.click()
        sleep(1.0/CPS)

"""
Moves the cursor to the specified pixel
(0, 0) is the topleft-most pixel. +x goes right, +y goes down
"""
def setCursor(x : int, y : int):
    pyautogui.moveTo(x, y)
