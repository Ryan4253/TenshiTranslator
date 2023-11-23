from OnlineTranslator import OnlineTranslator
from BatchTranslator import BatchTranslator
from OfflineTranslator import OfflineTranslator
from LineByLineFormat import LineByLineFormat
from EnglishOnlyFormat import EnglishOnlyFormat
from Glossary import Glossary

# Driver Code. Modify as needed
if __name__ == "__main__":
    file = "Chapter_1_preview.txt"
    SUGOI_IP = '10.10.18.229:14366'
    
    glossary = Glossary('Names.csv', 'Corrections.csv')

    translator = BatchTranslator(LineByLineFormat(), glossary, SUGOI_IP)
    translator.translate(file)

    # translator = OfflineTranslator(LineByLineFormat(), glossary, SUGOI_IP)
    # translator.translate(file)
    
    # translator = OnlineTranslator(EnglishOnlyFormat(), glossary)
    # translator.translate(file)