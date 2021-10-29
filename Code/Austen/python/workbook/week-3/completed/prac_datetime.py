

from datetime import datetime


def run():
  # Create Date ==================================================================
  # Write a function that creates and returns a new datetime given the components
  results = []

  def create_date(month, day, year):
      month = str(month)
      if len(month) == 1:
        month = f'0{month}'
      date = f'{year}-{month}-{day} 00:00:00'
      return date
  print(create_date(4, 20, 2021))  # 2021-04-20 00:00:00
  results.append(create_date(4, 20, 2021))

  # Get Year =====================================================================
  # Write a function that returns the year of a given datetime

  def get_year(dt):
      year = dt.year
      return year
  print(get_year(datetime(2021, 4, 20)))  # 2021
  results.append(get_year(datetime(2021, 4, 20)))
  # Parse Date ===================================================================
  # Write a function that converts the given string into a datetime

  def parse_date(date_string):
      from string import digits
      months = ['january', 'february', 'march', 'april', 'may', 'june',
                'july', 'august', 'september', 'october', 'november', 'december']
      date = date_string.lower()
      date = date.split()
      month = date[0]
      month = months.index(month) + 1
      month = str(month)
      if len(month) == 1:
        month = f'0{month}'
      day = date[1]
      day = list(day)
      formatted = ''
      for char in day:
        if char in digits:
          formatted += str(char)
      day = formatted
      year = date[2]
      date = f'{year}-{month}-{day} 00:00:00'
      return date
  print(parse_date('April 20, 2021'))  # 2021-04-20 00:00:00
  results.append(parse_date('April 20, 2021'))
  # Parse Datetime ===============================================================
  # Write a function that converts a given string into a datetime

  def parse_datetime(date_string):
      datetime_string = date_string.split()
      month = datetime_string[0]
      day = datetime_string[1]
      year = datetime_string[2]
      date = f'{month} {day} {year}'
      date = parse_date(date)
      date = date.split()
      date = date[0]
      time = datetime_string[3]
      time = time.split(':')
      hour = int(time[0])
      minute = time[1]
      second = '00'
      timeofday = datetime_string[4]
      if timeofday == 'PM':
        hour += 12
      hour = str(hour)
      if len(hour) == 1:
        hour = f'0{hour}'
      time = f'{hour}:{minute}:{second}'
      datetime_string = f'{date} {time}'
      return datetime_string
  print(parse_datetime('April 20, 2021 09:30 AM'))  # 2021-04-20 09:30:00
  results.append(parse_datetime('April 20, 2021 09:30 AM'))
  # Format Datetime ==============================================================
  # Write a function that converts the given datetime into a string

  def format_datetime(dt):
    months = ['january', 'february', 'march', 'april', 'may', 'june',
              'july', 'august', 'september', 'october', 'november', 'december']
    month = dt.month - 1
    month = months[month].capitalize()
    day = dt.day
    year = dt.year
    time = dt.time
    time = datetime.time(dt)
    hour = time.hour
    minute = time.minute
    timeofday = 'AM'
    if hour > 12:
      hour -= 12
      timeofday = 'PM'
    dt = f'{month} {day}, {year} {hour}:{minute} {timeofday}'
    return dt

  print(format_datetime(datetime(2021, 4, 20, 17, 30)))
  results.append(format_datetime(datetime(2021, 4, 20, 17, 30)))
  return results


run()
