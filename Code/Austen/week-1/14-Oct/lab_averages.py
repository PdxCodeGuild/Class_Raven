def v1():
    numbers = [5, 0, 8, 3, 4, 1, 6]
    total = 0
    for number in numbers:
        total += number
    average = total / len(numbers)
    average = round(average, 2)
    message = f'Your average is: {average}'
    return message


def v2():
    print('\n Average Calculator\n (enter done to see average or quit to exit.)')
    stop = ['quit', 'done']
    numbers = []
    total = 0
    response = input('Enter a number: \n')
    while response not in stop:
        try:
            number = float(response)
        except:
            print('invalid')
            response = input('Enter done, quit, or a number: \n')
        else:
            numbers.append(number)
            response = input('Enter a number: \n')
    if response == 'quit':
        print('Goodbye.')
    elif response == 'done':
        for number in numbers:
            total += number
        if total == 0:
            average = 0
        elif total > 0:
            average = total / len(numbers)
            average = round(average, 2)
        message = f'Your average is: {average}'
    return message


def version_picker():
    print('Welcome to Lab 03.')
    versions = ['v1', 'v2']
    response = input('Would you like to run v1 or v2?\n')
    if response == 'v1':
        average = v1()
        # print(average)
    elif response == 'v2':
        average = v2()
        # print(average)
    else:
        while response not in versions:
            print('Please enter \'v1\' or \'v2\'.')
            response = input('Would you like to run v1 or v2?\n')
    return average
