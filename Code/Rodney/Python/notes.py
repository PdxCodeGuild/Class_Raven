

normal_alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
new_alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
used_letters = []
new_letter = ''
user_number = 5
#x = 26 - user_number
#normal_alphabet2 = normal_alphabet2[:x:]

for letter in normal_alphabet:
    if letter in used_letters:
        continue
    index = normal_alphabet.index(letter) 
    new_index = index + user_number
    new_letter = normal_alphabet[new_index]
    new_alphabet[index] = normal_alphabet[new_index]
    new_alphabet[new_index] = normal_alphabet[index]



print(new_alphabet)