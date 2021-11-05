


#with open('testing.txt', 'r') as phone_book_file:
    #book_lines = phone_book_file.readlines()

#print(book_lines)


#with open('testing.txt', 'r') as phone_book_file:
    #for line in phone_book_file:
        #print(line)

lines = ['125', 'hi mom', 'whats up']
with open('testing.txt', 'a') as phone_book_file:
    phone_book_file.write('\n'.join(lines))

phonebook = {'David': '5551234','Alice': '6662345','Jake': '33'}
with open('testing.txt', 'w') as phone_book_file:
    for name, number in phonebook.items():
        line = f'{name} {number}\n'
        phone_book_file.write(line)

with open('testing.txt', 'r') as phone_book_file:
    phone_book_data = phone_book_file.read().split('\n')

print(phone_book_data)

phone_book = {}
for line in phone_book_data:
    name, number = line.split()
    phone_book[name] = number




        #print(line)
        #line = word.replace('\n', '')

#text = file.read().split('\n')
#import re   
#word_list = re.compile('/w+').findall(text)


#text = ''.join(text)
 #text = text.replace('\n', ' ')
#response.encoding = 'utf-8'

'''new_dict = 
with open('chance_book.txt', 'w') as file:
    for word, count in file.items():
        line = f'name} number}\n'
        phone_book_file.write(line)'''


#words = words.replace(i, '')

#with open('chance_book.txt', 'r') as file:
    #book_lines = file.readlines()

#print(book_lines)

#lines = []
#with open('chance_book.txt', 'w') as file:
    #file.write('\n'.join(lines))


#with open('chance_book.txt', 'r', encoding='utf-8') as file:
    #text = file.read()
#print(text)

#for words in 'chance_book.txt':
    #words.lower()

