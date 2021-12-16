from utils.importer import importer
from data.models import ATM, transaction
modules = [['responses', 'response'], ['generate', 'id'], ['timestamp', 'now']]
statements = []
response = ''
for module in modules:
  module = importer(module[0], module[1])
  statement = module.get_statement()
  statements.append(statement)
for statement in statements:
  exec(statement)


def lab_ATM():
    validator = response.validate()
    selection = input(f'What would you like to do? \n {ATM.account.start}\n')
    selection = validator.selection(selection, ATM.account.start)
    while selection != 'done':
        if selection == 'create account':
            message = ATM.account.newaccount()
            print(message)
        if selection == 'sign-in':
            login = ATM.account.login()
            success = login[0]
            account = login[1]
            print(success)
            if success == True:
                transaction = input(
                    f'What would you like to do? \n {ATM.account.transactions}\n')
                transaction = validator.selection(
                    transaction, ATM.account.transactions)
                while transaction != 'done':
                    if transaction == 'check balance':
                        message = transaction.balance(account)
                        print(message)
                    elif transaction == 'deposit':
                        message = transaction.deposit(account)
                        print(message)
                    elif transaction == 'withdraw':
                        message = transaction.withdraw(account)
                        print(message)
                    transaction = input(
                        f'What would you like to do? \n {ATM.account.transactions}\n')
                    transaction = response.validate(
                        transaction, ATM.account.transactions)
        selection = input(
            f'What would you like to do? \n {ATM.account.start}\n')
        selection = validator.selection(selection, ATM.account.start)
    message = 'Thank you!\nHere is a summary of today\'s transactions: \n'
    for item in ATM.account.recap:
        item = f'   {item}\n'
        message += item
    print(message)
    return message


lab_ATM()
