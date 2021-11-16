import requests

#Create a variable to store a response from a get request to an api to access dad jokes and include header information to request json format
response = requests.get('https://icanhazdadjoke.com/', headers={'accept': 'application/json'})
#Create another variable to convert the json in python readable text
data = response.json()
#Access the joke thorugh the 'joke' key from the returned dictionary and print
print(data['joke'])


'''term = input('Enter a search term: ')
number = input('How many do you want? ')
#Create a variable to store the URL which includes the base url for the search and concatenate with the search term
url = 'https://icanhazdadjoke.com/search?term=' + term
#Create a variable to store the get request
search_response = requests.get(url, headers={'accept': 'application/json'})
#Convert the search response from json to a python dictionary
data = search_response.json()
#Access the key 'results' from the dictionary of responses and store as a variable
joke_data = data['results']
print(data['results'])'''



