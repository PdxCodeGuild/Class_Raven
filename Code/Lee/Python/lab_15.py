"""
Lee Colburn
Evening Bootcamp - PDX Code Guild
Lab 15 - Rain Data
"""

import csv
from datetime import datetime
import pandas



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

    for entry in data_dict.keys():
        entry = datetime.strptime(entry, '%d-%b-%Y')

    sum_of_totals = 0
    for entry in data_dict.values():
        if entry == "-":
            entry = 0
        entry = int(entry)
        sum_of_totals += entry

    print(sum_of_totals)
