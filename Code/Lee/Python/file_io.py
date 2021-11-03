
# file = open('./test.txt') # Looks in current directory for 'test.txt' as 'file'
# contents = file.read() # Reads contents within 'file'
# file.close() # Closes the file... best practice, and enables file to be edited



'''with open('./test.txt', 'r') as file: # Opens 'test.txt' in read format as 'file'
    contents = file.read()'''

content_list = []

'''with open('./test.txt', 'r') as file: # Opens 'test.txt' in read format as 'file'. output: ['this is sample data\n', 'more data\n', 'more\n', 'new line!']
    for line in file:
        content_list.append(line)
    contents = file.read()'''


''' # write a phonebook to test.txt:
phonebook = {'David': '5551234', 'Alice': '6662345'}
with open('./test.txt', 'w') as phone_book_file:
    for name, number in phonebook.items():
        line = f'{name} {number}\n'
        phone_book_file.write(line)'''

# Read a phonebook to test.txt
with open('test.txt', 'r') as phone_book_file:
    phone_book_data = phone_book_file.read().split('\n')

phone_book = {}
for line in phone_book_data:
    name, number = line.split()
    phone_book[name] = number

print(phone_book)