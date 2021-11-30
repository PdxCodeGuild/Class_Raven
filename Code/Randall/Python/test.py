#Just Test Things
import csv
from tabulate import tabulate

class ATM(): 

    def __init__(self, balance=0):        
        self.balance = balance
        self.history = []
        self.datetime = 'Today'
        self.history.append(f'Date: {self.datetime}. Account opened with starting balance of ${self.balance}.')

    def check_balance(self):
        print(f'Balance is ${self.balance}.')
        return self.balance
        
    def deposit(self,amount):

        if amount <= 0:
            print(f'Invalid entry. Please use the withdrawl function to make a withdrawl. Balance is ${self.balance}.')
            return self.balance
        elif amount >0:
            self.balance += amount
            print(f'${amount} deposited. You new balance is ${self.balance}.')
            self.history.append(f'Date: {self.datetime}. Deposit: ${amount}. Balance is ${self.balance}.')
        else:
            print(f'Invalid input. Balance is ${self.balance}.')
        return self.balance

    def print_transactions(self):
        print('Beginning transaction history...')
        print(self.history)
        print('...end of transaction history.')
    
    def check_withdrawal(self, amount):
        if self.balance > amount and amount > 0:
            return True
        else:
            return False
        print('invalid!')

    def withdraw(self,amount):

        self.check_withdrawal(amount)

        if self.check_withdrawal(amount) == True:
            self.balance -= amount
            print(f'${amount} withdrawn. You new balance is ${self.balance}.')
            self.history.append(f'Date: {self.datetime}. Withdrawl: ${amount}. Balance is ${self.balance}.')
            return self.balance
        else:
            self.history.append(f'Date: {self.datetime}. REJECTED Withdrawl for amount: ${amount}. Balance is ${self.balance}.')
            print(f'Sorry! Current balance is ${self.balance}; but you tried to withdraw ${amount}.')
            return self.balance

atm = ATM() # create an instance of our class
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


update = int(input("Which row would you like to change? Enter 1 - " + str(len(file_content)) + " :"))
print("Please enter the new details for each of the following :")

for i in range(len(file_content[0])):
    updated_data = input("Enter new details for " + str(file_content[0][i]) + " :")
    file_content[update][i] = updated_data

print(("Please see new file below: "))
for i in range(len(file_content)):
    print("Row " + str(i) + " :" + str(file_content[i]))

changeCSV = input("Would you like to update the key roster? Y/N: ").lower()
if changeCSV == ("y"):
    with open("keys_doc.csv", "w+") as file:
        key_file = csv.writer(file)
        for i in range(len(file_content)):
            key_file.writerow(file_content[i])
