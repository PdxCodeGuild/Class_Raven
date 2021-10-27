import string

punc = string.punctuation
#print(punc)

punc_list = list(punc)

print("Anagram Checker")

word_1 = input("enter first word:\n>")

word_2 = input("enter second word:\n>")

word_1 = word_1.lower()

word_2 = word_2.lower()

while (" ") in word_1:
    word_1 = word_1.replace(" ", "")

while (" ") in word_2:
    word_2 = word_2.replace(" ", "")

for x in punc_list:
    if x in word_1:
        word_1 = word_1.replace(x, "")

for x in punc_list:
    if x in word_2:
        word_2 = word_2.replace(x, "")

check_1= list(word_1)

check_2= list(word_2)

check_1.sort()

check_2.sort()

#print(check_1)
#print(check_2)

if check_1 == check_2:
    print(f"{word_1} and {word_2} are anagrams.")
else:
    print(f"{word_1} and {word_2} are not anagrams.")