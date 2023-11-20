from abc import ABC, abstractmethod
from FileOutput import FileOutput

class Translator(ABC):  
    def __init__(self, outputOption : FileOutput):
        self.outputOption = outputOption
        
    def translate(self, inputFileName: str):
        pass
