from TenshiTranslator.UI.StdoutRedirector import StdoutRedirector

from TenshiTranslator.OutputFormat.OutputFormat import OutputFormat
from TenshiTranslator.Glossary.Glossary import Glossary
from TenshiTranslator.Translator.OnlineTranslator import OnlineTranslator
from TenshiTranslator.Translator.BatchTranslator import BatchTranslator
from TenshiTranslator.Translator.OfflineTranslator import OfflineTranslator

import multiprocessing
import sys

class TranslatorConfig:
    """ Configuration for a translation process.
    """

    def __init__(self, translatorType: str, preprocessGlossary: Glossary, postprocessGlossary: Glossary, 
                 outputFormat: OutputFormat, sugoiDirectory: str, timeout: int, batchSize: int):
        """ Initializes the translator configuration.

        :param translatorType: the type of translator to use
        :param preprocessGlossary: the preprocess glossary to use
        :param postprocessGlossary: the postprocess glossary to use
        :param outputFormat: the output format to use
        :param sugoiDirectory: the directory containing the Sugoi translator
        :param timeout: the timeout for the translation model
        :param batchSize: the batch size for the translation model
        """

        self.translatorType = translatorType
        self.preprocessGlossary = preprocessGlossary
        self.postprocessGlossary = postprocessGlossary
        self.outputFormat = outputFormat
        self.sugoiDirectory = sugoiDirectory
        self.timeout = timeout
        self.batchSize = batchSize

class TranslationProcess(multiprocessing.Process):
    """ A process that translates a list of files.
    """

    def __init__(self, translatorConfig: TranslatorConfig, files: list[str]):
        """ Initializes the translation process.
        """

        super().__init__()
        self.translatorConfig = translatorConfig
        self.files = files
        self.outputBuffer = multiprocessing.Queue()

    def run(self):
        """ Translates the list of files using the translator configuration.
        """

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

    def getBuffer(self) -> multiprocessing.Queue:
        """ Gets the output buffer.

        :return: the output buffer
        """

        return self.outputBuffer

    def buildTranslator(self):
        """ Builds the translator based on the translator configuration.
        """

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