# Lab 20 "Adventure"
# Austen C Myers
# 11-03-2021
from random import *
# * create a 10x10 board
board = []
board_x = 10
board_y = 10
# * create a list to represent each row
for y in range(board_y):
  board.append([])
# * create empty spaces to represent each column
for row in board:
  for x in range(board_x):
    board[x].append(' ')


def initial_position():
  x = randint(0, board_x-1)
  y = randint(0, board_y-1)
  return (x, y)


xy_pairs = []
# * add the player to the board
xy = initial_position()
xy_pairs.append(xy)
player = {'x': xy[0], 'y': xy[1], 'health': 10, 'damage': 3}
board[player['x']][player['y']] = 'σ'

# * add 4 enemies in random locations
enemy_count = 4
enemies = []
for e in range(enemy_count):
  xy = initial_position()
  while xy in xy_pairs:
    xy = initial_position()
  xy_pairs.append(xy)
  health = randint(6, 12)
  damage = randint(1, 3)
  enemy = {'x': xy[0], 'y': xy[1],
           'health': health, 'damage': damage}
  enemies.append(enemy)
for enemy in enemies:
  board[enemy['x']][enemy['y']] = '▲'
for row in board:
  print(row)
# * get player commands to move around the board
commands = ['left', 'right', 'up', 'down', 'done']
command = input(f'what would you like to do?\n{commands}\n')
full = player['health']
while command not in commands:
  command = input(f'what would you like to do?\n{commands}\n')
while player['health'] > 0:
  if command == 'done':
    break
  board[player['x']][player['y']] = ' '
  if command == 'up':
    player['x'] -= 1
  elif command == 'down':
    player['x'] += 1
  elif command == 'right':
    player['y'] += 1
  elif command == 'left':
    player['y'] -= 1
  # * check if the player is on the same space as an enemy
  # ~ fix combat sequence, barely functional
  if board[player['x']][player['y']] == '▲':
    for enemy in enemies:
      if enemy['x'] == player['x']:
        if enemy['y'] == player['y']:
          attacker = enemy
          break
    print('when stepping into the room; you are attacked by an enemy')
    player['health'] -= attacker['damage']
    health = player['health']
    damage = attacker['damage']
    print(
        f'you took {damage} points of damage.\n you\'re health is now {health}/{full}')
    print('how do you respond?')
    action = input('enter attack or flee:\n')
    if action == 'attack':
      attacker['health'] -= player['damage']
      while attacker['health'] > 0:
        if attacker['health'] <= 0:
          print('you\'ve slain the enemy')
          # * remove the enemy
          board[player['x']][player['y']] = 'σ'
          enemies.remove(attacker)
          break
        player['health'] -= attacker['damage']
        attacker['health'] -= player['damage']
    elif action == 'flee':
      x = randint(0, 2)
      y = randint(0, 2)
      player['x'] += x
      if player['x'] >= 10:
        player['x'] -= 10
      player['y'] += y
      if player['y'] >= 10:
        player['y'] -= 10
      board[player['x']][player['y']] = 'σ'
  else:
    board[player['x']][player['y']] = 'σ'
# * print out the board
  for row in board:
    print(row)
  command = input(f'what would you like to do?\n{commands}\n')
print('you died')
