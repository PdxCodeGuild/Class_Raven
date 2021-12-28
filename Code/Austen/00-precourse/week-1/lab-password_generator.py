import string
import random
print('Would you like to generate a password?')
response = input('Please enter: "yes" or "no": ')
print('')
if response == 'no':
  print('ok bye')
elif response == 'yes':
  letters = string.ascii_lowercase
  caps = string.ascii_uppercase
  special = string.punctuation
  digits = string.digits
  options = letters + caps + special + digits
  password = []
  print('')
  print('Would you like to specify the length?')
  response = input('Please enter: "yes" or "no": ')
  print('')
  if response == 'no':
    passlength = 10
  elif response == 'yes':
    response = input('Please enter the desired length: ')
    passlength = int(response)
  print('')
  print('Would you like to specify the character types?')
  print('(This only allows you to set minimums within each group.)')
  response = input('Please enter: "yes" or "no": ')
  if response == 'no':
    print('Your password will be randmonly selected from the following list of characters' + ''.join(options))
    print('')
    password = []
    while len(password) < passlength:
      char = random.choice(options)
      password.append(char)
  elif response == 'yes':
    og_passlength = passlength
    lowers = []
    print('Your password will be ' + str(passlength) + 'characters long.')
    print('How many should be lower case letters?')
    print('')
    print(''.join(letters))
    print('0 - ' + str(passlength))
    response = input('response: ')
    passlength -= int(response)
    while len(lowers) < int(response):
      letter = random.choice(letters)
      lowers.append(letter)
      print(lowers)
    print('How many should be upper case letters?')
    print('')
    print(''.join(caps))
    print('0 - ' + str(passlength))
    response = input('response: ')
    passlength -= int(response)
    pcaps = []
    while len(pcaps) < int(response):
        cap = random.choice(caps)
        pcaps.append(cap)
        print(pcaps)
    print('How many should be numbers?')
    print('')
    print(''.join(digits))
    print('0 - ' + str(passlength))
    response = input('response: ')
    passlength -= int(response)
    numbers = []
    while len(numbers) < int(response):
      digit = random.choice(digits)
      numbers.append(digit)
      print(numbers)
    print('How many should be special characters?')
    print('')
    print(''.join(special))
    print('0 - ' + str(passlength))
    response = input('response: ')
    passlength -= int(response)
    specials = []
    while len(specials) < int(response):
      spec = random.choice(special)
      specials.append(spec)
      print(specials)
    password = lowers + pcaps + numbers + specials
    if len(password) < og_passlength:
      while len(password) < og_passlength:
        char = random.choice(options)
        password.append(char) 
    print('Your password will be configured from this randmonly selected set of characters: ' + ''.join(password))
    random.shuffle(password)
  print('')
  print('')
  print('Your password is: ' + ''.join(password))
  print('')
  print('')
  print('Thanks for using my password generator!')
  print('')
  print('')