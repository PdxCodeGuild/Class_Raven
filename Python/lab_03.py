"""
Lee Colburn
Evening Bootcamp - PDX Code Guild
Lab 3
"""

# VERSION 1 - AVERAGE NUMBERS
"""We're going to average a list of numbers. 
Start with the following list, iterate through it, keeping a 'running sum'. 
then divide that sum by the number of elements in that list. 
Remember len will give you the length of a list."""

def ave_example(nums):
    print(f"We will iterate over this sample array: {nums}\n")
    running_value = 0
    running_list = []
    # loop over the elements
    for num in nums:
        running_value = running_value + int(num)
        running_list.append(num)
        running_length = len(running_list)
        running_average = running_value / running_length
        print(f"{num} is being added to the list: {running_list}.\n The current list has {running_length} elements. \n The current total of the list is {running_value} and average is {running_average}")



# VERSION 2 - USER DIRECTED
"""Ask the user to enter the numbers one at a time, 
putting them into a list. If the user enters 'done',
 then calculate and display the average."""

def user_directed(nums):
    running_value = 0
    running_list = []
    # loop over the elements
    for num in nums:
        running_value = running_value + int(num)
        running_list.append(num)
        running_length = len(running_list)
        running_average = running_value / running_length
    print(f"Entered Array: {running_list}.\n The list has {running_length} elements. \n The total of the list is {running_value} and average is {running_average}")



# MAIN MENU
complete = False
while not complete:
  # Select Option 1-Example, 2-User Input for Example Numbers, 3-Exit, 4+ Try Again
  start = int(input(f'\nPlease select from the following options:\n 1. Average Number Example \n 2. User Inputted Value Average\n 3. Exit Program \n\n Enter the number of your choice: \n'))

  # Allow user to escape
  if start == 3:
    print(f"\nClosing application.\n")
    complete = True
    break

  if start > 3:
    print(f'\n Try again:\n')
    continue
  
  # Direct user to appropriate function: 1-Palindrome, 2-Anagram, 3-Exit, 4+ Try Again
  if start == 1:
    nums = [5, 0, 8, 3, 4, 1, 6]
    ave_example(nums)

  if start == 2:
    nums = []
    done_with_input = False
    while not done_with_input:
      running_value = input("Enter a number or 'done': ")
      if running_value == "done":
        done_with_input = True
        continue
      nums.extend(running_value)
    user_directed(nums)