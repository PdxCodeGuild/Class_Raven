import requests

joke = requests.get('https://icanhazdadjoke.com/', headers = {'accept': 'application/json'})
#dictionary contains parameters for the header.. whatever that means.
data = joke.json()
#print(joke.json())
print(data['joke'])

'''
fact =requests.get('https://catfact.ninja/fact', headers = {'accept': 'application/json'})
data2 = fact.json()
print(data2['fact'])
'''