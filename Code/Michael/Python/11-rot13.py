"""
PDX Code Guild Full Stack Bootcamp
->Lab 11
  Rot13
Michael B

Write a program that prompts the user for a string, and encodes it with ROT13. For each character, find the corresponding character, add it to an output string. 
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


def rot_cipher(user_string, rot_num=13) -> str:
    import string

    rot_num = (
        rot_num % 26
    )  # If the number of rotations is greater than 26, it will loop back around to the beginning of the alphabet.
    alphabet = (
        string.ascii_letters + string.digits + string.punctuation
    )  # Creates a string of all the letters, numbers, and special characters.
    rot_alphabet = (
        alphabet[rot_num:] + alphabet[:rot_num]
    )  # Rotates the alphabet by the number of rotations specified.
    rot_dict = dict(
        zip(alphabet, rot_alphabet)
    )  # Creates a dictionary with the original alphabet as the keys and the rotated alphabet as the values.
    rot_string = ""
    for char in user_string:  # Loops through each character in the user_string.
        if (
            char in rot_dict
        ):  # If the character is in the dictionary, it will be replaced with the corresponding character in the rotated alphabet.
            rot_string += rot_dict[char]
        else:  # If the character is not in the dictionary, it will be left as is.
            rot_string += char
    return rot_string


def get_user_input() -> str:
    string = input("Enter a string to encrypt: ")
    rot_num = input("Enter a number of rotations: ")
    return string, int(rot_num)


if __name__ == "__main__":
    user_input = get_user_input()  # Gets the user input.
    ciphered = rot_cipher(
        user_input[0], user_input[1]
    )  # Calls the rot_cipher function and stores the result in the variable ciphered.
    print(
        f"You're ciphered phrases is: {ciphered} after rotating {user_input[1]} times."
    )
