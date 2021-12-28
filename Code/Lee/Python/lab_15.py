"""
Lee Colburn
Evening Bootcamp - PDX Code Guild
Lab 15 - Rain Data
"""

import csv
from datetime import datetime
import pandas
import math

def average(x):
    total = sum(x[i] for i in range(len(x)))
    return total / len(x)

def variance(x):
    mu = average(x)
    total = sum((x[i] - mu)**2 for i in range(len(x)))
    return total / len(x)

def standard_deviation(x):
    v = variance(x)
    return math.sqrt(v)

def most_rain(x):
    record = 0
    for current_record in x:
        current_record = int(current_record)
        if current_record > record:
            record = current_record

    for key, value in data_dict.items():
        if int(value) == record:
            print(f"Record rainfall of: {value} hundreths of an inch on {key}")
    return

with open('lab_15_data.csv', 'r', encoding='utf-8') as f:
    contents = f.read().split('\n')
    cleaned_data = []
    data_dict = {}
    counter = 0

    for line in contents:
        line = line.split()
        try:
            date = line[0]
            total = line[1]
            data_dict[date] = total
        except IndexError:
            continue

    del data_dict['Date']

    for entry in data_dict:
        entry = datetime.strptime(entry, '%d-%b-%Y')

    daily_rainfall = []
    for key, value in data_dict.items():
        if value == "-":
            data_dict[key] = 0
            value = 0
        value = int(value)
        daily_rainfall.append(0+value)

    most_rain(daily_rainfall)