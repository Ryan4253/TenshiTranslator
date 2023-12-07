from abc import ABC, abstractmethod

class OutputFormat(ABC):
    """ Abstract class that defines the interface for output formats
    """
 
    @abstractmethod
    def writeFile(outputFilePath: str, japaneseLines: list[str], englishLines: list[str]):
        """ Writes the translated lines to a file. file will be overwritten if it already exists
        
        :param outputFilePath: path to the output file. 
        :param japaneseLines: list of japanese lines
        :param englishLines: list of translated lines
        """
        pass