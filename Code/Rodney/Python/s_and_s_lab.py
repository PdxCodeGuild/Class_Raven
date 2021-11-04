

## part 1: linear search---------------------------------------------------------------------------------

def linear_search(nums, value):  # defining function with nums and value as paramaters 
	
	for i in range(len(nums)):  # for loop to loop through numbers in nums list 
	    if nums[i] == value:  ## if the value of the index in the list equals value entered by user, then true 
	        index_value = i  # we assign a variable to i 
	        break
	    else:
	        index_value = "Value's index not found" ## if value is not in list, we let user know 
	return index_value
	
nums = [1, 2, 3, 4, 5, 6, 7, 8]
index = linear_search(nums, 2)
print(index)


## part 2: binary search---------------------------------------------------------------------------------

def binary_search(nums, value):
    
    low_index = 0   ## setting a low index which starts at 0, high index which is length of list - 1, if list is 10 numbers long, index 9 is last index since indices start at 0 
    high_index = len(nums) - 1
    
    while (low_index <= high_index) == True:  # if the low index is less than or equal to high index, continue 
        middle_index = (high_index + low_index)//2  # middle index will be high + low // 2, so if high is 9 and low is 0(9 + 0 = 9 // 2 = 4)
        if nums[middle_index] < value: # if middle index value is lower than value we make new low index the middle index + 1 since we know the value we're looking for is at least that index or higher 
            low_index = middle_index + 1 
        elif nums[middle_index] > value:  # complete opposite of previous if statement, moving high index down one since we know value we're looking for is that index or lower 
            high_index = middle_index - 1
        else:
            return middle_index  # eventually the middle, high, and low index will be equal which will bring us to else statement in function and return middle index, which is value we're looking for 
    if low_index > high_index:
            no_value = "Value's index not found"  ## if low index is higher than high index, means value did not fall in our list and we let user know 
            return no_value                       ## say list was [2, 5, 7], user looking for 8, eventually low index = middle index + 1 will be 7 and high index will be 5 


search_list = [1, 2, 3, 4, 5, 6, 7, 9]   
index = binary_search(search_list, 7)
print(index) 

## part 3: bubble sort---------------------------------------------------------------------------------


list_to_sort = [12, 0, 2, 98, 4, 698, 1, 0, 0, 74] ## random list to sort 
list_length = len(list_to_sort) - 1  # we take length of list to sort - 1 
swapped = True

while swapped == True:  # while swap is true, run loop
    swapped = False # set swap to false 
    for i in range (list_length): # this will 'do something' so many times, which in this case is the number of indices in list 
        if list_to_sort[i] > list_to_sort[i + 1]:  ## using our list, say i is index 0, so i + 1 is index 1, in our list those are values: 12 and 0
            list_to_sort[i], list_to_sort[i + 1] = list_to_sort[i + 1], list_to_sort[i]  # 12 is greater than 0, so this line tells us to switch 0 to index 0 and 12 to index 1 
            swapped = True
               # eventually when swapped will be set to false: the list will be iterated all the way through each indice and
print(list_to_sort) ## there will be no values that need to be swapped, so swapped will continue to be false and then break the loop when the list is iterated through the last time 

