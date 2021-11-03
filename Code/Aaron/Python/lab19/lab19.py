import requests
import json
import html

# response = requests.get('https://opentdb.com/api.php?amount=10&category=18&type=boolean')

response = requests.get('https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=boolean')


# print(html.unescape('&quot;hello &amp; world&quot;'))

# print(response.status_code)

questions = json.loads(response.text)

# questions = questions["results"][0]["question"]


correct = 0 
incorrect = 0 
for i in range(10):

    answer = input(html.unescape(questions["results"][i]["question"]))

    if answer == questions["results"][i]['correct_answer']: 
        correct += 1

    else: 
        incorrect += 1
    
print(f"\nYou answered {correct} questions correctly and {incorrect} questions incorrectly.\n")





# print(html.unescape(questions))

# print(questions)