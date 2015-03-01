import os, requests, json
from flask import Flask, Response, request, url_for
import plivoxml

app = Flask(__name__)

@app.route('/')
def index():
    auth_id = 'MAOGJLZMVMNGVMYTBLZG'
    base = 'https://api.plivo.com/v1/Account/'+auth_id+'/Call/'
    payload = {
        'from': '14157232470',
        'to':'14084388066',
        'answer_url':'http://pacific-stream-4609.herokuapp.com/response/speak/',
        'answer_method': 'GET'
    }
    requests.post(base, payload)

@app.route('/response/speak/', methods=['GET'])
def speak():
    # Enter the message you want to play
    text = "You are a total scrub."
    parameters = {'loop': 0, 'language': "en-US", 'voice': "WOMAN"}

    response = plivoxml.Response()
    response.addSpeak(text, **parameters)

    return Response(str(response), mimetype='text/xml')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
