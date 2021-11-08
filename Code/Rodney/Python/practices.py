list_to_sort = [12, 0, 2, 98, 4, 698, 1, 0, 0, 74] ## random list to sort 
list_length = len(list_to_sort) - 1  # we take length of list to sort - 1 
swapped = True

while swapped == True:  # while our list doesn't equal the sorted list, continue 
    swapped = False
    for i in range (list_length): # this will 'do something' so many times, which in this case is the number of indices in list 
        if list_to_sort[i] > list_to_sort[i + 1]:  ## using our list, say i is index 1, so i - 1 is index 0, in our list those are values: 0 and 12 
            list_to_sort[i], list_to_sort[i + 1] = list_to_sort[i + 1], list_to_sort[i]  # 12 is greater than 0, so this line tells us to switch 0 to index 0 and 12 to index 1 
            swapped = True
               # this will repeat for every index in list and loop will repeat until our list to sort equals the sorted list    
print(list_to_sort)

