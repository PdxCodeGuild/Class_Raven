import json


def lab17():
  class Contact:
    def __init__(contact, data):
      contact.fullname = data['name'].split()
      contact.name = data['name']
      contact.length = len(contact.name)
      contact.first = contact.fullname[0].lower()
      contact.phone = data['phone_number']
      contact.email = data['email']

  class Contact_List:
    def __init__(contactlist, name, path):
      contactlist.name = name.capitalize()
      contactlist.path = path
      contactlist.contacts = contactlist.load()
      contactlist.count = len(contactlist.contacts)
      contactlist.actions = [
          {'id': '1', 'name': 'display contacts'},
          {'id': '2', 'name': 'new contact'},
          {'id': '3', 'name': 'update contact'},
          {'id': '4', 'name': 'delete contact'},
          {'id': '5', 'name': 'quit'}]

    def load(contactlist):
      file = open(contactlist.path)
      data = file.read()
      data = json.loads(data)
      data = data['contacts']
      contacts = []
      for contact in data:
        contact = Contact(contact)
        contacts.append(contact)
      return contacts

    def print(contactlist):
      print(f'\n {contactlist.name} contacts:\n')
      for contact in contactlist.contacts:
        string = f'\n   {contact.name}\n     {contact.phone}\n     {contact.email}'
        print(string)
      print()
      return

    def new(contactlist):
      import string
      first = input('first name: ').title()
      middle = input('middle name: ').title()
      last = input('last name: ').title()
      name = f'{first} {middle} {last}'
      print('enter "skip" if no phone number')
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
      print('enter "skip" if no email address')
      email = input('email address: ').lower()
      if email != 'skip':
        email_split = email.split('@')
        while len(email_split) != 2:
          print('please enter a valid email address')
          email = input('email address: ').lower()
          email_split = email.split('@')
          if email == 'skip':
            break
        if email != 'skip':
          address = email_split[0]
          domain = email_split[1]
          domain = domain.split('.')
          while len(domain) != 2:
            print('please enter a valid domain')
            domain = input(f'email domain: {address}@ ')
            domain = domain.split('.')
          dot = domain[1]
          domain = domain[0]
          email = f'{address}@{domain}.{dot}'
      if email == 'skip':
        email = ''
      if phone == 'skip':
        phone = ''
      contact = {'name': name, 'phone_number': phone, 'email': email}
      contact = Contact(contact)
      contactlist.contacts.append(contact)
      return

    def update(contactlist):
      import string
      options = [
          {'id': '1', 'name': 'name'},
          {'id': '2', 'name': 'phone'},
          {'id': '3', 'name': 'email'},
          {'id': '4', 'name': 'done'},
      ]
      print('What would you like to update?')
      for option in options:
        number = option['id']
        option = option['name']
        option = f'  #{number} - {option}'
        print(option)
      selection = input('enter the option name or number: ')
      for option in options:
        if selection == option['id']:
          selection = option['name']
      while selection != 'done':
        print('Which contact would you like to update?')
        name = input('enter the contact\'s first name: ').lower()
        for contact in contactlist.contacts:
          found = 'not found'
          if name == contact.first:
            found = contact
            break
        if selection == 'name':
          first = input('first name: ').title()
          middle = input('middle name: ').title()
          last = input('last name: ').title()
          name = f'{first} {middle} {last}'
          found.name = name
        elif selection == 'phone':
          print('enter "remove" if to delete phone number')
          phone = input('phone number: ')
          if phone != 'remove':
            while len(phone) != 10:
              print('please enter the ten digit phone number')
              print('do not include a hyphen or special characters')
              phone = input('phone number: ')
              if phone == 'remove':
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
            found.phone = phone
        elif selection == 'email':
          print('enter "remove" to delete email address')
          email = input('email address: ').lower()
          if email != 'remove':
            email_split = email.split('@')
            while len(email_split) != 2:
              print('please enter a valid email address')
              email = input('email address: ').lower()
              email_split = email.split('@')
              if email == 'remove':
                break
            if email != 'remove':
              address = email_split[0]
              domain = email_split[1]
              domain = domain.split('.')
              while len(domain) != 2:
                print('please enter a valid domain')
                domain = input(f'email domain: {address}@ ')
                domain = domain.split('.')
              dot = domain[1]
              domain = domain[0]
              email = f'{address}@{domain}.{dot}'
              found.email = email
        selection = input('enter the option name or number: ')
        for option in options:
          if selection == option['id']:
            selection = option['name']
      return

    def delete(contactlist):
      print('Which contact would you like to delete?')
      name = input('enter the contact\'s first name: ').lower()
      for contact in contactlist.contacts:
        found = 'not found'
        if name == contact.first:
          found = contact
          index = contactlist.contacts.index(found)
          break
      print(f'Are you sure you want to delete {found.name}?')
      confirmation = input('enter yes or no: ')
      if confirmation == 'yes':
          contact = contactlist.contacts.pop(index)
      return

    def save(contactlist):
      import json
      contacts = []
      for contact in contactlist.contacts:
        contact = {'name': contact.name,
                   'phone_number': contact.phone, 'email': contact.email}
        contacts.append(contact)
      contacts = {'contacts': contacts}
      file = open(contactlist.path, 'w')
      contacts = json.dumps(contacts)
      file.write(contacts)
      return

  contactlists = [{'name': 'work', 'file': 'storage/contacts.json'},
                  {'name': 'empty', 'file': 'storage/empty.json'}]
  print()
  print('Which contact list would you like to access?')
  for contactlist in contactlists:
    print('    ', contactlist['name'])
  print()
  selection = input('enter the list name: ')
  for contactlist in contactlists:
    name = 'not found'
    file = 'not found'
    if selection == contactlist['name']:
      name = selection
      file = contactlist['file']
      break
  try:
    contacts = Contact_List(name, file)
  except:
    print(f'{selection} not found')
  else:
    print()
    print(contacts.name, f': {contacts.count} contacts')
    print()
    for action in contacts.actions:
      number = action['id']
      action = action['name']
      option = f'  #{number} - {action}'
      print(option)
    print()
    selection = input('enter the action name or number: ')
    for action in contacts.actions:
      if selection == action['id']:
        selection = action['name']
    while selection != 'quit':
      if selection == 'display contacts':
        contacts.print()
      elif selection == 'new contact':
        contacts.new()
        contacts.print()
      elif selection == 'update contact':
        contacts.update()
        contacts.print()
      elif selection == 'delete contact':
        contacts.delete()
        contacts.print()
      print()
      selection = input('enter the action name or number: ')
      for action in contacts.actions:
        if selection == action['id']:
          selection = action['name']
    contacts.save()


lab17()
