import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import context
import unittest
from TenshiTranslator.Util.TextProcessor import *
import os

class TextProcessorTest(unittest.TestCase):
    def testRetrieveLines(self):
        lines = retrieveLines("test/assets/SampleInput.txt")
        self.assertEqual(lines, [
            "紙をペン先が撫で、カッカッとやや硬質な音を立てながら真っ白なページを文字で埋めていく。\n", 
            "\n", 
            "◇◇◇◇"])

    def testMakeOutputFilePath(self):
        self.assertEqual(makeOutputFilePath("Test.txt"), "Test-Translated.txt")
        self.assertEqual(makeOutputFilePath("C:/Desktop/Test.txt"), "C:/Desktop/Test-Translated.txt")

    def testIsEmptyLine(self):
        self.assertTrue(isEmptyLine("      "))
        self.assertFalse(isEmptyLine("wad"))

    def testRemoveIndent(self):
        self.assertEqual(removeIndent("　hello world"), "hello world")
        self.assertEqual(removeIndent("hello world"), "hello world")

    def testIsTimeoutMessage(self):
        self.assertTrue(isTimeoutMessage(
            "Too many requests from this IP, please try again after 5 minutes. BTW, If you think the translation \
            quality is SUGOI, feel free to join our discord server at: https://discord.gg/XFbWSjMHJh"))
        self.assertFalse(isTimeoutMessage("literally anything else"))

    def testSplitToSentence(self):
        self.assertEqual(splitToSentence("夕食後、後片付けも終わった後は、一人で筧くのだが、常に二人でくっつき合っている訳ではない。\
                                         クラスメイト達はおろか樹まで勘違いしていたので笑っていいのか思いのが。\
                                         周達は四六時中いちゃついていると思われているらしい。", 100))
        
        

    def testNoJapaneseCharacters(self):
        self.assertTrue(noJapaneseCharacters("◇◇◇◇"))
        self.assertTrue(noJapaneseCharacters("test"))
        self.assertFalse(noJapaneseCharacters("紙をペン先が撫で、"))