"""
Lee Colburn
Evening Bootcamp - PDX Code Guild
Lab 8
"""
from random import randint

# Generate a list of 6 random numbers representing the winning tickets
winning_ticket = []
def pick6(ticket):
    """Takes in a list & provides 6 random numbers [0-99]"""
    for x in range(6):
        ticket.append(randint(0,99))
    return ticket

def num_matches(winning, guess):
    """Takes in winning string and guess string. evaluates returns total match count"""
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
for i in range(1_000_000):
    # Generate a list of 6 random numbers representing the ticket 
    guess_ticket = []
    pick6(guess_ticket)

    # Add 2 to expenses (you bought a ticket) 
    expenses += 2

    # Find how many numbers match 
    match = num_matches(winning_ticket, guess_ticket)

    ############TEST STATEMENTS######################
    # print(f"Round:{i+1}")
    # print(f"Winning Ticket: {winning_ticket}")
    # print(f"Guess Ticket: {guess_ticket}")
    # print(f"matched {match} numbers")
    #################################################

    # Add to your balance the winnings from your matches    
    if match == 6:
        winnings += 25000000
        print(f"Msatched {match} numbers")
        print(f"Winning Ticket: {winning_ticket}")
        print(f"Guess Ticket: {guess_ticket}")
    elif match == 5:
        winnings += 1000000
        print(f"Matched {match} numbers")
        print(f"Winning Ticket: {winning_ticket}")
        print(f"Guess Ticket: {guess_ticket}")
    elif match == 4:
        print(f"Matched {match} numbers")
        print(f"Winning Ticket: {winning_ticket}")
        print(f"Guess Ticket: {guess_ticket}")
        winnings += 50000
    elif match == 3:
        winnings += 100
    elif match == 2:
        winnings += 7
    elif match == 1:
        winnings += 4
    elif match == 0:
        continue
    match = 0
    continue

# The ROI (return on investment) is defined as (earnings - expenses)/expenses. Calculate your ROI, print it out along with your earnings and expenses.
roi = ((winnings - expenses)/expenses)*100

# After the loop, print the final balance, round percentages to two places {a:.2f}
print(f"\nTotal Expenses: ${expenses:,} \nTotal Winnings: ${winnings:,} \nTotal Return:   ${winnings - expenses:,}\nROI (percentage): {roi:.2f}% \n") 