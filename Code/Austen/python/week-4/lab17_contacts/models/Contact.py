class Contact:
  def __init__(contact, data):
    contact.fullname = data['name'].split()
    contact.name = data['name']
    contact.length = len(contact.name)
    contact.first = contact.fullname[0].lower()
    contact.phone = data['phone_number']
    contact.email = data['email']

  def enter_name():
    first = input('first name: ').title()
    middle = input('middle name: ').title()
    last = input('last name: ').title()
    name = f'{first} {middle} {last}'
    return name

  def enter_phone():
    import string
    print('enter "skip" if no phone number or to delete an existing phone number')
    phone = input('phone number: ')
    if phone != 'skip':
      while len(phone) != 10:
        print('please enter the ten digit phone number')
        print('do not include a hyphen or special characters')
        phone = input('phone number: ')
        if phone == 'skip':
          break
      formatted = ''
      for digit in phone:
        if digit in string.digits:
          formatted += digit
        if len(formatted) == 3:
          formatted += '-'
        elif len(formatted) == 7:
          formatted += '-'
      phone = formatted
    elif phone == 'skip':
      phone = ''
    return phone

  def enter_email():
    print('enter "skip" if no email address or to delete an existing email address')
    email = input('email address: ').lower()
    if email != 'skip':
      email = email.split('@')
      while len(email) != 2:
        print('please enter a valid email address')
        email = input('email address: ').lower()
        email = email.split('@')
        if email == 'skip':
          break
      if email != 'skip':
        address = email[0]
        domain = email[1]
        domain = domain.split('.')
        while len(domain) != 2:
          print('please enter a valid domain')
          domain = input(f'email domain: {address}@ ')
          domain = domain.split('.')
        dot = domain[1]
        domain = domain[0]
        email = f'{address}@{domain}.{dot}'
    elif email == 'skip':
      email = ''
    return email

  def print(contact):
    contact = f'\n   {contact.name}\n     {contact.phone}\n     {contact.email}'
    return contact
