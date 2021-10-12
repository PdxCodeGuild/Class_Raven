"Hello" # string
4       # int
2.5     # float
True    # boolean / False
None    # none


x = input("Enter a number: ")

try:
    x = int(x)
except ValueError:
    print("That was not a number...")
    exit()

if x > 0:
    print("This number is positive")
    print("😎")
elif x == 0:
    print('The number is 0')
else:
    print("This number is negative")