# otonari-ln-translator

## About the project
This automatically translates a file with Japanese into English line by line using the [Sugoi Translator](https://sugoitranslator.com/). This is used by the Otonari no Tenshi-sama fan translation team to generate preliminary machine translations for new novels.

## Features
1. Timeout detection  
If a 'too many requests' timeout is detected on Sugoi TL, the translation will automatically pause and resume after 5 minutes.  
2. Name translation disruption prevention  
Sometimes kanji names are misinterpreted by Sugoi TL as they have connotations (e.g Mahiru vs mid day). This translator replaces all registered names with temporary placeholders (usually the name in katakana) so they will be recognized as names and not disrupt the translation. The placeholder names are then replaced with the English character names.

## Dependencies
pyautogui - for cursor / keyboard simulation  
pyperclip - to interface copy / paste clipboard with python  

You can install these dependencies using these two commands:
```
pip install pyautogui
pip install pyperclip
```

## How to use
1. Download translator.py and install dependencies.  
2. Configure the following constants to interface with Sugoi Translator.  
Pixel count of your monitor. This is used so you are interfacing with percentages when setting cursor locations.  
![image](https://user-images.githubusercontent.com/71594512/212532529-ae794522-ee2a-4942-b61f-d3fd26d4dc37.png)  
Then, you need to set the cursor location so that the it lands in the correct positions on the Sugoi TL site. Right is +x and down is +y. Use the 3 commented out methods in the main code to see if the cursor lands in the spots specified below.
![image](https://user-images.githubusercontent.com/71594512/212532591-6d17df33-f534-4dbe-a798-47c361ad69b9.png)![image](https://user-images.githubusercontent.com/71594512/212532634-b87c300f-8a18-4b0a-bce1-5e37d568a740.png)
![image](https://user-images.githubusercontent.com/71594512/212532373-398d72f7-6e6f-4a14-8d4c-bf433622569c.png)

3. Prepare input file.  
The input file should be lines of Japanese with paragraphs separated with a blank line. Usually running OCR will give the desired format. Then, place the file in the same folder as the translator.  
![image](https://user-images.githubusercontent.com/71594512/212532224-89023b94-ec7a-4b4c-8fee-dceb2d1f6187.png)
4. Run the code, and switch to the tab with Sugoi TL. The translation process should run until the entire file is translated.
