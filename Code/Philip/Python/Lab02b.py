#Ask for total cost
cost_input = input('Enter item cost: $')
#Set cost as float
cost = float(cost_input)
#Ask for payment received
payment_input = input('Enter payment received: $')
#Set payment as float
payment = float(payment_input)
#Determine total change
change = payment - cost
#Format change to two decimal places
format_str_change = "{:.2f}".format(change)
#Set change back to float
format_change = float(format_str_change)
#Determine the whole dollars
Dollar = format_change // 1.00
#Determine remainder
Dollar_change = format_change % 1.00
#Determine the number of whole quarters
Quarter = Dollar_change // .25
#Determine remainder
Quarter_change = Dollar_change % .25
#Determine the number of whole dimes
Dime = Quarter_change // .10
#Determine remainder
Dime_change = Quarter_change % .10
#Determine the number of whole nickles
Nickle = Dime_change // .05
#Determine remainder
Nickle_change = Dime_change % .05
#Determine the number of pennies
Penny = Nickle_change // .01
#Display total and all change
print(f'Total change = ${format_change} \nDollars = {int(Dollar)} \nQuarters = {int(Quarter)} \nDimes = {int(Dime)} \nNickles = {int(Nickle)} \nPennies = {int(Penny)}')
