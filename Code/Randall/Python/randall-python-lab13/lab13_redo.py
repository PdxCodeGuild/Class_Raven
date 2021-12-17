# Lab13 Count words do over
import string

with open('moby_dick.txt', 'r', encoding='utf-8') as file:
    all_words = file.read()
all_words = all_words.lower()
all_words = all_words.translate(str.maketrans('', '', string.punctuation))



print(all_words)       