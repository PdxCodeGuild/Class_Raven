

import string
import random

class game:
    def __init__(self, ship, weapon, power, position, structure_intergrity):
        self.ship = ship
        self.weapon = weapon
        self.position = position 
        self.power = 100
        self.structure_intergrity = 0

class Goodship:
    def __init__(self, ship, weapon=None): 
        super().__init__(ship, weapon)

    def spawn(self):
        for i in range(1):
            self.row = random.randint(0, height - 1)
            self.column = random.randint(0, width - 1)
            self.position = [row, column]

class Badship: 
    def __init__(self, ship, weapon=None): 
        super().__init__(ship, weapon)

    def spawn(self):
        for i in range(1):
            self.row = random.randint(0, height - 1)
            self.column = random.randint(0, width - 1)
            self.position = [row, column]


class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage 


five_inch_guns = Weapon('5 inch guns', 10)
torpedoes = Weapon('toredoes', 80)


'''board = [
['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o','o'],
['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
]'''


def create_board():
    width = 10
    height = 10
    board = []  # start with an empty list
    for i in range(height):  # loop over the rows
        board.append([])  # append an empty row
        for j in range(width):  # loop over the columns
            board[i].append('x')  # append an empty space to the board  

    for boards in board:
        print(' '.join(boards))

    row = 0
    column = 0

def spawn(self):
    for i in range(1):
        self.row = random.randint(0, height - 1)
        self.column = random.randint(0, width - 1)
        self.position = [row, column]


'''good_guy_row = 0
good_guy_column = 0

for i in range(1):
    good_guy_row = random.randint(0, height - 1)
    good_guy_column = random.randint(0, width - 1)
    good_guy_position = [good_guy_row, good_guy_column] '''




