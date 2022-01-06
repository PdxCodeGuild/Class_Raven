def bubble(data):
  # * n := length(A)
  length = len(data)
  # * repeat -swapped = false
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
  return data
