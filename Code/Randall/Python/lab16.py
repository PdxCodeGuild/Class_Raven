# Searching and Sorting

#Part 1 - Linear Search
'''
def linearSearch(num_list, n, x):
    for i in range(0, n):
        if (num_list[i] == x):
            return i
    return -1

num_list = [1, 2, 3, 4, 5, 6, 7, 8]
x = 1
n = len(num_list)
result = linearSearch(num_list, n, x)
if(result == -1):
    print("Number not found")
else:
    print("Number found at index: ", result)
'''  
#Part 2 - Binary Search
'''
def bin_search(list, low, high, x):
 
    if high >= low:
        mid = (high + low) // 2

        if list[mid] == x:
            return mid
 
        elif list[mid] > x:
            return bin_search(list, low, mid - 1, x)
 
        else:
            return bin_search(list, mid + 1, high, x)
 
    else:
        return -1
 
list = [ 1, 2, 3, 4, 5, 6, 7, 8, 9,]
x = 9
 
result = bin_search(list, 0, len(list)-1, x)
if result != -1:
    print("Number is present at index", str(result))
else:
    print("Number is not present in list")
'''
# Part 3 - Bubble Sort
# LOL 257 Steps with this list
def bub_sort(list_1):
    n = len(list_1)

    for i in range(n-1):

        for j in range(0, n-i-1):
            if list_1[j] > list_1[j + 1]:
                list_1[j], list_1[j+1] = list_1[j+1], list_1[j]

list_1 = [48, 33, 1, 22, 35, 5, 6, 4, 18, 10, 26, 0, 49]

bub_sort(list_1)

for i in range(len(list_1)):
    print('% d' % list_1[i]) 