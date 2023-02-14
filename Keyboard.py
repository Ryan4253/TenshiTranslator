from time import time, sleep
import keyboard
import pyautogui

KEYBOARD_STATE = {}

"""
Checks if the key's state changed to pressed from the previoud function call
"""
def changedToPressed(key : str) -> bool:
    state = keyboard.is_pressed(key)
    prev = False if not key in KEYBOARD_STATE else KEYBOARD_STATE[key]
    KEYBOARD_STATE[key] = state

    if state is True and prev is False:
        return True
    return False

"""
Simulates pressing ctrl+c on the keyboard
"""
def copy() -> None:
    pyautogui.hotkey('ctrl', 'c')

"""
Simulates pressing ctrl+v on the keyboard
"""
def paste() -> None:
    pyautogui.hotkey('ctrl', 'v')

