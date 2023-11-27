import subprocess
import requests
import json

if __name__ == "__main__":
    p = subprocess.Popen(['python', 'api.py'], stdout=subprocess.PIPE, creationflags=subprocess.CREATE_NO_WINDOW)
    data = {'Message': 'Translate', 
            'Translator': 'Batch',
            'BatchSize': 64,
            'SugoiDirectory': 'C:\\Users\\ryanl\\Documents\\Apps\\Sugoi-Translator-Toolkit-V6.0-Anniversary',
            'GlossaryNames': 'Names.csv',
            'GlossaryCorrections': 'Corrections.csv',
            'OutputFormat': 'LineByLine',
            'Files': ['sources/yume-no-ukihashi.txt', 'sources/Chapter_1_preview.txt']}
    headers = {'content-type': 'application/json'}
    requests.post(f'http://127.0.0.1:3200/', data=json.dumps(data), headers=headers)

    p.kill()

    for line in p.stdout:
        print ("test:", line.decode())