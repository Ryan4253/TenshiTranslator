import pyperclip
import Keyboard
import Mouse
import Names
import Timing
from  TextProcessor import *
from Constants import *

"""
Translates a line of Japanese into English using Sugoi TL.
Note that the tab must be open, and cursor positioning above should be tuned.

Parameter :
line - The japanese sentence to translate. This should be under 100 characters.

Return - the translated english
"""
def japaneseToEnglish(line : str) -> str:
    # Copy line to clipboard
    pyperclip.copy(line)

    # Paste text into the Japanese 
    Mouse.setCursor(ONLINE_JAPANESE_X, ONLINE_JAPANESE_Y) 
    Mouse.tripleClick()
    Keyboard.paste()

    # Click Translate, wait for results
    Mouse.setCursor(ONLINE_TL_X, ONLINE_TL_Y)
    Mouse.click()
    Timing.pausableSleep(ONLINE_PROCESS_TIME, PAUSE_KEY)

    # Copy English TL
    Mouse.setCursor(ONLINE_ENGLISH_X, ONLINE_ENGLISH_Y)
    Mouse.tripleClick()
    Keyboard.copy()

    # Get English TL
    return pyperclip.paste()

"""
Translates a set of lines of Japanese into English using Sugoi TL.
The translation output will be contencated into one line. 
Note that the tab must be open, and cursor positioning above should be tuned.

Parameter :
japList - The japanese sentences to translate.

Return - the translated english
"""
def japaneseListToEnglish(jpList : list) -> str:
    english = None
    for line in jpList:
        tl = japaneseToEnglish(line)

        if isTimeoutMessage(tl):
            print("Detected timeout, resuming once timeout is over.")
            Timing.pausableSleep(TIMEOUT_WAIT_TIME, PAUSE_KEY)
            tl = japaneseToEnglish(line)
        
        english = tl if english is None else english + ' ' + tl
        Timing.pausableSleep(ONLINE_WAIT_TIME, PAUSE_KEY)

    return english

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
def translate(inputFile : str, outputFile : str):
    with open(inputFile, 'r', encoding='utf8') as file, open(outputFile, 'w', encoding='utf8') as output:
        for japanese in file:
            if isEmptyLine(japanese):
                output.write('\n')
                continue

            output.write(japanese)

            japanese = replaceText(japanese, Names.JAPANESE_TO_KATAKANA)
            japanese = removeIndent(japanese)

            english = japaneseListToEnglish(splitToSentence(japanese, 100))
            english = replaceText(english, Names.ENGLISH_CORRECTION)

            output.write(english + '\n')
            output.write('\n')

            Timing.pausableSleep(ONLINE_WAIT_TIME, PAUSE_KEY)
