""" Linear search """
import math
import random

nums = [1, 2, 3, 4, 5, 6, 7, 8]


def linear_search(list, value):
    match = 'No match found'
    for i in range(len(nums)):
        if nums[i] == value:
            match = i + 1  # added + 1 to give the proper index
    print(match)
    return match


# linear_search(nums, 3)


length = range(len(nums))


def binary_search(list, target):

    nums.sort()
    low = min(nums)
    # print(low)
    high = max(nums)
    # print(high)
    # middle = (low + high) // 2

    while low <= high:
        middle = (low + high) // 2

        if nums[middle] < target:
            low = middle + 1

        elif nums[middle] > target:
            high = middle - 1

        else:
            return middle + 1  # added + 1 to give the proper index


# print(binary_search(nums, 5))


# """ bubble sort """
# random.shuffle(nums) # generating a random list to be used for the bubble sort function

swap_list = [5, 8, 6, 7, 1, 2, 3, 4]


def bubble_sort(array):
    amount_of_swaps = 0
    swapped = True
    while(swapped):  # while swap is True run the code.
        swapped = False
        for i in range(len(array) - 1):  # will run until second to last item in list
            if array[i] > array[i + 1]:
                # Swap the item in the list if it's greater then it's neighbor.
                array[i + 1], array[i] = array[i], array[i + 1]
                amount_of_swaps += 1  # was curious to see how many times the loop ran
                swapped = True
    print(amount_of_swaps)
    return array


# print(bubble_sort(swap_list))

insertion_list = [5, 8, 6, 7, 1, 2, 3, 4, 9]


def insertion_sort(array):
    i = 1
    loops = 0
    while i < len(array):
        j = i
        while j > 0 and array[j - 1] > array[j]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j = j - 1

        i = i + 1
        loops += 1
    print(array)
    print(loops)
    return array

# insertion_sort(insertion_list)


def quicksort(array):
    quicksort_recursive(array, 0, len(array) - 1)
    print(array)

def quicksort_recursive(array, lo, hi):
    if lo < hi:
        p = partition(array, lo, hi)
        quicksort_recursive(array, lo, p)
        quicksort_recursive(array, p + 1, hi)


def partition(array, lo, hi):
    pivot = array[math.floor(lo + (hi - lo) / 2)]
    i = lo - 1
    j = hi + 1
    while True:
        while array[i] < pivot:
            i = i + 1
        while array[j] > pivot:
            j = j - 1
        if i >= j:
            return j
        array[i] = array[j]
quicksort(insertion_list)
