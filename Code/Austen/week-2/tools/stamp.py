from datetime import datetime


# * creates a timestamp then provides addition methods to customize the formatting that the native code does not
class Stamp:
  def __init__(stamp):
    stamp.now = datetime.now()
    stamp.date = stamp.now.date()
    stamp.time = stamp.now.time()
    stamp.month = stamp.date.month
    stamp.day = stamp.date.day
    stamp.hour = stamp.time.hour
    stamp.minute = stamp.time.minute

# * method to create a 'results from:' timestamp
  def results(stamp):
    stamp = f'Results from {stamp.month}/{stamp.day} at {stamp.hour}:{stamp.minute}:'
    return stamp
