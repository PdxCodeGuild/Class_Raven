"""
PDX Code Guild Full Stack Bootcamp
->Lab 16
  Searching And Sorting
Michael B

Searching and Sorting
Big-O Notation is a measure of the complexity of an algorithm, specifically how many steps an algorithm takes depending on the size of the input.
For example, performing a linear search on a list of n elements takes, on average, n/2 steps, so we say a linear search is O(n). 
We throw away multiplicative and additive factors to characterize algorithms independently of the hardware it's running on. Big-O Cheat Sheet

Part 1 - Linear Search
Implement linear search, which simply loops through the given list and check if each element is equal to the value we're searching for. 
If it is, return the index at which it was found, otherwise, return a value indicating that it was not found.

Example run:

 I
[1, 2, 3, 4, 5, 6, 7, 8]
    I
[1, 2, 3, 4, 5, 6, 7, 8]
       I
[1, 2, 3, 4, 5, 6, 7, 8]
Stub:

def linear_search(nums, value):
  ...
# index 0  1  2  3  4  5  6  7
nums = [1, 2, 3, 4, 5, 6, 7, 8]
index = linear_search(nums, 3)
print(index) # 2
Part 2 - Binary Search
Implement binary search, which requires that a list is sorted and divides its search range in half each iteration until it finds its target.

Begin by defining two indices: low and high. Initialize low as the lowest index in the list and high as the highest.
Loop while low is less then high.
For each iteration, calculate a third index mid which is in the middle between low and high
If the element at mid is the one you're searching for, return it, otherwise check is the target value is less than or greater than the one at mid. If it's less, make high equal to mid and loop.
If it's greater, make low equal to mid and loop. If the loop terminates without returning, return a value indicating that it was not found.
Example run:

 L        M           H
[1, 2, 3, 4, 5, 6, 7, 8]
 L  M     H
[1, 2, 3, 4, 5, 6, 7, 8]
    L  M  H
[1, 2, 3, 4, 5, 6, 7, 8]
Psuedocode:

// A - the list
// n - the length of the list
// T - the value we're searching for
function binary_search(A, n, T) is
    L := 0
    R := n − 1
    while L ≤ R do
        m := floor((L + R) / 2)
        if A[m] < T then
            L := m + 1
        else if A[m] > T then
            R := m - 1
        else:
            return m
    return unsuccessful
Stub:

def binary_search(nums, value):
  ...
#       0  1  2  3  4  5  6  7
nums = [1, 2, 3, 4, 5, 6, 7, 8]
index = binary_search(nums, 3)
print(index) # 2
Part 3 - Bubble Sort
Bubble sort is one of the simplest and least efficient sorting algorithms. We repeatedly loop over the list, comparing each number to the one next to it, and swapping them if needed.

procedure bubbleSort(A : list of sortable items)
    n := length(A)
    repeat
        swapped = false
        for i := 1 to n - 1 inclusive do
            /* if this pair is out of order */
            if A[i - 1] > A[i] then
                /* swap them and remember something changed */
                swap(A[i - 1], A[i])
                swapped := true
            end if
        end for
    until not swapped
end procedure
Part 4 - Insertion Sort (optional)
Implement insertion sort, which like bubble sort is also O(n^2), but is efficient at placing new values into an already-sorted list.

Psuedocode:

i ← 1
while i < length(A)
    j ← i
    while j > 0 and A[j-1] > A[j]
        swap A[j] and A[j-1]
        j ← j - 1
    end while
    i ← i + 1
end while
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
        swap A[i] with A[j]

"""


def linear_search(nums, value) -> int:  # O(n)
    for i in range(len(nums)):
        if (
            nums[i] == value
        ):  # If the current element is equal to the value we're searching for, return the index.
            return i  # Return the index.
    return -1


def binary_search(nums, value) -> int:  # O(log n)
    low = 0  # Low index.
    high = len(nums) - 1  # High index.
    while low <= high:  # While the low index is less than or equal to the high index.
        mid = (low + high) // 2  # Calculate the middle index.
        if (
            nums[mid] == value
        ):  # If the middle index is equal to the value we're searching for, return the index.
            return mid
        elif (
            nums[mid] < value
        ):  # If the middle index is less than the value we're searching for, make the low index equal to the middle index.
            low = mid + 1
        else:  # If the middle index is greater than the value we're searching for, make the high index equal to the middle index.
            high = mid - 1
    return -1


def bubble_sort(nums) -> list:  # O(n^2)
    for i in range(len(nums)):
        for j in range(len(nums) - i - 1):  # -i is to skip the already sorted elements.
            if (
                nums[j] > nums[j + 1]
            ):  # If the current element is greater than the next element, swap them.
                nums[j], nums[j + 1] = (
                    nums[j + 1],
                    nums[j],
                )  # Swap the current element with the next element.
    return nums


def insertion_sort(nums) -> list:  # O(n^2)
    for i in range(1, len(nums)):
        j = i
        while (
            j > 0 and nums[j - 1] > nums[j]
        ):  # j - 1 is the index of the previous element.
            nums[j], nums[j - 1] = (
                nums[j - 1],
                nums[j],
            )  # Swap the previous element with the current element.
            j -= 1  # Decrement j to check the previous element.
    return nums


def quick_sort(nums) -> list:  # O(n log n)
    def partition(nums, low, high):
        pivot = nums[low + (high - low) // 2]  # Calculate the pivot index.
        adjusted_low = low - 1  # adjusted_low is the index of the previous element.
        adjusted_high = high + 1  # +1 to account for the pivot.
        while True:
            adjusted_low += 1  # Increment adjusted_low to check the next element.
            while (
                nums[adjusted_low] < pivot
            ):  # While the current element is less than the pivot.
                adjusted_low += 1  # Increment adjusted_low to check the next element.
            adjusted_high -= 1  # Decrement adjusted_high to check the previous element.
            while (
                nums[adjusted_high] > pivot
            ):  # While the current element is greater than the pivot.
                adjusted_high -= (
                    1  # Decrement adjusted_high to check the previous element.
                )
            if (
                adjusted_low >= adjusted_high
            ):  # If the adjusted_low index is greater than or equal to the adjusted_high index, return the adjusted_high index.
                return adjusted_high
            nums[adjusted_low], nums[adjusted_high] = (
                nums[adjusted_high],
                nums[adjusted_low],
            )  # Swap the current element with the previous element.

    def quicksort_recursive(nums, low, high) -> list:
        if low < high:  # If the low index is less than the high index.
            partitioned = partition(nums, low, high)  # Partition the list.
            quicksort_recursive(
                nums, low, partitioned
            )  # Sort the left side of the list.
            quicksort_recursive(
                nums, partitioned + 1, high
            )  # Sort the right side of the list.

    quicksort_recursive(nums, 0, len(nums) - 1)  # Sort the list.
    return nums


if __name__ == "__main__":
    # Test the all the search functions.
    test_search = [1, 2, 3, 4, 5, 6, 7, 8]
    test_sort = [-1, 1234, 99, 999, 8, 7, 6, 54, 5, 4, 3, 2, 1, 0]

    print("\nlinear search: ", linear_search(test_search, 3))
    print("binary search: ", binary_search(test_search, 3))
    print("bubble sort: ", bubble_sort(test_sort))
    print("insertion sort: ", insertion_sort(test_sort))
    print("quick sort: ", quick_sort(test_sort))
    print("")
