# Lab_06 Credit Card Validation

user_input = list(input('Enter 16 single digits from 0-9 with no spaces: '))


#1. Convert the input string into a list of ints
user_input = list(map(int, user_input))

print(user_input)

# 2. Slice off the last digit. That is the check digit.
check_digit = user_input.pop()
print(user_input)

# 3. Reverse the digits.
user_input.reverse() 
print(user_input)

# 4. Double every other element in the reversed list.
used_digits = []

for index, digit in enumerate(user_input): # enumerate allows to use the index as a list item integer to prevent typerror.
    
    if index % 2 == 0: #Takes 'even' numbers starting from index [0], [2], ... and later appends them to used_digits list after conditional minus 9 if greater than 9
        
        even_digits = int(digit) * 2 # multiplies all 'even' indexes in list by 2
        
# 5. Subtract nine from numbers over nine.    
    if even_digits > 9:
        even_digits = int(even_digits) - 9
        used_digits.append(even_digits)
    else: # Takes 'odd' numbers starting from [1], [3], ... and appends them to used_digits
        used_digits.append(int(digit))
    
"""
user_input = user_input[0] * 2, user_input[1], user_input[2] * 2, user_input[3],  user_input[4] * 2, user_input[5], user_input[6] * 2, user_input[7], user_input[8] * 2, user_input[9], user_input[10] * 2, user_input[11],  user_input[12] * 2, user_input[13], user_input[14] * 2
"""
"""
if user_input > 9:
    user_input = user_input - 9 
"""

print(used_digits)

 # 6. Sum all values.   
used_digits = sum(used_digits)


print(used_digits)


used_digits = str(used_digits)

# 7. Take the second digit of that sum.
used_digits = used_digits[1]

print(used_digits)

if used_digits == check_digit:
    print("Valid!")

# 8. If that matches the check digit, the whole card number is valid.
else:
    print("invalid")

# 4556737586899855



