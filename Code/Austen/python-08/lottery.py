def lab_lottery():
    ''
# * creates 6 random integers and outputs the ticket as a list
    def generate_ticket():
        counter = 1
        ticket = []
        while counter <= 6:
            import random
            number = random.randint(1, 99)
            ticket.append(number)
            counter += 1
        return ticket
# * compares the player's list to the winning list and outputs the prize money

    def compare_ticket(player):
        prizes = {0: 0, 1: 4, 2: 7, 3: 100, 4: 50000, 5: 1000000, 6: 2500000}
        matched = 0
        for number in player:
            i = 0
            if number == winning[i]:
                matched += 1
                i += 1
        prize = prizes[matched]
        return prize
# * creates the ticket that ALL tickets will be compared to
    winning = generate_ticket()
    counter = 1
    runs = input('How many tickets would you like to purchase?\n')
# * try except loop prevents python errors when user input is invalid
    while True:
        try:
            int(runs)
        except:
            break
        # * converts user input to integer
        runs = int(runs)
        balance = 0
# * charges the user for each ticket purchased then performs the core functionailty
        while counter <= runs:
            balance -= 2
            print(f'{counter} of {runs}')
            player = generate_ticket()
            balance += compare_ticket(player)
            counter += 1
        result = f'Your balance after {runs} tickets: ${balance}'
        print(result)
        return result
