
# Lab_06 Peaks and Valleys
# Rafael Medinally


"""
NOTE: version 1 ready for review 11/4/2021.

"""
"""
# peaks() Has a lower number on left and right
# valleys() Has a higher number on left and right
# peaks_and_valleys() Both the lowest and highest on left and right


                                                  X                 X
                                               X  X  X           X  X
                          X                 X  X  X  X  X     X  X  X
                       X  X  X           X  X  X  X  X  X  X  X  X  X
                    X  X  X  X  X     X  X  X  X  X  X  X  X  X  X  X
                 X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
              X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
           X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
        X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
# index 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20

Note: 20 is not a peak because it has nothing to compare to its right.
"""

# Version 1

# 21 indexex [0-20]
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]


peak_counts = 0
valley_counts = 0
peaks_valleys_counts = 0

peaks_list = []
valleys_list = []
peaks_valleys_list = []

# After looking into how to approach this lab without importing complex modules like scipi, I found https://www.geeksforgeeks.org/python-program-that-prints-the-count-of-either-peaks-or-valleys-from-a-list/ for reference on where to start with the range in the list "range(1, len(x) -1)". And https://stackoverflow.com/questions/50638502/find-all-the-hills-and-valley-in-a-list to get an idea on how of another approach to peaks and valleys not using a module.   
for i in range(1, len(data) - 1): # for an index in the range of the list. The -1 keeps the index within range to prevent error..
        
        # This finds the peaks. Python tutor has the counts at index [6]&[14]
        if data[i - 1] < data[i] > data[i + 1]: # If the previos index -1 index to the left is less than i and if the next index to the right +1 is less than i then it is a peak in data.

                peak_counts += 1 # Adds the peaks to the count.

#print(valley_counts)

# for an index in the range of the list. The -1 keeps the index within range
for i in range(1, len(data) - 1):
    # This finds the valleys. Python tutor has the counts at index [6]&[14]
        if data[i - 1] > data[i] < data[i + 1]: # If the previos index -1 to the left is greater than i and if the next +1 to the right is greater than i then it is a valley in data. 
                valley_counts += 1 # Adds the valleys to the count.

peaks_valleys_counts = peak_counts + valley_counts

"""
Instructions:
Define the following functions:
1. peaks(data) - Returns the indices of peaks. A peak has a lower number on both the left and the right.
2. valleys(data) - Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.
3. peaks_and_valleys(data) - uses the above two functions to compile a single list of the peaks and valleys in order of appearance in the original data.
"""
#1 peaks(data) - Returns the indices of peaks. A peak has a lower number on both the left and the right.
def peaks(data):
# To find the index values and print them, they will need to be appended to an empty list.
    for i in range(1, len(data) -1):
        if data[i - 1] < data[i] > data[i + 1]:
            peaks_list.append(i) # Instead of adding counts, this appends the [i] peaks into the peaks_list.
            #print(peaks_list)       
    return peaks_list
peaks_list = peaks(data)

# 2. valleys(data) - Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.
def valleys(data):
    for i in range(1, len(data) -1):
        if data[i - 1] > data[i] < data[i + 1]: 
            valleys_list.append(i) # Instead of adding counts, this appends the [i] valleys into the valleys_list.
            #print(valleys_list)
    return peaks_list
peaks_list = valleys(data)
# 3. peaks_and_valleys(data) - uses the above two functions to compile a single list of the peaks and valleys in order of appearance in the original data.

def peaks_and_valleys(data):
    peaks_valleys_list = []
    for i in range(1, len(data) -1):
        if data[i - 1] < data[i] > data[i + 1]:
            peaks_valleys_list.append(i)
        if data[i - 1] > data[i] < data[i + 1]:
            peaks_valleys_list.append(i)
    #print(peaks_valleys_list)
    return peaks_valleys_list
peaks_valleys_list = peaks_and_valleys(data)

#print(peaks_list)
#print(valleys_list)
#print(peaks_list + valleys_list)

print(f'\nThe functions found {peak_counts} peaks @ {peaks_list}, {valley_counts} valleys @ {valleys_list} and {peaks_valleys_counts} peaks and valleys @ {peaks_valleys_list}.')

 