from utils.importer import importer
modules = [['responses', 'response'], ['generate', 'id'], ['timestamp', 'now']]
statements = []
id = ''
for module in modules:
  module = importer(module[0], module[1])
  statement = module.get_statement()
  statements.append(statement)
for statement in statements:
  exec(statement)


class account:
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
    newaccount = account(number, password, balance=0)
    message = f'Your account information: \n  account number: {number}\n  password: {password}'
    account.accounts.append(newaccount)
    return message

  def login():
    number = input('please enter your account number: ')
    password = input('please enter your password: ')
    for profile in account.accounts:
      if number == profile.number:
        if password == profile.password:
          login = True
          break
        else:
          login = False
          profile = 'invalid'
      else:
        login = False
        profile = 'invalid'
    return login, profile
