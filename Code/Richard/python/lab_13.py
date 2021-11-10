import requests
import string

print('Count Words')

punc_list = string.punctuation

response = requests.get('https://www.gutenberg.org/files/1322/1322-0.txt')
response.encoding = 'utf-8' # set encoding to utf-8
book = response.text

book = str(book)
book = book.lower()

for x in punc_list:
    if x in book:
        book = book.replace(x, "")

list_set = book.split()

# word_dict is a dictionary where the key is the word and the value is the count
word_dict = {' a ': 0, ' the ': 0, ' that ': 0, ' you ': 0, ' of ': 0, ' and ': 0, ' in ':0, ' to ': 0, ' is ':0, ' it ':0}

for word in list_set:
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1

words = list(word_dict.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])