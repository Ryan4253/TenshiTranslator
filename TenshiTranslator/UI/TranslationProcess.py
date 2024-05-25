from TenshiTranslator.UI.StdoutRedirector import StdoutRedirector

from TenshiTranslator.Translator.OnlineTranslator import OnlineTranslator
from TenshiTranslator.Translator.BatchTranslator import BatchTranslator
from TenshiTranslator.Translator.OfflineTranslator import OfflineTranslator

import multiprocessing
import sys

class TranslatorConfig:
    def __init__(self, translatorType, preprocessGlossary, postprocessGlossary, outputFormat, sugoiDirectory, timeout, batchSize):
        self.translatorType = translatorType
        self.preprocessGlossary = preprocessGlossary
        self.postprocessGlossary = postprocessGlossary
        self.outputFormat = outputFormat
        self.sugoiDirectory = sugoiDirectory
        self.timeout = timeout
        self.batchSize = batchSize

class TranslationProcess(multiprocessing.Process):
    def __init__(self, translatorConfig, files):
        super().__init__()
        self.translatorConfig = translatorConfig
        self.files = files
        self.outputBuffer = multiprocessing.Queue()

    def run(self):
        sys.stdout = StdoutRedirector(self.outputBuffer)
        
        try:
            translator = self.buildTranslator()
            for file in self.files:
                translator.translate(file)
        except Exception as e:
            error_message = f"Error occurred during translation: {str(e)}"
            print(error_message)
        finally:
            sys.stdout = sys.__stdout__ 

    def getBuffer(self):
        return self.outputBuffer

    def buildTranslator(self):
        config = self.translatorConfig
        if config.translatorType == "Online":
            return OnlineTranslator(config.outputFormat, 
                                    config.preprocessGlossary, 
                                    config.postprocessGlossary, 
                                    config.timeOut)
        
        if config.translatorType == "Offline":
            return OfflineTranslator(config.outputFormat, 
                                     config.preprocessGlossary, 
                                     config.postprocessGlossary, 
                                     config.sugoiDirectory)
    
        if config.translatorType == "Batch":
            return BatchTranslator(config.outputFormat, 
                                   config.preprocessGlossary, 
                                   config.postprocessGlossary, 
                                   config.sugoiDirectory,
                                   config.batchSize) 
    
        return None