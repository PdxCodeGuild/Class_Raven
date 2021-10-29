
# Lab_16 Searching and Sorting
# Rafael Medina

"""
"""

#Part 1 - Linear Search

# Linear search method also called sequential, it search searches the list one by one until a condition is met. 

nums = [1, 2, 3, 4, 5, 6, 7, 8]

# Reference: https://pythonguides.com/python-binary-search/ Needed a guide after trying countless combinations for the print statements to show with return i

input_num = int(input("\nEnter a number to search in 'nums' index: ")) # int conversion needed to search index otherwise it returns not found

def linear_search(nums,search):

    for i in range(len(nums)): # For the integer i within the lists entire range/length.

        if nums[i] == search: # If i is in the list 'nums' then it returns i.

            return i # If i is in nums list range/length then return i.

    return -1 # If i is not in range/length of nums list return -1.

index = linear_search(nums,input_num) # function to find the index

# Return of -1 needs boolean before return i because i is inaccesible outside the function, so -1 gets the print boolean, else will print the input # and the index location "index = linear_search(nums,input_num)"

if index != -1:
    print(f"\nThe number {input_num} was found at index: {index}\n")
else:
    print(f"\nThe number {input_num} was not found within the index 'nums'.\n")




# Part 2 - Binary Searching

# 1st define low, high indices, and mid too, then loop while low is <= high. Calculate each time the mid index. If int/index not found at first then keep checking if the target is < or > than the mid. if it's <, make high = mid & loop. If it is >, make low = mid and continue the loop until the it returns the searched int or returns -1. 

# This could also be done with the recursive method for a list. "This means that the function will continue to call itself and repeat its behavior until some condition is met to return a result."

"""
list - list
length- length # Length not needed if converting the list into a len function.
value - value
"""
list = [1, 2, 3, 4, 5, 6, 7, 8]

value = int(input("\nEnter a number to search in 'nums' index: "))

def binary_search(list, value): 

    low = 0 # start left @ int 1 (left)
    high = len(list) - 1 # start right @ int 8 (right)
    mid = 0
    while low <= high: # loop while low is < high.
        mid = (low + high) // 2 # Mid is low plus high then floor divised by 2.
        if list[mid] < value: # If the middle number is less than input then low is equal to the mid plus 1.
            low = mid + 1 # Searches linear left to right
        elif list[mid] > value: # The opposite when going from high, -1. Use Elif and not if for boolean, otherwise it will return the int index one position higher. Should not be set to >= just >.
            high = mid -1 #Searches linear right to left
        else:
            return mid # else return the remaining int after high and low have exhausted their bi-directional linear searches. If not fount in mid then return False -1 outside range. If found in middle, return searched int value. 
    return -1

index = binary_search(list, value) # Class Raven example shows "linear_search" changed to binary_search to match the binary function parameter.

if index != -1:
    print(f"\nThe number {value} was found at index: {index}\n")
else:
    print(f"\nThe number {value} was not found within the index 'nums'.\n")
    



#Part 3 - Bubble Sort

# Bubble sort goes through a list and checks wether the current element is larger or smaller than the next element. This is considered on of the most inneficient methodologies I read.

# A good exmaple on how it is visualized https://visualgo.net/en/sorting

# NOTE: to self, double check on python tutor to visualize.

unsorted = [20, 4, 7, 1, 59, 77, 12345, 432, 2]

def bubble_sort(unsorted):
  
    # designates the length of the unsorted list to a variable to prevent typerrors.
    n = len(unsorted) # 9 indexes identified.
    for i in range(n - 1): # This sets the end of the range up to the last item on the list. 
        turns = 0 # amount of 0  means it starts without a swap.
        for x in range(n - 1): # Again sets the end of the list.
            if unsorted[x] > unsorted[x + 1]: # The x variable checks to see if the next number is greater from left to right.
                temp_var = unsorted[x] # Starts at index 0 int(20), uses a temporary variable that will not be printed to go through the steps.
                unsorted[x] = unsorted[x + 1] 
                unsorted[x + 1] = temp_var # temporary value to keep the check going
                turns =  1 # number of swaps per loop
        
        if turns == 0: # All list integers bo longer have greater than to their left, loop ends.
            break
    return unsorted # if indented one more time the sequence will be out of order, needs to be indented along with the begining of the function. 


sorted_list = bubble_sort(unsorted) # Changes the print variable name to be more specific to what is being called to print.

print(sorted_list)
    
# The result is [1, 2, 4, 7, 20, 59, 77, 432, 12345]

         






