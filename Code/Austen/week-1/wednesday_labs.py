def make_change():
    from py import lab_make_change
    result = lab_make_change.changer()
    return result


def turtle_v2():
    from py import lab_turtle_v2
    result = lab_turtle_v2.stickfigure()
    return result


def wednesday():
    options = ['change', 'turtle']
    response = input('change or turtle? \n')
    while response not in options:
        print('Enter \'change\' or \'turtle\':\n')
        response = input()
    if response == 'change':
        result = make_change()

    elif response == 'turtle':
        turtle_v2()

    return result
