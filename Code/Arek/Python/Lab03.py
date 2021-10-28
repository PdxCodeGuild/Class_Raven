"""
Lab 3: Average Numbers

We're going to average a list of numbers. Start with the following list, iterate through it, 
keeping a 'running sum', then divide that sum by the number of elements in that list. Remember len will give you the length of a list.

The code below shows how to loop through an array, and prints the elements one at a time.

nums = [5, 0, 8, 3, 4, 1, 6]

# loop over the elements
for num in nums:
    print(num)

# loop over the indices
for i in range(len(nums)):
    print(nums[i])

    Version 2

Ask the user to enter the numbers one at a time, putting them into a list. If the user enters 'done', then calculate and display the average. The following code demonstrates how to add an element to the end of a list.

nums = []
nums.append(5)
print(nums)

Below is an example input/output:

> enter a number, or 'done': 5
> enter a number, or 'done': 3
> enter a number, or 'done': 4
> enter a number, or 'done': done
average: 4



"""


"""#Version 1
nums = [5, 0, 8, 3, 4, 1, 6]
elements = len(nums)
#setting the total to 0 to build off of
total = 0
#setting a variable to stand in for the indexes of all elements inside num 
index_num = 0

for i in nums:
    total += nums[index_num]
    #we are increasing index_num by 1 each time so that way the loop iterates through each value in the list 'nums'
    index_num += 1
#we are getting the average by dividing the total by the number of elements inside nums
average = total / elements
print(f"The average of the list is {average}")
"""

nums = []
while True:
    user_num = input("Please enter a number or type 'done' to create the list: ")
    # this conditional is in place because if we convert user_num into an integer first and they enter 'done' we will get an error
    if user_num != 'done':
        nums.append(int(user_num))
    else:
        elements = len(nums)
        #setting the total to 0 to build off of
        total = 0
        #setting a variable to stand in for the indexes of all elements inside num 
        index_num = 0

        for i in nums:
            total += nums[index_num]
            #we are increasing index_num by 1 each time so that way the loop iterates through each value in the list 'nums'
            index_num += 1
        #we are getting the average by dividing the total by the number of elements inside nums
        average = total / elements
        print(f"\nThe average of the list is {average}")
        break



    
  
    

