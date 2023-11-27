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
    # file = "Chapter_1_preview.txt"
    SUGOI_DIRECTORY = "C:\\Users\\ryanl\\Documents\\Apps\\Sugoi-Translator-Toolkit-V6.0-Anniversary"

    # glossary = Glossary('Names.csv', 'Corrections.csv')

    # translator = BatchTranslator(LineByLineFormat(), glossary, SUGOI_DIRECTORY)
    # translator.translate(file)

    # # translator = OfflineTranslator(LineByLineFormat(), glossary, SUGOI_IP)
    # # translator.translate(file)
    
    # # translator = OnlineTranslator(EnglishOnlyFormat(), glossary)
    # # translator.translate(file)

    # server = subprocess.Popen(
    #     ['python', '']
    #     creationflags=subprocess.CREATE_NO_WINDOW,
    # )

    p = subprocess.Popen(['python', 'api.py'], stdout=subprocess.PIPE, creationflags=subprocess.CREATE_NO_WINDOW)
    data = {'Message': 'Translate', 
            'Translator': 'Batch',
            'BatchSize': 64,
            'SugoiDirectory': 'C:\\Users\\ryanl\\Documents\\Apps\\Sugoi-Translator-Toolkit-V6.0-Anniversary',
            'GlossaryNames': 'Names.csv',
            'GlossaryCorrections': 'Corrections.csv',
            'OutputFormat': 'LineByLine',
            'Files': ['sources/yume-no-ukihashi.txt', 'sources/Chapter_1_preview.txt']}

    headers = {'content-type': 'application/json'}
    requests.post(f'http://127.0.0.1:5000/', data=json.dumps(data), headers=headers)

    p.kill()

    for line in p.stdout:
        print ("test:", line.decode())
    
    