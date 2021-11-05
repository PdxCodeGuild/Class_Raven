import requests
import re 

response = requests.get('https://www.gutenberg.org/cache/epub/66588/pg66588.txt', params={'format': 'json'})

text = '' 
list_of_characters = []
list_of_lines = []

with open('apibook.txt', 'w') as file:
    text = response.text 
    file.write(text) 

with open('apibook.txt', 'r') as file:
    for characters in text:
        list_of_characters.append(characters)
words = text.split()

list_text = [text]
for element in list_text:
    list_of_lines += re.split("(?<=[.!?])\s+", element)


sentences = len(list_of_lines)
words = len(words)
characters = len(list_of_characters)

ari1 = 4.71 * (characters/words) 
ari2 = .5 * (words/sentences) 
ari = ari1 + ari2 - 21.43
if ari > 14:
    ari = 14

ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

output = list((ari_scale[ari]))

print(output)