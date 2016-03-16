import requests
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/forecast")
def get_forecast():
    return requests.get('https://earthnetworks.azure-api.net/getHourly6DayForecast/data/forecasts/v1/hourly?location=-17.9244,25.8567&locationtype=latitudelongitude&units=english&offset=0&metadata=true&verbose=true&subscription-key=d484f320c70e43528cd85eae0618c45a').content

if __name__ == "__main__":
    app.run()