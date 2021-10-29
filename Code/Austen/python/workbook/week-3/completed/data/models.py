from utils.importer import importer


class ATM:
  response = importer.response
  validator = response.validate()
  start = ['create account', 'sign-in', 'done']
  transactions = ['check balance', 'deposit', 'withdraw', 'done']
  accounts = []
  recap = []

  def __init__(account, number, password, balance):
    account.number = number
    account.password = password
    account.balance = balance
    account.interest = 0.1

  def newaccount():
    generateid = importer.generateid
    number = generateid.AN4()
    password = input('create a password: ')
    account = ATM(number, password, balance=0)
    message = f'Your account information: \n  account number: {number}\n  password: {password}'
    ATM.accounts.append(account)
    return message

  def login():
    number = input('please enter your account number: ')
    password = input('please enter your password: ')
    for account in ATM.accounts:
      if number == account.number:
        if password == account.password:
          login = True
          break
        else:
          login = False
          account = 'invalid'
      else:
        login = False
        account = 'invalid'
    return login, account

  class transaction:

    def balance(account):
      now = importer.now
      message = f'Your account has a balance of ${account.balance}.'
      stamp = now.standard()
      ATM.recap.append(f'{stamp} - checked balance')
      return message

    def deposit(account):
      now = importer.now
      amount = input('How much would you like to deposit?\n')
      try:
        amount = int(amount)
      except:
        message = 'please enter a valid whole number'
      else:
        account.balance += amount
        message = f'You deposited ${amount}\n Your new account balance is ${account.balance}.'
        stamp = now.standard()
        ATM.recap.append(f'{stamp} - deposited: ${amount}')
      return message

    def withdraw(account):
      now = importer.now
      amount = input('How much would you like to withdraw?\n')
      try:
        amount = int(amount)
      except:
        message = 'please enter a valid whole number'
      else:
        if amount < account.balance:
          account.balance -= amount
          message = f'You withdrew ${amount}\n Your new account balance is ${account.balance}.'
          stamp = now.standard()
          ATM.recap.append(f'{stamp} - withdrew: ${amount}')
        else:
          message = f'Your balance is less than your requested withdrawl.\n balance: ${account.balance}\n withdrawl: ${amount}'
      return message


class Contacts:
  def __init__(list, path):
      list.path = path
      list.file = []
      list.contacts = list.load()
      list.length = len(list.contacts)
      list.trash = []

  class Contact:
    def __init__(contact, data):
      contact.data = data
      contact.name = data['name']
      contact.split = data['name'].split()
      contact.first = contact.split[0]
      contact.middle = contact.split[1]
      contact.last = contact.split[2]
      contact.phone = data['phone_number']
      contact.email = data['email']

  def load(list):
      import json
      file = open(list.path).read()
      contacts = json.loads(file)['contacts']
      list.file = contacts
      formatted = []
      for contact in list.file:
        contact = Contacts.Contact(contact)
        formatted.append(contact)
      contacts = formatted
      return contacts

  def save(list):
      import json
      contacts = {'contacts': list.file, 'trash': list.trash}
      file = open(list.path, 'w')
      contacts = json.dumps(contacts)
      file.write(contacts)

  def print(list, pointer):
    if pointer == 'all':
      for contact in list.contacts:
          contact = f'\nname: {contact.first} {contact.last[0]}.\nphone number: {contact.phone}\nemail: {contact.email}\n'
          print(contact)
      print(f'\n total contacts: {list.length}')
    else:
      contact = pointer
      contact = f'\nname: {contact.first} {contact.last[0]}.\nphone number: {contact.phone}\nemail: {contact.email}\n'
      print(contact)

  def new(list):
      new = input('add new contact?\n')
      while new in importer.yes:
        validator = importer.validator
        name = importer.entry.fullname()
        phone = input('phone number: ')
        phone = validator.phone(phone)
        email = input('email: ')
        email = validator.email(email)
        contact = {'name': name, 'phone_number': phone, 'email': email}
        list.file.append(contact)
        contact = Contacts.Contact(contact)
        list.contacts.append(contact)
        print('added: ')
        list.print(contact)
        new = input('add another?\n')

  def delete(list):
      delete = input('delete contact?\n')
      while delete in importer.yes:
        name = input(
            f'which contact do you want to delete?\ncontact name: ').lower()
        for contact in list.contacts:
          notfound = True
          message = 'there is no contact by that name'
          if name in contact.name.lower():
            entry = contact
            contact = contact.data
            list.trash.append(contact)
            notfound = False
            break
        if notfound == False:
          confirm = input(f'are you sure you want to delete {entry.name}?\n')
          if confirm in importer.yes:
              print('deleted: ')
              list.print(entry)
              list.file.remove(contact)
              list.contacts.remove(entry)
              delete = input('delete another?\n')
        else:
          print(message)

  def update(list):
      update = input('update contact?\n')
      while update in importer.yes:
        validator = importer.validator
        name = input(
            f'which contact do you want to update?\ncontact name: ').lower()
        for contact in list.contacts:
          notfound = True
          message = 'there is no contact by that name'
          if name in contact.name.lower():
            confirm = input(f'update: {contact.name}?\n')
            contact = contact.data
            index = list.file.index(contact)
            file = list.file[index]
            options = ['name', 'phone', 'email', 'done']
            option = input(f'what would you like to update?\n{options}\n')
            option = validator.selection(option, options)
            while option == 'name':
              name = contact['name']
              new_name = importer.entry.fullname()
              contact.update({'name': new_name})
              file.update({'name': new_name})
              option = input(f'what would you like to update?\n{options}\n')
              option = validator.selection(option, options)
            while option == 'phone':
              phone = contact['phone_number']
              new_phone = input('new phone number: ')
              new_phone = validator.phone(new_phone)
              contact.update({'phone_number': new_phone})
              file.update({'phone_number': new_phone})
              option = input(f'what would you like to update?\n{options}\n')
              option = validator.selection(option, options)
            while option == 'email':
              email = contact['email']
              new_email = input('new email address: ')
              new_email = validator.email(new_email)
              contact.update({'email': new_email})
              file.update({'email': new_email})
              option = input(f'what would you like to update?\n{options}\n')
              option = validator.selection(option, options)
            contact = Contacts.Contact(contact)
            print('updated: ')
            list.print(contact)
            update = input('update another contact?\n')
            list.save()
            list.contacts = list.load()
            notfound = False
            break
        else:
          print(message)
