[![Docs](https://github.com/Ryan4253/TenshiTranslator/actions/workflows/docs.yml/badge.svg)](https://github.com/Ryan4253/TenshiTranslator/actions/workflows/docs.yml)
[![Unit Test](https://github.com/Ryan4253/TenshiTranslator/actions/workflows/test.yml/badge.svg)](https://github.com/Ryan4253/TenshiTranslator/actions/workflows/test.yml)
[![codecov](https://codecov.io/gh/Ryan4253/TenshiTranslator/graph/badge.svg?token=G04BIXZ45E)](https://codecov.io/gh/Ryan4253/TenshiTranslator)
[![PyPI version](https://badge.fury.io/py/TenshiTranslator.svg)](https://badge.fury.io/py/TenshiTranslator)

# TenshiTranslator
Sugoi Toolkit's [Sugoi Translator](https://sugoitoolkit.com/) is very effective for ACG (Anime, Comit, Games) media translation as the model is trained with data from the same medium. However, the project lacks automation support as all the features require manual control, which makes large file translation incredibly daunting. This project implements automation utility that interfaces with the translator to both automate the translation process and increase the translation accuracy. This project has since then been adopted by over 10 novel series to generate preliminary machine translations for new novels.  

## Demos
### GUI App (Click For Video)
[![image](https://github.com/Ryan4253/TenshiTranslator/assets/71594512/674100e7-1b61-4a23-9e72-5284a69a4091)](https://www.youtube.com/watch?v=CoYnrSkI5Q0&ab_channel=RyanLiao)

### CLI App
![project](https://github.com/Ryan4253/TenshiTranslator/assets/71594512/263efe3b-5062-4ec2-961e-943658f54ec7)  


## Getting Started
You can download both the CLI and GUI application from the [latest release](https://github.com/Ryan4253/TenshiTranslator/releases/latest) page
To use the code as a Python package, run ```pip install TenshiTranslator```  
For more information, visit the documentation [here](https://ryan4253.github.io/TenshiTranslator/)

## Translator Options

### Online Translator
This translator automates Sugoi Toolkit's [web translator](sugoitranslator.com) with zero extra setup required. However, it is both the slowest and the least accurate due to an older model, api limits, and a character limit.  
![online](https://github.com/Ryan4253/TenshiTranslator/assets/71594512/ee3a442d-a03e-4e27-9075-d0d9a8c627d7)

### Offline Translator
This translator uses Sugoi Toolkit’s offline translation server to perform translations. This translator requires Sugoi Toolkit but is faster than the online translator. It is also more accurate as it uses a newer model and has no character limits. The speed of this translator is dependent on your computer’s hardware, and is generally recommended if you don’t have an Nvidia GPU.   

### Batch Translator
This translator uses Sugoi Toolkit’s offline translation server to perform translations. Files are translated in batches, optimizating translation time by maximizing GPU utilization. This translator requires Sugoi Toolkit and a Nvidia GPU to be useful, but is magnitudes faster than the other translators. You will have to install CUDA and run the setup script to allow the sugoi toolkit to accept batch translation requests. This translator is recommended if you have an Nvidia GPU.

## Features
### Multiple format support  
The translator offers two output formats: english only where the original stucture of the file is preserved, and line by line where each line of Japanese is followed by its translation, accelerating translation checking speed. The package also provide abstraction over outputs so you are free to implement your own formats.  
<br>
![english](https://github.com/Ryan4253/TenshiTranslator/assets/71594512/818d7173-2d3f-49bf-822c-1494beb50dea)  
Example English only format
<br>  
![lbl](https://github.com/Ryan4253/TenshiTranslator/assets/71594512/1b685a9c-6bfd-4274-b894-8e45070d8486)  
Example line by line format

### High level glossary  
You can specify translations for specific phrases and also apply corrections to the translated text to improve translation accuracy. This is commonly used for names and other jargons that may not be translated correctly.  
<br>
![image](https://github.com/Ryan4253/TenshiTranslator/assets/71594512/2be406f1-ed6a-4eef-979f-24940f342ab3)
![image](https://github.com/Ryan4253/TenshiTranslator/assets/71594512/04264b62-1be2-4506-9889-7bb048533723)  
Example replacement & correction with regex

## Requirements
The applications are tested on Windows and are available directly for use
The Python package version requires Python >= 3.10
To use the offline and batch translator, you need to download Sugoi Toolkit from [here](https://www.patreon.com/mingshiba/about)  
To use the batch translator, you need a computer with a Nvidia GPU and [CUDA](https://developer.nvidia.com/cuda-downloads)

## Benchmarks
![benchmark](https://github.com/Ryan4253/TenshiTranslator/assets/71594512/e12ce131-ec07-4de8-a3bb-46bac0a13f41)  
Benchmark is done by measuring the time taken to translate 125 lines. Benchmark is run with an Intel i7-13700k and a Nvidia RTX 3060ti 8G

## Credits
CUDA Installation script is adapted from the work by Tenerezza from the Sugoi Toolkit Discord  
Batch translation is first implemented by [@EagleEye17](https://github.com/EagleEye17), who also gave a lot of suggestions to the overall project  
