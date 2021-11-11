import requests
import html
import json
import unicodedata

quiz = requests.get('https://opentdb.com/api.php?amount=10&category=22&difficulty=medium&type=boolean', headers = {'accept': 'application/json'})
#dictionary contains parameters for the header.. whatever that means.
data = quiz.json()
X = data['results']
Y = X[0]
total_c =0
total_i = 0

def question(question, correct, incorrect):
    query = ' '
    stop = 0
    #print(Y['correct_answer']) #check for value
    #print(Y['incorrect_answers']) #check for value
    while stop <2:
        query = input(f"{html.unescape(Y['question'])}\n>") #read question. Get feedback
        if query == 'True' or query =='False': #suitable feedback becomes bool
            bool(query)
        if query != 'True' and query != 'False': #unsuitable feedback gets a request to clarify
            #print(type(query)) #check data type
            #print("Invalid choice;type True or False.")
            continue  
        if query == Y['correct_answer']:
            stop +=3
            return True
        elif query != Y['correct_answer']:
            stop+=3
            return False
        #else:
        #    print("Invalid choice;type True or False?")

for Y in X:
    if question(Y['question'], Y['correct_answer'], Y['incorrect_answers']) == True:
        total_c += 1
    else:
        total_i += 1
print(f"total correct answer(s);{total_c}\ntotal incorrect answer(s);{total_i} ")

# W = question(Y['question'], Y['correct_answer'], Y['incorrect_answers']) # function test for one question
# print(W)
