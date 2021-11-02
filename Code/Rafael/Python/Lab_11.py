# Lab_11 Rot Cipher
#Rafael Medina

"""
NOTE: 11/01/2021

"""

# "Write a program that prompts the user for a string, and encodes it with ROT13. For each character, find the corresponding character, add it to an output string. Notice that there are 26 letters in the English language, so encryption is the same as decryption."


import string


# ascii string for alphabet letters in a list with indexes [i]
abc = list(string.ascii_lowercase)

#print(abc)

# function to return the converted characters in rotations = x spaces forward.
def rot_13(output):

# Number of rotations forward staring from [i] index location in abc.    
    rotations = 13
# User_input starts as an empty string prior to message concactinations.
    user_input = ""
   
    for i in output:
# If the user_input is equal to an empty string " " then it will be added to the output string as an empty string.
        if i == " ":
# Concactinates an empty string after the previous user_input [i] or " " empty space choosen user_input as it goes down the loop.
            user_input = user_input + " "
# Else if the user_input enters an alphabetic lowercase then that lowercase is moved forward the rotation value x 13 times as an integer value, so i[0] = i[13].

        else:
            index_position = abc.index(i) + int(rotations)
# If index position is within range of abc index < 26 and not an empty string then in can be included in the output with its new character position from the index_position function as long as it is index [25] or under after the 13 rotations have beend added.
            if index_position < 26:
                user_input = user_input + abc[index_position]

            else: 
# Otherwise if it is out of range beyond the [25]index, the modulus % 26 operator resets that position[i] if its over [25] and keeps the values in range [0] to [25]. For example if user_inputs "z" then the index position becomes 25 + 13 = 38, so greater than index[25] uses modulus % 26, this resets to index [0] on a chosen[i] outside the [25] range and moves the index 13 positions over again for a value within the abc[i]. So, "z" then becomes [12] or "m".                    
                user_input = user_input + abc[index_position % 26]
    return user_input


user_input = input("Enter text to cipher in lower case english only: ")

print(rot_13(user_input))



