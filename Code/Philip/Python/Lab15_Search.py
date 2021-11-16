'''Lab15 Searching and Sorting
By Philip Bartoo
10/27/2021'''

#Part 1 Linear Search

#Set up a function for a Linear Search with parameters for a list of numbers and a value to search for
def linear_search(nums, value):
#Set an index variable at 0 to track each iteration of the loop
    index = 0
#Establish a while loop that checks if the current iteration is less than the length of the list
    while index < len(nums):
#Logic statement to compare if the list value at the current index is equal to the value being searched for
        if nums[index] == value:
#If the logic evaluates to True, return the index
            return index
#If the logic evaluates to False, increment the index by +1 and continue the loop
        else:
            index += 1

#Provide the list input for the function
nums = [1, 2, 3, 4, 5, 6, 7, 8]
#Call the function, with the list and the value as attributes
index = linear_search(nums, 3)
#Print the results
print(index)


#Part 2 Binary Search

#Set up a function for a Binary Search with parameters for a list of numbers, the length of the list of numbers, and a value to search for
def super_search(A,n,T):
#Establish a low indicies and initialize as the lowest index in the list
    low = 0
#Establish a high indicies and initialize as the highest index in the list
    high = n - 1
#Create a loop that runs while the low indicides is less than the high indicies
    while low <= high:
#Calculate a middle index between high and low (via floor division)
        middle = ((low + high) // 2)
#If the value at the middle index is less than the value being searched for, reset the low value as the middle + 1
        if A[middle] < T:
            low = middle + 1
#Conversely, if the value at the middle index is greater than the value being searched for, reset the high value as the middle - 1
        elif A[middle] > T:
            high = middle - 1
#If neither of the above are true, this must mean the middle index value is equal to the searched for value, in which case we will return the index of the value
        else:
            return middle
#If there is a problem, return 'unsuccessful' to alert the user
    return 'unsuccessful'

#The input for the list, the list length and the searched for value are included
A = [1, 2, 3, 4, 5, 6, 7, 8]
n = len(A)
T = 6

#Call the function and store and print the result
index = super_search(A,n,T)
print(index)


#Part 3 Bubble Sort

#Set up a function that will Bubble Sort through a list using a list as the parameter
def bubbleSort(A):
#Establish a variable for the length of the list
    n = len(A)
#Create a loop that runs while True
    while True:
#Establish a variable that will stop the loop once the sorting is complete
        swapped = False
#For each item in the list sequentially run a logic check to see if the list value at the next index is less than the current index
        for i in range(n-1):
            if A[i+1] < A[i]:
#If the logic statement evaluates to True, then swap the positions of the current value with the next value
                A[i+1], A[i] = A[i], A[i+1]
#If the swap has occurred, update the swapped variable to True
                swapped = True
#Use logic to stop the loop once swapped evaluates to False and return the list in its new order
        if swapped == False:
            return A

#The input for the list, the list length
A = [8, 1, 7, 9, 22, 6, 15, 5]
n = len(A)

#Call the function, provide attributes, store as a variable, and print
sortedlist = (bubbleSort(A))
print(sortedlist)

