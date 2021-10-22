import requests
#user_search = input("Enter a search term: ")

response = requests.get('https://icanhazdadjoke.com'
,headers = {
'Accept': 'application/json'
})


#how to take user input and search the website with that term.
data = response.json()
print(data)

