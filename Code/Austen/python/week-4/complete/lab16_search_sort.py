def lab_search_sort():
  def generate():
    import random
    data = []
    while len(data) < 100:
      number = random.randint(0, 99)
      if number not in data:
        data.append(number)
    return data

  def linear_search(data, value):
    print(data)
    try:
      index = data.index(value)
      return index
    except:
      return 'value not found'

  def binary_search(data, value):
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
  # * procedure bubbleSort(A : list of sortable items)

  def bubble_sort(data):
    # * n := length(A)
    length = len(data)
    # * repeat
    ''  # * swapped = false
    counter = 0
    while counter < length:
      # * for i := 1 to n - 1 inclusive do
      for point in data:
        index = data.index(point)
        previous = index - 1
        if previous >= 0:
          # * /* if this pair is out of order */
          # * if A[i - 1] > A[i] then
          if point < data[previous]:
            # * swap(A[i - 1], A[i])
            point = data.pop(index)
            data.insert(previous, point)
            counter = 0
          else:
            counter += 1

        # * end if
      # * end for
    # * until not swapped
    return data

  data = generate()
  selection = input('search, sort, or quit?\n')
  results = []
  while selection != 'quit':
    if selection == 'search':
      value = int(input('which number?\n'))
      selection = input('linear or binary?\n')
      if selection == 'linear':
        index = linear_search(data, value)
        result = f'index of {value} using linear search: {index}'
        results.append(result)
        print(result)
        selection = input('search, sort, or quit?\n')
      elif selection == 'binary':
        index = binary_search(data, value)
        result = f'index of {value} using binary search: {index}'
        results.append(result)
        print(result)
        selection = input('search, sort, or quit?\n')
    elif selection == 'sort':
      data = generate()
      print('\nbefore sorting\n')
      print(data)
      data = bubble_sort(data)
      print('\nafter sorting\n')
      print(data)
      results.append(data)
      selection = input('search, sort, or quit?\n')
  return results


lab_search_sort()
