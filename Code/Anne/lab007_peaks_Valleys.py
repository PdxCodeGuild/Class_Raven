#peaks and valleys lab

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
peaks_list = []
def peaks(data):
    #peaks_list = []
    # print(data[1:-1])
    # parse through list and return the index of any number that has a lower number on either side of 
    for i in range(1, len(data)-1):
        if data[i] > data[i+1] and data[i] > data[i-1]:
            peaks_list.append(i)
    # return(peaks_list)

# peaks(data)

valley_list = []
def valleys(data):
#     #  parse through list and return the index of any number that has a lawer number on either side of it
    for i in range(1, len(data)-1):
        if data[i] < data[i+1] and data[i] < data[i-1]:
            valley_list.append(i)
    # return(valley_list)

# valleys(data)

def peaks_and_valleys(data):
    peaks(data)
    valleys(data)
    peaks_list.extend(valley_list)
    peaks_list.sort()
    return(peaks_list)
peaks_and_valleys(data)
#     #uses the above two functions to compile a single list of the peaks and valleys in order of appearance in the original data