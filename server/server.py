import requests
import json
import thread
from flask import Flask, jsonify, request
from apis import pulse
from db import Database
from scheduler import start_scheduled_jobs

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
    return jsonify(recipes)

@app.route('/recipe', methods = ['POST'])
def add_recipe():
    recipe_json = request.json
    recipe_id = database.add_recipe(recipe_json)
    return jsonify({'recipe_id': str(recipe_id)})

@app.route('/recipe/delete/<int:id>', methods=['DELETE'])
def delete_entry(id):
   if database.delete_recipe(id):
    return jsonify({'status':'OK','deleted':'1'})
   else:
    return jsonify({'status':'Not deleted','deleted':'0'})

if __name__ == "__main__":
    app.run(debug=True)