import requests
import html

response = requests.get('https://opentdb.com/api.php?amount=10&category=18&type=boolean', params = {'format': 'json'})
data = response.json()

correct_answers = 0
incorrect_answers = 0
index = 0

while index <= 9:
    print(html.unescape (data['results'][index]['question']))
    user_input = input("Is this (True / False)?: ")

    if user_input == 'True' or 'False':
        if user_input == data['results'][index]['correct_answer']:
            correct_answers += 1
            index += 1
        else:
            incorrect_answers += 1
            index += 1



print(f"You got {correct_answers} correct answers.")
print(f"You also got {incorrect_answers} answers incorrect.")