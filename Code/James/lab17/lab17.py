import json

# with open(r'C:/Users/james/Class_Raven/Code/James/contact_list.txt') as json_file:
#     data = json.load(json_file)


# print(data)


class ContactList:
    def __init__(self):
        self.contacts = []

    def load(self):
        with open(r'contacts.json', 'r') as contacts_file:
            
            contents = json.load(contacts_file) #got the file back as a python dictionary
            #print(data) # data is a python dictionary at this point
            contacts = contents['contacts']# get the list of contacts out of the contacts dictionary. 
            #print(list_contacts) #this is a list of the dictionary.
            
            self.contacts = contacts
        ...
    @property # changed to a property so I dont need () in the repl
    def count(self):
        return len(self.contacts)
        
        ...
    
    def save(self):
        with open('contacts.json', 'w') as contacts_file:
            # put self.contacts in a dictionary with the key 'contacts'
            contacts_dict = {
                'contacts': self.contacts
            }
            # convert the dictionary to a json string (json.dumps)
            contents = json.dumps(contacts_dict, indent=2)
            # write the json string to the file
            contacts_file.write(contents)
        
        
        ...

    def print(self):
        for contact in self.contacts:
        
            display = (
                    f"Name: {contact['name']}\n"
                    f"Phone: {contact['phone_number']}\n"
                    f"Email: {contact['email']}\n"
                )
            print(display)
        
        ...

    def add(self, name, phone_number, email):
        
        # searches with the input givin in the terminal to append to the contacts list.
        self.contacts.append({
            'name': name,
            'phone_number': phone_number,
            'email': email
        })
       
        ...
    
    def remove(self, name):
        for index in range(self.count):
            contact = self.contacts[index]
            if contact['name'] == name:
                return self.contacts.pop(index)
        ...
    
    def update(self, old_name, new_name, new_phone_number, new_email):
        for index in range(self.count):
            contact = self.contacts[index]
            if contact['name'] == old_name:
                self.contacts[index] = {
                    'name': new_name,
                    'phone_number': new_phone_number,
                    'email': new_email
                }

        
        ...



contact_list = ContactList() # create an instance of our class
contact_list.load()



print('Welcome to the Contact List App (CLA)')
while True:
    command = input('Enter a command: ')
    if command == 'load':
        contact_list.load()
        print(f'Loaded {contact_list.count} contacts.') # changed to a property in the class
    elif command == 'save':
        contact_list.save()
        print(f'Saved {contact_list.count} contacts.') # changed to a property in the class
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