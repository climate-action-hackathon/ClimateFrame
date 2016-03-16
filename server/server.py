from __future__ import print_function
import sys
import requests
import json
from flask import Flask
from db import Database

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/forecast")
def get_forecast():
    with open('config.json') as config_file:    
        key = json.load(config_file)['p_key']
        forecast_endpoint = 'https://earthnetworks.azure-api.net/getHourly6DayForecast/data/forecasts/v1/hourly'
        parameters = '?locationtype=latitudelongitude&units=english&offset=0&metadata=true&verbose=true'
        location = '-17.9244,25.8567'
        request_url = forecast_endpoint + parameters + '&location=' + location + '&subscription-key=' + key
        return requests.get(request_url).content

@app.route("/contents")
def get_contents():
	database = Database()

	result = database.query()

	return str(result)



if __name__ == "__main__":
    app.run(debug=True)