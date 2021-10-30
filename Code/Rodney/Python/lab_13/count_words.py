import requests
from string import punctuation


response = requests.get('https://www.gutenberg.org/cache/epub/66588/pg66588.txt', params={'format': 'json'})
## requesting all the plain text from above url 
text = '' # setting text = to blank string

with open('pet_book.txt', 'w') as file:# open the empty text file i created called pet_book
    text = response.text #assigning the text from the book to the empty text string i created
    text = text.lower() ## turning all characters in that string to lower case
    for character in text:
        if character in punctuation:
            text = text.replace(character, '')  #for loop to remove all punctuation from that string 
    file.write(text) ## writing that text onto the text file i created 
  

with open('pet_book.txt', 'r') as file: ## i wasn't able to split that string into list while opening as 'w'
    text = text.split()  #but i was allowed to split into list with .split() when opening file as 'r' 


new_dict = {}  # creating empty dictionary
used_words = [] #creating empty word list 
for word in text:
    if word in new_dict and word in used_words: ## looping through words and if word is already in new_dict and used_words, adding 1 to value 
        new_dict[word] += 1
        continue ## continuing to next word in list 
    new_dict[word] = 1 ## if word isn't in used_words list, then I assign it to dictinary with key of word and value of 1 
    used_words.append(word) #appending that word to used words list 


words = list(new_dict.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])


