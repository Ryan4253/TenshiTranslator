import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from TenshiTranslator.Translator.OfflineTranslator import OfflineTranslator
from TenshiTranslator.OutputFormat.LineByLineFormat import LineByLineFormat
from TenshiTranslator.Glossary.CSVGlossary import CSVGlossary
from TenshiTranslator.Util.TextProcessor import retrieveLines

@pytest.mark.skipif(os.getenv("GITHUB_ACTIONS") is not None, reason="Test doesn't work on Github Actions.")
def test_OfflineTranslator():
    preprocessGlossary = CSVGlossary("test/assets/SampleNames.csv")
    postprocessGlossary = CSVGlossary("test/assets/SampleCorrections.csv")
    translator = OfflineTranslator(LineByLineFormat(), preprocessGlossary, postprocessGlossary, "C:\\Users\\ryanl\\Documents\\Apps\\Sugoi-Translator-Toolkit-6.0")
    translator.translate("test/assets/SampleInput.txt")

    expected = retrieveLines("test/assets/SampleOfflineOutput.txt")
    result = retrieveLines("test/assets/SampleInput-Translated.txt")
    os.remove("test/assets/SampleInput-Translated.txt")

    assert expected == result