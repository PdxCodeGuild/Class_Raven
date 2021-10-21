#Lab 5: Palindrome
'''
word = input("Please enter a word: ")

if(word == word[:: - 1]):
   print("The word entered is a Palindrome")
else:
   print("This word entered is not a Palindrome")
'''

#Anagram

word1 = input("Enter a word: ")
word2 = input("Enter the second word: ")
def check(word1, word2):
       
    if(sorted(word1)== sorted(word2)):
        print("These are anagrams.")
    else:
        print("The aren't anagrams.")        
         
check(word1, word2)