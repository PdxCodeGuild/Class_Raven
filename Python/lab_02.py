# Make Change

# Have user enter dollar amount
user_input = input("Enter a dollar amount: ")

# Convert to float
user_input = float(user_input)

# Convert to pennies
user_input = int(user_input * 100)

# Compute for each change type

# Quarter
quarter = user_input // 25
user_input %= 25
# print(f"Quarters: {quarter}")
# print(f"remainder: {user_input}")

# Dimes
dime = user_input // 10
user_input %= 10
# print(f"Dimes: {dime}")
# print(f"remainder: {user_input}")

# Nickels
nickel = user_input // 5
user_input %= 5
# print(f"Nickels: {nickel}")
# print(f"remainder: {user_input}")

# Pennies
penny = user_input
# print(f"Pennies: {penny}")

# Print F statement summarizing change breakdown
print(f"The most efficient change breakdown is: {quarter} Quarters, {dime} Dimes, {nickel} Nickels, and {penny} Pennies.")