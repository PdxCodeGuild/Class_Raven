

# Read file
with open('data/phonebook.txt') as file:
    phonebook = file.read()

phonebook = phonebook.split('\n')
name = input("Lookup name: ")

found_entry = False
for entry in phonebook:
    if name.lower() in entry.lower():
        print(entry)
        found_entry = True

if not found_entry:
    print('No entry found.')
    name = input("Enter name for new entry: ")
    phone_number = input(f"Enter number for {name}: ")

    phonebook.append(name + " " + phone_number)

    phonebook.sort()
    with open('data/phonebook.txt', 'w') as file:
        file.write("\n".join(phonebook))