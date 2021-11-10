
#Lab 7: Peaks and Valleys

st_dat = [1,2,3,4,5,6,7,6,5,4,5,6,7,8,9,8,7,6,7,8,9]

def peaks(input_data):
    list_1 = []
    peak_list = []
    for n in range(len(input_data)):
        list_1.append(input_data[n])
        if n - 1 < 0 or n - 2 < 0:
            continue
        if list_1[n-2] < list_1[n-1] > list_1[n]:
            peak_list.append(n-1)
    return peak_list

def valleys(input_data):
    list_1 = []
    valley_list = []
    for n in range(len(input_data)):
        list_1.append(input_data[n])
        if n - 1 < 0 or n - 2 < 0:
            continue
        if list_1[n-2] > list_1[n-1] < list_1[n]:
            valley_list.append(n-1)
    return valley_list

def peaks_and_valleys():
    peak_list = peaks(st_dat)
    valley_list = valleys(st_dat)
    pv_list = peak_list
    pv_list.extend(valley_list)
    pv_list.sort()
    return pv_list

def draw_st_dat(input_data):
    peak_list = peaks(st_dat)
    valley_list = valleys(st_dat)
    horizontal =len(input_data)
    vertical = max(input_data)

    for v in range(vertical):
        print(' ' * 7,end='')
        for h in range(horizontal):
            if  (peak_list[1] - v) <= h <= (peak_list[1] + v) and (input_data[h] >= (vertical - v)) :
                print(' X ', end='')
            elif ((peak_list[0]-v) <= h <= (peak_list[0]+ v)) and (input_data[h] >= (vertical - v)):
                print(' X ',end='')
            elif h > (max(valley_list)-v) and (input_data[h] >= (vertical - v)):
                print(' X ',end='')
            elif (valley_list[0] - v) <= h <= (valley_list[0] + v)  and ((vertical - v - 1) <= peak_list[0]):
                print(' 0 ',end='')
            elif (valley_list[1] - v) <= h <= (valley_list[1] + v) and ((vertical - v - 1) <= peak_list[1]):
                print(' 0 ',end='')
            else:
                print(' . ', end='')
        print('\n')
    print(f'data = {input_data}')

print(peaks(st_dat))
print(valleys(st_dat))
print(peaks_and_valleys())
draw_st_dat(st_dat)