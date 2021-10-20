"""
Lee Colburn
Evening Bootcamp - PDX Code Guild
Lab 7
"""

"""
Define the following functions:

peaks(data) - Returns the indices of peaks. 
A peak has a lower number on both the left and the right.
take in list. Compare each index position (start at [1], end at [-1]) 
if the evaluated index is higher than both comparison values, it's a peak.

valleys(data) - Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.

peaks_and_valleys(data) - uses the above two functions to compile a single list of the peaks and valleys in order of appearance in the original data.
# print('[' + ', '.join(data) + ']') # add quotes to data list
# data = [i.replace('""', '') for i in data] # strips double quotes in data

"""
def peaks(data, peaks_data):
  """Returns the indices of peaks.
  A peak has a lower number on both the left and the right."""

  # Iterate over data set. peaks_data evaluates and extends as "P" or "0".  
  for i in range(len(data)):
    if data[i] > max(data[i - 1], data[(i + 1) % len(data)]):
        peaks_data.extend('P')
    else:
        peaks_data.extend("-")

  # Clean data on extremes
  peaks_data[0] = "-"
  peaks_data[-1] = "-"

  return peaks_data



def valleys(data, valleys_data):
  """Returns the indices of 'valleys'. 
  A valley is a number with a higher number on both the left and the right."""
  
  for i in range(len(data)):
      if data[i] < min(data[i - 1], data[(i + 1) % len(data)]):
          valleys_data.extend('V')
          # print(valleys)
      else:
          valleys_data.extend("-")
          # print(valleys)
  valleys_data[0]="-"
  valleys_data[-1]="-"
  return valleys_data



def comparison_data_set(data):
  """Reformats data to be comparable to peaks and valleys output sets"""
  display_data_set = []
  for i in range(len(data)):
    number = data[i]
    display_data_set.extend(str(number))
  print(display_data_set)
  return 



def peaks_and_valleys(data, pv_final):
  """Returns both peaks and valleys as a single list"""

  # Get peaks and valleys data via calling their functions
  peaks(data, peaks_data)
  valleys(data, valleys_data)
  

  # Make new list to merge valleys and peaks. 
  p_and_v = []
  for (p, v) in zip(peaks_data, valleys_data):
    p_and_v.append(p + v)

  # Clean p_and_v list to remove spaces
  p_and_v_clean = []
  p_and_v_clean = [x.strip('-') for x in p_and_v]

  # Add back charachters so the pv data is comparable to data set
  for i in range(len(p_and_v_clean)):
    pv = str(p_and_v_clean[i])
    if p_and_v_clean[i] == '':
      pv_final.extend('-')
    else:
      pv_final.extend(pv)
  return pv_final

def graph_simple(data):
  """Returns a graph of the dataset in vanilla python - no water"""
  data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
  print(" "* 14 + "x" + " " * 5 + "x")
  print(" " * 13 + "x"*3 + " "*3 + "x"*2) # “ “ 13, x 3, - 3, x2
  print(" "*6 + "x" + " "*5 + "x"*5 +" " + "x"*3) #6 spaces, 1x, 5 spaces, 5 x, 1space, 3x
  print(" "*5 + "x"*3 + " "*3 + "x"*10) # 5 spaces, 3 x, 3 zeros,  10 x
  print(" "*4 + "x"*5 + " "*1 + "x"*11) # 4 spaces. 5 x, 1 zero, 11 x
  print(" "*3 + "x"*18) # 3 spaces, 18 x
  print(" "*2 + "x"*19) # 2 spaces, 19 x
  print(" " + "x"*20) # 1 space, 20 x
  print("x"*21) # 20x
  return

def graph_fancy(data):
  """Returns a graph of the dataset in vanilla python - with water"""
  data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
  print(" "* 14 + "x" + "0" * 5 + "x")
  print(" " * 13 + "x"*3 + "0"*3 + "x"*2) # “ “ 13, x 3, - 3, x2
  print(" "*6 + "x" + "0"*5 + "x"*5 +"0" + "x"*3) #6 spaces, 1x, 5 spaces, 5 x, 1space, 3x
  print(" "*5 + "x"*3 + "0"*3 + "x"*10) # 5 spaces, 3 x, 3 zeros,  10 x
  print(" "*4 + "x"*5 + "0"*1 + "x"*11) # 4 spaces. 5 x, 1 zero, 11 x
  print(" "*3 + "x"*18) # 3 spaces, 18 x
  print(" "*2 + "x"*19) # 2 spaces, 19 x
  print(" " + "x"*20) # 1 space, 20 x
  print("x"*21) # 20x
  return

####################### INTERFACE ##############################################################
complete = False
while not complete:

  # Select Option 1-Peaks, 2-Valleys, 3 - Peaks and Valleys, 4 - Exit, 5+ Try Again
  start = int(input(f'\nPlease select from the following options:\n 0. Print graph of data set \n 1. Check test data for peaks \n 2. Check test data for valleys\n 3. Compile a single list of peaks and valleys.\n 4. Exit Program \n\n Enter the number of your choice: \n'))
  data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
  display_data_set=[]
  peaks_data =  []
  valleys_data = []
  pv_final = []


  ################### DIRECTORY ################################################################
  # Allow user to escape
  if start == 4:
    print(f"\nClosing application.\n")
    complete = True
    break
  if start > 4:
    print(f'\n Try again:\n')
    continue
  
  # Direct user to appropriate function: Select Option 1-Peaks, 2-Valleys, 3 - Peaks and Valleys
  if start == 1:
    peaks(data, peaks_data)
    print(f"Peaks noted as 'P':\n{peaks_data}")
    comparison_data_set(data)

  if start == 2:
    valleys(data, valleys_data)
    print(f"Valleys noted as 'V':\n{valleys_data}")
    comparison_data_set(data)

  if start == 3:
    peaks_and_valleys(data, pv_final)
    print(f"Peaks noted as 'P' and Valleys noted as 'V'\n{pv_final}")
    comparison_data_set(data)
  
  if start == 0:
    graph_simple(data)
    continue