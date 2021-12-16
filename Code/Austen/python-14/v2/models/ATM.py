from datetime import datetime


class ATM:
    #* balance and interest rate will default to a balance of 0 and an interest rate of 0.1%
    def __init__(atm):
      atm.balance = 0
      atm.interest = 0.001
      atm.query = '\nWhat would you like to do?\n'
      atm.options = [{'id': 1, 'name': 'check balance'}, {'id': 2, 'name': 'deposit'},
                     {'id': 3, 'name': 'withdraw'}, {'id': 4, 'name': 'calculate interest'}, {'id': 5, 'name': 'quit'}]
    #* `check_balance()` returns the account balance

    def stamper(atm):
      now = datetime.now()
      date = now.date()
      time = now.time()
      stamp = f'{date} - {time.hour}:{time.minute}'
      return stamp

    def print_balance(atm):
      stamp = atm.stamper()
      balance = f'{stamp} - Balance available: ${atm.balance}'
      return balance
    #* `deposit(amount)` deposits the given amount in the account

    def deposit(atm):
      stamp = atm.stamper()
      deposit = int(input('amount to deposit: $'))
      atm.balance += deposit
      deposit = f'{stamp} - Deposited ${deposit}.'
    #* `check_withdrawal(amount)` returns true if the withdrawn amount won't put the account in the negative `withdraw(amount)` withdraws the amount from the account and returns it

    def withdraw(atm):
      withrawl = int(input('amount to withdraw: $'))
      if atm.balance >= withrawl:
        atm.balance -= withrawl
        successful = True
      else:
        successful = False
      return successful
    #*  `calc_interest()` returns the amount of interest calculated on the account

    def interest_calculator(atm):
      rate = atm.interest
      time = int(input('Years to calculate: '))
      interest = atm.balance * rate * time
      interest = round(interest, 2)
      balance = round(atm.balance + interest, 2)
      interest = f'After {time} years, with a starting balance of ${atm.balance} and an interest rate of {rate*100}% the interest acquired would be ${interest}. Your new account balance would be ${balance}.'
      return interest
