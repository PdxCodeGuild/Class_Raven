def linear_search (value, list):
    #list =[]
    for item in list:
        if item == value:
            return list.index(item)

#print(linear_search(7, numbers))

def binary_search(value, list):
    Left = 0
    Right = len(list) - 1
    while Left <= Right:
        Middle = ((Left + Right) //2)
        if list[Middle] < value:
            Left = Middle + 1
        elif list[Middle] > value:
            Right = Middle - 1
        else:
            return Middle
    return False

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,]

#print(binary_search(7, numbers))

def swap(list, A, B):
    list[A], list[B] = list[B], list[A]
    return list


def bubble_sort (list):
    length = len(list)
    swapped = True
    while swapped == True:
        swapped = False
        for i in range(1, length):
            if list[i-1] > list[i]:
                swap(list, i-1, i)
                swapped = True
    return list

mixed_numbers = [3, 6, 1, 9, 8, 5, 4, 2, 7]

sorted = bubble_sort(mixed_numbers)
print(sorted)