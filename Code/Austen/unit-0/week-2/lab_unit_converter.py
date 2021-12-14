yes = ['y', 'yes', 'Yes', 'YES']
no = ['n', 'no', 'No', 'NO']
foot = {
    'feet': 1,
    'miles': 0.00018939,
    'meters': 0.3048,
    'kilometers': 0.0003048,
    'inches': 12,
    'yards': .333
}


def validator():
    print('Invalid response.')
    response = input('try again? \n (y/n) \n')
    if response in yes:
        return 'yes'
    elif response in no:
        return 'no'
    else:
        return True


def converter(unit_from, unit_to, number):
    feet = number / foot[unit_from]
    result = feet * foot[unit_to]
    return result


def version_1():
    def converter(feet):
        result = feet * foot['meters']
        return result

    query = 'Enter feet: '
    print(query)
    response = float(input())
    result = converter(response)
    conversion = f'{result} meters'
    print(conversion)


def version_2():
    def starter():
        options = ['feet', 'miles', 'meters', 'kilometers']
        query = 'What unit would you like to convert from?'
        invalid = True
        print(query)
        print(options)
        response = input()
        while response in options:
            unit_from = response
            query = f'How many {response}:'
            print(query)
            response = input()
            number = float(response)
            while float(number):
                query = 'What unit would you like to convert to?'
                print(query)
                print(options)
                response = input()
                unit_to = response
                while response in options:
                    confirmation = f'You would like to convert {number} {unit_from} to {unit_to}. \n Is that correct? \n (please enter y/n)'
                    print(confirmation)
                    confirmation = input()
                    while confirmation in yes:
                        invalid = False
                        result = converter(
                            unit_from, unit_to, number)
                        print(
                            f'{number} {unit_from} is equal to {result} {unit_to}.')
                        break
                    break
                break
            break
        if invalid == True:
            print('User canceled or invalid input, please try again.')
    starter()


def version_3():

    def starter():
        options = ['feet', 'miles', 'meters', 'kilometers', 'yards', 'inches']
        yes = ['y', 'yes', 'Yes', 'YES']
        welcome = 'Welcome to version 2.'
        query = 'What unit would you like to convert from?'
        invalid = True
        print(welcome)
        print(query)
        print(options)
        response = input()
        while response in options:
            unit_from = response
            query = f'How many {response}:'
            print(query)
            response = input()
            number = float(response)
            while float(number):
                query = 'What unit would you like to convert to?'
                print(query)
                print(options)
                response = input()
                unit_to = response
                while response in options:
                    confirmation = f'You would like to convert {number} {unit_from} to {unit_to}. \n Is that correct? \n (please enter y/n)'
                    print(confirmation)
                    confirmation = input()
                    while confirmation in yes:
                        invalid = False
                        result = converter(
                            unit_from, unit_to, number)
                        print(
                            f'{number} {unit_from} is equal to {result} {unit_to}.')

                        break
                    break
                break
            break
        if invalid == True:
            print('User canceled or invalid input, please try again.')
    starter()


def version_picker():
    versions = {'v1': 'feet to meters only',
                'v2': 'convert between feet, meters, miles, and kilometers',
                'v3': 'v2 + yards and inches'
                }
    welcome = f'Welcome to the unit converter! \n Which version would you like to run? \n {versions} \n Please enter "1", "2", "3", or "quit"'
    print(welcome)
    valid = ['1', '2', '3', 'quit', 'q']
    invalid = True
    response = input()
    while response in valid:
        invalid = False
        if response == '1':
            version_1()
            break
        elif response == '2':
            version_2()
            break
        elif response == '3':
            version_3()
            break
        else:
            break
    if invalid == True:
        invalid = validator()
        if invalid == 'yes':
            version_picker()
        elif invalid == 'no':
            print('ok bye')
        else:
            validator()


version_picker()
