import pyperclip
import Keyboard
import Mouse
import Names
import Timing
from  TextProcessor import *
from Constants import *

"""
Translates a Japanese sentence into English using Sugoi TL.
Directly interfaces with the site by controlling the keyboard and cursor
If timeout is detected on the site, the function will block until the translation is over
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

    # Get English TL, check for timeout
    result = pyperclip.paste()
    if not isTimeoutMessage():
        Timing.pausableSleep(ONLINE_WAIT_TIME)
        return result
    
    print("Detected timeout, resuming once timeout is over.")
    Timing.pausableSleep(TIMEOUT_WAIT_TIME, PAUSE_KEY)
    return japaneseToEnglish(line)

"""
Translates a set of Japanese sentences into English using Sugoi TL.
If timeout is detected on the site, the function will block until the translation is over
"""
def japaneseListToEnglish(japanese : list) -> str:
    return " ".join([japaneseToEnglish(sentence) for sentence in japanese])

"""
Translates a Japanese sentence into English using SugoiTL offline translator
Cursor positioning in Constants.py should be tuned.

Variable delay time will be used if constantTimeDelay is false, else OFFLINE_PROCESS_TIME will be used
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
