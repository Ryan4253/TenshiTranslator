## @package BatchTranslator
#  Contains the BatchTranslator class

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

## Translator that uses sugoi toolkit's offline translation server. Files are translated in batches through 
#  http requests, optimization translation time by maximizing GPU utilization. This translator requires sugoi 
#  toolkit and a Nvidia GPU to be useful, but is magnitudes faster than the other translators. You 
#  will have to install CUDA and run the setup script to allow the sugoi toolkit to accept batch translation 
#  requests. This translator is recommended if you have an Nvidia GPU.
class BatchTranslator(Translator):
    ## Constructor. Takes around 12 seconds to start the sugoi offline translator server.
    #
    #  @param outputOption the output format to use
    #  @param glossary the glossary to use
    #  @param sugoiDirectory the path to the sugoi toolkit
    #  @param batchSize the number of lines to translate per request, defaults to 64
    def __init__(self, outputOption: OutputFormat, glossary: Glossary, sugoiDirectory: str, batchSize: int = 64):
        super().__init__(outputOption, glossary)
        self.batchSize = batchSize
        self.sugoiDirectory = sugoiDirectory
        self.host = '127.0.0.1:14366'

        print("BatchTranslator: Starting Server...", flush=True)
        self.server = subprocess.Popen(
            self.sugoiDirectory + "\\Code\\backendServer\\Program-Backend\\Sugoi-Japanese-Translator\\offlineTranslation\\activateOfflineTranslationServer.bat", 
            cwd=self.sugoiDirectory + "\\Code\\backendServer\\Program-Backend\\Sugoi-Japanese-Translator\\offlineTranslation", 
            creationflags=subprocess.CREATE_NO_WINDOW
        )
        sleep(12)
        print("BatchTranslator: Server Started", flush=True)

    ## Destructor, stops the sugoi offline translator server
    def __del__(self):
        print("BatchTranslator: Stopping Server...", flush=True)
        self.server.kill()
        sleep(3)
        print("BatchTranslator: Server Stopped", flush=True)

    
    ## Translates a batch from japanese to english using the sugoi offline translator server
    # 
    #  @param batch of japanese lines to be translated
    #  @return the translated batch
    def sendTranslationRequest(self, batch: list[str]) -> list[str]:
        data = {'message': 'batch translate', 'content': batch}
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
            batch = []

            for index, japanese in enumerate(japaneseLines):
                japanese = self.glossary.replaceNames(japanese)
                japanese = TenshiTranslator.Util.TextProcessor.removeIndent(japanese)

                batch.append(japanese)

                if(len(batch) >= 64 or index == len(japaneseLines)-1):
                    englishLines.extend(self.sendTranslationRequest(batch))
                    print(f'Current File: {os.path.basename(inputFilePath)}, Progress: {index+1}/{len(japaneseLines)} lines', flush=True)
                    batch.clear()

            englishLines = [self.glossary.applyCorrections(english) for english in englishLines]

        except Exception as e:
            print(f"An error occurred: {str(e)}", flush=True)
            sys.exit(1)

        print(f"Translation Complete. Took {perf_counter() - startTime:.3f} seconds, with an average speed of {len(japaneseLines) / (perf_counter() - startTime):.3f} lines per second\n", flush=True)

        outputFilePath = TenshiTranslator.Util.TextProcessor.makeOutputFilePath(inputFilePath)
        self.outputOption.writeFile(outputFilePath, japaneseLines, englishLines)