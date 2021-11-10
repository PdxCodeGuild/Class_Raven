def linear(data, value):
  print(data)
  try:
    index = 0
    for item in data:
      if item != value:
        index += 1
      elif item == value:
        return index
  except:
    return 'value not found'


def binary(data, value):
  data.sort()
  print(data)
  length = len(data)
  left = 0
  right = length - 1
  while left <= right:
    median = (left + right) // 2
    if data[median] < value:
      left = median + 1
    elif data[median] > value:
      right = median - 1
    else:
      return median
  return 'value not found'
