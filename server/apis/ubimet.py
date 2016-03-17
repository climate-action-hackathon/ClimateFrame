import requests
import json

warnings_dict = {
    'tropical_cyclone': 0,
    'tornado': 3,
    'blizzard': 6,
    'monsoon': 9,
    'snow': 12,
    'freezing rain': 15,
    'thunderstorm': 18,
    'rain': 21,
    'wind': 24,
    'swell': 27,
    'fire_risk': 30,
    'uv_index': 33,
    'frost': 36
}

def get_current_warning(latitude, longitude):
    with open('../config.json') as config_file:
        key = json.load(config_file)['keys']['p_key']
        extreme_now_endpoint = 'https://met-api.ubimet.at:8090/pinpoint-data?sets=extreme_now'
        location = longitude + ' ' + latitude
        request_url = extreme_now_endpoint + '&coordinates=' + location
        response = requests.get(request_url,
            verify=False,
            headers={'Authorization': 'Token 0ae17c9399cd016022a68595adcb4322780d941f'})
        return response.json()[0]['met_sets'][0]['parameter_timesets'][0]['data'][0][0][0]

def is_warning(current_warning, warning_code, minimum_level):
    if minimum_level < 1 or 3 < minimum_level:
        print 'Warning: minimum_level must be between 1 and 3'
    return warning_code + minimum_level - 1 <= current_warning  and current_warning <= warning_code + 2

# minimum_level is an integer from 1 to 3
def is_tropical_cyclone_warning(latitude, longitude, minimum_level):
    current_warning = get_current_warning(latitude, longitude)
    warning_code = warnings_dict['tropical_cyclone']
    return is_warning(current_warning, warning_code, minimum_level)

# minimum_level is an integer from 1 to 3
def is_tornado_warning(latitude, longitude, minimum_level):
    current_warning = get_current_warning(latitude, longitude)
    warning_code = warnings_dict['tornado']
    return is_warning(current_warning, warning_code, minimum_level)

# minimum_level is an integer from 1 to 3
def is_blizzard_warning(latitude, longitude, minimum_level):
    current_warning = get_current_warning(latitude, longitude)
    warning_code = warnings_dict['blizzard']
    return is_warning(current_warning, warning_code, minimum_level)

# minimum_level is an integer from 1 to 3
def is_monsoon_warning(latitude, longitude, minimum_level):
    current_warning = get_current_warning(latitude, longitude)
    warning_code = warnings_dict['monsoon']
    return is_warning(current_warning, warning_code, minimum_level)

# minimum_level is an integer from 1 to 3
def is_snow_warning(latitude, longitude, minimum_level):
    current_warning = get_current_warning(latitude, longitude)
    warning_code = warnings_dict['snow']
    return is_warning(current_warning, warning_code, minimum_level)

# minimum_level is an integer from 1 to 3
def is_freezing_warning(latitude, longitude, minimum_level):
    current_warning = get_current_warning(latitude, longitude)
    warning_code = warnings_dict['freezing']
    return is_warning(current_warning, warning_code, minimum_level)

# minimum_level is an integer from 1 to 3
def is_thunderstorm_warning(latitude, longitude, minimum_level):
    current_warning = get_current_warning(latitude, longitude)
    warning_code = warnings_dict['thunderstorm']
    return is_warning(current_warning, warning_code, minimum_level)

# minimum_level is an integer from 1 to 3
def is_rain_warning(latitude, longitude, minimum_level):
    current_warning = get_current_warning(latitude, longitude)
    warning_code = warnings_dict['rain']
    return is_warning(current_warning, warning_code, minimum_level)

# minimum_level is an integer from 1 to 3
def is_wind_warning(latitude, longitude, minimum_level):
    current_warning = get_current_warning(latitude, longitude)
    warning_code = warnings_dict['wind']
    return is_warning(current_warning, warning_code, minimum_level)

# minimum_level is an integer from 1 to 3
def is_swell_warning(latitude, longitude, minimum_level):
    current_warning = get_current_warning(latitude, longitude)
    warning_code = warnings_dict['swell']
    return is_warning(current_warning, warning_code, minimum_level)

# minimum_level is an integer from 1 to 3
def is_fire_risk_warning(latitude, longitude, minimum_level):
    current_warning = get_current_warning(latitude, longitude)
    warning_code = warnings_dict['fire_risk']
    return is_warning(current_warning, warning_code, minimum_level)

# minimum_level is an integer from 1 to 3
def is_uv_index_warning(latitude, longitude, minimum_level):
    current_warning = get_current_warning(latitude, longitude)
    warning_code = warnings_dict['uv_index']
    return is_warning(current_warning, warning_code, minimum_level)

# minimum_level is an integer from 1 to 3
def is_frost_warning(latitude, longitude, minimum_level):
    current_warning = get_current_warning(latitude, longitude)
    warning_code = warnings_dict['frost']
    return is_warning(current_warning, warning_code, minimum_level)
