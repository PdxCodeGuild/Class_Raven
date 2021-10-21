"""
Lee Colburn
Evening Bootcamp - PDX Code Guild
Lab 11 - Rot Cipher
"""
import string

def encrypt(user_string,rot):
    """Takes in a string and integer to set a rotated alphabet. Encrypts a messsage and returns the string"""
    alphabet_printable = string.printable + " " # 101 chars: " " 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ 
    shifted_alphabet_printable = alphabet_printable[101-rot:] + alphabet_printable[0:(101-rot)] # rotates string to correspond with printable alphabet
    encrypted_message = ""

    for i in range(len(user_string)):
        encrypted_index = alphabet_printable.find(user_string[i])
        if encrypted_index == -1:
            encrypted_message = encrypted_message + user_string[i]
        else:
            encrypted_message = encrypted_message + shifted_alphabet_printable[encrypted_index]
        
    return encrypted_message

def decrypt(user_string, rot):
    """Returns a decrypted string based on the message and data offset"""
    decrypted_string = encrypt(user_string,101-rot)
    print(f"Your decrypted string is: {decrypted_string}\n Returning to main menu")
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
    rot = int(input("Enter the number of digits you'd like to offset the data (1-101): "))
    encrypted_string = encrypt(user_string, rot) # lower only test: encrypted_string = encrypt(user_string.lower(), rot)
    print(f"\nYour encrypted string is: {encrypted_string}\n\n If you'd like to decrypt this string, please remember it has been offset {rot} digits. \n Returning to main menu...")

  if start == 2:
    decrypted_string = ""
    selection = int(input(f"Would you like to: \n 1. If available, decrypt the stored message: {encrypted_string} \n 2. Decrypt your own message \n"))

    if selection == 1:
        rot = int(input("Enter the amount of digits the string is offset (1-101): \n"))
        decrypt(encrypted_string, rot)
        print(decrypted_string)

    if selection == 2:
        user_string = input("Enter the encrypted string: ")
        rot = int(input("Enter the amount of digits the string is offset (1-101): \n"))
        decrypted_string = decrypt(user_string, rot)
        print(f"Decrypted string: {decrypted_string} \n")