from Translator import Translator
from OutputFormat import OutputFormat
from Glossary import Glossary
import TextProcessor
from time import perf_counter, sleep
import requests
import json
import sys
import subprocess

class BatchTranslator(Translator):
    def __init__(self, outputOption: OutputFormat, glossary: Glossary, sugoiDirectory: str, batchSize: int = 64):
        super().__init__(outputOption, glossary)
        self.batchSize = batchSize
        self.sugoiDirectory = sugoiDirectory
        self.host = '127.0.0.1:14366'

        print("OfflineTranslator: Starting Server...")
        self.server = subprocess.Popen(
            self.sugoiDirectory + "\\Code\\backendServer\\Program-Backend\\Sugoi-Japanese-Translator\\offlineTranslation\\activateOfflineTranslationServer.bat", 
            cwd=self.sugoiDirectory + "\\Code\\backendServer\\Program-Backend\\Sugoi-Japanese-Translator\\offlineTranslation", 
            creationflags=subprocess.CREATE_NO_WINDOW,
        )
        sleep(12)
        print("OfflineTranslator: Server Started")

    def __del__(self):
        print("OfflineTranslator: Stopping Server...")
        self.server.kill()
        # data = {'message': 'close server'}
        # headers = {'content-type': 'application/json'}
        # response = requests.post(f'http://{SUGOI_IP}/', data=json.dumps(data), headers=headers)
        # time.sleep(5)
        print("OfflineTranslator: Server Stopped")

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
                japanese = self.glossary.replaceNames(japanese)
                japanese = TextProcessor.removeIndent(japanese)

                batch.append(japanese)

                if(len(batch) >= 64 or index == len(japaneseLines)-1):
                    englishLines.extend(self.sendTranslationRequest(batch))
                    print(f'Current File: {inputFilePath}, Progress: {index+1}/{len(japaneseLines)} lines')
                    batch.clear()

            englishLines = [self.glossary.applyCorrections(english) for english in englishLines]

        except Exception as e:
            print(f"An error occurred: {str(e)}")
            sys.exit(1)

        print(f"Translation Complete. Took {perf_counter() - startTime:.3f} seconds, with an average speed of {len(japaneseLines) / (perf_counter() - startTime):.3f} lines per second")

        outputFilePath = TextProcessor.makeOutputFilePath(inputFilePath)
        self.outputOption.writeFile(outputFilePath, japaneseLines, englishLines)