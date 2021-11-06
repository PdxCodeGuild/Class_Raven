## blue print for creating copies of a thing
##things that are made from it can have their own properties


# str, list, int

'''
OOP (Object Oriented Programming)

Orienting ourselves around idea of an object
Bundling variables and functions that work on those variables within one unit (Class)

Thinking of a program in terms of objects and their relationships instead a bunch of indep functions

3 Pillars of OOP:
Encapsulation: hiding the internals of class, specifying an interface by which other code can use the class
('has-a' relationship...the door has a knob)

Inheritance: Deriving one type from another type ('is-a relationshp)
a cat is a mammal, cats have characteristics of mammal

Polymorphsm: the ability of a type to be used like another type

'''
# dir(object) - return a list of all the members of the class from which the object is derived 


'''class Person: 
    def __init__(self, first_name, last_name, age):   ## how is this person gonna look? every object from this class will have these properties 
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __repr__(self):
        return f"{self.first_name}"

class Student(Person): # inheritcance - each student gets all the qualities of a Person class
    def __init__(self, first_name, last_name, age, subjects): 
       super().__init__(first_name, last_name, age)
       self.subjects = subjects ## only unique or new 

class Teacher(Person): # inheritcance - each student gets all the qualities of a Person class
    def __init__(self, first_name, last_name, age, subject): 
       super().__init__(first_name, last_name, age)
       self.subject = subject ## only unique or new 
       self.students = []

person_1 = Person('Keegan', 'Good', 33)
print(person_1.first_name, person_1.last_name, person_1.age)

student_1 = Student('Keegan', 'Good', 33, ['Math', 'Science', 'Python'])
print(student_1.first_name, student_1.subjects)

teacher_1 = Teacher('Lisa', 'Arnold', 33, 'Python')

teacher_1.students.append(student_1)
print(teacher_1.first_name, teacher_1.subject, teacher_1.students)


#class Point: 
    #def __init__(self, x, y):
        #self.x = x
        #self.y = y

    #def distance(self, p):
        #dx = self.x - p.x
        #dy = self.y - p.y  ## p has property x and property y 
        ### code here to determine distance

#p1 = Point(5, 2)
#p2 = Point(8, 3)

#print(p1)

#p1.distance(p2)  ## same thing as using .upper(distance) from string(Point)

### double underscore bdenotes a private variable

# _______________________________________encapsulation

#class Circle:
    #def __init__(self, radius, center_x, center_y):
        #self.radius = radius
        #self.center = Point(center_x, center_y) #encapsulated 

    #def __repr__(self):
        #return f'A circle centered at ({#self.center.x}, {#self.center.y}) with a raidus of {#self.radius}' # etc....


#circle = Circle(10, 5, 5)
#print(circle)
#print(circle.center)

    #def withdrawal_amount


    #def calc_interest


    #def test(self, money):
        #print('hello')

#atm1 = Atm(balance = 1000)
#atm2 = Atm(balance = 3)


#atm1.test(34)

#print(atm1.balance)
#print(atm2.balance)'''



## DON'T use self outside of class structure


