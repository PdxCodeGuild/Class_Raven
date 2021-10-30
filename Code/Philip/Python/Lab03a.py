'''We're going to average a list of numbers. Start with the following list, 
iterate through it, keeping a 'running sum', 
then divide that sum by the number of elements in that list. 
Remember len will give you the length of a list.

The code below shows how to loop through an array, and prints the elements one at a time.

nums = [5, 0, 8, 3, 4, 1, 6]

# loop over the elements
for num in nums:
    print(num)

# loop over the indices
for i in range(len(nums)):
    print(nums[i])'''
#Create list
nums = [5, 0, 8, 3, 4, 1, 6]
#Set total value
total = 0
#Create loop that will iterate through list
for x in nums:
#Add previous value to next value
    total = total + x
#Divide the total value by the length of the list
average = total / len(nums)
#Print the average
print(average)
