class atm:
    def __init__(self, balance = 0, interest = 0.1, history = []):
        self.balance = balance
        self.interest = interest
        self.history = history
    def check_balance(self):
        return self.balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
    def calc_interest(self):
        amount = self.interest
        self.interest = 0
        return amount
    def trans_history(self, transtype, amount):
        transaction = []
        receipt = (f"You {transtype}${amount} Updated balance: {self.balance}")
        transaction.append(receipt)
        self.history = self.history + transaction
        return self.history
    def print_history(self):
        print(self.history)
        return
        


atm = atm() # create an instance of our class
print('Welcome to the ATM')

menu_options = {
    '1': 'Balance',
    '2': 'Deposit',
    '3': 'Withdraw',
    '4': 'Interest',
    '5': 'History',
    '6': 'Exit'
}

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
        atm.trans_history("deposited: ", amount)
        if not success:
            print("Deposit amount must be a positive number.")
        else:
            print(f'Deposited ${amount}')

    elif command == 'Withdraw':
        amount = float(input('How much would you like to withdraw?\n> $'))
        success = atm.withdraw(amount)
        atm.trans_history("withdrew: ", amount)
        if not success:
            print('Insufficient funds')
        else:
            atm.withdraw(amount)
            print(f'Withdrew ${amount}')

    elif command == 'Interest':
        amount = atm.calc_interest() # call the calc_interest() method
        atm.deposit(amount)
        atm.trans_history("gained from interest: ", amount)
        print(f'Accumulated ${amount} in interest')
    
    elif command == 'History':
        atm.print_history()

    elif command == 'Exit':
        print("Goodbye!")
        break

    else:
        print('Command not recognized')