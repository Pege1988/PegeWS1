# Program to retrieve data from weather station using Ecowitt API v3 
# Version 3.0.0
from configparser import ConfigParser
import os
import urllib.parse as urlparse
from urllib.parse import urlencode

import api
import store_data as sd

path = os.path.dirname(os.path.realpath(__file__))

config = ConfigParser()
config.read(os.path.join(path, 'config.ini'))

database = os.path.join(path,"PegeWS1.sqlite")

# Base Ecowitt url
url = "https://api.ecowitt.net/api/v3/device/real_time?"

# Different request parameters
params = {'application_key': config['api']['APPLICATION_KEY'],'api_key': config['api']['API_KEY'], 'mac': config['api']['MAC_CODE'], 'temp_unitid': config['units']['temp_unitid'], 'pressure_unitid': config['units']['pressure_unitid'], 'wind_speed_unitid': config['units']['wind_speed_unitid'], 'rainfall_unitid': config['units']['rainfall_unitid'], 'solar_irradiance_unitid': config['units']['solar_irradiance_unitid'], 'call_back': 'all'}

url_parts = list(urlparse.urlparse(url))
query = dict(urlparse.parse_qsl(url_parts[4]))
query.update(params)
url_parts[4] = urlencode(query)
api_request = urlparse.urlunparse(url_parts)

# Get json file and make available for further processing
PWS1_json = api.read_json(api_request, database)
PWS1_data = api.get_data(PWS1_json, database)

if __name__ == '__main__':
    sd.save_file_status(PWS1_data, database)
    sd.save_outdoor_data(PWS1_data, database)
    sd.save_indoor_data(PWS1_data, database)
    sd.save_pressure_data(PWS1_data, database)
    sd.save_solar_and_uvi_data(PWS1_data, database)
    sd.save_wind_data(PWS1_data, database)
    sd.save_rainfall_data(PWS1_data, database)