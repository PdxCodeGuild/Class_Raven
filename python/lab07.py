data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

p_v = []
valleys = []
peaks = []
l_index = []
def peaks():
    for i in data:
        index = data.index(i)
        next_ = data.index(i)+1
        previous_ = data.index(i)-1
        if data[i]-1 < i and data[i]+1 < i:
            print(f'{i} at index {index} is a peak.')
            peaks.append(i)
        else:
            print(f'{i} at index {index} is not a peak.')
print(peaks)
peaks()

def valleys():
    for i in data:
        index = data.index(i)
        next_ = data.index(i)+1
        previous_ = data.index(i)-1
        if data[previous_] > i and data[next_] > i:
            print(f'{i} at index {index} is a valley.')
            valleys.append(i)
        else:
            print(f'{i} at index {index} is not a valley.')
            
# valleys()

def peaks_and_valleys():
    for i in data:
        index = data.index(i)
        l_index.append(index)
        next_ = data.index(i)+1
        previous_ = data.index(i)-1
        if data[previous_] < i and data[next_] < i:
            print(f'{i} at index {index} is a peak.')
            p_v.append('i')
        elif data[previous_] > i and data[next_] > i:
            p_v.append(i)
            print(f'{i} at index {index} is a peak.')
        else:
            p_v.append('')
    print('data',data)
    print('index',l_index)
    print('poi',p_v)

# peaks_and_valleys()

count = 0
s = 'x'
# for i in data:
#     print('x'*i, end='')

# a = """"""
# b = """"""

# for i in range(0, 3):
#     # a += str(f'{i}')
#     a += str(f'{i}\n')
#     b += str(f'{i}\n')
#     d = a+b
# print(d, end='')    

# c = """{e} {e} {e} {e}""".format(e=b)

