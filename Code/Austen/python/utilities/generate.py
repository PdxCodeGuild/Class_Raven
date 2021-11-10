class id:
  def AN4():
    import string, random
    id = ''
    options = string.digits + string.ascii_uppercase
    while len(id) < 4:
      char = random.choice(options)
      id += char
    return id