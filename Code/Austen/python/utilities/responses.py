class response:
  class polar:
    yes = ['yes', 'yep', 'sure']
    no = ['no', 'nope', 'nah']
    valid = yes + no

  class numeric:
    zero = [0, 'zero']
    one = [1, 'one']
    two = [2, 'two']
    three = [3, 'three']
    four = [4, 'four']
    five = [5, 'five']
    six = [6, 'six']
    seven = [7, 'seven']
    eight = [8, 'eight']
    nine = [9, 'nine']
    ten = [10, 'ten']
    valid = zero + one + two + three + four + \
        five + six + seven + eight + nine + ten

  def validate(selection, options):
    for option in options:
      matched = response.characters(selection, option)
      if matched == True:
        selection = option
    return selection

  def characters(selection, option):
    characters = list(selection)
    counter = 0
    option = option.lower()
    for char in characters:
      if char in option:
        counter += 1
      elif char == ' ':
        counter += 1
    if counter == len(characters):
        option = True
    else:
        option = False
    return option
