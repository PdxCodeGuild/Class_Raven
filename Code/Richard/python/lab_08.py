print("Pick 6 Lottery!")
import random
winning = []
ticket = []
number_of_tickets = 0
wallet_balance = 0
number_match = 0
wallet_gain = 0

def pick6():  #generate list -ticket
    ticket = []
    while len(ticket) < 6:
        num = random.randint(1,99)
        if num != any(ticket): 
#intially problems where a repeat digit would break the code before adding a requirement of 6 digits.
            ticket.append(num)
    return ticket

winning = pick6()
print(winning)

while number_of_tickets < 100000:
    win_num = 0
    #wallet_gain = 0
    attempt = pick6()
    for num in range(6):
        if attempt[num] == winning[num]:
            win_num += 1
            number_match += 1
    if win_num == 1:
        wallet_gain += 4
    if win_num == 2:
        wallet_gain += 7
    if win_num == 3:
        wallet_gain += 100
    if win_num == 4:
        wallet_gain += 50000
    if win_num == 5:
        wallet_gain += 1000000
    if win_num == 6:
        wallet_gain += 25000000
    win_num = 0
    number_of_tickets += 1
    wallet_balance -= 2

print(f"ticket costs i.e. expenses = ${wallet_balance}")
print(f'winnings = {wallet_gain}')
print(f"number of tickets purchased = {number_of_tickets}")
print(f"number of matches = {number_match}")
ROI = (wallet_gain - (number_of_tickets*2))/(number_of_tickets*2) 
print (f"ROI = ${ROI}")