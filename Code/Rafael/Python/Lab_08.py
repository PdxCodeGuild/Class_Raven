# Lab_08 Pick 6



import random 

lottery_ticket = []

def pick6(): # pick6() function
    numbers  = random.sample(range(1, 99), 6) #(range(1, 99), 6)
    return numbers


winning_ticket = pick6() # pick6() function

dollars = 0
tickets = 0



while tickets < 100000:
  
    dollars -= 2 # Cost of the ticket
    tickets += 1
    #lottery_ticket = pick6()
    
    for i in range(1):
        lottery_ticket = random.sample(range(1, 99), 6) #(range(1, 99), 6)
        

     #   dollars += 25000000
    if winning_ticket[0] and [1] and [2] and [3] and [4] and [5] == lottery_ticket [0] and [1] and [2] and [3] and [4] and [5]: 
        dollars += 25000000
     #   dollars += 1000000
    if winning_ticket[0] and [1] and [2] and [3] and [5] == lottery_ticket [0] and [1] and [2] and [3] and [5]: 
        dollars += 1000000
    if winning_ticket[1] and [2] and [3] and [4] and [5] == lottery_ticket [1] and [2] and [3] and [4] and [5]: 
        dollars += 1000000
    if winning_ticket[0] and [1] and [2] and [3] and [4] == lottery_ticket [0] and [1] and [2] and [3] and [4]: 
        dollars += 1000000
   #     dollars += 50000
    if winning_ticket[1] and [3] and [4] and [5] == lottery_ticket [1] and [3] and [4] and [5]: 
        dollars += 50000
    if winning_ticket[1] and [2] and [3] and [5] == lottery_ticket [1] and [2] and [3] and [5]: 
        dollars += 50000
    if winning_ticket[1] and [2] and [3] and [4] == lottery_ticket [1] and [2] and [3] and [4]: 
        dollars += 50000
    if winning_ticket[0] and [3] and [4] and [5] == lottery_ticket [0] and [3] and [4] and [5]: 
        dollars += 50000
    if winning_ticket[0] and [2] and [3] and [4] == lottery_ticket [0] and [2] and [3] and [4]: 
        dollars += 50000
    if winning_ticket[0] and [1] and [2] and [3] == lottery_ticket [0] and [1] and [2] and [3]: 
        dollars += 50000
#    100 dollars
    if winning_ticket[2] and [0] and [4] == lottery_ticket[2] and [0] and [4]: 
        dollars += 100
    if winning_ticket[2] and [0] and [3] == lottery_ticket[2] and [0] and [3]: 
        dollars += 100
    if winning_ticket[2] and [3] and [5] == lottery_ticket[2] and [3] and [5]: 
        dollars += 100
    if winning_ticket[1] and [5] and [3] == lottery_ticket[1] and [5] and [3]: 
        dollars += 100
    if winning_ticket[1] and [5] and [2] == lottery_ticket[1] and [5] and [2]: 
        dollars += 100
    if winning_ticket[1] and [4] and [3] == lottery_ticket[1] and [4] and [3]: 
        dollars += 100
    if winning_ticket[1] and [2] and [3] == lottery_ticket[1] and [2] and [3]: 
        dollars += 100
    if winning_ticket[1] and [0] and [4] == lottery_ticket[1] and [0] and [4]: 
        dollars += 100
    if winning_ticket[1] and [0] and [3] == lottery_ticket[1] and [0] and [3]: 
        dollars += 100
    if winning_ticket[1] and [0] and [2] == lottery_ticket[1] and [0] and [2]: 
        dollars += 100
    if winning_ticket[0] and [3] and [4] == lottery_ticket[0] and [3] and [4]: 
        dollars += 100
    if winning_ticket[0] and [4] and [2] == lottery_ticket[0] and [4] and [2]: 
        dollars += 100
    if winning_ticket[0] and [5] and [3] == lottery_ticket[0] and [5] and [3]: 
        dollars += 100
    if winning_ticket[0] and [4] and [3] == lottery_ticket[0] and [4] and [3]: 
        dollars += 100
    if winning_ticket[0] and [4] and [1] == lottery_ticket[0] and [4] and [1]: 
        dollars += 100
    if winning_ticket[0] and [5] and [2] == lottery_ticket[0] and [5] and [2]: 
        dollars += 100
    if winning_ticket[0] and [5] and [1] == lottery_ticket[0] and [5] and [1]: 
        dollars += 100
    if winning_ticket[0] and [4] and [5] == lottery_ticket[0] and [4] and [5]: 
        dollars += 100
    if winning_ticket[0] and [3] and [4] == lottery_ticket[0] and [3] and [4]: 
        dollars += 100
    if winning_ticket[0] and [2] and [3] == lottery_ticket[0] and [2] and [3]: 
        dollars += 100
    if winning_ticket[0] and [1] and [2] == lottery_ticket[0] and [1] and [2]: 
        dollars += 100
# 7 dollars  
    if winning_ticket[4] and [5] == lottery_ticket[4] and [5]: 
        dollars += 7
    if winning_ticket[3] and [5] == lottery_ticket[3] and [5]: 
        dollars += 7
    if winning_ticket[3] and [4] == lottery_ticket[3] and [4]: 
        dollars += 7
    if winning_ticket[2] and [5] == lottery_ticket[2] and [5]: 
        dollars += 7
    if winning_ticket[2] and [4] == lottery_ticket[2] and [4]: 
        dollars += 7
    if winning_ticket[2] and [3] == lottery_ticket[2] and [3]: 
        dollars += 7
    if winning_ticket[1] and [5] == lottery_ticket[1] and [5]: 
        dollars += 7
    if winning_ticket[1] and [4] == lottery_ticket[1] and [4]: 
        dollars += 7
    if winning_ticket[1] and [3] == lottery_ticket[1] and [3]: 
        dollars += 7
    if winning_ticket[1] and [2] == lottery_ticket[1] and [2]: 
        dollars += 7
    if winning_ticket[1] and [2] == lottery_ticket[1] and [2]: 
        dollars += 7
    if winning_ticket[0] and [5] == lottery_ticket[0] and [5]: 
        dollars += 7
    if winning_ticket[0] and [4] == lottery_ticket[0] and [4]: 
        dollars += 7
    if winning_ticket[0] and [3] == lottery_ticket[0] and [3]: 
        dollars += 7
    if winning_ticket[0] and [2] == lottery_ticket[0] and [2]: 
        dollars += 7
    if winning_ticket[0] and [1] == lottery_ticket[0] and [1]: 
        dollars += 7
# 4 dollars
    if winning_ticket[0] == lottery_ticket[0]:
        dollars += 4 
    if winning_ticket[1] == lottery_ticket[1]:
        dollars += 4
    if winning_ticket[2] == lottery_ticket[2]:
        dollars += 4
    if winning_ticket[3] == lottery_ticket[3]:
        dollars += 4
    if winning_ticket[4] == lottery_ticket[4]:
        dollars += 4
    if winning_ticket[5] == lottery_ticket[5]:
        dollars += 4  
  # 0 dollars 
    else: 
        winning_ticket == 0
        dollars += 0


winnings = tickets * 2 + dollars
roi = (winnings - tickets) / tickets


print(f'\nThe winning numbers are: {lottery_ticket}')
print(f'\nYou bought {tickets} tickets, for ${float(dollars)} dollars, you won ${float(winnings)} dollars\n' )
print(f'Your Return on Investment is: {roi}\n')
    


    
    
   
        

  


    