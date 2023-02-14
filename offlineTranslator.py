import pyperclip
import Keyboard
import Mouse
import Names
from Timing import pausableSleep, computeProcessingTime
from Constants import *
from TextProcessor import *

"""
Translates a line of Japanese into English using Sugoi TL.
Note that the tab must be open, and cursor positioning above should be tuned.

Parameter :
line - The japanese sentence to translate. This should be under 100 characters.

Return - the translated english
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
The function will translate line by line from Japanese to English
Japanese names are switched to placeholders, then back into English to prevent name with connotations (e.g. Mahiru)
to mess up the translation.

Parameter :
inputFile - file name of japanese texts to translate. This should be in the same folder as the file
outputFile - file name of the output. If the file is not present, it will be created by the program

Output - text file with format:
Original Line
English Translation
Empty line
With two empty lines between paragraphs
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


