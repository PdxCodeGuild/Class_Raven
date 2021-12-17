class info:
    def __init__(contact, data):
      contact.data = data
      contact.name = data['name']
      contact.split = data['name'].split()
      contact.first = contact.split[0]
      contact.middle = contact.split[1]
      contact.last = contact.split[2]
      contact.phone = data['phone_number']
      contact.email = data['email']
      contact.string = ''
