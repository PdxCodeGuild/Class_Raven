from utils.importer import importer
from data.models import ATM


def lab_ATM():
    response = importer.response
    validator = response.validate()
    generateid = importer.generateid
    now = importer.now
    selection = input(f'What would you like to do? \n {ATM.start}\n')
    selection = validator.selection(selection, ATM.start)
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
                transaction = validator.selection(
                    transaction, ATM.transactions)
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
                    transaction = response.validate(
                        transaction, ATM.transactions)
        selection = input(f'What would you like to do? \n {ATM.start}\n')
        selection = validator.selection(selection, ATM.start)
    message = 'Thank you!\nHere is a summary of today\'s transactions: \n'
    for item in ATM.recap:
        item = f'   {item}\n'
        message += item
    print(message)
    return message


lab_ATM()
