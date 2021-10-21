# Palindrome
# Write a function check_palindrome which takes a string, and returns True if the string's a palindrome, or False if it's not.


def check_palindrome():
    string = input("I can check for palindromes. Give me a word: ")
    back_string = string [::-1]
 
    if string == back_string:
        print(f'{string} is a palindrome!')
        return True
    else:
        print(f'{string} is not a palindrome.')
        return False

check_palindrome()


#Anagram

def check_anagram():

    print("Let's check words to see if they are anagrams.")
    first_word = input("\nPlease give me a word: " )
    first_word = first_word.lower()
    first_word = first_word.replace(" ", "")
    print(first_word)
    first_word = sorted(first_word)
    print(first_word)
    second_word = input("\nNow give me a word that may be an anagram of your first word: ")
    second_word = second_word.lower()
    second_word = second_word.replace(" ", "")
    second_word = sorted(second_word)
    print(second_word)

    if first_word == second_word:
        print('Your words are anagrams!')
        return True
    else:
        print("Your words are not anagrams")
        return False

check_anagram()
