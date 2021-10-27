data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

peak_list = []
valley_list = []
peaks_and_valleys = []

def peaks():
    
    index = data.index(7)
    index2 = data.index(9)
    peak_list.append(index)
    peak_list.append(index2)
    peaks_and_valleys.extend(peak_list)
    print(peak_list)
    print(peaks_and_valleys)

peaks()


def valleys():
    index = data.index(4, 8, 10)
    index2 = data.index(6, 16, 18)
    valley_list.append(index)
    valley_list.append(index2)
    (peaks_and_valleys).extend(valley_list)
    print(valley_list)
    # print(peaks_and_valleys)

valleys()


def peaks_and_valleys():
    peaks_and_valleys = valley_list + peak_list
    peaks_and_valleys.sort()
    print(peaks_and_valleys)

peaks_and_valleys()
count = 0
for element in data:
    #add one x until we reach index 5 in list
    if count < data.index(5):
        print('x')
        count += 1
