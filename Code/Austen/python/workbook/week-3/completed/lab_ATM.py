class importer:
  def system():
    import sys
    default = 'X:\\pdx-code-guild\\'
    root = default
    utilspath = f'{root}Class_Raven\\Code\\Austen\\python\\'
    sys.path.append(utilspath)


def lab_ATM():
  importer.system()
  from utilities.responses import response
  from utilities.generate import id
  from utilities.timestamp import now

  class ATM:
    start = ['create account', 'sign-in', 'done']
    transactions = ['check balance', 'deposit', 'withdraw', 'done']
    accounts = []
    recap = []

    def __init__(account, number, password, balance):
      account.number = number
      account.password = password
      account.balance = balance
      account.interest = 0.1

    def newaccount():
      number = id.AN4()
      password = input('create a password: ')
      account = ATM(number, password, balance=0)
      message = f'Your account information: \n  account number: {number}\n  password: {password}'
      ATM.accounts.append(account)
      return message

    def login():
      number = input('please enter your account number: ')
      password = input('please enter your password: ')
      for account in ATM.accounts:
        if number == account.number:
          if password == account.password:
            login = True
            break
          else:
            login = False
            account = 'invalid'
        else:
          login = False
          account = 'invalid'
      return login, account

    class transaction:
      def balance(account):
        message = f'Your account has a balance of ${account.balance}.'
        stamp = now.standard()
        ATM.recap.append(f'{stamp} - checked balance')
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
          ATM.recap.append(f'{stamp} - deposited: ${amount}')
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
            ATM.recap.append(f'{stamp} - withdrew: ${amount}')
          else:
            message = f'Your balance is less than your requested withdrawl.\n balance: ${account.balance}\n withdrawl: ${amount}'
        return message

  selection = input(f'What would you like to do? \n {ATM.start}\n')
  selection = response.validate(selection, ATM.start)
  while selection != 'done':
    if selection == 'create account':
      message = ATM.newaccount()
      print(message)
    if selection == 'sign-in':
      login = ATM.login()
      success = login[0]
      account = login[1]
      print(success)
      if success == True:
          transaction = input(
              f'What would you like to do? \n {ATM.transactions}\n')
          transaction = response.validate(transaction, ATM.transactions)
          while transaction != 'done':
            if transaction == 'check balance':
              message = account.transaction.balance(account)
              print(message)
            elif transaction == 'deposit':
              message = account.transaction.deposit(account)
              print(message)
            elif transaction == 'withdraw':
              message = account.transaction.withdraw(account)
              print(message)
            transaction = input(
                f'What would you like to do? \n {ATM.transactions}\n')
            transaction = response.validate(transaction, ATM.transactions)
    selection = input(f'What would you like to do? \n {ATM.start}\n')
    selection = response.validate(selection, ATM.start)
  message = 'Thank you!\nHere is a summary of today\'s transactions: \n'
  for item in ATM.recap:
    item = f'   {item}\n'
    message += item
  print(message)
  return message


lab_ATM()
