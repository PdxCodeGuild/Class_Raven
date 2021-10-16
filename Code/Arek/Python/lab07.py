"""
Peaks and Valleys

Define the following functions:

    peaks(data) - Returns the indices of peaks. A peak has a lower number on both the left and the right.

    valleys(data) - Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.

    peaks_and_valleys(data) - uses the above two functions to compile a single list of the peaks and valleys in order of appearance in the original data.

Visualization of test data:

"""

"""
# These are steps 1 and 2 of this lab, If you are using them seperately you just need to call them
def peaks(data):
    x = 0
    elements = len(data)

    while x != elements - 1:
        for i in data:
            x += 1
            if x == elements - 1:
                break
            elif data[x-1] < data[x] and data[x+1] < data[x]:
                peak_list.append(data[x])

    return peak_list
                


def valleys(data):
    x = 0
    elements = len(data)

    while x != elements - 1:
        for i in data:
            x += 1
            if x == elements - 1:
                break
            elif data[x-1] > data[x] and data[x+1] > data[x]:
                valley_list.append(data[x])

    return valley_list


"""

# This is step 3 of the first exercise in lab7
data = [1,2,3,4,5,6,7,6,5,4,5,6,7,8,9,8,7,6,7,8,9]
peak_list = []
valley_list = []
peaksAndValleys = []

def peaks(data):
    x = 0
    elements = len(data)

    while x != elements - 1:
        for i in data:
            x += 1
            if x == elements - 1:
                break
            elif data[x-1] < data[x] and data[x+1] < data[x]:
                peak_list.append(data[x])

    return peak_list
                
def valleys(data):
    x = 0
    elements = len(data)

    while x != elements - 1:
        for i in data:
            x += 1
            if x == elements - 1:
                break
            elif data[x-1] > data[x] and data[x+1] > data[x]:
                valley_list.append(data[x])

    return valley_list

#def peaks_valleys(data):

    