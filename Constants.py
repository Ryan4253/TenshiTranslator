import pyautogui

#Screen Config
SCREEN_LENGTH = 1920
SCREEN_WIDTH = 1080

# Mouse Config
CPS = 10 
pyautogui.FAILSAFE = False

# Pausing Config
PAUSE_KEY = 'esc'

# Cursor Config
OFFLINE_ENGLISH_X = 0.02 * SCREEN_LENGTH
OFFLINE_ENGLISH_Y = 0.05 * SCREEN_WIDTH

ONLINE_JAPANESE_X = 0.22 * SCREEN_LENGTH
ONLINE_JAPANESE_Y = 0.35 * SCREEN_WIDTH
ONLINE_TL_X = 0.75 * SCREEN_LENGTH
ONLINE_TL_Y = 0.25 * SCREEN_WIDTH
ONLINE_ENGLISH_X = 0.22 * SCREEN_LENGTH
ONLINE_ENGLISH_Y = 0.67 * SCREEN_WIDTH

# Timing Config
OFFLINE_PROCESS_TIME = 6 # Time to wait for the translation to generate

ONLINE_PROCESS_TIME = 5 # Time to wait for the translation to generate
ONLINE_WAIT_TIME = 10 # Time to wait between translating lines. This is added to prevent timeouts 
TIMEOUT_WAIT_TIME = 330 # Time to wait if timeout occurrs