import re

def replaceText(line : str, table : dict) -> str:
    ret = line
    for textOld, textNew in table.items():
        ret = ret.replace(textOld, textNew)
    
    return ret

def replaceTextRegex(line : str, table : dict) -> str:
    ret = line
    for pattern, replacement in table.items():
        ret = re.sub(pattern, replacement, ret)
    
    return ret

def isEmptyLine(line : str) -> bool:
    return not line.strip()

def removeIndent(line : str) -> str:
    return line[1:] if line[0] == '　' else line

def isTimeoutMessage(line: str) -> bool:
    return line.count('discord.gg') != 0

def splitToSentence(line : str, maxLength : int) -> list:
    if len(line) < maxLength:
        return [line]
    
    return [sentence + '。' for sentence in line.split('。') if sentence and sentence != '\n']