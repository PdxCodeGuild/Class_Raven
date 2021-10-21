"""
Lee Colburn
Evening Bootcamp - PDX Code Guild
Lab 11 - Rot Cipher
"""

"""Rot Cipher
Write a program that prompts the user for a string, and encodes it with ROT13. 
For each character, find the corresponding character, add it to an output string. 
Notice that there are 26 letters in the English language, so encryption is the same as decryption.

Index	0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	23	24	25
English	a	b	c	d	e	f	g	h	i	j	k	l	m	n	o	p	q	r	s	t	u	v	w	x	y	z
ROT+13	n	o	p	q	r	s	t	u	v	w	x	y	z	a	b	c	d	e	f	g	h	i	j	k	l	m


Version 2
Allow the user to input the amount of rotation used in the encryption. (ROTN)


Version 3 (optional)
Add support for capital letters, numbers, and special characters. These can be handled in two different ways:

Capital letters can be rotated as well, numbers and special characters can be put directly into the output (e.g. "hello world!" becomes "uryyb jbeyq!").

Instead of using an alphabet of just letters, include numbers, spaces, and special characters as well.
"""
import string

def encrypt(user_string,rot):
    alphabet_lowercase = string.ascii_lowercase
    alphabet_uppercase = string.ascii_uppercase
    shifted_alphabet_lowercase = alphabet_lowercase[26-rot:] + alphabet_lowercase[0:(26-rot)] 
    shifted_alphabet_uppercase = alphabet_uppercase[26-rot:] + alphabet_uppercase[0:(26-rot)]
    encrypted_message = ""


    for i in range(len(user_string)):
        if alphabet_lowercase.find(user_string[i]) == -1:
            encrypted_message = encrypted_message + user_string[i]
        elif user_string[i].isupper() == True:
            encrypted_index = alphabet_uppercase.find(user_string[i])
            encrypted_message = encrypted_message + shifted_alphabet_uppercase[encrypted_index]
        else: #user_string[i].islower() == True:
            encrypted_index = alphabet_lowercase.find(user_string[i])
            encrypted_message = encrypted_message + shifted_alphabet_lowercase[encrypted_index]
        
    print(encrypted_message)
    return encrypted_message

def decrypt(user_string, rot):
    """Returns a decrypted string based on the message and data offset"""
    decrypted_string = encrypt(encrypt(user_string,rot),26-rot)
    return decrypted_string

####################### INTERFACE ##############################################################
complete = False

while not complete:

  # Select Option 1-Pass Message, 2-Exit, 3+ Try Again
  start = int(input(f'\nPlease select from the following options:\n 1. Encode a string with ROT based encryption \n 2. Decrypt last message (or your own) \n 3. Exit Program \n\n Enter the number of your choice: \n'))
  
  ################### DIRECTORY ################################################################
  # Allow user to escape
  if start == 3:
    print(f"\nClosing application.\n")
    complete = True
    break

  if start > 3:
    print(f'\n Try again:\n')
    continue
  
  # Direct user to appropriate function: Select Option 1 - Pass Message
  if start == 1:

    user_string = input("Enter your string: ")
    rot = int(input("Enter the number of digits you'd like to offset the data (1-26): "))
    encrypted_string = encrypt(user_string.lower(), rot)

  if start == 2:
    decrypted_string = " "
    selection = input(f"Would you like to: \n 1. If available, decrypt the stored message: {encrypted_string} \n 2. Decrypt your own message ")
    if selection == 1:
        rot = int(input("Enter the number of digits you'd like to offset the data for decryption (1-26): "))
        decrypt(encrypted_string, rot)
        print(decrypted_string)

    if selection == 2:
        rot = int(input("Enter the number of digits you'd like to offset the data for decryption(1-26): "))
        user_string = input("Enter your string: ")
        decrypt(user_string, rot)
        print(decrypted_string)

