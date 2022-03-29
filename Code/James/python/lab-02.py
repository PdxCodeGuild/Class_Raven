coins = [
    ('half-dollar', 50),
    ('quarter', 25),
    ('dime', 10),
    ('nickel', 5),
    ('penny', 1)
]


dollar_amount = float(input("Enter a dollar amount: "))

dollar_amount = dollar_amount * 100


quarter = int(dollar_amount // coins[1][1])
total = dollar_amount - (quarter * coins[1][1])

dime = int(total // coins[2][1])
total = total - (dime * coins[2][1])

nickel = int(total // coins[3][1])

total = total - (nickel * coins[3][1])
penny = int(total // coins[4][1])



print(
    f'You have {quarter} quarters, {dime} dimes, {nickel} nickels, {penny} pennies.')
