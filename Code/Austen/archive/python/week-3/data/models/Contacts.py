from utils.importer import importer
from data.models import Contact
responses = importer('responses', 'response')
statement = responses.get_statement()
response = ''
exec(statement)


class List:
  def __init__(list, path):
      list.path = path
      list.file = list.loadfile()
      list.contacts = list.formatfile()
      list.length = len(list.contacts)
      list.trash = []
# *Methods that return a variable:

  def loadfile(list):
    import json
    file = open(list.path).read()
    contacts = json.loads(file)['contacts']
    return contacts

  def formatfile(list):
    formatted = []
    for contact in list.file:
      contact = Contact.info(contact)
      formatted.append(contact)
    contacts = formatted
    return contacts

  def contact_string(list, contact):
    string = f'\nname: {contact.first} {contact.last[0]}.\nphone number: {contact.phone}\nemail: {contact.email}\n'
    return string

  def update_name(list, contact, file, validator, options):
    name = contact['name']
    new_name = response.entry.fullname()
    contact.update({'name': new_name})
    file.update({'name': new_name})
    option = input(f'what would you like to update?\n{options}\n')
    option = validator.selection(option, options)
    return option

  def update_phone(list, contact, file, validator, options):
    phone = contact['phone_number']
    new_phone = input('new phone number: ')
    new_phone = validator.phone(new_phone)
    contact.update({'phone_number': new_phone})
    file.update({'phone_number': new_phone})
    option = input(f'what would you like to update?\n{options}\n')
    option = validator.selection(option, options)
    return option

  def update_email(list, contact, file, validator, options):
    email = contact['email']
    new_email = input('new email address: ')
    new_email = validator.email(new_email)
    contact.update({'email': new_email})
    file.update({'email': new_email})
    option = input(f'what would you like to update?\n{options}\n')
    option = validator.selection(option, options)
    return option
# *Methods that execute without returning

  def save(list):
    import json
    contacts = {'contacts': list.file, 'trash': list.trash}
    file = open(list.path, 'w')
    contacts = json.dumps(contacts)
    file.write(contacts)

  def print(list, contact):
    if contact == 'all':
      for contact in list.contacts:
          string = list.contact_string(contact)
          print(string)
      print(f'\n total contacts: {list.length}')
    else:
      string = list.contact_string(contact)
      print(string)

  def new(list):
      new = input('add new contact?\n')
      while new in response.polar.yes:
        validator = response.validate()
        name = response.entry.fullname()
        phone = input('phone number: ')
        phone = validator.phone(phone)
        email = input('email: ')
        email = validator.email(email)
        contact = {'name': name, 'phone_number': phone, 'email': email}
        list.file.append(contact)
        contact = Contact.info(contact)
        list.contacts.append(contact)
        print('added: ')
        list.print(contact)
        new = input('add another?\n')

  def delete(list):
      delete = input('delete contact?\n')
      while delete in response.polar.yes:
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
          if confirm in response.polar.yes:
              print('deleted: ')
              list.print(entry)
              list.file.remove(contact)
              list.contacts.remove(entry)
              delete = input('delete another?\n')
        else:
          print(message)

  def update(list):
      update = input('update contact?\n')
      while update in response.polar.yes:
        validator = response.validate()
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
              option = list.update_name(contact, file, validator, options)
            while option == 'phone':
              option = list.update_phone(contact, file, validator, options)
            while option == 'email':
              option = list.update_email(contact, file, validator, options)
            contact = Contact.info(contact)
            print('updated: ')
            list.print(contact)
            update = input('update another contact?\n')
            list.save()
            list.contacts = list.load()
            notfound = False
            break
        else:
          print(message)
