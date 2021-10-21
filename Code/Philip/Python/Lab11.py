'''Rot Cipher Lab11
By Philip Bartoo
PDX Code Guild'''

#Take user input for a string to encrypt and the rotation for the cypher as an integer
encrypt = input('Enter string to encrypt: ')
rotation = int(input('Enter rotation: '))

#Build two dictionaries, one with letter keys and one with number keys
alphabet1 = {
        'a' : '1', 
        'b' : '2', 
        'c' : '3', 
        'd' : '4', 
        'e' : '5', 
        'f' : '6', 
        'g' : '7', 
        'h' : '8', 
        'i' : '9', 
        'j' : '10', 
        'k' : '11', 
        'l' : '12', 
        'm' : '13', 
        'n' : '14', 
        'o' : '15', 
        'p' : '16', 
        'q' : '17', 
        'r' : '18', 
        's' : '19', 
        't' : '20', 
        'u' : '21', 
        'v' : '22', 
        'w' : '23', 
        'x' : '24', 
        'y' : '25', 
        'z' : '26'
    }

alphabet2 = {
        '1' : 'a', 
        '2' : 'b', 
        '3' : 'c', 
        '4' : 'd', 
        '5' : 'e', 
        '6' : 'f', 
        '7' : 'g', 
        '8' : 'h', 
        '9' : 'i', 
        '10' : 'j', 
        '11' : 'k', 
        '12' : 'l', 
        '13' : 'm', 
        '14' : 'n', 
        '15' : 'o', 
        '16' : 'p', 
        '17' : 'q', 
        '18' : 'r', 
        '19' : 's', 
        '20' : 't', 
        '21' : 'u', 
        '22' : 'v', 
        '23' : 'w', 
        '24' : 'x', 
        '25' : 'y', 
        '26' : 'z'
    }
#Create a list to hold the results of the for loop
code = []
#For loop to go through each character of the original string
for char in encrypt:
    w = int((alphabet1[char])) #Converts each character to an integer position
    x = w + rotation #Adds the rotation to the character position
    if x > 26: #Account for values which exceed 26 to loop back to beginning of alphabet
        x = rotation - (26 - w)
    y = str(x) #Convert new number to a string
    z = (alphabet2[y]) #Use number key to look up new letter
    code.append(z) #Append letter to code list
secret_code =''.join(code) #Clean it up by joining the list characters
print(f'Your secret code is: {secret_code}')

