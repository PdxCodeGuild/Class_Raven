import requests #<----Why does this still has a squigly line under it?
response = requests.get('https://icanhazdadjoke.com/', headers = {'accept': 'application/json'})
data = response.json()
joke = data["joke"]
print("Random Dad joke:", joke)