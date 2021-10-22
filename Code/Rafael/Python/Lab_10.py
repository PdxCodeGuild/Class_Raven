# Lab_10 Dad JokeAPI

import requests
import time
import random


url = "https://icanhazdadjoke.com/search"

response = requests.get(url)
# if Response [200] then it is valid
#print(response)

response.encoding = 'utf-8'

header = (f'\n        Dad Joke\n')
print(header)

while True:
    search = input("Enter a topic to search: ")

# returns the header in JSON format
    json_format = requests.get(f"{url}?term={search}", headers= {f"Accept":"application/json"},params={"search": search}).json()

    results = json_format["results"]
# displays the number of jokes
    total_jokes = json_format["total_jokes"]

# 3 second joke delay
    if total_jokes:
        print(f'\n         {total_jokes} found;\n Wait for it... wait for it...\n')
    time.sleep(3)
# random.choice picks a random joke
    print(f'Here is 1 Dad joke about {search}: {random.choice(results)}\n')
# Search again?  
    again = input('Would you like to try another search? "y" or "n" : ')
    
    if again == "y":
        continue

    else: 
        break
        
   
"""
# Need to figure out how to get rid of params id on print {'id': 'cUvsHt41gFd', 'joke':

# Tried different combination to get this if to work.
if results not in search:
        print('Sorry no results')
        again = input('Would you like to try another search? "y" or "no" : ')
"""