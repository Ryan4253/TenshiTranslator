from OnlineTranslator import OnlineTranslator
from BatchTranslator import BatchTranslator
from OfflineTranslator import OfflineTranslator
from LineByLineFormat import LineByLineFormat
from EnglishOnlyFormat import EnglishOnlyFormat
from Glossary import Glossary

from flask import Flask
from flask import request
import json

app = Flask("TenshiTranslatorAPI")

@app.route("/", methods=['POST'])
def process():
    data = request.get_json()

    if (data.get('Message') == "Shutdown"):
        shutdownServer()
        return json.dumps("Shutdown server")

    glossary = Glossary(data.get('GlossaryNames'), data.get('GlossaryCorrections'))
    outputFormat = LineByLineFormat() if data.get('OutputFormat') == 'LineByLine' else EnglishOnlyFormat
    sugoi = data.get('SugoiDirectory')

    translator = None
    if(data.get('Translator') == 'Batch'):
        translator = BatchTranslator(outputFormat, glossary, sugoi, data.get('BatchSize'))
    elif(data.get('Translator') == 'Online'):
        translator = OnlineTranslator(outputFormat, glossary, sugoi, data.get('TimeoutWait'))
    else:
        translator = OfflineTranslator(outputFormat, glossary, sugoi)

    files = data.get('Files')
    for file in files:
        translator.translate(file)
    
    return json.dumps("Translation Complete")

def shutdownServer():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

if __name__ == '__main__':
    print("HI", flush=True)
    app.run(host='127.0.0.1', port=5000)