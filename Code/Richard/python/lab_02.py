print("make change tool")
amount = input("what is the Dollar amount?\n>")
amount2 = float(amount)
print(amount2)
amount2 = amount2 * 100
amount2 = int(amount2)
print(amount2)
quarters = amount2 // 25
print(quarters)
remainder = amount2 % 25
dimes = remainder // 10
remainder2 = remainder % 10
nickels = remainder2 // 5
pennies = remainder2 % 5

print(f"${amount} converts to\n {quarters} Quarters\n {dimes} Dimes\n {nickels} Nickels\n {pennies} Pennies\n ")

#not very elegant but I was trying to do it quickly.  
# #I want to retool it to not show coins not used.