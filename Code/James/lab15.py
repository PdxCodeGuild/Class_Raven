""" Linear search """


nums = [1, 2, 3, 4, 5, 6, 7, 8]

def linear_search(list, value):
    match = 'No match found'
    for i in range(len(nums)):
        if nums[i] == value:
            match = i 
    print(match)
    return match


#linear_search(nums, 3)


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
            return middle
        
        if nums[middle] > target:
            high = middle - 1
        
        else:
            low = middle + 1
            
        
        
        

#print(binary_search(nums, 3))






""" bubble sort """

bubble_nums = [64, 34, 25, 12, 22, 11, 90]


def bubble_sort(array):
    
    swapped = True

    while(swapped):
        swapped = False
        for i in range(len(array) - 1): # will run until second to last item in list
            if array[i] > array[i + 1]:
                # Swap the item in the list if it's greater then it's neighbor.
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True
    return array


print(bubble_sort(bubble_nums))

    
    






