## @package OutputFormat
#  Contains the OutputFormat abstract class

from abc import ABC, abstractmethod

## Abstract class that defines the interface for output formats
class OutputFormat(ABC):
    ## writes the translated lines to a file. file will be overwritten if it already exists
    #
    #  @param outputFilePath path to the output file. 
    #  @param japaneseLines list of japanese lines
    #  @param englishLines list of translated lines
    @abstractmethod
    def writeFile(outputFilePath: str, japaneseLines: list[str], englishLines: list[str]):
        pass