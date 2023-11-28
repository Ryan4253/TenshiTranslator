import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from TenshiTranslator.Util.TextProcessor import *

def test_retrieveLines():
    lines = retrieveLines("test/assets/SampleInput.txt")
    assert lines == ["しゅくだいしているから邪魔じゃましないでくれ。\n", 
                     "\n", 
                     "◇◇◇◇"]
    
    with pytest.raises(SystemExit) as excinfo:  
        retrieveLines("lol.txt")  
    
    assert excinfo.value.code == 1

def test_makeOutputFilePath():
    assert makeOutputFilePath("Test.txt") == "Test-Translated.txt"
    assert makeOutputFilePath("C:/Desktop/Test.txt") == "C:/Desktop/Test-Translated.txt"

def test_isEmptyLine():
    assert isEmptyLine("      ")
    assert not isEmptyLine("   wad   ")

def testRemoveIndent():
    assert removeIndent("　hello world") == "hello world"
    assert removeIndent("hello world") == "hello world"

def testIsTimeoutMessage():
    assert isTimeoutMessage("Too many requests from this IP, please try again after 5 minutes. BTW, If you think the translation \
        quality is SUGOI, feel free to join our discord server at: https://discord.gg/XFbWSjMHJh")
    
    assert not isTimeoutMessage("literally anything else")

def testSplitToSentence():
    data = "しゅくだいしているから邪魔じゃましないでくれ。しゅくだいしているから邪魔じゃましないでく。しゅくだいしているから邪魔じゃましないで。しゅくだいしているから邪魔じゃましない。しゅくだいしているから邪魔じゃましな。"
    assert splitToSentence(data, 100) == ["しゅくだいしているから邪魔じゃましないでくれ。", 
                                          "しゅくだいしているから邪魔じゃましないでく。",
                                          "しゅくだいしているから邪魔じゃましないで。",
                                          "しゅくだいしているから邪魔じゃましない。",
                                          "しゅくだいしているから邪魔じゃましな。"]
    
    assert splitToSentence(data, 500) == [data]
    assert splitToSentence("", 100) == [""]
    assert splitToSentence("\n", 100) == ["\n"]
    
def testNoJapaneseCharacters():
    assert noJapaneseCharacters("◇◇◇◇")
    assert noJapaneseCharacters("test")
    assert not noJapaneseCharacters("しゅくだいしているから邪魔じゃましないでくれ。")