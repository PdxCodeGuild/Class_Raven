"""
Lee Colburn
Evening Bootcamp - PDX Code Guild
Lab 19 - Trivia API
"""

import html
from os import error
import requests
import random


def api_request(difficulty='any', type='any', category='any'):
    """Takes in question parameters and returns a list of questions"""
    category_url = "" if category == 'any' else f"&category={category}"
    type_url = "" if type == 'any' else f"&type={type}"
    difficulty_url = "" if difficulty ==  'any' else f"&difficulty={difficulty}"
    url = f"https://opentdb.com/api.php?amount=10{category_url}{difficulty_url}{type_url}"
    response = requests.request("GET", url).json()

    if response.get('response_code') != 0:
        print(f"error - response code {response['response_code']} encountered. Exiting to main menu")
        question_list = False
        return question_list
    question_list = response["results"]
    return question_list


def test(question_list):
    """Evaluates user collected information with question list and returns a score of how many questions were correct."""
    if question_list == False:
        return
    score_counter = 0
    for question in question_list:
        complete = False
        while not complete:
            generated_question = html.unescape(question.get("question"))
            generated_answer = html.unescape(question.get("correct_answer"))
            generated_incorrect_answer = html.unescape(question.get("incorrect_answers"))
            generated_type = html.unescape(question.get("type"))
            if generated_type == 'multiple':
                answer = multiple_choice(generated_question, generated_answer, generated_incorrect_answer)
            elif generated_type == 'boolean':
                answer = true_false(generated_question)

            if answer == str.lower(generated_answer):
                print(f"{answer.capitalize()} is correct!\n")
                question['user_answer'] = 'correct'
                score_counter += 1
            else:
                print(f"'{answer}' is not correct. Correct Answer: '{generated_answer}'\n")
                question['user_answer'] = 'incorrect'
            complete = True
    print(f'You scored {score_counter}/10 questions right!\n')
    return

def custom_game():
    """Returns game parameters needed for a custom trivia list."""
    # Difficulty
    print("\nChoose your difficulty: ")
    for choice in difficulties:
        parameter = choice['parameter']
        name = choice['name']
        print(f"For {name}  - Enter: {parameter}")
    difficulty = input("Enter difficulty: ")

    # Types
    print("\nChoose your game type: ")
    for choice in types:
        parameter = choice['parameter']
        name = choice['name']
        print(f"For {name}-  Enter: {parameter}")
    type = input("Enter game type: ")

    # Categories
    print("\nChoose your genre: ")
    for choice in categories:
        parameter = choice['parameter']
        name = choice['name']
        print(f"For {name} - Enter: {parameter}")
    category = input("Enter category: ")

    return difficulty, type, category

def multiple_choice(question, correct, incorrect):
    """Takes in correct and incorrect answer options to make a blinded list for user to evaluate the question. Returns user answer"""
    blinded_list = [correct]
    blinded_list.extend(incorrect)
    random.shuffle(blinded_list)
    html.unescape(blinded_list)
    print(f"{question}")
    print(*blinded_list, sep=', ')
    answer = input('\nAnswer: ')
    return str.lower(answer)

def true_false(question):
    """Presents question to user and returns a formatted user response"""
    print(f"{question}")
    answer = input(' Answer True or False: ')
    return str.lower(answer)



difficulties = [
    { 'parameter': 'any', 'name': 'Any Difficulty'},
    { 'parameter': 'easy', 'name': 'Easy' },
    { 'parameter': 'medium', 'name': 'Medium' },
    { 'parameter': 'hard', 'name': 'Hard' }
]

types = [
    { 'parameter': 'any', 'name': 'Any Type'},
    { 'parameter': 'multiple', 'name': 'Multiple Choice' },
    { 'parameter': 'boolean', 'name': 'True / False' }
]

categories = [
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

while True:
    select = input(f"Welcome to the trivia engine. Press '1' to start playing '2' to customize your game options, or '3' to exit:")
    if select == "1":
        question_list = api_request()
        test(question_list)
        continue
    if select == "2":
        difficulty, type, category = custom_game()
        question_list = api_request(difficulty, type, category)
        test(question_list)
        continue
    if select == '3':
        break
    else:
        print("Command not recognized. ")
        continue