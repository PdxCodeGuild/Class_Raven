from random import randint
from methods import *


def getdata(datalength):
    data = []

    for i in range(0, datalength):
        digit = randint(1, datalength * 2)
        while digit in data:
            digit = randint(1, datalength * 2) 
        if digit not in data:
            data.append(digit)
    return data

data = getdata(25)
print()
print('randomly generated dataset:\n', data)
print('\nlinear search for the number 8 \n  index= ', search.linear(data, 8))
data = sort.bubble(data)
print('\ndata sorted using the "bubble" method:\n', data)
print('\nbinary search for the number 10 \n  index= ', search.binary(data, 10))
print()
