def tues():
    from tuesday_labs import tuesday
    result = tuesday()
    return result


def wed():
    from wednesday_labs import wednesday
    result = wednesday()
    return result


def thurs():
    from thursday_labs import thursday
    result = thursday()
    return result


def fri():
  from friday_lab import friday
  result = friday()
  return result

def week_1():
    options = [
        {'tues': 'tuesday'},
        {'wed': 'wednesday'},
        {'thurs': 'thursday'},
        {'fri': 'friday'},
        {'q': 'quit'}
    ]
    counter = 1
    results = []
    print('\nThis app will print out all of the results of each instance after you enter \'q\'\n Unless you choose turtle... \n Then the whole chain breaks... \n do the turtles before or after... never during.')
    for option in options:
        print(option)
    selection = input(
        'Please enter the shorthand of the day you\'d like to access\n')
    while selection != 'q':
        if selection == 'tues':
            tues()
            result = 'dope greeting and/or stick figure'
        elif selection == 'wed':
            wed()
            result = 'dope coins and/or doper stick figure (ROUNDBOII)'
        elif selection == 'thurs':
            thurs()
            result = 'too many dope things, well 4... averages, card validation, palidromes, and anagrams'
        elif selection == 'fri':
            fri()
            result = 'the dopest chart'
        # print(result)
        result = f'day: {selection} output: {result}'
        results.append({counter: result})
        counter += 1
        print('\nWelcome back!')
        print(options)
        selection = input(
            'Please enter the shorthand of the day you\'d like to access\n')
    if selection == 'q':
        print('Thanks for checking out my week 1 labs! \n To recap your results were: \n ')
        for result in results:
            print(result)
    return results


week_1()
