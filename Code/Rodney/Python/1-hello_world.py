
profile1 = {
"username": 'mike2000',
"password": 'a12345!'
}
profile2 = {
"username": 'earl4pres',
"password": 'b1234@'
}
profile3 = {
"username": 'iheartMusic',
"password": 'c123#'
}
profile4 = {
"username": 'code_noob',
"password": 'd12$'
}
profile5 = {
"username": 'pythonISlife',
"password": 'e1%'
}

profile_list = [profile1, profile2, profile3, profile4, profile5]
      
def user_exists(user_name, profile):
    for profiles in profile:
        for value in profiles.items(): 
            if user_name in value: 
                exists = True
                return exists
        for value in profiles.items(): 
            if user_name not in value: 
                exists = False
    return exists 
 
def login(user_name, password_attempt, profile):
    if user_name == profile["username"] and password_attempt == profile["password"]:
            allow_access = True
            return allow_access
    if user_name != profile["username"] or password_attempt != profile["password"]:
            allow_access = False
            return allow_access         

def create_user(user_name, new_password): 

    while True:

        user_name = input("\nPlease enter your new username:\n> ")
        exists_tf = user_exists(user_name, profile_list)  
        if exists_tf == True:
            print("\nThat username already exists!")
            continue

        if exists_tf == False:
            new_password = input("\nWhat would you like your password to be? ")
            new_profile = {"username": user_name, "password": new_password}
            profile_list.append(new_profile)
            print(f"\nThanks for signing up {user_name}!")
            break

login_counter = 0

login_options = ['1', '2']

login_yn = input('''
Please select from the following options:

1. Create user
2. Login

Enter the number of your choice: ''')

while login_yn not in login_options:
    login_yn = input("Invalid option, please enter 1 or 2: ")  
  
if login_yn == '1':
    user_name = ''
    new_password = ''
    create_user(user_name, new_password)
    

elif login_yn == '2':
    while True: 
        user_name = input("\nPlease provide your username: \n> ")

        password_attempt = input("Please provide your password: \n> ")

        for profiles in profile_list:
            output = login(user_name, password_attempt, profiles)
            if output == True:
                break

                        
        yes_choices = ['yes', 'y', 'yep', 'yepper', 'yah']   
        no_choices = ['no', 'n', 'nope', 'nah']
        all_choices = [] 
                                    
        all_choices.extend(yes_choices)   
        all_choices.extend(no_choices)

        if output == True:
            print(f'Welcome {user_name}!')
            break
  
        if output == False: 
            login_counter += 1
            if login_counter > 2:
                print("You have had 3 unsuccessful login attempts. You shall not pass!")
                break
            attempts_remaining = 3 - login_counter
            print(f"Incorrect username/password combination, number of attempts remaining: {attempts_remaining}")
            again = input('Would you like to try again, yes or no?: ').lower()
            while again not in all_choices:   
                again = input("Please enter a valid selection: ").lower()
            if again in yes_choices:  
                continue
            elif again in no_choices:  
                break

                    
# practice