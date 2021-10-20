# ticket_devbox.py
import random


# creates on winning ticket
def winning_nums():
    winning_numbers = []
    for i in range(0,6):
        num = random.randint(1,99)
        winning_numbers.append(num)
    return(winning_numbers)

# winning_nums()

# Creates a list of lists. inner lists are lotto tickets
# def rand_ticket_nums():
#     ticket_numbers = []
#     rand_ticket_list = []
#     for i in range(0,6):
#         num = random.randint(1,99)
#         ticket_numbers.append(num)
#     # rand_ticket_list.append(ticket_numbers) #finally works! all three must be evenly indented 4 from for
#     return rand_ticket_list

#rand_ticket_nums()


# I want this function to go through the list of lotto tickets, compare the mumbers to the wining ticket
# perhaps it should create a list of how many match? 
# Later we could parse through the list to calculate the payout for each ticket and update balance
def num_matches(winning_ticket, tick):
    match_list = []
    how_many_match = 0
    print(f'winning ticket {winning_ticket}, tick, {tick}')
    if winning_ticket[0] == tick[0]:
        how_many_match +=1
    if winning_ticket[1]== tick[1]:
        how_many_match +=1
    if winning_ticket[2]== tick[2]:
        how_many_match +=1
    if winning_ticket[3]== tick[3]:
        how_many_match +=1
    if winning_ticket[4] in tick:
        how_many_match +=1
    if winning_ticket[5] in tick:
        how_many_match +=1
    match_list.append(how_many_match)

    return match_list




# Parse through the list created in how many match and calculate the payout for each ticket and update balance
def calculate(matches):
    win = 0

    for match in matches:
        if match == 1:
            win += 4
        elif match == 2:
            win += 7
        elif match == 3:
            win += 100
        elif match == 4:
            win += 50000
        elif match == 5:
            win += 1000000
        elif match == 6:
            win += 25000000
    return(win)

def your_cash_balance():
    balance = 0
    i = 0
    winning_ticket = winning_nums()
    while i < 100000:
    # purchase a lotto ticket
        tick = winning_nums()
        balance -= 2  
    # print(balance)
    # do comparisons here
    
    # add winnings to balance
    # do comparisons here
        matches = num_matches(winning_ticket, tick) # returns one numer - 0-6 the number of matches

        balance += calculate(matches)
        i += 1
        print(f' Your cash balance is: {balance}')
your_cash_balance()