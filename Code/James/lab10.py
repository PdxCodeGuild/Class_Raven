import requests
#user_search = input("Enter a search term: ")

user = input('Enter a search term: ')

response = requests.get(f'https://icanhazdadjoke.com/search?term={user}'
,headers = {
'Accept': 'application/json'
}) # trying to add a search term in the api


#how to take user input and search the website with that
data = response.json() # this is saved as dictionary

print(data['results'][0]['joke'])


#how to search through all the dictionaries to find the users search term?




# if user in data.values():
#     print(data.values())
# find = data[user]
# print(find)