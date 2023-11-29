## @package OfflineTranslator
#  Contains the OfflineTranslator class

from TenshiTranslator.Translator.Translator import Translator
from TenshiTranslator.OutputFormat.OutputFormat import OutputFormat
from TenshiTranslator.Util.Glossary import Glossary
import TenshiTranslator.Util.TextProcessor

from time import perf_counter, sleep
import requests
import json
import sys
import subprocess
import os

## Translator that uses sugoi toolkit's offline translation server. Files are translated line by line through http requests.
#  This translator requires sugoi toolkit but is faster than the online translator. It is also more accurate as it uses
#  a newer model and has no character limits. The speed of this translator is dependent on your computer's hardware, and is 
#  generally recommended if you don't have an Nvidia GPU.
class OfflineTranslator(Translator):
    ## Constructor. Takes around 12 seconds to start the sugoi offline translator server.
    #
    #  @param outputOption the output format to use
    #  @param glossary the glossary to use
    #  @param sugoiDirectory the path to the sugoi toolkit
    def __init__(self, outputOption: OutputFormat, glossary: Glossary, sugoiDirectory: str):
        super().__init__(outputOption, glossary)
        self.sugoiDirectory = sugoiDirectory
        self.host = '127.0.0.1:14366'

        print("OfflineTranslator: Starting Server...")
        self.server = subprocess.Popen(
            self.sugoiDirectory + "\\Code\\backendServer\\Program-Backend\\Sugoi-Japanese-Translator\\offlineTranslation\\activateOfflineTranslationServer.bat", 
            cwd=self.sugoiDirectory + "\\Code\\backendServer\\Program-Backend\\Sugoi-Japanese-Translator\\offlineTranslation", 
            creationflags=subprocess.CREATE_NO_WINDOW
        )
        sleep(12)
        print("OfflineTranslator: Server Started", flush=True)

    ## Destructor, stops the sugoi offline translator server
    def __del__(self):
        print("OfflineTranslator: Stopping Server...", flush=True)
        self.server.kill()
        sleep(3)
        print("OfflineTranslator: Server Stopped", flush=True)

    ## Translates a string from japanese to english using the sugoi offline translator server
    # 
    #  @param japanese the string to be translated
    #  @return the translated string
    def sendTranslationRequest(self, japanese: str) -> str:
        data = {'message': 'translate sentences', 'content': japanese}
        headers = {'content-type': 'application/json'}
        response = requests.post(f'http://{self.host}/', data=json.dumps(data), headers=headers)

        if response.status_code != 200:
            print(f"Translation request failed with status code {response.status_code}", flush=True)
            return []
        
        return response.json()

    ## Translates a file and writes to inputFilePath-Translated.txt
    #
    #  @param inputFilePath path to the file to be translated
    #  @exception FileNotFoundError if the file is not found
    #  @exception Exception if any other error occurs
    def translate(self, inputFilePath: str):
        startTime = perf_counter()
        japaneseLines = TenshiTranslator.Util.TextProcessor.retrieveLines(inputFilePath)
        englishLines = []

        try:
            for index, japanese in enumerate(japaneseLines):
                print(f'Current File: {os.path.basename(inputFilePath)}, Progress: {index+1}/{len(japaneseLines)} lines', flush=True)

                japanese = self.glossary.replaceNames(japanese)
                japanese = TenshiTranslator.Util.TextProcessor.removeIndent(japanese)

                english = self.sendTranslationRequest(japanese)
                english = self.glossary.applyCorrections(english)
                englishLines.append(english)

        except Exception as e:
            print(f"An error occurred: {str(e)}", flush=True)
            sys.exit(1)

        print(f"Translation Complete. Took {perf_counter() - startTime:.3f} seconds, with an average speed of {len(japaneseLines) / (perf_counter() - startTime):.3f} lines per second\n", flush=True)

        outputFilePath = TenshiTranslator.Util.TextProcessor.makeOutputFilePath(inputFilePath)
        self.outputOption.writeFile(outputFilePath, japaneseLines, englishLines)