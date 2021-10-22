
'''   Version 2
    
Ask the user to enter the numbers one at a time, putting them into a list. If the user enters 'done', 
then calculate and display the average. 
The following code demonstrates how to add an element to the end of a list.

nums = []
nums.append(5)
print(nums)
Below is an example input/output:

> enter a number, or 'done': 5
> enter a number, or 'done': 3
> enter a number, or 'done': 4
> enter a number, or 'done': done
average: 4'''


#Build an empty list to store numbers
nums=[]
#Create a while infinite loop
while True:
    #Take user input as a variable
    number=(input('Enter a number or "done" to quit: '))
    #Create the condition for quiting
    if number == 'done':
        #If quit condition activiated, print list
        print(nums)
        #Complete quit condition
        break
    #If loop continues
    else:
        #Convert number to an integer
        number=int(number)
        #Append the number to the list
        nums.append(number)
#Set the value for total variable
total = 0
#Build the for loop to iterate through the nums list
for x in nums:
#Build the total by adding the next value to the total
    total = total + x
#Determine the average by dividing the total by the list length
average = total / len(nums)
#Print the average result
print(average)