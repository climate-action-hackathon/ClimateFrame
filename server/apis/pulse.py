import requests
import json

def get_hourly_6day_forecast(latitude, longitude):
    with open('../config.json') as config_file:
        print('get_hourly_6day_forecast()')
        key = json.load(config_file)['keys']['p_key']
        forecast_endpoint = 'https://earthnetworks.azure-api.net/getHourly6DayForecast/data/forecasts/v1/hourly'
        parameters = '?locationtype=latitudelongitude&units=metric&offset=0&metadata=true&verbose=true'
        # location = '-17.9244,25.8567'
        location = latitude + ',' + longitude
        request_url = forecast_endpoint + parameters + '&location=' + location + '&subscription-key=' + key
        response = requests.get(request_url)
        return response.json()['hourlyForecastPeriod']

def filter_temperature_under(latitude, longitude, degree):
    forecast_list = get_hourly_6day_forecast(latitude, longitude)
    return filter(lambda x: x['temperature'] <= degree, forecast_list)

def filter_temperature_over(latitude, longitude, degree):
    forecast_list = get_hourly_6day_forecast(latitude, longitude)
    return filter(lambda x: x['temperature'] >= degree, forecast_list)

def filter_wind_speed_over(latitude, longitude, speed):
    forecast_list = get_hourly_6day_forecast(latitude, longitude)
    return filter(lambda x: x['windSpeed'] >= speed, forecast_list)

def filter_thunderstorm_probability_over(latitude, longitude, percentage):
    forecast_list = get_hourly_6day_forecast(latitude, longitude)
    return filter(lambda x: x['thunderstormProbability'] >= percentage, forecast_list)

def thunder_over(percentage):
    print( "Response of the function! BTW the percentage is " + str(percentage) )
    return True
