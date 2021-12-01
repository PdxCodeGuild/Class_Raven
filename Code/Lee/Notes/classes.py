# python3 -m http.server # starts a server at localhost port 8000

"""
Encapsulation - Hides the internal components of a class
Inheritance - Derives one type from another type ('has-a' relation)
Polymorphism - The ability of a type to be used as another type
"""

# dir(object) - return a list of all the different methods 


class Person:
    def __init__(self, first_name, last_name, age) -> None: # self is always the first thing done when defining a class
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def __repr__(self) -> str:
        return f"{self.first_name} {self.last_name} - {self.age}"

# person_1 = Person('Shankar', 'Vendata', 33)
# person_2 = Person('Keegan', 'Good', 33)

class Student(Person): # This is demonstrating inheritence - a student will get all the qualities of the Person class
    def __init__(self, first_name, last_name, age, subjects) -> None:
        super().__init__(first_name, last_name, age)
        self.subjects = subjects
        

student_1 = Student('Shankar', 'Vendata', 33, ['English', 'Algebra'])
# student_2 = Student('Keegan', 'Good', 33, ['Math', 'Science', 'Python'])

class Teacher(Person):
    def __init__(self, first_name, last_name, age, subject) -> None:
        super().__init__(first_name, last_name, age)
        self.subject = subject

teacher_1 = Teacher('Keegan', 'Good', 33, 'Python')

# ----------------------------------------------------------------- #
import math

'''def distance(p1, p2):
    dx = p1['x'] - p2['x']
    dy = p1['y'] - p2['y']
    return math.sqrt(dx*dx + dy*dy)

p1 = {'x': 5, 'y': 2}
p2 = {'x': 8, 'y': 4}
print(distance(p1, p2))'''

class Point:
    def __init__(self, x, y): # this is the initializer
        self.x = x # these are member variables
        self.y = y
    
    def distance(self, p): # method, or 'member function'
        dx = self.x - p.x
        dy = self.y - p.y
        return math.sqrt(dx*dx + dy*dy)
    
p1 = Point(5, 2) # call the initializer, instantiate the class
p2 = Point(8, 4)
print(p1.x) # 5
print(p1.y) # 2
print(type(p1)) # Point
print(p1.distance(p2))