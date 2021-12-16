def lab_card_validator():
  card = []

  def card_formatter(card_number):
      i = 0
      while len(card_number) > len(card):
          digit = card_number[i]
          digit = int(digit)
          card.append(digit)
          i += 1

  def card_validator():
      counter = 0
      total = 0
      card_id = str(card[12])+str(card[13])+str(card[14])+str(card[15])
      check_digit = card.pop()
      card.reverse()
      while len(card) > counter:
          digit = card.pop(counter)
          digit = digit * 2
          card.insert(counter, digit)
          counter += 2
      for digit in card:
          index = card.index(digit)
          digit = card.pop(digit)
          if digit > 9:
              digit -= 9
          card.insert(index, digit)
      for digit in card:
          total += digit
      total = str(total)
      total = int(total[1])
      if total == check_digit:
          valid = f'Card ending in {card_id} is a valid card number.'
      else:
          valid = f'Card ending in {card_id} is not a valid card number'
      return valid

  def shortcut(example, response):
      if response == 'shortcut':
          card_number = example
      else:
          card_number = response
      return card_number

  def validator():

      example = '1234567890123458'
      print(
          f'Valid example: {example}.\n enter \'shortcut\' to run the example number.')
      response = input('Enter a valid 16 digit card number: \n')
      card_number = shortcut(example, response)
      while len(card_number) != 16:
          response = input(
              'Enter a valid 16-digit card number or \'shortcut\': \n')
          card_number = shortcut(example, response)
      if len(card_number) == 16:
          card_formatter(card_number)
          valid = card_validator()
      return valid