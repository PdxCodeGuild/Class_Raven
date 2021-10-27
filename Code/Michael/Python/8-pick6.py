"""
PDX Code Guild Full Stack Bootcamp
->Lab 08
  Pick6
Michael B

Generate a list of 6 random numbers representing the winning tickets
Start your balance at 0
Loop 100,000 times, for each loop:
Generate a list of 6 random numbers representing the ticket
Subtract 2 from your balance (you bought a ticket)
Find how many numbers match
Add to your balance the winnings from your matches
After the loop, print the final balance
The ROI (return on investment) is defined as (earnings - expenses)/expenses. Calculate your ROI, print it out along with your earnings and expenses.

"""


def generate_ticket(num=6) -> list:
    from random import randint

    picked_numbers = []
    for number in range(0, num):
        picked_numbers.append(randint(1, 99))
    return picked_numbers


def calculate_roi(earnings=0, expenses=0) -> int:  # ROI not returning correctly.
    return (earnings - expenses) / expenses


def check_numbers(winning_ticket, chosen_ticket) -> int:
    correct_matches = 0
    winning_values = [
        (0, 0),
        (1, 4),
        (2, 7),
        (3, 100),
        (4, 50000),
        (5, 1000000),
        (6, 25000000),
    ]
    for number in range(0, len(winning_ticket) - 1):
        if winning_ticket[number] == chosen_ticket[number]:
            correct_matches += 1
    return winning_values[correct_matches][1]


if __name__ == "__main__":
    winnings = 0
    tickets = 100000
    ticket_cost = 2
    spendings = ticket_cost * tickets
    winning_ticket = generate_ticket()
    for ticket in range(1, tickets):
        chosen_ticket = generate_ticket()
        winnings = winnings + check_numbers(winning_ticket, chosen_ticket)

    print("ROI: ", calculate_roi(winnings, spendings))
    print("Winnings:", "${:,.2f}".format((winnings)))
    print(
        "Balance:",
        "${:,.2f}".format(-spendings + winnings)
        if -spendings + winnings >= 0
        else "(${:,.2f})".format(-spendings + winnings).replace("-", ""),
    )
