# Define the following functions:

# peaks(data) - Returns the indices of peaks. A peak has a lower number on both the left and the right.

# valleys(data) - Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.

# peaks_and_valleys(data) - uses the above two functions to compile a single list of the peaks and valleys in order of appearance in the original data.

# Visualization of test data:

# Data	1	2	3	4	5	6	7	6	5	4	5	6	7	8	9	8	7	6	7	8	9
# Index	0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20
# POI							P			V					P			V			
# Example I/O:

#                                                   X                 X
#                                                X  X  X           X  X
#                           X                 X  X  X  X  X     X  X  X
#                        X  X  X           X  X  X  X  X  X  X  X  X  X
#                     X  X  X  X  X     X  X  X  X  X  X  X  X  X  X  X
#                  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
#               X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
#            X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
#         X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
# # index 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20
# data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
# peaks(data) # [6, 14]
# valleys(data) # [9, 17]
# peaks_and_valleys(data) # [6, 9, 14, 17]






def peaks(data):
  peaks = []
  for i, x in enumerate(data):
    if i > 1 and i < 19:
      if data[i-1] < data[i] and data[i+1] < data[i]:
        peaks.append(i)
  return peaks

def valleys(data):
  valleys = []
  for i, x in enumerate(data):
    if i > 1 and i < 19:
      if data[i-1] > data[i] and data[i+1] > data[i]:
        valleys.append(i)
  return valleys

def peaks_and_valleys(data):
  peaks_and_valleys = peaks(data) + valleys(data)
  return peaks_and_valleys

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
print(peaks(data))
print(valleys(data))
print(peaks_and_valleys(data))


