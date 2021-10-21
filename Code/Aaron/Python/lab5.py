# def palindrome(string):
#     if(len(string) == 0):
#         return string
#     else:
#         return palindrome(string[1:]) + string[0]

# string1 = input("enter a word: ")
# string = palindrome(string1)
# # print(string1 + "is not a plalindrome")

# if(string1 == string):
#     print(string1 + " is a palindrome")
# else:
#     print(string1 + " is not a palindrome")


#I have been trying to make all this work together and I just looked at the solotion and its separate functions

#I wanted to see how the program worked so I used the solution from the github. im currently going work on the 

def check_anagram(word):
    word = word.lower()
    word = word.replace(' ', '')
    word = str(sorted(word))
    return word

anagram_ = input('what the 1st word?: ')
anagram1 = input('what is the 2nd word?: ') 
print('anagram_: '+anagram_)
print('anagram1: '+anagram1)
if check_anagram(anagram_) == check_anagram(anagram1):
    print(anagram_ + ' and ' + anagram1 + ' is a anagram' )
else:
    print(anagram_  + ' and ' +  anagram1 +  ' are not a anagram')