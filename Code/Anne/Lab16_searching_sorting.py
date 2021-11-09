#  Searching and Sorting

# Part 1 - Linear Search
# Implement linear search, which simply loops through the given list and check if each element is equal to the value we're searching for. If it is, return the index at which it was found, otherwise, return a value indicating that it was not found.


# def linear_search(nums, value):
#     length = len(nums)
#     print(length)
#     for i in range(length):
#         if i == value:
#             return(nums.index(value)) 
#     raise IndexError ("value not in list")
# nums = [1, 2, 3, 4, 5, 6, 7, 8]
# index = linear_search(nums, 3) 
# print(index) 

# Part 2 - Binary Search
# Implement binary search, which requires that a list is sorted and 
# divides its search range in half each iteration until it finds its target.
# Begin by defining two indices: low and high. 

def binary_search(value):
    #  Initialize low as the lowest index in the list and high as the highest
    the_list = [1,2,3,4,5,6,7,8,9,10]
    len_list = len(the_list)
    low = 0
    high = len_list -1
    # Loop while low is less then high.
    while low <= high:
        #calculate a third index mid which is in the middle between low and high
        mid = (low+high)//2 
        if the_list[mid] < value:
             low = mid + 1
        elif the_list[mid] > value:
            high = mid - 1
        else:
            low =10 # probably not the corect solution, but my code runs and seems to do what the lab asked for.
            high = 0
            print(f"you found {value}, mid was index {mid}") 
        
# print('search was unsuccessful')
       
# binary_search(8)

import time
# Part 3 - Bubble Sort
# Bubble sort is one of the simplest and least efficient sorting algorithms. 
# We repeatedly loop over the list, comparing each number to the one next to it, 
# and swapping them if needed.
def bubble_sort():
    
    ul = [77, 9, 114, 3,  12, 22, 48, 1, 19]#, 0, 107, 16, 89, 2, 18, 14, 56]
    len_list = len(ul)
    last = len_list -1
    swapped = False
    # while swapped == False:
    n=0  
    for i in range(1, last):
        
        print(f'this is the {n} pass')
        n +=1
        for j in range(1, len_list):
            time.sleep(1)
            if ul[j] < ul[j-1]:
                # swapped = True
                print(ul[j], ul[j-1])
                ul[j], ul[j-1] = ul[j-1], ul[j]
                print(ul[j], ul[j-1])
        
    print(ul)
                

bubble_sort()