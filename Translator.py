from abc import ABC, abstractmethod
from OutputFormat import OutputFormat
from Glossary import Glossary

class Translator(ABC):  
    def __init__(self, outputOption: OutputFormat, glossary: Glossary):
        self.outputOption = outputOption
        self.glossary = glossary
        
    def translate(self, inputFileName: str):
        pass