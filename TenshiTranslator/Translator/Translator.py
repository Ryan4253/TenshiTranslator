## @module Translator
#  Contains the Translator abstract class

from abc import ABC, abstractmethod
from TenshiTranslator.OutputFormat.OutputFormat import OutputFormat
from TenshiTranslator.Util.Glossary import Glossary

## Abstract class for translators that translates a file
class Translator(ABC):  
    ## Constructor
    #
    #  @param outputOption the output format to use
    #  @param glossary the glossary to use
    def __init__(self, outputOption: OutputFormat, glossary: Glossary):
        self.outputOption = outputOption
        self.glossary = glossary
        
    ## Translates the file and writes to inputFilePath-Translated.txt
    #
    #  @param inputFilePath path to the file to be translated
    def translate(self, inputFilePath: str):
        pass