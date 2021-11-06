# Lab_17 Contact List 
# Rafael Medina



""" 
Still in Progress 11/3/2021 
"""
import json

# C:\Users\rm210\Desktop\codepdx\extra\contacts.json


class ContactList:
    
    def __init__(self):
        self.contacts = []
       
    def load(self):
        
        # 1) open 'contacts.json' with option 'r' for read
        #with open(r'contacts.json') as contacts_file: # r had to be added in front of string to eliminate ('SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated')
        
        # Make sure that contacts.json file is in the same location and .py file.
        with open ('contacts.json','r') as contacts_file: # 'r' default reading 'w' (erasing) 'x' open file "failing if it exists" 'a' appending 't' read and write as text 'b' read and write as binary
          

        # 2) get the text from the file
            # read() gets the text from the file   
            #print(type(self.contacts))
            #print(contacts_file.read())

            contents = contacts_file.read()

        # 3) convert the text into a python dictionary (json.loads)
            
            contents = json.loads(contents)
            
            """
            #contacts_files = json.loads(self.contacts) 
            print(type(self.contacts))
            print(self.contacts)
            print(len(self.contacts))
            """
        # 4) get the list of contacts out of the dictionary
            
            contacts = contents['contacts'] # This links to the "contacts" list that was a .json object

      
            
        # 5) assign the list of dictionaries to self.contacts

            self.contacts = contacts # New assignment to self.contacts to populate the contents of 'contacts' list
        #
                      
        ...

    
    def count(self):
        lenght = len(self.contacts)
        # return the count of self.contacts
        # There is no count on the REPL exept for save and remove coomands.
        return lenght(self.contacts)
        ...
    
    def save(self):
        # 1) open 'contacts.json' with open 'w' for write
        with open ('contacts.json','r') as contacts_file:

        # 2) put self.contacts in a dictionary with the key 'contacts'
            contacts_dict = {'contacts': self.contacts}

        # 3) convert the dictionary to a json string (json.dumps)
        # .dumps "Serialize obj to a JSON formatted str".
            contents = json.dumps(contacts_dict, indent = 2) # indents print by 2
            
        # 4) write the json string to the file
            contacts_file .write(contents)
        ...

    def print(self):
        # loop over self.contacts
        for contact in self.contacts:
        # print the information for each contact on a separate line
         # in order to get a print beyond step #5, one has to loop through the contacts to print on seperate lines.
            output = (
                f"Name: {contact['name']}\n"
                f"Phone: {contact['phone_number']}\n"
                f"Email: {contact['email']}\n"
            )
            print(output)
        ...

    def add(self, name, phone_number, email):
        # create a new dictionary using the 3 parameters
        
        self.contacts.append({'name': name, 'phone_number': phone_number, 'email': email}) # Keep strings looking similar in keys so it will print like the others.

        # add the new dictionary to self.contacts

        ...
    
    def remove(self, name):
        # find the contact in self-contacts with the given name
        # remove the element at that index
        for index in range(self.count):
            contact = self.contacts[index]
            if contact['name'] == name:
                return self.contacts.pop(index)
            # pops the name from the contact list    
        ...
    
    def update(self, old_name, new_name, new_phone_number, new_email):
        # find the contact in self.contacts with the given old_name
        # set that contacts' name, phone number, etc to the given values
        for index in range(self.count):
            contact = self.contacts[index]
            if contact['name'] == old_name:
                self.contacts[index] = {'name': new_name, 'phone_number': new_phone_number, 'email': new_email}
        ...
    
contact_list = ContactList() # create an instance of our class
contact_list.load()

print('\nWelcome to the Contact List App (CLA)')
print(f"'help'   - 'available commands:")
print(f"'load'   - 'load all contacts from the file'")
print(f"'save'   - 'save contacts to a file'")
print(f"'print'  - 'print all contacts'")
print(f"'add'    - 'add a new contact'")
print(f"'remove' - 'remove a contact'")
print(f"'update' - 'update a contact'")
print(f"'exit'   - 'exit the program'\n")

while True:
    
    command = input("Enter a command or 'help' to see the commands list after this prompt: ")
    if command == 'load':

        contact_list.load()

        print(f'Loaded ${contact_list.count()} contacts.') # If a @property above the functions then it becomes part of that propert and the () are not needed any more.  

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
        removed = contact_list.remove(name)
        print(f"Removed: {removed['name']}")

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