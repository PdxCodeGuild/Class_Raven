# Lab_06 Credit Card Validation
#Rafael Medina

"""
NOTE: Need to rework this to re-do step #7 

Feedback:

"It looks like step 7 isn't doing the correct operations. The instructions say to take the second digit of the transformed CC number and compare it to the check number. The way the code is written, it's converting used_digits to the check_digit and then comparing them, so they're always going to be equal

used_digits = str(used_digits)
used_digits = check_digit
print('#7', used_digits)

# 8. If that matches the check digit, the whole card number is valid.

if used_digits == check_digit: # this will always be True
    print('#8',"Valid!")"
"""


# 4556737586899855

user_input = list(input('enter 16 single digits from 0-9 with no spaces: ')) 

# 1. Convert the input string into a list of ints.
user_input = list(map(int, user_input))
print('#1', user_input)

# 2. Slice off the lastdigit. That is the check digit.
check_digit = user_input.pop()
print('#2', user_input)

# 3. Reaverse the digits.
user_input.reverse()
print('#3', user_input)

used_digits = []
# 4. Double every other element in the reversed list.
# Enumerate allows to use the index as a list integer to prevent tyeerror.
for index, digit in enumerate(user_input): 
    
    if index % 2 == 0:
        used_digits.append(int(digit) * 2 )
  
    else:
        used_digits.append(int(digit))

print('#4', used_digits)

# 5. Subtract 9 from numbers over 9
# iterate through the list to prevent; TypeError: unsupported operand type(s) for -: 'list' and 'int' 
for x in range(len(used_digits)):
    if used_digits[x] > 9:
        used_digits[x] = used_digits[x] - 9
       
print('#5', user_input)

# 6. Sum all the values. 
used_digits = sum(used_digits) 
print('#6', used_digits)

# 7. Take the second digit of that sum.
used_digits = str(used_digits)
used_digits = check_digit
print('#7', used_digits)

# 8. If that matches the check digit, the whole card number is valid.

if used_digits == check_digit:
    print('#8',"Valid!")

elif used_digits != check_digit:
    print('#8', "invalid")


# 4556737586899855