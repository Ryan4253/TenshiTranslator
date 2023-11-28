import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from TenshiTranslator.Translator.OnlineTranslator import OnlineTranslator
from TenshiTranslator.OutputFormat.LineByLineFormat import LineByLineFormat
from TenshiTranslator.Util.Glossary import Glossary
from TenshiTranslator.Util.TextProcessor import retrieveLines

def test_OnlineTranslator():
    glossary = Glossary("test/assets/SampleNames.csv", "test/assets/SampleCorrections.csv")
    translator = OnlineTranslator(LineByLineFormat(), glossary)
    translator.translate("test/assets/SampleInput.txt")

    expected = retrieveLines("test/assets/SampleOnlineOutput.txt")
    result = retrieveLines("test/assets/SampleInput-Translated.txt")
    os.remove("test/assets/SampleInput-Translated.txt")

    assert expected == result