from Translator import Translator
from OutputFormat import OutputFormat
import Names
import TextProcessor
from time import perf_counter, sleep
import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OnlineTranslator(Translator):
    def __init__(self, outputOption: OutputFormat, timeoutWait: int = 315):
        super().__init__(outputOption)
        self.timeoutWait = timeoutWait

        self.url = "https://sugoitranslator.com/"
        self.swapLanguageButtonXPath = "//*[@id=\"routify-app\"]/div[1]/div/div[1]/div/div/div[2]/button"
        self.translateButtonXPath = "//*[@id=\"routify-app\"]/div[1]/div/div[1]/div/button"
        self.inputBoxPath = "//*[@id=\"routify-app\"]/div[1]/div/div[2]/div/div[1]"
        self.outputBoxPath = "//*[@id=\"routify-app\"]/div[1]/div/div[2]/div/div[2]"

        options = Options()
        options.add_argument("--headless=new")
        self.driver = webdriver.Chrome(options = options)
        self.initWebsite()

    def __del__(self):
        self.driver.quit()

    def initWebsite(self):
        self.driver.get("https://sugoitranslator.com/")

        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, self.swapLanguageButtonXPath))
        )

        swapLanguageButton = self.driver.find_element(By.XPATH, self.swapLanguageButtonXPath)
        swapLanguageButton.click()

    def japaneseToEnglish(self, japanese: str | list[str]) -> str:
        if(type(japanese) is list):
            return " ".join([self.japaneseToEnglish(lines) for lines in japanese])
        
        inputBox = self.driver.find_element(By.XPATH, self.inputBoxPath)
        inputBox.clear()
        inputBox.send_keys(japanese)

        outputBox = self.driver.find_element(By.XPATH, self.outputBoxPath)
        currentText = outputBox.text

        translateButton = self.driver.find_element(By.XPATH, self.translateButtonXPath)
        translateButton.click()

        WebDriverWait(self.driver, 5).until(
            lambda parent: outputBox.text != '' and outputBox.text != 'Waiting for translation' and outputBox.text != currentText
        )

        if TextProcessor.isTimeoutMessage(outputBox.text):
            print("Detected timeout, resuming once timeout is over.")
            sleep(self.timeoutWait)
            return self.japaneseToEnglish(japanese)
        
        return outputBox.text

    def translate(self, inputFilePath: str):
        startTime = perf_counter()
        japaneseLines = TextProcessor.retrieveLines(inputFilePath)
        englishLines = []

        try:
            for index, japanese in enumerate(japaneseLines):
                print(f'Current File: {inputFilePath}, Progress: {index+1}/{len(japaneseLines)} lines')

                if TextProcessor.isEmptyLine(japanese):
                    englishLines.append('\n')
                    continue
                
                japanese = TextProcessor.replaceText(japanese, Names.JAPANESE_TO_ENGLISH)
                japanese = TextProcessor.removeIndent(japanese)

                english = self.japaneseToEnglish(TextProcessor.splitToSentence(japanese, 100))
                english = TextProcessor.replaceTextRegex(english, Names.ENGLISH_CORRECTION)
                englishLines.append(english)
    
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            sys.exit(1)
        
        print(f'Translation Complete. Took {perf_counter() - startTime:.3f} seconds, with an average speed of {len(japaneseLines) / (perf_counter() - startTime):.3f} lines per second')
        
        outputFilePath = TextProcessor.makeOutputFilePath(inputFilePath)
        self.outputOption.writeFile(outputFilePath, japaneseLines, englishLines)
