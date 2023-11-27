from OnlineTranslator import OnlineTranslator
from BatchTranslator import BatchTranslator
from OfflineTranslator import OfflineTranslator
from LineByLineFormat import LineByLineFormat
from EnglishOnlyFormat import EnglishOnlyFormat
from Glossary import Glossary

from flask import Flask
from flask import Response
from flask import request

import socket 
from urllib3.connection import HTTPConnection 
HTTPConnection.default_socket_options = ( 
    HTTPConnection.default_socket_options + [ 
        (socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1), 
        (socket.SOL_TCP, socket.TCP_KEEPIDLE, 45), 
        (socket.SOL_TCP, socket.TCP_KEEPINTVL, 10), 
        (socket.SOL_TCP, socket.TCP_KEEPCNT, 6) 
    ] 
)

app = Flask("TenshiTranslatorAPI")

@app.route("/", methods=['POST'])
def process():
    data = request.get_json()

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
    
    return Response("Complete", status=200)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=6000)