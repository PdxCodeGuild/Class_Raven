

#from _typeshed import Self


class ATM:
    def __init__ (self, balance = 0, interest_rate = 0.6, transaction_log = []):
        self.balance = balance
        self.interest_rate = interest_rate
        self.transaction_log = transaction_log

    def check_balance(self):
        return print(f"Your balance is {self.balance}")

    def deposit(self, amount):
    #    self.amount = amount
        self.balance += amount
        #self.transaction_log = transaction_log
        #transaction_log.append(f"user deposited ${amount}\n")
        return self.balance

    def check_withdrawal(self, amount):
        if self.balance - amount <= 0:
            return False
        else:
            return True

    def withdraw (self, amount):
        self.balance = self.balance - amount
        #self.transaction_log = transaction_log
        #transaction_log.append(f"user withdrew ${amount}\n") 
        return self.balance - amount

    def calc_interest (self):
        self.balance += (self.balance * self.interest_rate)
        return self.balance

    def log_event(self, transaction_log, message):
        self.transaction_log = transaction_log
        transaction_log.append(message) 

    def print_log(self, transaction_log):
        return print(transaction_log)

# atm = ATM(1000, 0.6) # code for testing functions
# atm.check_balance()
# atm.deposit(100)
# atm.check_balance()
# print(atm.check_withdrawal(1200))
# atm.check_balance()
# atm.calc_interest()
# atm.check_balance()



atm = ATM(1000, 0.6) # create an instance of our class
#print(atm.balance)

print('Welcome to the ATM')
while True:
    command = input('Enter a command: ')
    if command == 'balance':
        balance = atm.check_balance() # call the check_balance() method
        #print(f'Your balance is ${balance}')
    elif command == 'deposit':
        amount = float(input('How much would you like to deposit? '))
        atm.deposit(amount) # call the deposit(amount) method
        print(f'Deposited ${amount}')
    elif command == 'withdraw':
        amount = float(input('How much would you like '))
        if atm.check_withdrawal(amount): # call the check_withdrawal(amount) method
            atm.withdraw(amount) # call the withdraw(amount) method
            atm.log_event(f"user withdrew ${amount}\n")
            print(f'Withdrew ${amount}')
        else:
            print('Insufficient funds')
    elif command == 'interest':
        amount = atm.calc_interest() # call the calc_interest() method
        atm.deposit(amount)
        print(f'Accumulated ${amount} in interest')
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