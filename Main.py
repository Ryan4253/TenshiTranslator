from Constants import *
import OfflineTranslator
import OnlineTranslator
import FileTranslator
import Mouse
import time

def testCursor():
    # Tune Cursor to Japanese 
    # Mouse.setCursor(ONLINE_JAPANESE_X, ONLINE_JAPANESE_Y) 

    # # Tune Cursor to translate button
    # Mouse.setCursor(ONLINE_TL_X, ONLINE_TL_Y)

    # # Tune Cursor to English (Online)
    # Mouse.setCursor(ONLINE_ENGLISH_X, ONLINE_ENGLISH_Y)

    # Tune Cursor to English (Offline)
    Mouse.setCursor(OFFLINE_ENGLISH_X, OFFLINE_ENGLISH_Y)

# Driver Code. Modify as needed
if __name__ == "__main__":
    time.sleep(1)
    file = "Anime_Blu-Ray_Volume_2_SS.txt"

    # Translate using the offline translator
    #start = time.perf_counter()
    #offlineTranslator.translate("Anime_Blu-Ray_Volume_2_SS.txt", "mogus.txt", useVariableTime=True)
    #print(time.perf_counter()-start)
    
    # Translate using the online translator
    #start = time.perf_counter()
    #onlineTranslator.translate(file, "mogus.txt")
    #print(time.perf_counter()-start)


    # Translate using the file translator
    #FileTranslator.preprocessJapanese(file)
    #FileTranslator.postprocessEnglish(file)
    #FileTranslator.mergeOutput(file)
    #FileTranslator.removeIntermediateFiles(file)

    # Test
    #testCursor()
    



