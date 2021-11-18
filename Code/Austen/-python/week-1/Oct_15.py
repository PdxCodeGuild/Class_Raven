def lab_data_visualization():
  index = []
  data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
  peaks = []
  valleys = []
  peak_or_valley = []

  def _peak_or_valley():
    counter = 0
    length = len(data)
    for point in data:
      if counter == 0:
        index.append(counter)
        counter += 1
      while 0 < counter < (length - 1):
        prev = data[counter - 1]
        current = data[counter]
        next = data[counter + 1]
        if current < prev:
          if current < next:
            valleys.append(counter)
            peak_or_valley.append(counter)
        elif current > prev:
          if current > next:
            peaks.append(counter)
            peak_or_valley.append(counter)
        index.append(counter)
        counter += 1

      index.append(counter)
      break

  def _draw_chart():
    _peak_or_valley()
    print('\n| index | value |')
    for i in index:
      id = i
      i = str(i)
      if len(i) == 1:
        i = '0' + i
      chart = 'X' * data[id]
      while len(chart) < 9:
        chart += '-'
      print(f'   |{i}|', f'   |{data[id]}|   ', chart)
    print('')
    response = input('Print raw lists (y/n)?\n')
    if response == 'y':
      print(f'\nData: {data}')
      print(f'Peaks: {peaks}')
      print(f'Valleys: {valleys}')
      print(f'Peaks & Valleys: {peak_or_valley}')
