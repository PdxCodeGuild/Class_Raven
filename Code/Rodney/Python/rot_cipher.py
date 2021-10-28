



cypher_dict = {'a': 'n','b': 'o','c': 'p', 'd': 'q', 'e': 'r','f': 's','g': 't','h': 'u','i': 'v','j': 'w','k': 'x','l': 'y',
'm': 'z','n': 'a','o': 'b','p': 'c','q': 'd','r': 'e','s': 'f','t': 'g','u': 'h','v': 'i','w': 'j','x': 'k','y': 'l','z': 'm'}
## dictionary with letter: cypher letters as key: value pairs

user_string = input("Please provide a word that you would like encrypted:\n> ") ## asking user for string
user_string = list(user_string) ## turning that string to list 

user_cypher_list = []  ## creating an empty list we will append the cypher letters to 
for letter in user_string: ## iterating through each letter in that user string list 
    for key in cypher_dict: ## if letter is same as key in dictionary, convert that letter to the value of that key in the dictionary 
        if letter == key:
            new_letter = cypher_dict[key]
            user_cypher_list.append(new_letter)  ## and then add to new cypher list 


user_cypher_list2 = []  ## creating an empty list we will append the cypher letters to 
for letter in user_cypher_list: ## iterating through each letter in that user string list 
    for key in cypher_dict: ## if letter is same as key in dictionary, convert that letter to the value of that key in the dictionary 
        if letter == key:
            new_letter = cypher_dict[key]
            user_cypher_list2.append(new_letter)

print(''.join(user_cypher_list)) ## convert new cypher list to string before printing 
print(''.join(user_cypher_list2))

