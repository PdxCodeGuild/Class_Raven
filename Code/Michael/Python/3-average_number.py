"""
PDX Code Guild Full Stack Bootcamp
->Lab 03
  Average Num
Michael B
"""
"""Version 1"""
nums = [5, 0, 8, 3, 4, 1, 6]  # Given test list.


def averager(table):
    total = 0  # Define total as an integer.
    for num in table:  # Loop through nums.
        total = total + float(num)  # Add value of all num in nums.
    try:
        average = total / len(table)  # Divide total by len of nums for average.
    except ZeroDivisionError:  # Shouldn't ever happen anymore, but happened during initial testing.
        return "Attempted to divide by zero. This is not possible."
    return average  # Return average from function.


print(f"\nVersion 1 average: {averager(nums)}.\n")  # Print results.

"""Version 2"""
print("Starting Version 2")
nums = []  # Define / Reset nums to an empty list.
enter_more_numbers = True  # Define invalid number
current_num = ""

while enter_more_numbers:  # Loop while user wants to enter more numbers.
    try:  # Catch errors.
        while not current_num.isdigit():  # Run while current_num is not a digit.
            if current_num.lower() == "done":
                if len(nums) == 0:  # If there are not any numbers in the nums list.
                    current_num = input(
                        "\nError: You must enter at least one number.\n\nPlease enter a number to add to averages or 'done' to finish: "
                    )
                else:  # If there are numbers, and done is entered, break.
                    enter_more_numbers = False
                    break
            elif current_num == "":  # Initial state, initial question to user.
                current_num = input(
                    "Please enter a number to add to averages or 'done' to finish: "
                )
            else:  # Word that is not done, or a number has been entered.
                current_num = input(
                    f"\n{current_num} is not a digit.\n\nPlease enter a number to add to averages or 'done' to finish: "
                )
        if not current_num.lower() == "done":
            nums.append(current_num)  # Add it to the list.
        current_num = ""
    except KeyboardInterrupt:  # check for CTRL+C to quit.
        quit()

print(f"\nVersion 2 average: {averager(nums)}.\n")  # Print results.
