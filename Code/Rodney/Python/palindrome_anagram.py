from string import punctuation  # importing just punctuation from string module 

def check_palindrome(check_word):  
    #This function will take user word and check whether that word is a palindrome
    check_word = check_word.lower()  ## next couple of lines to make word lower case, remove spaces, remove punctuation, prior to checking word 
    check_word = check_word.replace(" ", "")
    check_word = check_word.strip(punctuation)
    if check_word == check_word [::-1]:  # the [::-1] reverses order of characters in string, which we need to do to check for palindrome 
        print(f'{palindrome_word.strip(punctuation)} is a palindrome!')  ##if/elif statement, printing outcome based on whether or not word is palindrome 
    elif check_word != check_word [::-1]:
        print(f'{palindrome_word.strip(punctuation)} is not a palindrome!')

def check_anagram(user_word1, user_word2):  
 #function that takes in user words 1 and 2 ('the paper') and is passed through the body of function ('the shredder), which creates a list from user string, sorts it, and checks to see if they are anagrams
    user_word1 = user_word1.replace(" ", "")  ##next lines of code replaces spaces, turns into a list, sorts, turns back into string, strips punct, and then checks to see if they are anagrams
    user_word2 = user_word2.replace(" ", "")
    user_word1 = list(user_word1)
    user_word2 = list(user_word2)
    user_word1.sort()
    user_word2.sort()
    user_word1 = ''.join(user_word1)
    user_word2 = ''.join(user_word2)
    user_word1 = user_word1.strip(punctuation)
    user_word2 = user_word2.strip(punctuation)
    if user_word1 == user_word2:
        print(f'{user_word1} and {user_word2} are anagrams!') #if/elif, compares two words, prints whether or not they are anagrams 
    elif user_word1 != user_word2:
        print(f'{user_word1} and {user_word2} are not anagrams!')

yes_choices = ['yes', 'y', 'yep', 'yepper', 'yah']  #list of normal yes and no choices 
no_choices = ['no', 'n', 'nope', 'nah']
all_choices = ['no', 'n', 'nope', 'nah','yes', 'y', 'yep', 'yepper', 'yah'] #we also wanted them separate at first because we will
                        # will have if/elif statements to check if user is stating yes or no from each individual list 

while True: # making the checker repeatable 
    pal_or_anag = input('''  
Wecome to the Anagram and Palindrome checker!

1.) Palindrome

2.) Anagram

Please type '1' for Palindrome or '2' for Anagram: ''')

    while pal_or_anag != '1' and pal_or_anag != '2':  # if user enters neither 1 or 2, while loop asking for valid input 
        pal_or_anag = input("\nInvalid response. Please type '1' for Palindrome or '2' for Anagram\n> ")
    
    if pal_or_anag == '1':  # if user selects one, take word with input function, then feed word through palindrome checker function 
        palindrome_word = input("\nPlease enter a word:\n> ")
        check_palindrome(palindrome_word)
        try_again = input("Would you like to start over?\n> ")
        while try_again not in all_choices:    # is user types in random word that isn't in normal yes/no choices list (aslkfdsaflk for example), we have while loop that will keep checking 
            print(f"Choices: {', '.join(all_choices)}") ## to see if user chooses an appropriate yes/no option from the list 
            try_again = input("Please enter a valid selection: ")
        if try_again in yes_choices:  ## if they choose an option from yes list, program starts over 
            print("Sounds good, let's do it!")
            continue
        elif try_again in no_choices:  ## and if they choose an option from no list, program ends 
            print('Thanks for playing!')
            break
        
    elif pal_or_anag == '2':   # if user selects two, takes two words with input function, then feed word through anagram checker function 
        anagram_word1 = input('Please enter your first word: ')
        anagram_word2 = input('Please enter your second word: ')
        check_anagram(anagram_word1, anagram_word2)
        try_again = input("Would you like to start over?\n> ")
        while try_again not in all_choices:    # is user types in random word that isn't in normal yes/no choices list (aslkfdsaflk for example), we have while loop that will keep checking 
            print(f"Choices: {', '.join(all_choices)}") ## to see if user chooses an appropriate yes/no option from the list 
            try_again = input("Please enter a valid selection: ")
        if try_again in yes_choices:  ## if they choose an option from yes list, program starts over 
            print("Sounds good, let's do it!")
            continue
        elif try_again in no_choices:  ## and if they choose an option from no list, program ends 
            print('Thanks for playing!')
            break

