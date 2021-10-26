"""python  """
class ATM:
    balance = 0
    def __repr__(self): # stands for the representation of the class 'atm'
        return self.balance

    def check_balance(self):    # self refers to the class this method belongs to.
        return self.balance
    
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def check_withdrawal(self, amount): # I'm getting 
        if amount > self.balance:
            return False
        else:
            return True

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def calc_interest(self):
        return self.balance * .001



atm = ATM() # create an instance of our class


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
            
        success = atm.withdraw(amount)
            
        if not success:
            print('Insufficient funds')
        else:
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