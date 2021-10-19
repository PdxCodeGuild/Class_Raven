from math import exp
import random

winning_list = []
balance = 0
loop_times = 0
earnings = 0
expenses = 0


def win_list():
    for x in range (0, 6):
        winning_list.append(random.randint(1, 99))
    return winning_list


def get_ticket():
    ticket = []
    for x in range (0, 6):
        ticket.append(random.randint(1, 99))
    
    return ticket

win_list()
print(winning_list)

while loop_times < 100000:
    count = 0
    expenses -= 2
    ticket = get_ticket()
    for i in range(len(ticket)):
        if ticket[i] == winning_list[i]:
            count += 1
    if count == 1:
        earnings += 4
    elif count == 2:
        earnings += 7
    elif count == 3:
        earnings += 100
    elif count == 4:
        earnings += 50000
    elif count == 5:
        earnings += 1000000
    elif count == 6:
        earnings += 25000000

    loop_times += 1
roi = (earnings - expenses)/expenses

print(f'Your earned {earnings} and you lost {expenses} your roi is {roi}')

#get rid of redundancy, add comments to cement the ideas in your thinking
    
            
