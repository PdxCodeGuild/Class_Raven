#lab11 ROT-13

import string
def main():
    user_input = input("Enter word or phrase to be encrypted: ")
    while True:
        try:
            encrypt = int(input("Enter the number of cypher shifts: "))
            break
        except:
            print("Something went wrong, try again.")
            
    enc_str = encrypt_string(encrypt, user_input)
    print(str(enc_str))
def encrypt_string(num, str):
    encrypted = []
    for char in str:
        while (ord(char)) + num > 122:
            num = num - 26
        encrypted.append(chr(ord(char) + num))
    return encrypted

main()