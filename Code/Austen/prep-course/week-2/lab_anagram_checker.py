title = 'anagram checker'.title()
description = ''
author = 'austen c. myers'.title()
created = [10, 7, 2021]
valid = {'y', 'yes', 'n', 'no'}
affirmations = {'y', 'yes'}
messages = {
    'welcome': f'\nWelcome to the {title}!',
    'invalid': 5 * '\n Invalid response.',
    'goodbye': f'Thank you for using {title}! \n copyright {created[2]} {author} \n',
    'false': '\n These words are not anagrams. \n',
    'true': '\n These words are anagrams! \n',
}
queries = {
    'initialize': 'Would you like to begin?',
    'confirmation': 'Please enter yes or no: \n',
}


def validator(response):
    if response in valid:
        return True
    else:
        return False


def welcome():
    print(messages['welcome'])
    print(queries['initialize'])
    response = input(queries['confirmation']).lower()
    valid = validator(response)
    while not valid:
        print(messages['invalid'])
        welcome()
        break
    while valid:
        if response in affirmations:
            application()
            break
        else:
            print(messages['goodbye'])
            break


def application():
    def prompt(string):
        query = f'\nEnter the {string} word: '
        response = input(f'{query}')
        return response.lower()

    def string_validator(string):
        while string.isalpha() == False:
            print('Please only use characters of the alphabet.')
            string = prompt()
        return string

    def anagram_validator(string_1, string_2):
        while string_1 == string_2:
            print('The second word should not be identical to the first.')
            string_2 = prompt()
        while len(string_1) != len(string_2):
            print('Anagrams should be the same length.')
            string_2 = prompt()
        return string_2

    def final_validator(string_1, string_2):
        string_1 = string_validator(string_1)
        string_2 = string_validator(string_2)
        string_2 = anagram_validator(string_1, string_2)
        return True
    string_1 = prompt('first')
    string_1 = string_validator(string_1)
    string_2 = prompt('second')
    string_2 = string_validator(string_2)
    string_2 = anagram_validator(string_1, string_2)
    valid = final_validator(string_1, string_2)
    if valid:
        print(f'\n Your words are {string_1} and {string_2}. \n')
        list_1 = list(string_1)
        list_1.sort()
        list_2 = list(string_2)
        list_2.sort()
        if list_1 == list_2:
            print(messages['true'])
        elif list_1 != list_2:
            print(messages['false'])
        else:
            print(messages['invalid'])
        print(messages['goodbye'])


welcome()
