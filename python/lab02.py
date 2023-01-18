coins = [
    ('quarter', 25),
    ('dime', 10),
    ('nickel', 5),
    ('penny', 1)
]
results = []
while True:
    try:
        user_input = int((float(input("Enter a dollar amount: "))) * 100)
    except:
        print ("That's not a valid number. Try again.")
    else:
        break


for x in coins:
    (coin, value) = x
    if user_input != 0:
       calc = user_input // value
       results.append(calc)
       user_input = user_input - (value * calc)

print(f'You have {results[0]} quarters, {results[1]} dimes, {results[2]} nickels, {results[3]} pennies.')

