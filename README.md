# TextToCall
##A web service to make calls without saying a thing.
TextToCall is a Flask based web application that allows users to leave voice messages without
speaking. Entered text is delivered any phone number by Plivo, and read aloud by speech to text.
Also, there is an insult generator if you have nothing better to say.

Live app can be found at http://pacific-stream-4609.herokuapp.com/

##Quick setup
* (Assumes you have Python 2.X, pip, virtualenv, git, and Heroku Toolbelt installed):
* Clone this repo
* Inside the project folder, run the following terminal commands (from Plivo docs):

        virtualenv --distribute venv
        source venv/bin/activate
        pip install -r requirements.txt
        python app.py
        
* The server should now be running at localhost:5000
* To push to heroku, run the following terminal commands:

        heroku create
        git push heroku master
        heroku scale web=1
