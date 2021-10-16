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
"""
def peaks(data):
    print(f"Evaluating this data set for peaks:\n {data}")
    working_data = data
    working_data
    peaks = []
    for i in range(data):
        if data[i] > data[i+1] and data[i] > data[i-1]:
            peaks.extend('P')
            print(peaks)
        else:
            peaks.extend(' ')
            print(peaks)
    print(data)
    print(peaks)
    return

def valleys(data):
    print(f"Evaluating this data set for valleys:\n {data}")
    return

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
complete = False
while not complete:
  # Select Option 1-Peaks, 2-Valleys, 3 - Peaks and Valleys, 4 - Exit, 5+ Try Again
  start = int(input(f'\nPlease select from the following options:\n 1. Check test data for peaks \n 2. Check test data for valleys\n 3. Compile a single list of peaks and valleys.\n 4. Exit Program \n\n Enter the number of your choice: \n'))

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
    peaks(data)

  if start == 2:
    valleys(data)

  if start == 3:
    for num in data:
        print('x' * num) # needs to shift to vertical
    continue