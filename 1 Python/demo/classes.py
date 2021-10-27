'''
OOP (Object-Oriented Programming)
Bundling variables and functions that work on those variables within one unit (Class)
Thinking of a program in terms of objects and their relationships instead of a bunch of
independent functions.

Three Pillars of OOP
Encapsulation - Hiding the internals of class, specifying an interface by 
                which other code can use the class ('has-a' relation)
Inheritance - Deriving one type from another type ("Is-a" relationship)
Polymorphism - The ability of a type to be used like another type
'''

# dir(object) - return a list of all the members of the class from which the object is derived
'''
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__
format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash
__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__',
 '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__
rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefol
d', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 
'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower'
, 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'l
strip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rind
ex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip
', 'swapcase', 'title', 'translate', 'upper', 'zfill']
'''

# print(dir(''))

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __repr__(self):
        return f"{self.first_name} {self.last_name} - {self.age}"
    
class Student(Person): # Inheritance - each Student gets all the qualities of a Person class
    def __init__(self, first_name, last_name, age, subjects):
        super().__init__(first_name, last_name, age)
        self.subjects = subjects


class Teacher(Person):
    def __init__(self, first_name, last_name, age, subject):
        super().__init__(first_name, last_name, age)
        self.subject = subject
        self.students = []


# person_1 = Person('Shankar', 'Vedanta', 33)
# print(person_1.first_name, person_1.last_name, person_1.age)

# person_2 = Person('Keegan', 'Good', 33)
# print(person_2.first_name, person_2.last_name, person_2.age)

student_1 = Student('Linda', 'Belcher', 33, ['Math', 'Science', 'Python'])

# print(student_1.first_name, student_1.subjects)

teacher_1 = Teacher('Keegan', 'Good', 33, 'Python')

# teacher_1.students.append(student_1)
# print(teacher_1.first_name, teacher_1.subject, teacher_1.students) # 

# print(student_1) # Linda Belcher - 33


# -------------------------------------------------------------------------------------- #

import math

def distance(p1, p2):
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]

    return math.sqrt(dx ** 2 + dy ** 2)


p1 = [5, 2]
p2 = [8, 4]

# print(distance(p1, p2)) # 3.605551275463989

# More readability with a dictionary:

p1 = {'x': 5, 'y': 2}
p2 = {'x': 8, 'y': 4}

def distance(p1, p2):
    dx = p1['x'] - p2['x']
    dy = p1['y'] - p2['y']

    return math.sqrt(dx ** 2 + dy ** 2)

# print(distance(p1, p2)) # 3.605551275463989

# Group all data relavent to the points in a class
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, p):
        dx = self.x - p.x
        dy = self.y - p.y
        return math.sqrt(dx ** 2 + dy ** 2)

    def __str__(self):
        return f"({self.x}, {self.y})"

    # this will allow the use of the == comparison operator between two instances of a Point
    def __eq__(self, p):
        return self.x == p.x and self.y == p.y

p1 = Point(2, 2)
p2 = Point(2, 2)

print(p1 == p2)
# print(p1) # <__main__.Point object at 0x0000023BBF3F7C70>
# print(type(p1)) # <class '__main__.Point'>
# print(p1.distance(p2)) # 3.605551275463989

# ---------------------------------------------------------------------- #

class PrivatePoint:
    def __init__(self, x, y):
        self.__x = x # double underscore denotes a private variable
        self.__y = y

    def get_x(self):
        return self.__x

    def distance(self, p):
        dx = self.__x - p.__x
        dy = self.__y - p.__y
        return math.sqrt(dx ** 2 + dy ** 2)

p3 = PrivatePoint(3, 3)
p4 = PrivatePoint(4, 4)
# print(p3.__x) # AttributeError: 'PrivatePoint' object has no attribute '__x'
# print(p3.get_x())
# print(p3.distance(p4))

# ----------------------------------------------------------------------------------- #

class Circle:
    def __init__(self, radius, center_x, center_y):
        self.radius = radius
        self.center = Point(center_x, center_y) # encapsulation

    def __repr__(self):
        return f'A circle centered at ({self.center.x}, {self.center.y}) with a radius of {self.radius}'


circle = Circle(10, 5, 5)
print(circle) # A circle centered at (5, 5) with a radius of 10
print(circle.center)