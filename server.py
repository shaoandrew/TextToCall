import requests
from flask import Flask
import json
app = Flask(__name__)

@app.route('/')
def index():
	return insultreq()



def insultreq():
    requestUrl = 'http://quandyfactory.com/insult/json'
    page = urllib.urlopen(requestUrl)
	contents = page.read()
	insult = json.loads(contents)
	return insult['insult']



if __name__ == '__main__':
    app.run(debug=True)