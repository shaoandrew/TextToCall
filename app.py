import os, requests, json
from flask import Flask, Response, request, url_for
import plivoxml, plivo

app = Flask(__name__)

@app.route('/call')
def call():
    auth_id = ""
    auth_token = ""
    p = plivo.RestAPI(auth_id, auth_token)
    params = {
        'from': '14157232470',
        'to':'19169903451',
        'answer_url':'http://pacific-stream-4609.herokuapp.com/response/speak/',
        'answer_method': 'GET'
    }
    r = p.make_call(params)
    return str(r)

@app.route('/response/speak/', methods=['GET'])
def speak():
    # Enter the message you want to play
    text = "You are a total scrub."
    parameters = {'loop': 0, 'language': "en-US", 'voice': "WOMAN"}

    response = plivoxml.Response()
    response.addSpeak(text, **parameters)

    return Response(str(response), mimetype='text/xml')

def insultreq():
    requestUrl = 'http://quandyfactory.com/insult/json'
    page = urllib.urlopen(requestUrl)
	contents = page.read()
	insult = json.loads(contents)
	return insult['insult']



if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
