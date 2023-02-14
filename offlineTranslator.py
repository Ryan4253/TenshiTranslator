import pyperclip
import Keyboard
import Mouse
import Names
from Timing import pausableSleep, computeProcessingTime
from Constants import *
from TextProcessor import *

"""
Translates a Japanese sentence into English using SugoiTL offline translator
Cursor positioning in Constants.py should be tuned.

Variable delay time will be used if constantTimeDelay is false, else OFFLINE_PROCESS_TIME will be used
"""
def japaneseToEnglish(line : str, constantTimeDelay : bool) -> str:
    # Copy line to clipboard
    pyperclip.copy(line)
    if constantTimeDelay:
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

Parameter :
inputFile - File name of japanese texts to translate. This should be in the same folder as the file
outputFile - File name of the result. If the file is not present, it will be created by the program
useConstantTime - Whether to wait for a constant time as specified in Constants.py to wait for the translation to process
"""
def translate(inputFile : str, outputFile : str, useConstantTime = True):
    with open(inputFile, 'r', encoding='utf8') as file, open(outputFile, 'w', encoding='utf8') as output:
        for japanese in file:
            if isEmptyLine(japanese):
                output.write('\n')
                continue

            tempJapanese = replaceText(japanese, Names.JAPANESE_TO_ENGLISH)
            english = japaneseToEnglish(tempJapanese, useConstantTime)
            english = replaceTextRegex(english, Names.ENGLISH_CORRECTION)

            output.write(japanese)
            output.write(english)


