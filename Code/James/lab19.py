"""  Trivia API """
import html
import requests

class trivia:
    def __init__(self):
        self.info = []


    def load(self):
        response = requests.get('https://opentdb.com/api.php?amount=10&category=23', params={'format': 'json'})
        #print(response.text)
        contents = response.json() # this is python dictionary
        # now get question out of the dictionary
        questions = contents['results'] # gives all the data from the api
        
        self.info = questions # now the class is initialized
        
        print(self.info)
    
    
    # def print():

trivia = trivia() # create instance of our class
trivia.load()


# print('Welcome to history trivia')
# while True:
    