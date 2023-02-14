from time import time, sleep
from Keyboard import changedToPressed
import Constants
import math

def pausableSleep(timeout : float, key : str):
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

def computeProcessingTime(characterLength : int) -> float:
    variableTime = 0.735 * max.exp(characterLength * 0.0116)
    return min(max(1, variableTime), Constants.OFFLINE_MAX_PROCESS_TIME)
    