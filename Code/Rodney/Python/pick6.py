import random


def winning_money(number_of_tickets):
    matches = []
    winning_numbers_list = []
    winning_ticket_list = [random.randint(1,99) for x in range(6)]
    for x in range(number_of_tickets):
        user_ticket_list = [random.randint(1,99) for x in range(6)]
        for x in range(6):
            user_number = user_ticket_list[x]
            winning_number = winning_ticket_list[x]
            if user_number == winning_number:
                winning_numbers_list.append(user_number)
                matches.append(len(winning_numbers_list))
                winnings = [i*0 if i == 0 else i*4 if i == 1 else i/i*7 if i == 2 else i/i*100 if i == 3 else i/i*50000 if i == 4 else i/i*1000000000 if i == 5 else 25000000 for i in matches]        
                winnings = int(''.join([str(integer) for integer in winnings]))


winning_money(2)







'''matches = []
winning_numbers_list = []

for x in range(6):
    user_number = user_ticket_list[x]
    winning_number = winning_ticket_list[x]
    if user_number == winning_number:
        winning_numbers_list.append(user_number)
matches.append(len(winning_numbers_list))
winnings = [i*0 if i == 0 else i*4 if i == 1 else i/i*7 if i == 2 else i/i*100 if i == 3 else i/i*50000 if i == 4 else i/i*1000000000 if i == 5 else 25000000 for i in matches]        
winnings = int(''.join([str(integer) for integer in winnings]))

print(user_ticket_list)
print(winning_ticket_list)
print(winning_numbers_list)
print(f'${#winnings}')'''

import random


def winning_money(number_of_tickets):
    matches = []
    winning_numbers_list = []
    winning_ticket_list = [1, 3, 5, 6, 8, 9]#[random.randint(1,99) for x in range(6)]
    for x in range(number_of_tickets):
        user_ticket_list = [3, 3, 5, 4, 7, 9]#[random.randint(1,99) for x in range(6)]
        for x in range(6):
            user_number = user_ticket_list[x]
            winning_number = winning_ticket_list[x]
            if user_number == winning_number:
                winning_numbers_list.append(user_number)
                matches.append(len(winning_numbers_list))
            else:
                continue
            winnings = [i*0 if i == 0 else i*4 if i == 1 else i/i*7 if i == 2 else i/i*100 if i == 3 else i/i*50000 if i == 4 else i/i*1000000000 if i == 5 else 25000000 for i in matches]        
            winnings = int(''.join([str(integer) for integer in winnings]))
           

winning_money(2)