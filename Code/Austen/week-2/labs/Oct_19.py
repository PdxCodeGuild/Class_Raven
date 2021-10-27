def lab_blackjack():
  deck = ['A', '2', '3', '4', '5', '6',
          '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2', '3', '4', '5', '6',
          '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2', '3', '4', '5', '6',
          '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2', '3', '4', '5', '6',
          '7', '8', '9', '10', 'J', 'Q', 'K', ]
  options = ['hit', 'stay']
  yes = ['yes', 'y', 'sure']
  no = ['no', 'n', 'nope']
  validyn = []
  for y in yes:
    validyn.append(y)
  for n in no:
    validyn.append(n)

  def getcard():
    from random import choice
    card = choice(deck)
    index = deck.index(card)
    deck.pop(index)
    print(f'cards remaining: {len(deck)}')
    return card

  def gethand():
    hand = []
    card = getcard()
    if card != 'invalid':
      hand.append(card)
    card = getcard()
    if card != 'invalid':
      hand.append(card)
    return hand

  def getvalue(hand):
    value = 0
    aces = []
    for card in hand:
      while True:
        try:
          int(card)
        except:
          if card == 'A':
            value += 1
            ace = card
            aces.append(ace)
            break
          else:
            value += 10
            break
        else:
          card = int(card)
          value += card
          break
    for ace in aces:
      value += 10
      if value > 21:
        value -= 10
    return value

  def getadvise(hand):
    if len(hand) >= 2:
      value = getvalue(hand)
      print(f'hand value: {value}')
      if value < 17:
        advise = 'hit.'
      elif value < 21:
        advise = 'stay.'
      elif value == 21:
        advise = 'stay. You have blackjack!'
      else:
        advise = 'busted'
    else:
      advise = 'invalid hand'
    return advise

  def start():
    hand = gethand()
    print(f'your hand: {hand}')
    advise = getadvise(hand)
    print(f'you should probably: {advise}')
    print(options)
    choice = input('what would you like to do?\n')
    while choice not in options:
      print(options)
      choice = input('what would you like to do?\n')
    return choice, hand

  def hit(hand):
    card = getcard()
    hand.append(card)
    return hand
  opponent = gethand()
  result = start()
  choice = result[0]
  hand = result[1]
  while choice == 'hit':
    hand = hit(hand)
    print(f'your hand: {hand}')
    advise = getadvise(hand)
    if advise == 'busted':
      print('busted'.upper())
      result = 'busted'
      break
    print(f'you should probably: {advise}')
    print(options)
    choice = input('what would you like to do?\n')
  if choice == 'stay':
    value = getvalue(opponent)
    cards = hand
    hand = getvalue(hand)
    if hand > value:
      print(f'Your {cards} beat {opponent}.')
      print(f'You win!')
      result = 'win'
    elif hand == value:
      print(f'Your {cards} match {opponent}.')
      print('tie')
      result = 'tie'
    else:
      print(f'{opponent} beat your {cards}.')
      print('You lost.')
      result = 'lost'
  return result
