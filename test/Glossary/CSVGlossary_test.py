import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from TenshiTranslator.Glossary.CSVGlossary import CSVGlossary

def test_Constructor():
    glossary = CSVGlossary("test/assets/SampleNames.csv")
    
    assert glossary.processes == {'ジョナサン': 'Jonathan'}

    with pytest.raises(SystemExit) as excinfo:  
        glossary = CSVGlossary("lol.csv")
 
    assert excinfo.value.code == 1

def test_Replacements():
    glossary = CSVGlossary("test/assets/SampleNames.csv")
    line = "こんにちは、私の名前はジョナサンです"
    
    line = glossary.process(line)
    assert line == "こんにちは、私の名前はJonathanです"
