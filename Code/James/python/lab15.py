""" Linear search """
import random

nums = [1, 2, 3, 4, 5, 6, 7, 8]

def linear_search(list, value):
    match = 'No match found'
    for i in range(len(nums)):
        if nums[i] == value:
            match = i + 1 # added + 1 to give the proper index 
    print(match)
    return match


linear_search(nums, 3)


""" binary search """
def binary_search(list, target):

    nums.sort()
    low = min(nums)
    #print(low)
    high = max(nums)
    #print(high)
    middle = (low + high) // 2
    
    while low <= high:
        middle = (low + high) // 2
        
        if nums[middle] == target:
            return middle + 1 # added + 1 to give the proper index 
        
        if nums[middle] > target:
            high = middle - 1
        
        else:
            low = middle + 1
            
        
        
        

#print(binary_search(nums, 5))






# """ bubble sort """
# random.shuffle(nums) # generating a random list to be used for the bubble sort function



def bubble_sort(array):
    print('First list is inital list')
    print(nums)
    swapped = True

    while(swapped): # while swap is True run the code.
        swapped = False
        for i in range(len(array) - 1): # will run until second to last item in list
            if array[i] > array[i + 1]:
                # Swap the item in the list if it's greater then it's neighbor.
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True
    return array


# print(bubble_sort(nums))

    
    






