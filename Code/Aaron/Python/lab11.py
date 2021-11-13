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


# encrypt the message
input_number = []
for letter in holding:
    if letter == numbers[letter]:  # this gives user letter as number
        temp = numbers[letter]
        print(temp)


# decrypt the message

# print the encryption
