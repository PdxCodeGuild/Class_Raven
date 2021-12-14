def generate():
  import random
  data = []
  while len(data) < 100:
    number = random.randint(0, 99)
    if number not in data:
      data.append(number)
  return data
