def check_palindrome(palindrome_word):
    if palindrome_word == palindrome_word[::-1]:
        return True
    else:
        return False

def check_anagram(first_string, second_string):
    first_string = first_string.lower()
    second_string = second_string.lower()
    first_string = first_string.replace(" ", "")
    second_string = second_string.replace(" ", "")
    first_string = sorted(first_string)
    second_string = sorted(second_string)
    if first_string == second_string:
        return True
    else:
        return False


palindrome_word = input("enter a word to be checked if it's a palindrome of itself: \n")
if check_palindrome(palindrome_word) == True:
    print(f"'{palindrome_word}' is an palindrome. \n")
else:
    print(f"'{palindrome_word}' is not a palindrome. \n")


first_string = input("enter the first word: ")
second_string = input("enter the second word: ")

if check_anagram(first_string, second_string) == True:
    print(f"\n'{first_string}' and '{second_string}' are anagrams. ")
else:
    print(f"\n'{first_string}' and '{second_string}' are not anagrams. ")

