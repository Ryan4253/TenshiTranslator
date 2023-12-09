from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin

import json

from fairseq.models.transformer import TransformerModel

ja2en = TransformerModel.from_pretrained(
    './fairseq/japaneseModel/',
    checkpoint_file='big.pretrain.pt',
    source_lang = "ja",
    target_lang = "en",
    bpe='sentencepiece',
    sentencepiece_model='./fairseq/spmModels/spm.ja.nopretok.model',
    no_repeat_ngram_size=3,
	inter_threads=16,
	beam_size=5
)

ja2en.cuda()

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/", methods = ['POST'])
@cross_origin()

def sendImage():
    data = request.get_json()
    message = data.get("message")
    content = data.get("content")

    if (message == "batch translate"):
        return json.dumps(ja2en.translate(content))

    if (message == "translate sentences"):
        result = ja2en.translate(content)
        return json.dumps(result)

    if (message == "close server"):
        shutdown_server()
        return json.dumps("Shutdown server")

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=14366)