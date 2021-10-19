# A Lottery Sim

import random


# first generate one list of wining numbers
def winning_nums():
    winning_numbers = []
    for i in range(0,6):
        num = random.randint(1,99)
        winning_numbers.append(num)
    return(winning_numbers)

# then Generate a list of 6 random numbers representing the winning ticket 
# and call it 100000 times in anothe function 

def rand_ticket_nums():
    rand_ticket_nums = []
    for i in range(0,6):
        num = random.randint(1,99)
        rand_ticket_nums.append(num)
    return(rand_ticket_nums)


# see how many numbers match
# I'm confused about how to run rand_ticket_nums 1000000 times and winning tickets once
def num_matches(winning_nums, loto_ticket):
    how_many_match = 0
    #  how do I get winning tickets in here without changing it every time?
    
    #  do something here to compare the winning_nums list 
    # to rand_ticket_nums list and return how many match
    # I could do something sloppy like:
    if winning_numbers[0] in rand_ticket_nums:
        how_many_match +=1
    if wwinning_numbers[1]in rand_ticket_nums:
        how_many_match +=1
    if winning_numbers[2]in rand_ticket_nums:
        how_many_match +=1
    if winning_numbers[3]in rand_ticket_nums:
        how_many_match +=1
    if winning_numbers[4]in rand_ticket_nums:
        how_many_match +=1
    if winning_numbers[5]in rand_ticket_nums:
        how_many_match +=1
    print(how_many_match)

 
def calculate():
    num_matches()
    win = 0
    if how_many_match == 1:
        win += 4
    elif how_many_match == 2:
        win += 7
    elif how_many_match == 3:
        win += 100
    elif how_many_match == 4:
        win += 50000
    elif how_many_match == 5:
        win += 1000000
    elif how_many_match == 6:
        win += 25000000
    return win   



def your_cash_balance():
    balance = 0
    i = 0
    while i < 100000:
    # purchase a lotto ticket
        rand_ticket_nums() 
        balance -= 2  
    # print(balance)
    # add winnings to balance
        calculate()
        i += 1

  



   

# Loop 100,000 times, for each loop:
# Generate a list of 6 random numbers representing the ticket
# Subtract 2 from your balance (you bought a ticket)
# Find how many numbers match
# Add to your balance the winnings from your matches
# After the loop, print the final balance