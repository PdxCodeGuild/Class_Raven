#tuple for later..
coins = [ ('half-dollar' , 50), ('quarter', 25),
 ('dime', 10), ('nickel', 5), ('pennies',1)]

print("Make Change Tool")
amount = input("what is the Dollar amount?\n>")
amount2 = float(amount)
#print(amount2)
amount2 = amount2 * 100
amount2 = int(amount2)
#print(amount2)
print(f"${amount} converts to;")
quarters = amount2 // 25
if quarters != 0:
    print(f"{quarters} Quarters")
remainder = amount2 % 25
dimes = remainder // 10
if dimes != 0:
    print(f"{dimes} Dimes")
remainder2 = remainder % 10
nickels = remainder2 // 5
if nickels != 0:
    print(f"{nickels} Nickels")
pennies = remainder2 % 5
if pennies != 0:
    print(f"{pennies} Pennies")

#print(f"${amount} converts to\n {quarters} Quarters\n
# {dimes} Dimes\n {nickels} Nickels\n {pennies} Pennies\n ")
#not very elegant but I was trying to do it quickly.