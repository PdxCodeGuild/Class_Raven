import random
options = ['rock', 'paper', 'scissors']
player = input('Hello, and welcome. What is your name?: ')
message = 'Thank you, ' + player + '. You are now ready to begin.'
print(message)
message = 'The rules are simple. Pick the correct item and you wont be murdered.'
print(message)
message = 'Your choices are:'
print(message)
for option in options:
  print(option)
player_selection = input('Please enter in your choice now: ')
message = player + ' has selected: ' + player_selection + '.'
print(message)
computer_selection = random.choice(options)
print('The computer has selected: ' + computer_selection + '.')
if player_selection == 'rock':
  winner = 'paper'
  loser = 'scissors'
elif player_selection == 'paper':
  winner = 'scissors'
  loser = 'rock'
elif player_selection == 'scissors':
  winner = 'rock'
  loser = 'paper'
else:
  winner = 'invalid'
  loser = 'invalid'
if player_selection == computer_selection:
  result = 'There will be no killing today, in this time of peace.'
elif computer_selection == winner:
  result = 'Congratulations! You will now be brutally murdered with a ' + computer_selection + '.' + ' Have fun, ' + player + '!'
elif computer_selection == loser:
  result = 'You may now assault your computer with a ' + player_selection +', ' + player + '.'
else:
  first = random.choice(options)
  second = random.choice(options)
  third = random.choice(options)
  result = 'Due to improperly followed instructions; you will now be angrily murdered with: ' + first + ', then,' + second + ', and then finally, ' + third + '. Thanks for playing, ' + player + '!'
print(result)
