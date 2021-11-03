'''Lab 19 Trivia
By Philip Bartoo
10/2/2021'''

#Import the modules we will need for this exercise
import html
import json
import requests

#Send request to the API to get 10 trivia questions
response = requests.get('https://opentdb.com/api.php?amount=10&category=18&type=boolean')
#Use unescape to convert HTML to standard text (it didn't seem to work for me)
response = html.unescape(response)
#Convert from json to text
response = response.json()
#Go in and pull results for response dictionary
response = response['results']
#print(response)

#Create question/answer dictionary to store the question as a key and the correct_answer as the value, and create a counter
question_answer_dictionary = {}
index = 0
#Iterate through the response dictionary and pull out the question as the key and the correct answer as the value
for x in response:
    key = x['question']
    value = x['correct_answer']
#Assign the key/value pair to the question_answer_dictionary and increment the counter by 1
    question_answer_dictionary[key] = value
    index += 1

#print(question_answer_dictionary)
#print(index)

#Now it's time to loop through the questions and calculate how many responses are correct
#Start by creating a counter for the loop and a counter for the number of correct responses
user_answers = {}
index = 0
correct = 0
#Loop through the question_answer_dictionary
for question in question_answer_dictionary:
#Present the question to the user and request a True/False answer
    value = input(f'True/False: {question}')
#Evaluate the response by comparing it to the value in the question_answer_dictionary
    if question_answer_dictionary[question] == value:
#If the response evaluates to correct, increment the correct counter by 1
        correct += 1
    else:
        user_answers[question] = value
#Increment the loop counter by 1 to continue to the next question
    index += 1
#Print the total number correct
print(f'You got a total of {correct} correct')

for key in user_answers:
    print('Incorrect Answer: ',key,'The correct answer was: ',value)

