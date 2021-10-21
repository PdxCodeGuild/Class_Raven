#Ask user for amount of money they have
change_input = input('Enter your money: ')
#Convert the money into a floating point
change = float(change_input)
#Determine the whole dollars they have
Dollar = change // 1.00
#Determine remainder
Dollar_change = change % 1.00
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
#Display all change
print(f'Dollars = {int(Dollar)}, Quarters = {int(Quarter)}, Dimes = {int(Dime)}, Nickles = {int(Nickle)}, Pennies = {int(Penny)}')
