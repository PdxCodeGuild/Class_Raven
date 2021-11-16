# Programming 102 Lab 2
# * 2.1 Write sum() from scratch
def sum(numbers):
    total = 0
    for number in numbers:
        if len(numbers) > 0:
            total += number
    return total
# * 2.2 Use a REPL to build a list of numbers


def collector():
    import string
    print('Please enter the number to be added:')
    print('(enter \'done\' to see total or \'cancel\' to exit)')
    valid = ['done', 'cancel']
    integers = string.digits
    response = input()
    if response in valid:
        response = response
    elif response in integers:
        response = float(response)
    else:
        response = 'invalid'
    return response


numbers = []
response = collector()
message = 'Invalid response.'
while response != 'invalid':
    if response == 'cancel':
        message = 'ok bye'
        break
    elif response == 'done':
        total = sum(numbers)
        message = f'Your total is: {total}'
        break
    elif response == 0:
        print('Empty entry has been ignored.')
        response = collector()
    elif float(response):
        numbers.append(response)
        message = f'{response} has been added to list.'
        print(f'Your current list: {numbers}')
        print('')
        response = collector()


print(message)
