def palindrome(string):
    if(len(string) == 0):
        return string
    else:
        return palindrome(string[1:]) + string[0]

string1 = input("enter a word: ")
string = palindrome(string1)
# print(string1 + "is not a plalindrome")

if(string1 == string):
    print(string1 + " is a palindrome")
else:
    print(string1 + " is not a palindrome")


#I have been trying to make all this work together and I just looked at the solotion and its separate functions

#I wanted to see how the program worked so I used the solution from the github. im currently going work on the 

def check_anagram(string_1, string_2):
    
    # look at the words entered
    print(string_1, string_2)
    
    # convert each word to lower case
    word_1 = string_1.lower()
    word_2 = string_2.lower()
    
    # look at the words after they've been converted to lower case
    print(word_1, word_2)
    
    # remove any spaces from strings
    word_1 = word_1.replace(" ", "")
    word_2 = word_2.replace(" ", "")
    
    # sort the letters in each word
    # code used from here: https://stackoverflow.com/questions/15046242/how-to-sort-the-letters-in-a-string-alphabetically-in-python
    word_1_sorted = ''.join(sorted(word_1))
    word_2_sorted = ''.join(sorted(word_2))
    
    # look at the words after spaces are removed
    print(word_1_sorted, word_2_sorted)
    
    # check if the two strings are anagrams
    if word_1_sorted == word_2_sorted:
        print(f"'{string_1}' and '{string_2}' are anagrams")
    else:
        print(f"'{string_1}' and '{string_2}' are not anagrams")
    

string_1 = input("enter the first word:")
string_2 = input("enter the second word:")
check_anagram(string_1, string_2)

# some cases to check function
#print(check_anagram("wo rd1", "W ORD2"))
#print(check_anagram("hellow", "WOLLEH"))