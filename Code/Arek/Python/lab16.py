"""
Part 1 - Linear Search

Implement linear search, which simply loops through the given list and check if each element is equal to the value we're searching for. 
If it is, return the index at which it was found, otherwise, return a value indicating that it was not found.
"""

# removed the .index method to remove complexity
"""def linear_search(nums, value):
    long = len(nums)
    for i in range(long):
        if nums[i] == value:
            return i
    return f"Value not found"
    
        
# index 0  1  2  3  4  5  6  7
nums = [1, 2, 3, 4, 5, 6, 7, 8]
index = linear_search(nums, 3)
print(index) # 2"""



"""

Part 2 - Binary Search

Implement binary search, which requires that a list is sorted and divides its search range in half each iteration until it finds its target.

    Begin by defining two indices: low and high. Initialize low as the lowest index in the list and high as the highest.
    Loop while low is less then high.
        For each iteration, calculate a third index mid which is in the middle between low and high
        If the element at mid is the one you're searching for, return it, otherwise check is the target value is less than or greater than the one at mid. 
        If it's less, make high equal to mid and loop.
        If it's greater, make low equal to mid and loop. If the loop terminates without returning, return a value indicating that it was not found.
"""
"""def binary_search(nums, value):
    l = 0
    h = len(nums) - 1 # changed l and h to the the indices instead of the values of the indices
    
    while l < h:
        m = (l + h) // 2
        if nums[m] < value:
            l = m
        elif nums[m] > value:
            h = m         
        else:
            return m            
    return 'unsuccessful'
    
#       0  1  2  3  4  5  6  7
nums = [11, 2, 3, 44, 5, 6, 7, 8] # if this list is not sorted we will get an error with the numbers that are not in the correct order
#nums = sorted(nums)
index = binary_search(nums, 11)
print(index) # 2"""




"""
Part 3 - Bubble Sort

Bubble sort is one of the simplest and least efficient sorting algorithms. 
We repeatedly loop over the list, comparing each number to the one next to it, and swapping them if needed.

"""

"""def bubbleSort(nums):
    long = len(nums)
    reps = 0
    while reps < long + 1:
        reps += 1
        for i in range(1, long):
            x = nums[i - 1]
            
            if nums[i - 1] > nums[i]: # if nums[i] is changed then it will be skipped over next time
                nums[i -1] = nums[i]
                nums[i] = x
        
    return nums                
                   
                
        
    
                   
nums = [2, 4, 99, 45, 6, 5, 88, 8]
index = bubbleSort(nums)
print(index)"""



nums = [2, 4, 99, 45, 6, 5, 88, 8]

def bubble_sort(nums):
    long = len(nums) - 1
    
    while True:
        swapped = False
        for i in range(long):
           if nums[i] > nums[i + 1]:
                check = nums[i]
                nums[i] = nums[i + 1]
                nums[i + 1] = check
                swapped = True
        if swapped == False:
            break

    return nums

print(bubble_sort(nums))
    






