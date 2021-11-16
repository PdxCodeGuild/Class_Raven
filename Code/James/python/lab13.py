import requests
import string


# getting data from the website

response = requests.get('https://www.gutenberg.org/cache/epub/66585/pg66585.txt')
word_dict = {}

punctuation_list = string.punctuation

list(punctuation_list).append('\n')

with  open('lab11.txt', 'w', encoding='utf-8') as book:
    book.write(response.text)

with open('lab11.txt', 'r') as book:
    text = book.read()
    text = text.replace("\n\n", ' ')
    for punctuation in punctuation_list:
        # print(punctuation)
        if punctuation in text:
            text = text.replace(punctuation, '')
        
    text = text.lower().split(' ')
    

# words will be keys and counts will be values. if word isnt in dictionary add it with a count of 1 if it is, increment its count.

for word in text:
    if word not in word_dict and word != '':
        word_dict.update({word: 1})
    elif word != '':
        word_dict[word] += 1
    

words = list(word_dict.items()) # list of tuples
words.sort(key=lambda tup: tup[1], reverse=True) # sort largest to smallest.
for i in range(min(10, len(words))): # print the top ten words
    print(words[i])





