#lab21: Count words

import string

with open('story_book.txt', encoding='utf8') as book_txt:
    contents = book_txt.read()

stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]


def format_text(x):
    formats = contents.lower()
    formats = formats.replace("\n", " ")
    for each in string.punctuation:
        formats = formats.replace(each, "")
    return formats


def words(x):
    content = format_text(contents)
    content = content.split(" ")
    return content

def unique(x):
    content = words(contents)
    content = set(content)
    original = set(contents)
    stopwords_set  = set(stopwords)
    content = content | original
    content = content - stopwords_set
    content = list(content)
    content =  [each for each in content if each != ""]
    return content

unique_words = unique(contents)
counts = [1 for each in unique_words]

numword = dict(zip(unique_words, counts))

def count_words(x):
    check = words(contents)
    for i in check:
        if i in numword:
            value = numword[i]
            value += 1
            numword[i] = value
    return numword

numword = count_words(contents)

most_w = list(numword.items())
most_w.sort(key=lambda tup: tup[1], reverse=True) 
print(most_w[:10])
for i in range(min(10, len(most_w))):
    print(most_w[i])