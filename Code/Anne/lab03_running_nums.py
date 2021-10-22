# We're going to average a list of numbers
# iterate through the list, keeping a 'running sum'
# divide that sum by the number of elements in that list. 
# Remember len will give you the length of a list.

# version 1

# nums = [5, 0, 8, 3, 4, 1, 6]
# running_sum = []

# sum = 0
# for num in nums:
#     sum = (num + sum)
#     print(sum)
#     running_sum.append(sum)
# average = running_sum[-1] / len(running_sum)
# print(average)



# Version 2
# Ask the user to enter the numbers one at a time, putting them into a list. 
# If the user enters 'done', then calculate and display the average.

nums = []
running_sum = []
sum = 0
next_num = ""
on = True
while on == True:
    #get the number
    next_num = input("Enter a number or 'done':  ")
    if next_num != "done":
        next_num = int(next_num)
        
    # add the number to nums
        nums.append(next_num)
    #check it
        print(nums)

    else:   
    
        on = False
        
        for num in nums:
            sum = (num + sum)
            print(sum)
            running_sum.append(sum)
        average = running_sum[-1] / len(running_sum)
        print(f'Average of the numbers given is {average}.')


