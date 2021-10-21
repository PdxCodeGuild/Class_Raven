amount = input("Enter a dollar amount: ").replace(".","")
amount = int(amount)

quarter = amount // 25
quarters = quarter * 25

dime = (amount - quarters) // 10
dimes = dime * 10

nickel = (amount - dimes - quarters) // 5
nickels = nickel * 5

pennies = (amount - dimes - quarters - nickels)

print(f"{quarter} quarters, {dime} dimes, {nickel} nickels, {pennies} pennies.")