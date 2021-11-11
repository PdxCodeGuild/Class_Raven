def lab_search_sort():
  def generate():
    import random
    data = []
    while len(data) < 100:
      number = random.randint(1, 100)
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

  def bubble_sort(data):
    def swap(data, index):
      prev = index - 1
      item = data.pop(index)
      data.insert(prev, item)

    def sort(data):
      index = 0
      endex = len(data) - 1
      if index == 0:
        next = index + 1
        while data[index] > data[next]:
          swap(data, next)
        index += 1
      while index <= endex:
        prev = index - 1
        while data[prev] > data[index]:
          swap(data, index)
        index += 1
      return data

    def check(data):
      complete = False
      while complete == False:
        swapped = False
        for item in data:
          index = data.index(item)
          endex = len(data) - 1
          prev = index - 1
          next = index + 1
          if index < endex:
            if item > data[next]:
              data = sort(data)
              swapped = True
          elif index == endex:
            if item < data[prev]:
              data = sort(data)
              swapped = True
        if swapped == False:
          complete = True
      return data
    data = check(data)
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
