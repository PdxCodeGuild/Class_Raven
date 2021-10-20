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
i=0
while i < tickets:
    player_ticket = generate_ticket()
    #print(f'Player ticket: {player_ticket}')
    i=i+1
    #Evaluate player tickets to determine winnings
    winnings = 0
    if player_ticket[:6] == winning_ticket[:6]:
        winnings = 25000000
    elif player_ticket[:5] == winning_ticket[:5]:
        winnings = 1000000
    elif player_ticket[:4] == winning_ticket[:4]:
        winnings = 5000
    elif player_ticket[:3] == winning_ticket[:3]:
        winnings = 100
    elif player_ticket[:2] == winning_ticket[:2]:
        winnings = 7
    elif player_ticket[:1]== winning_ticket[:1]:
        winnings = 4
    #Track total winnings for the loop
    total_winnings = total_winnings + winnings
#Build in ticket cost
cost = tickets * 2
#Determine final balance
balance = total_winnings - cost
#Calculate return on investment
roi = (total_winnings-cost)/cost
#Print the balance and roi
print(balance)
print(roi)
