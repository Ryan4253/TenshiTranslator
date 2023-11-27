import csv
import re
import sys

class Glossary:
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
    
    def replaceNames(self, line: str) -> str:
        for nameInput, nameOutput in self.names.items():
            line = line.replace(nameInput, nameOutput)
        
        return line
    
    def applyCorrections(self, line: str) -> str:
        for pattern, correction in self.corrections.items():
            line = re.sub(pattern, correction, line)
    
        return line