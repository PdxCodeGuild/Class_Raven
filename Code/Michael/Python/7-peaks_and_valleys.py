'''
PDX Code Guild Full Stack Bootcamp
->Lab 07
  Peaks and Valleys
Michael B
'''
def peaks_and_valleys(data, options="None")->list:
    def peaks(data)->list:
        list_of_peaks = []
        for item in range(1,len(data)-1):
            if data[item] > data[item-1] and data[item] > data[item+1]: # If item is greater than previous item, and greater than following item, then is a peak.
                list_of_peaks.append(item)
        return list_of_peaks
    
    def valleys(data)->list:
        list_of_valleys = []
        for item in range(1,len(data)-1):
            if data[item] < data[item-1] and data[item] < data[item+1]: # If item is less then previous item, and less than following item, then is a valley.
                list_of_valleys.append(item)
        return list_of_valleys
    
    match options.split(): # Check options to do case.
        case ["peaks"]:
            return peaks(data)   
        case ["valleys"]:
            return valleys(data)
        case ["None"]:
            combined_list = []
            combined_list = peaks(data) + valleys(data)
            combined_list.sort()
            return combined_list
        case _:
            return "Error: Invalid input."   

if __name__ == '__main__':
    test_data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8]
    peak_and_valley = peaks_and_valleys(test_data)
    peak = peaks_and_valleys(test_data,"peaks")
    valley = peaks_and_valleys(test_data,"valleys")
    
    print(f' data: {test_data}')
    for i in reversed(range(0,max(test_data))):
        current_string = "        "
        highest_peak = 0
        for item in range(0,len(test_data)):
            
            if test_data[item] >= highest_peak: # Get highest peak to use later for water bounds.
                highest_peak = test_data[item]
            if test_data[item] >= i+1: # Become land.
                current_string = current_string + "X  "
                
                # Need to fix the below algorithm. 
            elif test_data[item]>=highest_peak or i>test_data[item]+(highest_peak-test_data[item]-1): # or test_data[item] == test_data[len(test_data)-1]: # I don't know, I brute forced this into existence. Become air.
                current_string = current_string + "   "
            else: # Become water.
                current_string = current_string + "O  "
        print(current_string)
    print('index: [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]')
    print("Peaks and Valleys: ",peak_and_valley)
    print("Peaks: ", peak)
    print("Valleys: ", valley)
    
    
      
""" Output:
data:  [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
                                                  X  O  O  O  O  O  X  
                                               X  X  X  O  O  O  X  X
                          X  O  O  O  O  O  X  X  X  X  X  O  X  X  X
                       X  X  X  O  O  O  X  X  X  X  X  X  X  X  X  X
                    X  X  X  X  X  O  X  X  X  X  X  X  X  X  X  X  X
                 X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
              X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
           X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
        X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
index: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20]
Peaks and Valleys:  [6, 9, 14, 17]
"""