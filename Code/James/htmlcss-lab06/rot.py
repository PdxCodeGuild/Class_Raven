import string
 
encrypt = list('catdog'.upper())
print(encrypt)

# encrypt_sort = encrypt.sort() 

    
    # here we have list of the alphabet
uppercase_alphabet = list(string.ascii_uppercase)

print(uppercase_alphabet)
# I want to compare each index of encrypt with the uppercase_alphabet index

encrypted_message = []

index= 0
# i want to loop through the list for as many characters are in list, 

for index in range(len(encrypt)):
    # its only doing first index during the loop
    # for encrypt[index] in uppercase_alphabet[index]:
    
    #this code is appending to the encrypt list 
    # this is just changing the uppercase alphabet list
        cipher = uppercase_alphabet.index(encrypt[index])
        encrypted_message.append(uppercase_alphabet[(cipher  + 13) % 26 ])
        
        
        
        index += 1
print(encrypted_message)