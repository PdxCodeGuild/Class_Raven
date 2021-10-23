#  Counts words longer than 4 letter in a text and returns the ten most used

word_dict = {}

with open("/Users/sheridover/Documents/Class_Raven/Code/Anne/test.txt", 'r') as my_file:
    contents = my_file.read()
    # Make everything lowercase,
    contents.lower()
    # strip punctuation
    punct = '''!()-[]_*{;}:'"\,<>./?$&'''
    new_line = '''\n'''
    for i in contents:
    #         print(i)  # it's going through each letter!        
        if i in punct:
            contents =contents.replace(i, " ")
    for i in contents:        
        if i in new_line:
            contents =contents.replace(i, " ")
             
    # split into a list of words
    a_list = contents.split(' ')

    new_list = [x for x in a_list if len(x) > 4]


    for word in new_list:
        if word not in word_dict:
            word_dict[word] = 1 
        else:
            word_dict[word] += 1
    the_test_dict = word_dict
  
    words = list(the_test_dict.items()) # .items() returns a list of tuples
    words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
    for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
        print(words[i])



