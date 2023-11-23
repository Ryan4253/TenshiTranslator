import re
import os
import sys

def retrieveLines(inputFilePath: str) -> list[str]:
    lines = []
    try:
        with open(inputFilePath, 'r', encoding='utf8') as file:
            for line in file:
                lines.append(line)

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        sys.exit(1)

    return lines

def makeOutputFilePath(inputFilePath: str) -> str:
    return os.path.splitext(inputFilePath)[0] + "-Translated.txt"

"""
Checks if a sentence is empty
"""
def isEmptyLine(line: str) -> bool:
    return not line.strip()

"""
Removes indent from a sentence
"""
def removeIndent(line: str) -> str:
    return line[1:] if line[0] == '　' else line

"""
Checks if the sentences provided is a timeout message the SugoiTL site
"""
def isTimeoutMessage(line: str) -> bool:
    return line.count('discord.gg') != 0

"""
Splits a Japanese paragraph into smaller sentences if it is longer than the max allowed length.
This is used to comply with SugoiTL online translator's 100 character limit
"""
def splitToSentence(line: str, maxLength: int) -> list:
    if len(line) <= maxLength:
        return [line]
    
    return [sentence + '。' for sentence in line.split('。') if sentence and sentence != '\n']

"""
Check if a sentence contains no Japanese characters
"""
def noJapaneseCharacters(line: str) -> bool:
    pattern = re.compile(r'[\u3040-\u30ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff\uff66-\uff9f]')
    return re.search(pattern, line) is None
