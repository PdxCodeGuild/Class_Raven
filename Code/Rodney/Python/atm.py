
deposits = []  #empty lists to hold deposits, withdrawl transactions 
withdrawls = []

class Atm: 
    def __init__(self, balance = 0, interest_rate = 0.001): ## initializing class, naming attributes of our class: self, balance, interest rate 
        self.balance = balance  ## this is 'blueprint', if new instance is created...becomes 'that instance'. balance = balance, etc 
        self.interest_rate = interest_rate

    def check_balance(self):  #balance is default value of 0, so returning 0 since user starts at 0 balance 
        return self.balance

    def deposit(self, amount):  ## parameters are self(always) and amount
        deposits.append(amount)  # add deposits to deposit list
        self.balance = self.balance + amount ## balance for instances will be starting balance of 0 plus any amounts added 
        return self.balance # returning balance 

    def check_withdrawal(self, amount):
        if amount <= self.balance:  ## if user doesn't try to withdraw more than balance, this function returns True
            return True

    def withdraw(self, amount):
        withdrawls.append(amount)#add withdrawls to deposit list
        self.balance = self.balance - amount  # subtracting withdrawls from balance 
        return self.balance

    def calc_interest(self):  # only parameter is self since interest rate is default value
        return self.balance * self.interest_rate # calculating interest 

atm = Atm()  ## creating new instance of atm 

print("Welcome to the ATM - Let's talk money!")

while True: 

    command = input('''
Please enter a command from the following options:
balance  - get the current balance
deposit  - deposit money
withdraw - withdraw money
interest - calculate interest
transactions - list of deposits and withdrawls 
exit - exit ATM interface:\n> ''').lower()

    if command == 'balance':
            balance = atm.check_balance() ## calling check balance function (atm is now 'self' is how I understand it) to return balance and assigning result to balance variable 
            print(f'Your balance is ${balance}')

    elif command == 'deposit':
        amount = float(input("How much do you want to deposit?\n> "))
        print(f'You deposited: ${amount}')
        new_balance = atm.deposit(amount) ## calling deposit function to return balance after added to current balance and assigning to variable 
        print(f'Your new balance is ${new_balance}')

    elif command == 'withdraw':
        amount = float(input('How much would you like to withdraw?\n> '))
        if atm.check_withdrawal(amount): ## calling withdrawal function to return balance after withdrawal subtracted from current balance and assigning to variable 
            print(f'You withdrew ${amount}')
            new_balance = atm.withdraw(amount)
            print(f'Your new balance is ${new_balance}')
        else:  ## if function doesn't return True: else statement 
            print('Insufficient funds')

    elif command == 'interest':
        amount = atm.calc_interest()  ## no argument to pass since interest is default for this class attribute 
        print(f'Accumulated interest: ${amount}')

    elif command == 'transactions':

        string_deposits = []  ##adding string values of deposits/transactions
        string_withdrawls = []

        for number in deposits:
            number = str(number)  ## turning each float into string and adding to empty string/deposits list 
            string_deposits.append(number)
        deposits = "\n".join(string_deposits)

        for number in withdrawls:
            number = str(number)
            string_withdrawls.append(number)
        withdrawls = "\n".join(string_withdrawls)  ##joining string, separated by a line 

        print(f'Deposits in $: \n{deposits}')
        print(f'Withdrawls in $: \n{withdrawls}')

    elif command == 'help':
            print('Available commands:')
            print('balance  - get the current balance')
            print('deposit  - deposit money')
            print('withdraw - withdraw money')
            print('interest - accumulate interest')
            print('transactions - list of deposits and withdrawls')
            print('exit - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')

