import json
from os import X_OK
contacts_list_dict = {}

class ContactList:

    def __init__(self):
        self.contacts = []

    def load(self):
        with open('contacts.json', 'r') as contacts_file: # 1) open 'contacts.json' with option 'r' for read
            contacts = contacts_file.read() # 2) get the text from the file
        contact_list_dict = json.loads(contacts) # 3) convert the text into a python dictionary (json.loads)
        contact_list = contact_list_dict['contacts']# 4) get the list of contacts out of the dictionary
        for contact in contact_list: # 5) assign the list of dictionaries to self.contacts
                self.contacts.append(contact)
        self.contacts = contact_list
        
    def count(self):
        return len(self.contacts)# return the length of self.contacts

    def save(self):
        with open('contacts.json', 'w') as contacts_file:# 1) open 'contacts.json' with open 'w' for write   
            contacts_list_dict['contacts'] = self.contacts# 2) put self.contacts in a dictionary with the key 'contacts'
            json_contacts_list_dict = json.dumps(contacts_list_dict)# 3) convert the dictionary to a json string (json.dumps)
            contacts_file.write(json_contacts_list_dict)# 4) write the json string to the file

    def print(self):
        for contact in self.contacts:# loop over self.contacts
           print(", ".join("{}:{}".format(*i) for i in contact.items())) # list comprehension that uses .format to format the tuple that is returned from .items function for each key/value in dictionary                      
                 # found a similar coding question/answer on stack overflow that I studied (read about .format and .items) to figure out how to print here https://stackoverflow.com/questions/49693464/converting-dictionary-into-string                                              
    
    def add(self, name, phone_number, email):
        new_contact = {}
        new_contact['name'] = name
        new_contact['phone_number'] = phone_number
        new_contact['email'] = email
        self.contacts.append(new_contact) #add the new dictionary to self.contacts
        

    def remove(self, name):
        for contact in self.contacts: # loop through each dict in self.contacts list 
            if contact['name'] == name:# find the contact in self-contacts with the given name
                self.contacts.remove(contact)# remove the element at that index'''
        
     

    def update(self, old_name, new_name, new_phone_number, new_email):
        for contact in self.contacts:
            if contact['name'] == old_name: # find the contact in self.contacts with the given old_name
                contact['name'] = new_name    # set that contacts' name, phone number, etc to the given values
                contact['phone_number'] = new_phone_number
                contact['email'] = new_email 

contact_list = ContactList() # create an instance of our class
contact_list.load()
print('Welcome to the Contact List App (CLA)')
while True:
    command = input('''
Please enter one of the following cammands: 

load   - load all contacts from the file
save   - save contacts to a file
print  - print all contacts
add    - add a new contact
remove - remove a contact
update - update a contact
exit   - exit the program\n\n> ''')

    if command == 'load':
        contact_list.load()
        print(f'Loaded {contact_list.count()} contacts.')
    elif command == 'save':
        contact_list.save()
        print(f'Saved {contact_list.count()} contacts.')
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


    