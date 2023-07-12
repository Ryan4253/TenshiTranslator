import Names
import os.path
from TextProcessor import *

"""
Processes a Japanese file by replacing all the names with its english counterpart, as specified in Names.py
Result is stored in a new file '[Name]-preprocess.txt'
Use the file name of the original file, all the postfix will be handled automaticaly
"""
def preprocessJapanese(file: str):
    outputFile = os.path.splitext(file)[0] + "-preprocess.txt"
    with open(file, 'r', encoding='utf8') as file, open(outputFile, 'w', encoding='utf8') as output:
        for line in file:
            processed = replaceText(line, Names.JAPANESE_TO_ENGLISH)
            output.write(processed)

"""
Processes an English file by fixing all the translated english names, as specified in Names.py
Result is stored in a new file '[Name]-english.txt'
Use the file name of the original file, all the postfix will be handled automaticaly
"""
def postprocessEnglish(file: str):
    outputFile = os.path.splitext(file)[0] + "-english.txt"
    file = os.path.splitext(file)[0] + '-preprocess_output.txt'
    with open(file, 'r', encoding='utf8') as englishLines, open(outputFile, 'w', encoding='utf8') as output:
        for english in englishLines:
            processed = replaceTextRegex(english, Names.ENGLISH_CORRECTION)
            output.write(processed)

    os.remove(file)

"""
Merges a Japanese file with the processed English file to create a line by line translation file
Result is stored in a new file '[Name]-Translated.txt'
Use the file name of the original file, all the postfix will be handled automaticaly
"""
def mergeOutput(file: str):
    outputFile = os.path.splitext(file)[0] + "-Translated.txt"
    englishFile = os.path.splitext(file)[0] + "-english.txt"
    japaneseFile = file

    with open(japaneseFile, 'r', encoding='utf8') as japaneseLines, \
         open(englishFile, 'r', encoding='utf8') as englishLines, \
         open(outputFile, 'w', encoding='utf8') as output:
        for japanese, english in zip(japaneseLines, englishLines):
            if isEmptyLine(japanese):
                output.write('\n')
                continue

            if not hasJapaneseCharacters(japanese):
                output.write(japanese)
                output.write('\n')
                continue

            output.write(japanese)
            output.write(english)
            output.write('\n')
    
    os.remove(englishFile)

"""
Removes all the intermediate files generated during the file translation process
"""
def removeIntermediateFiles(file: str):
    if os.path.isfile(os.path.splitext(file)[0] + "-preprocess.txt"):
        os.remove(os.path.splitext(file)[0] + "-preprocess.txt")

    if os.path.isfile(os.path.splitext(file)[0] + '-preprocess_output.txt'):
        os.remove(os.path.splitext(file)[0] + '-preprocess_output.txt')

    if os.path.isfile(os.path.splitext(file)[0] + "-english.txt"):
        os.remove(os.path.splitext(file)[0] + "-english.txt")


