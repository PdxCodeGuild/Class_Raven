data_list = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
# V1 
def peaks_func(data):
  peak_array = []
  for i in range(1, len(data)-1):
    if data[i-1] < data[i] and data[i+1] < data[i]:
      peak_array.append(i)
  return(peak_array)
  
def valleys_func(data):
  valley_array = []
  for i in range(1, len(data)-1):
    if data[i-1] > data[i] and data[i+1] > data[i]:
      valley_array.append(i)
  return(valley_array)
  

peaks = peaks_func(data_list)
valleys = valleys_func(data_list)
print(f'peaks {peaks}, valleys {valleys}')

# V2

