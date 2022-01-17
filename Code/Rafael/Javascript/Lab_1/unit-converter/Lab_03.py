# Lab 3: Unit Converter
# Version 1 
"""
meters_convert = {'ft': 0.3048}

q1 = input('\nWhat is the distance in feet? ')

q1 = int(q1)

convertion = q1 * meters_convert['ft']

print(f"{q1} ft is {convertion} m\n")

# Version 2: no if/elifs 

"""

meters_convert = {
    'ft': 0.3048, 
    'm': 1, 
    'km': 1000, 
    'mi': 1609.34    
}

while True:

    q1 = input('\nWhat is the distance? ')
    
    q2 = input('What are the units? ')

    
    q1 = int(q1)
    
  
    solution = [q2]

    ft = q1 * meters_convert['ft']
    mi = q1 * meters_convert['mi']
    m = q1 * meters_convert['m']
    km = q1 * meters_convert['km']


    print(f'{q1}{q2} is  m\n')

    break



# Working Version 2: (if/elifs) 

"""

meters_convert = {'ft': 0.3048, 'm': 1, 'km': 1000, 'mi': 1609.34,  }


q1 = int()


q1 = int(input('\nWhat is the distance? '))
q2 = input('What are the units? ')

mi = q1 * meters_convert['mi']
m = q1 * meters_convert['m']
km = q1 * meters_convert['km']
ft = q1 * meters_convert['ft']   

if q2 == 'km':
    print(f"{q1} {q2} is {km} m\n")
elif q2 == 'm':
    print(f"{q1} {q2} is {m} m\n")
elif q2 == 'mi':
    print(f"{q1} {q2} is {mi} m\n")
elif q2 == 'ft':
    print(f"{q1} {q2} is {ft} m\n")
else: 
    print('Try again, select either miles: "mi", meters: "m", kilometers: "km" or feet: "ft" after entering a distance')
    

"""