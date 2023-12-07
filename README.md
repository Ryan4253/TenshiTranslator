[![Unit Test](https://github.com/Ryan4253/TenshiTranslator/actions/workflows/test.yml/badge.svg)](https://github.com/Ryan4253/TenshiTranslator/actions/workflows/test.yml)
[![codecov](https://codecov.io/gh/Ryan4253/TenshiTranslator/graph/badge.svg?token=G04BIXZ45E)](https://codecov.io/gh/Ryan4253/TenshiTranslator)

#TenshiTranslator
This automatically translates a file with Japanese into English line by line using the [Sugoi Translator](https://sugoitranslator.com/). This is used by the Otonari no Tenshi-sama fan translation team to generate preliminary machine translations for new novels.

## Translator Options

### Online Translator

### Offline Translator

### Batch Translator

## Features
1. Multiple format support
2. High level glossary
3. Batch Translation
4. GUI Support

## Requirements

## Dependencies
selenium - automatically controls website given commands
chromedriver-autoinstaller - automatically installs driver for chromium for selenium
requests - https request processing for backend communication
Flask - backend server setup to communicate with frontend

## How to use
1. Download this package using ```pip install TenshiTranslator```
2. Prepare input file.  
The input file should be lines of Japanese with paragraphs separated with a blank line. Usually running OCR will give the desired format. Then, place the file in the same folder as the translator.  
![image](https://user-images.githubusercontent.com/71594512/212532224-89023b94-ec7a-4b4c-8fee-dceb2d1f6187.png)
3. Run the code, and switch to the tab with Sugoi TL. The translation process should run until the entire file is translated.

## Benchmarks
