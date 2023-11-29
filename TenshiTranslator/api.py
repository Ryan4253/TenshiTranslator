## @package api
#  Contains flask server api for TenshiTranslator

from TenshiTranslator.Translator.OnlineTranslator import OnlineTranslator
from TenshiTranslator.Translator.BatchTranslator import BatchTranslator
from TenshiTranslator.Translator.OfflineTranslator import OfflineTranslator
from TenshiTranslator.OutputFormat.LineByLineFormat import LineByLineFormat
from TenshiTranslator.OutputFormat.EnglishOnlyFormat import EnglishOnlyFormat
from TenshiTranslator.Util.Glossary import Glossary

from flask import Flask
from flask import Response
from flask import request

# https://stackoverflow.com/questions/72393655/connection-aborted-remotedisconnected-remote-end-closed-connection-without-re
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

## Processes a translation request. the request is a json file with the following parameters
# 'Translator': 'Online' | 'Offline' | 'Batch', the type of translator to use
# 'OutputFormat': 'LineByLine' | 'EnglishOnly', the output format to use
# 'GlossaryNames': file path to the glossary names file
# 'GlossaryCorrections': file path to the glossary corrections file
# 'Files': list of file paths to translate
# 'SugoiDirectory': path to the sugoi directory, required if Translator is 'Batch' or 'Offline'
# 'BatchSize': number of lines to translate at once, required if Translator is 'Batch'
# 'TimeoutWait': number of seconds to wait before resuming translation after a timeout, required if Translator is 'Online'
@app.route("/", methods=['POST'])
def process():
    data = request.get_json()

    glossary = Glossary(data.get('GlossaryNames'), data.get('GlossaryCorrections'))
    outputFormat = LineByLineFormat() if data.get('OutputFormat') == 'LineByLine' else EnglishOnlyFormat

    translator = None
    if(data.get('Translator') == 'Batch'):
        sugoi = data.get('SugoiDirectory')
        translator = BatchTranslator(outputFormat, glossary, sugoi, data.get('BatchSize'))
    elif(data.get('Translator') == 'Online'):
        translator = OnlineTranslator(outputFormat, glossary, data.get('TimeoutWait'))
    else:
        sugoi = data.get('SugoiDirectory')
        translator = OfflineTranslator(outputFormat, glossary, sugoi)

    files = data.get('Files')
    for file in files:
        translator.translate(file)
    
    return Response("Complete", status=200)

## Starts the server
def startServer():
    app.run(host='127.0.0.1', port=6000)
