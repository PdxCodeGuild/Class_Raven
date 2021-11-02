"""
PDX Code Guild Full Stack Bootcamp
->Lab 17
  Contact List
Michael B

Contact List
Let's write class for managing a contact list. Copy the code below into a file and fill in the functions. Save the following files below to your personal code folder. To open the file, look at the File IO doc, to parse the JSON into a Python dictionary, look at json module.

contacts.json

{
    "contacts": [{
        "name": "Dora M. Smith",
        "phone_number": "919-781-7129",
        "email": "doramsmith@hotmail.com"
    },{
        "name": "Annette D. Berube",
        "phone_number": "662-319-6954",
        "email": "annette@gmail.com"
    },{
        "name": "Austin M. Pigott",
        "phone_number": "478-777-8878",
        "email": "austin@aol.com"
    }]
}
lab17_contact_list.py

class ContactList:
    
    def __init__(self):
        self.contacts = []

    def load(self):
        # 1) open 'contacts.json' with option 'r' for read
        # 2) get the text from the file
        # 3) convert the text into a python dictionary (json.loads)
        # 4) get the list of contacts out of the dictionary
        # 5) assign the list of dictionaries to self.contacts
        ...
    
    def count(self):
        # return the length of self.contacts
        ...
    
    def save(self):
        # 1) open 'contacts.json' with open 'w' for write
        # 2) put self.contacts in a dictionary with the key 'contacts'
        # 3) convert the dictionary to a json string (json.dumps)
        # 4) write the json string to the file
        ...

    def print(self):
        # loop over self.contacts
        # print the information for each contact on a separate line
        ...

    def add(self, name, phone_number, email):
        # create a new dictionary using the 3 parameters
        # add the new dictionary to self.contacts
        ...
    
    def remove(self, name):
        # find the contact in self-contacts with the given name
        # remove the element at that index
        ...
    
    def update(self, old_name, new_name, new_phone_number, new_email):
        # find the contact in self.contacts with the given old_name
        # set that contacts' name, phone number, etc to the given values
        ...
    
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
    elif command == 'help':
        print('Available commands:')
        print('load   - load all contacts from the file')
        print('save   - save contacts to a file')
        print('print  - print all contacts')
        print('add    - add a new contact')
        print('remove - remove a contact')
        print('update - update a contact')
        print('exit   - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')

"""


import json

class ContactList:
    def __init__(self):
        self.contacts = [] # Initialize the list of contacts.
        
    def load(self):
        try:
            with open('contacts.json', 'r') as f: # Open the file for reading.
                self.contacts = json.load(f)['contacts'] # Load the list of contacts from the file.
                return True
        except FileNotFoundError: # If the file does not exist.
            return False
        
    @property    
    def count(self):
        return len(self.contacts) # Return the number of contacts.
    
    def save(self):
        with open('contacts.json', 'w') as f: # Open the file for writing.
            json.dump({'contacts': self.contacts}, f) # Save the list of contacts to the file.
    
    def print(self):
        for contact in self.contacts: # Loop over the list of contacts.
            print(f'Name: {contact["name"]}')
            print(f'Phone Number: {contact["phone_number"]}')
            print(f'Email: {contact["email"]}')
            print()
            
    def add(self, name, phone_number, email):
        self.contacts.append({
            'name': name,
            'phone_number': phone_number,
            'email': email
        }) # Add a new contact to the list.
    
    def remove(self, name):
        for contact in self.contacts: # Loop over the list of contacts.
            if contact['name'] == name: # If the contact's name matches the given name.
                self.contacts.pop(self.contacts.index(contact)) # Remove the contact from the list.
                return True
        return False
        
    def update(self, old_name, new_name, new_phone_number, new_email):
        for contact in self.contacts: # Loop over the list of contacts.
            if contact['name'] == old_name: # If the contact's name matches the given name.
                contact['name'] = new_name
                contact['phone_number'] = new_phone_number
                contact['email'] = new_email
                return True
        return False

    def check_if_in_list(self, name):
        for contact in self.contacts: # Loop over the list of contacts.
            if contact['name'] == name: # If the contact's name matches the given name.
                return True
        return False

    def __str__(self):
        return f'{self.__class__.__name__}({self.contacts})' # Return a string representation of the object.
    
    

if __name__ == '__main__': # If this file is being run as a script.
    valid_command = False
    contact_list = ContactList() # create an instance of our class.
    print('\nWelcome to the Contact List App (CLA)!\n')
    
    while not valid_command: # Loop until the user enters a valid command.
        command = input('Enter a command (help for list of commands): ')
        match command.split(): # Split the command into a list of words.
            case ['load']: # If the command is 'load'.
                success = contact_list.load()
                if success:
                    print(f'\nLoaded {contact_list.count} contacts.\n')
                else:
                    print('\nNo contacts file found.\n')
            case ['save']: # If the command is 'save'.
                if contact_list.count == 0: # If there are no contacts.
                    print('\nNo contacts to save.\n')
                else:
                    contact_list.save()
                    print(f'\nSaved {contact_list.count} contacts.\n')
            case ['print'|'p'|'list'|'ls'|'l']: # If the command is 'print' or 'p' or 'list' or 'ls' or 'l'.
                if contact_list.count == 0: # If there are no contacts.
                    print('\nNo contacts to print.\n')
                else:
                    contact_list.print()
            case ['add'|'+']: # Add a new contact.
                print('\nEnter info of contact to add:')
                name = input('Name: ')
                phone_number = input('Phone Number: ')
                email = input('Email: ')
                contact_list.add(name, phone_number, email)
            case ['remove'|'delete'|'del'|'rm'|'rem'|'-']: # If the command is 'remove' or 'delete' or 'del' or 'rm' or 'rem' or '-'.
                name = input('\nName of contact to remove: ')
                success = contact_list.remove(name)
                if success:
                    print('Contact removed')
                else:
                    print('Contact not found')
            case ['update'|'edit'|'change']: # If the command is 'update' or 'edit' or 'change'.
                print('\nEnter info of contact to add:')
                old_name = input('Name of contact to update: ')
                success = contact_list.check_if_in_list(old_name)
                if success:  
                    new_name = input('New Name: ')
                    new_phone_number = input('New Phone Number: ')
                    new_email = input('New Email: ')
                    success = contact_list.update(old_name, new_name, new_phone_number, new_email)
                    if success:
                        print('Contact updated')
                else:
                    print('Contact not found')
            case ['help'|'h'|'?']: # If the command is 'help' or 'h' or '?'.
                #Dictionary of commands and their descriptions.
                commands = {
                    'load': 'Load all contacts from the file',
                    'save': 'Save contacts to a file',
                    'print': 'Print all contacts',
                    'add': 'Add a new contact',
                    'remove': 'Remove a contact',
                    'update': 'Update a contact',
                    'exit': 'Exit the program'}
                print('\nAvailable commands:')
                for command in commands: # Loop over the dictionary of commands.
                    print(f'{command} - {commands[command]}') # Print the command and its description.
                print()
            case ['exit'|'q'|'quit']: # If the command is 'exit' or 'q' or 'quit'.
                print(contact_list) # Print the contact list.
                quit()
            case unknown_command: # If the command is not recognized.
                print(f'Command {unknown_command} not recognized.')
                valid_command = False
