def lab_averages():
  def v1():
    numbers = [5, 0, 8, 3, 4, 1, 6]
    total = 0
    for number in numbers:
      total += number
    average = total / len(numbers)
    average = round(average, 2)
    message = f'Your average is: {average}'
    return message

  def v2():
    print('\n (enter done to see average or quit to exit.)')
    stop = ['quit', 'done']
    numbers = []
    total = 0
    response = input('Enter a number: \n')
    while response not in stop:
      try:
        number = float(response)
      except:
        print('invalid')
        response = input('Enter done, quit, or a number: \n')
      else:
        numbers.append(number)
        response = input('Enter a number: \n')
      if response == 'quit':
        print('Goodbye.')
      elif response == 'done':
        for number in numbers:
          total += number
        if total == 0:
          average = 0
        elif total > 0:
          average = total / len(numbers)
          average = round(average, 2)
        message = f'Your average is: {average}'
    return message


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


def lab_palindromes():
  def is_palindrome(letters, reversed):
      reversed.reverse()
      if letters == reversed:
          palindrome = 'is'
      else:
          palindrome = 'is not'
      return palindrome

  def check_palindrome():
      letters = []
      reversed = []
      response = input('Enter a word: \n').lower()
      i = 0
      while len(response) > len(letters):
          letter = response[i]
          letters.append(letter)
          reversed.append(letter)
          i += 1
      palindrome = is_palindrome(letters, reversed)
      message = f'{response.capitalize()} {palindrome} a palindrome.'
      return message


def lab_anagrams():
  messages = {
      'invalid': 5 * '\n Invalid response.',
      'false': 'These words are not anagrams. \n',
      'true': 'These words are anagrams! \n',
  }

  def check_anagram():
      def prompt(string):
          query = f'\nEnter the {string} word: '
          response = input(f'{query}')
          return response.lower()

      def string_validator(string):
          while string.isalpha() == False:
              print('Please only use characters of the alphabet.')
              string = prompt()
          return string

      string_1 = prompt('first')
      string_1 = string_validator(string_1)
      string_2 = prompt('second')
      string_2 = string_validator(string_2)
      print(f'\n Your words are {string_1} and {string_2}. \n')
      list_1 = list(string_1)
      list_1.sort()
      list_2 = list(string_2)
      list_2.sort()
      if list_1 == list_2:
          anagram = messages['true']
      elif list_1 != list_2:
          anagram = messages['false']
      else:
          print(messages['invalid'])
      return anagram
