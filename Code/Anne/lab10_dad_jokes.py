# Use the requests library to send an HTTP request to https://icanhazdadjoke.com/ 
# with the accept header as application/json. 
# This will return a dad joke in JSON format.
#  You can then use the .json() method on the response to get a dictionary. 
#  Get the joke out of the dictionary and show it to the user.


import requests
# response = requests.get('https://icanhazdadjoke.com', headers = {'accept': 'application/json'}) 
# data = response.json() # turn raw json into a python dictionary
# print(data['joke'])

response = requests.get('https://catfact.ninja/facts')
the_data = response.json()
print(the_data['data'][1]['fact']) #headers = {'accept': 'application/json'}) 
