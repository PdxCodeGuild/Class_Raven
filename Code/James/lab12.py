"""python  """
class ATM:
    balance = 0
<<<<<<< HEAD
    transaction_list = []
    
=======
>>>>>>> e4c274c31aef799921e6dfd2717e820861eb5a6c
    def __repr__(self): # '_repr_ stands for the representation of the class 'atm'
        return self.balance

    def check_balance(self):    # self refers to the class this method belongs to.
        return round(self.balance, 2) # got rid of big balance decimal with the round function
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount # returned a bool to define success.
<<<<<<< HEAD
            self.transaction_list.append(amount)
=======
>>>>>>> e4c274c31aef799921e6dfd2717e820861eb5a6c
            return True
        else:
            return False
    
    def check_withdrawal(self, amount): # If amount is greater than balance return false
        if amount > self.balance: 
            return False
        elif amount <= self.balance:
            return True

    def withdraw(self, amount):
        if ATM.check_withdrawal(self, amount): #calling check_withdrawal method to check if withdraw amount is valid
            self.balance -= amount
<<<<<<< HEAD
            self.transaction_list.append(amount)
=======
>>>>>>> e4c274c31aef799921e6dfd2717e820861eb5a6c
            return True
        else:
            return False
        

    def calc_interest(self):
        return self.balance * .001

<<<<<<< HEAD
    def print_transactions(self):
        """   print the transactions """
        print(self.transaction_list)
=======
    # def print_transactions(self):
    #      everytime User deposits or withdraws add a string to a list 
    #     if atm.withdraw(self, amount)
>>>>>>> e4c274c31aef799921e6dfd2717e820861eb5a6c



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
            
        success = atm.withdraw(amount) #changed withdraw method to return a bool so conditioanl statements work
           
        if not success:
            print('Insufficient funds')
        else:
                print(f'Withdrew ${amount}')
<<<<<<< HEAD
                print(atm.transaction_list)
=======
>>>>>>> e4c274c31aef799921e6dfd2717e820861eb5a6c
        
    elif command == 'Interest':
        amount = atm.calc_interest() # call the calc_interest() method
        atm.deposit(amount)
        print(f'Accumulated ${amount} in interest')

    elif command == 'Exit':
        print("Goodbye!")
        break
        
    else:
        print('Command not recognized')