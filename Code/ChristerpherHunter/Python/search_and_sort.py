"""
Christerpher Hunter
Lab 16: Searching and Sorting

Big-O Notation is a measure of the complexity of an algorithm, specifically
how many steps an algorithm takes depending on the size of the input.
For example, performing a linear search on a list of n elements takes, on
average, n/2 steps, so we say a linear search is O(n). We throw away
multiplicative and additive factors to characterize algorithms independently
of the hardware it's running on. 
"""


class Search:
    """Implement Linear and Binary search w/ a Bubble Sort"""

    def __init__(self) -> None:

        pass

    def linear_search(self, nums: list, value: int) -> int:
        """Implement a linear search algorithm"""

        for i in nums:
            if i == value:
                return i

    def bin_search(self, nums: list, value: int) -> int:
        """Implement binary search algorithm"""

        begg_ind = 0
        last_ind = len(nums) - 1

        while begg_ind <= last_ind:

            midd_ind = (begg_ind + last_ind) // 2
            if nums[midd_ind] < value:
                begg_ind = midd_ind + 1

            elif nums[midd_ind] > value:
                last_ind = midd_ind - 1

            else:
                return midd_ind

        return -1

    def bubb_sort(self, nums: list) -> list:
        """Implement a bubble sort algorithm"""

        swapped = True
        while swapped:

            swapped = False
            for i in range(1, len(nums)):
                if nums[i - 1] > nums[i]:
                    nums[i - 1], nums[i] = nums[i], nums[i - 1]
                    swapped = True
        return nums

    def insert_sort(self, nums: list, n) -> list:
        """Implement insertion sort algorithm, recursively"""

        if n > 0:
            self.insert_sort(nums, n - 1)
            x = nums[n]
            j = n - 1
            while j >= 0 and nums[j] > x:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = x

        return nums

    def quicksort(self, nums: list) -> list:
        """Implement a quicksort recursive algorithm"""

        def quicksort_rec(nums, low, high):
            if low < high:
                p = partition(nums, low, high)
                quicksort_rec(nums, low, p)
                quicksort_rec(nums, p + 1, high)

        def partition(nums, low, high):
            pivot = nums[low + (high - low) // 2]
            i = low - 1
            j = high + 1
            while True:
                i += 1
                while nums[i] < pivot:
                    j -= 1
                while nums[j] > pivot:
                    i += 1
                    if i >= j:
                        return j
                nums[i], nums[j] = nums[j], nums[i]

        quicksort_rec(nums, 0, len(nums) - 1)


def main() -> None:

    search_and_sort = Search()
    nums = [1, 2, 3, 4, 5, 6, 7, 8]

    val = search_and_sort.linear_search(nums, 6)
    print(val)

    val2 = search_and_sort.bin_search(nums, 6)
    print(val2)

    sort_me = [85, 12, 59, 26, 64, 77, 54, 45, 896, 8474, 89, 65, 21, 31, 98]

    val3 = search_and_sort.bubb_sort(sort_me)
    print(val3)

    sort_you = [85, 12, 59, 27, 64, 77, 54, 45, 896, 8474, 89, 65, 21, 32, 98]

    val4 = search_and_sort.insert_sort(sort_you, len(sort_you) - 1)
    print(val4)

    sort_us = [85, 12, 59, 27, 61, 76, 54, 45, 896, 8474, 89, 65, 21, 32, 98]

    val5 = search_and_sort.quicksort(sort_us)
    print(val5)


if __name__ == "__main__":
    main()
