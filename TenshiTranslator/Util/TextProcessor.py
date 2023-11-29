## @module TextProcessor
#  Contains functions that process text, such as removing indent, splitting sentences, etc.
 
import re
import os
import sys

## Retrieves every line from a .txt file. The code terminates if the file is not found.
#
#  @param inputFilePath path to the desired file
#  @return list of lines from the file
#  @exception FileNotFoundError if the file is not found
def retrieveLines(inputFilePath: str) -> list[str]:
    lines = []
    try:
        with open(inputFilePath, 'r', encoding='utf8') as file:
            for line in file:
                lines.append(line)

    except Exception as e:
        print(f"An error occurred: {str(e)}", flush=True)
        sys.exit(1)

    return lines

## Builds the output file path from the input file path
#
#  @param inputFilePath path to the desired file
#  @return path of the output file, in format of <input file name>-Translated.<extension>
def makeOutputFilePath(inputFilePath: str) -> str:
    return os.path.splitext(inputFilePath)[0] + "-Translated.txt"

## Checks if a line is empty
#
#  @param line line to be checked
#  @return True if the line is empty, False otherwise
def isEmptyLine(line: str) -> bool:
    return not line.strip()

## Removes indent from a sentence
#
#  @param line line to be modified
#  @return line without indent
def removeIndent(line: str) -> str:
    return line[1:] if line[0] == '　' else line

## Checks if the line is a timeout message from the Sugoi Translator site
#
#  @param line line to be checked
#  @return True if the line is a timeout message, False otherwise
def isTimeoutMessage(line: str) -> bool:
    return line.count('discord.gg') != 0

## If the japanese paragraph is longer than the max allowed length, splits it into smaller sentences.
#  The sentences are split by the period character. This is used to comply with Sugoi translator site's 
#  100 character limit.
#
#  @param line line to be split
#  @param maxLength max allowed length of a sentence
#  @return list of sentences
def splitToSentence(line: str, maxLength: int) -> list:
    if len(line) <= maxLength:
        return [line]
    
    return [sentence + '。' for sentence in line.split('。') if sentence and sentence != '\n']

## Checks if string contains no Japanese characters
#
#  @param line line to be checked
#  @return True if the line contains no Japanese characters, False otherwise
def noJapaneseCharacters(line: str) -> bool:
    pattern = re.compile(r'[\u3040-\u30ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff\uff66-\uff9f]')
    return re.search(pattern, line) is None