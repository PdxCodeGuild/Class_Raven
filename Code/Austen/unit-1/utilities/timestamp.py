from datetime import datetime


# * creates a timestamp then provides addition methods to customize the formatting that the native code does not
class now:
  now = datetime.now()
  date = now.date()
  month = date.month
  day = date.day
  year = date.year
  time = now.time()
  hour = time.hour
  minute = time.minute
  second = time.second

  def standard():
    standard = f'{now.year}{now.month}{now.day} {now.hour}:{now.minute}:{now.second}'
    return standard

# * method to create a 'result from:' timestamp
  def result():
    result = f'Result from {now.month}/{now.day} at {now.hour}:{now.minute}:'
    return result
