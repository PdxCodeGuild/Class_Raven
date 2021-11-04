import random
    
    
class Character():
    def __init__(self, power= 10, name= 'Jeff', health= 10, x = 1, y = 3):
        self.x = x
        self.y = y
        self.power = power
        self.name = name
        self.health = health

    ...

class Enemy(Character):
    def __init__(self, power= 10, name= 'Tom', health= 10, x = 9, y = 3, coins=0):
        super().__init__(name, health, power, x, y)
        self.coins = coins
       
    ...

class Board():
    def __init__(self, width=10, height=10, board=[]):
        self.width = width
        self.height = height
        self.board = board
        for i in range(height):
            board.append([])
            for j in range(width):
                board[i].append(' ')


        
        

board = Board()
player = Character('Player', 100, 20, 0, 0)
player.x=4
player.y=4

enemy = Enemy()
#print(enemy.x, enemy.y)
enemies = int(input("How many enemies do you want to fight? "))
for i in range(0, enemies):

    enemy.x = random.randint(0, board.height - 1)
    enemy.y = random.randint(0, board.width - 1)
    board.board[enemy.x][enemy.y] = '§'


action = 'None'
while True:
    
    
    
    
    for i in range(board.height):
        for j in range(board.width):
            # if we're at the player location, print the player icon
            if i == player.x and j == player.y:
                print('☺', end=' ')
            else:
                print(board.board[i][j], end=' ')  # otherwise print the board square
        print()
    if board.board[player.x][player.y] == '§':
        print('You\'ve encountered an enemy!')
        action = input('what will you do? ')
    if action == 'attack':
        print('You\'ve slain the enemy')
        board.board[player.x][player.y] = ' '  # remove the enemy from the board
        enemies -= 1
        if enemies == 0:
            print('Congrats you won!')
            break
    
    elif not board.board[player.x][player.y] == '§':
        pass
    
    else:
        print('You hestitated and were slain')
        break

        
    
        
        
            
    
    command = input('what is your command? ')  # get the command from the user
    def try_move(value, axis, bounds, increment):
        if not axis == bounds:
            if increment == 'increase':
                axis += value
            else:
                axis -= value
        else:
            print('Go another direction')

    
    if command == 'done':
        break  # exit the game
    elif command == 'left':
        if not player.y == 0:

            player.y -= 1# move left
        else:
            print('Out of range go another direction.')  
        
    elif command == 'right':
        if not player.y >= 9:
            player.y += 1  # move right
        else:
            player.y = 9
            print('Out of range go another direction.')  # move right
    
    elif command == 'up':
        if player.x == 0:
            print('Out of range go another direction.')
        else:
            player.x -= 1  # move up
    
    elif command == 'down':
        if player.x == 9:
            print('Out of range go another direction.')
        else:
            player.x += 1  # move down
    print('enemies remaining:', enemies)
   