""" rot cipher"""
import string



#generating two lists and then fusing them in a dictionary
alpha = string.ascii_lowercase
# num = [i for i in range(26)]
# res = {alpha[i]: num[i] for i in range(len(alpha))}

# taking user input
while True:
    user = input("Enter your message here: \n>>>").lower()
    if not user.isalpha():
        print("Please enter only letters.")
        continue
    
    rot = input("Enter your rotation: ")
    if not rot.isnumeric():
        print("Please enter only numbers.")
        continue
    else:
        rot = int(rot)

    user_output = []
    #for each character in user input add it to an output list
    for element in user:
        #alpha.append(element)
        index = alpha.find(element)
        encrypt = (index + rot) % 26
        print(encrypt)
        user_output.append(alpha[encrypt])
        print(user_output)
    # for each element in the list match it the dictionary index

    print(''.join(user_output))
    break
# new_index = index + 13

# a


# for element in user_output:
#     if element in res:
#         element + 13
        #move the element 13 positions to the right



#print(user_output)