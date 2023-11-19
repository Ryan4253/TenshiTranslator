import pyautogui

#Screen Config
SCREEN_LENGTH = 1920
SCREEN_WIDTH = 1080

# Mouse Config
CPS = 100 
pyautogui.FAILSAFE = False

# Keyboard Config
PAUSE_KEY = 'esc'

# Cursor Config
OFFLINE_ENGLISH_X = 0.02 * SCREEN_LENGTH
OFFLINE_ENGLISH_Y = 0.05 * SCREEN_WIDTH

# Constant Timing Config
OFFLINE_PROCESS_TIME = 6
TIMEOUT_WAIT_TIME = 330

# Offline Variable Timing Config. You will have to go into timing.py to edit the function
OFFLINE_MAX_PROCESS_TIME = 30

# Website Config
SUGOI_TL_URL = "https://sugoitranslator.com/"
SWAP_LANGUAGE_BUTTON_XPATH = "//*[@id=\"routify-app\"]/div[1]/div/div[1]/div/div/div[2]/button"
TRANSLATE_BUTTON_XPATH = "//*[@id=\"routify-app\"]/div[1]/div/div[1]/div/div/div[2]/button"
INPUT_BOX_XPATH = "//*[@id=\"routify-app\"]/div[1]/div/div[2]/div/div[1]"
OUTPUT_BOX_XPATH = "//*[@id=\"routify-app\"]/div[1]/div/div[2]/div/div[2]"