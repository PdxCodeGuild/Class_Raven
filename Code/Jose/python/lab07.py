data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def peaks(data):
    peaks_output = []
    for i in range(1, len(data) - 1):    # Start the range with 1 and loop one less than the length of data, to avoid causing out of index error.
        if data[i] > data[i - 1] and data[i] > data[i + 1]:
            peaks_output.append(i)
    return peaks_output

def valleys(data):
    valleys_output = []
    for i in range(1, len(data) - 1):    # Almost the exact same as peaks, just reverse the comparison.
        if data[i] < data[i - 1] and data[i] < data[i + 1]:
            valleys_output.append(i)
    return valleys_output

def peaks_and_valleys(data):
    the_order = both_peaks + both_valleys
    the_order.sort()
    return the_order



both_peaks = peaks(data)
both_valleys = valleys(data)
both_peaks_and_valleys = peaks_and_valleys(data)
print(f"The peaks are {both_peaks}, the valleys are {both_valleys}, and the order in which they appear is {both_peaks_and_valleys}. ")