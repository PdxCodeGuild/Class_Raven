import string

punc = string.punctuation
#print(punc)

punc_list = list(punc)

print("Palindrome Checker")

word_1 = input("enter word:\n>")

word_1 = word_1.lower()

while (" ") in word_1:
    word_1 = word_1.replace(" ", "")

for x in punc_list:
    if x in word_1:
        word_1 = word_1.replace(x, "")

word_list = list(word_1)

word_list.reverse()

reverse_1 = ''.join(word_list)

### or you can use reverse_1= word_1[::-1]

if word_1 == reverse_1:
    print(f"{word_1} is a palindrome.")
else:
    print(f"{word_1} is not a palindrome.")