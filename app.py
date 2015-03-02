import os, requests, json
from flask import Flask, Response, request, url_for, send_from_directory
import plivoxml, plivo

app = Flask(__name__, static_url_path='')

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/call', methods=['POST'])
def call():
    num = request.form['number']
    msg = request.form['message']
    auth_id = ""
    auth_token = ""
    p = plivo.RestAPI(auth_id, auth_token)
    params = {
        'from': '14157232470',
        'to': num,
        'answer_url':'http://pacific-stream-4609.herokuapp.com/response/speak/',
        'answer_method': 'GET'
    }
    r = p.make_call(params)
    return str(r)

@app.route('/response/speak/', methods=['POST'])
def speak():
    # Enter the message you want to play
    text = "You are a total scrub."
    parameters = {'loop': 0, 'language': "en-US", 'voice': "WOMAN"}

    response = plivoxml.Response()
    response.addSpeak(text, **parameters)

    return Response(str(response), mimetype='text/xml')

#def insultreq():
#    requestUrl = 'http://quandyfactory.com/insult/json'
#    page = urllib.urlopen(requestUrl)
#	contents = page.read()
#	insult = json.loads(contents)
#	return insult['insult']



if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
