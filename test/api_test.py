import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from TenshiTranslator.Util.TextProcessor import retrieveLines
import subprocess
import requests
import json

@pytest.mark.skipif(os.getenv("GITHUB_ACTIONS") is not None, reason="Test doesn't work on Github Actions.")
def test_api():
    p = subprocess.Popen(['python', 'TenshiTranslator/api.py'])

    data = {'Message': 'Translate', 
            'Translator': 'Online',
            'TimeoutTime': 315,
            'GlossaryNames': 'test/assets/SampleNames.csv',
            'GlossaryCorrections': 'test/assets/SampleCorrections.csv',
            'OutputFormat': 'LineByLine',
            'Files': ['test/assets/SampleInput.txt']}

    headers = {'content-type': 'application/json'}
    requests.post(f'http://127.0.0.1:6000/', data=json.dumps(data), headers=headers)
    p.kill()

    expected = retrieveLines("test/assets/SampleOnlineOutput.txt")
    result = retrieveLines("test/assets/SampleInput-Translated.txt")
    os.remove("test/assets/SampleInput-Translated.txt")

    assert expected == result
