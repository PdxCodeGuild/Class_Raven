"""

Rot Cipher ( this is just a normal ROT cipher so no rotation has not been specified yet) ( the example below is a ROT14 cipher because it rotates the character 14 places)

Write a program that prompts the user for a string, and encodes it with ROT13.
For each character, find the corresponding character, add it to an output string. 
Notice that there are 26 letters in the English language, so encryption is the same as decryption.

Index 	0 	1 	2 	3 	4 	5 	6 	7 	8 	9 	10 	11 	12 	13 	14 	15 	16 	17 	18 	19 	20 	21 	22 	23 	24 	25
English 	a 	b 	c 	d 	e 	f 	g 	h 	i 	j 	k 	l 	m 	n 	o 	p 	q 	r 	s 	t 	u 	v 	w 	x 	y 	z
ROT+13 	n 	o 	p 	q 	r 	s 	t 	u 	v 	w 	x 	y 	z 	a 	b 	c 	d 	e 	f 	g 	h 	i 	j 	k 	l 	m

Version 2
Allow the user to input the amount of rotation used in the encryption. (ROTN)


Version 3 (optional)

Add support for capital letters, numbers, and special characters. These can be handled in two different ways:

Capital letters can be rotated as well, numbers and special characters can be put directly into the output (e.g. "hello world!" becomes "uryyb jbeyq!").

Instead of using an alphabet of just letters, include numbers, spaces, and special characters as well.

"""

#this is all version of the lab combined

from string import ascii_lowercase,ascii_uppercase


plainLowerLetters = ascii_lowercase
plainUpperLetters = ascii_uppercase
cipher_text = []
plain_text = input("Please enter a string: ")
rotation = int(input("Please enter the rotation you would like for encryption: "))

for i in plain_text:
    if i in plainLowerLetters:
        new_index = (plainLowerLetters.find(i) + rotation) % 26 # needed stack overflows help on this one, to prove I did not copy pasta, new_index is a place holder for the flipped version of the original character in the users given string
        # the find() method will return the index of the given character or word from a string, we add that index to the rotaion the user wanted, then divide it  by 26.
        #the % 26 is in case the user puts a rotation equal to or over 26, if its equal to 26 it will return a new index of 0, if not then the % will return the index as if we looped all the way around the list 'plain_letter'
        # this lets us avoid the 'index out of range error"
        cipher_text.append(plainLowerLetters[new_index])# here were are creating the encypted version or the users string. It just goes into the list 'plain letters' and grabs the values located at the 'new_index'
    elif i in plainUpperLetters: # this does the same thing as the above if statement except in case the user enteres Capital letters
        new_index = (plainUpperLetters.find(i) + rotation) % 26
        cipher_text.append(plainUpperLetters[new_index])
    else:
        cipher_text.append(i) # this is so that if the user enters anything that is not a letter, It still gets added to the encrypted string

cipher_text = ''.join(cipher_text)
print(f"Encrypted string is : {cipher_text}")


