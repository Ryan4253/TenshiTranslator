import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from TenshiTranslator.Glossary.PassthroughGlossary import PassthroughGlossary

def test_Replacements():
    glossary = PassthroughGlossary()
    line = "こんにちは、私の名前はジョナサンです"
    
    line = glossary.process(line)
    assert line == "こんにちは、私の名前はジョナサンです"