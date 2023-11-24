from OnlineTranslator import OnlineTranslator
from BatchTranslator import BatchTranslator
from OfflineTranslator import OfflineTranslator
from LineByLineFormat import LineByLineFormat
from EnglishOnlyFormat import EnglishOnlyFormat
from Glossary import Glossary
import subprocess
import time

import requests
import json

# Driver Code. Modify as needed
if __name__ == "__main__":
    file = "Chapter_1_preview.txt"
    SUGOI_DIRECTORY = "C:\\Users\\ryanl\\Desktop\\Sugoi Translator"

    # p = subprocess.Popen(SUGOI_DIRECTORY + "\\Code\\backendServer\\Program-Backend\\Sugoi-Japanese-Translator\\offlineTranslation\\activateOfflineTranslationServer.bat", 
    #                     cwd=SUGOI_DIRECTORY + "\\Code\\backendServer\\Program-Backend\\Sugoi-Japanese-Translator\\offlineTranslation", 
    #                     creationflags=subprocess.CREATE_NO_WINDOW)

    #time.sleep(10)

    glossary = Glossary('Names.csv', 'Corrections.csv')

    translator = OfflineTranslator(LineByLineFormat(), glossary, SUGOI_DIRECTORY)
    translator.translate(file)

    # data = {'message': 'close server'}
    # headers = {'content-type': 'application/json'}
    # response = requests.post(f'http://{SUGOI_IP}/', data=json.dumps(data), headers=headers)
    # time.sleep(5)

    # translator = OfflineTranslator(LineByLineFormat(), glossary, SUGOI_IP)
    # translator.translate(file)
    
    # translator = OnlineTranslator(EnglishOnlyFormat(), glossary)
    # translator.translate(file)