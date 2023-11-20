import Names
import os
from  TextProcessor import *
from Constants import *
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""
Translates a Japanese sentence into English using Sugoi TL.
Directly interfaces with the site by controlling the keyboard and cursor
If timeout is detected on the site, the function will block until the translation is over
"""
def japaneseToEnglish(driver: webdriver, japanese : str) -> str:
    inputBox = driver.find_element(By.XPATH, INPUT_BOX_XPATH)
    inputBox.clear()
    inputBox.send_keys(japanese)

    outputBox = driver.find_element(By.XPATH, OUTPUT_BOX_XPATH)
    currentText = outputBox.text

    translateButton = driver.find_element(By.XPATH, TRANSLATE_BUTTON_XPATH)
    translateButton.click()

    WebDriverWait(driver, 5).until(
        lambda parent: outputBox.text != '' and outputBox.text != 'Waiting for translation' and outputBox.text != currentText
    )

    if isTimeoutMessage(outputBox.text):
        print("Detected timeout, resuming once timeout is over.")
        time.sleep(TIMEOUT_WAIT_TIME)
        return japaneseToEnglish(driver, japanese)
    
    return outputBox.text

"""
Translates a set of Japanese sentences into English using Sugoi TL.
If timeout is detected on the site, the function will block until the translation is over
"""
def japaneseLinesToEnglish(driver: webdriver, japaneseLines : list) -> str:
    return " ".join([japaneseToEnglish(driver, japanese) for japanese in japaneseLines])

"""
Translates a Japanese sentence into English using SugoiTL online translator
Cursor positioning in Constants.py should be tuned.
Result is stored in a new file '[Name]-Translated.txt'
"""
def translate(inputFilePath : str):
    outputFilePath = os.path.splitext(inputFilePath)[0] + "-Translated.txt"
    startTime = time()
    numLines = sum(1 for _ in open(inputFilePath, encoding='utf8'))

    options = Options()
    options.add_argument("--headless=new")

    driver = webdriver.Chrome(options = options)
    driver.get("https://sugoitranslator.com/")

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, SWAP_LANGUAGE_BUTTON_XPATH))
    )

    swapLanguageButton = driver.find_element(By.XPATH, SWAP_LANGUAGE_BUTTON_XPATH)
    swapLanguageButton.click()


    with open(inputFilePath, 'r', encoding='utf8') as japaneseLines, open(outputFilePath, 'w', encoding='utf8') as output:
        for index, japanese in enumerate(japaneseLines):
            print(f'Current File: {inputFilePath}, Progress: {index+1}/{numLines} lines')

            if isEmptyLine(japanese):
                output.write('\n')
                continue

            output.write(japanese)

            japanese = replaceText(japanese, Names.JAPANESE_TO_ENGLISH)
            japanese = removeIndent(japanese)

            english = japaneseLinesToEnglish(driver, splitToSentence(japanese, 100))
            english = replaceTextRegex(english, Names.ENGLISH_CORRECTION)

            output.write(english + '\n')
            output.write('\n')
    
    print(f"Translation Complete. Took {time() - startTime:.3f} seconds, with an average speed of {numLines / (time() - startTime):.3f} lines per second")
    driver.quit()
