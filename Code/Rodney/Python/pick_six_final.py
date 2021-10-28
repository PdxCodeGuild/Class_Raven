
import random ## import to generate random numbers
from string import ascii_letters  ## import to create a list to check if user entering letter, not number
ascii_letters = list(ascii_letters) ## list of those letters

def number_or_not(how_many_tickets, ascii_letters):
    ## this function will compare list of user entry to ascii letters to check if user entering letter
    for i in how_many_tickets:
       if i in ascii_letters:
            return True  ## if user entry anywhere in ascii letters, returns True 
    return False

def total_return(number_of_tickets, total_won):
    ## this function will calculate toal ROI
    cost_of_tickets = -number_of_tickets * 2 ## cost of tickets user entered * $2 per ticket
    earnings = cost_of_tickets + total_won ## removing total won from total cost of tickets
    roi = earnings/abs(cost_of_tickets) ## total roi is total earnings/cost of tickets 
    return roi*100 ## function returns roi * 100 for percentage 

def winnings_decider(number_of_matches):
## this function is de-cluttering lottery machine function and looks at number in number_of_matches list to determine amount won for that ticket 
    winnings = [i*0 if i == 0 else i*4 if i == 1 else i/i*7 if i == 2 else i/i*100 if i == 3 else i/i*50000 if i == 4 else i/i*1000000 if i == 5 else 25000000 for i in number_of_matches]          
    winnings = ''.join([str(integer) for integer in winnings]) ## ^^ using list comprehension to avoid multiple lines of code
    #winnings = float(winnings) ## amount of winnings is turned into string then float, then int
    winnings = int(winnings)
    return winnings ## function returns winnings for that ticket 
    
def lottery_machine(number_of_tickets):
    ## this function takes in user entered number of tickets as argument, generates winning ticket, user tickets, calculates total winnings based on winnings for each ticket 
    matches = []  ## creating empty matches list, 0 balance, default 0 in number of matches, and empty winning numbe rlist 
    total_winnings = 0
    number_of_matches = [0]
    winning_numbers_list = []
    winning_ticket_list = [random.randint(1,99) for x in range(6)] ## generates list of six random numbers
    for x in range(number_of_tickets):  # repeates based on number of tickets user bought 
        user_ticket_list = [random.randint(1,99) for x in range(6)] ## generates new number each iteration for user ticket
        for x in range(6): ## for each number in user/winning ticket list:
            user_number = user_ticket_list[x] ## assigning value based on index position of each list 
            winning_number = winning_ticket_list[x]
            if user_number == winning_number: ## if those values match, we add to winning number list 
                winning_numbers_list.append(user_number)
                matches = len(winning_numbers_list) ## the number of matches = length of winning number list (based on number of numbers in winning number list)
                number_of_matches[0] = matches #number of matches list at index 0 (it's only index) will now equal number of matches for that ticket 
            else:
                continue       
        winnings = winnings_decider(number_of_matches) ## send number of matches as argument to winnings decicer to determine amount won for that ticket 
        total_winnings += winnings ## winning decider tells us what total winnings is for that ticket and we add to balance of total winnings 
        number_of_matches = [0] ## reverting number of winning numbers/matches/winning_numbers_list back to original value prior to main loop repeating 
        winning_numbers_list = [] 
    return total_winnings  ## function returns total winnings for the tickets user purchased 

how_many_tickets = input('How many tickets would you like to buy?\n>')  ##input function to ask user how many tickets they want to buy 
how_many_tickets = list(how_many_tickets)  ## turning user answer into list to send to number_or_not function as argument 
while number_or_not(how_many_tickets, ascii_letters) == True:  ## if user entered != number, function will return True, user asked to enter number 
    how_many_tickets = input("Please enter a number :)\n> ")
how_many_tickets = ''.join(how_many_tickets) ## turning list back to string
how_many_tickets = int(how_many_tickets)  ## number of tickets converted to integer prior being sent to lotter_machine as argument 
total_winnings = lottery_machine(how_many_tickets)
return_on_investment = total_return(how_many_tickets, total_winnings) ## user entered number of tickets and return from lottery machine sent to function to determine roi 

print(f'You spent: ${how_many_tickets * 2}')
print(f'The total amount of your winnings is: ${total_winnings}')
print(f'The return on your investment is: {round(return_on_investment)}%')


