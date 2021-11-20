list_of_teams = []

class Basketball_team:

    def __init__(self, first_name, last_name, age, position):
        self.first = first_name
        self.last = last_name
        self.age = age
        self.position = position 
        self.fullname = self.first + ' ' + self.last

    def total_points(self, points, num_of_seasons):
        total_points = points * num_of_seasons
        return total_points

    def add_teams(self, teams):
        list_of_teams.append(teams)
    
    def print_teams(self):
        print(', '.join(list_of_teams))  
        return list_of_teams

player_1 = Basketball_team('Cade', 'Cunningham', 23, 'forward')

new_team = input("do you want to add a new team?\n> ")
while new_team == 'yes':
    what_team = input("what team do you want to add?\n> ")
    player_1.add_teams(what_team)
    new_team = input('how about another team?\n> ')
    if new_team == 'yes':
        continue
    else: 
        break 

print(player_1.print_teams())
