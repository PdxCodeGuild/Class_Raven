colors = ['red', 'green', 'blue', 'yellow', 'cyan', 'orange']

colors.insert(0, 'brown')

colors.remove('green')

some_color = colors.pop(3)

more_colors = ['purple', 'teal', 'white', 'black']

# colors.extend(more_colors)

# all_colors = colors + more_colors

# extended_colors = more_colors.copy()

# more_colors.pop(2)


# colors.reverse()
import random
test = ['abc', 'bcd', 'abcd', 'abcde', 'bcdef']
random.shuffle(test)
test.sort(key=lambda color: len(color))

# new_list = list(reversed(colors))
# new_list = list(sorted(colors))

print(test)
