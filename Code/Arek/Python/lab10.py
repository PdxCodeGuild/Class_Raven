# https://icanhazdadjoke.com/search?term=cat


"""
Dad Joke API

Use the Dad Joke API to get a dad joke and display it to the user. You may want to also use time.sleep to add suspense.
Part 1

Use the requests library to send an HTTP request to https://icanhazdadjoke.com/ with the accept header as application/json. 
This will return a dad joke in JSON format. You can then use the .json() method on the response to get a dictionary. 
Get the joke out of the dictionary and show it to the user.
Part 2 (optional)

Add the ability to "search" for jokes using another endpoint. 
Create a REPL that allows one to enter a search term and go through jokes one at a time. 
You can also add support for multiple pages.


"""

from time import sleep
import requests

#version 1
"""response = requests.get('https://icanhazdadjoke.com/', headers={'accept': 'application/json'})
data = response.json()
sleep(1)
print(data['joke'])"""

#version 2
usr_search = input("What do kind of jokes do you want to search for? ")
jokeNum = 0 #using this to cycle through different jokes
while True:
    if jokeNum == 10: # this is me being lazy and only letting the user look at 10 options for the word they entered
        print("Thats all the jokes for now, The jokes will now start over from the first option.")
        jokeNum = 0
    url = f"https://icanhazdadjoke.com/search?term={usr_search}" # using this to add the word the user entered to the endpoint URL
    response = requests.get(url, headers={'accept': 'application/json'}) #$on the website it says to use the accept header 'application/json' however at first I did not know that that was the value and 'accept' was the key.
    data = response.json() # this converts the json output into a dictionary for us to use in python
    print(data['results'][jokeNum]['joke'])
    print("\n")
    jokeNum += 1 # changing the index number if the user wants to see a different joke
    answer = input("Type 'next' to see a different joke or 'done' if you have found the perfect dad joke:\n")
    if answer != 'next' and answer != 'done': # just some input validation
        print("You did not enter the correct option. The program will now end.")
        exit()
    elif answer == 'done':
        print("Thanks for stopping by.")
        break
    
