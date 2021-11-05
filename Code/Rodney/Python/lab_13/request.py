


import requests

response = requests.get('https://catfact.ninja/fact', params={'format': 'json'})
print(response.text)

import json

data = json.loads(response.text)

print(data)
