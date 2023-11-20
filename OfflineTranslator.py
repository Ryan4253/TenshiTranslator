import requests
import json
from time import perf_counter
import os
import Names
import TextProcessor

class OfflineTranslator:
    def __init__(self, host: str):
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
        outputFilePath = os.path.splitext(inputFilePath)[0] + "-Translated.txt"
        startTime = perf_counter()
        numLines = sum(1 for _ in open(inputFilePath, encoding='utf8'))
        englishLines = []

        try:
            with open(inputFilePath, 'r', encoding='utf8') as japaneseLines, open(outputFilePath, 'w', encoding='utf8') as output:
                for index, japanese in enumerate(japaneseLines):
                    print(f'Current File: {inputFilePath}, Progress: {index+1}/{numLines} lines')

                    if TextProcessor.isEmptyLine(japanese):
                        output.write('\n')
                        continue
                    
                    output.write(japanese)

                    japanese = TextProcessor.replaceText(japanese, Names.JAPANESE_TO_ENGLISH)
                    japanese = TextProcessor.removeIndent(japanese)

                    english = self.sendTranslationRequest(japanese)
                    english = TextProcessor.replaceTextRegex(english, Names.ENGLISH_CORRECTION)

                    output.write(english + '\n')
                    output.write('\n')

                englishLines = [TextProcessor.replaceTextRegex(english, Names.ENGLISH_CORRECTION) for english in englishLines]

        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return

        print(f"Translation Complete. Took {perf_counter() - startTime:.3f} seconds, with an average speed of {numLines / (perf_counter() - startTime):.3f} lines per second")
