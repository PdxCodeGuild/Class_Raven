def intro():
    from py import git_intro
    result = git_intro.hello()
    return result


def turtle():
    from py import lab_turtle
    result = lab_turtle.turtle_v1()
    return result


def tuesday():
    options = ['hello', 'turtle']
    response = input('hello or turtle? \n')
    while response not in options:
        print('Enter \'hello\' or \'turtle\':\n')
        response = input()
    if response == 'hello':
        result = intro()
    elif response == 'turtle':
        turtle()
    return result
