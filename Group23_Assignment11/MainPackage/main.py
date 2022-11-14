#main.py
import requests
import json
from functions import html_Cleaner as hc
#gets data from NASA API
response = requests.get('https://api.nasa.gov/techtransfer/spinoff/?engine&api_key=ADNQpEjTKmiNQlpGKnP7KfiCTfrZ9qLpsoAsVtjr')
#stores data as a string
json_string = response.content 
#cleans data, removing HTML formatting from strings
data = json.loads(json_string)
hc.cleanup(data)
json_string = json.dumps(data)

parsed_json = json.loads(json_string) # Now we have a python dictionary

#showing some interesting data from NASA Tech Transfer
print(parsed_json['results'][6][2])
print(parsed_json['results'][6][3])