def linear_search(nums, value):
    current_index = 0    # Declare variable for keeping track of the current index

    for x in range(len(nums)):    # Loop over all index of nums
        if value == nums[current_index]:    # If the input is equal to nums at the specified index, return the specified index
            return current_index
        current_index += 1
    return None    # If the current index never matches the value, eventually return None

def binary_search(nums, value):
    low = nums[0]
    high = nums[-1]

    if value == nums[0]:    # Accounting for the beginning since there can't be a low, mid, and high at the start
        return 0
    elif value == nums[-1]:    # Same thing for the end, returns the length of the list minus 1 to match the current index
        return (len(nums) - 1)

    while low <= high:    # Starts the loop 
        mid = int((low + high) / 2)    # Convert using the int, int is used to "round" here
        
        if nums[mid] < value:
            low = mid + 1
        elif nums[mid] > value:
            high = mid - 1
        else:
            return mid
    return None

#def bubblesort(nums):
    #for i in range(len(nums)):
        #for x in range(len(nums) - 1 - i):    # i is used to prevent the bubblesort from looping over index which have been sorted already.
            #if nums[x] > nums[x + 1]:            # range 0 to 8 minus the last index in the list AND i.
                #nums[x], nums[x + 1] = nums[x + 1], nums[x]    # The new index are swapped in place of each other.
    #return nums
# index 0  1  2  3  4  5  6  7

def bubblesort(nums):
    length = len(nums)

    while True:
        swapped = False

        for i in range(length - 1):    # Counter measure to not go out of index
            if nums[i + 1] < nums [i]:
                nums[i + 1], nums[i] = nums[i], nums[i + 1]
                swapped = True
        
        if swapped == False:
            return nums

nums = [8, 7, 6, 5, 4, 3, 2, 1]
index = bubblesort(nums)
print(nums)