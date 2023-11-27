import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import context
import unittest
import TenshiTranslator.Util.TextProcessor

class TextProcessorTest(unittest.TestCase):
    def test(self):
        self.assertTrue(True)