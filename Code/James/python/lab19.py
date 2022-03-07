"""  Trivia API """
import html
import requests

class trivia:
    def __init__(self):
        self.info = []
        self.correct_answers = []
        self.i = 0
        self.points = 0
        self.current_question = 1

    def load(self):
        response = requests.get('https://opentdb.com/api.php?amount=10&category=23&type=boolean', params={'format': 'json'})
        #print(response.text)
        contents = response.json() # this is python dictionary
        # now get question out of the dictionary
        questions = contents['results'] # gives all the data from the api
        
        self.info = questions # now the class is initialized

        
        
        

        
        
        
    def questions_answers(self):    
       
       for question in self.info:
            #print(html.unescape(question['question']))
            self.correct_answers.append(html.unescape(question['correct_answer'])) # questoin is just an iterable its not important
            
    
    def answer_checker(self, user_answer):
           
        if user_answer == self.correct_answers[self.i]:
            print('Correct')
            self.i += 1
            self.points += 1
            return True
            

        elif user_answer != self.correct_answers[self.i]:
            print('Incorrect')
            self.i += 1
            return False
            
        

            
            
            
        
    
    
trivia = trivia() # create instance of our class
trivia.load()
trivia.questions_answers()



print('Welcome to history trivia enter True or False for the following questions.')
counter = 0
play = True



while play:
     #added these three lines to check if answers were correct and they are.
    
    # print(trivia.info)
    print(trivia.current_question, html.unescape(trivia.info[counter]['question']))  
    # print(trivia.current_question, html.unescape(trivia.info[counter]['correct_answer']))
    
    user_answer = input('Enter True or False: ').capitalize()
    
    if user_answer not in  ['True', 'False']:
        print('Please enter True or False only.')
        continue
    
    trivia.answer_checker(user_answer)
    
    counter += 1
    trivia.current_question += 1
    
    
    if counter == 10:
        print(f'You answered {trivia.points} questions correctly')
        play_again = (input('Do you want to play again type yes or no \n>> ')).lower()
        if play_again == 'no':
            play = False
        
        elif play_again == 'yes':
            trivia.load()
            counter = 0
           
            



    