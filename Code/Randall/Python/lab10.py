import requests
response = requests.get('https://icanhazdadjoke.com/', headers = {'accept': 'application/json'})
data = response.json()
joke = data["joke"]
print("Random Dad joke:", joke)