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

        def quicksort_rec(numbs: list, low: int, high: int) -> list:
            if low < high:
                p = partition(numbs, low, high)
                quicksort_rec(numbs, low, p - 1)
                quicksort_rec(numbs, p + 1, high)

            return numbs

        def partition(numbers: list, low: int, high: int) -> int:
            pivot = numbers[high]
            i = low - 1
            for j in range(low, high):
                if numbers[j] <= pivot:
                    i += 1
                    numbers[i], numbers[j] = numbers[j], numbers[i]

            numbers[i + 1], numbers[high] = numbers[high], numbers[i + 1]

            return i + 1

        return quicksort_rec(nums, 0, len(nums) - 1)


def main() -> None:

    search_and_sort = Search()
    nums = [1, 2, 3, 4, 5, 6, 7, 8]

    val = search_and_sort.linear_search(nums, 6)
    print(f"\nLinear Search: {val}\n")

    val2 = search_and_sort.bin_search(nums, 6)
    print(f"Binary Search: {val2}\n")

    sort_me = [85, 12, 59, 26, 64, 77, 54, 45, 896, 8474, 89, 65, 21, 31, 98]

    val3 = search_and_sort.bubb_sort(sort_me)
    print(f"Bubble Sort: {val3}\n")

    sort_you = [85, 12, 59, 27, 64, 77, 54, 45, 896, 8474, 89, 65, 21, 32, 98]

    val4 = search_and_sort.insert_sort(sort_you, len(sort_you) - 1)
    print(f"Insert Sort: {val4}\n")

    sort_us = [86, 12, 57, 25, 61, 76, 51, 42, 899, 8475, 81, 64, 22, 30, 99]

    val5 = search_and_sort.quicksort(sort_us)
    print(f"Quick Sort: {val5}\n")


if __name__ == "__main__":
    main()
