import Names
import os
import TextProcessor
from Constants import *
from time import perf_counter, sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OnlineTranslator:
    def __init__(self, timeoutWait : int):
        self.timeoutWait = timeoutWait

        self.url = "https://sugoitranslator.com/"
        self.swapLanguageButtonXPath = "//*[@id=\"routify-app\"]/div[1]/div/div[1]/div/div/div[2]/button"
        self.translateButtonXPath = "//*[@id=\"routify-app\"]/div[1]/div/div[1]/div/button"
        self.inputBoxPath = "//*[@id=\"routify-app\"]/div[1]/div/div[2]/div/div[1]"
        self.outputBoxPath = "//*[@id=\"routify-app\"]/div[1]/div/div[2]/div/div[2]"

        options = Options()
        options.add_argument("--headless=new")
        self.driver = webdriver.Chrome(options = options)
    
    def japaneseToEnglish(self, japanese) -> str:
        if(type(japanese) is list):
            return " ".join([self.japaneseToEnglish(lines) for lines in japanese])
        
        inputBox = self.driver.find_element(By.XPATH, INPUT_BOX_XPATH)
        inputBox.clear()
        inputBox.send_keys(japanese)

        outputBox = self.driver.find_element(By.XPATH, OUTPUT_BOX_XPATH)
        currentText = outputBox.text

        translateButton = self.driver.find_element(By.XPATH, TRANSLATE_BUTTON_XPATH)
        translateButton.click()

        WebDriverWait(self.driver, 5).until(
            lambda parent: outputBox.text != '' and outputBox.text != 'Waiting for translation' and outputBox.text != currentText
        )

        if TextProcessor.isTimeoutMessage(outputBox.text):
            print("Detected timeout, resuming once timeout is over.")
            sleep(self.timeoutWait)
            return self.japaneseToEnglish(japanese)
        
        return outputBox.text

    def fileOutput(self, inputFilePath:  str, japaneseLines: list[str], englishLines: list[str]):
        outputFilePath = os.path.splitext(inputFilePath)[0] + "-Translated.txt"
        with open(outputFilePath, 'w', encoding='utf8') as output:
            for japanese, english in zip(japaneseLines, englishLines):
                if TextProcessor.isEmptyLine(japanese):
                    output.write('\n')
                    continue

                if not TextProcessor.hasJapaneseCharacters(japanese):
                    output.write(japanese)
                    output.write('\n')
                    continue

                output.write(japanese)
                output.write(english)
                output.write('\n\n')

    def translate(self, inputFilePath: str):
            startTime = perf_counter()
            self.driver.get("https://sugoitranslator.com/")

            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, SWAP_LANGUAGE_BUTTON_XPATH))
            )

            swapLanguageButton = self.driver.find_element(By.XPATH, SWAP_LANGUAGE_BUTTON_XPATH)
            swapLanguageButton.click()

            japaneseLines = []
            englishLines = []

            with open(inputFilePath, 'r', encoding='utf8') as file:
                for line in file:
                    japaneseLines.append(line)

            japaneseLines = [TextProcessor.replaceText(japanese, Names.JAPANESE_TO_ENGLISH) for japanese in japaneseLines]
            japaneseLines = [TextProcessor.removeIndent(japanese) for japanese in japaneseLines]

            for index, japanese in enumerate(japaneseLines):
                print(f'Current File: {inputFilePath}, Progress: {index+1}/{len(japaneseLines)} lines')

                if TextProcessor.isEmptyLine(japanese):
                    englishLines.append('\n')
                    continue

                english = self.japaneseToEnglish(TextProcessor.splitToSentence(japanese, 100))
                english = TextProcessor.replaceTextRegex(english, Names.ENGLISH_CORRECTION)
                englishLines.append(english)
        
            print(f"Translation Complete. Took {perf_counter() - startTime:.3f} seconds, with an average speed of {len(japaneseLines) / (perf_counter() - startTime):.3f} lines per second")
            self.fileOutput(inputFilePath, japaneseLines, englishLines)
            self.driver.quit()