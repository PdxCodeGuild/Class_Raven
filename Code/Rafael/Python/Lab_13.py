# Lab_17 Count Words
# Rafael Medina 

import string
import requests

# Book Title: STUDENT'S HAND-BOOK OF MUSHROOMS OF AMERICA EDIBLE AND POISONOUS by THOMAS TAYLOR, M.D., WASHINGTON, D.C. 1897 

"""
Instructions:
Take the following steps to build up our dictionary. The result should look something like {'a': 3, 'the': 4}
Make everything lowercase, strip punctuation, split into a list of words.
Your dictionary will have words as keys and counts as values. If a word isn't in your dictionary yet, add it with a count of 1. If it is, increment its count.
Print the most frequent top 10 out with their counts. 
"""

response = requests.get('https://www.gutenberg.org/cache/epub/32982/pg32982.txt') 

response.encoding = 'utf-8' # stands for "Unicode Transmission Response- 8 bits" example is "01000001" decodes as letter A and has an asciii code of 065.

#print(response) # <Response [200]> received meaning it is a communicating with their servers.

# Converts the book text into lower case before running the function.
text = response.text
text = response.text.lower() # <class 'str'>
"""
# The original intent was to find the actual starting point and ending point of the book and only word count the official book material nested within the disclaimers and Project Guttemberg information, but after continual conversion and strips the start and end became more difficult to find and use. 
start = '*** START OF THIS PROJECT GUTENBERG EBOOK MUSHROOMS ***' 
end = '*** END OF THIS PROJECT GUTENBERG EBOOK MUSHROOMS ***'
# print(text[17:344809])
# print(len(text[17:344809])) #344,792 
print(response.text.find(start)) # 547 letters
print(response.text.find(end)) # 344,809 letters
"""
# This is called string.punctuation which strips a strins of "!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~" most common keyboard special characters and puctuation. reference: "https://www.geeksforgeeks.org/string-punctuation-in-python/." and "https://docs.python.org/3/library/string.html"
text = ''.join([i for i in text if i not in string.punctuation]) # Takes the punctuation out and joins an empty string in between strings that are ignored that do not contain string.punctuation characters.  

# Split into a list of words.
text = text.split()
#print(type(text)) # List

occurence = {} # empty dict to place the occurences in key and value.
for word in text: 
   if (word in occurence): # if the word that is tallied into the .items dict{} occurence appears more than once than it is counted each loop and added to the tally each loop +=1. 
      occurence[word] += 1
   else:
      occurence[word] = 1 # Otherwise leaves the x1 found word and appends it to the .items with only the of value 1.
for key, value in occurence.items(): # This returns the list with all dictionary keys and values.

   #print(type(occurence))# Converts into a dictionary with string words as the key += occurence is tallied and displayed in the value index of the dictionary.

# Lab_13 Class Raven instructions on how to take the top 10 most occured words and print them as a tuple in seperate lines.  
   words = list(occurence.items()) # .items() returns a list of tuples
   words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])
 
# Note: By printing a larger number like 500 instead of 10 gives a more accurate of main words that are not intermediate words like "the" "of" "in" and instead guage the frequency of more topic orriented words like "gills" "spores" "edible" "poisonous" and so on.. There is a way around this by counting the words next to the intermediate words and tallying the frequency of those as well or even making an exemption list to strip most common intermediate words found in the top word count and include the rest into the count tally. 