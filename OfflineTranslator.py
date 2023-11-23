from Translator import Translator
from OutputFormat import OutputFormat
import Names
import TextProcessor
from time import perf_counter
import requests
import json
import sys

class OfflineTranslator(Translator):
    def __init__(self, outputOption: OutputFormat, host: str):
        super().__init__(outputOption)
        self.host = host

    def sendTranslationRequest(self, japanese: str) -> str:
        data = {'message': 'translate sentences', 'content': japanese}
        headers = {'content-type': 'application/json'}
        response = requests.post(f'http://{self.host}/', data=json.dumps(data), headers=headers)

        if response.status_code != 200:
            print(f"Translation request failed with status code {response.status_code}")
            return []
        
        return response.json()

    def translate(self, inputFilePath: str):
        startTime = perf_counter()
        japaneseLines = TextProcessor.retrieveLines(inputFilePath)
        englishLines = []

        try:
            for index, japanese in enumerate(japaneseLines):
                print(f'Current File: {inputFilePath}, Progress: {index+1}/{len(japaneseLines)} lines')

                japanese = TextProcessor.replaceText(japanese, Names.JAPANESE_TO_ENGLISH)
                japanese = TextProcessor.removeIndent(japanese)

                english = self.sendTranslationRequest(japanese)
                english = TextProcessor.replaceTextRegex(english, Names.ENGLISH_CORRECTION)
                englishLines.append(english)

        except Exception as e:
            print(f"An error occurred: {str(e)}")
            sys.exit(1)

        print(f"Translation Complete. Took {perf_counter() - startTime:.3f} seconds, with an average speed of {len(japaneseLines) / (perf_counter() - startTime):.3f} lines per second")

        outputFilePath = TextProcessor.makeOutputFilePath(inputFilePath)
        self.outputOption.writeFile(outputFilePath, japaneseLines, englishLines)