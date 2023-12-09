[![Docs](https://github.com/Ryan4253/TenshiTranslator/actions/workflows/docs.yml/badge.svg)](https://github.com/Ryan4253/TenshiTranslator/actions/workflows/docs.yml)
[![Unit Test](https://github.com/Ryan4253/TenshiTranslator/actions/workflows/test.yml/badge.svg)](https://github.com/Ryan4253/TenshiTranslator/actions/workflows/test.yml)
[![codecov](https://codecov.io/gh/Ryan4253/TenshiTranslator/graph/badge.svg?token=G04BIXZ45E)](https://codecov.io/gh/Ryan4253/TenshiTranslator)
[![PyPi](https://img.shields.io/pypi/v/TenshiTranslator)](https://pypi.org/project/TenshiTranslator/)

# TenshiTranslator
This package provides translators that translate files from Japanese into English into various formats using [Sugoi Translator](https://sugoitranslator.com/). This is used by the Otonari no Tenshi-sama fan translation team to generate preliminary machine translations for new novels.

## Translator Options

### Online Translator
This translator automates [sugoitranslator.com](sugoitranslator.com) using selenium. This translator does not require any setup. However, it is both the slowest and the least accurate as it uses an older model and has a character limit of 100 characters per request. Long sentences will be split into multiple requests, and contexts will not be taken into account.
    
### Offline Translator
This translator uses sugoi toolkit’s offline translation server. Files are translated line by line through http requests. This translator requires sugoi toolkit but is faster than the online translator. It is also more accurate as it uses a newer model and has no character limits. The speed of this translator is dependent on your computer’s hardware, and is generally recommended if you don’t have an Nvidia GPU.

### Batch Translator
This translator uses sugoi toolkit’s offline translation server. Files are translated in batches through http requests, optimizating translation time by maximizing GPU utilization. This translator requires sugoi toolkit and a Nvidia GPU to be useful, but is magnitudes faster than the other translators. You will have to install CUDA and run the setup script to allow the sugoi toolkit to accept batch translation requests. This translator is recommended if you have an Nvidia GPU.

## Features
### Multiple format support  
The translator allows you to output translations either in an all english format or in an japanese and english alternate format that speeds up translation checking. The package also provide abstraction over output formats so you are free to implement your own formats.

### High level glossary  
You can specify translations for specific phrases and also apply corrections to the translated text to improve translation accuracy. This is commonly used for names and other jargons that may not be translated correctly.
  
## Requirements
To run the program, you need Python >= 3.10  
To use the offline and batch translator, you need Windows, and have to download Sugoi Toolkit from [here](https://www.patreon.com/mingshiba/about)  
To use the batch translator, you need a computer with a Nvidia GPU, [CUDA](https://developer.nvidia.com/cuda-downloads), then download and run ```sugoiCudaInstall.ps1``` in ```scripts/```

## Installation
You can install the package directly using ```pip install TenshiTranslator```  
Alternatively, clone the repository

## Getting Started
Visit the documentation [here](https://ryan4253.github.io/TenshiTranslator/)

## Benchmarks
