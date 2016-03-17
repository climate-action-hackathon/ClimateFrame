import requests
import json
import thread
from flask import Flask, jsonify, request, render_template
from apis import pulse
from db import Database
from scheduler import start_scheduled_jobs
from actions import send_sms, send_voice_message, get_records
from apis.ubimet import get_current_warning, is_tropical_cyclone_warning

app = Flask(__name__)
database = Database()
start_scheduled_jobs()

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

@app.route('/recipes', methods=['DELETE'])
def delete_all_recipes():
   status = database.delete_all_recipes()
   return jsonify(status)

@app.route('/recipe/<string:id>', methods=['DELETE'])
def delete_entry(id):
   status = database.delete_recipe(id)
   return jsonify(status)

@app.route("/textmessage")
def textmessage():
    numbers = ["+255765299266"]
    text = "Water your plants. There will be no rain in the next 3 hours."
    send_sms(text, numbers)
    return "None"

@app.route("/text")
def text():
    numbers = ["+255765299266"]
    text = ".\n      _____    _\n  __|         | (*)\n |   |          |//\"\"\n  \ |           / \"\"\n     |______|  \"\"\n                   \"\"\n (o) (o) (o) \"(o)\n   |     |     |   \"\" |\n---------------------\n"
    send_sms(text, numbers)
    return "None"    

@app.route("/call")
def call():
    numbers = ["+255765299266"]
    voice_url="http://demo.twilio.com/docs/voice.xml"    
    send_voice_message(voice_url, numbers)
    return "None"    

@app.route("/records")
def records():
    return get_records()


@app.route('/login')
def login():

    return render_template('login.html')


@app.route('/dashboard')
def show_dashboard():
    with open('config.json') as data_file:
        data = json.load(data_file)

    # providers = map(lambda x: data['apis'][x]['name'], data['apis'])
    # triggers = ""
    # print data['apis']
    # for provider in data['apis']:
    #     print provider
    #     if 'triggers' in provider:
    #         triggers = provider.triggers
    # print triggers

    # final_data = {}
    # final_data['providers'] = providers
    # final_data['triggers']  = triggers

    return render_template('dashboard.html', data=data)


if __name__ == "__main__":
    app.run(debug=True)

# @app.route("/call")
# def call():
#     numbers = ["+255765299266"]
#     voice_url="http://demo.twilio.com/docs/voice.xml"    
#     send_voice_message(voice_url, numbers)
#     return "None"    

# @app.route("/records")
# def records():
#     return get_records()

# if __name__ == "__main__":
#     # app.run(debug=True)
#     app.run()
>>>>>>> 354a99dbb09a8b30ab8568297ca2c684850f1200
