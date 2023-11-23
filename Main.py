from OnlineTranslator import OnlineTranslator
from BatchTranslator import BatchTranslator
from OfflineTranslator import OfflineTranslator
import Constants
from LineByLineFormat import LineByLineFormat
from EnglishOnlyFormat import EnglishOnlyFormat

# Driver Code. Modify as needed
if __name__ == "__main__":
    file = "Chapter_1_preview.txt"
    
    translator = BatchTranslator(EnglishOnlyFormat(), Constants.SUGOI_IP, Constants.BATCH_SIZE)
    translator.translate(file)

    # translator = OfflineTranslator(LineByLineFormat(), Constants.SUGOI_IP)
    # translator.translate(file)
    
    # translator = OnlineTranslator(EnglishOnlyFormat(), Constants.TIMEOUT_WAIT_TIME)
    # translator.translate(file)



