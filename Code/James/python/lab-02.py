coins = [
    ('half-dollar', 50),
    ('quarter', 25),
    ('dime', 10),
    ('nickel', 5),
    ('penny', 1)
]
dollar_amount = int(input("Enter a dollar amount: "))



quarter = dollar_amount // coins[1][1]
dime = dollar_amount // coins[2][1]
nickel = dollar_amount // coins[3][1]
penny = dollar_amount // coins[4][1]

total = dollar_amount // quarter

print(penny)