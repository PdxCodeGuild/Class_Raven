"""
    Lee Colburn
    Evening Bootcamp - PDX Code Guild
    Lab 17 - Contact List
    """
'''
Reference...

contacts.json:
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
'''

"""Let's write class for managing a contact list. 
Copy the code below into a file and fill in the functions. 
Save the following files below to your personal code folder. 
To open the file, look at the File IO doc, to parse the JSON into a Python dictionary, look at json module."""
import json

class ContactList:
    
    def __init__(self, ):
        self.contacts = []

    def load(self):
        # 1) open 'contacts.json' with option 'r' for read
        f = open('contacts.json', 'r')

        # 2) get the text from the file
        contents = f.read()

        # 3) convert the text into a python dictionary (json.loads)
        contents = json.loads(contents)
        list_of_contents = [i for i in contents['contacts']]

        # 5) assign the list of dictionaries to self.contacts
        self.contacts = list_of_contents
        return
    
    def count(self):
        return len(self.contacts)
    
    def save(self):
        # 1) open 'contacts.json' with open 'w' for write
        f = open('contacts.json', 'w')
        # 2) put self.contacts in a dictionary with the key 'contacts'
        contacts_list = self.contacts
        contacts = {'contacts': contacts_list}
        # 3) convert the dictionary to a json string (json.dumps)
        json_contacts = json.dumps(contacts, indent=2)
        # 4) write the json string to the file
        f.write(json_contacts)
        return

    def print(self, contact=False):
        for counter, i in enumerate(self.contacts, start=1):
            
            display = (
                f"\nContact {counter}:\n"
                f"Name: {i['name']}\n"
                f"Phone: {i['phone_number']}\n"
                f"Email: {i['email']}"
            )
            print(display)
        return

    def add(self, name, phone_number, email):
        # create a new dictionary using the 3 parameters
        new_contact = {'name': name, 'phone_number': phone_number, 'email': email}
        # add the new dictionary to self.contacts
        self.contacts.append(new_contact)
        return
        
    def remove(self, name_to_delete):
        # find the contact in self-contacts with the given name
        index = 0
        listing = self.contacts
        for entry in listing:
            name_check = entry['name']
            if name_check == name_to_delete:
                listing.pop(index)  
            index += 1
        self.contacts = listing
        return 
    
    def update(self, old_name, new_name, new_phone_number, new_email):
        
        listing = self.contacts
        # find the contact in self.contacts with the given old_name
        for index, entry in enumerate(listing):
            name_check = entry['name']
            # set that contacts' name, phone number, etc to the given values
            if name_check == old_name:
                entry['name'] = new_name
                entry['phone_number'] = new_phone_number
                entry['email'] = new_email
        return



    
contact_list = ContactList() # create an instance of our class
contact_list.load()
print('Welcome to the Contact List App (CLA)')
print('Available commands:')
print('load   - load all contacts from the file')
print('save   - save contacts to a file')
print('print  - print all contacts')
print('add    - add a new contact')
print('remove - remove a contact')
print('update - update a contact')
print('exit   - exit the program')

while True:

    command = input('Enter a command: ')
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
