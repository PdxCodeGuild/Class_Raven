def alphabet_creator(user_number):
##this function will create a cypher alphabet based on user entered rotations
    normal_alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    new_alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    ## one alphabet to draw from, one to convert to new alphabet
    counter = 0 # set counter to 0, will be used in while function 
    new_letter = '' # creating new letter variable 
    x = 25 - user_number # creating variable set to 25 (indices) minus number user enters
    sliced_alphabet = normal_alphabet[:user_number:] ## [beginning of alpha: end will be based on user entry:interval is 1], slicing off end of alphabet based on user entry 

    for letter in normal_alphabet: ## looping through letters in alphabet
        while counter > x: ## while counter is greater than number of indices minus what will be sliced
            new_alphabet.pop() ## remove letters from end of new alphabet 
            if len(new_alphabet)-2 < x: ## if length of new_alphabet -2 (to account for 0 index) is less than counter, break out of loop by making counter -1
                counter = -1
        if counter == -1:
            break
        index = normal_alphabet.index(letter) ## index = normal alphabet index 
        new_index = index + user_number ## new index is that index + user entered number, which will give us new letter
        new_letter = normal_alphabet[new_index]
        new_alphabet[index] = new_letter # assign the new alphabet index that new letter
        counter += 1 ## counter + 1 to allow for above while loop
    new_alphabet.extend(sliced_alphabet) ## add the slided off alphabet to the new alphabet we just created and return function 
    outcome = new_alphabet
    return outcome 

def new_dict(new_alphabet, cypher_dict):
## this function will create new cyber dict based on the new cypher alphabet we just created
    for letter in new_alphabet:  ## essentially looping through the old dictionary and replacing old values(random alphabet) with new values (alphabet based on user entry for rotations)
        for key,val in cypher_dict.items():
            cypher_dict[key] = letter
            new_alphabet.remove(letter)
            if len(new_alphabet) != 0:
                letter = new_alphabet[0]
            else: 
                break
    new_dict = cypher_dict
    return new_dict  ## returning that new dict 

cypher_dict = {'a': 'n','b': 'o','c': 'p', 'd': 'q', 'e': 'r','f': 's','g': 't','h': 'u','i': 'v','j': 'w','k': 'x','l': 'y',
'm': 'z','n': 'a','o': 'b','p': 'c','q': 'd','r': 'e','s': 'f','t': 'g','u': 'h','v': 'i','w': 'j','x': 'k','y': 'l','z': 'm'}

rot_number = input("Hello, please provide rotation number:\n> ")
rot_number = int(rot_number)
new_alphabet = alphabet_creator(rot_number) ## calling alphabet creater function based on user entry 
user_word = input("What word would you like to encode?\n> ")
user_word = list(user_word) ## turning that string to list 
new_cypher_dict = new_dict(new_alphabet, cypher_dict) ## calling new_dict function 

user_cypher_list = []  ## creating an empty list we will append the cypher letters to 
for letter in user_word: ## iterating through each letter in that user string list 
    for key in new_cypher_dict: ## if letter is same as key in dictionary, convert that letter to the value of that key in the dictionary 
        if letter == key:
            new_letter = new_cypher_dict[key]
            user_cypher_list.append(new_letter)  ## and then add to new cypher list 


user_cypher_list = ''.join(user_cypher_list) ## convert new cypher list to string before printing 
print(f'Your enconded word by {rot_number} rotations is: {user_cypher_list}')
