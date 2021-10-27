
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
    #changed this from -= to += because it was messing with the calculation
    expenses += 2
    #this generates a new ticket each time by calling on the get_ticket() function.
    ticket = get_ticket()
    #for each element in the ticket list im setting a statement to compare the values to see if they're equal to eachother.
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
roi = (earnings - expenses)/expenses * 100
roi = round(roi)
print(f'Your earned {earnings} and you lost {expenses} your roi is {roi} %.')


    
            
