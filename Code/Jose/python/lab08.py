import random

def pick6():    # Generating 6 random numbers and appending them into a list.
    random_numbers = []
    random_number = 0
    for i in range(6):
        random_number = random.randint(1,99)
        random_numbers.append(random_number)
    return random_numbers

winning_numbers = pick6()
ticket = pick6()

x = 0    # Variable used to keep track of the amount of times we reroll.
earnings = 0
expenses = 0

while x < 100000:
    x += 1
    y = 0    # Variable used to specify the indices in the lists.
    ticket = pick6()
    expenses += 2
    matched_numbers = 0
    while y < len(ticket):
        if ticket[y] == winning_numbers[y]:    # Comparing the indices one at a time, each in their exact order. 
            matched_numbers += 1
        y += 1    # Move up one index after every comparison
    if matched_numbers == 1:
        earnings += 4
    elif matched_numbers == 2:
        earnings += 7
    elif matched_numbers == 3:
        earnings += 100
    elif matched_numbers == 4:
        earnings += 50000
    elif matched_numbers == 5:
        earnings += 1000000
    elif matched_numbers == 6:
        earnings += 25000000

roi = (earnings - expenses)/expenses
print(f"""
{earnings} are your net winnings.
{expenses} are your expenses.
{roi} is your return on invesments.
""" )
