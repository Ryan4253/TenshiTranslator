import requests
import json

if __name__ == "__main__":
    data = {'Translator': 'Batch',
        'BatchSize': 64,
        'SugoiDirectory': 'C:\\Users\\ryanl\\Documents\\Apps\\Sugoi-Translator-Toolkit-V6.0-Anniversary',
        'GlossaryNames': 'C:\\Users\\ryanl\\Desktop\\tenshi-translator\\Names.csv',
        'GlossaryCorrections': 'C:\\Users\\ryanl\\Desktop\\tenshi-translator\\Corrections.csv',
        'OutputFormat': 'LineByLine',
        'Files': ['C:\\Users\\ryanl\\Desktop\\tenshi-translator\\sources\\yume-no-ukihashi.txt', 'C:\\Users\\ryanl\\Desktop\\tenshi-translator\\sources\\Chapter_1_preview.txt']}

    headers = {'content-type': 'application/json'}
    a = requests.post('http://127.0.0.1:6000/', data=json.dumps(data), headers=headers)