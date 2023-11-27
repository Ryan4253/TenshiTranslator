from abc import ABC, abstractmethod

class OutputFormat(ABC):
    def writeFile(outputFilePath: str, japaneseLines: list[str], englishLines: list[str]):
        pass