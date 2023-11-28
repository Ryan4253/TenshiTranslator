import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from TenshiTranslator.Util.Glossary import Glossary

def test_Constructor():
    glossary = Glossary("test/assets/SampleNames.csv", "test/assets/SampleCorrections.csv")
    names = glossary.names
    corrections = glossary.corrections

    assert names == {'ジョナサン': 'Jonathan'}
    assert corrections == {'na': 'hna'}

    with pytest.raises(SystemExit) as excinfo:  
        glossary = Glossary("test/assets/SampleNames.csv", "lol.csv")
 
    assert excinfo.value.code == 1

def test_Replacements():
    glossary = Glossary("test/assets/SampleNames.csv", "test/assets/SampleCorrections.csv")
    line = "こんにちは、私の名前はジョナサンです"
    
    line = glossary.replaceNames(line)
    assert line == "こんにちは、私の名前はJonathanです"

    line = glossary.applyCorrections(line)
    assert line == "こんにちは、私の名前はJohnathanです"