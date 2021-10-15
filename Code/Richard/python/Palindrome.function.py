import string

punc = string.punctuation
#print(punc)

punc_list = list(punc)
word = ""

print("Palindrome Checker")

def check_palindrome(word_1):
    word = word_1
    word = word.lower()

    while (" ") in word:
        word = word.replace(" ", "")

    for x in punc_list:
        if x in word:
            word = word.replace(x, "")

    word_list = list(word)

    word_list.reverse()

    reverse_1 = ''.join(word_list)

    if word == reverse_1:
        return print(f"{word_1} is a palindrome.")
    else:
        return print(f"{word_1} is not a palindrome.")

word = input("enter word:\n>")
check_palindrome(word)
