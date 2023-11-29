## @package Glossary
#  Contains the glossary class

import csv
import re
import sys

## High level glossary that allows you to specify translations for specific phrases and also apply corrections
#  to the translated text. This is commonly used for names and other jargons that may not be translated correctly.
#  The glossary is loaded from two .csv files, one for replacements and one for post translation corrections.
#  Name replacement is done directly, while corrections are done using regex. The .csv files must be in the format 
#  of <input>,<output>, with each entry separated by a new line.
class Glossary:
    ## Constructor
    #
    #  @param namePath path to the .csv file containing the name replacements
    #  @param correctionPath path to the csv file containing the post translation corrections
    #  @exception FileNotFoundError if any file is not found
    def __init__(self, namePath: str, correctionPath: str):
        self.names = dict()
        self.corrections = dict()

        try:
            with open(namePath, 'r', encoding='utf8', newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                for (nameInput, nameOutput) in reader:
                    self.names[nameInput] = nameOutput

            with open(correctionPath, 'r', encoding='utf8', newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                for (pattern, correction) in reader:
                    self.corrections[pattern] = correction
        
        except Exception as e:
            print(f'An error occurred: {e}', flush=True)
            sys.exit(1)
    
    ## Replaces names in a line
    #
    #  @param line line to be modified
    #  @return line with names replaced according to the loaded csv file
    def replaceNames(self, line: str) -> str:
        for nameInput, nameOutput in self.names.items():
            line = line.replace(nameInput, nameOutput)
        
        return line
    
    ## Apply corrections in a line using regex
    #
    #  @param line line to be modified
    #  @return line corrected according to the loaded csv file
    def applyCorrections(self, line: str) -> str:
        for pattern, correction in self.corrections.items():
            line = re.sub(pattern, correction, line)
    
        return line