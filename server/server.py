import requests
import json
import thread
from flask import Flask, jsonify, request
from apis import pulse
from db import Database
from scheduler import start_scheduled_jobs
from pprint import pprint
from twilio.rest import TwilioRestClient
from requests.auth import HTTPBasicAuth

app = Flask(__name__)
database = Database()
thread.start_new_thread(start_scheduled_jobs, ())
account_sid = "AC9568bf793a849cc44080274f2d87a303"
auth_token = "e41444c4a72004173b1707b5841a9626"
client = TwilioRestClient(account_sid, auth_token)

@app.route("/")
def hello():
    return "ClimateFrame FTW!"

@app.route("/forecast")
def get_forecast():
    latidude = '-17.9244'
    longitude = '25.8567'
    forecast = pulse.get_hourly_6day_forecast(latidude, longitude)
    return jsonify({'forecast': forecast})

@app.route("/recipes")
def get_recipes():
    recipes = database.get_all_recipes()
    return jsonify({'recipes': recipes})

@app.route('/recipe', methods = ['POST'])
def add_recipe():
    recipe_json = request.json
    recipe_id = database.add_recipe(recipe_json)
    return jsonify({'recipe_id': str(recipe_id)})

@app.route("/contents")
def get_contents():
    result = database.query()
    return jsonify(result)

@app.route("/number")
def number():
    return "number"

@app.route("/textmessage")
def textmessage():
    # agent_phone_number = "+905301148060"
    agent_phone_number = "+255765299266"
    twilio_phone_number = "+12014310707"

    sms = "Water your plants. There will be no rain in the next 3 hours."

    message = client.messages.create(to=agent_phone_number,
                                     from_=twilio_phone_number,
                                     body=sms)
    
    return sms


@app.route("/text")
def text():
    # agent_phone_number = "+905301148060"
    agent_phone_number = "+255765299266"
    twilio_phone_number = "+12014310707"

    sms = ".\n      _____    _\n  __|         | (*)\n |   |          |//\"\"\n  \ |           / \"\"\n     |______|  \"\"\n                   \"\"\n (o) (o) (o) \"(o)\n   |     |     |   \"\" |\n---------------------\n"

    message = client.messages.create(to=agent_phone_number,
                                     from_=twilio_phone_number,
                                     body=sms)
    
    return sms

@app.route("/call")
def call():
    # agent_phone_number = "+905301148060"
    agent_phone_number = "+255765299266"
    twilio_phone_number = "+12014310707"
    call = client.calls.create(url="http://demo.twilio.com/docs/voice.xml",
    to=agent_phone_number,
    from_=twilio_phone_number)
    print call.sid    
    return "hello"


@app.route("/records")
def records():
    phonenumbers = []

    r = requests.get("https://api.twilio.com/2010-04-01/Accounts/AC9568bf793a849cc44080274f2d87a303/Calls.json", data={'url': 'websiteUrl'}, auth=HTTPBasicAuth('AC9568bf793a849cc44080274f2d87a303', 'e41444c4a72004173b1707b5841a9626'))
    if (r.status_code == 200):
        for a in json.loads(r.content)["calls"]:
            print ""
            phonenumbers.append(str(a["from"]))
    else:
        print ":("

    print phonenumbers

    return ', '.join(phonenumbers)



if __name__ == "__main__":
    app.run(debug=True)
