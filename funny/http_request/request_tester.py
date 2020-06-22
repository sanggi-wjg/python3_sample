import json
from pprint import pprint

import requests
from requests import Request

with open("request_data/sample_jamy.json", "rb") as file:
    sample_json = json.load(file)

print(sample_json.get('apiMethod'))
result = requests.post(
    url = 'http://192.168.10.7/partner/jamy/',
    data = {
        'data': json.dumps(sample_json)
    },
    headers = { 'Accept': 'application/json' },
)

print(result)
print(result.headers)
print(result.history)
print(result.json())
