# Let's write class for managing a contact list. 
# Copy the code below into a file and fill in the functions. 
# Save the following files below to your personal code folder. To open the file, 
# look at the File IO doc, 
# to parse the JSON into a Python dictionary, look at json module.

# contacts_json 
# {
#     "contacts": [{
#         "name": "Dora M. Smith",
#         "phone_number": "919-781-7129",
#         "email": "doramsmith@hotmail.com"
#     },{
#         "name": "Annette D. Berube",
#         "phone_number": "662-319-6954",
#         "email": "annette@gmail.com"
#     },{
#         "name": "Austin M. Pigott",
#         "phone_number": "478-777-8878",
#         "email": "austin@aol.com"
#     }]
# }
import json
class ContactList:
    
    def __init__(self):
        self.contacts = []

    def load(self):
        # 1) open 'contacts.json' with option 'r' for read
        with open("contacts.json", 'r') as my_file:
            # 2) get the text from the file
            contents = my_file.read()
        # 3) convert the text into a python dictionary (json.loads)
        pyth_dict = json.loads(contents)
        # 4) get the list of contacts out of the dictionary
        # and assign the list of dictionaries to self.contacts
        self.contacts = pyth_dict['contacts']
        print(self.contacts)
    
    
    def count(self):
        # return the length of self.contacts
        return len(self.contacts) # I don't think I nedd the dunder in fromt becasue that's just for hiding 
        
        ...
    
    def save(self):

        # 1) open 'contacts.json' with open 'w' for write
        with open('contacts.json', 'w') as save_file:
        # 2) put self.contacts [] in a dictionary with the key 'contacts'
            fu_king_dict = {'contacts': self.contacts}
            # print(fu_king_dict)
            # convert the dictionary to a json string (json.dumps)
            # self.contacts.json.write(fu_king_dict)
        # 3) convert the dictionary to a json string (json.dumps)
            other_fu_king_thing = json.dumps(fu_king_dict,indent=4) #returns dict into string
        # 4) write the json string to the file 
            save_file.write(other_fu_king_thing)
    
     


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
print(contact_list.contacts)



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