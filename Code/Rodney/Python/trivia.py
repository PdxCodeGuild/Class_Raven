import requests  # requests module allows us to send HTTP requests from python 
import html # html module (and unescape method) allows us to decode certain characters 
import json # json module allows us to turn raw json into python dictionary 

questions = requests.get('https://opentdb.com/api.php?amount=10&category=18&type=boolean', params={'format': 'json'}) # using get method of request module to send HTTP request and obtain data
questions_dict = questions.json() # turns raw json into a pythong dictionary 
responses = questions_dict['results'] # assigning the value of the 'results' key into a list of dictionaries called responses
number_correct = 0 # defining number correct

for question_dictionary in responses: # for loop to loop through each dictionary in response list 
    print(html.unescape(question_dictionary['question'])) # using unescape method to decode characters
    answer = input('True or False?\n> ').capitalize() # assigning input of user's respsonse to answer variable 
    while answer != 'True' and answer != 'False':  # if the answer is neither true nor false, ask again 
        answer = input('Please answer True or False only:\n> ').capitalize()
    if question_dictionary['correct_answer'] == answer:  # if user reponse equals the value of the correct answer key in each dictionary, user gets question correct 
        number_correct += 1  # if user answer is correct, adding 1 to tally of correct answers 
        
number_incorrect = 10 - number_correct 
print(f'You got {number_correct} answers corrrect and {number_incorrect} answers wrong!')


