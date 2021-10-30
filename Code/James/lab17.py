import json

# with open(r'C:/Users/james/Class_Raven/Code/James/contact_list.txt') as json_file:
#     data = json.load(json_file)


# print(data)


class ContactList:
    def __init__(self):
        self.contacts = []

    def load(self):
        with open(r'C:/Users/james/Class_Raven/Code/James/contacts') as json_file:
            data = json.load(json_file) #got the file back as a python dictionary
            #print(data) # data is a python dictionary at this point
            list_contacts = data.get('contacts')# get the list of contacts out of the contacts dictionary. 
            #print(list_contacts) #this is a list of the dictionary.
            
            self.contacts = list_contacts
        ...
    
    def count(self):
        return print(len(self.contacts))
        
        ...
    
    def save(self):
        new_dict = {'contacts': self.contacts}
        dict_json = json.dumps(new_dict)
        print(dict_json)
        with open(r'C:/Users/james/Class_Raven/Code/James/contacts', 'w') as Contact_list:
            
        
        
        
        ...

    # def print(self):
        
    #     ...

    # def add(self, name, phone_number, email):
       
    #     ...
    
    # def remove(self, name):
        
    #     ...
    
    # def update(self, old_name, new_name, new_phone_number, new_email):
        
        ...



contact_list = ContactList() # create an instance of our class
contact_list.load()
#contact_list.count()
contact_list.save()
# print('Welcome to the Contact List App (CLA)')
# while True:
#     command = input('Enter a command: ')
#     if command == 'load':
#         contact_list.load()
#         print(f'Loaded ${contact_list.count()} contacts.')
#     elif command == 'save':
#         contact_list.save()
#         print(f'Saved ${contact_list.count()} contacts.')
#     elif command == 'print':
#         contact_list.print()
#     elif command == 'add':
#         print('Enter info of contact to add:')
#         name = input('Name: ')
#         phone_number = input('Phone Number: ')
#         email = input('Email: ')
#         contact_list.add(name, phone_number, email)
#     elif command == 'remove':
#         name = input('Name of contact to remove: ')
#         contact_list.remove(name)
#     elif command == 'update':
#         print('Enter info of contact to add:')
#         old_name = input('Name of contact to update: ')
#         new_name = input('New Name: ')
#         new_phone_number = input('New Phone Number: ')
#         new_email = input('New Email: ')
#         contact_list.update(old_name, new_name, new_phone_number, new_email)
#     elif command == 'help':
#         print('Available commands:')
#         print('load   - load all contacts from the file')
#         print('save   - save contacts to a file')
#         print('print  - print all contacts')
#         print('add    - add a new contact')
#         print('remove - remove a contact')
#         print('update - update a contact')
#         print('exit   - exit the program')
#     elif command == 'exit':
#         break
#     else:
#         print('Command not recognized')