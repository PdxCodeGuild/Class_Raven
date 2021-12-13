import json
class ContactList:
    
    def __init__(self):
        self.path = 'storage/contacts.json'
        self.contacts = self.load()
        self.count = len(self.contacts)

    def load(self):
        with open(self.path) as file:
            contacts = file.read()
            contacts = json.loads(contacts)
            contacts = contacts['contacts']
            return contacts
    
    def save(self):
        with open(self.path, 'w') as file:
            contacts = {'contacts': self.contacts}
            contacts = json.dumps(contacts)
            file.write(contacts)


    def print(self):
        for contact in self.contacts:
            print('\n  ', contact['name'])
            print('    ', contact['phone_number'])
            print('    ', contact['email'])
            print()

    def add(self, name, phone, email):
        contact = {'name': name, 'phone_number': phone, 'email': email}
        self.contacts.append(contact)

    
    def remove(self, name):
        index = 0
        for contact in self.contacts:
            if contact['name'] == name:
                self.contacts.pop(index)
                return 'contact removed'
            index += 1
        return 'contact not found'

    def update(self, name, new_data):
        index = 0
        for contact in self.contacts:
            if contact['name'] == name:
                found = self.contacts.pop(index)
                break
            index += 1
            # return 'contact not found'
        found.update({'name': new_data['name'], 'phone_number': new_data['phone'], 'email': new_data['email']})
        self.contacts.insert(index, found)