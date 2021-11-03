# import requests

# # response = requests.get('https://www.gutenberg.org/cache/epub/66584/pg66584-images.html')

# # response.encoding = 'utf-8'

# # print(response.text)
# response = requests.get('https://www.gutenberg.org/cache/epub/66584/pg66584-images.html')
# with open('the_raven.txt', 'response', encoding='utf-8') as file:
#     text = file.read()
# print(text)

import requests
import string
import re   #added this because it helped with a more complex string search

booklink = 'https://www.gutenberg.org/files/5343/5343-0.txt'
def word_count(str, params = None):
    counts = dict()
    words = str.split()

    if not params:
        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
    else:
        for word in words:
            if word == params:
                if word in counts:
                    counts[word] += 1
                else:
                    counts[word] = 1
    return counts


response = requests.get(booklink)
response.encoding = 'utf-8' # set encoding to utf-8


text = re.sub(r'[^\w\s]','',response.text)
text = (re.sub(r'_','',text)).lower()

wordcount = word_count(text)
words = list(wordcount.items()) 
words.sort(key=lambda tup: tup[1], reverse=True)  
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
        print(words[i])
   