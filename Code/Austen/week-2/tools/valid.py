class answers:
  positive = []
  negative = []

  def validate(selection, options):
    characters = list(selection)
    counter = 0
    for option in options:
      for char in characters:
        if char in option:
          counter += 1
        elif char == ' ':
          counter += 1
      if counter == len(characters):
        selection = option
      return selection
