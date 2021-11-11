import requests

response = requests.get('https://icanhazdadjoke.com', headers={'accept': 'application/json'}).json()

print(response.get("joke"))

# data = response.json()

# print(type(data))


# print(response)

# print(response.text)

# print(data['fac'])