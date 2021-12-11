class response:
  class polar:
    yes = ['yes', 'yep', 'sure']
    no = ['no', 'nope', 'nah']
    valid = yes + no

  class entry:
    def fullname():
        first = input('first name: ').capitalize()
        middle = input('middle initial: ').capitalize()
        middle = f'{middle[0]}.'
        last = input('last name: ').capitalize()
        name = f'{first} {middle} {last}'
        return name

  class validate:
    def characters(selection, option):
        characters = list(selection)
        counter = 0
        option = option.lower()
        for char in characters:
          if char in option:
            counter += 1
          elif char == ' ':
            counter += 1
        if counter == len(characters):
            option = True
        else:
            option = False
        return option

    def selection(validate, option, options):
      characters = response.validate.characters
      for entry in options:
        matched = characters(option, entry)
        if matched == True:
          selection = entry
      return selection

    def phone(validator, phone_number):
      phone = phone_number
      if phone != '':
        integers = 0
        while integers != 10:
          number = ''
          for char in phone:
            try:
              int(char)
            except:
              integers += 0
            else:
              integers += 1
          if integers != 10:
            integers = 0
            print('please enter a valid 10 digit phone number')
            phone = input('phone number: ')
        counter = 0
        for char in phone:
          try:
            int(char)
          except:
            ''
          else:
            integers += 1
            if counter == 3:
              char = f'-{char}'
            elif counter == 6:
              char = f'-{char}'
            number += char
            counter += 1
        phone = number
      return phone

    def email(validator, address):
      if address != '':
        required = ['@', '.']
        valid = False
        while valid == False:
          valid = True
          for char in required:
            if char not in address:
              valid = False
              print('please enter a valid email address')
              print(f'"{address}" is not valid')
              address = input('email: ')
      return address
