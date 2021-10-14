#getting users dollar amount
dollar_amount = input("Enter a dollar amount: ")
dollar_amount = float(dollar_amount)
#converting to an integer
x = True

#trying to do value exception error.
# while x:
#     dollar_amount = int(dollar_amount)
#     if isinstance(dollar_amount, int):
#         x = False
#     dollar_amount = input("Enter a dollar amount: ")


#setting all the variables for the coins
quarters = .25
dimes = .1
nickels = .05
pennies = .01

#converting the dollar amount into coins. I think just do floor division.
# 
convert_quarter = dollar_amount // quarters 
convert_quarter = int(convert_quarter)
remaining_balance = dollar_amount - (convert_quarter * quarters)

convert_dime = remaining_balance // dimes
convert_dime = int(convert_dime)
remaining_balance = remaining_balance - (convert_dime * dimes)

convert_nickel = remaining_balance // nickels
convert_nickel = int(convert_nickel)
remaining_balance = remaining_balance - (convert_nickel * nickels)

convert_pennies = remaining_balance // pennies
convert_pennies = int(convert_pennies)
remaining_balance = remaining_balance -(convert_pennies * pennies)

# print("convert quarter",convert_quarter)
# print("convert dime",convert_dime)
# print("convert nickels", convert_nickel)
# print("convert pennies", convert_pennies)
# print("remaining", remaining_balance)

print(f"{convert_quarter} quarters, {convert_dime} dimes, {convert_nickel} nickels, {convert_pennies} pennies.")


