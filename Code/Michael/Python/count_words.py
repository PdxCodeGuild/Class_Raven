"""
PDX Code Guild Full Stack Bootcamp
->Lab 13
  Count Words
Michael B

Let's write a python module to analyze a given text file containing a book for its vocabulary frequency and display the most frequent words to the user in the terminal.
Remember there isn't any "perfect" way to identify a word in english (acronymns, mr/ms, contractions, etc), try to find rules that work best.

Find a book on Project Gutenberg and navigate to the plain-text version. You can then send a request to that url using the requests library to get the text into Python. 
You can also save the file into the same folder as the .py file and open it using with.

import requests
response = requests.get('https://www.gutenberg.org/files/62897/62897-0.txt')
response.encoding = 'utf-8' # set encoding to utf-8
print(response.text)
We can also download a file of english words and place it next our .py file and load it like so:

with open('the_raven.txt', 'r', encoding='utf-8') as file:
    text = file.read()
print(text)
Take the following steps to build up our dictionary. The result should look something like {'a': 3, 'the': 4}

Make everything lowercase, strip punctuation, split into a list of words.
Your dictionary will have words as keys and counts as values. If a word isn't in your dictionary yet, add it with a count of 1. If it is, increment its count.
Print the most frequent top 10 out with their counts. You can do that with the code below.
# word_dict is a dictionary where the key is the word and the value is the count
word_dict = {'apples': 2, 'bananas': 1, 'pears': 1, 'kiwi': 7}
words = list(word_dict.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])
Version 2 (optional)
Count how often each unique pair of words is used, then print the top 10 most common pairs with their counts.

Version 3 (optional)
Let the user enter a word, then show the words which most frequently follow it.
"""


def count_words(text) -> dict:
    text = text.lower()  # make everything lowercase.
    for c in '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~':  # strip punctuation.
        text = text.replace(c, " ")
    words = text.split()  # split into a list of words.
    word_dict = {}
    for word in words:  # loop through words
        if word in word_dict:  # if the word is in the dictionary.
            word_dict[word] += 1
        else:  # if the word is not in the dictionary.
            word_dict[word] = 1
    return word_dict


def get_following_words(word, text) -> list:
    text = text.lower()  # make everything lowercase
    for c in '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~':  # strip punctuation.
        text = text.replace(c, " ")
    words = text.split()  # split into a list of words.
    word_dict = {}
    for i in range(len(words)):
        if (
            words[i] == word
        ):  # if the word is in the dictionary and matches the word entered.
            if i < len(words) - 1:  # if the word is not the last word in the list.
                if words[i + 1] in word_dict:  # if the word is in the dictionary.
                    word_dict[words[i + 1]] += 1
                else:  # if the word is not in the dictionary.
                    word_dict[words[i + 1]] = 1
    return word_dict


def load_file(
    file_name="the_raven.txt", url="https://www.gutenberg.org/files/62897/62897-0.txt"
) -> str:
    try:  # Open the file 'file_name' if it exists.
        with open(file_name, "r", encoding="utf-8") as file:
            text = file.read()  # read the file.
            print("File loaded.\n")
    except FileNotFoundError:  # If the file doesn't exist, download it from 'url'.
        import requests

        response = requests.get(url)
        response.encoding = "utf-8"  # set encoding to utf-8.
        text = response.text  # get the text.
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(text)
            print("File downloaded and saved.\n")
    except:
        print("Something went wrong.\n")
    return text


if __name__ == "__main__":
    text = load_file()
    word_dict = count_words(
        text
    )  # call the count_words function and assign the result to a variable.
    words = list(word_dict.items())  # .items() returns a list of tuples.
    words.sort(
        key=lambda tup: tup[1], reverse=True
    )  # sort largest to smallest, based on count.
    print(f"There are {len(words)} words. The most common words are:")
    for i in range(
        min(10, len(words))
    ):  # print the top 10 words, or all of them, whichever is smaller.
        print(words[i])

    user_word = input("\nEnter a word: ")  # get a word from the user.
    word_dict = get_following_words(
        user_word, text
    )  # call the get_following_words function and assign the result to a variable.
    words = list(word_dict.items())  # .items() returns a list of tuples.
    words.sort(
        key=lambda tup: tup[1], reverse=True
    )  # sort largest to smallest, based on count.
    print(f'\nThere are {len(words)} words following "{user_word}"')
    for i in range(
        min(10, len(words))
    ):  # print the top 10 words, or all of them, whichever is smaller.
        print(words[i])
    if len(words) == 0:  # if there are no words following the word entered.
        print("There are no words following", user_word)
    elif len(words) < 10:  # if there are less than 10 words following the word entered.
        print("There are less than 10 words followings", user_word)
