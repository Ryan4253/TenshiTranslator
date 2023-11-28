from abc import ABC, abstractmethod

class OutputFormat(ABC):
    @abstractmethod
    def writeFile(outputFilePath: str, japaneseLines: list[str], englishLines: list[str]):
        pass