from Translator import Translator
from OutputFormat import OutputFormat
from Glossary import Glossary
import TextProcessor
from time import perf_counter, sleep
import requests
import json
import sys
import subprocess

class OfflineTranslator(Translator):
    def __init__(self, outputOption: OutputFormat, glossary: Glossary, sugoiDirectory: str):
        super().__init__(outputOption, glossary)
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
        print("OfflineTranslator: Server Stopped")

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

                japanese = self.glossary.replaceNames(japanese)
                japanese = TextProcessor.removeIndent(japanese)

                english = self.sendTranslationRequest(japanese)
                english = self.glossary.applyCorrections(english)
                englishLines.append(english)

        except Exception as e:
            print(f"An error occurred: {str(e)}")
            sys.exit(1)

        print(f"Translation Complete. Took {perf_counter() - startTime:.3f} seconds, with an average speed of {len(japaneseLines) / (perf_counter() - startTime):.3f} lines per second")

        outputFilePath = TextProcessor.makeOutputFilePath(inputFilePath)
        self.outputOption.writeFile(outputFilePath, japaneseLines, englishLines)