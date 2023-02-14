from time import time, sleep
from Keyboard import changedToPressed
import Constants

"""
Sleeps for the specified time. The sleep is paused if the given key is pressed, and unpaused if pressed again
The time measurement does not stop when paused. If the pause took longer than the timeout, it will exit once unpaused
"""
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

"""
Computes ideal processing time based on the sentence length. 
The time will be greater than 1 and not exceed OFFLINE_MAX_PROCESS_TIME in Constants.py
This is used for the offline translator where translation time is dependent on computer performance
The constants within this function is user-dependent. You should measure time vs length empirically and fit an exponential function
"""
def computeProcessingTime(characterLength : int) -> float:
    variableTime = 0.735 * max.exp(characterLength * 0.0116)+1 # +1 to make sure the equation is always greater than the data points
    return min(max(1, variableTime), Constants.OFFLINE_MAX_PROCESS_TIME)
    