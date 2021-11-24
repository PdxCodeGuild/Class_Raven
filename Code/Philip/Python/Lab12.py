'''Count Words Lab 13
By Philip Bartoo
PDX Code Guild
'''
import requests
response = requests.get('https://www.gutenberg.org/files/98/98-0.txt')
response.encoding='utf-8'
#print(response.text)

#open a file in read mode specifying the encoding via
# a with statement in the event it throws an IO error when opening
with open('a_tale_of_two_cities.txt', 'r', encoding='utf-8') as file: 
#read the contents all at once
    text = file.read() 
    #print(type(text))
#Turn 'text' into lowercase to better compare all words
text = text.lower()
text = text.strip('.!,')
#Build a List with each word as an item from the 'text' string using .split
text = text.split()
#Create a dictionary to store the counted words
word_dict = {}
#Build a function that takes the 'text' list as an input
def word_counter(text):
#For loop through each word in the 'text' list
    for word in text:
#If the function finds the word in the dictionary key posiiton, increment the value by 1
        if word in word_dict:
            word_dict[word] += 1
#If the function didn't find the word in the dictionary key, it adds the word with a value of 1
        else:
            word_dict[word] = 1
    return(word_dict)
#Call the function with the 'text' and return the dictionary variable
counted_words = word_counter(text)
#Creates a list of tuples in the words variable
words = list(counted_words.items())
#Sorts the tuples in reverse value order
words.sort(key=lambda tup: tup[1], reverse=True)
#Loop to return first 10 tuples and prints the outcome
for i in range(min(10, len(words))):
    print(words[i])
