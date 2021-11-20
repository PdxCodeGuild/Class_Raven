'''Lab 19 Adventure
By Philip Bartoo, Randall Mayton and Arek Smullen
10/3/2021'''

'''
Option 1: Loop the character from one side of the board to the other.
Option 2: Create health point system for enemy and villan. Randomize villan & player (player base attack (2)
Option 3: Power up item at a random spot on the board (i.e. weapon) to increase attack or increase move speed
Option 4: Hide enemy
Option 5: Goal to win game
Option 6: Add run option only once
'''

from random import randint,choice

height = 10
width = 10
board = []  # start with an empty list

for i in range(height):  # loop over the rows
    board.append([])  # append an empty row
    for j in range(width):  # loop over the columns
        board[i].append(' ')  # append an empty space to the board  
    #print(board,'\n')

class Player:
    def __init__(self,i=0,j=0,lives=2):
        self.i = i
        self.j = j
        self.lives = lives

    def print_board(self):
        for row in board:
            print(row,'\n')
        
class Villan:
    def __init__(self,i=0,j=0):
        self.i = i
        self.j = j


player = Player()
trap = Villan() 



for i in range(4):
    trap.i = randint(0, height - 1)
    trap.j = randint(0, width - 1)
    board[trap.i][trap.j] = ''

for i in range(1):
    gift_i = randint(0, height - 1)
    gift_j = randint(0, width - 1)
    board[gift_i][gift_j] = 's'

for i in range(1):
    life_i = randint(0, height - 1)
    life_j = randint(0, width - 1)
    board[life_i][life_j] = 'l'

speed_boost = 0

board[9][9] = 'b'
print('Oh no, after a long day of coding with PDX Code Guild your power has gone out!\nNow you\'d like to get some sleep but there are hidden enemies in your way.\nNavigate to your bed while killing any enemies you encounter. You have two lives remaining. Good luck!')
while True:
    command = input('What is your command (up, down, left, right, or done)? ')  # get the command from the user

    if command == 'done':
        break  # exit the game
    elif command == 'left':
        player.j -= 1 + speed_boost # move left
    elif command == 'right':
        player.j += 1 + speed_boost# move right
    elif command == 'up':
        player.i -= 1 + speed_boost# move up
    elif command == 'down':
        player.i += 1 + speed_boost# move down

    # check if the player is on the same space as an enemy
    if board[player.i][player.j] == '':
        #print(f'You\'ve encountered a trap! You have {player.lives} remaining.')
        player.lives -= 1
        board[player.i][player.j] = 'x'
        if player.lives == 0:
            print('You died....thank you for playing')
            exit() # remove the enemy from the board
            # print out the board

    if board[player.i][player.j] == board[gift_i][gift_j]:
        speed_boost += 1
        print('You gained a speed boost!')
    if board[player.i][player.j] == board[life_i][life_j]:
        player.lives += 1
        print('You gained one life!')
    for i in range(height):
        for j in range(width):
            # if we're at the player location, print the player icon
            if i == player.i and j == player.j:
                print('☺', end=' ')
            elif player.i == 9 and player.j == 9:
                print('You made it! Goodnight!')
                exit()
            else:
                print(board[i][j], end=' ')  # otherwise print the board square
        print()

                