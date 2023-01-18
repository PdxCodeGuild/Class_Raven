'''palindrome'''
#user_input = input('Enter a word: ')
def palindrome(word):
    while True: 

        #taking user input
        user_input = input('Enter a word:\n>> ')
        #if the input is not an alphabet character we print the message and start loop over.
        if not user_input.isalpha():
            print("Please enter only letters.")
            continue
#flipping the user input backwards
        user_inputb = user_input[::-1]

#print(word.split())

#checking if the input is the same spelt backwards
        if user_input[::-1] == user_inputb:
            print(f'\n{user_input} is a palindrome.')
        elif user_input != user_inputb:
            print(f'\n{user_input} is not a palindrome.')
        
        continue_play = input('\nDo you want to keep playing y/n?: \n>>')
        if continue_play == 'y':
            continue
        elif continue_play == 'n':
            break
#calling the function
palindrome(input)


'''Anagram'''
def anagram():
    while True:   
            
        user_input = input('Enter the first word or type q to quit: ')
        if not user_input.isalpha():
            print('please enter only letters.')
            continue
        if user_input == 'q':      
            break
        user_input_list = user_input.lower().replace(' ', '')
        user_input_list = sorted(user_input)

                
        user_input2 = input('Enter the first word or type q to quit: ')
        if not user_input2.isalpha():
            print('please enter only letters.')
            continue
        if user_input2 == 'q':      
            break
        user_input2_list = user_input2.lower().replace(' ', '')
        user_input2_list = sorted(user_input)
        
        if set(user_input_list) == set(user_input2_list):
            user = ''.join(user_input)
            user2 = ''.join(user_input2)
            print(f'{user_input} and {user_input2} are anagrams!')
        elif user_input != user_input2:
            print(f'{user_input} and {user_input2} are not anagrams.')

# anagram()