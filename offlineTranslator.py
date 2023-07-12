import pyperclip
import os
import Keyboard
import Mouse
import Names
from Timing import pausableSleep, computeProcessingTime
from Constants import *
from TextProcessor import *

"""
Translates a Japanese sentence into English using SugoiTL offline translator
Cursor positioning in Constants.py should be tuned.

Variable delay time will be used if useVariableTime is true, else OFFLINE_PROCESS_TIME will be used
"""
def japaneseToEnglish(line : str, useVariableTime : bool) -> str:
    # Copy line to clipboard
    pyperclip.copy(line)
    if useVariableTime:
        pausableSleep(computeProcessingTime(len(line)), PAUSE_KEY)
    else:
        pausableSleep(OFFLINE_PROCESS_TIME, PAUSE_KEY)

    # Copy English TL
    Mouse.setCursor(OFFLINE_ENGLISH_X, OFFLINE_ENGLISH_Y)
    Mouse.tripleClick()
    Keyboard.copy()

    # Get English TL
    return pyperclip.paste()

"""
Translates a Japanese text file into English line by line using the Sugoi offline translator
Japanese names are switched to english first to prevent name with connotations from affecting
translation results.
Result is stored in a new file '[Name]-Translated.txt'

Parameter :
file - File name of japanese texts to translate. This should be in the same folder as the file
useVariableTime - Whether to wait for a time dependent on line specified in Constants.py for the translation to process
"""
def translate(file : str, useVariableTime = False):
    outputFile = os.path.splitext(file)[0] + "-Translated.txt"
    with open(file, 'r', encoding='utf8') as lines, open(outputFile, 'w', encoding='utf8') as output:
        for japanese in lines:
            if isEmptyLine(japanese):
                output.write('\n')
                continue

            tempJapanese = replaceText(japanese, Names.JAPANESE_TO_ENGLISH)
            english = japaneseToEnglish(tempJapanese, useVariableTime)
            english = replaceTextRegex(english, Names.ENGLISH_CORRECTION)

            output.write(japanese)
            output.write(english)


