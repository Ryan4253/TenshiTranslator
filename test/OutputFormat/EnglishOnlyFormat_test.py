import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from TenshiTranslator.OutputFormat.EnglishOnlyFormat import EnglishOnlyFormat
from TenshiTranslator.Util.TextProcessor import retrieveLines

def test_writeFile():
    japaneseLines = retrieveLines("test/assets/SampleInput.txt")
    englishLines = retrieveLines("test/assets/SampleTranslation.txt")
    
    output = EnglishOnlyFormat()
    output.writeFile("EnglishOnlyTeset.txt", japaneseLines, englishLines)

    result = retrieveLines("EnglishOnlyTeset.txt")
    os.remove("EnglishOnlyTeset.txt")
    expected = retrieveLines("test/assets/SampleEnglishOnly.txt")
    assert result == expected