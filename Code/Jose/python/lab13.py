import string

with open('github\Class_Raven\Code\Jose\python/the_raven.txt', 'r', encoding='utf-8') as file:
    text = file.read()
text = text.translate(str.maketrans('', '', string.punctuation))    # Translating the book to remove any punctuation.
text = text.lower()
list_of_text = text.split()
dict_of_words = {}

for word in list_of_text:
    dict_of_words[word] = list_of_text.count(word)    # Word goes to the keys and the return of counts goes to values.

words = list(dict_of_words.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])

# The code block to return the top 10 words was taken from the lab. Not my work!