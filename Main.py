from OnlineTranslator import OnlineTranslator
from BatchTranslator import BatchTranslator
import Constants
from OfflineTranslator import OfflineTranslator

# Driver Code. Modify as needed

if __name__ == "__main__":
    file = "Chapter_1_preview.txt"
    
    # translator = BatchTranslator(Constants.BATCH_SIZE, Constants.SUGOI_IP)
    # translator.translate(file)

    # translator = OfflineTranslator(Constants.SUGOI_IP)
    # translator.translate(file)
    
    translator = OnlineTranslator(330)
    translator.translate(file)


    # Translate using the online translator
    #OnlineTranslator.translate(file)



