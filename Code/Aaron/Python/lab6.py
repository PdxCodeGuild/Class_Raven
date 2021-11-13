# Lab 6: Credit Card Validation
# Let's write a function which returns whether a string containing a credit card number is valid as a boolean. The steps are as follows:

# Convert the input string into a list of ints
# Slice off the last digit. That is the check digit.
# Reverse the digits.
# Double every other element in the reversed list.
# Subtract nine from numbers over nine.
# Sum all values.
# Take the second digit of that sum.
# If that matches the check digit, the whole card number is valid.
# For example, the worked out steps would be:

# 4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5
# 4 5 5 6 7 3 7 5 8 6 8 9 9 8 5
# 5 8 9 9 8 6 8 5 7 3 7 6 5 5 4
# 10 8 18 9 16 6 16 5 14 3 14 6 10 5 8
# 1 8 9 9 7 6 7 5 5 3 5 6 1 5 8
# 85
# 5
# Valid!





def get_total_from_list(list):
  total = 0
  for i, x in enumerate(list):
    total += list[i] 
  return total

def get_last_digit_from_string(number, n):
    number = str(number)
    nDigit = number[n]
    return int(nDigit)

def get_cc_input():
    ccNumber = input('Please provide us with a credit card #:')
    valid_CC_length = False
    while valid_CC_length == False:
        if (len(ccNumber) != 16):
            ccNumber = input('Your CC length is invalid try again:')
        elif (len(ccNumber) == 16):
            #print('This is a valid CC# length')
            valid_CC_length = True
            return ccNumber

def double_ever_number_in_list(list):
  for i, x in enumerate(list):
    if (i % 2 == 0):
      list[i] = list[i] * 2
  return list

def subract_nine_from_numbers_over_nine_list(list):
  for i, x in enumerate(list):
    if(list[i] > 9):
      list[i] = list[i] - 9
  return list
  
ccNumber = get_cc_input()
ccNumberList = [int(x) for x in str(ccNumber)]
checkDigit = ccNumberList[-1]
del ccNumberList[-1]

# reverse list
ccNumberList.reverse()

# double every other number in list
ccNumberList = double_ever_number_in_list(ccNumberList)

# Subtract nine from numbers over nine.
ccNumberList = subract_nine_from_numbers_over_nine_list(ccNumberList)

# Get Total from List
total = get_total_from_list(ccNumberList)

# ccNumberInt = int(ccNumber)
# print(ccNumberList)
# print(total)
lastDigit = get_last_digit_from_string(total, 1)

# print(get_last_digit_from_string(total,1))
# print(checkDigit)

if (lastDigit == checkDigit):
  print ("Valid!")
else: 
  print ("Invalid!")