"""
Lee Colburn
Evening Bootcamp - PDX Code Guild
Lab 16 - Search
"""

"""Part 1 - Linear Search
Implement linear search, which simply loops through the given list and check if each element is equal to the value we're searching for. 
If it is, return the index at which it was found, otherwise, return a value indicating that it was not found.
"""
def linear_search(nums, value):
    for i in range(len(nums)):
        if nums[i] == value:
            return i
        if i == (len(nums)-1):
            return "Number not found."
  
'''# index 0  1  2  3  4  5  6  7
nums = [1, 2, 3, 4, 5, 6, 7, 8]
index = linear_search(nums, 0)
print(index) # 2'''


"""Part 2 - Binary Search
Implement binary search, which requires that a list is sorted and divides its search range in half each iteration until it finds its target.
"""

def binary_search(nums, value):
  low = 0
  high = len(nums)
  counter = 0
  while low < high:
      mid = (high + low) // 2
      counter += 1 # Counter prevents infinite loops
      # print(f"Iteration {counter}. low = {low}, middle = {mid}, high = {high}") # Test printout
      if counter == 100:
          break
      
      if nums[mid] > value:
          high = mid
          continue
      
      elif nums[mid] < value:
          low = mid
          continue
      
      elif nums[mid] == value:
          return f"The value '{value}' is located at index '{mid}'"
'''
#       0  1  2  3  4  5  6  7
nums = [1, 2, 3, 4, 5, 6, 7, 8]
index = binary_search(nums, 2)
print(index) # 2
'''

'''Part 3 - Bubble Sort
Bubble sort is one of the simplest and least efficient sorting algorithms. 
We repeatedly loop over the list, comparing each number to the one next to it, and swapping them if needed.'''

def bubble_search(nums):
    complete = False
    index = 0
    while not complete:
      if index >= (len(nums)):
            complete == True
            return nums
      try: 
            next_value = nums[index+1]
      except IndexError:
            break
      if nums[index] <= next_value:
          try:
              index += 1
          except IndexError:
              break
      elif nums[index] > next_value:
          swap_value = nums.pop(index)
          nums.insert(index+1,swap_value)
          index = 0
          continue


    return nums

#       0  1  2  3  4  5  6  7  8
# nums = [6, 7, 8, 4, 0, 1, 2, 3, 5]
# index = bubble_search(nums)
#print(index) # 2

"""Part 4 - Insertion Sort (optional)
Implement insertion sort, which like bubble sort is also O(n^2), but is efficient at placing new values into an already-sorted list.
"""

def insertion_sort(nums):
    sorted = []
    unsorted_value = []
    n = len(nums)
    for i in range(n-1):
        unsorted_value.append(nums.pop())
        if not sorted: # if there is nothing in the sorted list, append it as first value
            sorted.append(unsorted_value.pop(0))
            continue
        for ii in range(len(sorted)): # Evaluates sorted index values (at [ii]) until the unsorted value is smaller. Then pops the value in at the index.
            if sorted[ii] >= unsorted_value[0]:
                sorted.insert(ii, unsorted_value.pop())
                break
            if ii == (len(sorted)-1): # If [ii] iterates to the end for the sorted list, unsorted value is popped in at the end of the sorted list.
                sorted.append(unsorted_value.pop())
                break
    return sorted
            
'''nums = [6, 7, 8, 4, 0, 1, 2, 3, 5, -1, 19, 23, -6]
index = insertion_sort(nums)
print(index)'''
"""

Part 5 - Quicksort (optional)
Quicksort is one of the most efficient sorting algorithms. It works by swapping elements on either side of a pivot value.

Psuedocode:

algorithm quicksort(A) is
    quicksort_recursive(A, 0, length(A) - 1)

algorithm quicksort_recursive(A, lo, hi) is
    if lo < hi then
        p := partition(A, lo, hi)
        quicksort_recursive(A, lo, p)
        quicksort_recursive(A, p + 1, hi)

algorithm partition(A, lo, hi) is
    pivot := A[lo + (hi - lo) / 2]
    i := lo - 1
    j := hi + 1
    loop forever
        do
            i := i + 1
        while A[i] < pivot
        do
            j := j - 1
        while A[j] > pivot
        if i ≥ j then
            return j
        swap A[i] with A[j]"""