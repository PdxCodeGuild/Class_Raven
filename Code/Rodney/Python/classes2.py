
board = [['o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o']]



class Character:
    def __init__(self, name, weapon=None, ability=None):
        self.name = name
        self.weapon = weapon
        self.ability = ability
        self.hp = 100
        self.mana = 0

    def is_defeated(self):
        # return a boolean indicating if character has hp left
        return self.hp <= 0

    def attack(self, opponent):
        opponent.hp -= self.weapon.damage

        print (f'{self.name} attacked {opponent.name}')

        if opponent.is_defeated():
            print(f'{opponent.name} is defeated')
            return True
        else:
            print(f'{opponent.name} now has {opponent.hp} hp!')

        #return true or false 
        return opponent.is_defeated 
    
    def __str__(self): 
        return f'Name: {self.name}, weapon: {self.weapon} hp: {self.hp}'


class Hero(Character):
    def __init__(self, name, weapon=None, ability=None):
        super().__init__(name, weapon, ability)

    def battle_cry(self):
        return 'I will conquer the world!'

class Villain(Character):
    def __init__(self, name, weapon=None, ability=None):
        super().__init__(name, weapon, ability)

    def battle_cry(self):
        return 'I will defeat all evil!'

class Weapon:
    def __init__(self, name, damage, sprite=None):
        self.name = name
        self.damage = damage
        self.sprite = sprite

    def __str__(self):
        return f'{self.sprite} {self.name} - damage: {self.damage}'


sword = Weapon('Greatsword', 30, 'sword_pic')
dagger = Weapon('TheDagger', 20, 'picture_of_dagger')
bow_n_arrow = Weapon('TheBow', 10, 'picture_of_bow')


hero = Hero('Andromeda', weapon=sword)
villain = Villain('Helios', weapon=bow_n_arrow)


print(hero)
print(hero.battle_cry())

fighters = [hero, villain]

turn = 0
while True:
    attacker = fighters[turn % 2]
    opponent = fighters[(turn + 1) % 2]

    fight_over = attacker.attack(opponent)
    if fight_over:
        print(f'{opponent.name} is defeated!')

    turn += 1



#hero.attack(villain)

#print(sword)

'''def save(self):
    with open('contacts.json', 'w') as contacts_file:   
        contacts_list_dict['contacts'] = self.contacts
        json_contacts_list_dict = json.dumps(contacts_list_dict)
        contacts_file.write(json_contacts_list_dict)
        print(json_contacts_list_dict)'''