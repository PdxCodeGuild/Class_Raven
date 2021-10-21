"""Pick6

Have the computer play pick6 many times and determine net balance.

Initially the program will pick 6 random numbers as the 'winner'. 
Then try playing pick6 100,000 times, with the ticket cost and payoff below.

A ticket contains 6 numbers, 1 to 99, and the number of matches between the ticket and the winning numbers determines the payoff. 
Order matters, if the winning numbers are [5, 10] and your ticket numbers are [10, 5] you have 0 matches. 
If the winning numbers are [5, 10, 2] and your ticket numbers are [10, 5, 2], you have 1 match. 
Calculate your net winnings (the sum of all expenses and earnings).

    a ticket costs $2
    if 1 number matches, you win $4
    if 2 numbers match, you win $7
    if 3 numbers match, you win $100
    if 4 numbers match, you win $50,000
    if 5 numbers match, you win $1,000,000
    if 6 numbers match, you win $25,000,000

One function you might write is pick6() which will generate a list of 6 random numbers, which can then be used for both the winning numbers and tickets.
 Another function could be num_matches(winning, ticket) which returns the number of matches between the winning numbers and the ticket.

Steps

    Generate a list of 6 random numbers representing the winning tickets
    Start your balance at 0
    Loop 100,000 times, for each loop:
    Generate a list of 6 random numbers representing the ticket
    Subtract 2 from your balance (you bought a ticket)
    Find how many numbers match
    Add to your balance the winnings from your matches
    After the loop, print the final balance

Version 2

The ROI (return on investment) is defined as (earnings - expenses)/expenses. Calculate your ROI, print it out along with your earnings and expenses.
"""




from random import choice
    
def create_winning_ticket():
    winner = [choice(range(0,99)) for x in range(6)] # this is using list comprehension to pick a random number from 0 - 99 6 times to create the winning ticket    
    return winner

def gambling(winner):
    matches = 0
    winnings = 0
    expenses = 0
    for i in range(100000):
        if matches == 1: # These if statments are going to be checked after each random ticket is done being compared to the winning ticket. 
           winnings += 4
        elif matches == 2:
            winnings += 7
        elif matches == 3:
            winnings += 100
        elif matches == 4:
            winnings += 50000
        elif matches ==  5:
            winnings += 1000000
        elif matches == 6:
            winnings += 25000000
        matches = 0
        user_ticket = [choice(range(0,99)) for x in range(6)] # same idea as creating the winning ticket
        expenses -= 2 # each time a ticket is created, you just paid $2 so its subtracting that.
        for num in range(len(user_ticket)): # using the for loop to compare each element in user_ticket with each element in the winning ticket. Since they are the same length it makes this part simple
            if user_ticket[num] == winner[num]:
                matches += 1 # each time an element matches in both lists we increment by 1, so that we can add winnings equal to the amount of matches
    expenses += winnings

    if expenses == 0: # If expenses is zero than we are going to get the 'ZeroDivisionError: division by zero' error 
            roi = 0
    else:
        roi = (winnings - expenses)/expenses
    print(f"your winnings are: ${winnings}\ntotal expenses with your winnings subtracted(if any) is: ${expenses}\nTotal Return of Investment is: {roi}, thanks for playing.")
    
    
gambling(create_winning_ticket())

            

        
