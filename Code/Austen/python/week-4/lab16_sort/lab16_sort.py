from functions.generate import generate
from functions.search import linear, binary
from functions.sort import bubble

data = generate()
selection = input('search, sort, or quit?\n')
results = []
while selection != 'quit':
  if selection == 'search':
    value = int(input('which number?\n'))
    selection = input('linear or binary?\n')
    if selection == 'linear':
      index = linear(data, value)
      result = f'index of {value} using linear search: {index}'
      results.append(result)
      print(result)
      selection = input('search, sort, or quit?\n')
    elif selection == 'binary':
      index = binary(data, value)
      result = f'index of {value} using binary search: {index}'
      results.append(result)
      print(result)
      selection = input('search, sort, or quit?\n')
  elif selection == 'sort':
    data = generate()
    print('\nbefore sorting\n')
    print(data)
    data = bubble(data)
    print('\nafter sorting\n')
    print(data)
    results.append(data)
    selection = input('search, sort, or quit?\n')
