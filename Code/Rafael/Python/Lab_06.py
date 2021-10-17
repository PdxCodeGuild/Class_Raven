# Lab_06 Credit Card Validation

user_input = list(input('Enter 16 single digits from 0-9 with no spaces: '))

#1. Convert the input string into a list of ints
user_input = list(map(int, user_input)) 

# 2. Slice off the last digit. That is the check digit.
check_digit = user_input.pop()

# 3. Reverse the digits.
user_input.reverse() 

# 4. Double every other element in the reversed list.
user_input = user_input[0] * 2, user_input[1], user_input[2] * 2, user_input[3],  user_input[4] * 2, user_input[5], user_input[6] * 2, user_input[7], user_input[8] * 2, user_input[9], user_input[10] * 2, user_input[11],  user_input[12] * 2, user_input[13], user_input[14] * 2 

user_input = list(user_input) 

# 5. Subtract nine from numbers over nine.
if user_input > 9:
	user_input = user_input - 9 
    
 # 6. Sum all values.        
user_input = sum(user_input) 

# 7. Take the second digit of that sum.
if user_input[1] == check_digit:
    print("valid")

# 8. If that matches the check digit, the whole card number is valid.
else:
    print("invalid")

# 4556737586899855

