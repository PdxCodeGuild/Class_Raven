from data.models import ATM
from utils.importer import importer
modules = [['responses', 'response'], ['generate', 'id'], ['timestamp', 'now']]
statements = []
now = ''
for module in modules:
  module = importer(module[0], module[1])
  statement = module.get_statement()
  statements.append(statement)
for statement in statements:
  exec(statement)


class transaction:

    def balance(account):
      message = f'Your account has a balance of ${account.balance}.'
      stamp = now.standard()
      ATM.ATM.recap.append(f'{stamp} - checked balance')
      return message

    def deposit(account):
      amount = input('How much would you like to deposit?\n')
      try:
        amount = int(amount)
      except:
        message = 'please enter a valid whole number'
      else:
        account.balance += amount
        message = f'You deposited ${amount}\n Your new account balance is ${account.balance}.'
        stamp = now.standard()
        ATM.ATM.recap.append(f'{stamp} - deposited: ${amount}')
      return message

    def withdraw(account):
      amount = input('How much would you like to withdraw?\n')
      try:
        amount = int(amount)
      except:
        message = 'please enter a valid whole number'
      else:
        if amount < account.balance:
          account.balance -= amount
          message = f'You withdrew ${amount}\n Your new account balance is ${account.balance}.'
          stamp = now.standard()
          ATM.ATM.recap.append(f'{stamp} - withdrew: ${amount}')
        else:
          message = f'Your balance is less than your requested withdrawl.\n balance: ${account.balance}\n withdrawl: ${amount}'
      return message
