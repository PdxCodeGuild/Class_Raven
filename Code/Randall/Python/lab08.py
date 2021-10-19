#the_picks

import random

def the_picks(the_picks):
    the_picks = [random.randint(1, 99) for x in range(0, 6)]
    balance = 0
    winnings = 0
    for i in range(100000):
        balance -= 2
        next6 = [random.randint(1, 99) for x in range(0, 6)]
        six = [x for x in range(0,6)]
        chk_res = dict(zip(six, the_picks))
        chk_comp = dict(zip(six, next6))
        same_num = 0   
        if chk_res[0] == chk_comp[0]:
            same_num += 1
        elif chk_res[1] == chk_comp[1]:
            same_num += 1
        elif chk_res[2] == chk_comp[2]:
            same_num += 1
        elif chk_res[3] == chk_comp[3]:
            same_num += 1    
        elif chk_res[4] == chk_comp[4]:
            same_num += 1
        elif chk_res[5] == chk_comp[5]:
            same_num += 1
        match_winnings = {0:0, 1:4, 2:7, 3:100, 4:50000, 5:1000000, 6:25000000}
        winnings += (match_winnings[same_num])
    print(f"ROI: {(winnings - abs(balance))/abs(balance) *100} %")
    print(f"Total Winnings: {winnings}")
    print(f"Total Expenses: {balance}")
    return (f'Ending Balance: {winnings - abs(balance)}')
print(the_picks(the_picks))