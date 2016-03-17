import requests
import json

def get_hourly_6day_forecast(latitude, longitude):
    with open('../config.json') as config_file:
        key = json.load(config_file)['keys']['p_key']
        forecast_endpoint = 'https://earthnetworks.azure-api.net/getHourly6DayForecast/data/forecasts/v1/hourly'
        parameters = '?locationtype=latitudelongitude&units=metric&offset=0&metadata=true&verbose=true'
        # location = '-17.9244,25.8567'
        location = latitude + ',' + longitude
        request_url = forecast_endpoint + parameters + '&location=' + location + '&subscription-key=' + key
        response = requests.get(request_url)
        return response.json()['hourlyForecastPeriod']

def temperature_less_than(latitude, longitude, degree):
    predictions = get_hourly_6day_forecast(latitude, longitude)
    filtered_predictions = filter(lambda x: x['temperature'] <= degree, forecast_list)
    return len(filtered_predictions) > 0

def temperature_greater_than(latitude, longitude, degree):
    predictions = get_hourly_6day_forecast(latitude, longitude)
    filtered_predictions = filter(lambda x: x['temperature'] >= degree, forecast_list)
    return len(filtered_predictions) > 0

def wind_speed_greater_than(latitude, longitude, speed):
    predictions = get_hourly_6day_forecast(latitude, longitude)
    filtered_predictions = filter(lambda x: x['windSpeed'] >= speed, forecast_list)
    return len(filtered_predictions) > 0

def thunderstorm_probability_greater_than(latitude, longitude, percentage):
    predictions = get_hourly_6day_forecast(latitude, longitude)
    filtered_predictions = filter(lambda x: x['thunderstormProbability'] >= percentage, predictions)
    return len(filtered_predictions) > 0

def precipitation_probability_greater_than(latitude, longitude, percentage):
    predictions = get_hourly_6day_forecast(latitude, longitude)
    filtered_predictions = filter(lambda x: x['adjustedPrecipProbability'] >= percentage, predictions)
    return len(filtered_predictions) > 0

def precipitation_probability_less_than(latitude, longitude, percentage):
    predictions = get_hourly_6day_forecast(latitude, longitude)
    filtered_predictions = filter(lambda x: x['adjustedPrecipProbability'] >= percentage, predictions)
    return not len(filtered_predictions) > 0
