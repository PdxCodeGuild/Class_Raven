
print('\nLets convert dollars to coins \n please enter a number: ')
coins = [
    {'singular': 'dollar coin', 'plural': 'dollar coins', 'worth': 1},
    {'singular': 'half-dollar coin',
     'plural': 'half-dollar coins', 'worth': .5},
    {'singular': 'quarter', 'plural': 'quarters', 'worth': .25},
    {'singular': 'dime', 'plural': 'dimes', 'worth': .1},
    {'singular': 'nickle', 'plural': 'nickles', 'worth': .05},
    {'singular': 'penny', 'plural': 'pennies', 'worth': .01},
]
message_pieces = [f'Your change is: ']


def coin_exchange(balance, multiplier):
  result = balance // multiplier
  return result


def new_balance(balance, result, multiplier):
  new_balance = balance - (result * multiplier)
  new_balance = round(new_balance, 2)
  return new_balance


def piece_formatter(result, coin):
  if result == 1:
    name = coin['singular']
  elif result > 1:
    name = coin['plural']
  message_pieces.append(f'{int(result)} {name}')


def message_formatter():
  formatted_message = f''
  counter = 1
  while len(message_pieces) > 0:
    for item in message_pieces:
      item = message_pieces.pop(0)
      last = False
      if len(message_pieces) == 0:
        last = True
        formatted_message += ', and ' + item + '.'
        break
      while not last:
        if counter < 3:
          formatted_message += item
          break
        elif counter > 2:
          formatted_message += ', ' + item
          break
        counter += 1
  return formatted_message


def changer():
  balance = input()
  while True:
    try:
      float(balance)
    except:
      print('please enter a valid number')
      balance = input()
    else:
      balance = float(balance)
      balance = round(balance, 2)

    for coin in coins:
      multiplier = coin['worth']
      result = coin_exchange(balance, multiplier)
      balance = new_balance(balance, result, multiplier)
      if result > 0:
        piece_formatter(result, coin)
      message = message_formatter()
      return message
      break
