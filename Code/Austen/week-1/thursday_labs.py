def average():
    from py import lab_averages
    average = lab_averages.version_picker()
    return average


def card_validator():
    from py import lab_card_validator
    valid = lab_card_validator.validator()
    return valid


def palindrome():
    from py import lab_palindromes
    result = lab_palindromes.check_palindrome()
    return result


def anagram():
    from py import lab_anagrams
    result = lab_anagrams.check_anagram()
    return result


def thursday():
    options = [
        {1: 'averages'},
        {2: 'card validator'},
        {3: 'palidrome checker'},
        {4: 'anagram checker'},
        {'q': 'quit'}
    ]
    counter = 1
    results = []
    for option in options:
        print(option)
    selection = input(
        'Please enter the number of the app you\'d like to run\n')
    while selection != 'q':
        if selection == '1':
            result = average()
        elif selection == '2':
            result = card_validator()
        elif selection == '3':
            result = palindrome()
        elif selection == '4':
            result = anagram()
        print(result)
        result = f'app number: {selection} output: {result}'
        results.append({counter: result})
        counter += 1
        print('\nWelcome back!')
        print(options)
        selection = input(
            'Please enter the number of the app you\'d like to run\n')
    if selection == 'q':
        print('Thanks for checking these apps out! \n To recap your results were: \n ')
        for result in results:
            print(result)
    return results
