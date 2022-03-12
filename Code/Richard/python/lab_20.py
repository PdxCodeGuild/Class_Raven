import string
import random
class game:
    def _init_(self, name, ship, weapon, power, structure_intergrity ):
        self.name = name
        self.ship = ship
        self.weapon = weapon
        self.power = power(5)
        self.structure_intergrity = structure_intergrity
board = [
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
]

print(board)

class Weapon:
    def __init__(self, name, damage, hit, count=999):
        self.name = name
        self.damage = damage
        self.count = count
        self.hit = hit

five_inch_guns = Weapon('5 in. Guns', 2, random.randit(10, 20), 999)
torpedo = Weapon('Mk 18 Torpedo', 8, random.randit(60, 80), 3)

def attack(self, opponent):
        self.count -= 1
        shot = random.randint(1, 20)
        if shot >= self.hit:
            opponent.hp -= self.weapon.damage
            print(f'{self.name} attacked {opponent.name} with their {self.weapon.name}')
        else:
            print(f'{self.name} missed')
        if opponent.is_defeated():
            print(f'{opponent.name} is defeated!')

        else:
            print(f'{opponent.name} now has {opponent.hp} hp!')
        
        # Return True or False
        return opponent.is_defeated()



def pick6():  #generate list -ticket
    ticket = []
    while len(ticket) < 6:
        num = random.randint(1,99)
        if num != any(ticket): 
#intially problems where a repeat digit would break the code before adding a requirement of 6 digits.
            ticket.append(num)
    return ticket

def count(list, type)