

#Lab 13: Count Words



import requests
from string import punctuation

response = requests.get('https://www.gutenberg.org/cache/epub/66585/pg66585.txt')
book = response.text 
book = book.translate(book.maketrans("", "", punctuation)).lower().split() # found this on stack overflow, The translate method requires a table or dictionary in order  to replace certain characters
# you can either use 2 parameters, which just replaces on thing with another, or you can use 3 which will remove everything that matches the 3rd parameter.)
# In this case we replace "" with "" which does nothing, and then removed all punctuation with string.punctuation

word_count = {}
for i in book:
    word_count[i] = 0 # this for loop is going to add each word in 'book' to the dictionary, and set it to zero. We will change that later. Also there are no duplicates since dictionarys do not allow them.

book = ''.join(book) #changing this back to a string so I can use the .count() method
for i in word_count:
  total = book.count(i) # this is setting the variable 'total' to the total amount 'i' occurs in the string 'book', then it adds that values to the dictionarys matching key value pair
  word_count[i] = total

words = list(word_count.items()) #items() will return a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True) # this is will sort by each tuple at index[1] which is the number of times it was counted. we added 'reverse=True' because that places the tuples with the highest numbers at the top.
#Other wise the lowest tuples would be at the top.
# I did use the code given in the lab however I typed it out myself. The only thing I dont understand is the lambda part.
for i in range(10):
    print(words[i])





