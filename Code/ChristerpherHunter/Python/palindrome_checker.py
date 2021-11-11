# Christerpher Hunter
# Lab 05... again: Palindrome and Anagram checker

from colorama import Fore as F

R = F.RESET


def check_palindrome() -> bool:
    """Take in a string and return T or F; Palindrome"""

    user_input = input("\nPlease enter a word: ").lower().replace(" ", "")

    rev_word = str()
    for i in reversed(user_input):
        rev_word += i

    if rev_word == user_input:
        return True
    else:
        return False


def check_anagram():
    """Check if two input are Anagrams of each other"""

    user_word1 = input("\nPlease enter the first word: ")\
        .lower().replace(" ", "")
    user_word2 = input("Please enter the second word: ")\
        .lower().replace(" ", "")

    word1 = list()
    word2 = list()
    for i in user_word1:
        word1.append(i)
    for j in user_word2:
        word2.append(j)

    word1.sort()
    word2.sort()

    if word1 == word2:
        return True
    else:
        return False


def main() -> None:

    yay_or_nay = check_palindrome()

    print(f"\nPalindrome {F.YELLOW}{yay_or_nay}{R}")

    yay_or_nay_again = check_anagram()

    print(f"\nAnagram {F.YELLOW}{yay_or_nay_again}{R}")


if __name__ == "__main__":
    main()
