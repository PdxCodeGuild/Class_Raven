'''ATM Lab14
By Philip Bartoo
10/25/21
Updated 1/16/22
'''

class ATM:
    def __init__(self, balance, interest):
        self.balance = balance
        self.interest = interest
    
    def check_balance(self):
        return self.balance
    
    def deposit(self, amount):
        if amount < 0:
            return print("Not Allowed")
        else:
            self.balance += amount
            return self.balance
    
    def check_withdrawal(self, amount):
        if self.balance - amount > 0:
            return True
        else:
            return False

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance
    
    def calc_interest(self):
        interest = self.balance * .01
        return float(interest)

atm = ATM(1000, 0.01) 
print('Welcome to the ATM')

menu_options = {
    '1': 'Balance',
    '2': 'Deposit',
    '3': 'Withdraw',
    '4': 'Interest',
    '5': 'Exit'
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
        if not success:
            print("Deposit amount must be a positive number.")
        else:
            print(f'Deposited ${amount}')

    elif command == 'Withdraw':
        amount = float(input('How much would you like to withdraw?\n> $'))
        success = atm.check_withdrawal(amount)

        if not success:
            print('Insufficient funds')
        else:
            atm.withdraw(amount)
            print(f'Withdrew ${amount}')

    elif command == 'Interest':
        amount = atm.calc_interest() # call the calc_interest() method
        atm.deposit(amount)
        print(f'Accumulated ${amount} in interest')

    elif command == 'Exit':
        print("Goodbye!")
        break

    else:
        print('Command not recognized')