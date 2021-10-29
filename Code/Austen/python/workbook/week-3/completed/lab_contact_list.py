from utils.importer import importer
from data.models import Contacts


def lab_contacts_list():
  validator = importer.validator
  path = 'data/lab_contact_list.json'
  contact_list = Contacts(path)
  options = ['see contacts', 'new contact',
             'update contact', 'delete contact', 'quit']
  message = '\nwhat would you like to do?\n'
  for option in options:
    message += f'{option}\n'
  action = input(message)
  action = validator.selection(action, options)
  while action != options[4]:
    if action == options[0]:
      contact_list.print('all')
      action = input(message)
      action = validator.selection(action, options)
    if action == options[1]:
      contact_list.new()
      action = input(message)
      action = validator.selection(action, options)
    if action == options[2]:
      contact_list.update()
      action = input(message)
      action = validator.selection(action, options)
    if action == options[3]:
      contact_list.delete()
      action = input(message)
      action = validator.selection(action, options)
  clear = input(
      'clear the trash(enter yes) or save it just in case(enter no)?\n')
  if clear in importer.yes:
    contact_list.trash.clear()
  contact_list.save()
  print('contacts saved...')
  print('\ngood bye\n')


lab_contacts_list()
