data_list = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
data_list2 = [1, 2, 3, 4, 2, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
data_list3 = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9, 10]
data_list4 = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9, 10, 11, 10, 9, 10]
data_list5 = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9, 10, 11, 10, 9, 10, 11]

# V1 
def peaks_func(data):
  return [
      i for i in range(1,
                       len(data) - 1)
      if data[i - 1] < data[i] and data[i + 1] < data[i]
  ]
  
def valleys_func(data):
  return [
      i for i in range(1,
                       len(data) - 1)
      if data[i - 1] > data[i] and data[i + 1] > data[i]
  ]
  
peaks = peaks_func(data_list)
valleys = valleys_func(data_list)
print(f'peaks {peaks}, valleys {valleys}')

# V2
def print_land(data):
  height = 0
  for i in range(len(data)):
    if data[i] > height:
      height = data[i]
  while height > 0:
    display_array = []
    for i in range(len(data)):
      if data[i] >= height:
        display_array.append('X')
      else:
        display_array.append(' ')
    height = height - 1
    print_str = ' '.join(display_array)
    print(print_str)
    
# print_land(data_list)

# V3
def print_land_water(data):
  peaks = peaks_func(data)
  height = 0
  for i in range(len(data)):
    if data[i] > height:
      height = data[i]
  while height > 0:
    display_array = []
    for i in range(len(data)):
      skip = False
      #check if in between two peaks
      for p in range(len(peaks)):
        if i <= peaks[p]: #if the index is less then or equal to the first peak break no water would go there
          break
        lowest_peak = ''
        try: # find the lowest peak in the peaks array
          if i >= peaks[p] and i <= peaks[p+1]: #ensure we are using the correct peaks to compare with
            lowest_peak = min(data[peaks[p]], data[peaks[p+1]])
        except IndexError: # if index of peak array out of range use the last element of the data list to compare with
          lowest_peak = min(data[peaks[-1]], data[-1])
        if (lowest_peak != '' and lowest_peak != data
            and data[i] <= lowest_peak and height <= lowest_peak
            and height > data[i]):
          display_array.append('0')
          skip = True
      if data[i] >= height:
        display_array.append('X')
      elif not skip:
        display_array.append(' ')
    height = height - 1
    print_str = ' '.join(display_array)
    print(print_str)
print_land_water(data_list)