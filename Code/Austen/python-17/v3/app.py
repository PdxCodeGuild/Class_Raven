from methods import ContactList

contacts = ContactList() # create an instance of our class
print('Welcome to your Contact List.')
while True:
    options = ['display', 'add', 'update', 'remove', 'quit']
    print('What would you like to do?')
    for option in options:
      print(option)
    command = input('Enter a command: ')
    if command == 'display':
        contacts.print()
    elif command == 'add':
        print('Enter info of contact to add:')
        name = input('Name: ')
        phone = input('Phone Number: ')
        email = input('Email: ')
        contacts.add(name, phone, email)
    elif command == 'remove':
        name = input('Name of contact to remove: ')
        contacts.remove(name)
    elif command == 'update':
        print('Which contact would you like to update?')
        for contact in contacts.contacts:
          print(contact['name'])
        name = input('enter their current full name (case-sensitive): ')
        print('If field doesn\'t need to be updated enter "skip"')
        for contact in contacts.contacts:
          if contact['name'] == name:
            found = contact
            break
        new_name = input('New Name: ')
        if new_name == "skip":
          new_name = found['name']
        new_phone = input('New Phone Number: ')
        if new_phone == "skip":
          new_phone = found['phone_number']
        new_email = input('New Email: ')
        if new_email == "skip":
          new_email = found['email']
        new_data = {'name': new_name, 'phone': new_phone, 'email': new_email}
        contacts.update(name, new_data)
    elif command == 'quit':
      contacts.save()
      print('all changes saved')
      print('good-bye')
      break
    else:
        print('Command not recognized')
