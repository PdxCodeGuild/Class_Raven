from models.Contact import Contact


class Contact_List:
  def __init__(contactlist, name, path):
    contactlist.name = name.capitalize()
    contactlist.path = path
    contactlist.contacts = contactlist.load()
    contactlist.count = len(contactlist.contacts)
    contactlist.actions = {
        'main menu': [{'id': '1', 'name': 'display contacts'},
                      {'id': '2', 'name': 'new contact'},
                      {'id': '3', 'name': 'update contact'},
                      {'id': '4', 'name': 'delete contact'},
                      {'id': '5', 'name': 'quit'}],
        'update': [{'id': '1', 'name': 'name'},
                   {'id': '2', 'name': 'phone'},
                   {'id': '3', 'name': 'email'},
                   {'id': '4', 'name': 'done'}, ]
    }

  def load(contactlist):
    import json
    file = open(contactlist.path)
    data = file.read()
    data = json.loads(data)
    data = data['contacts']
    contacts = []
    for contact in data:
      contact = Contact(contact)
      contacts.append(contact)
    return contacts

  def save(contactlist):
    import json
    contacts = []
    for contact in contactlist.contacts:
      contact = {'name': contact.name,
                 'phone_number': contact.phone, 'email': contact.email}
      contacts.append(contact)
    contacts = {'contacts': contacts}
    try:
      file = open(contactlist.path, 'w')
      contacts = json.dumps(contacts)
      file.write(contacts)
    except:
      result = 'error when saving contacts'
    else:
      result = 'contacts saved'
    return result

  def find(contactlist):
    name = input('enter the contact\'s first name: ').lower()
    for contact in contactlist.contacts:
      found = 'not found'
      if name == contact.first:
        found = contact
        break
    return found

  def select(contactlist, selection, options):
    for option in options:
      if selection == option['id']:
        selection = option['name']
        break
      elif selection in option['name']:
        selection = option['name']
        break
    return selection

  def print(contactlist):
    for contact in contactlist.contacts:
      contact = Contact.print(contact)
      print(contact)

  def new(contactlist):
    import string
    name = Contact.enter_name()
    phone = Contact.enter_phone()
    email = Contact.enter_email()
    contact = {'name': name, 'phone_number': phone, 'email': email}
    contact = Contact(contact)
    contactlist.contacts.append(contact)
    return

  def update(contactlist):
    print('What would you like to update?')
    options = contactlist.actions['update']
    for option in options:
      print('  ', option['id'], option['name'])
    selection = input(
        'Enter 4 or "done" when finished updating.\nenter the option name or number: ')
    selection = contactlist.select(selection, options)
    while selection != 'done':
      print('Which contact would you like to update?')
      found = contactlist.find()
      if selection == 'name':
        name = Contact.enter_name()
        found.name = name
      elif selection == 'phone':
        phone = Contact.enter_phone()
        found.phone = phone
      elif selection == 'email':
        email = Contact.enter_email()
        found.email = email
      selection = input(
          'Enter 4 or "done" when finished updating\nenter the option name or number: ')
      selection = contactlist.select(selection, options)
    contact = Contact.print(found)
    return contact

  def delete(contactlist):
    print('Which contact would you like to delete?')
    found = contactlist.find()
    index = contactlist.contacts.index(found)
    print(f'Are you sure you want to delete {found.name}?')
    confirmation = input('enter yes or no: ')
    if confirmation == 'yes':
      contact = contactlist.contacts.pop(index)
    return contact
