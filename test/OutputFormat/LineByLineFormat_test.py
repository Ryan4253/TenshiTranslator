import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from TenshiTranslator.OutputFormat.LineByLineFormat import LineByLineFormat
from TenshiTranslator.Util.TextProcessor import retrieveLines

def test_writeFile():
    japaneseLines = retrieveLines("test/assets/SampleInput.txt")
    englishLines = retrieveLines("test/assets/SampleTranslation.txt")
    
    output = LineByLineFormat()
    output.writeFile("LineByLineTest.txt", japaneseLines, englishLines)

    result = retrieveLines("LineByLineTest.txt")
    os.remove("LineByLineTest.txt")

    expected = retrieveLines("test/assets/SampleLineByLine.txt")
    assert result == expected
    