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