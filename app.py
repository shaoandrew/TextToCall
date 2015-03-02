import os, requests, json
from flask import Flask, Response, request, url_for, send_from_directory, redirect, render_template
import plivoxml, plivo
import urllib

app = Flask(__name__, static_url_path='')

messages = {}

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/call', methods=['POST'])
def call():
    num = request.form['number']
    msg = request.form['message']
    messages[num] = msg
    auth_id = ""
    auth_token = ""
    p = plivo.RestAPI(auth_id, auth_token)
    params = {
        'from': '14157232470',
        'to': num,
        'answer_url':'http://pacific-stream-4609.herokuapp.com/response/speak/' + num,
        'answer_method': 'POST'
    }
    r = p.make_call(params)
    return render_template('complete.html', number=num)

@app.route('/response/speak/<num>', methods=['POST'])
def speak(num):
    # Enter the message you want to play
    text = messages[num]
    parameters = {'loop': 1, 'language': "en-US", 'voice': "WOMAN"}

    response = plivoxml.Response()
    response.addSpeak(text, **parameters)

    return Response(str(response), mimetype='text/xml')

@app.route('/insult')
def insultreq():
    requestUrl = 'http://quandyfactory.com/insult/json'
    page = urllib.urlopen(requestUrl)
    contents = page.read()
    insult = json.loads(contents.decode())
    return insult['insult']

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True) 