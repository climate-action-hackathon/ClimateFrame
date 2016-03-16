import requests
import json
from flask import Flask, jsonify
from apis import pulse
from db import Database

app = Flask(__name__)
database = Database()

@app.route("/")
def hello():
    return "ClimateFrame FTW!"

@app.route("/forecast")
def get_forecast():
    return jsonify({'forecast': pulse.get_hourly_6day_forecast()})

@app.route("/recipes")
def get_recipes():
    recipes = database.get_recipes()
    return jsonify(recipes)

if __name__ == "__main__":
    app.run(debug=True)