"""
PDX Code Guild Full Stack Bootcamp
->Lab 18
  Trivia API
Michael B

Trivia API
Let's use the Open Trivia Database API to a write a quiz program.

Part 1
Send a request to the following url: https://opentdb.com/api.php?amount=10&category=18&type=boolean. 
This will return a list of 10 true/false computer questions. 
Ask the user each question, ask them for their answer, and keep track of the score. 
At the end show them how many they got correct/incorrect.

Certain characters in the question text are encoded, to decode them you'll have to use the html module's unescape method.

import html
print(html.unescape('&quot;hello&amp;world&quot;')) # "hello&world"
Part 2 (optional)
The API has many more options for different difficulties, different categories, and both true/false and multiple choice questions. 
Below are list of dictionaries containing the parameter name (what gets put into the query string) and a friendly name to show the user. 
Prompt the user for each of these parameters, and include them in the request to get the list of questions. 
Ask the user each question, ask them for their answer, and keep track of the score. At the end show them how many they got correct/incorrect.

    Save for later.
    def get_answer(self, question):
        if question['type'] == 'boolean': # If the question is a true/false question.
            answer = question['correct_answer'] # Get the correct answer.
        else: # If the question is a multiple choice question.
            answers = question['incorrect_answers'] # Get the incorrect answers.
            answers.append(question['correct_answer']) # Add the correct answer to the list of incorrect answers.
            shuffle(answers) # Shuffle the list of incorrect answers.
            answer = choice(answers) # Get a random answer from the list of incorrect answers.
        return answer
    

"""

import requests
from random import shuffle, choice
from html import unescape
from colorama import Fore, Style

class Trivia:
    def __init__(self) -> None:
        """
        Initialize the class.
        :return: None
        :rtype: None
        """
        self.questions = []
        self.score = 0
        self.total = 0
        self.difficulties = [
            { 'parameter': 'any', 'name': 'Any Difficulty'},
            { 'parameter': 'easy', 'name': 'Easy' },
            { 'parameter': 'medium', 'name': 'Medium' },
            { 'parameter': 'hard', 'name': 'Hard' }
        ]
        self.types = [
            { 'parameter': 'any', 'name': 'Any Type'},
            { 'parameter': 'multiple', 'name': 'Multiple Choice' },
            { 'parameter': 'boolean', 'name': 'True / False' }
        ]
        self.categories = [
            { 'parameter': 'any', 'name': 'Any Category' },
            { 'parameter': '9', 'name': 'General Knowledge' },
            { 'parameter': '10', 'name': 'Entertainment: Books' },
            { 'parameter': '11', 'name': 'Entertainment: Film' },
            { 'parameter': '12', 'name': 'Entertainment: Music' },
            { 'parameter': '13', 'name': 'Entertainment: Musicals &amp; Theatres' },
            { 'parameter': '14', 'name': 'Entertainment: Television' },
            { 'parameter': '15', 'name': 'Entertainment: Video Games' },
            { 'parameter': '16', 'name': 'Entertainment: Board Games' },
            { 'parameter': '17', 'name': 'Science &amp; Nature' },
            { 'parameter': '18', 'name': 'Science: Computers' },
            { 'parameter': '19', 'name': 'Science: Mathematics' },
            { 'parameter': '20', 'name': 'Mythology' },
            { 'parameter': '21', 'name': 'Sports' },
            { 'parameter': '22', 'name': 'Geography' },
            { 'parameter': '23', 'name': 'History' },
            { 'parameter': '24', 'name': 'Politics' },
            { 'parameter': '25', 'name': 'Art' },
            { 'parameter': '26', 'name': 'Celebrities' },
            { 'parameter': '27', 'name': 'Animals' },
            { 'parameter': '28', 'name': 'Vehicles' },
            { 'parameter': '29', 'name': 'Entertainment: Comics' },
            { 'parameter': '30', 'name': 'Science: Gadgets' },
            { 'parameter': '31', 'name': 'Entertainment: Japanese Anime &amp; Manga' },
            { 'parameter': '32', 'name': 'Entertainment: Cartoon &amp; Animations' }
        ]

    def get_data(self, url) -> dict:
        """
        Get the data from the url.
        :param url: The url to get the data from.
        :return: The data from the url.
        :rtype: dict
        """
        data = requests.get(url).json() # Get the data from the url.
        return data

    def get_question(self, data) -> dict:
        """
        Get the question from the data.
        :param data: The data from the url.
        :return: The question.
        :rtype: dict
        :raises: IndexError
        """
        results = data['results'] # Get the results from the data.
        try:
            question = choice(results) # Get a random question from the results.
        except IndexError: # If there are no results.
            print(f'{Fore.RED}>>>No questions found. Using default URL.<<<{Style.RESET_ALL}') # Print an error message.
            data = self.get_data_from_settings() # Get the default data.
            results = data['results'] # Get the results from the data.
            question = choice(results) # Get a random question from the results.
        return question # Return the question.

    def ask_question(self, question) -> None:
        """
        Ask the question.
        :param question: The question.
        :return: None
        :rtype: None
        """
        answer = "Invalid"
        print(unescape(question['question'])) # Print the question.
        correct = question['correct_answer'] # Get the correct answer.
        answers = question['incorrect_answers'] # Get the incorrect answers.
        answers.append(correct) # Add the correct answer to the incorrect answers.
        answers = list(set(answers)) # Remove duplicates.
        shuffle(answers) # Shuffle the answers.
        for i in range(len(answers)): # Loop through the answers.
            print(f'>>> {answers[i]}')
        while answer == "Invalid":
            answer = input('Answer: ') # Ask the user for their answer.
            if answer.strip() == "": # If the answer is blank.
                print("Please enter an answer.")
                answer = "Invalid"
        if answer.lower() == correct.lower(): # If the answer is correct.
            print('Correct!')
            self.score += 1 # Add to the score.
        else: # If the answer is incorrect.
            print(f'Incorrect! The correct answer was {correct}')
        self.total += 1 # Add to the total.

    def get_settings(self) -> dict:
        """
        Get the settings.
        :return: The settings.
        :rtype: dict
        """
        settings = {}
        print('\nPlease choose your settings, no answer will default to any.\n')
        for difficulty in self.difficulties: # Loop through the difficulties.
            print(f'{difficulty["parameter"]}: {difficulty["name"]}') # Print the difficulty name and parameter.
        settings['difficulty'] = input('\nChoose Difficulty: ').lower() # Get the difficulty.
        print()
        for type in self.types: # Loop through the types.
            print(f'{type["parameter"]}: {type["name"]}') # Print the type name and parameter.
        settings['type'] = input('\nChoose Type: ').lower() # Get the type.
        print()
        for category in self.categories: # Loop through the categories.
            print(f'{category["parameter"]}: {unescape(category["name"])}') # Print the category name and parameter.
        settings['category'] = input('\nChoose Category: ').lower() # Get the category.
        print()
        for diff in self.difficulties: # Loop through the difficulties.
            if diff['parameter'] == settings['difficulty']: # If the difficulty is valid.
                settings['difficulty'] = diff['parameter'] # Set the difficulty.
                break
        else: # If the difficulty is invalid.
            settings['difficulty'] = 'any' # Set the difficulty to any.
    
        for typ in self.types: # Loop through the types.
            if typ['parameter'] == settings['type']: # If the type is valid.
                settings['type'] = typ['parameter'] # Set the type.
                break
        else: # If the type is invalid.
            settings['type'] = 'any' # Set the type to any.
        
        for cat in self.categories: # Loop through the categories.
            if cat['parameter'] == settings['category']: # If the category is valid.
                settings['category'] = cat['parameter'] # Set the category.
                break 
        else: # If the category is invalid.
            settings['category'] = 'any' # Set the category to any.
        return settings
    
    def get_data_from_settings(self, difficulty='any', type='any', category='any'): 
        """
        Get the data from the settings.
        :param difficulty: The difficulty.
        :   type: The type.
        :   category: The category.
        :return: The data from the settings.
        :rtype: dict
        """
        if difficulty == 'any': # If the difficulty is any.
            difficulty = '' # Set the difficulty to empty.
        else: # If the difficulty is not any.
            difficulty = f'&difficulty={difficulty}' # Add the difficulty to the url
        if type == 'any': # If the type is any.
            type = '' # Set the type to empty.
        else: # If the type is not any.
            type = f'&type={type}' # Add the type to the url.
        if category == 'any': # If the category is any.
            category = '' # Set the category to empty.
        else: # If the category is not any.
            category = f'&category={category}' # Add the category to the url.
        url = f'https://opentdb.com/api.php?amount=10{difficulty}{type}{category}' # Create the url.
        data = self.get_data(url) # Get the data from the url.
        return data


if __name__ == "__main__": 
    """
    Run the program.
    """
    play_again = True
    print("Welcome to the Trivia Quiz!")
    trivia = Trivia()
    settings = trivia.get_settings()
    data = trivia.get_data_from_settings(settings['difficulty'], settings['type'], settings['category'])
    
    while play_again: # Loop until the user says no.
        """
        Play the game.
        """
        question = trivia.get_question(data) # Get the question.
        trivia.ask_question(question) # Ask the question.
        print(f'You got {trivia.score} out of {trivia.total} correct!')
        play_again = 'invalid' # Set play_again to invalid.
        while play_again == 'y' or play_again == 'n' or play_again == 'invalid': # Loop until the user enters a valid answer.
            play_again = input('Would you like to play again? (y/n) ') # Ask the user if they want to play again.
            match play_again.lower().split(): # Split the answer.
                case ['y'|'yes'|'true']: # If the answer is yes.
                    play_again = True
                    break
                case ['n'|'no'|'false']: # If the answer is no.
                    play_again = False
                    break
                case _: # If the answer is invalid.
                    play_again = 'invalid'
                    print('Invalid input!')