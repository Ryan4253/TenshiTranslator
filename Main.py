from Constants import *
import TextProcessor
import OfflineTranslator
import OnlineTranslator
import Names
import Mouse
import time

# Driver Code. Modify as needed
if __name__ == "__main__":
    # Delay so you can tab to the sugoi page
    time.sleep(1)

    # Translate File
    OfflineTranslator.translate('in.txt', 'out.txt')

    # Tune Cursor to Japanese 
    #Mouse.setCursor(ONLINE_JAPANESE_X, ONLINE_JAPANESE_Y) 

    # Tune Cursor to translate button
    #Mouse.setCursor(ONLINE_TL_X, ONLINE_TL_Y)

    # Tune Cursor to English (Online)
    #Mouse.setCursor(ONLINE_ENGLISH_X, ONLINE_ENGLISH_Y)

    # Tune Cursor to English (Offline)
    #Mouse.setCursor(OFFLINE_ENGLISH_X, OFFLINE_ENGLISH_Y)
