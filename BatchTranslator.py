from Translator import Translator
import requests
import json
from time import perf_counter
import os
import Names
import TextProcessor

class BatchTranslator(Translator):
    def __init__(self, host: str, batchSize: int):
        self.batchSize = batchSize
        self.host = host

    def sendTranslationRequest(self, batch: list[str]):
        data = {'message': 'batch translate', 'content': batch}
        headers = {'content-type': 'application/json'}
        response = requests.post(f'http://{self.host}/', data=json.dumps(data), headers=headers)

        if response.status_code != 200:
            print(f"Translation request failed with status code {response.status_code}")
            return []
        
        return response.json()

    def fileOutput(self, inputFilePath: str, englishLines: list[str]):
        outputFilePath = os.path.splitext(inputFilePath)[0] + "-Translated.txt"
        with open(inputFilePath, 'r', encoding='utf8') as japaneseLines, open(outputFilePath, 'w', encoding='utf8') as output:
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
        numLines = sum(1 for _ in open(inputFilePath, encoding='utf8'))
        englishLines = []
        
        try:
            with open(inputFilePath, 'r', encoding='utf8') as japaneseLines:
                batch = []

                for index, japanese in enumerate(japaneseLines):
                    japanese = TextProcessor.replaceText(japanese, Names.JAPANESE_TO_ENGLISH)
                    japanese = TextProcessor.removeIndent(japanese)

                    batch.append(japanese)

                    if(len(batch) >= 64):
                        englishLines.extend(self.sendTranslationRequest(batch))
                        print(f'Current File: {inputFilePath}, Progress: {index+1}/{numLines} lines')
                        batch.clear()

                if batch:
                    englishLines.extend(self.sendTranslationRequest(batch))
                    print(f'Current File: {inputFilePath}, Progress: {index+1}/{numLines} lines')

                englishLines = [TextProcessor.replaceTextRegex(english, Names.ENGLISH_CORRECTION) for english in englishLines]

        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return

        print(f"Translation Complete. Took {perf_counter() - startTime:.3f} seconds, with an average speed of {numLines / (perf_counter() - startTime):.3f} lines per second")
        self.fileOutput(inputFilePath, englishLines)