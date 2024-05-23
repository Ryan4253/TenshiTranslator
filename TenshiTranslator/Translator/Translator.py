from abc import ABC, abstractmethod
from TenshiTranslator.OutputFormat.OutputFormat import OutputFormat
from TenshiTranslator.Glossary.Glossary import Glossary


class Translator(ABC):  
    """ Abstract class for translators that translates a file
    
    :param outputOption: the output format to use
    :param preprocessGlossary: the glossary to use for preprocessing
    :param postProcessGlossary: the glossary to use for postprocessing
    """

    def __init__(self, outputOption: OutputFormat, preprocessGlossary: Glossary, postProcessGlossary: Glossary):
        self.outputOption = outputOption
        self.preprocessGlossary = preprocessGlossary
        self.postProcessGlossary = postProcessGlossary
        

    def translate(self, inputFilePath: str):
        """ Translates a file and writes to inputFilePath-Translated.txt
    
        :param inputFilePath: path to the file to be translated
        """

        pass