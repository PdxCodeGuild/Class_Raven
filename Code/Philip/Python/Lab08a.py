from random import randint
tickets = int(input('Enter the number of tickets: '))
ticket = []
def generate_ticket():
    ticket = []
    i=0
    while i < 6:
        x = randint(1,99)
        ticket.append(x)
        i=i+1
    return ticket


winning_ticket = generate_ticket()
winnings = 0
t = 0
while t < tickets:
    winnings = 0
    matched = 0
    t = t + 1
    lucky_ticket = generate_ticket()
    for z in range(6):
        if lucky_ticket[z] == winning_ticket[z]:
            matched = matched + 1
    if matched == 1:
        winnings = winnings + 4
    elif matched == 2:
        winnings = winnings + 7
    elif matched == 3:
        winnings = winnings + 100
    elif matched == 4:
        winnings = winnings + 5000
    elif matched == 5:
        winnings = winnings + 1000000
    elif matched == 6:
        winnings = winnings + 25000000
roi = float((winnings - (tickets * 2))/(tickets * 2))
print(winnings)
print (roi)







def evaluate_ticket(seqeunce):
    winnings = 0
    for x in sequence:
        match = 0
        if sequence[0] == winning_ticket[0]:
            match = match + 1
        elif sequence[1] == winning_ticket[1]:
            match = match + 1
        elif sequence[2] == winning_ticket[2]:
            match = match + 1
        elif sequence[3] == winning_ticket[3]:
            match = match + 1
        elif sequence[4] == winning_ticket[4]:
            match = match + 1
    if match == 1:
        winnings = 4
    elif match == 2:
        winnings == 7
    elif match == 3:
        winnings == 100
    elif match == 4:
        winnings == 5000
    elif match == 5:
        winnings == 1000000
    elif match == 6:
        winnings == 25000000
    return winnings


i = 0
cost = 0
while i < tickets:
    cost = cost - 2
    sequence = generate_ticket()
    balance = evaluate_ticket(sequence)
    i = i + 1
print(balance)


'''def generate_ticket():
    ticket = []
    i=0
    z=0
    while i < 6:
        x = randint(1,99)
        ticket.append(x)
        i = i + 1
        match = 0
        if ticket[0] == winning_ticket[0]:
            match = match + 1
        elif ticket[1] == winning_ticket[1]:
            match = match + 1
        elif ticket[2] == winning_ticket[2]:
            match = match + 1
        elif ticket[3] == winning_ticket[3]:
            match = match + 1
        elif ticket[4] == winning_ticket[4]:
            match = match + 1




i = 1
y = 0
balance = 0
while i < tickets:
    y = generate_ticket()
    balance = balance + y
    i = i + 1
cost = tickets * 2
total = balance - cost
print(total)'''

