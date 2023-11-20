from OnlineTranslator import OnlineTranslator
from BatchTranslator import BatchTranslator
from OfflineTranslator import OfflineTranslator
import Constants

# Driver Code. Modify as needed
if __name__ == "__main__":
    file = "Chapter_1_preview.txt"
    
    # translator = BatchTranslator(Constants.SUGOI_IP, Constants.BATCH_SIZE)
    # translator.translate(file)

    # translator = OfflineTranslator(Constants.SUGOI_IP)
    # translator.translate(file)
    
    # translator = OnlineTranslator(Constants.TIMEOUT_WAIT_TIME)
    # translator.translate(file)

    # Translate using the online translator
    #OnlineTranslator.translate(file)



