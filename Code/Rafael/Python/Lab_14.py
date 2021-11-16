# Lab_14 ATM
# Rafael Medina



# created an instance of our class ATM

class ATM:
# This is known as the constructor or initializer.
    def __init__(self, balance = 0, interest = 0.1):
# should these be made private? ex __XX = xx
        self.balance = balance
        self.interest = interest
# calling the deposit(amount) method
    def deposit(self, amount):
        self.balance += amount
# calling the withdraw(amount) method     
    def withdraw(self, amount):
        self.balance -= amount
# calling the check_balance() method
    def check_balance(self):
        return self.balance
# calling the calc_interest() method
    def calc_interest(self):
        return self.interest * self.balance
# note it is important to have the initializers and variables match the command       

print('Welcome to the ATM')

menu_options = {
        '1': 'Balance',
        '2': 'Deposit',
        '3': 'Withdraw',
        '4': 'Interest',
        '5': 'Exit'
    }
# atm called by the ATM class above
atm = ATM()
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
            
            success = atm.withdraw(amount)
            
            if not success:
                 print(f'Withdrew ${amount}')
                #print('Insufficient funds')
            else:
                #print('Insufficient funds')
                print(f'Withdrew ${amount}')
                # Note I was getting insuficient funds print even though there were more than ample funds
                # < boolean < > not supported 'float' and 'Nonetype'
        
        elif command == 'Interest':
            amount = atm.calc_interest() # call the calc_interest() method
            atm.deposit(amount)
            print(f'Accumulated ${amount} in interest')

        elif command == 'Exit':
            print("Goodbye!")
            break
        
        else:
            print('Command not recognized')




