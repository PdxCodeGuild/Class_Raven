from time import sleep

class Character:
    def __init__(self, name, weapon=None, ability=None):
        self.name = name
        self.weapon = weapon
        self.ability = ability
        self.hp = 100
        self.mana = 0

    def is_defeated(self):
        '''Return a boolean indicating if the character has hp left'''
        return self.hp <= 0

    def attack(self, opponent):
        opponent.hp -= self.weapon.damage

        print(f'{self.name} attacked {opponent.name} with their {self.weapon.name} {self.weapon.sprite}')

        if opponent.is_defeated():
            print(f'{opponent.name} is defeated!')

        else:
            print(f'{opponent.name} now has {opponent.hp} hp!')
        
        # Return True or False
        return opponent.is_defeated()

    def __str__(self):
        return f'Name: {self.name}, weapon: {self.weapon}, hp: {self.hp}'


class Hero(Character):
    def __init__(self, name, weapon=None, ability=None):
        super().__init__(name, weapon, ability)

    def battle_cry(self):
        return 'I will defeat all evil!'

class Villain(Character):
    def __init__(self, name, weapon=None, ability=None):
        super().__init__(name, weapon, ability)

    def battle_cry(self):
        return 'I will conquer the world!'



class Weapon:
    def __init__(self, name, damage, sprite=None):
        self.name = name
        self.damage = damage
        self.sprite = sprite

    def __str__(self):
        return f'{self.sprite} {self.name} - damage: {self.damage}'


sword = Weapon('Greatsword', 30, '🗡️')
dagger = Weapon('Dagger', 20, '🔪')
bow_n_arrow = Weapon('Longbow', 45, '🏹')


hero = Hero('Andromeda', weapon=sword)
villain = Villain('Helios', weapon=bow_n_arrow)


fighters = [hero, villain]

turn = 0 # count whose turn it is
while True:
    sleep(1.5)

    attacker = fighters[turn % 2] # % 2 to alternate fighters
    opponent = fighters[(turn + 1) % 2]

    fight_over = attacker.attack(opponent)
    if fight_over:
        print(f'{opponent.name} is defeated, {attacker.name} wins!')
        break

    turn += 1