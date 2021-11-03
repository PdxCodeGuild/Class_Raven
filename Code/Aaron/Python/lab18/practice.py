import requests
import json
import html




response = requests.get('https://opentdb.com/api.php?amount=10&category=18&type=boolean')


# print(html.unescape('&quot;hello &amp; world&quot;'))

# print(response.status_code)

questions = json.loads(response.text)
correct = 0 
incorrect = 0 
for question in questions['results']:
    answer = input(question['question'])
    if answer == question['correct_answer']: correct += 1
    else: incorrect += 1
    
print(f"You answered {correct} questions correctly and {incorrect} questions incorrectly.")
