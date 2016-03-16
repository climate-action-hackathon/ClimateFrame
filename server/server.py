import requests
import json
from flask import Flask, jsonify
from apis import pulse
app = Flask(__name__)

@app.route("/")
def hello():
    return "ClimateFrame FTW!"

@app.route("/forecast")
def get_forecast():
    return jsonify({'forecast': pulse.get_hourly_6day_forecast()})

if __name__ == "__main__":
    app.run()
