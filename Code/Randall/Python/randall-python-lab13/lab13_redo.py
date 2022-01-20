# Lab13 Count words do over
import string
from collections import Counter

with open('moby_dick.txt', 'r', encoding='utf-8') as file:
    all_words = file.read()
all_words = all_words.lower()
all_words = all_words.translate(str.maketrans('', '', string.punctuation))

split_it = all_words.split()
Counter = Counter(split_it)
most_occur = Counter.most_common(10)
  
print(most_occur)



"""
word_dict = {split_it}
words = list(word_dict.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])
"""