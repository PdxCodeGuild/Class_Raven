from random import randint
tickets = int(input('Enter the number of tickets: '))
#balance = int(input('Enter beginning balance: $'))

winner_list = []
for i in range(6):
    winner_list.append(randint(1,99))
print(winner_list)

def generate(tickets):
    attempts = 1
    winnings = []
    while attempts <= tickets:
        attempts = attempts + 1
        i = 0
        mylist = []
        while i < 6:
            mylist.append(randint(1,99))
            i = i + 1
            if mylist == winner_list:
                winnings.append(int(25000000))
            elif mylist[0] == winner_list[0]:
                winnings.append(int(4))
            elif mylist[1::] == winner_list[1::]:
                winnings.append(int(7))
            elif mylist[2::] == winner_list[2::]:
                winnings.append(int(100))
            elif mylist[3::] == winner_list[3:]:
                winnings.append(int(5000))
            elif mylist[4::] == winner_list[4::]:
                winnings.append(int(1000000))
        return winnings
    print(sum(winnings))


cost = tickets * 2
balance = sum(winnings) - cost
generate(tickets)

'''
tries = 1
result = 'no match'
winnings = 0
total_winnings = 0
while tries <= attempts:
    tries = tries + 1
    i = 0
    player_list=[]
    cost = attempts * 2
    total_winnings = total_winnings + winnings
    while i < 6:
        x = randint(1,99)
        player_list.append(int(x))
        i = i +1
        if player_list == winner_list:
            result = 'You win $25,000,000!'
            winnings = 25000000
            if winnings == 25000000:
                print(winnings)
        elif player_list[0] == winner_list[0]:
            result = 'You win $4'
            winnings = 4
            if winnings == 4:
                print(winnings)
        elif player_list[1::] == winner_list[1::]:
            result = 'You win $7'
            winnings = 7
            if winnings == 7:
                print(winnings)
        elif player_list[2::] == winner_list[2::]:
            result = 'You win $100'
            winnings = 100
            if winnings == 100:
                print(winnings)
        elif player_list[3::] == winner_list[3:]:
            result = 'You win $50,000'
            winnings = 50000
            if winnings == 50000:
                print(winnings)
        elif player_list[4::] == winner_list[4::]:
            result = 'You win $1000000'
            winnings = 1000000
            if winnings == 1000000:
                print(winnings)
    #print(player_list)
total_balance = balance + total_winnings
print (attempts)
print(f'Final balance ${total_balance}')'''
