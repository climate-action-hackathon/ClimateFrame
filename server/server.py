import requests
import json
from flask import Flask, jsonify
from apis import pulse
from db import Database
from scheduler import start_scheduled_jobs

app = Flask(__name__)
database = Database()
start_scheduled_jobs()

@app.route("/")
def hello():
    return "ClimateFrame FTW!"

@app.route("/forecast")
def get_forecast():
    return jsonify({'forecast': pulse.get_hourly_6day_forecast()})

@app.route("/contents")
def get_contents():
    result = database.query()

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)