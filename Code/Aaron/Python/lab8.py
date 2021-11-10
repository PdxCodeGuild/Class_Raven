# lottery numbers
# demonstrates random number generation

# generate random number 1-6
import random

winning_ticket  = random.sample(range(1,  99),  6)



#still having issues with this working on it though. 
balance = 0

counter = 0

while counter < 100000:

    counter = counter + 1
    ticket  = random.sample(range(1,  99),  6)
    balance = balance - 2
    if winning_ticket == ticket:
        balance = balance + 25000000

    elif winning_ticket[:5] == ticket[:5]:
        balance = balance + 1000000

    elif winning_ticket[:4] == ticket[:4]:
        balance = balance + 50000

    elif winning_ticket[:3] == ticket[:3]:
        balance = balance + 100

    elif winning_ticket[:2] == ticket[:2]:
        balance = balance + 7

    elif winning_ticket[:1] == ticket[:1]:
        balance = balance + 4
        continue

print("Your Numbers are ", ticket)
print("Winning Ticket numbers ", winning_ticket)
input("/n/nPress the enter key to exit.")
