import pyautogui
import pyperclip
import keyboard
from time import sleep, time

# Names to replace
JAPANESE_NAMES = {
    '藤宮'   : 'フジミヤ', 
    '志保子' : 'シホコ', 
    '修斗'   : 'フブキ', 
    '椎名'   : 'シイナ', 
    '真昼'   : 'マヒル', 
    '小夜'   : 'コヨル', 
    '朝陽'   : 'アサヒ', 
    '赤澤'   : 'アカザワ', 
    '樹'     : 'イツキ', 
    '大輝'   : 'タイキ', 
    '白河'   : 'シラカワ', 
    '千歳'   : 'チトセ', 
    '門脇'   : 'カドワキ', 
    '優太'   : 'ユウタ', 
    '九重'   : 'ココノエ', 
    '柊'     : 'ヒイラギ',
    '一哉'   : 'カズヤ',
    '木戸'   : 'キド',
    '彩香'   : 'アヤカ',
    '茅野'   : 'タツキ',
    '総司'   : 'ソウジ',
    '糸巻'   : 'イトマキ',
    '文華'   : 'フミカ'
}

# English names to replace back
ENGLISH_NAMES = {
    'Zhou'    : 'Amane',
    'Shu'     : 'Amane',
    'Fubuki'  : 'Shuuto',
    'Fubuchi' : 'Shuuto',
    'Shina'   : 'Shiina',
    'mahiru'  : 'Mahiru',
    'Kojou'   : 'Koyoru',
    'Coconoe' : 'Kokonoe',
    'Tatsuki' : 'Kayano',
    'Itmaki'  : 'Itomaki'
}

#Screen Config
SCREEN_LENGTH = 1920
SCREEN_WIDTH = 1080

# Cursor Config. This is specific to your monitor.
SUGOI_JAPANESE_X = 0.22 * SCREEN_LENGTH
SUGOI_JAPANESE_Y = 0.35 * SCREEN_WIDTH
SUGOI_TL_X = 0.75 * SCREEN_LENGTH
SUGOI_TL_Y = 0.25 * SCREEN_WIDTH
SUGOI_ENGLISH_X = 0.22 * SCREEN_LENGTH
SUGOI_ENGLISH_Y = 0.67 * SCREEN_WIDTH

# Mouse Config
CPS = 10 

# Timing Config
TRANSLATION_PROCESS_TIME = 5 # Time to wait for the translation to generate
TRANSLATION_WAIT_TIME = 10 # Time to wait between translating lines. This is added to prevent timeouts 
TIMEOUT_WAIT_TIME = 330 # Time to wait if timeout occurrs

# Pausing Config
PAUSE_KEY = 'esc'
KEYBOARD_STATE = {}

# File Config
FILE_INPUT = "sample.txt"
FILE_OUTPUT = "Chap9TL.txt"

def changedToPressed(key):
    state = keyboard.is_pressed(key)
    prev = False if not key in KEYBOARD_STATE else KEYBOARD_STATE[key]
    KEYBOARD_STATE[key] = state

    if state is True and prev is False:
        return True
    return False

def pausableSleep(timeout, key):
    startTime = time()
    while time() - startTime < timeout:
        if changedToPressed(key):
            print('Pause')
            while not changedToPressed(key):
                sleep(0.01)
            print('Resume')

        sleep(0.01)

"""
Simulates 3 mouse clicks using the CPS specified above
"""
def tripleClick():
    for i in range(3):
        pyautogui.click()
        sleep(1.0/CPS)

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
    pyautogui.moveTo(SUGOI_JAPANESE_X, SUGOI_JAPANESE_Y) 
    tripleClick()
    pyautogui.hotkey('ctrl', 'v')

    # Click Translate, wait for results
    pyautogui.moveTo(SUGOI_TL_X, SUGOI_TL_Y)
    pyautogui.click()
    pausableSleep(TRANSLATION_PROCESS_TIME, PAUSE_KEY)
    # Copy English TL
    pyautogui.moveTo(SUGOI_ENGLISH_X, SUGOI_ENGLISH_Y)
    tripleClick()
    pyautogui.hotkey('ctrl', 'c')

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
def japaneseListToEnglish(japList : list) -> str:
    english = None
    for line in japList:
        tl = japaneseToEnglish(line)
        if tl.count('discord.gg') != 0:
            print("Detected timeout, resuming once timeout is over.")
            pausableSleep(TIMEOUT_WAIT_TIME, PAUSE_KEY)
            tl = japaneseToEnglish(line)
        english = tl if english is None else english + ' ' + tl
        pausableSleep(TRANSLATION_WAIT_TIME, PAUSE_KEY)

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
def translateFile(inputFile : str, outputFile : str):
    with open(inputFile, 'r', encoding='utf8') as file, open(outputFile, 'w', encoding='utf8') as output:
        for japanese in file:
            # Add line breaks if end of paragraph (empty line)
            if not japanese.strip():
                output.write('\n')
                continue

            # Output unaltered Japanese for proofread
            output.write(japanese)

            # Replacing character names
            for characterName, tempName in JAPANESE_NAMES.items():
                japanese = japanese.replace(characterName, tempName)

            # Removing Indent
            japanese = japanese[1:] if japanese[0] == '　' else japanese

            # Split the sentence up if over 100 characters
            tlList = [sentence + '。' for sentence in japanese.split('。') if sentence and sentence != '\n'] if len(japanese) > 100 else [japanese]

            # Initial translation
            english = japaneseListToEnglish(tlList)

            # Replacing incorrectly translated names
            for tempName, characterName  in ENGLISH_NAMES.items():
                english = english.replace(tempName, characterName)

            # Output English TL
            output.write(english + '\n')
            output.write('\n')

            # Wait to prent timeouts
            pausableSleep(TRANSLATION_WAIT_TIME, PAUSE_KEY)

# Driver Code. Modify as needed
if __name__ == "__main__":
    # Delay so you can tab to the sugoi page
    sleep(1)

    # Translate File
    translateFile(FILE_INPUT, FILE_OUTPUT)

    # Tune Cursor to Japanese 
    #pyautogui.moveTo(SUGOI_JAPANESE_X, SUGOI_JAPANESE_Y) 

    # Tune Cursor to English
    #pyautogui.moveTo(SUGOI_ENGLISH_X, SUGOI_ENGLISH_Y)

    # Tune Cursor to translate button
    #pyautogui.moveTo(SUGOI_TL_X, SUGOI_TL_Y)