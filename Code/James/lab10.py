import requests
#user_search = input("Enter a search term: ")

response = requests.get('https://icanhazdadjoke.com/search'
,headers = {
'Accept': 'application/json'
})


#how to take user input and search the website with that
data = response.json() # this is saved as dictionary

print(type(data))


#how to search through all the dictionaries to find the users search term?


user = input('Enter a search term: ')

if user in data.values():
    print(data.values())
# find = data[user]
# print(find)