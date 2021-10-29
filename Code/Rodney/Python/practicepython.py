

#sports = ['soccer', 'baseball', 'golf', 'tennis']

#print(sports[-1])

#for sport in sports:
    #print(sport)

#sports.append('water polo')

#print(sports)

#squares = []

#for x in range(1,11):
    #print(x)
    #squares.append(x**2)

#print(squares)

#first_two = sports[:2]
#copy_of_sports = sports[:]

#print(first_two)
#print(copy_of_sports)

#items in a tuple CAN'T be modified

#dimensions = (1920, 1080)

#print('soccer'in sports)

#alien = {
#'color': 'green',
#'planet': 'blupopia'
#}

#print(f"color is: {alien['color']}")

#alien['x_position'] = 'pizza'

#print(alien)

#for factoid_title, factoid in alien.items():
    #print(f"{factoid_title}: {factoid}")

#fav_numbers = {
#'eric': 17,
#'daniel': 37
#}

#for name in fav_numbers.keys():
    #print(name + 'loves a number')

#def greet_user(username= 'sarah'):
    #print(f'what is up {username}!')

#greet_user('Rodney')


#def add_numbers(x, y):
    #"""add two numbers and return sum"""
    #return x + y

#sum = add_numbers(2535, 523)

#print(sum)

#lass Dog():

   # """Represents a dog"""

    #def __init__(self, name):
        
        #""" initializing a dog object"""
        #self.name = name

    #def sit(self):

        #""" simulate sitting """
        #print(self.name + " is sitting")

#my_dog = Dog('Peso')

#print(my_dog.name + " is a great dog")
#my_dog.sit()


class Sports():

    """ represents a sport"""

    def __init__(self, sport):

        self.sport = sport

    def currently_on(self):

        print(self.sport + 'is currently live on TV')

sport_type = Sports('Soccer')

print(sport_type.sport + "is awesome" )



'''classes:

two robots: Tom and Jerry...there job is to introduce themselves when someone goes to website
need to store 2 sets of info: 
1.) Properties (like name, color, weight) (called attributes)

2.) Set of functionalities (introduce itself)  (called methods)
    so you could have introduce_self()

Is there a way to organize these properties and functions?

Yes!  It's called an object (a collection of properties can be expressed as variables and functions)

once you have an object, you can assign it to a variable
for example, r1 = first robot (contains all properties and functions)
second robot will equal r2 for example

so you see these two objects, and think, well these are similar. hmmmm.
is there a convenient way to organize that?

yes! A CLASS... a class is basically a blueprint from which you can make objects

so a class in this case would be:

  name, color, weight
  introduce_self()

  and class doesn't specify exactly what name color or weight is, for example

when you define a class... have to name it...first letter is capitalized '''


class Robot {
name,
color,
weight

void introduc

}

r1 = new Robot(),

r1.name = "Tom",
r1.color = "red",
r1.weight = 30

r2 = new Robot(),

r2.name = "Jerry",
r2.color = "white",
r2.weight = 40

r1.introduce_self(),
r2.introduce_self()














































