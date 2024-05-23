from TenshiTranslator.Glossary.Glossary import Glossary

class PassthroughGlossary(Glossary):
    """ Passthrough glossary that does not perform any modifications to the text. """
    
    def __init__(self):
        pass
    
    def process(self, line: str) -> str:
        """ Process corrections to a line 

        :param line: line to be modified
        :return: process line
        """

        return line