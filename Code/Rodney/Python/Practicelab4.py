import string

def list_sorter(user_word):  #function that takes in user words 1 and 2 ('the paper') and is passed through the body of function ('the shredder), which
                                #creates a list from user string, sorts it, and returns that sorted list
    while True: 
        ## while True to make repeatable if user wants to try again 
        first_word = input("Please enter first word or words: > ").lower()  ## input for first and second words to compare 
        first_word = first_word.replace(" ", "") #replaces space between words with no space 

        second_word = input("Please enter second word or words: > ").lower()
        second_word = second_word.replace(" ", "")
        
        output1 = list_sorter(first_word)  #assigning variable to return value of function once user words are passed through that function 
        output2 = list_sorter(second_word)

        punctuation = string.punctuation  ## imported string module and assigned a variable to all punctuation characters 
        
        output1 = ''.join(output1)  # joining items in output1 list into a string
        output1final = output1.strip(punctuation) #removing all punctuation from that string before comparing whether or not the words are anagrams

        output2 = ''.join(output2)   # same as immediately above, just for word 2 now 
        output2final = output2.strip(punctuation)

        user_word_list = list(user_word)
        user_word_list.sort()
        return user_word_list


   
    yes_choices = ['yes', 'y', 'yep', 'yepper', 'yah']  #list of normal yes and no choices 
    no_choices = ['no', 'n', 'nope', 'nah']
    all_choices = [] # blank list that we can append the yes and no choices to...we also wanted them separate at first because we will
                        # will have if/elif statements to check if user is stating yes or no from each individual list 
    all_choices.extend(yes_choices)  ## cant' use append here, because we are adding multiple values 
    all_choices.extend(no_choices)


    if output1final == output2final:   ## if statement that will tell us words are anagrams if the sorted list of each word matches, and then ask user to play again 
        print(f'{first_word} and {second_word} are anagrams')
        again = input('Do you want to try again, yes or no? ')
        while again not in all_choices:    # is user types in random word that isn't in normal yes/no choices list (aslkfdsaflk for example), we have while loop that will keep checking 
            print(f"Choices: {', '.join(all_choices)}") ## to see if user chooses an appropriate yes/no option from the list 
            again = input("Please enter a valid selection: ")
        if again in yes_choices:  ## if they choose an option from yes list, program starts over 
            print("Sounds good, let's do it!")
            continue
        elif again in no_choices:  ## and if they choose an option from no list, program ends 
            print('See ya later alligator')
            break

    else: 
        print(f'{first_word} and {second_word} are not anagrams')   ## basically doing the same thing as the above code block, except it is initiated if the words are not an anagram 
        again = input('Do you want to try again, yes or no? ')
        while again not in all_choices:
            print(f"Choices: {', '.join(all_choices)}") 
            again = input("Please enter a valid selection: ")
        if again in yes_choices:
                print("Sounds good, let's do it!")
                continue
        elif again in no_choices:
            print('See ya later alligator')
            break
