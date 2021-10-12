
# with open('example.txt') as llama:
#     text = llama.read()


# text += '\nHere is some new content.'

# 'w' write
# with open('example.txt', 'w') as cool_stuff:
#     cool_stuff.write(text)


# 'a' append
# with open('example.txt', 'a') as file:
#     file.write('\nSome other example')


# file = open('example.txt')
# text = file.read()
# print(text)

# file.close()


with open('data/colors.txt') as file:
    colors = file.read()

colors = colors.split(', ')

with open('data/colors.txt', 'w') as file:
    for color in colors:
        if len(color) > 4:
            file.write(color + '\n')

# with open('data/colors.txt', 'w') as file:
#     file.write('\n'.join(colors))

# print('\n'.join(colors))