"""
Lee Colburn
Evening Bootcamp - PDX Code Guild
Lab 7
"""


"""Have the computer play pick6 many times and determine net balance.

Initially the program will pick 6 random numbers as the 'winner'. Then try playing pick6 100,000 times, with the ticket cost and payoff below.

A ticket contains 6 numbers, 1 to 99, and the number of matches between the ticket and the winning numbers determines the payoff. 
Order matters, if the winning numbers are [5, 10] and your ticket numbers are [10, 5] you have 0 matches. If the winning numbers are [5, 10, 2] and your ticket numbers are [10, 5, 2], you have 1 match. Calculate your net winnings (the sum of all expenses and earnings).

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
x Generate a list of 6 random numbers representing the winning tickets
x Start your balance at 0
x Loop 100,000 times, for each loop:
Generate a list of 6 random numbers representing the ticket
Subtract 2 from your balance (you bought a ticket)
Find how many numbers match 
Add to your balance the winnings from your matches

After the loop, print the final balance

Version 2
The ROI (return on investment) is defined as (earnings - expenses)/expenses. Calculate your ROI, print it out along with your earnings and expenses."""
from random import randint

# Generate a list of 6 random numbers representing the winning tickets
winning_ticket = []
def pick6(ticket):
    """Takes in a list & provides 6 random numbers [0-99]"""
    for x in range(6):
        ticket.append(randint(0,99))
    return ticket

def num_matches(winning, guess):
    match = 0
    for (w, g) in zip(winning, guess):
        if w == g:
            match += 1
    return match

# Start your balances at 0
balance = 0
expenses = 0
match = 0
winnings = 0
pick6(winning_ticket)

# Loop 100,000 times: 
for i in range(100000):

    # Generate a list of 6 random numbers representing the ticket 
    guess_ticket = []
    pick6(guess_ticket)

    # Subtract 2 from your balance (you bought a ticket) 
    expenses += 2

    # Find how many numbers match 
    match = num_matches(winning_ticket, guess_ticket)

    ############TEST STATEMENTS######################
    # print(f"Round:{i+1}")
    # print(f"Winning Ticket: {winning_ticket}")
    # print(f"Guess Ticket: {guess_ticket}")
    # print(f"matched {match} numbers")

    # Add to your balance the winnings from your matches
    
    if match == 1:
        winnings += 4
    elif match == 2:
        winnings += 7
    elif match == 3:
        winnings += 100
    elif match == 4:
        winnings += 50000
    elif match == 5:
        winnings += 1000000
        print(f"matched {match} numbers")
        print(f"Winning Ticket: {winning_ticket}")
        print(f"Guess Ticket: {guess_ticket}")
    elif match == 6:
        winnings += 25000000
        print(f"matched {match} numbers")
        print(f"Winning Ticket: {winning_ticket}")
        print(f"Guess Ticket: {guess_ticket}")
    match = 0
    continue

# The ROI (return on investment) is defined as (earnings - expenses)/expenses. Calculate your ROI, print it out along with your earnings and expenses.
roi = ((winnings - expenses)/expenses)*100

# After the loop, print the final balance, round percentages to two places {a:.2f}
print(f"\nTotal Expenses: ${expenses} \n Total Winnings: ${winnings} \n Total Return: ${winnings - expenses}\n ROI (percentage): {roi:.2f}%") 