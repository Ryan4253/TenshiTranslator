from OnlineTranslator import OnlineTranslator
from BatchTranslator import BatchTranslator
from OfflineTranslator import OfflineTranslator
from LineByLineFormat import LineByLineFormat
from EnglishOnlyFormat import EnglishOnlyFormat
from Glossary import Glossary
import subprocess
import time

# Driver Code. Modify as needed
if __name__ == "__main__":
    file = "Chapter_1_preview.txt"
    SUGOI_DIRECTORY = "C:\\Users\\ryanl\\Documents\\Apps\\Sugoi-Translator-Toolkit-V6.0-Anniversary"

    glossary = Glossary('Names.csv', 'Corrections.csv')

    translator = BatchTranslator(LineByLineFormat(), glossary, SUGOI_DIRECTORY)
    translator.translate(file)

    # translator = OfflineTranslator(LineByLineFormat(), glossary, SUGOI_IP)
    # translator.translate(file)
    
    # translator = OnlineTranslator(EnglishOnlyFormat(), glossary)
    # translator.translate(file)