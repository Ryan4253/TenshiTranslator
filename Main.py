from OnlineTranslator import OnlineTranslator
from BatchTranslator import BatchTranslator
from OfflineTranslator import OfflineTranslator
import Constants
from LineByLineFormat import LineByLineFormat
from EnglishOnlyFormat import EnglishOnlyFormat

# Driver Code. Modify as needed
if __name__ == "__main__":
    file = "Chapter_1_preview.txt"
    SUGOI_IP = '10.10.18.229:14366'
    
    translator = BatchTranslator(EnglishOnlyFormat(), SUGOI_IP)
    translator.translate(file)

    # translator = OfflineTranslator(LineByLineFormat(), Constants.SUGOI_IP)
    # translator.translate(file)
    
    # translator = OnlineTranslator(EnglishOnlyFormat(), Constants.TIMEOUT_WAIT_TIME)
    # translator.translate(file)



