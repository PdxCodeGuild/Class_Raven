person = {
    'first_name': 'Brad',
    'last_name': 'Doe',
    'age': 47
    }


person['fav_color'] = 'red'
person['fav_color'] = 'blue'

person['first_name'] = 'John'

person['pet_name'] = 'Rocky'

person['nickname'] = 'Flash'

nickname = person.get('nickname', False)

# if nickname:
#     print(f"{person['first_name']}'s nickname is {nickname}")
# else:
#     print(f"{person['first_name']} has no nickname")

del person['pet_name']


person['fav_operating_system'] = 'MacOS'

# if 'fav_food' in person:
#     print(f"{person['first_name']}'s favorite food is {person['fav_food']}")
# elif 'fav_operating_system' in person:
#     print(f"{person['first_name']}'s favorite OS is {person['fav_operating_system']}")

colors = ['red', 'blue', 'yellow']

# for color in colors:
#     print(color)

# for key in person:
#     if key == 'first_name':
#         print('This is a real person')



# Create a user login system, use a dictionary to store username: password
accounts = {
    'username': 'password',
    'batman': 'notbrucewayne1'
}

while True:
    choice = input('Select (1) Sign up, (2) Login, (3) Quit: ')
    if choice == '1':
        # Sign up a new user (username cannot be taken)
        username = input("Enter a username: ")
        password = input("Enter a password: ")

        if username in accounts:
            print('Username already exists...')
            continue
        else:
            accounts[username] = password
    elif choice == '2':
        # Login user
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        
        # None != 'None'
        if accounts.get(username, None) == password:
            print(f'Welcome {username}')
        else:
            print('Username or password incorrect.')
    else:
        break


new_users = {
    'llama': 'banana',
    'Bear': 'None',
    'John': 'Doe'
}

accounts.update(new_users)

print(accounts)


# This is nasty, dont look
other_types = {
    1: 'Doe',
    3.4: 'This is ok',
    'string': 'this is a string',
    'int': 4,
    'list': ['red', 'green', 'blue'],
    'dictionaries': {
        'first_name': 'something'
    }
}