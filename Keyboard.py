from time import time, sleep
import keyboard
import pyautogui

KEYBOARD_STATE = {}

def changedToPressed(key : str) -> bool:
    state = keyboard.is_pressed(key)
    prev = False if not key in KEYBOARD_STATE else KEYBOARD_STATE[key]
    KEYBOARD_STATE[key] = state

    if state is True and prev is False:
        return True
    return False

def pausableSleep(timeout : float, key : str) -> None:
    startTime = time()
    while time() - startTime < timeout:
        sleep(0.01)
        if not changedToPressed(key):
            continue

        # Wait for resume
        print('Pause')
        while not changedToPressed(key):
            sleep(0.01)
        print('Resume')

def copy() -> None:
    pyautogui.hotkey('ctrl', 'c')

def paste() -> None:
    pyautogui.hotkey('ctrl', 'v')

