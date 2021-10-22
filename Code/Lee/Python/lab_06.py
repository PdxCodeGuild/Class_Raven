"""
Lee Colburn
Evening Bootcamp - PDX Code Guild
Lab 6
"""

'''
Let's write a function which returns whether a string containing a credit card number is valid as a boolean. The steps are as follows:
sample string: 4556737586899855
'''

def check_cc(cc_string):
    # 1 - Convert the input string into a list of ints
    cc_string = list(map(int, cc_string))
    print(f"Step 1 - Convert the input string into a list of ints: {cc_string}")

    # 2 - Slice off the last digit. That is the check digit.
    check_digit = cc_string.pop()
    print(f"Step 2 - Slice off the last digit. That is the check digit: {check_digit}")

    # 3 - Reverse the digits.
    reversed_list = cc_string[::-1] # slicer: [start:stop:step] 
    print(f"Step 3 - Reverse the digits: {reversed_list}")

    # 4 - Double every other element in the reversed list.
    doubled_list = list(reversed_list)
    for i in range(len(doubled_list)):
        if i % 2 == 0:
            doubled_list[i] = doubled_list[i]*2
    print(f"Step 4 - Double every other element in the reversed list: {doubled_list}")

    # 5 - Subtract nine from numbers over nine.
    subtract_nine = doubled_list
    for i in range(len(subtract_nine)):
        if subtract_nine[i] > 9:
            subtract_nine[i] = subtract_nine[i]-9
    print(f"Step 5 - Subtract nine from numbers over nine: {subtract_nine}")

    # 6 - Sum all values.
    sum_of_values = int(0)
    for i in range(len(subtract_nine)):
        sum_of_values = sum_of_values + subtract_nine[i]
    print(f"Step 6 - Sum all values: {sum_of_values}")

    # 7 - Take the second digit of that sum.
    string_of_values = sum_of_values
    string_of_values = str(string_of_values)
    string_of_values = list(string_of_values)
    print(f"Step 7 - Take the second digit of that sum: {string_of_values}")

    # 8 - If that matches the check digit, the whole card number is valid.
    final_value = string_of_values.pop()
    final_value = int(final_value)
    print(f"Step 8 - If digit matches the check digit, the whole card number is valid: {final_value}")
    if final_value == check_digit:
        print(f"\n YES - Check values '{final_value}' and '{check_digit}' match. This is a valid Credit Card number \nExiting to main menu:")
        return complete == True
    else:
        print(f"\n NO - Check values '{final_value}' and '{check_digit}' do not match. This is NOT a valid Credit Card number \nExiting to main menu:")

complete = False
while not complete:
  # Select Option 1-Check for CC, 2-Exit, 3+ Try Again
  start = int(input(f'\nPlease select from the following options:\n 1. Check for CC Number \n 2. Exit Program \n\n Enter the number of your choice: \n'))

  # Allow user to escape
  if start == 2:
    print(f"\nClosing application.\n")
    complete = True
    break

  if start > 2:
    print(f'\n Try again:\n')
    continue
  
  # Direct user to appropriate function: 1-Palindrome, 2-Anagram, 3-Exit, 4+ Try Again
  if start == 1:
    cc_string = input("\nPlease enter the the Credit Card Number to check: ")
    check_cc(cc_string)

