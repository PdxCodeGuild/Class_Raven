# Lab_11 Rot Cipher
#Rafael Medina

"""
NOTE: Still in progress
10/28/2021

"""

import string



abc = ['ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz' ]
# list index upper[0] and lower[1]



 
# function to move the character index by 13
def rot_cipher(cipher, rotate = 13):
#    .maketrans allows the mapping of a character to its translation/replacement for interchangeable lowers and uppers.
    trans_abc = str.maketrans(f'{abc[0]}{abc[1]}{abc[0]}',f'{abc[0][rotate:]}{abc[0][rotate]}{abc[1][:rotate]}')

    return str.translate(cipher, rotate)

cipher = input('\n\nEnter what you would like to get encoded: ')
# # of rotations
rotate = input('How many rotations would you like?: ')

#if rotate == 0 or 26 or 52 or 78 or 104 or 130 or 156 or 182 or 208:
    #print(f'Use another rotation number that is less than 208 and not {rotate}. This resets the cipher')

print(f'Your ciphere\'d message is: {rot_cipher(cipher, rotate)}')








"""
def rot_cipher(abc):

    cipher = input('\n\nEnter what you would like to get encoded: ')

    for i in abc:
        if i.isupper():
            cipher.append(string.ascii_upper)[string.ascii_upper.find(i) + 13 % 2




"""
"""

cipher = input('\n\nEnter what you would like to get encoded: ')
# # of rotations
rotation = input('How many rotations would you like?: ')
  

# allows to use a range
iterations = len(cipher)

# Output is gooing to be a string. 
# non ascii alphabet spaces and characters
output = ""

for i in range(iterations):
    new_char = cipher[i]
   
# find() method finds the first occurrence of the specified value 26 is the range.
    location = string.ascii_lowercase.find(new_char)

    if location < 0:
        output += cipher[i]
    else:
        index_shit = string.ascii_lowercase.index[i] + rotation % 26
        output += string.ascii_lowercase[index_shit]
    

print(output)







rotation = int()


# function to include user_input rotation amount  
def rot_cipher (cipher, rotation):
# non ascii alphabet spaces and characters     
    blank_spaces = ''
    
    
    
    for i in cipher:
        if i in string.ascii_lowercase:

            index_rotation = string.ascii_lowercase.index[i] + rotation % 26
# moves the blank_spaces allong with the cipher abc 
            blank_spaces = blank_spaces + string.ascii_lowercase[index_rotation]
        else:
            blank_spaces = blank_spaces + i
       
        return blank_spaces
    
    
    cipher = input('\n\nEnter what you would like to get encoded: ')
    rotation = input(int('How many rotations would you like?: '))
    print(cipher, rotation)


"""