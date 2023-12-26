from TenshiTranslator.Translator.Translator import Translator
from TenshiTranslator.OutputFormat.OutputFormat import OutputFormat
from TenshiTranslator.Util.Glossary import Glossary
import TenshiTranslator.Util.TextProcessor

from time import perf_counter, sleep
import sys
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import chromedriver_autoinstaller

class OnlineTranslator(Translator):
    """ Translator that translates by automating sugoitranslator.com using selenium
    
    As sugoi translator has a rate limit, this translator automatically waits for the timeout to end before resuming.
    The advantage of this translator is that it is free and does not require any setup. However, it is both the slowest 
    and the least accurate as it uses an older model and has a character limit of 100 characters per request. Long 
    sentences will be split into multiple requests, and contexts will not be taken into account.

    :param outputOption: the output format to use
    :param glossary: the glossary to use
    :param timeoutWait: the time to wait in seconds when a timeout is detected, defaults to 315 seconds
    """

    def __init__(self, outputOption: OutputFormat, glossary: Glossary, timeoutWait: int = 315):
        super().__init__(outputOption, glossary)
        self.timeoutWait = timeoutWait

        self.url = "https://sugoitranslator.com/"
        self.swapLanguageButtonXPath = "//*[@id=\"routify-app\"]/div[1]/div/div[1]/div/div/div[2]/button"
        self.translateButtonXPath = "//*[@id=\"routify-app\"]/div[1]/div/div[1]/div/button"
        self.inputBoxPath = "//*[@id=\"routify-app\"]/div[1]/div/div[2]/div/div[1]"
        self.outputBoxPath = "//*[@id=\"routify-app\"]/div[1]/div/div[2]/div/div[2]"

        chromedriver_autoinstaller.install()

        options = Options()
        options.add_argument("--headless=new")
        self.driver = webdriver.Chrome(options = options)
        self.initWebsite()

    def __del__(self):
        """ Destructor, closes the selenium driver
        """

        self.driver.quit()

    def initWebsite(self):
        """ Initializes the website by opening the site then swapping the language to japanese
        """

        self.driver.get("https://sugoitranslator.com/")

        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, self.swapLanguageButtonXPath))
        )

        swapLanguageButton = self.driver.find_element(By.XPATH, self.swapLanguageButtonXPath)
        swapLanguageButton.click()

    def japaneseToEnglish(self, japanese: str | list[str]) -> str:
        """ Translates a string or a list of strings from japanese to english using the sugoitranslator website and selenium
    
        :param japanese: the string or list of strings to be translated
        :return: the translated string
        """

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

        if TenshiTranslator.Util.TextProcessor.isTimeoutMessage(outputBox.text):
            print("Detected timeout, resuming once timeout is over.", flush=True)
            sleep(self.timeoutWait)
            return self.japaneseToEnglish(japanese)
        
        sleep(5)
        return outputBox.text

    def translate(self, inputFilePath: str):
        """ Translates a file and writes to inputFilePath-Translated.txt
    
        :param inputFilePath: path to the file to be translated
        :raises: FileNotFoundError if the file is not found
        :raises: Exception if any other error occurs
        """
            
        startTime = perf_counter()
        japaneseLines = TenshiTranslator.Util.TextProcessor.retrieveLines(inputFilePath)
        englishLines = []

        try:
            for index, japanese in enumerate(japaneseLines):
                print(f'Current File: {os.path.basename(inputFilePath)}, Progress: {index+1}/{len(japaneseLines)} lines', flush=True)

                if TenshiTranslator.Util.TextProcessor.isEmptyLine(japanese):
                    englishLines.append('\n')
                    continue
                
                japanese = self.glossary.replaceNames(japanese)
                japanese = TenshiTranslator.Util.TextProcessor.removeIndent(japanese)

                # Sugoi web translator has a character limit of 150 characters per request
                english = self.japaneseToEnglish(TenshiTranslator.Util.TextProcessor.splitToSentence(japanese, 150))
                english = self.glossary.applyCorrections(english)
                englishLines.append(english)
    
        except Exception as e:
            print(f"An error occurred: {str(e)}", flush=True)
            sys.exit(1)
        
        print(f'Translation Complete. Took {perf_counter() - startTime:.3f} seconds, with an average speed of {len(japaneseLines) / (perf_counter() - startTime):.3f} lines per second\n', flush=True)
        
        outputFilePath = TenshiTranslator.Util.TextProcessor.makeOutputFilePath(inputFilePath)
        self.outputOption.writeFile(outputFilePath, japaneseLines, englishLines)