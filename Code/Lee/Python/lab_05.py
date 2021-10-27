"""
Lee Colburn
Evening Bootcamp - PDX Code Guild
Lab 5
"""


# PALINDROME
def check_palindrome(first_string):
    #convert to lowercase remove spaces
    first_string = first_string.lower()
    first_string = first_string.replace(" ", "")
    
    # Reverse string to evaluate. IF the string is the same forwards and backwards... it's a palindrome
    string_reversed = first_string[::-1]
    
    # show the check of both strings
    print(f"\nPalindrome Analysis:\n string: {first_string} \n string reversed: {string_reversed}")
    if string_reversed == first_string:
       print(f"\n YES - '{first_string}' is a palindrome. \nExiting to main menu:")
       return complete == True
    else:
        print(f"\n NEGATIVE - '{first_string}' is not a palindrome. \nExiting to main menu:")
        return 


# ANAGRAM
def check_anagram(first_string, second_string):
    
    is_anagram = False

    #convert to lowercase remove spaces
    first_string = first_string.lower()
    first_string = first_string.replace(" ", "")
    second_string = second_string.lower()
    second_string = second_string.replace(" ", "")
    
    # convert to list
    first_list = list(first_string)
    second_list = list(second_string)

    # Sort the letters of each list
    first_list.sort()
    second_list.sort()
    
    # show the check of both strings
    print(f"\nAnagram Analysis:\n ordered first string: {first_list} \n ordered second string: {second_list}")
        
    # Check if the two lists are equal
    if first_list == second_list:
        print("\n YES - Words are anagrams. \nExiting to main menu:")
        return complete == True
        
    else:
        print("\n NEGATIVE - Words are not anagrams. \nExiting to main menu:")
        return 


complete = False
while not complete:
  # Select Option 1-Palindrome, 2-Anagram, 3-Exit, 4+ Try Again
  start = int(input(f'\nPlease select from the following options:\n 1. Check for Palindrome \n 2. Check for Anagram\n 3. Exit Program \n\n Enter the number of your choice: \n'))

  # Allow user to escape
  if start == 3:
    print(f"\nClosing application.\n")
    complete = True
    break

  if start > 3:
    print(f'\n Try again:\n')
    continue
  
  # Direct user to appropriate function: 1-Palindrome, 2-Anagram, 3-Exit, 4+ Try Again
  if start == 1:
    first_string = input("\nPlease enter the the string to check: ")
    check_palindrome(first_string)

  if start == 2:
    first_string = input("\nPlease enter the the first string to check: ")
    second_string = input("\nEnter the second string to check: ")
    check_anagram(first_string, second_string)

