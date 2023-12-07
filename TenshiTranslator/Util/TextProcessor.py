"""
Contains functions that process text, such as removing indent, splitting sentences, etc.
"""
 
import re
import os
import sys

def retrieveLines(inputFilePath: str) -> list[str]:
    """ Retrieves every line from a .txt file. The code terminates if the file is not found.

    :param inputFilePath: path to the desired file
    :raises: FileNotFoundError if the file is not found
    :return: list of lines from the file
    """

    lines = []
    try:
        with open(inputFilePath, 'r', encoding='utf8') as file:
            for line in file:
                lines.append(line)

    except Exception as e:
        print(f"An error occurred: {str(e)}", flush=True)
        sys.exit(1)

    return lines

def makeOutputFilePath(inputFilePath: str) -> str:
    """ Builds the output file path from the input file path

    :param inputFilePath: path to the desired file
    :return: path of the output file, in format of <input file name>-Translated.<extension>
    """

    return os.path.splitext(inputFilePath)[0] + "-Translated.txt"

def isEmptyLine(line: str) -> bool:
    """ Checks if a line is empty

    :param line: line to be checked
    :return: 'True' if the line is empty, 'False' otherwise
    """

    return not line.strip()

def removeIndent(line: str) -> str:
    """ Removes indent from a sentence

    :param line: line to be modified
    :return: line without indent
    """

    return line[1:] if line[0] == '　' else line

def isTimeoutMessage(line: str) -> bool:
    """ Checks if the line is a timeout message from the Sugoi Translator site

    :param line: line to be checked
    :return: 'True' if the line is a timeout message, 'False' otherwise
    """

    return line.count('discord.gg') != 0

def splitToSentence(line: str, maxLength: int) -> list:
    """ If the japanese paragraph is longer than the max allowed length, splits it into smaller sentences.

    The sentences are split by the period character. This is used to comply with Sugoi translator site's 
    100 character limit.

    :param line: lline to be split
    :param maxLength: max allowed length of a sentence
    :return: list of sentences
    """

    if len(line) <= maxLength:
        return [line]
    
    return [sentence + '。' for sentence in line.split('。') if sentence and sentence != '\n']

def noJapaneseCharacters(line: str) -> bool:
    """ Checks if string contains no Japanese characters

    :param line: line to be checked
    :return: 'True' if the line contains no Japanese characters, 'False' otherwise
    """
    
    pattern = re.compile(r'[\u3040-\u30ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff\uff66-\uff9f]')
    return re.search(pattern, line) is None