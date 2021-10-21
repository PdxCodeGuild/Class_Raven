encrypt = input('Enter string to encrypt: ')
rotation = int(input('Enter rotation: '))

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
code = []
for char in encrypt:
    w = int((alphabet1[char])) 
    x = w + rotation
    if x > 26:
        x = rotation - (26 - w)
    y = str(x)
    z = (alphabet2[y])
    code.append(z)
secret_code =''.join(code)
print(f'Your secret code is: {secret_code}')

