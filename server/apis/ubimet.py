import requests
import json

def current_warning(latitude, longitude):
    with open('../config.json') as config_file:
        key = json.load(config_file)['keys']['p_key']
        extreme_now_endpoint = 'https://met-api.ubimet.at:8090/pinpoint-data?sets=extreme_now'
        location = longitude + ' ' + latitude
        request_url = extreme_now_endpoint + '&coordinates=' + location
        response = requests.get(request_url,
        	verify=False,
        	headers={'Authorization': 'Token 0ae17c9399cd016022a68595adcb4322780d941f'})
        return response.json()[0]['met_sets'][0]['parameter_timesets'][0]['data'][0][0][0]