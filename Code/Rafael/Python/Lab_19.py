# Lab 19 Trivia API
# Rafael Medina


"""
NOTE: Part 1 complete with the exeption of getting html module's unescape method to work correctly.
"""


"""
Send a request to the following url: https://opentdb.com/api.php?amount=10&category=18&type=boolean This will return a list of 10 True/false computer questions. Ask the user each question, ask them for their answer, and keep track of the score. At the end show them how many they got correct/incorrect.

Certain characters in the question text are encoded, to decode them you'll have to use the html module's unescape method.

"""

"""
# Example on how the response from .json is displayed as an object and then accessed as a list of dicts in this case 10 lists.
[
{'category': 'Science: Computers', 'type': 'boolean', 'difficulty': 'medium', 'question': 'All program codes have to be compiled into an executable file in order to be run. This file can then be executed on any machine.', 'correct_answer': 'False', 'incorrect_answers': ['True']}, 
{'category': 'Science: Computers', 'type': 'boolean', 'difficulty': 'easy', 'question': 'The programming language &quot;Python&quot; is based off a modified version of &quot;JavaScript&quot;.', 'correct_answer': 'False', 'incorrect_answers': ['True']},
{'category': 'Science: Computers', 'type': 'boolean', 'difficulty': 'medium', 'question': 'To bypass US Munitions Export Laws, the creator of the PGP published all the source code in book form. ', 'correct_answer': 'True', 'incorrect_answers': ['False']},
{'category': 'Science: Computers', 'type': 'boolean', 'difficulty': 'easy', 'question': 'Ada Lovelace is often considered the first computer programmer.', 'correct_answer': 'True', 'incorrect_answers': ['False']},
{'category': 'Science: Computers', 'type': 'boolean', 'difficulty': 'medium', 'question': 'The open source program Redis is a relational database server.', 'correct_answer': 'False', 'incorrect_answers': ['True']},
{'category': 'Science: Computers', 'type': 'boolean', 'difficulty': 'hard', 'question': 'DHCP stands for Dynamic Host Configuration Port.', 'correct_answer': 'False', 'incorrect_answers': ['True']},
{'category': 'Science: Computers', 'type': 'boolean', 'difficulty': 'easy', 'question': 'Time on Computers is measured via the EPOX System.', 'correct_answer': 'False', 'incorrect_answers': ['True']},
{'category': 'Science: Computers', 'type': 'boolean', 'difficulty': 'medium', 'question': 'It&#039;s not possible to format a write-protected DVD-R Hard Disk.', 'correct_answer': 'True', 'incorrect_answers': ['False']},
{'category': 'Science: Computers', 'type': 'boolean', 'difficulty': 'medium', 'question': 'A Boolean value of &quot;0&quot; represents which of these words?', 'correct_answer': 'False', 'incorrect_answers': ['True']},
{'category': 'Science: Computers', 'type': 'boolean', 'difficulty': 'easy', 'question': 'The Python programming language gets its name from the British comedy group &quot;Monty Python.&quot;', 'correct_answer': 'True', 'incorrect_answers': ['False']}
]
"""

import html

import requests

# url copied from Lab_19 instructions. Or you can go to the site and custumize your own.
url = 'https://opentdb.com/api.php?amount=10&category=18&type=boolean'

# Gets the url data and assigns it to response.
response = requests.get(url)

# response [200] meaning link is valid.
#response.encoding = 'utf-8'

# To get out of the response[200] and convert the response to .json object.
response = response.json() # "It's not possible to format a write-protected DVD-R Hard Disk" error if using the html.unescape(response) on .json response

# Assigns the requested response to a list of dicts to be able to access from response{}

response = response['results']

"""
print()
print(response,'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
"""
#decoded_string = html.unescape(response)# Takes out html characters from requested response.

#print(response)
#print(type(response))
#print(len(response))
  


header = (f'\n                     Trivia API')# Centering the header over the bottom text.

print(header)


points = 0 # Note: to keep point values staring tally outside the loop and not inside to reset the values each cycle. 
index = -1 # Negative value 1 allows for the while loop to start at 0 and run less than 10 times up to index[9]


# http://projectpython.net/chapter07/ reference on how to begin a while loop for multiple lists.

while index < 9: # 10 cycles
    index = index + 1 # Takes away a cycle each loop.

    print("\nThe topic is",response[index]['category'],':'' The dificulty is',response[index]['difficulty'],':''\n\nThe question is:', response[index]['question'], "\nIs this True 't' or False 'f' ? ")
    
    user_input = input()

# Note that only 'incorrect_answers' could be used for this boleean checks. I tried boolean the "correct_answer" and it was not getting a response from the loop progression. 
    if user_input == 'f' and response[index]['incorrect_answers'] == ['True']:
        points = points + 1
    
    elif  user_input == 't' and response[index]['incorrect_answers'] == ['False']:
        points = points + 1

    elif user_input == 'f' and response[index]['incorrect_answers'] != ['True']:
        points = points + 0
    
    elif  user_input == 't' and response[index]['incorrect_answers'] != ['False']:
        points = points + 0
    # One liner version of the last elif's shown.
    #if  user_input == 'f' and response[index]['correct_answer'] == ['True'] or  user_input == 't' and response[index]['correct_answer'] == ['False']: 
            #points = points + 0 
    else:
        print('Looks you typed a wrong response, please try the 10 question trivia again')
        break
print(f'You got {points} out of 10 points.')
           
    
    
        
        
        
"""      
    print('Looks you typed a wrong response, please try the trivia again')        
      user_input("Type 'yes' to continue a new trivia or 'no' to quit")
    if user_input == 'yes':
        index = -1
    if user_input == 'no':
        break
"""
