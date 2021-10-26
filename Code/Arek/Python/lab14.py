"""
Lab 12: ATM

Let's represent an ATM with a class containing two attributes: a balance and an interest rate. 
A newly created account will default to a balance of 0 and an interest rate of 0.1%. Implement the initializer, as well as the following functions:

    check_balance() returns the account balance
    deposit(amount) deposits the given amount in the account
    check_withdrawal(amount) returns true if the withdrawn amount won't put the account in the negative
    withdraw(amount) withdraws the amount from the account and returns it
    calc_interest() returns the amount of interest calculated on the account
---------------------------------------------------------------------------------------------------------------
Version 2 (not optional)

Have the ATM maintain a list of transactions. 
Every time the user makes a deposit or withdrawal, add a string to a list saying 'user deposited $15' or 'user withdrew $15'. 
Add a new method print_transactions() to your class for printing out the list of transactions.


"""




class ATM:
    def __init__(self, balance=0, interest_rate=0.1):
        self.balance = balance
        self.interest_rate = interest_rate

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount

    def check_withdrawal(self, amount):
        if self.balance - amount < 0:
            return False
        else:
            return True

    def withdraw(self, amount):
        self.balance -= amount

    def calc_interest(self):
        return self.interest_rate * self.balance
    # adding this for version 2
    def print_transactions(self,transactions):
        return transactions
        

atm = ATM() # create an instance of our class
print('Welcome to the ATM')
transactions = [] # added for version 2 
while True:
    command = input('Enter a command: ')
    if command == 'balance':
        balance = atm.check_balance() # call the check_balance() method
        print(f'Your balance is ${balance}')
    elif command == 'deposit':
        amount = float(input('How much would you like to deposit? '))
        atm.deposit(amount) # call the deposit(amount) method
        print(f'Deposited ${amount}')
        transactions.append(f"Deposited ${amount}") # adding the string to the transactions list for version 2
    elif command == 'withdraw':
        amount = float(input('How much would you like '))
        if atm.check_withdrawal(amount): # call the check_withdrawal(amount) method
            atm.withdraw(amount) # call the withdraw(amount) method
            print(f'Withdrew ${amount}')
            transactions.append(f"Withdrew ${amount}") # adding the string to the transactions list for version 2
        else:
            print('Insufficient funds')
    elif command == 'interest':
        amount = atm.calc_interest() # call the calc_interest() method
        atm.deposit(amount)
        print(f'Accumulated ${amount} in interest')
    elif command == 'print': # this is adding the new command to call the print_transactions method for version 2
        print(atm.print_transactions(transactions))
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('exit     - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')

