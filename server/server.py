import requests
import json
import thread
from flask import Flask, jsonify, request
from apis import pulse
from db import Database
from scheduler import start_scheduled_jobs
from actions import send_sms, send_voice_message, get_records

app = Flask(__name__)
database = Database()
thread.start_new_thread(start_scheduled_jobs, ())

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
    text = "Water the plants.\n      _____    _\n  __|         | (*)\n |   |          |//\"\"\n  \ |           / \"\"\n     |______|  \"\"\n                   \"\"\n (o) (o) (o) \"(o)\n   |     |     |   \"\" |\n---------------------\n"
    send_sms(text, numbers)
    return "None"

@app.route("/text")
def text():
    numbers = ["+255765299266"]
    text = "Water the plants.\n      _____    _\n  __|         | (*)\n |   |          |//\"\"\n  \ |           / \"\"\n     |______|  \"\"\n                   \"\"\n (o) (o) (o) \"(o)\n   |     |     |   \"\" |\n---------------------\n"
    send_sms(text, numbers)
    return "None"    

@app.route("/call")
def call():
    numbers = ["+255765299266"]
    voice_url="http://demo.twilio.com/docs/voice.xml"    
    send_voice_message(voice_url, numbers)
    return "None"    

if __name__ == "__main__":
    app.run(debug=True)
