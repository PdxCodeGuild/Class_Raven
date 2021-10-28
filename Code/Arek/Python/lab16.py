"""
Part 1 - Linear Search

Implement linear search, which simply loops through the given list and check if each element is equal to the value we're searching for. 
If it is, return the index at which it was found, otherwise, return a value indicating that it was not found.
"""


"""def linear_search(nums, value):
    if value in nums:
        return nums.index(value)
    else:
        return f'value not found'
# index 0  1  2  3  4  5  6  7
nums = [1, 2, 3, 4, 5, 6, 7, 8]
index = linear_search(nums, 3)
print(index) # 2
"""


"""

Part 2 - Binary Search

Implement binary search, which requires that a list is sorted and divides its search range in half each iteration until it finds its target.

    Begin by defining two indices: low and high. Initialize low as the lowest index in the list and high as the highest.
    Loop while low is less then high.
        For each iteration, calculate a third index mid which is in the middle between low and high
        If the element at mid is the one you're searching for, return it, otherwise check is the target value is less than or greater than the one at mid. 
        If it's less, make high equal to mid and loop.
        If it's greater, make low equal to mid and loop. If the loop terminates without returning, return a value indicating that it was not found.

def binary_search(nums, value):
    l = nums[0]
    h = nums[len(nums) - 1]
    
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
nums = [1, 2, 3, 4, 5, 6, 7, 8]
index = binary_search(nums, 3)
print(index) # 2
"""



"""
Part 3 - Bubble Sort

Bubble sort is one of the simplest and least efficient sorting algorithms. 
We repeatedly loop over the list, comparing each number to the one next to it, and swapping them if needed.

"""

def bubbleSort(nums):
    long = len(nums)
    while True:
        for i in range(long):
            if nums[i + 1] > long - 1:
                break
            elif nums[i] > nums[i + 1]:
                x = nums[i + 1]
                nums[i + 1] = nums[i]
                nums[i] = x   
        break
    return nums
    
                
nums = [1, 2, 4, 3, 6, 5, 7, 8]
index = bubbleSort(nums)
print(index)





