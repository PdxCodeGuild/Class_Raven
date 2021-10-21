
## I reviewed and, after understanding how it worked, used my own version of code found on the following webpage in the body of my functions:
#  https://www.geeksforgeeks.org/python-program-that-prints-the-count-of-either-peaks-or-valleys-from-a-list/

def peaks(data):
    ## creating a function to determine the peaks from a provided list of numbers 
    peaks = []  # creating empty list that we will append peaks to 
    for idx in range(1, len(test_list) - 1):  # starting at index 1 and going to end of list -1
                                # we are doing this because if we started at first or last number in list, we can't check numbers on either side 
        if test_list[idx + 1] < test_list[idx] > test_list[idx - 1]:
                # if number to right of index is less sthan index and the index is greater than number on left, it's a peak!
            peaks.append(idx)  # now we can append peak to list of peaks 
    print(peaks)

def valleys(data):
    ## creating a function to determine the valleys from a provided list of numbers 
    valleys = [] # creating empty list that we will append valleys to 
    for idx in range(1, len(test_list) - 1):
        if test_list[idx - 1] > test_list[idx] < test_list[idx + 1]:
            # if number to left of index is greater than index and the index is less than number on right, it's a valley!
            valleys.append(idx)
    print(valleys)

def peaks_valleys(data):
    ## creating a function that determines peaks and valleys and returns them in order of appearance in list 
    peaks_valleys = []
    for idx in range(1, len(test_list) - 1):
        if test_list[idx - 1] > test_list[idx] < test_list[idx + 1] or test_list[idx + 1] < test_list[idx] > test_list[idx - 1]: 
            peaks_valleys.append(idx)  ## essentially combines the body of the previous two functions and appends to peaks_valleys list 
    print(peaks_valleys)

test_list = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

peaks(test_list)
valleys(test_list)
peaks_valleys(test_list)

## calling the functions 




#for idx in range(1, len(test_list) - 1):
    #if test_list[idx + 1] < test_list[idx] > test_list[idx - 1]:
         #peaks.append(idx)
#print(peaks)

#test_list_2 = [1, 2, 10, 2, 6, 7, 12, 3]  ## why doesn't this use value at index to check if over 9, but above for loop prints out value at that index 
#for idx in range(len(nines_list)):
    #if idx > 9:   ## but if you do nines_list[idx] it works 
        #nines_list[idx] = nines_list[idx] - 9
