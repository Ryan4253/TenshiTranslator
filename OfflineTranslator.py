from Translator import Translator
import requests
import json
from time import perf_counter
import os
import Names
import TextProcessor
from OutputFormat import OutputFormat

class OfflineTranslator(Translator):
    def __init__(self, outputOption: OutputFormat, host: str):
        super().__init__(outputOption)
        self.host = host

    def sendTranslationRequest(self, japanese: str):
        data = {'message': 'translate sentences', 'content': japanese}
        headers = {'content-type': 'application/json'}
        response = requests.post(f'http://{self.host}/', data=json.dumps(data), headers=headers)

        if response.status_code != 200:
            print(f"Translation request failed with status code {response.status_code}")
            return []
        
        return response.json()

    def translate(self, inputFilePath: str):
        startTime = perf_counter()
        
        japaneseLines = []
        englishLines = []

        with open(inputFilePath, 'r', encoding='utf8') as file:
            for line in file:
                japaneseLines.append(line)

        try:
            for index, japanese in enumerate(japaneseLines):
                print(f'Current File: {inputFilePath}, Progress: {index+1}/{len(japaneseLines)} lines')

                if TextProcessor.isEmptyLine(japanese):
                    englishLines.append('\n')
                    continue

                japanese = TextProcessor.replaceText(japanese, Names.JAPANESE_TO_ENGLISH)
                japanese = TextProcessor.removeIndent(japanese)

                english = self.sendTranslationRequest(japanese)
                english = TextProcessor.replaceTextRegex(english, Names.ENGLISH_CORRECTION)
                englishLines.append(english)

            outputFilePath = os.path.splitext(inputFilePath)[0] + "-Translated.txt"
            self.outputOption.writeFile(outputFilePath, japaneseLines, englishLines)

        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return

        print(f"Translation Complete. Took {perf_counter() - startTime:.3f} seconds, with an average speed of {len(japaneseLines) / (perf_counter() - startTime):.3f} lines per second")
