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

class OfflineTranslator(Translator):
    """ Translator that uses sugoi toolkit's offline translation server. 
    
    Files are translated line by line through http requests. This translator requires sugoi toolkit but is faster than the online 
    translator. It is also more accurate as it uses a newer model and has no character limits. The speed of this translator is 
    dependent on your computer's hardware, and is generally recommended if you don't have an Nvidia GPU. The object takes around
    12 seconds to initialize, as it starts the sugoi offline translator server.
    
    :param outputOption: the output format to use
    :param glossary: the glossary to use
    :param sugoiDirectory: the path to the sugoi toolkit
    """

    def __init__(self, outputOption: OutputFormat, glossary: Glossary, sugoiDirectory: str):
        super().__init__(outputOption, glossary)
        self.sugoiDirectory = sugoiDirectory
        self.host = '127.0.0.1:14366'

        print("OfflineTranslator: Starting Server...", flush=True)
        self.server = subprocess.Popen(
            self.sugoiDirectory + "\\Code\\backendServer\\Program-Backend\\Sugoi-Japanese-Translator\\offlineTranslation\\activateOfflineTranslationServer.bat", 
            cwd=self.sugoiDirectory + "\\Code\\backendServer\\Program-Backend\\Sugoi-Japanese-Translator\\offlineTranslation", 
            creationflags=subprocess.CREATE_NO_WINDOW
        )
        sleep(12)
        print("OfflineTranslator: Server Started", flush=True)

    def __del__(self):
        """ Destructor, stops the sugoi offline translator server
        """

        print("OfflineTranslator: Stopping Server...", flush=True)
        headers = {'content-type': 'application/json'}
        data = {'message': 'close server', 'content': 1}
        requests.post(f'http://{self.host}/', data=json.dumps(data), headers=headers)
        sleep(3)
        print("OfflineTranslator: Server Stopped", flush=True)

    def sendTranslationRequest(self, japanese: str) -> str:
        """ Translates a string from japanese to english using the sugoi offline translator server

        :param japanese: the string to be translated
        :return: the translated string
        """
        
        data = {'message': 'translate sentences', 'content': japanese}
        headers = {'content-type': 'application/json'}
        response = requests.post(f'http://{self.host}/', data=json.dumps(data), headers=headers)

        if response.status_code != 200:
            print(f"Translation request failed with status code {response.status_code}", flush=True)
            return []
        
        return response.json()

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