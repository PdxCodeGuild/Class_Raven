# Rot Cipher
# Write a program that prompts the user for a string, and encodes it with ROT13. For each character, find the corresponding character, add it to an output string. Notice that there are 26 letters in the English language, so encryption is the same as decryption.

# Index	  	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	23	24	25 26
# English	a	b	c	d	e	f	g	h	i	j	k	l	m	n	o	p	q	r	s	t	u	v	w	x	y	z
# ROT+13	n	o	p	q	r	s	t	u	v	w	x	y	z	a	b	c	d	e	f	g	h	i	j	k	l	m
# Version 2
# Allow the user to input the amount of rotation used in the encryption. (ROTN)

import string

# words is a variable coming from the user
words = input("choose words to encrypt: ")

# all letters lower case and replace spaces
holding = words.lower().replace(" ", "")

extra_val = ""

# replace non letters
for letter in words:
    if not letter.isalpha():
        extra_val = letter  # punctuation holder
        holding = holding.replace(letter, "")
    
# number the alphabet
alpha = {}
numbers = {}
for num, letter in enumerate(string.ascii_lowercase, start=1):
    alpha[num] = letter
    numbers[letter] = num


# grab each letter in user input and assign number
input_number = []
for letter in holding:
    input_number.append(numbers[letter] + 13)  # appends the number of the letter of the user input
print(input_number)
        
# adjust alphabet limit       
for num, letter in enumerate(input_number):
    if letter > len(string.ascii_lowercase):
        input_number[num]= letter - len(string.ascii_lowercase)
print(input_number)

# grab the associated letter to the ROT number
encrypted_message = ""
for num in input_number:
    encrypted_message += alpha[num]
print(encrypted_message)


# store the index number of the space and special character
spaces = [i for i, space in enumerate(words) if space.isspace()]

# insert spaces in the rot string
for count in spaces:
    encrypted_message = encrypted_message[:count] + " " + encrypted_message[count:] # overloading the variable, inserting a space into string

# print the encryption
print(encrypted_message)