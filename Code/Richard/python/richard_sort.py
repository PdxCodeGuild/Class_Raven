def rich_sort(list):
    length = len(list)
    new_list =[list.pop()]
    counter = 0
    max_num = 0
    for i in range(length-1):
        current = len(new_list)
        object = list.pop()
        while counter < current:
            if object > max_num:
                max_num= object
                new_list.append(object)
                break
            if object < new_list[counter]:
                new_list.insert(counter,object)
                counter = 0
                break
            elif object > new_list[counter] and counter == current-1:
                new_list.append(object)
                counter = 0
                break
            elif object > new_list[counter]:
                counter+=1
    return new_list

numbers = [29, 45, 67, 21, 56, 97, 1, 30, 50, 90, 25, 12, 17, 11, 13, 5, 7, 2]

test = rich_sort(numbers)
print(test)
