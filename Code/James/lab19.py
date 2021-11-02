"""  Trivia API """
import html
import requests

class trivia:
    #def __init__(self):
    def load():
        response = requests.get('https://opentdb.com/api.php?amount=10&category=23', params={'format': 'json'})
        #print(response.text)
        data = response.json()
        print(data)


trivia.load()


print('Welcome to history trivia')
while True:
    