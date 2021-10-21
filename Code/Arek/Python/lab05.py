"""

Lab 5: Palindrome and Anagram

Let's write a palindrome and anagram checker.
Palindrome

A palindrome is a word that's the same forwards or backwards, e.g. racecar. Another way to think of it is as a word that's equal to its own reverse.

Write a function check_palindrome which takes a string, and returns True if the string's a palindrome, or False if it's not.

>>> enter a word: racecar
>>> 'racecar' is a palindrome

>>> enter a word: palindrome
>>> 'palindrome' is not a palindrome

Anagram

Two words are anagrams of eachother if the letters of one can be rearranged to fit the other. e.g. anagram and nag a ram.

Write another function check_anagram that takes two strings as parameters and returns True if they're anagrams of eachother, False if they're not. 
The procedure for comparing the two strings is as follow:

    Convert each word to lower case (lower)
    Remove all the spaces from each word (replace)
    Sort the letters of each word (sorted)
    Check if the two are equal

>>> enter the first word: anagram
>>> enter the second word: nag a ram
>>> 'anagram' and 'nag a ram' are anagrams


"""
#Palindrome
"""def check_palindrome(random_string):
    normal = list(random_string)
    check = list(random_string)
    check.reverse()

    if check == normal:
        return True
    else:
        return False

random_string = input("Please enter a word: ")
if check_palindrome(random_string):
    print("The word is a palindrome")
else:
    print("The Word is not a palindrome")"""

#Anagram

def check_anagram(string1, string2):
    string1.sort()
    string2.sort()

    if string1 == string2:
        return True
    else:
        return False
        

string1 = list(input("Please enter a word: ").lower().replace(" ", ""))
string2 = list(input("Please enter a second word: ").lower().replace(" ", ""))

if check_anagram(string1, string2):
    print("The words are anagrams")
else:
    print("The words are not anagrams")