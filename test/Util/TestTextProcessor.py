import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from TenshiTranslator.Util.TextProcessor import *

class TextProcessorTest(unittest.TestCase):
    def testRetrieveLines(self):
        lines = retrieveLines("test/assets/SampleInput.txt")
        self.assertEqual(lines, [
            "しゅくだいしているから邪魔じゃましないでくれ。\n", 
            "\n", 
            "◇◇◇◇"])

    def testMakeOutputFilePath(self):
        self.assertEqual(makeOutputFilePath("Test.txt"), "Test-Translated.txt")
        self.assertEqual(makeOutputFilePath("C:/Desktop/Test.txt"), "C:/Desktop/Test-Translated.txt")

    def testIsEmptyLine(self):
        self.assertTrue(isEmptyLine("      "))
        self.assertFalse(isEmptyLine("   wad   "))

    def testRemoveIndent(self):
        self.assertEqual(removeIndent("　hello world"), "hello world")
        self.assertEqual(removeIndent("hello world"), "hello world")

    def testIsTimeoutMessage(self):
        self.assertTrue(isTimeoutMessage("Too many requests from this IP, please try again after 5 minutes. BTW, If you think the translation \
            quality is SUGOI, feel free to join our discord server at: https://discord.gg/XFbWSjMHJh")
        )
        self.assertFalse(isTimeoutMessage("literally anything else"))

    def testSplitToSentence(self):
        data = "しゅくだいしているから邪魔じゃましないでくれ。しゅくだいしているから邪魔じゃましないでく。しゅくだいしているから邪魔じゃましないで。しゅくだいしているから邪魔じゃましない。しゅくだいしているから邪魔じゃましな。"
        self.assertEqual(splitToSentence(data, 100), 
                        ["しゅくだいしているから邪魔じゃましないでくれ。",
                         "しゅくだいしているから邪魔じゃましないでく。",
                         "しゅくだいしているから邪魔じゃましないで。",
                         "しゅくだいしているから邪魔じゃましない。",
                         "しゅくだいしているから邪魔じゃましな。"])
        
        self.assertEqual(splitToSentence(data, 500), [data])
        
    def testNoJapaneseCharacters(self):
        self.assertTrue(noJapaneseCharacters("◇◇◇◇"))
        self.assertTrue(noJapaneseCharacters("test"))
        self.assertFalse(noJapaneseCharacters("しゅくだいしているから邪魔じゃましないでくれ。"))