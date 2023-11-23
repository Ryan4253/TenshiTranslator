from abc import ABC, abstractmethod
from OutputFormat import OutputFormat

class Translator(ABC):  
    def __init__(self, outputOption : OutputFormat):
        self.outputOption = outputOption
        
    def translate(self, inputFileName: str):
        pass
