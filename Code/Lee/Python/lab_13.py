"""
Lee Colburn
Evening Bootcamp - PDX Code Guild
Lab 13 - Word Counts
"""

############################ VERSION 1 ########################################
"""Let's write a python module to analyze a given text file containing a book for its vocabulary frequency and display the most frequent words to the user in the terminal."""

import requests

with open('ulysses.txt','r', encoding='utf-8') as book:
    ulysses_text = book.readlines()
    cleaned_text = []
    book_dict = {}
    
    for line in ulysses_text:
        
        
        line.translate(str.maketrans("", ""))
        for word in line.split():
            
            word = word.strip("-")
            word = word.strip(",")
            word = word.strip(".")
            word = word.strip("!")
            word = word.strip(";")
            word = word.strip("â")
            word = word.strip("'")
            word = word.strip(" ")
            word = word.lower()
            cleaned_text.append(word)

            if word not in book_dict.keys():
                book_dict[word] = 1
            else:
                book_dict[word] += 1
    

    sorted_counts = sorted(book_dict.items(), key = lambda t: t[1], reverse = True)


    count = 1
    print("Top Ten Most Used Words in James Joyces' 'Ulysses':")
    for i in sorted_counts[:10]:
        print(f"({count}/10): {i}")
        count += 1

    ############################ VERSION 2 ########################################
    """Count how often each unique pair of words is used, then print the top 10 most common pairs with their counts."""

    doubles = zip(cleaned_text[:-1], cleaned_text[1:])
    doubles_dict = {}

    for words in doubles:
        if words not in doubles_dict.keys():
            doubles_dict[words] = 1
        else:
            doubles_dict[words] += 1

    doubles_counts = sorted(doubles_dict.items(), key = lambda t: t[1], reverse = True)
    count = 1
    print("Top Ten Most Used Word Pairs in James Joyces' 'Ulysses': ")
    for i in doubles_counts[:10]:
        print(f"{count}/10): {i}")

    ############################ VERSION 3 ########################################
    """Let the user enter a word, then show the words which most frequently follow it."""

    search_word_init = input("Enter '1' if you'd like to search for a term, or press any key to exit. ")
    if search_word_init == "1":
        search_word = input("Enter a word to search for: ")
        text_match = False
        while text_match == False:
            print(f"\nSearching for: '{search_word}' ....... \n")
            search_result = book_dict.get(search_word, "Zero")
            print(f"The word '{search_word}' appears {search_result} times.")
            text_match = True
    book.close()

