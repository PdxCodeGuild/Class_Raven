#Bringing in the string module to get the ascii punctuation characters
from string import punctuation as characters
#Create two lists, one for each input that we will use to compare against eachother
value_1_list = []
value_2_list = []
#Ask user for words and store them as a variable
value_1 = input('Enter the first word: ')
value_2 = input('Enter the second word: ')
#First convert anything entered to lower case
value_1.lower()
value_2.lower()
#Next remove white space
value_1.replace(" ","")
value_2.replace(" ","")
#Create a blank string to store the results of our comparison between the input and punctuation
value_1_clean = ''
#Create a for loop that iterates through the input word
for i in value_1:
    #Create an if statement that identifies if a letter is not in the punctuation and save it to the clean variable
    if i not in characters:
        value_1_clean = value_1_clean + i
#Follow the same process for the second variable
value_2_clean = ''
for i in value_2:
    if i not in characters:
        value_2_clean = value_2_clean + i
#Convert the string variable to a list
value_1_list.extend(value_1_clean)
value_2_list.extend(value_2_clean)
#Sort the list alphabetically
value_1_list.sort()
value_2_list.sort()
#Complete the logic to test the sorted lists against eachother to identify if they are anagrams.
if value_1_list == value_2_list:
    print(f'"{value_1_clean}" and "{value_2_clean}" are anagrams')
else:
    print(f'"{value_1_clean}" and "{value_2_clean}" are not anagrams')