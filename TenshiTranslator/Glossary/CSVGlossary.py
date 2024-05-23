from TenshiTranslator.Glossary.Glossary import Glossary

import csv
import re
import sys

class CSVGlossary(Glossary):
    """ Glossary with inputs from CSV files

    The glossary is loaded from a CSV file
    Processing is done using regex. The CSV file must be in the format <input>,<output>, with each entry separated by a new line.
    
    :param processPath: path to the .csv file containing processing replacements
    :raises: FileNotFoundError if any file is not found
    """

    def __init__(self, processPath: str):
        self.processes = dict()

        try:
            with open(processPath, 'r', encoding='utf8', newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                for (processInput, processOutput) in reader:
                    self.processes[processInput] = processOutput
        
        except Exception as e:
            print(f'An error occurred: {e}', flush=True)
            sys.exit(1)
    
    def process(self, line: str) -> str:
        """ Apply corrections to a line using regex

        :param line: line to be modified
        :return: line corrected according to the loaded csv file
        """

        for pattern, correction in self.processes.items():
            line = re.sub(pattern, correction, line)
        
        return line
