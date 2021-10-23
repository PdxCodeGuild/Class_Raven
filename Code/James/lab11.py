import requests
import string


# getting data from the website

response = requests.get('https://www.gutenberg.org/cache/epub/66585/pg66585.txt')

# print(response.text)
punctuation_list = string.punctuation

list(punctuation_list).append('\n')

with  open('lab11.txt', 'w', encoding='utf-8') as book:
    book.write(response.text)

with open('lab11.txt', 'r') as book:
    text = book.read()
    text = text.replace("\n\n", '')
    for punctuation in punctuation_list:
        # print(punctuation)
        if punctuation in text:
            text = text.replace(punctuation, '')
        
    text = text.lower().strip('').split(' ')
    
print(text)
#the words are saved as a list now I need to count them.


