'''Lab16 Contact List
By Philip Bartoo
11/1/2021'''

import json

class ContactList:
    def __init__(self):
        self.contacts = []

    
    def load(self):
        with open('./Code/Philip/Python/contacts.json', 'r') as f:
            contents = f.read()
            data = json.loads(contents)
            self.contacts = data['contacts']
 
    def count(self):
        count = (len(self.contacts))
        return count
        
    
    def save(self):
        with open('./Code/Philip/Python/contacts.json', 'w') as f:
            dictionary = {}
            dictionary["contacts"] = self.contacts
            #dictionary = {'contacts': self.contacts}
            contents = json.dumps(dictionary, indent=2)
            f.write(contents)
    
    def print(self):
        for x in self.contacts:
            name_print = x['name']
            phone_number_print = x['phone_number']
            email_print = x['email']
            print(f'Name: {name_print}, Phone Number: {phone_number_print}, Email: {email_print}')

    def add(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.new_contact = {}
        self.new_contact['name'] = self.name
        self.new_contact['phone_number'] = self.phone_number
        self.new_contact['email'] = self.email
        self.contacts.append(self.new_contact)

    def remove(self, name):
        for x in self.contacts:
            if x['name'] == name:
                remove = self.contacts.index(x)
        del self.contacts[remove]
    
    def update(self, old_name, new_name, new_phone_number, new_email):
        self.old_name = old_name
        self.new_name = new_name
        self.new_phone_number = new_phone_number
        self.new_email = new_email
        self.updated_contact = {}
        self.updated_contact['name'] = self.new_name
        self.updated_contact['phone_number'] = self.new_phone_number
        self.updated_contact['email'] = self.new_email
        for x in self.contacts:
            if x['name'] == old_name:
                update_index = self.contacts.index(x)
        self.contacts[update_index] = self.updated_contact

contact_list = ContactList() # create an instance of our class
contact_list.load()
print('Welcome to the Contact List App (CLA)')
while True:
    command = input('Enter a command: ')
    if command == 'load':
        contact_list.load()
        print(f'Loaded ${contact_list.count()} contacts.')
    elif command == 'save':
        contact_list.save()
        print(f'Saved ${contact_list.count()} contacts.')
    elif command == 'print':
        contact_list.print()
    elif command == 'add':
        print('Enter info of contact to add:')
        name = input('Name: ')
        phone_number = input('Phone Number: ')
        email = input('Email: ')
        contact_list.add(name, phone_number, email)
    elif command == 'remove':
        name = input('Name of contact to remove: ')
        contact_list.remove(name)
    elif command == 'update':
        print('Enter info of contact to add:')
        old_name = input('Name of contact to update: ')
        new_name = input('New Name: ')
        new_phone_number = input('New Phone Number: ')
        new_email = input('New Email: ')
        contact_list.update(old_name, new_name, new_phone_number, new_email)
    elif command == 'count':
        print(f'There are {contact_list.count()} contacts.')
    elif command == 'help':
        print('Available commands:')
        print('load   - load all contacts from the file')
        print('save   - save contacts to a file')
        print('print  - print all contacts')
        print('add    - add a new contact')
        print('remove - remove a contact')
        print('update - update a contact')
        print('count  - count all contacts')
        print('exit   - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')

            








