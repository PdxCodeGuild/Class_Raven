
"""
Lee Colburn
Evening Bootcamp - PDX Code Guild
Lab 14 - ATM
"""
'''
Let's represent an ATM with a class containing two attributes: a balance and an interest rate. 
A newly created account will default to a balance of 0 and an interest rate of 0.1%. 


check_balance() returns the account balance
deposit(amount) deposits the given amount in the account
check_withdrawal(amount) returns true if the withdrawn amount won't put the account in the negative
withdraw(amount) withdraws the amount from the account and returns it
calc_interest() returns the amount of interest calculated on the account


Version 2
Have the ATM maintain a list of transactions. 
Every time the user makes a deposit or withdrawal, add a string to a list saying 'user deposited $15' or 'user withdrew $15'.
 Add a new method print_transactions() to your class for printing out the list of transactions.'''

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
        if amount <= self.balance:
            return True 
        else:
            return False
    
    def withdraw(self, amount):
        self.balance = self.balance - amount
        return self.balance
    
    def add_trans(self, trans_type, amount):        
        note = []
        message = str(f"User {trans_type} ${amount}")
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

menu_options = {
'1': 'Balance',
'2': 'Deposit',
'3': 'Withdraw',
'4': 'Interest',
'5': 'Exit'
}


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
        print('1  - get the current balance')
        print('2  - deposit money')
        print('3 - withdraw money')
        print('4 - accumulate interest')
        print('4     - exit the program')

    elif command == '5':
        break

    elif command == '0':
        atm.print_transactions()
    
    else:
        print('Command not recognized')