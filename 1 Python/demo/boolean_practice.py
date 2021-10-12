
# Practice 2: Booleans, Comparisons, & Conditionals
# Copy and paste this file into your own "02_booleans.py"
# Fill in the code for each of the functions
# Run the tests by typing "pytest 02_booleans.py"


# Go Hiking
# Write a function that takes a string indicating energy level and weather


def go_hiking(energy, weather):
    if energy == 'tired' or weather == 'rainy':
        return False
    else:
        return True

def test_go_hiking():
    assert go_hiking('tired', 'rainy') == False
    assert go_hiking('tired', 'sunny') == False
    assert go_hiking('spry', 'rainy') == False
    assert go_hiking('spry', 'sunny') == True

# test_go_hiking()

# Double Digit
# Write a function that returns True if the number is a double digit

def double_digit(num):
    if 9 < abs(num) < 100:
        return True
    return False

def test_double_digit():
    assert double_digit(5) == False
    assert double_digit(55) == True
    assert double_digit(672) == False
    assert double_digit(-56) == True

# test_double_digit()

# Opposite
# Write a function that takes two integers, `a` and `b`, and returns `True` if one is positive and the other is negative, and return `False` otherwise.

def is_pos(num):
    return num >= 0

def opposite(a, b):
    if is_pos(a) == is_pos(b):
        return False
    else:
        return True


    # return a * b < 0


def test_opposite():
    assert opposite(10, -1) == True
    assert opposite(2, 3) == False
    assert opposite(-1, -1) == False

# test_opposite()

# Near 100
# Write a function that returns True if a number within 10 of 100.


def near_100(num):
    if num > 89 and num < 111:
        return True
    return False

def test_near_100():
    assert near_100(50) == False
    assert near_100(99) == True
    assert near_100(105) == True
    assert near_100(115) == False
# test_near_100()

# Maximum of Three
# Write a function that returns the maximum of 3 parameters.


def maximum_of_three(a, b, c):
    # return max(a,b,c)
    nums = [a, b, c]
    nums.sort()
    return nums[-1]

def test_maximum_of_three():
    assert maximum_of_three(5,6,2) == 6
    assert maximum_of_three(-4,3,10) == 10
test_maximum_of_three()