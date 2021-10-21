'''Pick6 Lab08
By Philip Bartoo
PDX Code Guild'''

from random import randint
#Request the number of player tickets
tickets = int(input('Enter the number of tickets: '))

#Create function to generate tickets
def generate_ticket():
    ticket = []
    i=0
    while i < 6:
        x = randint(1,99)
        ticket.append(x)
        i=i+1
    return ticket

#Generate the winning ticket from the function and print
winning_ticket = generate_ticket()
print(f'Winning ticket: {winning_ticket}')

#Create the logic to loop through and generate player tickets
total_winnings = 0
winnings = 0
i=0
while i < tickets:
    player_ticket = generate_ticket()
    #print(f'Player ticket: {player_ticket}')
    i=i+1
    index = 0
    #Evaluate player tickets to determine winnings
    match = 0
    while index < len(player_ticket):
        if player_ticket[index] == winning_ticket[index]:
            match += 1
        index = index + 1
    #winnings = 0
    if match == 6:
        winnings += 25000000
    elif match == 5:
        winnings += 1000000
    elif match == 4:
        winnings += 5000
    elif match == 3:
        winnings += 100
    elif match == 2:
        winnings += 7
    elif match == 1:
        winnings += 4
#Track total winnings for the loop
#total_winnings = total_winnings + winnings
#Build in ticket cost
cost = tickets * 2
#Determine final balance
balance = winnings - cost
#Calculate return on investment
roi = (winnings-cost)/cost
#Print the balance and roi
print(f'${balance}')
print(f'${winnings}')
print(roi)
