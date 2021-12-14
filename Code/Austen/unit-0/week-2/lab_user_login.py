profiles = [
    {'username': 'admin',
     'password': '123'},
    {'username': 'user',
     'password': '1234'}
]


def validate(username, password, profiles):
    for profile in profiles:
        if username == profile['username']:
            valid_username = True
        elif username != profile['username']:
            valid_username = False
        if password == profile['password']:
            valid_password = True
        elif password != profile['password']:
            valid_password = False
        if valid_password and valid_username == True:
            valid = True
            break
        else:
            valid = False
    return valid


def create_user():
    username = input('desired username: ').lower()
    for profile in profiles:
        while username == profile['username']:
            print('Username not unique, please try again.')
            username = input('desired username: ').lower()
    password = input('enter a strong password: ')
    profile = {'username': username, 'password': password}
    return profile


def login():
    username = input('username: ').lower()
    password = input('password: ')
    valid = validate(username, password, profiles)
    counter = 3
    if valid:
        username = username.capitalize()
        print(f'Welcome: {username}.')
    while not valid:
        counter -= 1
        print('Invalid username or password.')
        if counter > 0:
            print(f'You have {counter} login attempts remaining.')
            response = input(
                '\nTry again with the same username?\n Please enter y/n:\n')
            if response == 'n':
                print('Goodbye.')
                break
            elif response == 'y':
                password = input('password: ')
                valid = validate(username, password, profiles)
                if valid:
                    username = username.capitalize()
                    print(f'Welcome: {username}.')
                    break
            else:
                print('invalid input')
                break
        elif counter == 0:
            print('too many attempts')
            break


def portal():
    response = input(
        'Are you a new or existing user? \n (please enter \'new\' or \'login\')\n')
    if response == 'new':
        new_profile = create_user()
        profiles.append(new_profile)
        print('\nNow please login with the profile you just created\n')
        login()
    elif response == 'login':
        login()
    else:
        print('Invalid response please try again and enter \'new\' or \'login\'')
        portal()


portal()
