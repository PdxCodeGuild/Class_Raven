from datetime import datetime
from models.ATM import ATM
#* represent an ATM with a class containing two attributes

account = ATM()
record = []
print(account.query)
for option in account.options:
  print('  ', option['id'], option['name'])
transaction = input('\n   enter the transaction (name or number): ').lower()
for option in account.options:
  if transaction == option['id']:
    transaction = option['name']
    break
while transaction != 'quit':
  if transaction == 'check balance':
    balance = account.print_balance()
    record.append(f'{transaction}, {balance}')
    print('\n    ', balance)
  elif transaction == 'deposit':
    account.deposit()
    balance = account.print_balance()
    record.append(f'{transaction}, {balance}')
    print('\n    ', balance)
  elif transaction == 'withdraw':
    successful = account.withdraw()
    stamp = account.stamper()
    if successful == True:
      balance = account.print_balance()
      record.append(f'{transaction}, {balance}')
      print('\n    ', balance)
    else:
      failure = '\n    Balance too low. Withdrawl aborted.'
      record.append(failure)
      print(failure)
  elif transaction == 'calculate interest':
    interest = account.interest_calculator()
    record.append(f'{transaction}, {interest}')
    print('\n    ', interest)
  transaction = input(
      '\n   enter the transaction (name or number): ').lower()
  for option in account.options:
    if transaction == option['id']:
      transaction = option['name']
date = datetime.now().date()
print(f'\n  Transactions for {date}')
for entry in record:
  print('\n    ', entry)
