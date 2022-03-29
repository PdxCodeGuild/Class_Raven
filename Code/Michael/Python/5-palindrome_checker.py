'''
PDX Code Guild Full Stack Bootcamp
->Lab 05
  Palindrome Checker
Michael B
'''
def check_palindrome(list_of_strings)->list:
    compiled_word = ""
    compiled_list = []
    for word in list_of_strings:
        compiled_word = ''.join(reversed(word)) # Reverses the word then rejoins it to string.
        if compiled_word == word: # If words match, they're palindrome.
            is_palindrome = True
        else:
            is_palindrome = False
        compiled_list.append(tuple((word,is_palindrome))) # Create a new list to return that contains the word and if it is paldindome.
    return compiled_list

if __name__ == '__main__':
    from lab_04 import check_anagram
    from lab_04 import get_list_of_words
    valid_command = False
    word_list = get_list_of_words()
    
    while not valid_command:
        command = input("Would you like to check for Palindrome or Anagram? ").lower()
        match command.split(): 
            case ["quit"|"q"|"exit"|"quit()"]:
                valid_command = True # Could be quit() but maybe I want to do something later.
            case ["palindrome"|"pal"]:
                for word in check_palindrome(word_list):
                    if word[1] == True:
                        print(f'{word[0]} is a palindrome.')
                    else:
                        print(f'{word[0]} is not a palindrome.')
                valid_command = True
            case ["anagram"|"ana"]:
                if check_anagram(word_list):
                    print(f'{word_list} are an anagram.')
                else:
                    print(f'{word_list} are not an anagram.')
                valid_command = True
            case unknown_command:
                print (f"\nUnknown command '{unknown_command}' Please enter Palindrome or Anagram or Quit.")
                valid_command = False
                

    print("\nGoodbye. Thank you for using this program.")