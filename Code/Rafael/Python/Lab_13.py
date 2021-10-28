# Lab_13.py Count Words
# Rafael Medina 


"""
NOTE: Still in progress
10/28/2021


"""

import requests
# from string import punctuation and regex makes it easier to assign punctuation to be removed, but I am going to do it with a for loop manually.
#from collections import Counter
# Supposedly using the conter instead of a for loop is meant to be faster, I will use a for loop to get more comfortable with looping. 


# Book Title: STUDENT'S HAND-BOOK OF MUSHROOMS OF AMERICA EDIBLE AND POISONOUS by THOMAS TAYLOR, M.D., WASHINGTON, D.C. 1897 


response = requests.get('https://www.gutenberg.org/cache/epub/32982/pg32982.txt')
response.encoding = 'utf-8' # set encoding to utf-8



# Setting a start and end in order to not include the header info and the footer info outside the book.
start = '*** START OF THIS PROJECT GUTENBERG EBOOK MUSHROOMS ***'
end = '*** END OF THIS PROJECT GUTENBERG EBOOK MUSHROOMS ***'

# The dictionary has keys and values to represent the occurence of a particular word and its instances in the book.


text = ''
# Convert the book text into lower case before running the function
text = response.text.lower()
# For loop to remove punctuation from text '' 

punct__and_special = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''


# empty string to replace the punctuation and special characters
empty_punct__and_special = ""


#Split the text before removing punctuation and special characters


text = text.split()
test = str()
with open(text) as f:

    # skip the header bit
    for line in f:
        if start in line:
            break
    else:
        print("end of file reached without seeing the start text")
        
    # count the words - finish when we get to the end line
    count = 0
    for line in f:
        if end in line:
            break
        count += len(line.strip().split())
    else:
        print("end of file reached without seeing the end text")

print(count, 'words')



# words will be stored in a dictionary {}
word_count = {}

#print(text)



    
"""

def count_words(text):
    # For loop to designate where to start the text
        for start_end in response.text:
            if start in start_end:
                break
            else: 
                print("Text beginning not found")
                break
    print(response.text)

    """    