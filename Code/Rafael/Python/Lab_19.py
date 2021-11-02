# Lab 19 Trivia API
# Rafael Medina


""" 
NOTE: In progress 11/2/2021
NOTE: To self.. See if you can rewirte this more efficiently without having to number each list item, maybe there is a way to switch to the next library item in a loop from an index, value perspective. Also fix the score. it is broken printing -6 on firts 'f' and 0 after 10x 't'
"""
"""
Send a request to the following url: https://opentdb.com/api.php?amount=10&category=18&type=boolean This will return a list of 10 true/false computer questions. Ask the user each question, ask them for their answer, and keep track of the score. At the end show them how many they got correct/incorrect.

Certain characters in the question text are encoded, to decode them you'll have to use the html module's unescape method.

"""

"""
{'category': 'Science: Computers', 'type': 'boolean', 'difficulty': 'medium', 'question': 'All program codes have to be compiled into an executable file in order to be run. This file can then be executed on any machine.', 'correct_answer': 'False', 'incorrect_answers': ['True']}, 
{'category': 'Science: Computers', 'type': 'boolean', 'difficulty': 'easy', 'question': 'The programming language &quot;Python&quot; is based off a modified version of &quot;JavaScript&quot;.', 'correct_answer': 'False', 'incorrect_answers': ['True']},
{'category': 'Science: Computers', 'type': 'boolean', 'difficulty': 'medium', 'question': 'To bypass US Munitions Export Laws, the creator of the PGP published all the source code in book form. ', 'correct_answer': 'True', 'incorrect_answers': ['False']},
{'category': 'Science: Computers', 'type': 'boolean', 'difficulty': 'easy', 'question': 'Ada Lovelace is often considered the first computer programmer.', 'correct_answer': 'True', 'incorrect_answers': ['False']},
{'category': 
'Science: Computers', 'type': 'boolean', 'difficulty': 'medium', 'question': 'The open source program Redis is a relational database server.', 'correct_answer': 'False', 'incorrect_answers': ['True']},
{'category': 'Science: Computers', 'type': 'boolean', 'difficulty': 'hard', 'question': 'DHCP stands for Dynamic Host Configuration Port.', 'correct_answer': 'False', 'incorrect_answers': ['True']},
{'category': 'Science: Computers', 'type': 'boolean', 'difficulty': 'easy', 'question': 'Time on Computers is measured via the EPOX System.', 'correct_answer': 'False', 'incorrect_answers': ['True']},
{'category': 'Science: Computers', 'type': 'boolean', 'difficulty': 'medium', 'question': 'It&#039;s not possible to format a write-protected DVD-R Hard Disk.', 'correct_answer': 'True', 'incorrect_answers': ['False']},
{'category': 'Science: Computers', 'type': 'boolean', 'difficulty': 'medium', 'question': 'A Boolean value of &quot;0&quot; represents which of these words?', 'correct_answer': 'False', 'incorrect_answers': ['True']},
{'category': 'Science: Computers', 'type': 'boolean', 'difficulty': 'easy', 'question': 'The Python programming language gets its name from the British comedy group &quot;Monty Python.&quot;', 'correct_answer': 'True', 'incorrect_answers': ['False']}
"""

import html
import requests


url = 'https://opentdb.com/api.php?amount=10&category=18&type=boolean'


response = requests.get(url)


response = response.json()

response = response['results']

# response [200] meaning link is valid.
#response.encoding = 'utf-8'

print(response)
print(type(response))
print(len(response))

header = (f'\n        Trivia API\n')

print(header)


questions = 0
points = 0

# replace the html characters with regular characters from the listed dictionaries and have them output at each print before when the question is given.

#if questions > 9 and questions < 10 or questions == 0:


while True:



        print("\n1st) question is",response[0]['category'],'and the dificulty is',response[0]['difficulty'],'\n\nThe question is:', response[0]['question'], "Is this True 't' or False 'f' ? Type 't' of 'f'")
        user_input = input()

        if user_input == 't' and response[0]['correct_answer'] == ['True']:
            points += 1
    
        if  user_input == 'f' and response[0]['incorrect_answers'] == ['False']:
            points += 1

        if  user_input == 'f' and response[0]['incorrect_answers'] == ['true']  or user_input == 'f' and response[0]['correct_answer']: 
            points -= 1

        else:
            print("\n2nd) question is",response[1]['category'],'and the dificulty is',response[1]['difficulty'],'\n\nThe question is:', response[1]['question'], "Is this True 't' or False 'f' ?")
            user_input = input()

        if user_input == 't' and response[1]['correct_answer'] == ['True']:
            points += 1
    
        if  user_input == 'f' and response[1]['incorrect_answers'] == ['False']:
            points += 1

        if  user_input == 'f' and response[1]['incorrect_answers'] == ['true']  or user_input == 'f' and response[1]['correct_answer']: 
            points -= 1
           
        else:            
            print("\n3rd) question is",response[2]['category'],'and the dificulty is',response[2]['difficulty'],'\n\nThe question is:', response[2]['question'], "Is this True 't' or False 'f' ?")
            user_input = input()
        if user_input == 't' and response[2]['correct_answer'] == ['True']:
            points += 1
    
        if  user_input == 'f' and response[2]['incorrect_answers'] == ['False']:
            points += 1

        if  user_input == 'f' and response[2]['incorrect_answers'] == ['true']  or user_input == 'f' and response[0]['correct_answer']: 
            points -= 1
        else:            
            print("\n4th) question is",response[3]['category'],'and the dificulty is',response[3]['difficulty'],'\n\nThe question is:', response[3]['question'], "Is this True 't' or False 'f' ?")
            user_input = input()

        if user_input == 't' and response[3]['correct_answer'] == ['True']:
            points += 1
    
        if  user_input == 'f' and response[3]['incorrect_answers'] == ['False']:
            points += 1

        if  user_input == 'f' and response[3]['incorrect_answers'] == ['true']  or user_input == 'f' and response[3]['correct_answer']: 
            points -= 1

        else:            
            print("\n5th) question is",response[4]['category'],'and the dificulty is',response[4]['difficulty'],'\n\nThe question is:', response[4]['question'], "Is this True 't' or False 'f' ?")
            user_input = input()

        if user_input == 't' and response[4]['correct_answer'] == ['True']:
            points += 1
    
        if  user_input == 'f' and response[4]['incorrect_answers'] == ['False']:
            points += 1

        if  user_input == 'f' and response[4]['incorrect_answers'] == ['true']  or user_input == 'f' and response[4]['correct_answer']: 
            points -= 1

        else:            
            print("\n6th) question is",response[5]['category'],'and the dificulty is',response[5]['difficulty'],'\n\nThe question is:', response[5]['question'], "Is this True 't' or False 'f' ?")
            user_input = input()

        if user_input == 't' and response[5]['correct_answer'] == ['True']:
            points += 1
    
        if  user_input == 'f' and response[5]['incorrect_answers'] == ['False']:
            points += 1

        if  user_input == 'f' and response[5]['incorrect_answers'] == ['true']  or user_input == 'f' and response[5]['correct_answer']: 
            points -= 1

        else:            
            print("\n7th) question is",response[6]['category'],'and the dificulty is',response[6]['difficulty'],'\n\nThe question is:', response[6]['question'], "Is this True 't' or False 'f' ?")
            user_input = input()

        if user_input == 't' and response[6]['correct_answer'] == ['True']:
            points += 1
    
        if  user_input == 'f' and response[6]['incorrect_answers'] == ['False']:
            points += 1

        if  user_input == 'f' and response[6]['incorrect_answers'] == ['true']  or user_input == 'f' and response[6]['correct_answer']: 
            points -= 1

        else:            
            print("\n8th) question is",response[7]['category'],'and the dificulty is',response[7]['difficulty'],'\n\nThe question is:', response[7]['question'], "Is this True 't' or False 'f' ?")
            user_input = input()

        if user_input == 't' and response[7]['correct_answer'] == ['True']:
            points += 1
    
        if  user_input == 'f' and response[7]['incorrect_answers'] == ['False']:
            points += 1

        if  user_input == 'f' and response[7]['incorrect_answers'] == ['true']  or user_input == 'f' and response[7]['correct_answer']: 
            points -= 1

        else:            
            print("\n9th) question is",response[8]['category'],'and the dificulty is',response[8]['difficulty'],'\n\nThe question is:', response[8]['question'], "Is this True 't' or False 'f' ?")
            user_input = input()

        if user_input == 't' and response[8]['correct_answer'] == ['True']:
            points += 1
    
        if  user_input == 'f' and response[8]['incorrect_answers'] == ['False']:
            points += 1

        if  user_input == 'f' and response[8]['incorrect_answers'] == ['true']  or user_input == 'f' and response[8]['correct_answer']: 
            points -= 1

        else:            
            print("\n10th) question is",response[9]['category'],'and the dificulty is',response[4]['difficulty'],'\n\nThe question is:', response[9]['question'], "Is this True 't' or False 'f' ?")
            user_input = input()

        if user_input == 't' and response[9]['correct_answer'] == ['True']:
            points += 1
    
        if  user_input == 'f' and response[9]['incorrect_answers'] == ['False']:
            points += 1

        if  user_input == 'f' and response[9]['incorrect_answers'] == ['true']  or user_input == 'f' and response[9]['correct_answer']: 
            points -= 1

        if questions == 0: 
                break
                    
print(f'You got {points} out of 10')


"""
user_input = input("Welcome to trivia 10 questions, would you like to play? 'y' or 'n':\n")
    if user_input == 'y':  

        if user_input == 'n':
            break
    
"""


# Create a for loop to replace the html characters with regular characters from the listed dictionaries and have them output at each print before an answer is given.

