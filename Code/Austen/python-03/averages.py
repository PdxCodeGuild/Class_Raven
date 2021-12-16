def lab_averages():
  def v1():
    numbers = [5, 0, 8, 3, 4, 1, 6]
    total = 0
    for number in numbers:
      total += number
    average = total / len(numbers)
    average = round(average, 2)
    message = f'Your average is: {average}'
    return message

  def v2():
    print('\n (enter done to see average or quit to exit.)')
    stop = ['quit', 'done']
    numbers = []
    total = 0
    response = input('Enter a number: \n')
    while response not in stop:
      try:
        number = float(response)
      except:
        print('invalid')
        response = input('Enter done, quit, or a number: \n')
      else:
        numbers.append(number)
        response = input('Enter a number: \n')
      if response == 'quit':
        print('Goodbye.')
      elif response == 'done':
        for number in numbers:
          total += number
        if total == 0:
          average = 0
        elif total > 0:
          average = total / len(numbers)
          average = round(average, 2)
        message = f'Your average is: {average}'
    return message