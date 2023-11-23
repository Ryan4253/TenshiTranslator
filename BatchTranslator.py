from Translator import Translator
from OutputFormat import OutputFormat
import Names
import TextProcessor
from time import perf_counter
import requests
import json

class BatchTranslator(Translator):
    def __init__(self, outputOption: OutputFormat, host: str, batchSize: int = 64):
        super().__init__(outputOption)
        self.batchSize = batchSize
        self.host = host

    def sendTranslationRequest(self, batch: list[str]) -> list[str]:
        data = {'message': 'batch translate', 'content': batch}
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
            batch = []

            for index, japanese in enumerate(japaneseLines):
                japanese = TextProcessor.replaceText(japanese, Names.JAPANESE_TO_ENGLISH)
                japanese = TextProcessor.removeIndent(japanese)

                batch.append(japanese)

                if(len(batch) >= 64 or index == len(japaneseLines)-1):
                    englishLines.extend(self.sendTranslationRequest(batch))
                    print(f'Current File: {inputFilePath}, Progress: {index+1}/{len(japaneseLines)} lines')
                    batch.clear()

            englishLines = [TextProcessor.replaceTextRegex(english, Names.ENGLISH_CORRECTION) for english in englishLines]

        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return

        print(f"Translation Complete. Took {perf_counter() - startTime:.3f} seconds, with an average speed of {len(japaneseLines) / (perf_counter() - startTime):.3f} lines per second")

        outputFilePath = TextProcessor.makeOutputFilePath(inputFilePath)
        self.outputOption.writeFile(outputFilePath, japaneseLines, englishLines)