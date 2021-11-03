import html
import json
import requests

#Send request
response = requests.get('https://opentdb.com/api.php?amount=10&category=18&type=boolean')
response = html.unescape(response)
response = response.json()

response = response['results']
#print(response)
#Create question/answer dictionary
question_answer_dictionary = {}
index = 0
#Pull list from dictionary
for x in response:
    key = x['question']
    value = x['correct_answer']
    question_answer_dictionary[key] = value
    index += 1

#print(question_answer_dictionary)
#print(index)


#Create a second dictionary to assign the question to a number
'''user_answer_dictionary= {}
index = 0
for user_answer in response:
    key = index + 1
    value = correct_answer['correct_answer']
    user_answer_dictionary[key] = value
    index += 1
print(user_answer_dictionary)
#print(correct_answer_index)'''

#Create a third dictionary to store results for each number

index = 0
correct = 0
for question in question_answer_dictionary:
    value = input(f'True/False: {question}')
    if question_answer_dictionary[question] == value:
        correct += 1
    index += 1
print(f'You got a total of {correct} correct')
#print(index)


