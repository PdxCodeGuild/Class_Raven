# Christerpher Hunter
# Lab 05... again: Palindrome and Anagram checker

from colorama import Fore as F

R = F.RESET

def check_palindrome() -> bool:
    """Take in a string and return T or F; Palindrome"""

    user_input = input("Please enter a word: ")

    rev_word = str()
    for i in reversed(user_input):
        rev_word += i
    if rev_word == user_input:
        return True
    else:
        return False    

def check_anagram():
    """Check if two input are Anagrams of each other"""

    pass
    

def main() -> None:

    yay_or_nay = check_palindrome()

    print(f"\nPalindrome {F.YELLOW}{yay_or_nay}{R}")

if __name__ == "__main__":
    main()

