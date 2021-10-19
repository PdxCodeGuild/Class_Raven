# Lab_08 Pick 6



import random 

lottery_ticket = []

def pick6(): # pick6() function
    numbers  = random.sample(range(1, 10), 6) #(range(1, 99), 6)
    return numbers


winning_ticket = pick6() # pick6() function

dollars = 0
tickets = 0



while tickets < 10:
  
    dollars -= 2 # Cost of the ticket
    tickets += 1
    #lottery_ticket = pick6()
    
    for i in range(1):
        lottery_ticket = random.sample(range(1, 10), 6) #(range(1, 99), 6)
        
    # if x wins you win $x
    if lottery_ticket == 6:
        dollars += 25000000

    if lottery_ticket == 5:
        dollars += 1000000

    if lottery_ticket == 4:
        dollars += 50000
    
    if lottery_ticket == 3:
        dollars += 100

    if lottery_ticket == 2: 
        dollars += 7

    if lottery_ticket == 1:
        dollars += 4
    
    if lottery_ticket == 0:
        dollars += 0

        
    
    winnings = tickets * 2 + dollars
    
    print(f'\nThe winning numbers are: {lottery_ticket}')
    print(f'\nYou bought {tickets} tickets, for ${float(dollars)} dollars, you won ${float(winnings)} dollars\n\n' )
    
    
    
   
        

  


    