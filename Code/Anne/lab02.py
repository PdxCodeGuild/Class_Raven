#get input of how much money to break into coins


answer = input("how much money do you have?  ")
cash = float(answer)

tot_pennies = cash * 100
print(tot_pennies)
num_half_dollars = tot_pennies // 50
remain_aft_half_dollars = tot_pennies % 50

num_quarters = remain_aft_half_dollars // 25
remain_aft_quarters = remain_aft_half_dollars % 25

num_dimes = remain_aft_quarters // 10
remain_aft_dimes = remain_aft_quarters % 10

num_nickles = remain_aft_dimes // 5
pennies = remain_aft_dimes % 5

num_half_dollars = int(num_half_dollars)
num_quarters = int(num_quarters)
num_dimes = int(num_dimes)
num_nickles = int(num_nickles)
pennies = int(pennies)

print(f'Your change is {num_half_dollars} half dollars, {num_quarters} quarters, {num_dimes} dimes, {num_nickles} nickles, and {pennies} pennies. ')





