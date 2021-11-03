import random

def total_return(number_of_tickets, total_won):
    cost_of_tickets = -number_of_tickets * 2
    earnings = cost_of_tickets + total_won
    roi = earnings/abs(cost_of_tickets)
    return roi*100

def lottery_machine(number_of_tickets):
    matches = []
    total_winnings = 0
    number_of_matches = [0]
    winning_numbers_list = []
    winning_ticket_list = [random.randint(1,99) for x in range(6)]
    for x in range(number_of_tickets):
        user_ticket_list = [random.randint(1,99) for x in range(6)]
        for x in range(6):
            user_number = user_ticket_list[x]
            winning_number = winning_ticket_list[x]
            if user_number == winning_number:
                winning_numbers_list.append(user_number)
                matches = len(winning_numbers_list)
                number_of_matches[0] = matches
            else:
                continue       
        winnings = [i*0 if i == 0 else i*4 if i == 1 else i/i*7 if i == 2 else i/i*100 if i == 3 else i/i*50000 if i == 4 else i/i*1000000000 if i == 5 else 25000000 for i in number_of_matches]          
        winnings = ''.join([str(integer) for integer in winnings])
        winnings = float(winnings)
        winnings = int(winnings)
        total_winnings += winnings
        winning_numbers_list = []
        number_of_matches = [0]
    return total_winnings

how_many_tickets = int(input('How many tickets would you like to buy?\n> '))

total_winnings = lottery_machine(how_many_tickets)

return_on_investment = total_return(how_many_tickets, total_winnings)

print(f'You spent ${how_many_tickets * 2}')
print(f'The total amount of your winnings is: ${total_winnings}')
print(f'The return on your investment is: {round(return_on_investment)}%')

