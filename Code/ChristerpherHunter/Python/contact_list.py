"""
Christerpher Hunter
Lab 17: Contact List Management

Let's write class for managing a contact list. Copy the code below into a file
and fill in the functions. Save the following files below to your personal
code folder. To open the file, look at the File IO doc, to parse the JSON into
a Python dictionary, look at json module.
"""
from json import load, dumps
from colorama import Fore as F

R = F.RESET


class ContactList:

    def __init__(self):
        self.contacts = []

    def load(self):
        """
        1) open 'contacts.json' with option 'r' for read
        2) get the text from the file
        3) convert the text into a python dictionary (json.loads)
        4) get the list of contacts out of the dictionary
        5) assign the list of dictionaries to self.contacts
        """
        with open("contact_list.json", "r") as f_read:
            self.contacts = load(f_read)

        return self.contacts

    def count(self):
        """return the length of self.contacts"""

        return len(self.contacts["contacts"])

    def save(self):
        """
        1) open 'contacts.json' with open 'w' for write
        2) put self.contacts in a dictionary with the key 'contacts'
        3) convert the dictionary to a json string (json.dumps)
        4) write the json string to the file
        """

        string_dict = dumps(self.contacts, indent=4)

        with open("contact_list.json", "w") as f_write:
            f_write.write(string_dict)

    def print(self):
        """
        loop over self.contacts
        print the information for each contact on a separate line
        """

        for i in range(len(self.contacts["contacts"])):
            print(f"\n{F.YELLOW}Name:{R} " +
                  self.contacts["contacts"][i]["name"],
                  f"{F.YELLOW}Number:{R} " +
                  self.contacts["contacts"][i]["phone_number"],
                  f"{F.YELLOW}Email:{R} " +
                  self.contacts["contacts"][i]["email"])

    def add(self, name, phone_number, email):
        """
        create a new dictionary using the 3 parameters
        add the new dictionary to self.contacts
        """

        new_contact = {
            "name": f"{name}",
            "phone_number": f"{phone_number}",
            "email": f"{email}"
        }

        self.contacts["contacts"].append(new_contact)

    def remove(self, name):
        """
        find the contact in self-contacts with the given name
        remove the element at that index
        """

        for i in self.contacts["contacts"]:
            if i["name"] == name:
                self.contacts["contacts"].remove(i)

    def update(self, old_name, new_name, new_phone_number, new_email):
        """
        find the contact in self.contacts with the given old_name
        set that contacts' name, phone number, etc to the given values
        """

        for i in self.contacts["contacts"]:
            if i["name"] == old_name:
                self.add(new_name, new_phone_number, new_email)
                self.remove(old_name)


def main():
    contact_list = ContactList()  # create an instance of our class
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
            contact_list.update(old_name, new_name, new_phone_number,
                                new_email)
        elif command == 'help':
            print('Available commands:')
            print('load   - load all contacts from the file')
            print('save   - save contacts to a file')
            print('print  - print all contacts')
            print('add    - add a new contact')
            print('remove - remove a contact')
            print('update - update a contact')
            print('q   - exit the program')
        elif command == 'q':
            break
        else:
            print('Command not recognized')


if __name__ == "__main__":
    main()
