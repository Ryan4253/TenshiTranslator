from abc import ABC

class Glossary(ABC):
    """ High level glossary that allows you to specify translations for specific phrases and also apply corrections
    to the translated text. 

    This is commonly used for names and other jargons that may not be translated correctly.
    """

    def __init__(self):
        pass
    
    def process(self, line: str) -> str:
        """ Process corrections to a line 

        :param line: line to be modified
        :return: process line
        """

        pass