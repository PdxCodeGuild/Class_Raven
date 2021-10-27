# Lab 05: Palindrome and Anagram
# Palindrome

user_input = input('\nenter a word ').lower()

if list(user_input) == list(reversed(user_input)): # compares the default list to a reversed list if eaqual it is a palindrome.
    print(user_input, 'is a Palindrome')
else:
    print(user_input, 'is not a Palindrome')



# Lab 05: Palindrome and Anagram
# Anagram

"""
user_input1= list(input(f"\nenter the first word: ").lower())
user_input2 = list(input(f"\nenter the second word: ").lower())

user_input2.sort()
user_input1.sort()

if len(user_input1) == len(user_input2):
    
    if user_input1 == user_input2:
        #print(f"'{user_input1}' and '{user_input2}' are anagrams")
        print ("'",''"".join(user_input1),"'", "and", "'",''"".join(user_input2),"'", "are", "anagrams")    
    
    elif user_input1 != user_input2:
        
        print ("'",''"".join(user_input1),"'", "and", "'",''"".join(user_input2),"'", "are", "not", "anagrams")   
  
else: 
        #print(f"'{user_input1}' and '{user_input2}' are not anagrams")
        print ("'",''"".join(user_input1),"'", "and", "'",''"".join(user_input2),"'", "are", "not", "anagrams")

# I still need to figure out how to print the original user input1 & 2, instead of printing the sorted version from original output. Note: ask Sarah or a student for tips.

"""




