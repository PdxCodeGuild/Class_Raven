'''Lab 19 Adventure
By Philip Bartoo, Randall Mayton and Arek Smullen
10/3/2021'''

from random import randint

height = 10
width = 10
board = []  # start with an empty list

for i in range(height):  # loop over the rows
    board.append([])  # append an empty row
    for j in range(width):  # loop over the columns
        board[i].append(' ')  # append an empty space to the board  
    #print(board,'\n')

class Player:
    def __init__(self,i=0,j=0):
        self.i = i
        self.j = j

    def print_board(self):
        for row in board:
            print(row,'\n')
    
class Villan:
    def __init__(self,i=0,j=0):
        self.i = i
        self.j = j

player = Player()
enemy = Villan() 

for i in range(4):
    enemy.i = randint(0, height - 1)
    enemy.j = randint(0, width - 1)
    board[enemy.i][enemy.j] = '§'

while True:
    command = input('what is your command? ')  # get the command from the user

    if command == 'done':
        break  # exit the game
    elif command == 'left':
        player.j -= 1  # move left
    elif command == 'right':
        player.j += 1  # move right
    elif command == 'up':
        player.i -= 1  # move up
    elif command == 'down':
        player.i += 1  # move down

    # check if the player is on the same space as an enemy
    if board[player.i][player.j] == '§':
        print('You\'ve encountered an enemy!')
        action = input('what will you do? ')
        if action == 'attack':
            print('You\'ve slain the enemy')
            board[player.i][player.j] = ' '  # remove the enemy from the board
        else:
            print('You hestitated and were slain')
            break

            # print out the board

    for i in range(height):
        for j in range(width):
            # if we're at the player location, print the player icon
            if i == player.i and j == player.j:
                print('☺', end=' ')
            else:
                print(board[i][j], end=' ')  # otherwise print the board square
        print()

