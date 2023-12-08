import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from TenshiTranslator.Translator.BatchTranslator import BatchTranslator
from TenshiTranslator.OutputFormat.LineByLineFormat import LineByLineFormat
from TenshiTranslator.Util.Glossary import Glossary
from TenshiTranslator.Util.TextProcessor import retrieveLines

@pytest.mark.skipif(os.getenv("GITHUB_ACTIONS") is not None, reason="Test doesn't work on Github Actions.")
def test_BatchTranslator():
    glossary = Glossary("test/assets/SampleNames.csv", "test/assets/SampleCorrections.csv")
    translator = BatchTranslator(LineByLineFormat(), glossary, "C:\\Users\\ryanl\\Documents\\Apps\\Sugoi-Translator-Toolkit-V6.0-Anniversary")
    translator.translate("test/assets/SampleInput.txt")

    expected = retrieveLines("test/assets/SampleBatchOutput.txt")
    result = retrieveLines("test/assets/SampleInput-Translated.txt")
    os.remove("test/assets/SampleInput-Translated.txt")

    assert expected == result