""" rot cipher"""
import string



#making alphabet from string module.
alpha = string.ascii_lowercase



while True:
        # taking user input
        user = input("Enter your message here: \n>>>").lower()
        if not user.isalpha():
            print("Please enter only letters.")
            continue
            
        rot = input("Enter your rotation: ")
        if not rot.isnumeric():
            print("Please enter only numbers.")
            continue
        rot = int(rot)

        user_output = []
        #for each character in user input add it to an output list
        for element in user:
            #alpha.append(element)
            index = alpha.find(element)
            encrypt = (index + rot) % 26
            #print(encrypt)
            user_output.append(alpha[encrypt])
            #print(user_output)
        
        #why is print printing the list and the string?
        print(''.join(user_output))
        break






print(user_output)