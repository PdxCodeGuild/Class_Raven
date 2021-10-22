# I wanted to get the text of sense and sensibility form https://www.gutenberg.org/cache/epub/21839/pg21839.txt
# but I couldn't figure how to take the retrieved text and write it to a file I made. 
word_dict = {}

with open("/Users/sheridover/Documents/Class_Raven/Code/Anne/test.txt", 'r') as my_file:
    contents = my_file.read()
    # Make everything lowercase,
    contents.lower()
    # strip punctuation
    punct = '''!()-[]_*{;}:'"\,<>./?$&'''
    for i in contents:
        if i in punct:
            contents = contents.replace(i, " ")
    new_line = '''\n'''
    for i in contents:
        if i in new_line:
            contents = contents.replace(i, " ")
    # split into a list of words
    list = contents.split(' ')
    for word in list:
        if word not in word_dict:
            word_dict[word] = 1 #fruits['banana'] = 0.25
        else:
            word_dict[word] += 1 # fruits['apple'] = 2.0 a_dict["a"] += 1
    print(word_dict)



# Print the most frequent top 10 out with their counts. You can do that with the code below.


# words = word_dict.items()
# print(words) # .items() returns a list of tuples
# words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
# for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
#     print(words[i])