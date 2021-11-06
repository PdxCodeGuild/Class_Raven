import string
import random
import unicodedata
import time

class Ship:  
    def __init__(self, ship, weapon): # creating class, initializing class parameters
        self.ship = ship
        self.weapon = weapon
        self.power = 100
        self.structure_intergrity = 0

class Goodship(Ship):
    def __init__(self, ship, weapon=None): 
        super().__init__(ship, weapon) # allows us to inherit methods/variables from parent class

    def __str__(self):  # allows us to return name of ship 
        return self.ship

class Badship(Ship): 
    def __init__(self, ship, weapon=None): 
        super().__init__(ship, weapon)
    
    def __str__(self):
        return self.ship

class Weapon:
    def __init__(self, name, damage, number): 
        self.name = name
        self.damage = damage 
        self.number = number
    
    def __str__(self):
        return self.name

torpedo = Weapon('Torpedo', 80, 3)  #instantiating class objects for Weapon class
five_inch_gun = Weapon('5 inch gun', 20, 5)
cannon_balls = Weapon('Cannon-balls', 50, 3)

good_ship = Goodship('USS Good Ship', torpedo) #instantiating class objects for good ship/bad ship classes
bad_ship  = Badship('Pirate Ship', cannon_balls)

height = 10
width = 10
board = []  # start with an empty list
for i in range(height):  # loop over the rows
    board.append([])  # append an empty row
    for j in range(width):  # loop over the columns
        board[i].append('.')  # append an empty space to the board 
for i in range(1):
    good_ship_c = random.randint(0, height - 1)
    good_ship_r = random.randint(0, width - 1)  ## randomly placing good/bad ship on board by obtaining random indexes for 
    board[good_ship_c][good_ship_r] = '\U0001F6E5'  ## outer lists (columns) and inner lists (rows)
for i in range(1):
    bad_ship_c = random.randint(0, height - 1) 
    bad_ship_r = random.randint(0, width - 1) 
    board[bad_ship_c][bad_ship_r] = '\U0001F480'
for boards in board:
    print(' '.join(boards))
   

while bad_ship.power >= 0:    ## we can break out of this outer loop if bad ship power is 0 (we sunk bad ship)
    command = input('what is your command? ')  
    if command == 'done':
        break  
    elif command == 'left':
        if good_ship_r >= 1:  ## if user enters left but are at far left of row like this: |x| | | | | |
            good_ship_r -= 1   ## then they can't go farther left, so thats why we make sure they are at index 1 at least like this:
        else:                                                                                  # | |x| | | |
            print("You're at left edge of map!")
    elif command == 'down':
        if good_ship_c <= 8:
            good_ship_c += 1  
        else:
            print("You're at bottom of map!")
    elif command == 'up':
        if good_ship_c >= 1:
            good_ship_c -= 1  
        else:
            print("You're at top of map!")
    elif command == 'right':
        if good_ship_r <= 8:
            good_ship_r  += 1  
        else:
            print("You're at right edge of map!")

    if board[good_ship_c][good_ship_r] == board[bad_ship_c][bad_ship_r]:  ## if good/bad ship at same place in list within a list then, the fight is on! 
        action = input(f'''
{good_ship}, you have encountered a {bad_ship}

Enter '1' for attack
Enter '2' to retreat
\n> ''')
        
        if action == '1':
            while bad_ship.structure_intergrity >= 0:  
                weapon_choice = input(f"\nWould you like to fire a {good_ship.weapon}? (You have {good_ship.weapon.number} remaining)?\n> ")

                if weapon_choice == 'yes':       ## using instances of classes we created to simply deduct power from each ship based on the damage of 
                    good_ship.weapon.number -= 1   ## their opponents weapon
                    bad_ship.power = bad_ship.power - good_ship.weapon.damage
                    print(f"\n{good_ship} fired {good_ship.weapon} at {bad_ship}!")
                    time.sleep(3)
                    bad_ship.weapon.number -= 1
                    good_ship.power = good_ship.power - bad_ship.weapon.damage
                    print(f"\n{bad_ship} fired {bad_ship.weapon} at {good_ship}!")
                    time.sleep(3)
                    print("\nAssessing damage...")
                    time.sleep(3)

                    if bad_ship.power > bad_ship.structure_intergrity:  ## if bad ship still has power we restart inner loop and offer chance to fire again 
                        print(f"\n{bad_ship} power is at {bad_ship.power}%")
                        print(f"\n{good_ship} power is at {good_ship.power}%")

                    elif bad_ship.power <= bad_ship.structure_intergrity:  ## if bad ship power is less than structural integrity, we break inner and outer loop 
                        print(f"\n{good_ship} sunk the pirate ship! The ocean is safe again!")
                        board[bad_ship_c][bad_ship_r] = '.' 
                        break

        else:
            print('Your bravery is questionable, but you will live another day')
            break

for boards in board:
    print(' '.join(boards))






















