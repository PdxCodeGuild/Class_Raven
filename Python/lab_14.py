"""
Lee Colburn
Evening Bootcamp - PDX Code Guild
Lab 14 - ATM
"""

class ATM:
    def __init__(self, balance, interest, history) -> None: # self is always the first thing done when defining a class
        self.balance = balance
        self.interest = interest
        self.history = history

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def check_withdrawal(self, amount):
        return amount <= self.balance
    
    def withdraw(self, amount):
        self.balance = self.balance - amount
        return self.balance
    
    def add_trans(self, trans_type, amount):        
        note = []
        message = str(f"User {trans_type} ${amount:,.2f}. Updated balance of ${self.balance:,.2f}")
        note.append(message)
        self.history = self.history + note
        return 

    def calc_interest(self):
        amount = self.interest
        self.interest = 0 # this zeros the heretofore un-accumulated interest to prevent exploitation.
        return amount
    
    def print_transactions(self):
        print(self.history)
        return

atm = ATM(10_000, 14.992315, []) # create an instance of our class

print('Welcome to the ATM')

while True:

    command = input("Enter a command: \n'1': 'Balance' \n'2': 'Deposit' \n'3': 'Withdraw' \n'4': 'Interest' \n'0': Print a list of recent transactions \n'5': 'Exit' \n Choice: ")
    if command == '1':
        balance = atm.check_balance() # call the check_balance() method
        print(f'Your balance is ${balance:,.2f}\n')

    elif command == '2':
        amount = float(input('How much would you like to deposit? '))
        atm.deposit(amount) # call the deposit(amount) method
        ledger_add = atm.add_trans('Deposit of:',amount)
        print(f'Deposited ${amount:,.2f} \nUpdated balance: ${atm.balance:,.2f}\n')
        

    elif command == '3':
        amount = float(input('Enter the amount you would like to withdrawl: '))
        if atm.check_withdrawal(amount): # call the check_withdrawal(amount) method
            atm.withdraw(amount) # call the withdraw(amount) method
            ledger_add = atm.add_trans('Withdrew:',amount)
            print(f'Withdrew ${amount:,.2f} \nUpdated balance: ${atm.balance:,.2f}\n')
        else:
            print('Insufficient funds - Transaction not processed.\n')

    elif command == '4':
        amount = atm.calc_interest() # call the calc_interest() method and zeros the self.interest amount
        atm.deposit(amount) # deposits interest into current account balanc
        if amount > 0:
            ledger_add = atm.add_trans('Deposit of:',amount)
        print(f'Accumulated ${amount:,.2f} in interest. \nUpdated balance: ${atm.balance:,.2f} \n')

    elif command == 'help':
        print('Available commands:')
        print('1 - get the current balance')
        print('2 - deposit money')
        print('3 - withdraw money')
        print('4 - accumulate interest')
        print('5 - exit the program')
        
    elif command == '5':
        break

    elif command == '0':
        atm.print_transactions()
    
    else:
        print('Command not recognized')