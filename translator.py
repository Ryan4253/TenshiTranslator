import pyautogui
import pyperclip
from time import sleep

# Names to replace
JAPANESE_NAMES = {
    '藤宮'   : 'フジミヤ', 
    '志保子' : 'シホコ', 
    '修斗'   : 'シュウト', 
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
    '総司'   : 'ソウジ'
}

# English names to replace back
ENGLISH_NAMES = {
    'Zhou'    : 'Amane',
    'Shu'     : 'Amane',
    'Shut'    : 'Shuuto',
    'Shina'   : 'Shiina',
    'Kojou'   : 'Koyoru',
    'Coconoe' : 'Kokonoe',
    'Tatsuki' : 'Kayano',   
}

#Screen Config
SCREEN_LENGTH = 1920
SCREEN_WIDTH = 1080

# Cursor Config. This is specific to your monitor.
SUGOI_JAPANESE_X = 0.25 * SCREEN_LENGTH
SUGOI_JAPANESE_Y = 0.4 * SCREEN_WIDTH
SUGOI_TL_X = 0.8 * SCREEN_LENGTH
SUGOI_TL_Y = 0.275 * SCREEN_WIDTH
SUGOI_ENGLISH_X = 0.25 * SCREEN_LENGTH
SUGOI_ENGLISH_Y = 0.8 * SCREEN_WIDTH

# Mouse Config
CPS = 10 

# Timing Config
TRANSLATION_PROCESS_TIME = 5 # Time to wait for the translation to generate
TRANSLATION_WAIT_TIME = 10 # Time to wait between translating lines. This is added to prevent timeouts 

# File Config
FILE_INPUT = "input.txt"
FILE_OUTPUT = "output.txt"

def tripleClick():
    for i in range(3):
        pyautogui.click()
        sleep(1.0/CPS)

def japaneseToEnglish(line):
    # Copy line to clipboard
    pyperclip.copy(line)

    # Paste text into the Japanese 
    pyautogui.moveTo(SUGOI_JAPANESE_X, SUGOI_JAPANESE_Y) 
    tripleClick()
    pyautogui.hotkey('ctrl', 'v')

    # Click Translate, wait for results
    pyautogui.moveTo(SUGOI_TL_X, SUGOI_TL_Y)
    pyautogui.click()
    sleep(TRANSLATION_PROCESS_TIME)

    # Copy English TL
    pyautogui.moveTo(SUGOI_ENGLISH_X, SUGOI_ENGLISH_Y)
    tripleClick()
    pyautogui.hotkey('ctrl', 'c')

    # Get English TL
    return pyperclip.paste()

def japaneseListToEnglish(japList):
    english = None
    for line in japList:
        english = japaneseToEnglish(line) if english is None else english + ' ' + japaneseToEnglish(line)
        sleep(TRANSLATION_WAIT_TIME)

    return english

def translateFile():
    with open(FILE_INPUT, 'r', encoding='utf8') as file, open(FILE_OUTPUT, 'w', encoding='utf8') as output:
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

            # Check if timed out, if yes wait 5 min and retry
            if english.count('discord.gg') != 0:
                print("Detected timeout, resuming in 5 minutes")
                sleep(315)
                english = japaneseListToEnglish(tlList)

            # Replacing incorrectly translated names
            for characterName, tempName in ENGLISH_NAMES.items():
                english = english.replace(characterName, tempName)

            # Output English TL
            output.write(english + '\n')
            output.write('\n')

            # Wait to prent timeouts
            sleep(TRANSLATION_WAIT_TIME)

# Delay so you can tab to the sugoi page
sleep(3)

# Translate File
translateFile()

# Tune Cursor to Japanese 
#pyautogui.moveTo(SUGOI_JAPANESE_X, SUGOI_JAPANESE_Y) 

# Tune Cursor to English
#pyautogui.moveTo(SUGOI_ENGLISH_X, SUGOI_ENGLISH_Y)

# Tunr Cursor to translate button
#pyautogui.moveTo(SUGOI_TL_X, SUGOI_TL_Y)
