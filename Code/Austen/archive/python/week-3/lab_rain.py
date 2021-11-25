from datetime import datetime
from data.models import Node, Stack


def lab_rain():
  def getdata(file):
    from requests import get
    url = 'https://or.water.usgs.gov/non-usgs/bes/hayden_island.rain'
    response = get(url)
    data = response.text
    file = open(file, 'w')
    file = file.write(data)

  def read_data(file):
    file = open(file).read()
    data = file.split()
    return data

  def parse_data(data):
    dateformat = '%d-%b-%Y'
    raindata = stack()
    raintotals = stack()
    rain = []
    for entry in data:
      raindata.push(entry)
    while raindata.count > 0:
      entry = raindata.pop()
      try:
        date = datetime.strptime(entry, dateformat)
      except:
        rain.append(entry)
      else:
        year = date.year
        month = date.month
        day = date.day
        rain.reverse()
        daily = {f'{year}-{month}-{day}': rain[0]}
        raintotals.push(daily)
        rain = []
    return raintotals

  def save_stack(stack, file):
    import json
    data = {}
    while stack.count > 0:
      node = stack.pop()
      data.update(node)
    data = json.dumps(data)
    file = open(file, 'w')
    file.write(data)

  file = 'X:\pdx-code-guild\Class_Raven\Code\Austen\python\week-3\data\\raw-rain-data.txt'
  node = Node.node
  stack = Stack.stack

  getdata(file)
  data = read_data(file)
  raintotals = parse_data(data)
  print(raintotals.count)

  file = 'X:\pdx-code-guild\Class_Raven\Code\Austen\python\week-3\data\\rain-data.json'
  save_stack(raintotals, file)


lab_rain()
