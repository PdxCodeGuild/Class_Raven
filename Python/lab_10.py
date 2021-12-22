"""
Lee Colburn
Evening Bootcamp - PDX Code Guild
Lab 10 - Dad Jokes ... and Their APIs
"""
import requests
url = "https://icanhazdadjoke.com/search?term="
user_search_term = input("Enter a search term: ")
response = requests.get(url+user_search_term, headers={"Accept": "application/json"})
data = response.json()

total_results = data['total_jokes']
print(f"There were {total_results} jokes found.\n")

results = data['results']
counter = 1

for result in results:
    print(f"Joke {counter}/{total_results}")
    joke = result['joke']
    print(joke)
    counter += 1
    if counter > total_results:
        break
    more_jokes = input("\nWant more? Enter 1 to continue: ")
    if more_jokes == "1":
        pass
    else:
        break
