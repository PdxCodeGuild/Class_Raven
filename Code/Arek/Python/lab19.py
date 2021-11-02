"""
Part 2 (optional)

The API has many more options for different difficulties, different categories, and both true/false and multiple choice questions.
 Below are list of dictionaries containing the parameter name (what gets put into the query string) and a friendly name to show the user. 
 Prompt the user for each of these parameters, and include them in the request to get the list of questions. 
 Ask the user each question, ask them for their answer, and keep track of the score. At the end show them how many they got correct/incorrect.


"""
#Part 1

#Modules being used
"""import requests
import html
from time import sleep

#Defining functions
def get_questions():
    questionList = requests.get('https://opentdb.com/api.php?amount=10&category=18&type=boolean')
    global data
    data = questionList.json()
    data = data['results']
    
def ask_question(): # This function will ask the user a question, compare it to the correct answer, and give them a point if answered correctly
    get_questions()
    score = 0
    question_number = 0
    for i in range(len(data)):
        question_number += 1
        print(f"Question {question_number}.) {html.unescape(data[i]['question'])}")
        sleep(0.5)
        inpVal = True
        while inpVal:
            user_answer = input("Is this True or False?\n")
            if user_answer != 'True' and user_answer != 'False':
                print('your only options are True or False.\n')
                continue
            else:
                if user_answer == html.unescape(data[i]['correct_answer']):
                    score += 1
                    inpVal = False
                elif user_answer != html.unescape(data[i]['correct_answer']):
                    inpVal = False          
    return score

print(f"Your score is: {ask_question}")"""


import requests
import html
from time import sleep

#Defining functions
def get_questions():
    diff = input(f"What difficulty do you want? Your choices are 'easy,'medium','hard': ")
    cat = input(f"What category do you want? Your choices are any number from 9-32: ")
    _type = input(f"what type of questions do you want? Your choices are 'multiple','boolean': ")
    questionList = requests.get('https://opentdb.com/api.php', params={
        'amount': '10',
        'difficulty': diff,
        'category': cat,
        'type': _type})
    
    global data
    data = questionList.json()
    data = data['results']
    
    
def ask_question(): # This function will ask the user a question, compare it to the correct answer, and give them a point if answered correctly
    get_questions()
    score = 0
    question_number = 0
    
    for i in range(len(data)):
        question_number += 1
        
        print(f"Question {question_number}.) {html.unescape(data[i]['question'])}")
        if html.unescape(data[i]['type']) == 'multiple':
            answer_choices = html.unescape(data[i]['correct_answer']).split(" ", 0) + html.unescape(data[i]['incorrect_answers'])
            print(f"Your answer choices are: {html.unescape(answer_choices)}")
        elif html.unescape(data[i]['type']) == 'boolean':
            print("Your answer choices are True or False")
        sleep(0.5)
        user_answer = input('Please enter your answer: \n').lower()
        if user_answer == html.unescape(data[i]['correct_answer']).lower():
            score += 1
        else:
            continue
    return score

print(f"Your Score is: {ask_question()}")

