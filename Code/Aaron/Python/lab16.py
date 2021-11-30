# 2Searching and Sorting
# Big-O Notation is a measure of the complexity of an algorithm, specifically how many steps an algorithm takes depending on the size of the input. For example, performing a linear search on a list of n elements takes, on average, n/2 steps, so we say a linear search is O(n). We throw away multiplicative and additive factors to characterize algorithms independently of the hardware it's running on. Big-O Cheat Sheet

# Part 1 - Linear Search
# Implement linear search, which simply loops through the given list and check if each element is equal to the value we're searching for. If it is, return the index at which it was found, otherwise, return a value indicating that it was not found.

def linear_search(array_list: list, num: int) -> int:
    for i in array_list:
        if i == num:
            return i
        else:
            return -1

# index 0  1  2  3  4  5  6  7
nums = [1, 2, 3, 4, 5, 6, 7, 8]
index = linear_search(nums, 8)
print(index) # 2


