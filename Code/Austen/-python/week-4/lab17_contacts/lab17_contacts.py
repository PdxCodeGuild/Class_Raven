from models.Contact import Contact
from models.Contact_List import Contact_List


lists = [{'name': 'default', 'file': 'storage/contacts.json'}]
if len(lists) > 1:
  print('Which contact list would you like to access?')
  for contactlist in lists:
    print(contactlist['name'])
  selection = input('enter the list name: ')
  for contactlist in lists:
    name = 'not found'
    file = 'not found'
    if selection == contactlist['name']:
      name = selection
      file = contactlist['file']
      break
else:
  selection = lists[0]
  name = selection['name']
  file = selection['file']
try:
  contacts = Contact_List(name, file)
except:
  print(f'{selection} not found')
else:
  print(contacts.name, f': {contacts.count} contacts')
  options = contacts.actions['main menu']
  for option in options:
    print(option['id'], option['name'])
  selection = input('enter the action name or number: ')
  selection = contacts.select(selection, options)
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
    selection = input('enter the action name or number: ')
    selection = contacts.select(selection, options)
  contacts.save()
