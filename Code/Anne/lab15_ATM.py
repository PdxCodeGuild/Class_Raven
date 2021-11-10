# Let's represent an ATM with a class containing two attributes: a balance and an interest rate. 


class ATM:
    def __init__(self, balance = 0 , interest_rate = 0.001): #listed as a decimal instead of a percent
        self.balance = balance
        self.interest_rate = interest_rate

        # returns the account balance
    def check_balance(self):
        return self.balance
        
        # deposits the given amount in the account
    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
        else:
            return False
        
        # withdraws the amount from the account and returns it
    def withdraw(self, amount):
        if amount < self.balance:
            self.balance = self.balance - amount
        else:
            print("your balance is too low for this withdrawl")
        
        # returns true if the withdrawn amount won't put the account in the negative
    def check_withdrawal(self, amount):
        if amount < self.balance:
            return True
        
        return False

        # returns the amount of interest calculated on the account
    def calc_interest(self):
        interest = self.balance * self.interest_rate
        interest = float(interest)
        return interest

# Lab 15 - The ATM currently allows negative amounts to be deposited and 
# withdrawals to be more than the available balance. 
        
atm = ATM() # create an instance of our class
print('Welcome to the ATM')

menu_options = {
    '1': 'Balance',
    '2': 'Deposit',
    '3': 'Withdraw',
    '4': 'Interest',
    '5': 'Exit'
}
amount = 0
while True:
    print()
    for label, option in menu_options.items():
        print(f'{label}. {option}')
    
    command = input('\nEnter the number of the option you would like to perform\n> ')
    command = menu_options.get(command)

    if command == 'Balance':
        balance = atm.check_balance() # call the check_balance() method
        print(f'Your balance is ${balance}')
    
    elif command == 'Deposit':
        amount = float(input('How much would you like to deposit? '))
        success = atm.deposit(amount) # call the deposit(amount) method
        if success == False:
            print("Deposit amount must be a positive number.") #this doesn't work. It deposits the amount and still prints this.
        else: 
            print(f'Deposited ${amount}')
    
    elif command == 'Withdraw':
        amount = float(input('How much would you like to withdraw?\n> $'))
        
        success = atm.withdraw(amount)
        
        if success == False:
            print('Insufficient funds')
        else:
            print(f'Withdrew ${amount}')

    elif command == 'Interest':
        amount = atm.calc_interest() # call the calc_interest() method
        atm.deposit(amount)   #Why is this here?
        print(f'Accumulated ${amount} in interest')

    elif command == 'Exit':
        print("Goodbye!")
        break
    
    else:
        print('Command not recognized')
