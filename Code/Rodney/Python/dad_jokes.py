
import requests  ## library that allows us to send http requests and get data from that website 
import time ##provides various time related functions

response = requests.get('https://icanhazdadjoke.com', headers = {'Accept': 'application/json'})
## sending GET request to retrieve body of text from website 
data = response.json()  ## turning raw json into a python dict

dad_joke = input("Hey there! Want to hear a good dad joke:\n> ") ## input function to ask if user wants to hear joke 

while True:
    if dad_joke == 'yes':
        time.sleep(2)
        print(data['joke'])  ## asccessing the value of the joke key in library that we received
        break
    else: 
        break


